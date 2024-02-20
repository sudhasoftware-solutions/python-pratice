import re

text = "The quick red fox"
pattern = r"red"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")