# NYC 311 Service Requests Analysis
 
## How to Run
 
1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:
 
python3 analysis.py
 
Output will be saved to `output.txt`. The console will confirm when the file has been written.
 
## What This Script Does
 
The program begins by opening nyc_311_requests.csv, reading each row, and storing the data in a list. It then creates variables to track the information needed for the final output. By iterating through each row, the program updates counters and dictionaries based on the row's resolution_status, complaint_type, and borough values. To determine the most frequently occurring items, it uses the max() function to find the dictionary keys with the highest counts. Finally, it opens output.txt and writes the calculated results to the file.
 
## Dependencies
 
This script uses only Python's built-in libraries: `csv`.
 
## Notes
 
[Optional: anything you want to flag about your approach or assumptions.]