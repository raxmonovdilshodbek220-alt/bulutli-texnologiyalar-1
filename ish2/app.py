from decimal import Decimal, InvalidOperation
from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')

@app.get('/health')
def health():
    return {'holat': 'ishlayapti'}, 200

@app.post('/hisobla')
def hisobla():
    data = request.get_json(silent=True) or {}
    try:
        narx = Decimal(str(data['narx']))
        miqdor = int(data['miqdor'])
        if not narx.is_finite() or narx < 0 or miqdor < 1:
            raise ValueError
    except (KeyError, ValueError, TypeError, InvalidOperation):
        return jsonify({'xato': 'Narx nol yoki undan katta, miqdor esa kamida 1 bo‘lishi kerak.'}), 400
    return jsonify({'narx': str(narx), 'miqdor': miqdor,
                    'jami': str(narx * miqdor), 'valyuta': 'UZS'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '8080')))

