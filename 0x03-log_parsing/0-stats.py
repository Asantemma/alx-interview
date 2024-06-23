#!/usr/bin/python3

import sys


def print_stats(status_counts, total_size):
    """
    Print the total file size and the number
    of occurrences of each status code.
    Args:
        status_counts: Dictionary of status codes.
        total_size: Total file size.
    Returns:
        Nothing
    """

    print("File size: {}".format(total_size))
    for key, val in sorted(status_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize metrics
total_size = 0
status_code = 0
line_count = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # splits the line into parts
        parsed_line = parsed_line[::-1]  # reverses the parts for easier access

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_size += int(parsed_line[0])
                status_code = parsed_line[1]

                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count == 10:
                print_stats(status_counts, total_size)
                line_count = 0

finally:
    print_stats(status_counts, total_size)
