import os

# Define the folder path and CSV content
folder_path = "data"
file_path = os.path.join(folder_path, "transactions.csv")

csv_data = """transaction_id,date,merchant,amount,type,status,description
T001,2026-01-01,Swiggy,450,UPI,Success,Food delivery
T002,2026-01-02,Amazon,1200,UPI,Success,Shopping
T003,2026-01-03,Uber,350,UPI,Success,Travel
T004,2026-01-04,Netflix,649,UPI,Success,Entertainment
T005,2026-01-05,BigBasket,850,UPI,Success,Grocery
T006,2026-01-06,Electricity Board,2300,UPI,Success,Electricity bill
T007,2026-01-07,Swiggy,700,UPI,Success,Food delivery
T008,2026-01-08,Amazon,2500,UPI,Success,Shopping"""

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Write the data to the file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(csv_data)

print(f"File successfully created at: {file_path}")