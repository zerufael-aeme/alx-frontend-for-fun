#!/usr/bin/python3
"""
markdown2html.py - Script to check Markdown input file and output HTML filename.
"""
import sys
import os
import re

def main():
    with open (sys.argv[1], 'r') as md_file, open(sys.argv[2], 'w') as html_file:
        for line in md_file:
            stripped = line.strip()

            heading_match = re.match(r'^(#{1,6}) (.+)', stripped)

            if heading_match:
                level = len(heading_match.group(1))
                content = heading_match.group(2)
                html_file.write(f"<h{level}>{content}</h{level}>") 

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
