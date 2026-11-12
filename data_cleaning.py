
import pandas as pd
import numpy as np

# Step 1: Create raw dataset
data = {
    'Name': ['Ravi', 'Kumar', 'Ravi', 'Priya', 'Arun',
             'John', 'Kumar'],
    'Age': [20, 21, 20, np.nan, 22, 23, 21],
    'Marks': [85, 90, 85, 95, np.nan, 78, 90],
    'City': ['Chennai', 'chennai', 'Chennai',
             'Coimbatore', 'CHENNAI', 'coimbatore', 'chennai']
}

df = pd.DataFrame(data)

# Save raw dataset
df.to_csv('raw_data.csv', index=False)

print("Original Dataset:")
print(df)

# Step 2: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Remove duplicate records
df = df.drop_duplicates()

# Step 4: Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Marks'] = df['Marks'].fillna(df['Marks'].median())

# Step 5: Correct inconsistent formats
df['Name'] = df['Name'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()

# Step 6: Convert data types
df['Age'] = df['Age'].astype(int)
df['Marks'] = df['Marks'].astype(float)

# Step 7: Structural validation
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

# Step 8: Validate values
print("\nAge Validation:")
print(df['Age'].between(1, 100).all())

print("\nMarks Validation:")
print(df['Marks'].between(0, 100).all())

# Step 9: Save cleaned dataset
df.to_csv('cleaned_data.csv', index=False)

print("\nFinal Cleaned Dataset:")
print(df)

print("\nData Cleaning Completed Successfully!")

