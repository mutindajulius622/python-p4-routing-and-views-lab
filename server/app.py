#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text


@app.route('/count/<int:count>')
def count(count):
    output = '\n'.join(str(i) for i in range(count))
    if output:
        output = output + '\n'
    return output


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Unknown operation'
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
