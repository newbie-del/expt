import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# 1. Create the dataset
data = {
    "Marks": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    "Result": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

# 2. Create a DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 3. Separate features and target
X = df[["Marks"]]
y = df["Result"]

# 4. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5. Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Predict test data
y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(y_pred)

# 7. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# 8. Display confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("\nConfusion Matrix:")
print(cm)

# 9. Predict for a new student
new_marks = pd.DataFrame({"Marks": [58]})

prediction = model.predict(new_marks)

print("\nPrediction for Student with Marks = 58:")

if prediction[0] == 1:
    print("PASS")
else:
    print("FAIL")

# 10. Plot the data and logistic regression curve
plt.figure(figsize=(8, 5))

# Plot students who failed
plt.scatter(
    df.loc[df["Result"] == 0, "Marks"],
    df.loc[df["Result"] == 0, "Result"],
    color="red",
    marker="o",
    s=100,
    label="Fail"
)

# Plot students who passed
plt.scatter(
    df.loc[df["Result"] == 1, "Marks"],
    df.loc[df["Result"] == 1, "Result"],
    color="green",
    marker="x",
    s=100,
    label="Pass"
)

# Generate marks for the prediction curve
X_range = pd.DataFrame({
    "Marks": np.linspace(20, 85, 500)
})

# Probability of passing
y_prob = model.predict_proba(X_range)[:, 1]

# Plot logistic regression curve
plt.plot(
    X_range["Marks"],
    y_prob,
    color="blue",
    linewidth=2,
    label="Logistic Regression Curve"
)

# Decision boundary
plt.axhline(
    y=0.5,
    color="black",
    linestyle="--",
    label="Decision Boundary"
)

plt.xlabel("Marks")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression - Student Pass/Fail Prediction")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()