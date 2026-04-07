import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46],
    'Salary': [30000, 40000, 80000, 110000, 90000],
    'Purchased': [0, 1, 1, 0, 1]
})

X = data[['Age', 'Salary']]
y = data['Purchased']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(X_train)
print(y_train)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)

# 1️⃣ Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 2️⃣ Create a sample dataset
data = {
    'Size': [750, 800, 1200, 1500, 1800, 2000, 2200],
    'Bedrooms': [2, 2, 3, 3, 4, 4, 5],
    'Price': [150000, 160000, 200000, 240000, 280000, 300000, 350000]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# 3️⃣ Define features and target
X = df[['Size', 'Bedrooms']]  # features
y = df['Price']               # target

# 4️⃣ Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5️⃣ Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6️⃣ Predict on test data
y_pred = model.predict(X_test)

# 7️⃣ Show predictions
print("\nPredicted Prices:", y_pred)

# 8️⃣ Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R^2 Score:", r2)
