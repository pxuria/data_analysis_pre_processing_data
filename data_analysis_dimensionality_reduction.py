from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Step 1: Load cleaned dataset
data_cleaned = pd.read_excel("./output/Cleaned_AirQualityUCI.xlsx")

# Step 2: Drop non-numeric columns
data_numeric = data_cleaned.select_dtypes(include='number')

# Step 3: Normalize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_numeric)

# Step 4: Perform PCA
# Retain enough components to explain 95% of the variance
pca = PCA(n_components=0.95)  # Keep components explaining 95% variance
data_pca = pca.fit_transform(data_scaled)

# Create a DataFrame with reduced dimensions
pca_columns = [f"PC{i+1}" for i in range(data_pca.shape[1])]
data_reduced = pd.DataFrame(data_pca, columns=pca_columns)

# Step 5: Save the reduced data to Excel
output_pca_path = './output/Reduced_AirQualityUCI.xlsx'
data_reduced.to_excel(output_pca_path, index=False, engine='openpyxl')

# Step 6: Print explained variance ratio
explained_variance = pca.explained_variance_ratio_
print(f"Explained Variance Ratio for each component: {explained_variance}")
print(f"Total Variance Explained: {sum(explained_variance):.2f}")
print(f"Dimensionality reduced data saved to {output_pca_path}")
