from flask import Flask, render_template, request
import webbrowser
from threading import Timer

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/auto_submit', methods=['POST'])
def get_info():
    global user_input_data, dropdown1_data, dropdown2_data
    user_input_data = request.form.get('user_input', '')
    dropdown1_data = request.form.get('dropdown1', '')
    dropdown2_data = request.form.get('dropdown2', '')
    return f'Key Ingredient: {user_input_data}, Meal Type: {dropdown1_data}, Key Flavor: {dropdown2_data}'


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)
