import pandas as pd
import joblib

from sklearn.ensemble import GradientBoostingRegressor


# Load the dataset
df = pd.read_csv("data/Sales_Transactions_Dataset_Weekly.csv")


# Set how many weeks of past sales to use
window_size = 6


# Create the training data
x_train = []
y_train = []


for product_index in range(len(df)):

    sales = df.loc[
        product_index,
        "W0":"W40"
    ].astype(int).values

    for i in range(len(sales) - window_size):

        window = sales[i:i + window_size]
        target = sales[i + window_size]

        # Calculate the sales trend
        trend = window[-1] - window[0]

        # Use the 6 weeks of sales and the trend
        features = list(window) + [trend]

        # Do not use the last 5 weeks for training
        if i + window_size < 36:

            x_train.append(features)
            y_train.append(target)


print("Training samples:", len(x_train))


# Create the Gradient Boosting model
model = GradientBoostingRegressor(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(x_train, y_train)


print("Model trained.")


# Save the trained model
joblib.dump(model, "smartstock_model.pkl")


print("Model saved successfully.")