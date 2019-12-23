#! /usr/bin/python3

from collections import defaultdict as ddict
from re import finditer, sub
from os import listdir, path

from subprocess import (
    DEVNULL,
    check_call   as cc,
    check_output as co,
)


ellipsis = '\u2026'
hl_cmd = 'pandoc -t html5 --highlight-style kate'
my_full_path = path.dirname (path.abspath(__file__))
my_dir_name  = path.basename(my_full_path)


def get_fpath(inclusion_statement):
    start = inclusion_statement.find('<+[') + 3
    end = inclusion_statement.find('|')
    if end == -1:
        end = inclusion_statement.find(']+>')
    return inclusion_statement[start:end]

def get_slice_str(inclusion_statement):
    start = inclusion_statement.find('|') + 1
    if start == 0:
        return ''
    end = inclusion_statement.find(']+>')
    return inclusion_statement[start:end]

def extract_lang(slice_str):
    start_lang = 1 # we already know it starts with '#'
    end_lang = slice_str.find(',')
    if end_lang == -1:
        end_lang = None
    hl_lang = slice_str[start_lang:end_lang]

    slice_str = slice_str.replace(F'#{hl_lang}', '')
    if slice_str.startswith(','):
        slice_str = slice_str[1:]
    return hl_lang, slice_str

def highlight_lines(lang, lines):
    code_start = '```{.default .lineAnchors}\n'
    code_end = '\n```'
    if lang:
        code_start = code_start.replace('.default', F'.{lang}')

    jl = '\n'.join(lines)
    _input = F'{code_start}{jl}{code_end}'.encode()
    # Ignoring errors because we'll handle duplicate anchors manually.
    return co(hl_cmd.split(), input=_input, stderr=DEVNULL).decode()

def get_slice(s):
    if not s:
        return None, None
    if ':' in s:
        start, end = [int(s) if s else None for s in s.split(':')]
    else:
        start = int(s)
        end = start + 1
        if start < 0:
            end = None
    return start, end

def get_table_rows(numbered_lines, lang):
    table_rows = list()
    for num, line in numbered_lines:
        tr_class = ''
        if len(table_rows) % 2 != 0:
            tr_class = ' class="even"'

        line_number = F'{num + 1}</a>'
        if num == -1: # it's an ellipsis
            line_number = ''

        # Transfer the anchor to line_number
        tag_end = line.find(">")+1
        line_number = F'<td>{line[:tag_end]}{line_number}</td>'
        if num != -1: # if it's not an ellipsis
            line = line[tag_end:-4] # -4 to account for '</a>'

        lang_class = ''
        if lang:
            lang_class = F'class="{lang}"'
        table_rows.append((
            F'<tr{tr_class}>'
            F'{line_number}'
            F'<td>'
            F'<pre  {lang_class}>'
            F'<code {lang_class}>{line}'
            '</code></pre></td></tr>'
        ))
    return table_rows


report = ''
chapters = [chapter for chapter in listdir(my_full_path) if chapter.endswith('.md') and chapter.split('_')[0].isnumeric()]
chapters.sort(key = lambda c: int(c.split('_')[0]))
for chapter in chapters:
    with open(chapter) as f:
        report += f.read()

fpaths_flines, fpaths_slices = ddict(list), ddict(list)
for m in finditer('<\+\[(.+)\]\+>', report):
    inclusion_statement = m.group(0)
    fpath = get_fpath(inclusion_statement)
    slice_str = get_slice_str(inclusion_statement)
    fpaths_slices[fpath].append(slice_str)
    if fpath in fpaths_flines:
        continue
    with open(F'{my_full_path}/{fpath}') as f:
        fpaths_flines[fpath] = f.read().splitlines()

cb_num = 1
replacements, fpaths__hl_lines = ddict(str), ddict(str)
for fpath, slices_list in fpaths_slices.items():
    for slice_str in slices_list:
        flines = fpaths_flines[fpath]
        replacement_pattern = F'<+[{fpath}|{slice_str}]+>'
        if not slice_str:
            replacement_pattern = F'<+[{fpath}]+>'
            replacements[replacement_pattern] = '\n'.join(flines)
            continue

        make_table = False
        hl_lang = ''
        if slice_str.startswith('#'):
            make_table = True
            hl_lang, slice_str = extract_lang(slice_str)

            hl_lines = fpaths__hl_lines.get(fpath, None)
            if hl_lines is None:
                hl_lines = highlight_lines(hl_lang, flines)
                fpaths__hl_lines[fpath] = hl_lines

            hl_lines = sub(
                '(<a class="sourceLine" id="c)b1(-\d{1,3})(" href="#c)b1(-\d{1,3}")',
                F'\\g<1>t{cb_num}\\g<2>\\g<3>t{cb_num}\\g<4>',
                hl_lines
            )
            cb_num += 1

            flines = [
                line[ line.find('<a') : line.find('</a>')+4 ]
                for line in hl_lines.splitlines()
            ]

        lines_to_include = list()
        slices = slice_str.split(',')
        for i, s in enumerate(slices):
            start, end = get_slice(s)
            if i == 0 and start is not None:
                lines_to_include.append((-1, ellipsis))

            lines = [l.rstrip() for l in flines[start:end]]
            for line_index, line in enumerate(lines):
                lines_to_include.append(((start or 0) + line_index, line))
            lines_to_include.append((-1, ellipsis))

            if i == len(slices)-1 and end is None:
                lines_to_include.pop(-1)

        if make_table:
            file_slice = '\n'.join(get_table_rows(lines_to_include, hl_lang))
            file_slice = (
                F'<div class="code">\n'
                '<table><tbody>\n'
                F'{file_slice}'
                '</tbody></table>\n'
                '</div>'
            )
        else:
            file_slice = '\n'.join([v for i, v in lines_to_include])

        replacements[replacement_pattern] = file_slice


for pattern, replacement in replacements.items():
    report = report.replace(pattern, replacement)

report_file = F'{my_full_path}/{my_dir_name}.md'
with open(report_file, 'w') as f:
    f.write(report)

output =  'pandoc -f markdown -t html5+yaml_metadata_block ' \
       + F'-s --toc --toc-depth 3 --highlight-style kate --template={my_full_path}/template.html ' \
       + F'-o {my_full_path}/{my_dir_name}.html {report_file} {my_full_path}/metadata.yaml'
cc(output.split())

output = 'weasyprint -m screen -p {0}/{1}.html {0}/{1}.pdf'.format(my_full_path, my_dir_name)
cc(output.split())

