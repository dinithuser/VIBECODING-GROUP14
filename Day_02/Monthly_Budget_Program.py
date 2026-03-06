# Monthly Budget Program

# Ask the user for their total monthly budget
budget = float(input("Enter your total monthly budget: "))

# Collect expenses until user types 'done'
expenses = []
count = 1
while True:
    entry = input(f"Enter expense #{count} (or type 'done' to finish): ")
    if entry.strip().lower() == 'done':
        break
    try:
        expense = float(entry)
    except ValueError:
        print("Please enter a valid number or 'done'.")
        continue
    expenses.append(expense)
    count += 1

# Calculate remaining balance
remaining = budget - sum(expenses)

# Display the remaining balance
print(f"Remaining balance after expenses: ${remaining:.2f}")

# Warning for low funds
if remaining < 500:
    print("Warning: Low Funds")
