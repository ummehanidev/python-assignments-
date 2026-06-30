# OPERATORS ASSIGNMENT
# ------------------------------------------------------------------------------
# Q1 — Food Delivery Bill System
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  ★     \t   FOOD DELIVERY BILL SYSTEM \t    ★  ")
print("="*60)

# Input/Store data
# Assignment Operator
burger_price = 350
pizza_price  = 1350
burger_qty   = 2
pizza_qty    = 1
delivery_charges = 150

# Arithmetic Operator
total_burger_Cost = burger_price * burger_qty
total_Pizza_Cost  = pizza_price * pizza_qty
total_food_price  = total_burger_Cost + total_Pizza_Cost
final_bill        = total_food_price + delivery_charges

# ----- OUTPUT DISPLAY -----
print("\t Burger Price (Rs. 350 x 2) :  \t Rs.  ",total_burger_Cost)
print("\t Pizza Price (Rs. 1350 x 1) :  \t Rs.  ",total_Pizza_Cost)
print("\t--------------------------------------------")
print("\t Total Food Price :            \t Rs.  ",total_food_price)
print("\t Delivery Charges :            \t Rs.  ",delivery_charges)
print("\t--------------------------------------------")
print("\t FINAL PAYABLE BILL :         \t Rs.  ",final_bill)
print("============================================================\n")

# ------------------------------------------------------------------------------
# Q2 — Student Result Calculator
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  ◆      \t   STUDENT RESULT CALCULATOR \t    ◆  " )
print("="*60)

#  Store marks of 5 subjects
# Assignment Operator
sub1, sub2, sub3, sub4, sub5 = 85, 78, 92, 65, 89


# Arithmetic Operator
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage  = (total_marks / 500) * 100

# Relational Operator
pass_status = percentage >= 50

# ----- OUTPUT DISPLAY -----
print("\t Subject Marks         :         \t ",sub1 , sub2 , sub3 , sub4 , sub5)
print("\t--------------------------------------------")
print("\t Total Obtained        :         \t ",total_marks)
print("\t Percentage            :         \t ",percentage)
print("\t Pass Status           :         \t ",pass_status)
print("="*60 + "\n")


# ------------------------------------------------------------------------------
# Q3 — Online Shopping Discount
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  ✿     \t   ONLINE SHOPPING DISCOUNT \t    ✿  ")
print("="*60)

# Input/Store data
# Assignment Operator
original_price      = 6500
discount_percentage = 20

# Arithmetic Operator
discount_amount     = original_price * (discount_percentage / 100)
final_price         = original_price - discount_amount

# Relational Operator
comparison_result   = final_price < 5000

# ----- OUTPUT DISPLAY -----
print("\t Original Price        :         \t Rs.",original_price)
print("\t Discount Applied:     :         \t",discount_percentage,"% (-Rs",discount_amount,")")
print("\t--------------------------------------------")
print("\t Final Price           :         \t Rs.",final_price)
print("\t FiIs Budget Friendly (<5k)?       :     ",comparison_result)
print("="*60 + "\n")


# ------------------------------------------------------------------------------
# Q4 — Bank Account Balance
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  ⌂     \t   BANK ACCOUNT BALANCE TRANSACTION \t    ⌂  ")
print("="*60)

 # Variables
current_balance    = 50000
atm_withdrawal     = 15000
mobile_banking_fee = 25

# Assignment Operator
remaining_balance  = current_balance
remaining_balance -= atm_withdrawal
remaining_balance -= mobile_banking_fee

# ----- OUTPUT DISPLAY -----
print("\tOpening Balance    :      \t Rs.", current_balance)
print("\tATM Withdrawal     :       \t Rs.", atm_withdrawal)
print("\tMobile Banking Fee :   \t Rs.", mobile_banking_fee)
print("\t--------------------------------------------")
print("\tREMAINING BALANCE  :       Rs.", remaining_balance)
print("=" * 60 + "\n")

# ------------------------------------------------------------------------------
# Q5 — Mobile Login Verification
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  🔒    \t MOBILE LOGIN VERIFICATION \t    🔒  " )
print("="*60)

# Boolean Variables 
username_status = True
password_status = True
fingerprint_status = False

# Logical Operators 
final_login_result = (username_status and password_status) or fingerprint_status

# ----- OUTPUT DISPLAY -----
print("\tCredential Check   :     \t Username:", username_status, "| Password:", password_status)
print("\tBiometric Check    :     \t Fingerprint:", fingerprint_status)
print("\t--------------------------------------------")
print("\tACCESS GRANTED     :     \t Fingerprint:", final_login_result)
print("=" * 60 + "\n")


# ------------------------------------------------------------------------------
# Q6 — Car Fuel Average
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  🚗    \t CAR FUEL AVERAGE CALCULATOR \t    🚗  ")
print("="*60)

# Assignment Operator
total_km    = 600
fuel_liters = 40

# Arithmetic Operator 
car_average = total_km / fuel_liters

# Relational Operator
comparison_result = car_average >= 15

# ----- OUTPUT DISPLAY -----
print("\tTotal Distance   :     \t ", total_km   , "Kilometers")
print("\tFuel Consumed    :     \t ", fuel_liters , "Liters")
print("\t--------------------------------------------")
print("\tFuel Average     :     \t ", car_average  , "km/liter")
print("\tExcellent Mileage (>=15)? : \t ", comparison_result)
print("=" * 60 + "\n")


# ------------------------------------------------------------------------------
# Q7 — Employee Salary Management
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  💼    \t EMPLOYEE SALARY MANAGEMENT \t    💼  ")
print("="*60)

basic_salary = 85000     
bonus        = 12000            # Performance bonus
tax_rate     = 15         

# Calculation using assignment operator
gross_salary  = basic_salary
gross_salary += bonus
tax           = gross_salary * (tax_rate / 100)
final_salary  = gross_salary - tax

# ----- OUTPUT DISPLAY -----
print("\tBasic Salary   :     \t Rs.", basic_salary)
print("\tBonus Added    :     \t Rs.", bonus)
print("\tTax Deducted (", tax_rate, "%)  :  Rs.", tax)
print("\t--------------------------------------------")
print("\tNET PAYABLE SALARY    :\t Rs.", final_salary)
print("=" * 60 + "\n")


# ------------------------------------------------------------------------------
# Q8 — University Eligibility Check
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  🎓    \t UNIVERSITY ELIGIBILITY CHECK \t    🎓  ")
print("="*60)

student_percentage = 72
test_status = True
# Using Logical Operator
eligibility_result = (student_percentage >= 60) and test_status

# ----- OUTPUT DISPLAY -----
print("\tAcademic Percentag        : \t",student_percentage,"% (Required: >=60%) ")
print("\tEntry Test Status         : \t ",test_status )
print("\t--------------------------------------------")
print("\tADMISSION ELIGIBILITY     : \t ", eligibility_result )
print("=" * 60 + "\n")


# ------------------------------------------------------------------------------
# Q9 — Electricity Bill Calculator
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  ⚡    \t ELECTRICITY BILL CALCULATOR \t    ⚡  ")
print("="*60)

units = 320
price_per_unit = 18
tax_charges = 450

# Calculation Using Arithmetic Operator 
total_bill = units * price_per_unit
final_bill = total_bill + tax_charges

# ----- OUTPUT DISPLAY -----
print("\tUnits Consumed             : \t ", units ," Units")
print("\tRate per Unit              : \t Rs. ", price_per_unit )
print("\tBase Electricity Cost      : \t Rs. ", total_bill )
print("\tGovernment Tax             : \t Rs. ", tax_charges )
print("\t--------------------------------------------")
print("\tTOTAL ELECTRICITY BILL     : \t Rs. ", final_bill )
print("=" * 60 + "\n")

# ------------------------------------------------------------------------------
# Q10 — Smartphone Installment System
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print ( "  📱    \t SMARTPHONE INSTALLMENT SYSTEM \t    📱  ")
print("="*60)

phone_price = 85000
down_payment = 25000

remaining_amount = phone_price - down_payment
monthly_installment = remaining_amount / 12
comparison_result = monthly_installment <= 5000

# ----- OUTPUT DISPLAY -----
print("\tTotal Phone Price                 : \t Rs. ", phone_price )
print("\tDown Payment Paid                 : \t Rs. ",down_payment )
print("\tFinanced Amount                   : \t Rs. ",remaining_amount )
print("\t--------------------------------------------")
print("\tMonthly Installment               : \t Rs. ",monthly_installment )
print("\tIs Affordability Match (<=5k)?    : \t Rs. ",comparison_result )
print("="*60)
print("=" * 60 + "\n")