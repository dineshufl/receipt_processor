import uuid
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for receipts and points
receipts = {}

def calculate_points(receipt):
    points = 0
    retailer = receipt['retailer']
    total = float(receipt['total'])
    items = receipt['items']
    purchase_date = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d')
    purchase_time = datetime.strptime(receipt['purchaseTime'], '%H:%M')

    # Rule 1: One point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in retailer)

    # Rule 2: 50 points if the total is a round dollar amount with no cents
    if total.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items on the receipt
    points += (len(items) // 2) * 5

    # Rule 5: Points for item description length multiple of 3
    for item in items:
        description_len = len(item['shortDescription'].strip())
        if description_len % 3 == 0:
            item_price = float(item['price'])
            points += int(item_price * 0.2 + 0.9999)  # round up

    # Rule 6: 6 points if the day of the purchase is odd
    if purchase_date.day % 2 != 0:
        points += 6

    # Rule 7: 10 points if the time of purchase is between 2:00pm and 4:00pm
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    receipt = request.json
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    
    # Store the points in-memory using receipt_id as the key
    receipts[receipt_id] = points

    return jsonify({"id": receipt_id})

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    points = receipts.get(receipt_id)
    if points is not None:
        return jsonify({"points": points})
    else:
        return jsonify({"error": "Receipt not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
