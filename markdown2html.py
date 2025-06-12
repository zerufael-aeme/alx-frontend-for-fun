#!/usr/bin/python3
"""
markdown2html.py - Script to check Markdown input file and output HTML filename.
"""
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
