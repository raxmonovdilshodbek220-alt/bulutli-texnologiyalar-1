from http.server import BaseHTTPRequestHandler
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

RATE = Decimal('0.12')  # O‘quv uchun qo‘yilgan misol stavkasi

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length < 1 or length > 4096:
                raise ValueError
            payload = json.loads(self.rfile.read(length).decode('utf-8'))
            amount = Decimal(str(payload.get('amount', '')))
            if not amount.is_finite() or amount < 0:
                raise ValueError
        except (ValueError, TypeError, InvalidOperation, json.JSONDecodeError):
            return self._send(400, {'error': 'Nol yoki undan katta son kiriting.'})

        tax = (amount * RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        total = amount + tax
        self._send(200, {
            'amount': float(amount), 'rate': float(RATE),
            'tax': float(tax), 'total': float(total)
        })

    def _send(self, status, data):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

