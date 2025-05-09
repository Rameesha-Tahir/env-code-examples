# Function to compute average of a list
def average(values):
    return sum(values) / len(values)

data = [72, 55, 101, 90]
print("Average:", average(data))

# Station data
stations = [
    ['A1', 62],
    ['B2', 88],
    ['C3', 110],
    ['D4', 99]
]

for station in stations:
    print(f"{station[0]} → {station[1]}")

# Status reporting
def report_status(stations, threshold):
    for station in stations:
        status = "OK" if station[1] <= threshold else "ALERT"
        print(f"{station[0]}: {station[1]} → {status}")

report_status(stations, 100)
