import csv
import tabula
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

def convert_pdfs_to_csv(pdfs):
    csv_data = []
    for pdf in pdfs:
        tabula.convert_into(pdf, 'converted.csv', output_format="csv",
                            pages="all", area=(80, 30, 1080, 810))
        csv_data.append(pd.read_csv('converted.csv').values.tolist())
    return csv_data

@app.route('/', methods=['GET'])
def index():
    return 'Get - Working!'

@app.route('/convert', methods=['POST'])
def convert():
    pdfs = request.files.getlist('pdfs')
    csv_data = convert_pdfs_to_csv(pdfs)
    return jsonify({'data': csv_data})

if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('PORT', 8080)), host='0.0.0.0')
