import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
complaint_counts = {}
borough_counts = {}
open_by_borough = {}
closed_by_borough = {}

for row in rows:
    borough = row['borough']
    complaint = row['complaint_type']
    status = row['resolution_status']

    if status == 'Open':
        open_requests += 1
        open_by_borough[borough] = open_by_borough.get(borough, 0) + 1
    else:
        closed_by_borough[borough] = closed_by_borough.get(borough, 0) + 1

    complaint_counts[complaint] = complaint_counts.get(complaint, 0) + 1

    borough_counts[borough] = borough_counts.get(borough, 0) + 1

most_common = max(complaint_counts, key=complaint_counts.get)

most_open_borough = max(open_by_borough, key=open_by_borough.get)

top_boroughs = sorted(
    borough_counts.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_requests}\n\n")

    f.write(
        f"Most common complaint type: {most_common} "
        f"({complaint_counts[most_common]} requests)\n\n"
    )

    f.write("Requests per borough:\n")
    for borough in sorted(borough_counts):
        f.write(f"- {borough}: {borough_counts[borough]}\n")

    f.write("\nRequests by complaint type:\n")
    top_complaints = sorted(
        complaint_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:4]

    for complaint, count in top_complaints:
        f.write(f"- {complaint}: {count}\n")

    f.write(
        f"\nBorough with most open requests: "
        f"{most_open_borough} "
        f"({open_by_borough[most_open_borough]} open)\n"
    )

    f.write("\nClosure rate by borough:\n")
    for borough in sorted(borough_counts):
        total = borough_counts[borough]
        closed = closed_by_borough.get(borough, 0)

        rate = (closed / total) * 100

        f.write(f"- {borough}: {rate:.1f}%\n")

    f.write("\nTop 3 boroughs by total requests:\n")
    for i, (borough, count) in enumerate(top_boroughs, start=1):
        f.write(f"{i}. {borough} ({count} requests)\n")

print("Output saved to output.txt")