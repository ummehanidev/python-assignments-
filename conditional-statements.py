# Question 1 - ATM Machine System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖             CENTRAL BANK CORE             ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

account_balance = float(input("💳 Enter Account Balance:\t"))
withdraw_amount = float(input("💰 Enter Withdraw Amount:\t"))

print("╌" * 45)
print("🔍 TRANSACTION SUMMARY:")
print("╌" * 45)

if (withdraw_amount > account_balance):
    print("❌ Status: Insufficient Balance")

elif (withdraw_amount < 500):
    print("⚠️ Policy: Minimum withdrawal is 500")

else:
    remaining_balance = account_balance - withdraw_amount
    print("💸 Status: Withdrawal Successful")
    print("💵 Available Balance:\t", remaining_balance)
    
    if (remaining_balance > 10000):
        print("✨ Account Type:\tPremium User")
    else:
        print("👤 Account Type:\tNormal User")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# Question 2 - Smart Username Validator
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖            SECURITY GATEWAY               ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

username = input("Enter Username to Validate:\t")

print("-" * 45)
print("🔍 VALIDATION REPORT:")
print("-" * 45)

username_length  = len(username)
space_count      = username.count(" ")
is_first_capital = username[0].isupper()

has_number = ("0" in username or "1" in username or "2" in username or "3" in username or 
              "4" in username or "5" in username or "6" in username or "7" in username or 
              "8" in username or "9" in username)

is_valid = True

if (username_length < 8):
    print("❌ Status: Rejected (Length must be 8+ characters)")
    is_valid = False

if (space_count > 0):
    print("❌ Status: Rejected (Spaces are not allowed)")
    is_valid = False

if (is_first_capital == False):
    print("❌ Status: Rejected (First character must be uppercase)")
    is_valid = False

if (has_number == False):
    print("❌ Status: Rejected (Must contain at least one digit)")
    is_valid = False

if (is_valid == True):
    print("✅ Status: Accepted (Username is secure)")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Question 3 — Exam Eligibility Checker
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖          EXAM ELIGIBILITY GATEWAY         ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

student_name = input("Enter Student Name:\t\t")
attendance   = float(input("Enter Attendance (%):\t\t"))
fees_status  = input("Enter Fees Status (paid/unpaid):")

print("-" * 45)
print("🔍 VALIDATION REPORT:")
print("-" * 45)

fees_status = fees_status.lower()

if (attendance >= 75 and fees_status == "paid"):
    print("✅ Eligible For Exam")

elif (attendance < 75 and fees_status == "unpaid"):
    print("❌ Rejected: Low attendance AND unpaid fees")

elif (attendance < 75):
    print("❌ Rejected: Attendance must be greater than or equal to 75")

else:
    print("❌ Rejected: Fees status must be 'paid'")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")



# Question 4 — Password Security Checker
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖          PASSWORD SECURITY GATEWAY       ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

password = input("Enter Password to Check:\t")

print("-" * 45)
print("🔍 VALIDATION REPORT:")
print("-" * 45)

password_length  = len(password)
space_count      = password.count(" ")
is_first_capital = password[0].isupper()

has_special_char = ("@" in password or "#" in password)
is_valid = True


if (password_length < 8):
    print("❌ Rejected: Password length should be greater than or equal to 8")
    is_valid = False

if (has_special_char == False):
    print("❌ Rejected: Password must contain '@' or '#'")
    is_valid = False

if (space_count > 0):
    print("❌ Rejected: Password should not contain spaces")
    is_valid = False

if (is_first_capital == False):
    print("❌ Rejected: First character should be uppercase")
    is_valid = False

if (is_valid == True):
    print("✅ Strong Password")
else:
    print("❌ Weak Password")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Question 5 — Online Shopping Discount System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖          ONLINE SHOPPING GATEWAY          ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

customer_name = input("Enter Customer Name:\t\t")
total_bill    = float(input("Enter Total Bill:\t\t"))
membership    = input("Is Membership Status Active? (yes/no):\t")

print("-" * 45)
print("🧾 BILL RECEIPT & DISCOUNT REPORT:")
print("-" * 45)

membership = membership.lower()

if (total_bill > 5000 and membership == "yes"):
    discount_percentage = 20
elif (total_bill > 3000):
    discount_percentage = 10
else:
    discount_percentage = 0

discount_amount = total_bill * (discount_percentage / 100)
final_bill      = total_bill - discount_amount

print("Customer Name:\t\t",customer_name)
print("Original Bill:\t\t Rs." ,total_bill)
print("Discount Applied:\t",discount_percentage,"%" " " "(Rs.", discount_amount,")")
print("-" * 45)
print("Total Payable Bill:\tRs." ,final_bill)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Question 6 — Email Verification System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖         EMAIL VERIFICATION GATEWAY        ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

email = input("📧 Enter Your Email Address:\t")

print("-" * 45)
print("🔍 VALIDATION REPORT:")
print("-" * 45)

email = email.lower()
email_length = len(email)
space_count  = email.count(" ")

if (space_count > 0):
    print("❌ Invalid Email: Spaces are not allowed")

elif (email_length <= 12):
    print("❌ Invalid Email: Email length must be greater than 12 characters")

elif (email.endswith("@gmail.com") == False):
    print("❌ Invalid Email: Email must end with '@gmail.com'")

else:
    print("✅ Email Verified")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Question 7 — Smart Number Analyzer
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖           SMART NUMBER GATEWAY            ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

number = int(input("🔢 Enter Any Integer Number:\t"))

print("-" * 45)
print("📊 ANALYSIS REPORT:")
print("-" * 45)

if (number >= 0):
    print("✨ Sign Status:\t\tPositive Number")
else:
    print("✨ Sign Status:\t\tNegative Number")

if (number % 2 == 0):
    print("🔢 Parity Status:\tEven Number")
else:
    print("🔢 Parity Status:\tOdd Number")

if (number % 5 == 0):
    print("🎯 Divisibility:\tYes, Divisible by 5")
else:
    print("🎯 Divisibility:\tNo, Not Divisible by 5")

if (number > 100):
    print("🚀 Scale Status:\tLarge Number")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Question 8 — Truthy Falsy Login System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖           AUTHENTICATION GATEWAY          ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

username = input("👤 Enter Username:\t")
password = input("🔑 Enter Password:\t")

print("-" * 45)
print("🔐 ACCESS REPORT:")
print("-" * 45)

if (username and password):
    print("✅ Status:\t\tLogin Attempted")
    
    username_lower    = username.lower()
    username_reversed = username[::-1]
    
    print("🔤 Lowercase Name:\t",username_lower)
    print("🔄 Reversed Name:\t", username_reversed )

else:
    print("❌ Error:\t\tFields Cannot Be Empty")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Question 9 — Word Analyzer System
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖           WORD ANALYSIS GATEWAY           ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

sentence = input("📝 Enter a Sentence:(Must include the word 'Python'):\t")

print("-" * 45)
print("📊 TEXT METRICS & ANALYSIS:")
print("-" * 45)

if ("Python" in sentence):
    print("🎯 Keyword Status:\tPython Found")

    if (len(sentence) > 20):
     print("📏 Length Category:\tLong Sentence")
    else:
        print("📏 Length Category:\tShort Sentence")

    modified_sentence = sentence.replace("Python", "JavaScript")
    reversed_sentence = sentence[::-1]

    print("-" * 45)
    print("🔄 Replaced Text:\t", modified_sentence)
    print("↩️ Reversed Text:\t", reversed_sentence)

else:
    print("❌ Error:\t\tRequired keyword 'Python' was not found in the sentence.")
    print("💡 Suggestion:\t\tPlease run the program again and use the word 'Python'.")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Question 10 — Nested Login & Role Checker
# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("❖           ROLE MANAGEMENT GATEWAY         ❖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

correct_username = "admin123"
correct_password = "securepass"

username = input("👤 Enter Username:\t\t")
password = input("🔑 Enter Password:\t\t")
role     = input("🎖️ Enter Role (admin/student):\t")

print("-" * 45)
print("🔐 SECURITY ACCESS REPORT:")
print("-" * 45)

username = username.lower()
password = password.lower()
role     = role.lower()

if (username == correct_username and password == correct_password):
    
    if (role == "admin"):
        print("✅ Access Granted: Welcome Admin")
    elif(role == "student"):
        print("✅ Access Granted: Welcome Student")
    else:
        print("❌ Login Success, but Error: Invalid Role")

else:
    print("❌ Access Denied: Invalid Credentials")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")