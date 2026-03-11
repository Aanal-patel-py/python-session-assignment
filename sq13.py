from collections import Counter, defaultdict,deque,namedtuple
# 1-------------------------------------------------
words = []
with open("collections_data.txt") as f:
    for line in f:
        words.extend(line.split())
word_counts=Counter(words)
# print(word_counts)
print(word_counts.most_common(10))
# 2-------------------------------------------------
d=defaultdict(list)
for x in words:
    d[x[0]].append(x)

print(d)
# 3------------------------------------------------
buffer=deque(maxlen=2)
with open("collections_data.txt") as f:
    for line in f:
        buffer.append(line.strip())

for recent_line in buffer:
    print(recent_line)

# 4-----------------------------------------------
LogEntry = namedtuple('LogEntry', ['timestamp', 'level', 'message'])

entries = []

with open("collections_data.txt") as f:
    for line in f:
        parts = line.strip().split(maxsplit=3) 
        if len(parts) >= 3:  
            entry = LogEntry(timestamp=parts[0] + " " + parts[1],
                             level=parts[2],
                             message=parts[3] if len(parts) == 4 else "")
            entries.append(entry)
print(entries[0].timestamp, entries[0].level, entries[0].message)