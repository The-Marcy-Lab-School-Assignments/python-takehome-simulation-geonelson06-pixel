# NYC 311 Service Requests Analysis
 
## How to Run
 
1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:
 
python3 analysis.py
 
Output will be saved to `output.txt`. The console will confirm when the file has been written.
 
## What This Script Does
 
The program begins by opening `nyc_311_requests.csv`, reading each row, and storing the data in a list. It then creates variables to track the information needed for the final output. As it loops through each row, it updates counters and dictionaries based on `resolution_status`, `complaint_type`, and `borough`.

To find the most common values, it uses `max()` to return the key with the highest count in a dictionary. The program also tracks additional data such as open and closed requests per borough using separate dictionaries, updating them during the same loop through the dataset.

After processing the data, it uses `sorted()` to organize results like complaint types and boroughs by frequency, which allows it to identify the top entries, including the top three boroughs by total requests. It also calculates closure rates by dividing closed requests by total requests per borough and formatting the result as a percentage.

Finally, it writes all computed results to `output.txt`, including open requests, most common complaint type, borough breakdowns, complaint breakdowns, the borough with the most open requests, closure rates, and the top three boroughs by total requests.
 
## Dependencies
 
This script uses only Python's built-in libraries: `csv`.
 
## Notes
 
[Optional: anything you want to flag about your approach or assumptions.]