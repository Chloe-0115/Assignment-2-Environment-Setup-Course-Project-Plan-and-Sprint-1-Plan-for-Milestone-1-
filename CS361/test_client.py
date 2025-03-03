import requests
import os

URL = "http://127.0.0.1:5000/generate-pdf"
OUTPUT_FILE = "test_report.pdf"

# Sample JSON data to test the microservice
json_data = {
    "user_name": "John Doe",
    "report_period": "January 2025",
    "total_income": 5000,
    "total_expenses": 3200,
    "savings_goal": 1000,
    "net_savings": 1800,
    "progress_to_goal": 800,
    "detailed_transactions": [
        {"amount": 2000, "category": "income", "date": "2025-01-05", "description": "Salary"},
        {"amount": 100, "category": "expense", "date": "2025-01-10", "description": "Groceries"},
        {"amount": 500, "category": "expense", "date": "2025-01-15", "description": "Rent"}
    ]
}

def test_microservice():
    print("Sending request to microservice...")
    try:
        response = requests.post(URL, json=json_data)
        if response.status_code == 200:
            print("Response received successfully!")
            with open(OUTPUT_FILE, "wb") as f:
                f.write(response.content)
            print(f"PDF report generated and saved as {OUTPUT_FILE}")
        else:
            print(f"Failed to generate PDF. Status code: {response.status_code}")
            print("Response content:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to microservice: {e}")

if __name__ == '__main__':
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        print(f"Old file '{OUTPUT_FILE}' removed.")
    test_microservice()
    if os.path.exists(OUTPUT_FILE):
        print("Test completed successfully.")
    else:
        print("Test failed. No PDF file generated.")
