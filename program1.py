import numpy as np


class LogisticRegression:
    def __init__(self, learning_rate=0.1, iterations=10000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = 0.0

    def sigmoid(self, z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        X = np.asarray(X, dtype=float).reshape(-1, 1)
        y = np.asarray(y, dtype=float).reshape(-1, 1)

        n_samples, n_features = X.shape
        self.weights = np.zeros((n_features, 1))
        self.bias = 0.0

        for _ in range(self.iterations):
            # Calculate predicted probabilities
            z = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(z)

            # Calculate gradients
            dw = np.dot(X.T, (y_pred - y)) / n_samples
            db = np.sum(y_pred - y) / n_samples

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

        return self

    def predict(self, X):
        X = np.asarray(X, dtype=float).reshape(-1, 1)

        z = np.dot(X, self.weights) + self.bias
        probabilities = self.sigmoid(z)
        predictions = (probabilities >= 0.5).astype(int)

        return probabilities.flatten(), predictions.flatten()


# Dataset
X = np.array([0.50, 1.50, 2.00, 4.25, 3.25, 5.50])
y = np.array([0, 0, 0, 1, 1, 1])

# Create and train the model
model = LogisticRegression(learning_rate=0.1, iterations=10000)
model.fit(X, y)

print("Logistic Regression Model")
print("Weights:", model.weights.flatten())
print("Bias:", model.bias)

# Predict for a new input
new_value = 2.7
probability, prediction = model.predict([new_value])

print("\nInput value:", new_value)
print("Probability of class 1:", round(probability[0], 4))
print("Predicted class:", prediction[0])
print("Class:", "1" if prediction[0] == 1 else "0")