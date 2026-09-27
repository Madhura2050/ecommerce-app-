from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models import Product
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    cart = list(session['cart'])
    cart.append(product_id)
    session['cart'] = cart
    session.modified = True
    
    return redirect(url_for('main.cart'))

@main.route('/cart')
def cart():
    cart = session.get('cart', [])
    products = Product.query.filter(Product.id.in_(cart)).all()
    return render_template('cart.html', products=products)

@main.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = list(session.get('cart', []))
    if product_id in cart:
        cart.remove(product_id)
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('main.cart'))