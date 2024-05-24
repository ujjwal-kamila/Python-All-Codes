# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Read the dataset
df = pd.read_csv("Ecommerce Customers.csv")

# Display the first few rows of the dataset
print(df.head(4))

# Display information about the dataset
print(df.info())

# Display descriptive statistics of the dataset
print(df.describe())

# Drop unnecessary columns from the dataset
df = df.drop(['Email', 'Address', 'Avatar'], axis=1)

# Plot a scatter plot between 'Time on App' and 'Yearly Amount Spent'
plt.scatter(df['Time on App'], df['Yearly Amount Spent'])
plt.xlabel('Time on App')
plt.ylabel('Yearly Amount Spent')
plt.title('Relationship between Time on App and Yearly Amount Spent')
plt.show()

# Plot a scatter plot between 'Time on Website' and 'Yearly Amount Spent'
plt.scatter(df['Time on Website'], df['Yearly Amount Spent'])
plt.xlabel('Time on Website')
plt.ylabel('Yearly Amount Spent')
plt.title('Relationship between Time on Website and Yearly Amount Spent')
plt.show()

# Define features (X) and target variable (y)
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict the target variable on the testing set
y_pred = lr.predict(X_test)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
