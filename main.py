from collections import Counter

with open("books/frankenstein.txt") as f:
    counts = Counter(f.read().lower())
    print(counts)
