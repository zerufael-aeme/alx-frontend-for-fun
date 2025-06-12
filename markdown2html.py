#!/usr/bin/python3
import sys
import os

# Check for the correct number of arguments (2 file names = 3 argv items total)
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Check if the input Markdown file exists
if not os.path.exists(sys.argv[1]):
    print(f"Missing {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)

# All good
sys.exit(0)
