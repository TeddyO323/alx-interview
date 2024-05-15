#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables for tracking metrics
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def parse_line(line):
    global total_file_size, status_counts, line_count
    line_count += 1

    # Use regular expression to extract data from the line
    match = re.match(r'^.*\[(.*)\] "GET .*" (\d+) (\d+)$', line)
    if match:
        date, status_code, file_size = match.groups()
        total_file_size += int(file_size)
        status_counts[int(status_code)] += 1

def print_stats():
    global total_file_size, status_counts
    print(f'Total file size: File size: {total_file_size}')
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f'{code}: {count}')

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parse_line(line)
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    signal_handler(signal.SIGINT, None)
