#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_file_size = 0
status_code_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}


def print_stats():
    """Prints the accumulated statistics."""
    print("File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal."""
    print_stats()
    sys.exit(0)


# Register the signal handler for SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        # Remove any leading/trailing whitespace characters
        line = line.strip()

        # Split the line based on spaces
        parts = line.split()
        if len(parts) < 7:
            # Skip lines that don't match the expected format
            continue

        # Extract the status code and file size from the line
        status_code = parts[-2]
        file_size = parts[-1]

        # Update total file size if file size is an integer
        try:
            total_file_size += int(file_size)
        except ValueError:
            continue

        # Update the count for the status code if it's expected codes
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Increment the line counter
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handles keyboard interrupt (CTRL + C)
    print_stats()
    raise
finally:
    # Always print the stats when the script ends
    print_stats()
