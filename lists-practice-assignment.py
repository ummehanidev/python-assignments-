# Q1 — Online Food Delivery System
print("=" * 70)
print(" \t\t  ONLINE FOOD DELIVERY SYSTEM")
print("=" * 70 ,)

foods = ["Burger", "Pizza", "Fries", "Broast", "Sandwich"]

print("\nOriginal List           :", foods)
print("-" * 70)

print("• First Food Item         :", foods[0])

print("• Last Food Item          :", foods[-1])

foods[2] = "Pasta"
print("• After Replacing Fries   :", foods)

foods.append("Zinger")
print("• After Adding Zinger     :", foods)

foods.insert(2, "Shawarma")
print("• After Inserting Shawarma:", foods)

foods.remove("Pizza")
print("• After Removing Pizza    :", foods)

foods.pop()
print("• After Pop Operation     :", foods)

print("• Total Items             :", len(foods))

print("• First 3 Items           :", foods[:3])

print("• Last 2 Items            :", foods[-2:])

foods.reverse()
print("• Reversed List           :", foods)

foods.sort()
print("• Sorted List             :", foods)

print("\nFinal Updated List      :", foods)
print("=" * 70)

# Q2 — Student Attendance Management

print("=" * 70)
print(" \t\t  STUDENT ATTENDANCE MANAGEMENT")
print("=" * 70)

students = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]

print("\nOriginal List             :", students)
print("-" * 70)

print("• Second Student            :", students[1])
print("• Last Student              :", students[-1])

students[2] = "Hamza"
print("• After Changing Ahmed      :", students)

students.append("Fatima")  
print("• After Adding Fatima       :", students)

students.insert(1, "Ayesha")
print("• After Inserting Ayesha    :", students)

students.remove("Sara")
print("• After Removing Sara       :", students)

students.pop(3)
print("• After Pop Operation       :", students)

print("• Total Students:", len(students))
print("• Students From Index 1 To 4:", students[1:5])

students.reverse()
print("• Reversed List             :", students)

print("\nFinal Updated List        :", students)
print("=" * 70)

# Q3 — Mobile Prices Analysis

print("=" * 70)
print(" \t\t  MOBILE PRICES ANALYSIS")
print("=" * 70)

prices = [45000, 120000, 30000, 85000, 60000]

print("\nOriginal Prices:", prices)
print("-" * 70)

prices.sort()
print("• Highest Price         :", prices[-1])
print("• Lowest Price          :", prices[0])
print("• Ascending Order       :", prices)

prices.sort(reverse=True)
print("• Descending Order      :", prices)

prices.append(75000)
print("• After Adding New Price:", prices)

prices.remove(30000)
print("• After Removing 30000  :", prices)

prices.pop()
print("• After Pop Operation   :", prices)

print("• First 3 Prices        :", prices[:3])
print("• Last 2 Prices         :", prices[-2:])
print("• Total Number of Prices:", len(prices))

print("\nFinal Updated List    :", prices)
print("=" * 70)

# Q4 — Cricket Team Management

print("=" * 70)
print(" \t\t  CRICKET TEAM MANAGEMENT")
print("=" * 70)

players = ["Babar", "Rizwan", "Shaheen", "Naseem", "Shadab"]

print("\nOriginal Squad:", players)
print("-" * 70)

print("• Captain Name           :", players[0])
print("• Last Player            :", players[-1])

players[-1] = "Imad"
print("• After Replacing Shadab :", players)

players.append("Fakhar")
print("• After Adding New Player:", players)

players.insert(2, "Haris")
print("• After Inserting Player :", players)

players.remove("Naseem")
print("• After Removing Naseem  :", players)

print("• First 4 Players        :", players[:4])
print("• Last 3 Players         :", players[-3:])

players.reverse()
print("• Reversed Team          :", players)

print("\nFinal Squad            :", players)
print("=" * 70)

# Q5 — Shopping Cart System

print("=" * 70)
print(" \t\t  SHOPPING CART SYSTEM")
print("=" * 70)

cart = ["Shoes", "Watch", "Bag", "Laptop", "Bottle"]

print("\nOriginal Cart:", cart)
print("-" * 70)
  
print("• First Cart Item       :", cart[0])
print("• Last Item             :", cart[-1])

cart[-1] = "Headphones"
print("• After Replacing Bottle:", cart)

cart.append("Keyboard")
print("• After Adding Keyboard :", cart)

cart.insert(1, "Mouse")
print("• After Inserting Mouse :", cart)

cart.remove("Bag")
print("• After Removing Bag    :", cart)

cart.pop()
print("• After Pop Operation   :", cart)

print("• Total Cart Items      :", len(cart))
print("• Middle 3 Items        :", cart[1:4])

cart.reverse()
print("• Reversed Cart         :", cart)

print("\nUpdated Cart          :", cart)
print("=" * 70)

# Q6 — Employee Salary Records

print("=" * 70)
print(" \t\t  EMPLOYEE SALARY RECORDS")
print("=" * 70)

salaries = [25000, 40000, 70000, 55000, 90000]

print("\nOriginal Salaries:", salaries)
print("-" * 70)

salaries.sort()
print("• Highest Salary              :", salaries[-1])
print("• Lowest Salary               :", salaries[0])
print("• Salaries In Ascending Order :", salaries)

salaries.sort(reverse=True)
print("• Salaries In Descending Order:", salaries)

salaries.append(60000)
print("• After Adding New Salary     :", salaries)

salaries.remove(25000)
print("• After Removing Salary       :", salaries)

salaries.sort(reverse=True)
print("• Second Highest Salary       :", salaries[1])

print("• First 3 Salaries            :", salaries[:3])
print("• Total Salaries Count        :", len(salaries))

print("\nFinal Salary List           :", salaries)
print("=" * 70)

# Q7 — Movie Collection System

print("=" * 70)
print(" \t\t  MOVIE COLLECTION SYSTEM")
print("=" * 70)

movies = ["Avatar", "Inception", "Joker", "Titanic", "Interstellar"]

print("\nOriginal Collection:", movies)
print("-" * 70)

print("• First Movie               :", movies[0])
print("• Last Movie                :", movies[-1])

movies[2] = "Batman"
print("• After Replacing Joker     :", movies)

movies.append("Avengers")
print("• After Adding Movie        :", movies)

movies.insert(3, "Spider-Man")
print("• After Inserting Movie     :", movies)

movies.remove("Titanic")
print("• After Removing Titanic    :", movies)

movies.pop()
print("• After Pop Operation       :", movies)

print("• First 4 Movies            :", movies[:4])

movies.reverse()
print("• Reversed Collection       :", movies)

print("\nFinal Updated Collection:", movies)
print("=" * 70)

# Q8 — Exam Marks Analysis

print("-" * 70)
print(" \t\t  EXAM MARKS ANALYSIS")
print("-" * 70)

marks = [78, 45, 90, 66, 82]

print("\nOriginal Marks                :", marks)
print("-" * 70)
marks.sort()
print("• Highest Marks                 :", marks[-1])
print("• Lowest Marks                  :", marks[0])
print("• Sorted Marks (Ascending)      :", marks)

marks.sort(reverse=True)
print("• Sorted Marks (Descending)     :", marks)

marks.append(88)
print("• After Adding New Marks        :", marks)

marks.remove(45)
print("• After Removing Failed Marks   :", marks)

marks.sort(reverse=True)
print("• Top 3 Marks                   :",marks[:3])
print("• Last 2 Marks                  :",marks[-2:])
print("• Total Subjects Count          :",len(marks))

print("\nFinal Marks List              :", marks)
print("=" * 70)

# Q9 — Website Visitors Record

print("=" * 70)
print(" \t\t  WEBSITE VISITORS RECORD")
print("=" * 70)

visitors = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]

print("\nOriginal Collection:", visitors)
print("-" * 70)

print("• First Visitor               :", visitors[0])
print("• Last Visitor                :", visitors[-1])

visitors.append("Bilal")
print("• After Adding New Visitor    :", visitors)

visitors.insert(2, "Raza")
print("• After Inserting Visitor     :", visitors)

visitors.remove("Ahmed")
print("• After Removing Ahmed        :", visitors)

visitors.pop()
print("• After Remove Last Visitor   :", visitors)

print("• First 3 Visitors            :", visitors[:3])
print("• Last 3 Visitors             :", visitors[-3:])

visitors.reverse()
print("• Reversed Visitors List      :", visitors)

print("• Total Visitors              :", len(visitors))

print("\nFinal Visitors List:", visitors)
print("=" * 70)

# Q10 — Programming Languages System

print("=" * 70)
print(" \t\t  PROGRAMMING LANGUAGES SYSTEM")
print("=" * 70)

languages = ["Python", "JavaScript", "Java", "C++", "PHP"]

print("\nOriginal Collection:", languages)
print("-" * 70)

print("• First Language              :", languages[0])
print("• Last Language (Negative)    :", languages[-1])

languages[4] = "TypeScript"
print("• After Replacing PHP         :", languages)

languages.append("Go")
print("• After Adding Go             :", languages)

languages.insert(2, "Rust")
print("• After Inserting Rust        :", languages)

languages.remove("Java")
print("• After Removing Java         :", languages)

print("• First 4 Languages           :", languages[:4])

print("• Last 2 Languages            :", languages[-2:])

languages.sort()
print("• Sorted Alphabetically       :", languages)

languages.reverse()
print("• Reversed Languages List     :", languages)

print("\nFinal Updated Languages List:", languages)
print("=" * 70)
