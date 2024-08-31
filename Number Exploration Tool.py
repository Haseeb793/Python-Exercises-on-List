# Step 1: Get user's name and favorite numbers
name = input("Enter your name: ")

numbers = []
for i in range(3):
    number = int(input(f"Enter favorite number {i+1}: "))
    numbers.append(number)

# Step 2: Greet the user
print(f"\nHello, {name}! Thanks for sharing your favorite numbers with me.")

# Step 3: Determine if each number is even or odd
even_odd_list = []
for number in numbers:
    if number % 2 == 0:
        even_odd_list.append((number, "even"))
    else:
        even_odd_list.append((number, "odd"))

# Step 4: Print the square of each number
print("\nHere's something cool:")
for number in numbers:
    square = number ** 2
    print(f"The square of {number} is {square}.")

# Step 5: Calculate the sum of the numbers
total_sum = sum(numbers)
print(f"\nThe sum of your favorite numbers is {total_sum}.")

# Step 6: Check if the sum is a prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(total_sum):
    print(f"Wow! The sum {total_sum} is a prime number!")
else:
    print(f"The sum {total_sum} is not a prime number.")
