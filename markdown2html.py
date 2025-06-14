#!/usr/bin/python3
"""
markdown2html.py - Script to check Markdown input file and output HTML filename.
"""
import sys
import os
import re

def convert_markdown_to_html():
    with open (sys.argv[1], 'r') as md_file, open(sys.argv[2], 'w') as html_file:
        in_list = False
        first_line = True

        for line in md_file:
            stripped = line.strip()

            heading_match = re.match(r'^(#{1,6}) (.+)', stripped)

            if heading_match:
                level = len(heading_match.group(1))
                content = heading_match.group(2)
                html_file.write(f"<h{level}>{content}</h{level}>")

            if (stripped.startswith('* ')):
                if not in_list:
                    in_list = True
                    html_file.write(f"<ol>\n")
                item = stripped[2:]
                html_file.write(f"<li>{item}</li>\n")
            else:
                in_list = False
                html_file.write(f"</ol>\n")

            if not (stripped.startswith('* ', '- ', '#')):
                if first_line:
                    html_file.write('<p>\n')
                    html_file.write(stripped)
                    first_line = False
                elif stripped= == "" and first_line == False:
                    first_line == True
                    html_file.write('</p>\n')
                else:
                    html_file.write(stripped)





        html_file.write(f"</ol>\n")



def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html()

    sys.exit(0)

if __name__ == "__main__":
    main()
