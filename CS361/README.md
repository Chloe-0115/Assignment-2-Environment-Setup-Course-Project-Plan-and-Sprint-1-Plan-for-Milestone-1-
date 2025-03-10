# CS-361
This is a repository for CS 361.
Read Me for Assignment 8.

Overview

This microservice accepts a JSON payload containing budget summary data via a RESTful API and generates a well-formatted PDF report as the response. It is built using Python, Flask, and FPDF.

Key Features：

-Accepts JSON input with budget data

-Generates a well-formatted PDF report

-Provides a simple RESTful API with a POST request

-Returns a response indicating success or failure

Prerequisites

Before running the microservice, ensure that you have installed the necessary dependencies:
<img width="441" alt="image" src="https://github.com/user-attachments/assets/2a65773b-bfb9-4ac8-b527-0e9cbccf9e14" />


How to Use the Microservice:

Run the Flask server using the following command:

python app.py

You should see the server running at http://127.0.0.1:5000.

You can interact with the microservice using any HTTP client (e.g., Postman, curl, or custom Python scripts).

How to Use the Microservice

You can interact with the microservice using any HTTP client (e.g., Postman, curl, or a custom Python script).

Expected API Behavior

Endpoint: /generate-pdf

-Method: POST

-Content-Type: application/json

-Input: JSON object containing budget data

-Output: PDF file (as a downloadable response or stored locally)

-Response: JSON confirmation message with a status code

Input Format

The JSON payload should follow this structure:
<img width="417" alt="image" src="https://github.com/user-attachments/assets/f393c607-be77-427c-80ef-9c12e6e79a30" />

Example API Request

Using curl:
<img width="427" alt="image" src="https://github.com/user-attachments/assets/b1acc892-1dc9-48b5-a8d1-aba351b6a3b3" />

Response Format

Upon a successful request, the microservice returns:
<img width="394" alt="image" src="https://github.com/user-attachments/assets/80eacbd8-6026-4a25-bf78-89171bac6399" />
If an error occurs, an error response will be sent:
<img width="336" alt="image" src="https://github.com/user-attachments/assets/171ca454-bbb5-486c-b9a9-fc59c56cff7b" />

Example Code to Receive PDF Data (Python)
<img width="416" alt="image" src="https://github.com/user-attachments/assets/c38162a0-95c9-460e-ba4c-b44e5cb4eabf" />

UML Sequence Diagram:

Below is the UML Sequence Diagram for the JSON to PDF Microservice:
![output](https://github.com/user-attachments/assets/0586fedf-ecb6-48b2-a098-ef5b5522044d)


This diagram demonstrates the interaction between the client, the microservice, and the PDF generator.

Additional Notes:

If you change the default port or host, please let your teammate know.

