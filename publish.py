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

def number_lines(lines):
    numbered_lines = list()
    for i, l in enumerate(lines):
        line_number = F'<span class="ln">{i + 1}</span>'
        line_number = ' ' * (30 - len(line_number)) + line_number
        numbered_lines.append(F'{line_number} {l}')
    return numbered_lines

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

    with open('{}/{}'.format(my_full_path, fpath)) as f:
        flines = f.readlines()

    if slices:
        ellipsis = '...\n'
        prepend  = ''
        append   = ''
        include  = list()

        make_table = '#' in slices

        slices = slices.replace('#', '' )
        slices = slices.replace(',', ' ')
        slices = slices.split()

        if make_table:
            flines   = number_lines(flines)
            ellipsis = ' ' * 31 + ellipsis

        for i, s in enumerate(slices):
            start, end = get_slice(s)
            if i == 0 and start is not None:
                prepend = ellipsis
            include.append(''.join(flines[start:end]))
            if i == len(slices) - 1 and end is not None:
                append = ellipsis

        include = prepend + ellipsis.join(include) + append

        if make_table:
            table_delimiter = '-' * 30 + ' ---\n'
            include = F'<div class="code">\n\n{table_delimiter}{include}{table_delimiter}\n</div>'

    else: # if not slices, include the entire file
        include = ''.join(flines)

    report = sub(inclusion_pattern, repr(include.strip())[1:-1], report, count=1)

report_file = F'{my_full_path}/{my_dir_name}.md'
with open(report_file, 'w') as f:
    f.write(report)

output =  'pandoc -f markdown -t html5+smart+yaml_metadata_block ' \
       + F'-s --toc --toc-depth 3 --highlight-style kate --template={my_full_path}/template.html ' \
       + F'-o {my_full_path}/{my_dir_name}.html {report_file} {my_full_path}/metadata.yaml'
cc(output.split(' '))

output = 'weasyprint -m screen -p {0}/{1}.html {0}/{1}.pdf'.format(my_full_path, my_dir_name)
cc(output.split(' '))

