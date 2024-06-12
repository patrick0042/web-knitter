#!/usr/bin/python3

import os
from wrapper import wrap_file
from datetime import datetime as dt

index = []
posting_html = []
menu = ''

fh = open('helper/skel_header.html', 'r')
for line_head in fh:
    index.append(line_head)
fh.close()

index.append('<h3>Platzhalter</h3>')

fh = open('helper/about.md', 'r')
for about_item in fh:
    index.append(about_item)
fh.close()

dir_path = r'content/'
count = 0
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
last_file = count
count = 0

for root, dirs, files in os.walk("content/"):
    for file in sorted(files):
        count += 1
        posting = os.path.join(root, file)
        base = file[4:len(file)-3]
        wrap_file(posting, base)
        mdate = os.path.getmtime(posting)
        post_date = dt.fromtimestamp(mdate).strftime("%Y-%m-%d")
        link = ('<a href="'+base+'.html">'+base+'</a>')
        if count < last_file:
            menu = menu+link+' ('+post_date+')'+'&nbsp;&nbsp;\n'
        else:
            menu = menu+link+' ('+post_date+')'+'\n'
    posting_html = []

index.append('<br>')
index.append('<h3>Angebote zur Interaktion</h3>')
index.append('<p>'+menu+'</p>')

index.append('<br>')
index.append('<h3>Micro Blog</h3>')

count = 0
fh = open('helper/changes.md', 'r')
index.append('<p><ul>')
for changes_item in fh:
    count += 1
    if count <= 3:
        index.append('<li>'+changes_item+'</li>')
    else:
        break
fh.close()
index.append('</ul></p>')

fh = open('helper/skel_footer.html', 'r')
for line_foot in fh:
    index.append(line_foot)
fh.close()

index_fh = open('upload/index.html', 'w')
for index_line in index:
    index_fh.write(index_line)
index_fh.close()
