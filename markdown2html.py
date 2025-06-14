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
                html_file.write(f"<h{level}>{apply_formatting(content)}</h{level}>\n")
                continue

            # Lists
            if stripped.startswith('- '):
                if not in_list:
                    in_list = True
                    html_file.write("<ul>\n")
                html_file.write(f"<li>{apply_formatting(stripped[2:])}</li>\n")
                continue
            elif in_list:
                in_list = False
                html_file.write("</ul>\n")

            # Blank lines (paragraph close)
            if stripped == "":
                if not first_line:
                    html_file.write('\n</p>\n')
                    first_line = True
                continue

            # Paragraph text
            if first_line:
                html_file.write('<p>\n')
                html_file.write(apply_formatting(stripped))
                first_line = False
            else:
                html_file.write('\n<br />\n')
                html_file.write(apply_formatting(stripped))

        if in_list:
           html_file.write("</ul>\n")
        if not first_line:
           html_file.write('\n</p>\n')


def apply_formatting(content):
    # Apply bold formatting first
    bold_match = re.search(r'(.*)\*\*(.+?)\*\*(.*)', content)
    if bold_match:
        content = f"{bold_match.group(1)}<b>{bold_match.group(2)}</b>{bold_match.group(3)}"

    # Apply italic formatting next
    italic_match = re.search(r'(.*)__(.+?)__(.*)', content)
    if italic_match:
        content = f"{italic_match.group(1)}<em>{italic_match.group(2)}</em>{italic_match.group(3)}"

    return content

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
