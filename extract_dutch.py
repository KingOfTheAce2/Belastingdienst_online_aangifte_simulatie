import re

# Path to the large JS file
target_file = 'pa-24.js'

# Minimum length for a string to be considered 'long'
MIN_LENGTH = 40

# Regex to match string literals (single or double quotes, not escaped)
string_literal_re = re.compile(r'(?:"([^"\\]*(?:\\.[^"\\]*)*)"|\'([^\'\\]*(?:\\.[^\'\\]*)*)\')')

# Heuristic: likely user-facing if contains punctuation, spaces, or HTML tags
user_facing_re = re.compile(r'[\.\,\!\?\:\;\(\)\[\]\{\}\<\>\s]')

with open(target_file, encoding='utf-8', errors='ignore') as f:
    for lineno, line in enumerate(f, 1):
        for match in string_literal_re.finditer(line):
            s = match.group(1) or match.group(2)
            if s and len(s) >= MIN_LENGTH and user_facing_re.search(s):
                # Filter out likely technical/code strings (no spaces, no punctuation)
                print(f"Line {lineno}: {s}") 
