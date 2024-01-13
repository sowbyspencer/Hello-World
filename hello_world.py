"""
A script to print a greeting and the current timestamp. The timestamp is 
formatted as YYYY-MM-DD HH:MM:SS, demonstrating Python's datetime module 
and print function.

Author:
    Spencer Sowby (sowbyspencer@gmail.com)
"""

# Importing the datetime class from the datetime module
from datetime import datetime

# Printing a greeting message
print(f"\nHello World!")

# Getting and formatting the datetime into a string
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Printing the formatted timestamp
print(f"Timestamp: {timestamp}\n")