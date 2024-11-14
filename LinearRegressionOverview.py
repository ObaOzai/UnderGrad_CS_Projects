"""

Linear Regression Overview

Linear regression is a statistical method used to model the relationship between a dependent 
variable (target) and one or more independent variables (features).

The goal is to find the best-fitting line (for simple linear regression with one feature) or
hyperplane (for multiple features) that minimizes the difference between the predicted and actual values.
Applications: Predictive analytics, trend analysis, economics, and machine learning.
Concept
The equation of a linear regression model can be written as:

y=mx+b
y: Predicted value (dependent variable)
x: Input feature (independent variable)
m: Slope of the line (weight)
b: Intercept (bias)
We want to minimize the Mean Squared Error (MSE) to find the best-fitting line:

MSE= 1/n ( n ∑ n (i-1) (yi1 - yi2)^2 )

y i : Actual value
y^i : Predicted value

Explanation of the Code

Generating Synthetic Data:
We generate 100 random data points for 
X between 0 and 2.

The target 
y is generated using the equation 
y=4+3x+noise.

Fitting the Linear Regression Model:
We use scikit-learn's LinearRegression class to fit the model to our data.
Making Predictions:
After fitting the model, we predict the values of 
y for our dataset.

Measuring Performance:
We calculate the Mean Squared Error (MSE) to evaluate the model’s accuracy.
We also measure the time taken to fit the model using time.time().
Plotting the Results:
We visualize the actual data points and the fitted regression line.

the code, you should see something like:

Estimated Coefficients: Slope = 3.0025, Intercept = 3.9123
Mean Squared Error: 0.9374
Time taken: 0.0062 seconds

Try adjusting the parameters for generating data (like slope, intercept, and noise) to see how it affects the fitted line.
Experiment with larger datasets to see how it impacts the model's performance and time taken.


"""

# Linear Regression with scikit-learn
# Astro Pema Software (c)
# Oba Ozai & ChatGPT4 Nov 2024

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import time

# Generate synthetic data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Features (100 random points between 0 and 2)
y = 4 + 3 * X + np.random.randn(100, 1)  # Linear relationship with noise

# Start timer
start_time = time.time()

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# End timer
end_time = time.time()

# Calculate Mean Squared Error
mse = mean_squared_error(y, y_pred)

# Print the results
print(f"Estimated Coefficients: Slope = {model.coef_[0][0]:.4f}, Intercept = {model.intercept_[0]:.4f}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"Time taken: {end_time - start_time:.4f} seconds")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Fitted Line')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# EOF




​	
 −
