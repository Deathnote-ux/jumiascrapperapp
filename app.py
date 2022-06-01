from flask import Flask, render_template, request
from scraper import *


app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/result', methods=["POST"])
def show_result():
  item = request.form['item']
  min_price = int(request.form['min_prc'])
  max_price = int(request.form['max_prc'])
  type = ''
  if item == 'phones':
    get_phones(min_price, max_price)
    type = 'Phones'
    
  else:
    get_electronics(min_price, max_price)
    type = 'Electronics'

  return render_template('product_index.html', type=type)
    

if __name__ == "__main__":
  app.run(debug=True)