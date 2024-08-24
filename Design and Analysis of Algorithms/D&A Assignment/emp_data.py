# Step 1: Parse the CSV data and store it in a list of dictionaries
data = []
with open('Business-employment-dataset.csv', 'r') as file:
    header = file.readline().strip().split(',')
    for line in file:
        values = line.strip().split(',')
        record = dict(zip(header, values))
        data.append(record)

# Step 2: Calculate the earning difference and earnings percentage difference for each row
for row in data:
    filled_jobs = int(row['filled jobs'])
    filled_jobs_revised = int(row['filled jobs revised'])
    filled_jobs_diff = filled_jobs_revised - filled_jobs
    filled_jobs_percentage_diff = (filled_jobs_diff / filled_jobs) * 100 if filled_jobs != 0 else 0

    # Update the data with the calculated values
    row['filled jobs diff'] = str(filled_jobs_diff)
    row['filled jobs % diff'] = f"{filled_jobs_percentage_diff:.2f}%"

# Step 3: Find the highest and lowest differences
# Initialize variables to track the highest and lowest differences and their corresponding rows
highest_diff = None
lowest_diff = None
highest_row = None
lowest_row = None

for row in data:
    filled_jobs_diff = int(row['filled jobs diff'])

    # Check for the highest difference
    if highest_diff is None or filled_jobs_diff > highest_diff:
        highest_diff = filled_jobs_diff
        highest_row = row

    # Check for the lowest difference
    if lowest_diff is None or filled_jobs_diff < lowest_diff:
        lowest_diff = filled_jobs_diff
        lowest_row = row

# Step 4: Print the highest and lowest differences in the console
if highest_row is not None:
    print("Highest Difference:")
    print(f"Period: {highest_row['period']}, Region: {highest_row['region_name']}")
    print(f"Filled Jobs Difference: {highest_row['filled jobs diff']}")
    print(f"Filled Jobs Percentage Difference: {highest_row['filled jobs % diff']}")
    print("-" * 30)

if lowest_row is not None:
    print("Lowest Difference:")
    print(f"Period: {lowest_row['period']}, Region: {lowest_row['region_name']}")
    print(f"Filled Jobs Difference: {lowest_row['filled jobs diff']}")
    print(f"Filled Jobs Percentage Difference: {lowest_row['filled jobs % diff']}")
    print("-" * 30)

# Step 5: Write the updated data to a new CSV file
with open('updated_employment_data.csv', 'w') as file:
    file.write(','.join(header) + '\n')
    for row in data:
        file.write(','.join(row.values()) + '\n')
