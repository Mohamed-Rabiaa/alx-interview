#!/usr/bin/python3
"""
"""

import sys
import signal
import re


lst = []
file_size = 0
status_codes_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                      "403": 0, "404": 0, "405": 0, "500": 0}

pattern = (
    r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
    r'"GET /projects/260 HTTP/1.1" \d{3} \d+$'
)


def signal_handler(sig, frame):
    """
    This function handles the SIGINT signal (Ctrl+C)
    """
    print_stats()
    sys.exit(0)


def log_parsing():
    """
    This function parses logs and prints statistics every 10 lines
    """
    global lst
    count = 0
    for line in sys.stdin:
        if re.match(pattern, line):
            lst.append(line.strip())
            count += 1
            if count == 10:
                print_stats()
                lst = []
                count = 0


def print_stats():
    """
    This function prints the statistics
    """
    global file_size, lst, status_codes_count
    for text in lst:
        file_size += int(text.split()[8])
        key = text.split()[7]
        if key in status_codes_count.keys():
            status_codes_count[key] += 1
    print("File size: {}".format(file_size))
    for k, v in status_codes_count.items():
        if v > 0:
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    log_parsing()
