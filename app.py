from flask import Flask, request, send_file, jsonify
from fpdf import FPDF
import json
import os

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Budget Summary Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Budget Summary for {data.get("user_name")}', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Report Period: {data.get("report_period")}', ln=True)
    pdf.ln(10)
    pdf.cell(0, 10, f'Total Income: ${data.get("total_income")}', ln=True)
    pdf.cell(0, 10, f'Total Expenses: ${data.get("total_expenses")}', ln=True)
    pdf.cell(0, 10, f'Savings Goal: ${data.get("savings_goal")}', ln=True)
    pdf.cell(0, 10, f'Net Savings: ${data.get("net_savings")}', ln=True)
    pdf.cell(0, 10, f'Progress to Goal: ${data.get("progress_to_goal")}', ln=True)
    pdf.ln(10)
    pdf.cell(0, 10, 'Detailed Transactions:', ln=True)
    pdf.ln(5)
    for transaction in data.get('detailed_transactions', []):
        pdf.cell(0, 10, f"{transaction['date']} - {transaction['description']} - {transaction['category']} - ${transaction['amount']}", ln=True)
    
    pdf_path = 'budget_summary_report.pdf'
    pdf.output(pdf_path)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
