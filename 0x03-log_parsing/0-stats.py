#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_codes_count = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


# Define a signal handler for SIGINT
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Function to print statistics
def print_statistics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        if status_codes_count[status_code] > 0:
            print(f"{status_code}: {status_codes_count[status_code]}")


# Attach the signal handler to SIGINT
signal.signal(signal.SIGINT, signal_handler)


# Regex pattern to match the log line format
log_pattern = re.compile(
    r'^(?P<ip>[\d\.]+) - \['
    r'(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" '
    r'(?P<status>\d{3}) (?P<size>\d+)$'
)

# Read from stdin line by line
for line in sys.stdin:
    line_count += 1
    match = log_pattern.match(line)

    if match:
        # Extract the file size and status code
        file_size = int(match.group('size'))
        status_code = int(match.group('status'))

        # Update totals
        total_file_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics()

# Final print in case the program exits without a keyboard interrupt
print_statistics()
