# =================================================================
# SMIT Summer Camp Assignment
# Task: Python Strings Assignment 
# =================================================================
# Q1 — Professional Email Management System

email       = "zayyan.khan2026@googlecorp.com"
username    = email[0:15]
company     = email[16:26]
domain_ext  = email[26:]
without_ext = email[0:26]
first_12    = email[0:12]
last_10     = email[-10:]

print("\n=========================================================")
print("       ✉️   Professional Email Management System           ")
print("=========================================================")
print(" Original Email    : " , email)
print("---------------------------------------------------------")

print("► Employee Username      :", username)
print("► Company Name           :", company)
print("► Domain Extension       :", domain_ext)
print("► Without Ext Extension  :", without_ext)
print("► First 12 Characters    :", first_12)
print("► Last 10 Characters     :", last_10)
print("=========================================================\n")

# =================================================================
# Q2 — E-Commerce Product Code Analyzer

product_code = "LAP-DELL-INSPIRON16-512GB-SILVER"
category     = product_code[0:3]
company      = product_code[4:8]
model        = product_code[9:19]
storage      = product_code[-12:-9]
color        = product_code[-6:]
first_char_company = product_code[4]
last_char_model    = product_code[18]

print("\n=========================================================")
print("        🏷️   E-COMMERCE PRODUCT CODE ANALYZER              ")
print("=========================================================")
print("Original Product Code : " , product_code)
print("---------------------------------------------------------")

print("► Product Category    :", category)
print("► Company Name        :", company)
print("► Model Name          :", model)
print("► Storage Size        :", storage)
print("► Product Color       :", color)
print("► First Char Company  :", first_char_company)
print("► Last Char Model     :", last_char_model)
print("=========================================================\n")


# =================================================================
# Q3 — Online Banking SMS Processor

banking_sms = "USD 75000 has been successfully transferred to account 98124"
amount      = banking_sms[4:9]
account_number = banking_sms[-5:]
status_word = banking_sms[18:30]
first_25    = banking_sms[0:25]
last_15     = banking_sms[-15:]
count_a     = banking_sms.count("a")

print("\n=========================================================")
print("          💰   ONLINE BANKING SMS PROCESSOR       ")
print("=========================================================")
print(" INCOMING SMS STREAM  : " , banking_sms)
print("---------------------------------------------------------")

print("► Transferred Amount : ", amount)
print("► Target Account No  : ", account_number)
print("► Transaction Status :",status_word)
print("► First 25 Chars     : ", first_25)
print("► Last 15 Chars      : ", last_15)
print("► Occurrences of 'a' : ", count_a)

print("=========================================================\n")

# =================================================================
# Q4 — University Student Record Formatter

student_record = "AI|2026|128|Rayyan Shahraiz Khan"
dept_name      = student_record[0:2]
batch_year     = student_record[3:7]
roll_number    = student_record[8:11]
full_name  = student_record[12:]
first_name = student_record[12:18]
initials = student_record[12] + student_record[19] + student_record[-4]

print("\n=========================================================")
print("           🎓   ACADEMIC REGISTRY RECORD       ")
print("=========================================================")
print(" STUDENT RAW RECORD   : " ,student_record)
print("---------------------------------------------------------")

print("► Department Name       :", dept_name)
print("► Batch Enrollment Year :", batch_year)
print("► Academic Roll Number  :", roll_number)
print("► Registered Full Name  :", full_name)
print("► Primary First Name    :", first_name)
print("► Initials             : ", initials)

print("=========================================================\n")

# =================================================================
# Q5 — Website URL Processing System

web_url = "https://www.cloudnexus.com"
without_https  = web_url[8:]
without_www    = web_url[12:]
website_name   = web_url[12:22]
domain_ext     = web_url[-4:]
is_dot_com     = web_url.endswith(".com")
middle_portion = web_url[12:17]

print("\n=========================================================")
print("            🌐   WEB URL ANALYSIS ENVIRONMENT       ")
print("=========================================================")
print(" ORIGINAL URL TEXT   : " ,web_url)
print("---------------------------------------------------------")
print("► Cleaned (No HTTP)     :", without_https)
print("► Cleaned (No WWW)      :", without_www)
print("► Extracted Brand Name  :", website_name)
print("► Domain Extension Type :", domain_ext)
print("► Verifying (.com) Ends :", is_dot_com)
print("► Segment Middle Block  :", middle_portion)

print("=========================================================\n")

# =================================================================
# Q6 — Secure Password Formatter

user_password = "Admin#Vortex99"
hidden_format = "*" * len(user_password)
first_char    = user_password[0]
last_char     = user_password[-1]
password_len  = len(user_password)
middle_chars  = user_password[6:12]
ends_with_num = user_password.endswith("99")

print("\n=========================================================")
print("            🔒   USER AUTHENTICATION GATEWAY        ")
print("=========================================================")
print(" ORIGINAL PASSWORD INPUT : " ,user_password )
print("---------------------------------------------------------")

print("► Hidden Password Format     :", hidden_format)
print("► First Character Only       :", first_char)
print("► Last Character Only        :", last_char)
print("► Total Password Length      :", password_len, "characters")
print("► Middle Character Block     :", middle_chars)
print("► Ends With Specific Number  :", ends_with_num)

print("=========================================================\n")

# =================================================================
# Q7 — File Management System

file_name    = "cloud_infrastructure_deployment_matrix_2026.pdf"
clean_spaces = file_name.replace("_", " ")
name_only    = file_name[:-4]
file_ext     = file_name[-4:]
is_pdf       = file_name.endswith(".pdf")
first_20     = file_name[0:20]
last_10      = file_name[-10:]

print("\n=========================================================")
print("            📁   AUTOMATED FILE RECORD SYSTEM        ")
print("=========================================================")
print(" SOURCE FILE DATA INPUT : " , file_name)
print("---------------------------------------------------------")

print("► Spaces Instead Of Underscores     :", clean_spaces)
print("► Filename Without Extension        :", name_only)
print("► File Extension Only               :", file_ext)
print("► Document Validation (.pdf)        :", is_pdf)
print("► First 20 Characters Only          :", first_20)
print("► Last 10 Characters Only           :", last_10)

print("=========================================================\n")

# =================================================================
# Q8 — Social Media Username Generator

first_name = "abbiyan"
last_name  = "khan"
fav_game   = "apex"
lucky_num  = "77"
username   = first_name + "_" + last_name + "_" + fav_game + "_" + lucky_num

user_no_lucky = username[:-2]
only_game     = username[13:17]
only_lucky    = username[-2:]
first_8_char  = username[0:8]
last_6_char   = username[-6:]
capital_user  = username.capitalize()

print("\n=========================================================")
print("            🆔   SOCIAL MEDIA USERNAME GENERATOR        ")
print("=========================================================")
print(" ORIGINAL USERNAME INPUT : " , username)
print("---------------------------------------------------------")

print("► Username Without Lucky Num :", user_no_lucky)
print("► Extracted Game Name Only   :", only_game)
print("► Extracted Lucky Number Only:", only_lucky)
print("► First 8 Characters Output  :", first_8_char)
print("► Last 6 Characters Output   :", last_6_char)
print("► Capitalized Username Style :", capital_user)
print("=========================================================\n")

# =================================================================
# Q9 — Chat Application Message Analyzer

chat_message = "hi team i have deployed my web application successfully"

capitalized_msg = chat_message.capitalize()
replaced_msg    = chat_message.replace("web", "cloud")
position_word   = chat_message.find("application")
count_s         = chat_message.count("s")
first_18        = chat_message[0:18]
last_20         = chat_message[-20:]
sliced_word     = chat_message[15:23]

print("\n=========================================================")
print("            💬   SMART CHAT MESSAGING SYSTEM               ")
print("=========================================================")
print(" Original Message : " , chat_message)
print("---------------------------------------------------------")

print("► Capitalized Case     :", capitalized_msg)
print("► String Replacement   :", replaced_msg)
print("► Keyword Position     : Index", position_word)
print("► Occurrences of 's'   :", count_s)
print("► Head (18 Chars)      :", first_18)
print("► Tail (20 Chars)      :", last_20)
print("► Extracted Action     :", sliced_word)

print("=========================================================\n")

# =================================================================
# Q10 — Online Course Information System

course_title = "Machine Learning Complete Masterclass 2026"

course_name    = course_title[0:16]
batch_year     = course_title[-4:]
first_word     = course_title[0:7]
last_word      = course_title[-4:]
first_15       = course_title[0:15]
last_12        = course_title[-12:]
count_o        = course_title.count("o")
ends_with_2026 = course_title.endswith("2026")

print("\n=========================================================")
print("             📚   COURSE INFORMATION SYSTEM               ")
print("=========================================================")
print(" Original Title : " , course_title)
print("---------------------------------------------------------")

print("► Course Name          :", course_name)
print("► Batch/Year           :", batch_year)
print("► First Keyword        :", first_word)
print("► Last Keyword         :", last_word)
print("► Head (15 Chars)      :", first_15)
print("► Tail (12 Chars)      :", last_12)
print("► Occurrences of 'o'   :", count_o)
print("► Ends with '2026'?    :", ends_with_2026)

print("=========================================================\n")
print("=========================================================")