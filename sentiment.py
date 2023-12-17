import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns


# Function to load the reviews into a DataFrame
def load_reviews(directory, sentiment):
    reviews = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                reviews.append(file.read())
    return pd.DataFrame({'review': reviews, 'sentiment': sentiment})

# Load all reviews
pos_reviews = load_reviews('/Users/nikhilpujari/Downloads/review_polarity/txt_sentoken/pos', 1)
neg_reviews = load_reviews('/Users/nikhilpujari/Downloads/review_polarity/txt_sentoken/neg', 0)

# Combine datasets
df = pd.concat([pos_reviews, neg_reviews], ignore_index=True)

# Preprocess the text (simple example)
df['review'] = df['review'].str.lower()  # Convert to lower case
df['review'] = df['review'].str.replace('[^\w\s]', '')  # Remove punctuation

# Create feature vectors using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict the sentiment on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))


# Assuming y_test and y_pred are the true labels and predicted labels respectively
cm = confusion_matrix(y_test, y_pred)

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
