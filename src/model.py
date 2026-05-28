import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("data.csv")

# Features and labels
X = df[
    [
        "session_length",
        "articles_read",
        "comments_posted",
        "subscription_status"
    ]
]

y = df["user_type"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print(classification_report(y_test, y_pred))

# SAVE MODEL
joblib.dump(model, "model.pkl")

print("model.pkl created successfully")
