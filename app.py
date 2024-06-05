from flask import Flask, render_template, request
import math

app = Flask(__name__)




@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':

        loan_amount = float(request.form.get('loan_amount'))
        interest_rate = int(request.form.get('interest_rate'))
        loan_term = int(request.form.get('loan_term'))

        monthly_payment = calculate_mortgage_payment(loan_amount, interest_rate, loan_term)

        answer = f"Monthly payment: ${monthly_payment:.2f}"  # Округляем до двух знаков после запятой
        return render_template('index.html', ans=answer, val=loan_amount)

    return render_template('index.html')
def calculate_mortgage_payment(loan_amount, interest_rate, loan_term):


    monthly_interest_rate = interest_rate / 1200

    loan_term_months = loan_term * 12

    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / ((1 + monthly_interest_rate) ** loan_term_months - 1)

    return monthly_payment

@app.route('/hello')
def hello():
    return render_template("hello.html");


if __name__ == '__main__':
    app.run(debug=True)