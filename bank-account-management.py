# Store only actual values in variables
# Bank Information:
Bank_Name       = "INDUS UNION BANK"
Branch_Name     = "Clifton Premium Branch"
Branch_Code     = 5012
City            = "Karachi"
# Customer Information:
Customer_Name   = "Zayan Khan"
Father_Name     = "kamran Khan"
Age             = 21
Phone_Number    = "+92 300 9876543"
Email_Address   = "zayan.khan@indusbank.com"
#Account Information:
Account_Number  = 5544332211
Account_Type    = "Asaan Saving Account"
Currency        = "PKR"
Account_Balance = 60000
Loan_Amount     = 40000
ATM_Card_Number = "541278009123"
# Account Status:
Account_Active_Status =  True
Loan_Approved_Status  =  True
# Main Header
print("---------------------------------------------------------------------")
print("                              "+ Bank_Name)
print("---------------------------------------------------------------------")
print()
# Welcome Messages
print("Welcome" , Customer_Name, "to", Bank_Name)
print(Customer_Name , "from" , City , "has opened an" , Account_Type)
print()
# Customer & Account Data | multiple variables together in one line
print("Father's Name:" , Father_Name , "    ■    Age:" , Age)
print("Branch Name:" , Branch_Name , "     ■   Branch Code:" , Branch_Code)
print("Account Number:", Account_Number , "        ■   ATM Card Number:",ATM_Card_Number)
print("Phone Number:", Phone_Number , "     ■   Email:", Email_Address )
print()
# Financial Status Overview
print("Current Balance      :" , Account_Balance , Currency)
print("Loan Amount Approved :" , Loan_Amount , Currency )
print("Account Active Status:" , Account_Active_Status)
print("Loan Approved Status : ", Loan_Approved_Status )
print()
# Balance Updates Section
print("===============================================")
print("              ACCOUNT INFORMATION              ")
print("===============================================")
print("Old Balance:", Account_Balance, Currency)
print("Updated Balance:", Account_Balance + Loan_Amount, Currency)
print("■==================================================■")
# DATA TYPES DISPLAY
print(type(Bank_Name))
print(type(Branch_Code))
print(type(Account_Balance))
print(type(Account_Active_Status))
