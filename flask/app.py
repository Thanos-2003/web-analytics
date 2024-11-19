from flask import Flask, render_template,request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("greet.html")
@app.route("/form")
def greet():
    return render_template("hello.html")

@app.route("/hello",methods=["POST"])
def hello():
    return render_template("form.html",name=request.form.get("fullname"))

@app.route('/operation')
def operation():
    return render_template("operation.html")
@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = request.form.get("result")

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"

    return render_template('operation.html', result=result)


if __name__=='__main__':
    app.run(debug=True)