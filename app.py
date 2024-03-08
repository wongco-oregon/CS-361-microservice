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


@app.route('/email_list', methods=['GET', 'POST'])
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
        msg = Message("Test", sender='enter your own email', recipients=[new_email])
        msg.body = f"Hello {new_name}. Your total for order number {new_id} is {new_total}. Thank you."
        mail.send(msg)
        return jsonify(invoice_email_list), 201 , 'Email delivered successfully'


@app.route('/email_list/<int:input_id>', methods=['GET', 'PUT', 'DELETE'])
def email_function(input_id):

    if request.method == 'GET':
        for item in invoice_email_list:
            if item['order_number'] == input_id:
                return jsonify(item), 201
        return 'Nothing Found', 404

    if request.method == 'PUT':
        for item in invoice_email_list:
            if item['order_number'] == input_id:
                item['order_email'] = request.form['order_email']
                item['order_name'] = request.form['order_name']
                item['order_total'] = request.form['order_total']
                new_entry = {
                    'order_number': item['order_number'],
                    'order_email': item['order_email'],
                    'order_name': item['order_name'],
                    'order_total': item['order_total']
                }

                return jsonify(new_entry), 201
        return 'Order number not found'

    if request.method == 'DELETE':

        if len(invoice_email_list) == 0:
            return 'No orders available'

        for index, item in enumerate(invoice_email_list):
            if item['order_number'] == input_id:
                invoice_email_list.pop(index)
                return jsonify(invoice_email_list), 201
        return 'Order number not found'


if __name__ == '__main__':
    app.run(debug=True)
