# Kaggle-dataset
Here's a step-by-step guide on how to connect to Kaggle and download the dataset from the given link.



### Step-by-Step Guide to Download the Dataset from Kaggle

1. **Set Up Your Kaggle Account**  
   - Visit [Kaggle's website](https://www.kaggle.com) and create an account if you don’t already have one.  
   - Once logged in, navigate to your account settings by clicking on your profile picture in the top-right corner and selecting **Account**.

2. **Generate and Download an API Token**  
   - In your Kaggle account settings, scroll to the **API** section.  
   - Click **Create New API Token**. This will download a `kaggle.json` file to your computer, which contains your API credentials.

3. **Install Kaggle Python Package**  
   - Make sure you have Python installed.  
   - Install the Kaggle package by running the following command:  
     ```bash
     pip install kaggle
     ```

4. **Set Up Your Kaggle API Credentials**  
   - Move the downloaded `kaggle.json` file to the `.kaggle` directory in your home folder. Use the following commands:  
     ```bash
     mkdir ~/.kaggle
     mv /path/to/kaggle.json ~/.kaggle/
     chmod 600 ~/.kaggle/kaggle.json
     ```
     Replace `/path/to/kaggle.json` with the actual path to the file.

5. **Verify Your Kaggle API Setup**  
   - Run the following command to test your Kaggle API setup:  
     ```bash
     kaggle datasets list
     ```

6. **Download the Dataset**  
   - Use the Kaggle API to download the dataset. Navigate to the dataset page [here](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales).  
   - Run the following command to download the dataset:  
     ```bash
     kaggle datasets download -d aungpyaeap/supermarket-sales
     ```
   - This will download a `.zip` file to your current working directory.

7. **Extract the Dataset**  
   - Extract the `.zip` file using the following command:  
     ```bash
     unzip supermarket-sales.zip
     ```

8. **Load the Dataset into Your Project**  
   - The dataset files (e.g., CSV files) are now ready for use. You can load the data using Python's `pandas` library:  
     ```python
     import pandas as pd
     data = pd.read_csv('supermarket_sales.csv')
     print(data.head())
     ```

