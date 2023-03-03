# import csv
# import tabula
# from flask import Flask, request, jsonify

# app = Flask(__name__)


# def convert_pdfs_to_csv(pdfs):
#     csv_data = []
#     for pdf in pdfs:
#         tabula.convert_into(pdf, 'converted.csv', output_format="csv",
#                             pages="all", area=(80, 30, 1080, 810))
#         with open('converted.csv', 'r') as file:
#             reader = csv.reader(file)
#             csvvalues = list(reader)
#             csv_data.append(csvvalues)
#     return csv_data


# @app.route('/', methods=['GET'])
# def index():
#     return 'Get - Working!'


# @app.route('/convert', methods=['POST'])
# def convert():
#     pdfs = request.files.getlist('pdfs')
#     csv_data = convert_pdfs_to_csv(pdfs)
#     return jsonify({'data': csv_data})


# if __name__ == '__main__':
#     app.run(debug=True)

import tabula
import pandas as pd

# Read the PDF file and extract the data to a DataFrame
df = tabula.read_pdf("my_pdf_file.pdf")

# Write the DataFrame to a CSV file
df.to_csv("my_csv_file.csv", index=False)
