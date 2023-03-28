from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
input_data = db['input_data']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        family_name = request.form['family_name']
        birthday = request.form['birthday']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        username = request.form['username']
        phone_number = request.form['phone_number']
        email_address = request.form['email_address']

        input_data.insert_one({
            'name': name,
            'family_name': family_name,
            'birthday': birthday,
            'country': country,
            'city': city,
            'address': address,
            'username': username,
            'phone_number': phone_number,
            'email_address': email_address
        })
    data = input_data.find()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
