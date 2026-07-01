from collections import defaultdict

text = "cloud computing is powerful cloud computing is useful"

# Map Phase
mapped = [(word, 1) for word in text.split()]

# Reduce Phase
reduced = defaultdict(int)

for word, count in mapped:
    reduced[word] += count

print("Word Count:")

for word, count in reduced.items():
    print(word, ":", count)
