#!/usr/bin/python3
"""
Log parsing
"""

import sys
import signal
import re


# Initialize variables
filesize, count = 0, 0
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {k: 0 for k in codes}


# Define a signal handler for keyboard interruption
def signal_handler(sig, frame):
    print_stats(stats, filesize)
    sys.exit(0)


# Function to print statistics
def print_stats(stats: dict, file_size: int) -> None:
    print("File size: {:d}".format(file_size))
    for k in sorted(stats.keys()):
        if stats[k] > 0:
            print("{}: {}".format(k, stats[k]))


# Attach the signal handler to SIGINT
signal.signal(signal.SIGINT, signal_handler)


# Regular expression for log entry parsing
log_pattern = re.compile(
    r'^(?P<ip>[\d\.]+) - \['
    r'(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" '
    r'(?P<status>\d{3}) (?P<size>\d+)$'
)


# Read from stdin line by line
try:
    for line in sys.stdin:
        count += 1
        match = log_pattern.match(line)

        if match:
            status_code = match.group('status')
            file_size = int(match.group('size'))

            if status_code in stats:
                stats[status_code] += 1

            filesize += file_size

        # Print statistics every 10 lines
        if count % 10 == 0:
            print_stats(stats, filesize)

    print_stats(stats, filesize)


except KeyboardInterrupt:
    print_stats(stats, filesize)
    raise
