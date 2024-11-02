import csv
import random
import datetime

# Generate a large dataset (10,000 rows) of employee data
def generate_large_dataset(file_name, num_records=10000):
    # Open a CSV file in write mode
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["EmployeeID", "Name", "Department", "Salary", "HireDate"])
       
        # List of sample departments and names for data generation
        departments = ["HR", "Sales", "Engineering", "Marketing", "Finance"]
        names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]

        for i in range(1, num_records + 1):
            # Randomly generate data for each employee
            emp_id = f"E{i:05d}"  # EmployeeID with padding (e.g., E00001)
            name = random.choice(names)
            department = random.choice(departments)
            salary = random.randint(30000, 120000)  # Salary between 30k and 120k
            hire_date = datetime.date(2000, 1, 1) + datetime.timedelta(days=random.randint(0, 7300))  # Random date within 20 years
            writer.writerow([emp_id, name, department, salary, hire_date])

# Read and format the dataset
def read_and_format_dataset(file_name):
    employees = []

    # Open the CSV file in read mode
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        # Read each row and store in a list of dictionaries
        for row in reader:
            employees.append(row)
   
    # Filter employees with a salary above 80,000
    high_salary_employees = [emp for emp in employees if int(emp["Salary"]) > 80000]
   
    # Sort employees by hire date
    high_salary_employees.sort(key=lambda x: x["HireDate"])

    # Display formatted output
    print("Employees with Salary Above 80,000 (Sorted by Hire Date):")
    print(f"{'EmployeeID':<10} {'Name':<10} {'Department':<12} {'Salary':<8} {'HireDate':<10}")
    print("-" * 50)
    for emp in high_salary_employees[:20]:  # Show top 20 records for readability
        print(f"{emp['EmployeeID']:<10} {emp['Name']:<10} {emp['Department']:<12} {emp['Salary']:<8} {emp['HireDate']}")

# Main function to run the program
def main():
    # Specify the file name for the dataset
    file_name = "large_employee_dataset.csv"
   
    # Step 1: Generate the dataset
    print("Generating a large dataset...")
    generate_large_dataset(file_name)
    print("Dataset created successfully.")
   
    # Step 2: Read and format the dataset
    print("\nReading and formatting the dataset...")
    read_and_format_dataset(file_name)
    print("\nData processing completed.")

# Run the main function
if __name__ == "__main__":
    main()

