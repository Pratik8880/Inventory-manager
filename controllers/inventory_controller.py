from flask import render_template, request, redirect
from util.db_util import query_db, execute_db

def show_inventory():
    products = query_db("SELECT * FROM products")
    return render_template("inventory.html", products=products)

def add_product():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        description = request.form.get('description', '')
        supplier_id = request.form.get('supplier_id') or None

        execute_db("INSERT INTO products (name, quantity, description, supplier_id) VALUES (%s, %s, %s, %s)",
                   (name, quantity, description, supplier_id))
        return redirect('/inventory')
    
    return render_template("add_product.html")

def edit_product(id):
    product = query_db("SELECT * FROM products WHERE id = %s", (id,), one=True)

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        description = request.form.get('description', '')
        supplier_id = request.form.get('supplier_id') or None

        execute_db("""
            UPDATE products
            SET name = %s, quantity = %s, description = %s, supplier_id = %s
            WHERE id = %s
        """, (name, quantity, description, supplier_id, id))

        return redirect('/inventory')

    return render_template("edit_product.html", product=product)
