from app import create_app, db
from app.models import Product

app = create_app()

def seed_products():
    if Product.query.count() == 0:
        products = [
    Product(name='Laptop', price=75999.99, description='A powerful laptop', image_url='https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=300&h=180&fit=crop'),
    Product(name='Phone', price=29999.99, description='A sleek smartphone', image_url='https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=300&h=180&fit=crop'),
    Product(name='Headphones', price=4999.99, description='Noise cancelling headphones', image_url='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&h=180&fit=crop'),
    Product(name='Keyboard', price=2999.99, description='Mechanical keyboard', image_url='https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=300&h=180&fit=crop'),
]
        db.session.add_all(products)
        db.session.commit()
        print('Sample products added!')

with app.app_context():
    db.create_all()
    seed_products()

if __name__ == '__main__':
    app.run(debug=True)