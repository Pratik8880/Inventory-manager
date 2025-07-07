from flask import Blueprint
from controllers.supplier_controller import show_suppliers, add_supplier

supplier_routes = Blueprint('suppliers', __name__)


@supplier_routes.route('/suppliers')  #defining route to connect with show supplier controller 
def suppliers():
    return show_suppliers()

@supplier_routes.route('/suppliers/add', methods=['GET', 'POST']) #defining route to get to the add supplier controller 
def add():
    return add_supplier()