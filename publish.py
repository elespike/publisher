#! /usr/bin/python3

from re import finditer, sub
from os import listdir , path
from subprocess import check_call as cc


my_full_path = path.dirname (path.abspath(__file__))
my_dir_name  = path.basename(my_full_path)


def get_slice(s):
    if ':' in s:
        start, end = [int(s) if s else None for s in s.split(':')]
    else:
        start = int(s)
        end = start + 1
        if start < 0:
            end = None
    return start, end

def get_table_rows(numbered_lines):
    table_rows = list()
    for i, l in numbered_lines:
        tr_class = ''
        if len(table_rows) % 2 != 0:
            tr_class = ' class="even"'

        line_number = F'<td><pre>{i + 1}</pre></td>'
        if i == -1: # it's an ellipsis
            line_number = '<td></td>'

        table_rows.append(F'<tr{tr_class}>{line_number}<td><pre>{l}</pre></td></tr>')
    return table_rows

report = ''
chapters = [chapter for chapter in listdir(my_full_path) if chapter.endswith('.md') and chapter.split('_')[0].isnumeric()]
chapters.sort(key = lambda c: int(c.split('_')[0]))
for chapter in chapters:
    with open(chapter) as f:
        report += f.read()

inclusion_pattern = '<\+\[(.+)\]\+>'
for m in finditer(inclusion_pattern, report):
    slices = ''
    try:
        fpath, slices = m.group(1).split('|')
    except ValueError:
        fpath = m.group(1)

    with open(F'{my_full_path}/{fpath}') as f:
        flines = f.readlines()

    if slices:
        ellipsis = '\u2026'
        prepend  = ''
        append   = ''
        include  = list()

        make_table = '#' in slices

        slices = slices.replace('#', '' )
        slices = slices.replace(',', ' ')
        slices = slices.split()

        for i, s in enumerate(slices):
            start, end = get_slice(s)
            if i == 0 and start is not None:
                include.append((-1, ellipsis))

            lines = [l.rstrip() for l in flines[start:end]]
            for line_index, line in enumerate(lines):
                include.append(((start or 0) + line_index, line))
            include.append((-1, ellipsis))

            if i == len(slices) - 1 and end is None and include:
                include.pop(-1)

        if make_table:
            include = '\n'.join(get_table_rows(include))
            include = F'<div class="code">\n<table><tbody>\n{include}</tbody></table>\n</div>'
        else:
            include = '\n'.join([v for i, v in include])

    else: # if not slices, include the entire file
        include = ''.join(flines)

    report = sub(inclusion_pattern, include.strip(), report, count=1)


report_file = F'{my_full_path}/{my_dir_name}.md'
with open(report_file, 'w') as f:
    f.write(report)

output =  'pandoc -f markdown -t html5+yaml_metadata_block ' \
       + F'-s --toc --toc-depth 3 --highlight-style kate --template={my_full_path}/template.html ' \
       + F'-o {my_full_path}/{my_dir_name}.html {report_file} {my_full_path}/metadata.yaml'
cc(output.split(' '))

output = 'weasyprint -m screen -p {0}/{1}.html {0}/{1}.pdf'.format(my_full_path, my_dir_name)
cc(output.split(' '))

