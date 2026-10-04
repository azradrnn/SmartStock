import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


# Import the dataset
df = pd.read_csv("data/Sales_Transactions_Dataset_Weekly.csv")


# Set how many weeks of past sales to use
window_size = 6


# Create training and test data
x_train = []
y_train = []

x_test = []
y_test = []


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

        # Use the last 5 weeks for testing
        if i + window_size >= 36:

            x_test.append(features)
            y_test.append(target)

        else:

            x_train.append(features)
            y_train.append(target)


print("Training samples:", len(x_train))
print("Test samples:", len(x_test))


# 1. Gradient Boosting

gb_model = GradientBoostingRegressor(
    n_estimators=100,
    random_state=42
)

gb_model.fit(x_train, y_train)

gb_predictions = gb_model.predict(x_test)

gb_mae = mean_absolute_error(y_test, gb_predictions)
gb_r2 = r2_score(y_test, gb_predictions)


# 2. Random Forest

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(x_train, y_train)

rf_predictions = rf_model.predict(x_test)

rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)


# 3. Linear Regression 

linear_model = LinearRegression()

linear_model.fit(x_train, y_train)

linear_predictions = linear_model.predict(x_test)

linear_mae = mean_absolute_error(y_test, linear_predictions)
linear_r2 = r2_score(y_test, linear_predictions)


# Show the results

print("\nMODEL RESULTS")

print("\nGradient Boosting")
print("MAE:", gb_mae)
print("R²:", gb_r2)

print("\nRandom Forest")
print("MAE:", rf_mae)
print("R²:", rf_r2)

print("\nLinear Regression")
print("MAE:", linear_mae)
print("R²:", linear_r2)