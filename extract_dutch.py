import re

# Path to the large JS file
target_file = 'pa-24.js'
output_file = 'long_user_facing_strings.txt'

# Minimum length for a string to be considered 'long'
MIN_LENGTH = 30

# Regex to match string literals (single or double quotes, not escaped)
string_literal_re = re.compile(r'(?:"([^"\\]*(?:\\.[^"\\]*)*)"|\'([^\'\\]*(?:\\.[^\'\\]*)*)\')')

# Heuristic: likely user-facing if contains punctuation, spaces, or HTML tags
user_facing_re = re.compile(r'[\.\,\!\?\:\;\(\)\[\]\{\}\<\>\s]')

# Regex to filter out technical dot-separated identifiers (like namespaces, class paths, etc.)
technical_identifier_re = re.compile(r'^[a-zA-Z0-9_.]+\.[a-zA-Z0-9_.]+$')

with open(target_file, encoding='utf-8', errors='ignore') as f, open(output_file, 'w', encoding='utf-8') as out:
    for lineno, line in enumerate(f, 1):
        for match in string_literal_re.finditer(line):
            s = match.group(1) or match.group(2)
            if (
                s
                and len(s) >= MIN_LENGTH
                and user_facing_re.search(s)
                and not technical_identifier_re.fullmatch(s.strip())
            ):
                out.write(f"Line {lineno}: {s}\n")
