# ============================================================
# Print the Length of a List
# ============================================================

print("\n" + "─" * 60)
print("            PRINT THE LENGTH OF A LIST")
print("─" * 60)

def list_length(items):
    print("Length of the list is:", len(items))

numbers = [10, 20, 30, 40, 50]

list_length(numbers)

# ============================================================
# Print All Elements of a List
# ============================================================

print("\n" + "─" * 60)
print("          PRINT ALL ELEMENTS OF A LIST")
print("─" * 60)

def print_list(items):
    for item in items:
        print(item)

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print_list(fruits)


# ============================================================
# Find the Factorial of a Number
# ============================================================

print("\n" + "─" * 60)
print("          FIND THE FACTORIAL OF A NUMBER")
print("─" * 60)

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    print("Factorial of", number, "is:", result)

factorial(5)

# ============================================================
# Convert PKR into USD
# ============================================================

print("\n" + "─" * 60)
print("             CONVERT PKR INTO USD")
print("─" * 60)

def convert_currency(pkr):
    usd = pkr / 280
    print("USD =", usd)

convert_currency(28000)

# ============================================================
# Check Even or Odd
# ============================================================

print("\n" + "─" * 60)
print("               CHECK EVEN OR ODD")
print("─" * 60)

def check_number(number):

    if number % 2 == 0:
        print(number, "is Even")

    else:
        print(number, "is Odd")

check_number(15)