
# Python Loops Assignment
# -----------------------------------------------------------
# Using While Loop

# ============================================================
# Question 1: Print Numbers from 1 to 100
# ============================================================

print("\n" + "=" * 60)
print("          PRINT NUMBERS FROM 1 TO 100")
print("=" * 60)

number = 1

while number <= 100:
    print(number)
    number += 1


# ============================================================
# Question 2: Print Numbers from 100 to 1
# ============================================================

print("\n" + "=" * 60)
print("          PRINT NUMBERS FROM 100 TO 1")
print("=" * 60)

number = 100

while number >= 1:
    print(number)
    number -= 1


# ============================================================
# Question 3: Print the Multiplication Table
# ============================================================

print("\n" + "=" * 60)
print("          Multiplication Table")
print("=" * 60)


number = int(input("Enter a number: "))

count = 1

while count <= 10:
    print(number ,"x" , count ,"=" ,number * count)
    count += 1


# ============================================================
# Question 4: Print All Elements of a List
# ============================================================

print("\n" + "=" * 60)
print("          PRINT ALL ELEMENTS OF A LIST")
print("=" * 60)

numbers = [12, 45, 8, 23, 67, 34, 90, 15, 56, 78]

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1


# ============================================================
# Question 5: Search a Number in a Tuple
# ============================================================

print("\n" + "=" * 60)
print("          SEARCH A NUMBER IN A TUPLE")
print("=" * 60)

numbers = (18, 45, 72, 91, 34, 56, 29, 83, 67, 10)

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
index = 0

while index < len(numbers):

    if numbers[index] == x:
        print("Element found at index", index)
        break

    index += 1
   
else:
    print("Number not found.")


# ============================================================
# Question 6: Find the Sum of First N Natural Numbers
# ============================================================

print("\n" + "=" * 60)
print("          FIND THE SUM OF FIRST N NATURAL NUMBERS")
print("=" * 60)

n = 10

total = 0
count = 1

while count <= n:
    total += count
    count += 1

print("Sum of first", n, "natural numbers is:", total)


# Using For Loop

# ============================================================
# QUESTION 1 : PRINT ALL ELEMENTS OF A LIST
# ============================================================

print("\n" + "=" * 60)
print("          PRINT ALL ELEMENTS OF A LIST")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes",
          "Peach", "Cherry", "Guava", "Pineapple", "Watermelon"]

for fruit in fruits:
    print(fruit)


# ============================================================
# QUESTION 2 : SEARCH A STRING IN A TUPLE
# ============================================================

print("\n" + "=" * 60)
print("          SEARCH A STRING IN A TUPLE")
print("=" * 60)

cities = ("Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta")

x = "Islamabad"

for city in cities:
    if city == x:
        print(x, "Found in the tuple")
        break


# ============================================================
# QUESTION 3 : FIND THE FACTORIAL OF A NUMBER
# ============================================================

print("\n" + "=" * 60)
print("          FIND THE FACTORIAL OF A NUMBER")
print("=" * 60)

number = 5
factorial = 1

numbers = (1, 2, 3, 4, 5)

for i in numbers:
    factorial = factorial * i

print("Factorial of", number, "is:", factorial)

# Using range()

# ============================================================
# Print Numbers from 1 to 100
# ============================================================

print("\n" + "=" * 60)
print("               PRINT NUMBERS FROM 1 TO 100")
print("=" * 60)

for number in range(1, 101):
    print(number)


# ============================================================
# Print Numbers from 100 to 1
# ============================================================

print("\n" + "=" * 60)
print("               PRINT NUMBERS FROM 100 TO 1")
print("=" * 60)

for number in range(100, 0, -1):
    print(number)


# ============================================================
# Print the Multiplication Table
# ============================================================

print("\n" + "=" * 60)
print("                 MULTIPLICATION TABLE")
print("=" * 60)

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)