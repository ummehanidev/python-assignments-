# Dictionary Assignment
# ==============================================================================
# Question 1 — Student Profile System
# ==============================================================================

student_profile = {
    "name": "Umm e Hani",
    "age": 16,
    "city": "Karachi",
    "hobbies": ["Coding", "Reading", "Gaming"],
    "skills": ["Python", "HTML", "CSS", "Data Analytics"]
}

print("=========================================")
print("         STUDENT PROFILE SYSTEM          ")
print("=========================================")

print("Student Name  :", student_profile["name"])
print("Primary Hobby :", student_profile["hobbies"][0])
print("Total Skills  :", len(student_profile["skills"]))

print("=========================================\n")

# ==============================================================================
# Question 2 — Student Marks System
# ==============================================================================

student_marks = {
    "marks": {
        "math": 85,
        "english": 78,
        "science": 92,
        "computer": 95
    }
}

print("=========================================")
print("          STUDENT MARKS REPORT           ")
print("=========================================")

marks_data = student_marks["marks"]
print("Math Marks    :", marks_data["math"])
print("English Marks :", marks_data["english"])
print("Science Marks :", marks_data["science"])
print("Computer Marks:", marks_data["computer"])

print("-----------------------------------------")

total_marks = marks_data["math"] + marks_data["english"] + marks_data["science"] + marks_data["computer"]
print("Total Marks   :", total_marks)

average_marks = total_marks / 4
print("Average Marks :", average_marks)

print("=========================================\n")

# ==============================================================================
# Question 3 — Grade Checking System
# ==============================================================================

print("=========================================")
print("         GRADE ANALYSIS DASHBOARD        ")
print("=========================================")

if (average_marks >= 80):
    final_grade = "A"
    status = "Passed"
elif (average_marks >= 70):
    final_grade = "B"
    status = "Passed"
elif (average_marks >= 60):
    final_grade = "C"
    status = "Passed"
else:
    final_grade = "Fail"
    status = "Failed"

print("Final Grade   :", final_grade)
print("Exam Status   :", status)

print("=========================================\n")

# ==============================================================================
# Question 4 — Attendance Management System
# ==============================================================================

attendance = {
    "records": {
        "total_classes": 40,
        "attended_classes": 32
    }
}

print("=========================================")
print("       ATTENDANCE COMPLIANCE SYSTEM      ")
print("=========================================")

total = attendance["records"]["total_classes"]
attended = attendance["records"]["attended_classes"]

attendance_percentage = (attended / total) * 100
print("Total Classes :", total)
print("Classes Attended:", attended)
print("Attendance (%) :", attendance_percentage)

print("-----------------------------------------")

if (attendance_percentage < 75):
    status = "Short Attendance"
else:
    status = "Eligible For Exam"

print("Exam Status   :", status)
print("=========================================\n")

# ==============================================================================
# Question 5 — Fee Management System
# ==============================================================================

fee_status = {
    "records": {
        "fee_paid": True  
    }
}

print("=========================================")
print("         FEE MANAGEMENT SYSTEM           ")
print("=========================================")

is_paid = fee_status["records"]["fee_paid"]

if (is_paid == True):
    status_message = "Fee Cleared"
else:
    status_message = "Fee Pending"

print("Payment Status:", status_message)
print("=========================================\n")

# ==============================================================================
# Question 6 — Skills Management System
# ==============================================================================

developer_profile = {
    "skills": ["Python", "HTML", "CSS"]
}

print("=========================================")
print("        SKILLS MANAGEMENT SYSTEM        ")
print("=========================================")

print("Original Skills:", developer_profile["skills"])
print("-----------------------------------------")

developer_profile["skills"].append("Data Analytics")
developer_profile["skills"].remove("HTML")

print("Updated Skills :", developer_profile["skills"])

total_skills = len(developer_profile["skills"])
print("Total Skills   :", total_skills)

print("=========================================\n")

# ==============================================================================
# Question 7 — Login Authentication System
# ==============================================================================

auth_database = {
    "credentials": {
        "username": "admin123",
        "password": "securepassword"
    }
}

print("=========================================")
print("       SECURE AUTHENTICATION SYSTEM      ")
print("=========================================")

input_username = input("Enter Username : ")
input_password = input("Enter Password : ")

print("-----------------------------------------")

correct_user = auth_database["credentials"]["username"]
correct_pass = auth_database["credentials"]["password"]

if (input_username == correct_user) and (input_password == correct_pass):
    auth_status = "Login Successful"
else:
    auth_status = "Invalid Credentials"

print("Login Status   :", auth_status)
print("=========================================\n")


# ==============================================================================
# Question 8 — Address Management System
# ==============================================================================

student_address = {
    "address": {
        "area": "Gulshan-e-Iqbal",
        "street": "Main University Road",
        "house_number": "D-45"
    }
}

print("=========================================")
print("        ADDRESS MANAGEMENT SYSTEM        ")
print("=========================================")

print("Original Area   :", student_address["address"]["area"])
print("Street Details  :", student_address["address"]["street"])
print("House Number    :", student_address["address"]["house_number"])

print("-----------------------------------------")

student_address["address"]["area"] = "Clifton"
student_address["address"]["zip_code"] = "75600"

print("Updated Area    :", student_address["address"]["area"])
print("Assigned Zip    :", student_address["address"]["zip_code"])

print("=========================================\n")

# ==============================================================================
# Question 9 — Multiple Students Database
# ==============================================================================

students_database = {
    "students": {
        "student1": {
            "name": "Zoha Khan",
            "city": "Karachi",
            "marks": 87.5
        },
        "student2": {
            "name": "Ayesha Ahmed",
            "city": "Lahore",
            "marks": 91.0
        }
    }
}

print("=========================================")
print("       MULTIPLE STUDENTS DATABASE        ")
print("=========================================")

db_records = students_database["students"]
db_records["student1"]["city"] = "Islamabad"

print("Student 1 Name :", db_records["student1"]["name"])
print("Student 2 Marks:", db_records["student2"]["marks"])
print("Updated City   :", db_records["student1"]["city"])

print("=========================================\n")

# ==============================================================================
# Question 10 — Final Student Report Card System
# ==============================================================================

print("==================================================")
print("           FINAL STUDENT REPORT CARD              ")
print("==================================================")

# Section 1: Personal Profile Info
print(" --- PERSONAL PROFILE ---")
print("Student Name    :", db_records["student1"]["name"])
print("City Location   :", db_records["student1"]["city"])
print("--------------------------------------------------")

# Section 2: Academic Performance Details
print(" --- ACADEMIC PERFORMANCE ---")
print("Math Marks      :", student_marks["marks"]["math"])
print("English Marks   :", student_marks["marks"]["english"])
print("Science Marks   :", student_marks["marks"]["science"])
print("Computer Marks  :", student_marks["marks"]["computer"])
print("Total Score     :", total_marks)
print("Average Marks   :", average_marks)
print("Final Grade     :", final_grade)
print("--------------------------------------------------")

# Section 3: Status & Attendance Records
print(" --- ELIGIBILITY & FEES STATUS ---")
print("Attendance (%)  :", attendance_percentage)
print("Exam Status     :", status)  
print("Tuition Fees    :", status_message)  
print("--------------------------------------------------")

# Section 4: Skills & Residential Address
print(" --- PORTFOLIO & LOCALIZATION ---")
print("Active Skills   :", developer_profile["skills"])
print("Area            :", student_address["address"]["area"])
print("Street Details  :", student_address["address"]["street"])
print("House Number    :", student_address["address"]["house_number"])
print("Assigned Zip    :", student_address["address"]["zip_code"])
print("==================================================")