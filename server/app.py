from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_text(text):
    print(text)  
    return text

@app.route('/count/<int:number>')
def count_numbers(number):
    count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n' 
    print(count)
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operations(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return "Invalid operation or division by zero"

if __name__ == '__main__':
    app.run(debug=True)