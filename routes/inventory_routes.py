from flask import Blueprint
from controllers.inventory_controller import show_inventory, add_product, edit_product

inventory_routes = Blueprint('inventory', __name__)


@inventory_routes.route('/inventory') #route for showwing inventory 
def inventory():
    return show_inventory()

@inventory_routes.route('/inventory/add', methods=['GET', 'POST']) #route for adding into inventory 
def add():
    return add_product()

@inventory_routes.route('/inventory/edit/<int:id>', methods=['GET', 'POST']) #route for edit the inventory 
def edit(id):
    return edit_product(id)



