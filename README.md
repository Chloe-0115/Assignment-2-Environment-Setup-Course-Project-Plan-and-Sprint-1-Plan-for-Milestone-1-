# CS-361
This is a repository for CS 361.
Read Me for Assignment 8.

This microservice accepts a JSON payload with budget summary data via a RESTful API and generates a PDF report as the response. It is built using Python, Flask, and FPDF.

Key Features：

-Accepts JSON input with budget data

-Generates a well-formatted PDF report

-Simple RESTful API with POST request

How to Use the Microservice:

First, ensure you have installed the necessary dependencies:

pip install flask fpdf

Run the Flask server using the following command:

python app.py

You should see the server running at http://127.0.0.1:5000.

You can interact with the microservice using any HTTP client (e.g., Postman, curl, or custom Python scripts).

Expected Output:

-Upon a successful request, a PDF file (report.pdf) will be generated.

-Open the file to verify the data matches the input JSON.

Example API Request:

You can interact with the microservice using any HTTP client (e.g., Postman, curl, or custom Python scripts).
Example Request using Python.

[import requests

url = "http://127.0.0.1:5000/generate-pdf"
json_data = {...}  # Use the JSON payload as shown above

response = requests.post(url, json=json_data)

if response.status_code == 200:
    with open("report.pdf", "wb") as f:
        f.write(response.content)
    print("PDF report generated successfully!")
else:
    print(f"Failed to generate PDF. Status code: {response.status_code}")]
    

UML Sequence Diagram:

Below is the UML Sequence Diagram for the JSON to PDF Microservice:
![json_to_pdf_sequence_diagram](https://github.com/user-attachments/assets/b48b12f1-9bc4-49c2-aaf7-5c9cfa2cefdc)

This diagram demonstrates the interaction between the client, the microservice, and the PDF generator.

Additional Notes:

If you change the default port or host, please let your teammate know.

