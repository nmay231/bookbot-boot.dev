from collections import Counter
from textwrap import dedent

file_path = "books/frankenstein.txt"
with open(file_path) as f:
    contents = f.read()
    word_count = len(contents.split())

    print(dedent(f"""
          --- Begin report of {file_path} ---
          {word_count} words found in the document\n"""))

    counts = Counter(contents.lower())
    for char, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times")
