# Inventory-manager
📦 Inventory Manager App 

A modular Flask application to manage products, suppliers, and users, backed by a MySQL database. 

 

# Project structure 

inventory_manager_app/  

|-app.py                                 #Main Flask app entry point (initializes app, loads routes, runs server) 

|-config.py                            # MySQL credentials and settings 

|-requirements.txt            # Lists Python dependencies (Flask, sqlite3) 

|-db/                                        # Contains raw SQL and DB-related scripts 

|--users.sql                       # SQL schema to create `users` table 

|--inventory.sql               # SQL schema to create `inventory` table 

|--suppliers.sql               # SQL schema to create `suppliers` table 

|--init_db.py                      # Script to run all SQL files and initialize the database 

|--database.db                # SQLite database file (auto-generated when `init_db.py` runs) 

|-routes/                                       # Maps HTTP URLs to controllers (views) 

|--user_routes.py                  # Handles `/login`, `/logout`, user-related URLs 

|--inventory_routes.py        # Handles `/inventory`, `/add-product`, `/edit-product` routes 

|--supplier_routes.py          # Handles `/suppliers` routes 

|-controllers/                                    # Contains business logic for each module 

|--user_controller.py              # Logic for login/logout, user validation 

|--inventory_controller.py    # Logic to view, add, edit, delete products 

|--supplier_controller.py      # Logic to view and manage suppliers 

|-templates/                                  # HTML templates for rendering UI 

|--layout.html                        # Base layout with navbar/footer and content block 

|--login.html                           # Login page for users 

|--dashboard.html              # Admin dashboard/home after login 

|--inventory.html                 # Page showing product list (inventory) 

|--add_product.html         # Form to add a new product 

|--edit_product.html         # Form to update/edit product details 

|--suppliers.html                # Page displaying all suppliers 

|-utils/                                             # Common utility functions (like DB access) 

|--db_util.py                          # Reusable functions for DB connection, query, insert, update, delete 

 

 

⚙️ Setup & Run 

# Install dependencies 

py -m pip install -r requirements.txt 

 

# Run the app 

bash 

python app.py 
 

 

# App will be live at: 

Browser 

http://127.0.0.1:5000/login 