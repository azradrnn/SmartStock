import joblib


# Load the trained model
model = joblib.load("smartstock_model.pkl")


print("=" * 50)
print("          SMARTSTOCK - INVENTORY PLANNING")
print("=" * 50)


# Get the sales data from the last 6 weeks
print("\nEnter the sales amounts for the last 6 weeks.")

sales = []

for week in range(1, 7):

    value = int(input(f"Week {week} sales: "))

    sales.append(value)


# Get the current stock amount

current_stock = int(input("\nCurrent stock amount: "))


# Calculate the trend for the model

model_trend = sales[-1] - sales[0]


# Create the features for the model

features = sales + [model_trend]


# Predict sales for the next week

prediction = model.predict([features])[0]

prediction = max(0, round(prediction))


# Analyze the recent sales trend

# Get the last 4 weeks
recent_sales = sales[-4:]


# Calculate the changes between weeks

changes = []

for i in range(1, len(recent_sales)):

    change = recent_sales[i] - recent_sales[i - 1]

    changes.append(change)


# Count the increases and decreases

positive_changes = sum(change > 0 for change in changes)
negative_changes = sum(change < 0 for change in changes)


# Find the highest and lowest sales in the last 4 weeks

max_recent = max(recent_sales)
min_recent = min(recent_sales)


# Calculate the sales range

variation = max_recent - min_recent


# Calculate the average sales for the last 4 weeks

recent_average = sum(recent_sales) / len(recent_sales)


# Compare the sales range with the average

variation_ratio = variation / recent_average if recent_average != 0 else 0


# Decide the sales trend

if variation_ratio > 0.60:

    trend_message = "↔️ Sales have been changing a lot."

elif positive_changes >= 2 and positive_changes > negative_changes:

    trend_message = "📈 Sales have been increasing in recent weeks."

elif negative_changes >= 2 and negative_changes > positive_changes:

    trend_message = "📉 Sales have been decreasing in recent weeks."

else:

    trend_message = "↔️ There is no clear sales trend."


# Calculate the safety stock

safety_stock = round(prediction * 0.20)


# Calculate the total stock needed

total_need = prediction + safety_stock


# Calculate the recommended order amount

recommended_order = max(0, total_need - current_stock)


# Show the results

print("\n" + "=" * 50)
print("                  RESULTS")
print("=" * 50)

print(f"\nPredicted sales for next week: {prediction} units")

print(f"Current stock: {current_stock} units")

print(f"\n{trend_message}")

print(f"Average sales in the last 4 weeks: {recent_average:.1f} units")

print(f"Sales range in the last 4 weeks: {min_recent} - {max_recent} units")

print(f"\nSafety stock: {safety_stock} units")

print(f"Total stock needed: {total_need} units")

print(f"\n Recommended order: {recommended_order} units")

print("\n" + "=" * 50)