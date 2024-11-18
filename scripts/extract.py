import os
import subprocess
import zipfile

# Step 1: Ensure the Kaggle credentials are in the correct location
kaggle_json_path = os.path.expanduser("~/.kaggle/kaggle.json")
if not os.path.exists(kaggle_json_path):
    raise FileNotFoundError(f"Kaggle API key file not found at {kaggle_json_path}. Ensure it exists.")

# Step 2: Define the output folder and dataset name
output_folder = "data/raw"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Define the Kaggle dataset name
dataset_name = "aungpyaeap/supermarket-sales"

# Step 4: Define the Kaggle command
command = [
    "kaggle", "datasets", "download", "-d", dataset_name,
    "-p", output_folder, "--unzip"
]

# Step 5: Run the Kaggle command to download and extract the dataset
try:
    print(f"Downloading dataset '{dataset_name}' to '{output_folder}'...")
    subprocess.run(command, check=True)
    print(f"Dataset downloaded and extracted to '{output_folder}'.")

    # Step 6: Rename the downloaded file to "supermarket_sales from supermarket_sales - Sheet1"
    for filename in os.listdir(output_folder):
        if filename.endswith(".csv"):
            old_file = os.path.join(output_folder, filename)
            new_file = os.path.join(output_folder, "supermarket_sales.csv")
            os.rename(old_file, new_file)
            print(f"File renamed to '{new_file}'")
            break

except subprocess.CalledProcessError as e:
    print(f"Error while downloading the dataset: {e}")
    raise
except FileNotFoundError:
    print("The 'kaggle' CLI tool was not found. Ensure it is installed and accessible in your PATH.")
    raise
