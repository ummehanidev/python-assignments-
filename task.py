#  ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
#  Question 1 — Student Profile System
#  ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tPORTAL INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

#  Inputs
user_name = input("Enter Full Name:\t\t")
user_city = input("Enter City Name:\t\t")
user_course    = input("Enter Course Name:\t\t")
total_marks    = input("Enter Total Marks:\t\t")
obtained_marks = input("Enter Obtained Marks:\t\t")

# Type Conversion & Percentage Calculation
total_int    = int(total_marks)
obtained_int = int(obtained_marks)
percentage   = (obtained_int / total_int) * 100

# String Methods 
student_name = user_name.capitalize()
student_city = user_city.upper()
clean_course = user_course.capitalize()

# Formatted Output 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tSTUDENT PROFILE CARD")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Student Name:\t\t",student_name)
print("Student City:\t\t",student_city)
print("Course Name :\t\t",clean_course)
print("Total Percentage:\t",percentage, "%")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Show Data Types using type() 
print("\n  SYSTEM DATA CHECK")
print("Name Type      :\t", type(student_name))
print("City Type      :\t" , type(student_city))
print("Course Type    :\t" , type(clean_course))
print("Percentage Type:\t" , type(percentage))
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 2 - Username Generator
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tSECURITY INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Inputs 
first_name = input("Enter First Name:\t")
last_name  = input("Enter Last Name:\t")
birth_year = input("Enter Birth Year:\t")

# Joining Strings & Making Lowercase
full_text = first_name + last_name + birth_year
generated_username = full_text.lower()

# Finding Length
username_length = len(generated_username)

# First and Last Character using Indexing
first_char = generated_username[0]
last_char  = generated_username[-1]

# Output Display 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tUSER LOGIN INFO")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Username:\t\t", generated_username)
print("ID Length:\t\t", username_length)
print("First Letter:\t\t", first_char)
print("Last Letter:\t\t", last_char)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 3 - Smart Calculator
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tCALCULATOR INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Input and Type Conversion 
num1 = int(input("Enter First Value:\t\t"))
num2 = int(input("Enter Second Value:\t\t"))

# Operations (Addition, Subtraction, Multiplication, Division, Modulus, Power)
ans_add = num1 + num2
ans_sub = num1 - num2
ans_mul = num1 * num2
ans_div = num1 / num2
ans_mod = num1 % num2
ans_pow = num1 ** num2

# Formatted Output 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tCALCULATION REPORT")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Addition Result      :\t", ans_add)
print("Subtraction Result   :\t", ans_sub)
print("Multiplication Result:\t", ans_mul)
print("Division Result      :\t", ans_div)
print("Modulus Result       :\t", ans_mod)
print("Power Result         :\t", ans_pow)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 4 - String Analyzer
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tANALYTICS INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Input 
user_sentence = input("Enter Any Sentence:\t")

# String Methods Operations
txt_upper   = user_sentence.upper()
txt_lower   = user_sentence.lower()
txt_cap     = user_sentence.capitalize()
count_a     = user_sentence.count("a")

# Word Replace 
txt_replace = user_sentence.replace("World", "Python")

# Reversing String using Slicing
txt_reverse = user_sentence[ ::-1]

# Formatted Output Block 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tTEXT ANALYTICS INFO")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Uppercase Text     :\t", txt_upper)
print("Lowercase Text     :\t", txt_lower)
print("Capitalized Text   :\t", txt_cap)
print("Count of Letter 'a':\t", count_a)
print("Replaced Text      :\t", txt_replace)
print("Reverse Text       :\t", txt_reverse)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 5 - Email Checker System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tVALIDATION INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Input 
user_email = input("Enter Gmail Address:\t")

# Check email using endswith() 
is_valid_gmail = user_email.endswith("@gmail.com")

# Print username part only using replace()
email_username = user_email.replace("@gmail.com", "")

# Find email length using len()
email_length = len(user_email)

# Output Display 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tEMAIL DATA CHECK")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Verification Status:\t", is_valid_gmail)
print("User ID Name:\t\t", email_username)
print("Total Characters:\t", email_length)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 6 - Shopping Bill Generator
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tTRANSACTION INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Inputs and Conversions 
item_name = input("Enter Item Name:\t\t").capitalize()
item_price = float(input("Enter Item Price:\t\t"))   
item_qty = int(input("Enter Item Quantity:\t\t"))

# Bill Calculations
total_bill = item_price * item_qty
discount_amount = total_bill * 0.10               
final_bill = total_bill - discount_amount

# Output Display
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tINVOICE DETAILS")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Item Description:\t", item_name)
print("Purchase Quantity:\t", item_qty)
print("Gross Total:\t\t", total_bill)
print("Discount (10%):\t\t", discount_amount)
print("Net Payable:\t\t", final_bill)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 7 - Mini Bio Data Card
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tREGISTRATION INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Inputs 
bio_name   = input("Enter Full Name:\t").capitalize()
bio_age    = input("Enter Your Age :\t")
bio_city   = input("Enter Current City  :\t").capitalize()
bio_course = input("Enter Active Program:\t").capitalize()


# String Concatenation & Escape Sequences 
output_text = (
    "Identity Name:\t\t" + bio_name + "\n" +
    "Current Age  :\t\t" + bio_age + "\n" +
    "Location City:\t\t" + bio_city + "\n" +
    "Enrolled Course:\t" + bio_course
)
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tUSER BIO DATA")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print(output_text)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 8 - Password Strength Checker
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tPASSWORD CHECK IN")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Input
user_password = input("Enter Your Password:\t")

# Logic Calculations (Using .find() method)
pass_length   = len(user_password)

has_at_symbol = user_password.find("@") >= 0

# Slicing
first_three   = user_password[:3]
last_three    = user_password[-3:]

# Output Display 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tPASSWORD SUMMARY")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Character Count  :\t", pass_length)
print("Contains '@' Sign:\t", has_at_symbol)
print("Starting Code:\t\t", first_three)
print("Ending Code  :\t\t", last_three)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 9 - Movie Ticket System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tBOOKING INITIALIZATION")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Inputs
movie_name   = input("Enter Movie Name:\t\t").capitalize()
ticket_price = float(input("Enter Ticket Price:\t\t"))
ticket_qty   = int(input("Enter Seats Quantity:\t\t"))

# Total Calculation
total_amount = ticket_price * ticket_qty

# Output Display 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tTICKET RECEIPT")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Selected Movie:\t\t", movie_name)
print("Reserved Seats:\t\t", ticket_qty)
print("Total Fair Amount:\t", total_amount)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")


# Question 10 - Online Food Order System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tORDER ENTRY PROCESS")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

# Inputs, Conversions & String Formatting
cust_name  = input("Enter Customer Name:\t\t").capitalize()
food_item  = input("Enter Food Item:\t\t").capitalize()
item_price = float(input("Enter Item Price:\t\t"))
item_qty   = int(input("Enter Item Quantity:\t\t"))

base_total       = item_price * item_qty
delivery_charges = base_total * 0.05               # 5% delivery fee calculation
grand_total      = base_total + delivery_charges

# Output Display 
print("\n―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("\t\tDIGITAL FOOD INVOICE")
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("Client Name:\t\t", cust_name)
print("Ordered Item:\t\t", food_item)
print("Order Quantity:\t\t", item_qty)
print("Delivery Service Fee:\t", delivery_charges)
print("Final Amount Due:\t", grand_total)
print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")