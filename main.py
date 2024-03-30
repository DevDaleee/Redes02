from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def factorial(n):
    return math.factorial(n)

def permutation(n, r):
    return math.perm(n, r)

def combination(n, r):
    return math.comb(n, r)

def arrangement(n, r):
    return math.perm(n, r)

@app.route('/factorial')
def calc_factorial():
    n = int(request.args.get('n'))
    result = factorial(n)
    return jsonify({'result': result})

@app.route('/permutation')
def calc_permutation():
    n = int(request.args.get('n'))
    r = int(request.args.get('r'))
    result = permutation(n, r)
    return jsonify({'result': result})

@app.route('/combination')
def calc_combination():
    n = int(request.args.get('n'))
    r = int(request.args.get('r'))
    result = combination(n, r)
    return jsonify({'result': result})

@app.route('/arrangement')
def calc_arrangement():
    n = int(request.args.get('n'))
    r = int(request.args.get('r'))
    result = arrangement(n, r)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
