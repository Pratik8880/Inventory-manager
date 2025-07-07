from flask import render_template, request, redirect
from util.db_util import query_db, execute_db

def show_suppliers():
    suppliers = query_db("SELECT * FROM suppliers")
    return render_template("suppliers.html", suppliers=suppliers)

def add_supplier():
    if request.method == 'POST':
        name = request.form['name']
        contact_info = request.form.get('contact_info', '')

        execute_db("INSERT INTO suppliers (name, contact_info) VALUES (%s, %s)", (name, contact_info))
        return redirect('/suppliers')
    
    return render_template("add_supplier.html")
