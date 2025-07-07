import os
from flask import Flask
from routes.user_routes import user_routes
from routes.inventory_routes import inventory_routes
from routes.supplier_routes import supplier_routes

app = Flask(__name__) #for session-based login
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev_secret')

app.register_blueprint(user_routes)
app.register_blueprint(inventory_routes)
app.register_blueprint(supplier_routes)

if __name__ == '__main__':
    app.run(debug=True)
