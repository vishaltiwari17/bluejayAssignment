from datetime import datetime, timedelta

# Function to parse the file and extract employee data
def analyze_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    employees = {}

    for line in lines[1:]:  # Skip the header line
        data = line.strip().split(',')
        position_id = data[0]
        position_status = data[1]
        if data[2]:  # Check if Time is not empty
            start_time = datetime.strptime(data[2], '%m/%d/%Y %I:%M %p')
        else:
            start_time = None
        if data[3]:  # Check if Time Out is not empty
            end_time = datetime.strptime(data[3], '%m/%d/%Y %I:%M %p')
        else:
            end_time = None
        if data[7]:  # Check if Employee Name is not empty
            employee_name = data[7]
        else:
            employee_name = None

        if employee_name and start_time and end_time:  # Only process if essential data is present
            if employee_name not in employees:
                employees[employee_name] = []

            employees[employee_name].append((start_time, end_time, position_id, position_status))

    return employees

# Function to analyze employee data based on given criteria
def analyze_employees(employees):
    for name, shifts in employees.items():
        for i in range(len(shifts) - 1):
            # Check for consecutive days
            if (shifts[i+1][0] - shifts[i][1]).days == 1:
                print(f"{name} worked for 7 consecutive days. Position ID: {shifts[i+1][2]}")

            # Check for less than 10 hours between shifts but greater than 1 hour
            if shifts[i+1][0] - shifts[i][1] < timedelta(hours=10) and shifts[i+1][0] - shifts[i][1] > timedelta(hours=1):
                print(f"{name} has less than 10 hours between shifts but greater than 1 hour. Position ID: {shifts[i+1][2]}")

            # Check for more than 14 hours in a single shift
            if shifts[i][1] - shifts[i][0] > timedelta(hours=14):
                print(f"{name} has worked for more than 14 hours in a single shift. Position ID: {shifts[i][2]}")

# Main function
def main():
    file_path = r"C:\Users\Bansa\Downloads\Assignment_Timecard.xlsx - Sheet1.csv"
    employees = analyze_file(file_path)
    analyze_employees(employees)

if __name__ == "__main__":
    main()
