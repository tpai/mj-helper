# type: ignore
import os
import hu_result
from flask import Flask, jsonify, request

api = Flask(__name__)

@api.route('/', methods=['GET'])
def root():
    return jsonify({ 'status': 0 })

@api.route('/hu', methods=['POST'])
def hu():
    p = request.json
    is_hu = hu_result.hu(p['mj'], p['getmj'])
    return jsonify({ 'hu': is_hu })

@api.route('/hu_tai', methods=['POST'])
def hu_tai():
    p = request.json
    result = hu_result.hu_result(
      p['mj'],
      p['dmj'], 0, 1, [], -1, -1, False, None, 0,
      p['getmj'],
      False, False, False
    )
    print(result.table)
    return jsonify({ 'tai': result.table })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    api.run(host='0.0.0.0', port=port)
