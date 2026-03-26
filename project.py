expenses = []

print("💰 Welcome to Expense Tracker")

# Input section
while True:
    date = input("\nEnter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = float(input("Enter amount: ₹"))

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })

    choice = input("Add another expense? (y/n): ")
    if choice.lower() != 'y':
        break

# Analysis
total = sum(item["amount"] for item in expenses)

print("\n📊 Total Spending: ₹", total)

# Category-wise calculation
category_total = {}

for item in expenses:
    cat = item["category"]
    category_total[cat] = category_total.get(cat, 0) + item["amount"]

print("\n📂 Category-wise Spending:")
for cat, amt in category_total.items():
    print(f"{cat}: ₹{amt}")

# Highest spending category
max_category = max(category_total, key=category_total.get)
print(f"\n🔥 Highest spending category: {max_category}")

# Suggestion
if total > 2000:
    print("⚠️ Warning: You are spending too much!")
else:
    print("✅ Good job! Your spending is under control.")