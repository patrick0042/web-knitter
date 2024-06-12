#!/usr/bin/python3

def wrap_file(posting, base):
    posting_html = []

    header_fh = open('helper/skel_header.html', 'r')
    for header_line in header_fh:
        posting_html.append(header_line)
    header_fh.close()

    posting_html.append('<a href="index.html">Home</a>')
    posting_html.append('<br>')
    posting_html.append('<h4>'+base+'</h4>')

    posting_fh = open(posting, 'r')
    for posting_line in posting_fh:
        posting_html.append(posting_line)
    posting_fh.close()

    footer_fh = open('helper/skel_footer.html', 'r')
    for footer_line in footer_fh:
        posting_html.append(footer_line)
    footer_fh.close()

    html_file = base + '.html'

    html_fh = open('upload/' + html_file, 'w')
    for html_line in posting_html:
        html_fh.write(html_line)
    html_fh.close()
