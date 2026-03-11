def read_logs(filename):
     with open(filename) as f:
        for line in f:
            yield line.strip()
            # print(line)

def parse_logs(lines):
    for line in lines:         
        parts = line.split() 
        if len(parts)<3:
            continue   
        yield {
            "timestamp": parts[0] + " " + parts[1],
            "level": parts[2],
            "message": " ".join(parts[3:])
        }

def filter_errors(log):
    for x in log:
        if x["level"]=="ERROR":
            yield x
        else:
            continue

def timestamps(log):
    for y in log:
        yield y['timestamp']
# for line in read_logs("logfile.txt"):
#     print(line)

lines=read_logs("logfile.txt")
parsed_logs=parse_logs(lines)
errors=filter_errors(parsed_logs)
extracted_timestamp=timestamps(errors)

for t in extracted_timestamp:
    print(t)
