from flask import Flask, jsonify, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'enter your own email'
app.config['MAIL_PASSWORD'] = 'enter email password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
invoice_email_list = []


@app.route('/', methods=['GET', 'POST'])
def emails():
    if request.method == 'GET':
        if len(invoice_email_list) > 0:
            return jsonify(invoice_email_list)
        else:
            return 'Nothing Found', 404

    if request.method == 'POST':
        new_name = request.form['order_name']
        new_email = request.form['order_email']
        new_total = request.form['order_total']
        if len(invoice_email_list) == 0:
            new_id = 1
        else:
            new_id = invoice_email_list[-1]['order_number'] + 1

        new_entry = {
            'order_name': new_name,
            'order_email': new_email,
            'order_total': new_total,
            'order_number': new_id
        }

        invoice_email_list.append(new_entry)
        msg = Message("Test", sender='k76922045@gmail.com', recipients=[new_email])
        msg.body = f"Hello {new_name}. Your total for order number {new_id} is {new_total}. Thank you."
        mail.send(msg)
        return 'Email Sent Successfully'


if __name__ == '__main__':
    app.run(debug=True)
