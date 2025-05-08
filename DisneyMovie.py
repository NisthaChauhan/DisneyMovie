import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Nistha\NetflixMovie\disney_plus_titles.csv")  # Change this to your file path

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('No Cast')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('NR')
df['duration'] = df['duration'].fillna('0')
    
# Feature Engineering
df['duration_numeric'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['added_year'] = df['date_added'].dt.year.fillna(0)
df['added_month'] = df['date_added'].dt.month.fillna(0)

# Encode categorical columns
df['type_encoded'] = df['type'].astype('category').cat.codes
df['rating_encoded'] = df['rating'].astype('category').cat.codes
df['country_encoded'] = df['country'].astype('category').cat.codes

# Select features and target
features = ['duration_numeric', 'added_year', 'added_month', 'rating_encoded', 'country_encoded']
df = df.dropna(subset=features)  # Drop rows with NaNs in features

X = df[features]
y = df['type_encoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Evaluate
print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))

# Visualize tree
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=features, filled=True, class_names=['Movie', 'TV Show'])
plt.title("Netflix Content Decision Tree")
plt.show()
