#!/usr/bin/python3
import sys
import signal

def compute_metrics(log_lines):
    """
    Computes the metrics from the given log lines.

    Args:
        log_lines (list): A list of log lines to process.

    Returns:
        int: The total file size.
        dict: A dictionary containing status code counts.
    """
    total_size = 0
    status_code_counts = {}

    for line in log_lines:
        try:
            parts = line.split()
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

        except (ValueError, IndexError):
            pass  # Ignore lines with incorrect format

    return total_size, status_code_counts

def print_metrics(total_size, status_code_counts):
    """
    Prints the computed metrics.

    Args:
        total_size (int): The total file size.
        status_code_counts (dict): A dictionary containing status code counts.

    Returns:
        None
    """
    print("Total file size: File size:", total_size)
    for status_code in sorted(status_code_counts.keys()):
        print(status_code + ":", status_code_counts[status_code])

def handle_interrupt(signal, frame):
    """
    Handles interrupt (CTRL+C) by printing metrics and exiting.

    Args:
        signal: The signal received.
        frame: The current stack frame.

    Returns:
        None
    """
    print_metrics(total_size, status_code_counts)
    sys.exit(0)

total_size = 0
status_code_counts = {}
log_lines = []

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        log_lines.append(line.strip())
        if len(log_lines) % 10 == 0:
            total_size, status_code_counts = compute_metrics(log_lines)
            print_metrics(total_size, status_code_counts)
except KeyboardInterrupt:
    pass
