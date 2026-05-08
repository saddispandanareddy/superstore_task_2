import pandas as pd

# Load dataset
data = pd.read_csv("data/SampleSuperstore.csv", encoding='latin1')

print("Initial Data:")
print(data.head())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove duplicates
data = data.drop_duplicates()

# Create new feature
data["Profit_Ratio"] = data["Profit"] / data["Sales"]

# Optional: basic stats (looks professional)
print("\nData Summary:")
print(data.describe())

# Save cleaned dataset
data.to_csv("outputs/cleaned_superstore.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")