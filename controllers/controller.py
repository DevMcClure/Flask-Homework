from app import app
from flask import render_template
from models.order_list import orders
@app.route('/')
def index():
    return "Game Shop Orders"


@app.route('/orders')
def get_orders():
    return render_template('index.html', title="Order list",orders = orders)