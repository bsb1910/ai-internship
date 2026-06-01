# Student Information System

print("=== Student Information System ===")

# Taking input from user
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
branch = input("Enter Branch: ")
cgpa = float(input("Enter CGPA: "))

# Storing data in a dictionary
student = {
    "Name": name,
    "Age": age,
    "Branch": branch,
    "CGPA": cgpa
}

# Displaying student details
print("\nStudent Details")
print("-" * 30)

for key, value in student.items():
    print(f"{key:<10}: {value}")