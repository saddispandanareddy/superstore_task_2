import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# CREATE IMAGES FOLDER (AUTO)
# -------------------------------
os.makedirs('../images', exist_ok=True)

# -------------------------------
# LOAD CLEANED DATA
# -------------------------------
df = pd.read_csv('../data/cleaned_superstore.csv')

sns.set(style="whitegrid")

# -------------------------------
# 1. Sales by Category
# -------------------------------
plt.figure()
sns.barplot(x='category', y='sales', data=df, estimator=sum)
plt.title("Sales by Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('../images/sales_by_category.png')
plt.show()

# -------------------------------
# 2. Sales by Region
# -------------------------------
plt.figure()
sns.barplot(x='region', y='sales', data=df, estimator=sum)
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig('../images/sales_by_region.png')
plt.show()

# -------------------------------
# 3. Profit Distribution
# -------------------------------
plt.figure()
sns.histplot(df['profit'], bins=30, kde=True)
plt.title("Profit Distribution")
plt.tight_layout()
plt.savefig('../images/profit_distribution.png')
plt.show()

# -------------------------------
# 4. Top 5 Sub-Categories
# -------------------------------
top_sub = df.groupby('sub_category')['sales'].sum().nlargest(5).reset_index()

plt.figure()
sns.barplot(x='sales', y='sub_category', data=top_sub)
plt.title("Top 5 Sub-Categories by Sales")
plt.tight_layout()
plt.savefig('../images/top_subcategories.png')
plt.show()

print(" EDA plots generated and saved in 'images/' folder")