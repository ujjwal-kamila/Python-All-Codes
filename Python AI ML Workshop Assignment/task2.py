# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Step 1: Read the Dataset
url = 'https://drive.google.com/uc?export=download&id=16aBn3PDrhFJlWs7cT1AuxW5-uu289Akb'
df = pd.read_csv(url)

# Step 2: Perform Exploratory Data Analysis (EDA)
print(df.info())
print(df.describe())

# Scatter plot between 'Time on App' and 'Yearly Amount Spent'
sns.scatterplot(x='Time on App', y='Yearly Amount Spent', data=df)
plt.title('Time on App vs Yearly Amount Spent')
plt.show()

# Scatter plot between 'Time on Website' and 'Yearly Amount Spent'
sns.scatterplot(x='Time on Website', y='Yearly Amount Spent', data=df)
plt.title('Time on Website vs Yearly Amount Spent')
plt.show()

# Scatter plot between 'Length of Membership' and 'Yearly Amount Spent'
sns.scatterplot(x='Length of Membership', y='Yearly Amount Spent', data=df)
plt.title('Length of Membership vs Yearly Amount Spent')
plt.show()

# Step 3: Train-Test Split the Dataset
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Model using Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Display the Model Performance Score
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
