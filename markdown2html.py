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

            # Headings
            heading_match = re.match(r'^(#{1,6}) (.+)', stripped)
            if heading_match:
                if not first_line:
                    html_file.write('\n</p>\n')
                    first_line = True
                level = len(heading_match.group(1))
                content = heading_match.group(2)
                style_match = re.match(r'(.+)\*\*(.+?)\*\*(.+)', content)
                if style_match:
                    html_file.write(f'<h{level}>{style_match.group(1)} <b>{style_match.group(2)}</b> {style_match.group(3)}</h{level}>\n')
                else:
                    html_file.write(f"<h{level}>{content}</h{level}>\n")
                
                continue

            # Lists
            if stripped.startswith('* '):
                if not in_list:
                    in_list = True
                    html_file.write("<ol>\n")
                html_file.write(f"<li>{stripped[2:]}</li>\n")
                continue
            elif in_list:
                in_list = False
                html_file.write("</ol>\n")

            # Blank lines (paragraph close)
            if stripped == "":
                if not first_line:
                    html_file.write('\n</p>\n')
                    first_line = True
                continue

            # Paragraph text
            if first_line:
                html_file.write('<p>\n')
                html_file.write(stripped)
                first_line = False
            else:
                html_file.write('\n<br />\n')
                html_file.write(stripped)

        if in_list:
           html_file.write("</ol>\n")
        if not first_line:
           html_file.write('\n</p>\n')




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
