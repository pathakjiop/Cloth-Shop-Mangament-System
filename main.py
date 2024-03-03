import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Function to create a connection to the MySQL database
def create_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Panda2005",
            database="clothing_shop_db"
        )
    except mysql.connector.Error as e:
        messagebox.showerror("Database Connection Error", str(e))
        return None

# Function to add a cloth to the database
def add_cloth(db_connection, name, size, price, quantity):
    cursor = db_connection.cursor()
    query = "INSERT INTO cloths (name, size, price, quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, size, price, quantity))
    db_connection.commit()
    cursor.close()
    messagebox.showinfo("Success", "Cloth added successfully.")

# Function to display all cloths in the database
def view_cloths(db_connection, text_widget):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM cloths")
    rows = cursor.fetchall()
    cursor.close()
    
    text_widget.delete('1.0', tk.END)  # Clear the text widget first
    text_widget.insert(tk.END, "{:<5} {:<30} {:<10} {:<10} {:<10}\n".format('ID', 'Name', 'Size', 'Price', 'Quantity'))
    for row in rows:
        text_widget.insert(tk.END, "{:<5} {:<30} {:<10} {:<10} {:<10}\n".format(*row))

# Function to allow a user to buy a cloth
def buy_cloth(db_connection, cloth_id, quantity):
    cursor = db_connection.cursor()
    cursor.execute("SELECT quantity FROM cloths WHERE id = %s", (cloth_id,))
    result = cursor.fetchone()
    
    if result and result[0] >= quantity:
        new_quantity = result[0] - quantity
        update_query = "UPDATE cloths SET quantity = %s WHERE id = %s"
        cursor.execute(update_query, (new_quantity, cloth_id))
        db_connection.commit()
        messagebox.showinfo("Success", f"You bought {quantity} of cloth ID {cloth_id}.")
    else:
        messagebox.showerror("Error", "Not enough stock or cloth not found.")
    cursor.close()

# Function to remove a cloth from the database
def remove_cloth(db_connection, cloth_id):
    cursor = db_connection.cursor()
    query = "DELETE FROM cloths WHERE id = %s"
    cursor.execute(query, (cloth_id,))
    db_connection.commit()
    cursor.close()
    messagebox.showinfo("Success", "Cloth removed successfully.")

# Main GUI application class
class ClothShopApp(tk.Tk):
    def __init__(self):  # Corrected from `def __init__(root):` to `def __init__(self):`
        super().__init__()
        self.title("Cloth Shop Management System")
        self.geometry("800x600")

        # Create a database connection
        self.db_connection = create_connection()
        if not self.db_connection:
            self.destroy()
            return

        # Setup the notebook (tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Add Cloth Tab
        self.add_tab = tk.Frame(self.notebook)
        self.notebook.add(self.add_tab, text="Add Cloth")

        # Input fields for Add Cloth
        tk.Label(self.add_tab, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.add_tab)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.add_tab, text="Size:").grid(row=1, column=0)
        self.size_entry = tk.Entry(self.add_tab)
        self.size_entry.grid(row=1, column=1)

        tk.Label(self.add_tab, text="Price:").grid(row=2, column=0)
        self.price_entry = tk.Entry(self.add_tab)
        self.price_entry.grid(row=2, column=1)

        tk.Label(self.add_tab, text="Quantity:").grid(row=3, column=0)
        self.quantity_entry = tk.Entry(self.add_tab)
        self.quantity_entry.grid(row=3, column=1)

        tk.Button(self.add_tab, text="Add Cloth", command=self.on_add_cloth).grid(row=4, columnspan=2)

        # View Cloths Tab
        self.view_tab = tk.Frame(self.notebook)
        self.notebook.add(self.view_tab, text="View Cloths")
        self.cloths_text = tk.Text(self.view_tab, height=15, width=70)
        self.cloths_text.pack(side="left", fill="y")
        scrollbar = tk.Scrollbar(self.view_tab, command=self.cloths_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.cloths_text['yscrollcommand'] = scrollbar.set
        tk.Button(self.view_tab, text="Refresh List", command=self.on_view_cloths).pack()

        # Buy Cloth Tab
        self.buy_tab = tk.Frame(self.notebook)
        self.notebook.add(self.buy_tab, text="Buy Cloth")
        tk.Label(self.buy_tab, text="Cloth ID:").grid(row=0, column=0)
        self.buy_id_entry = tk.Entry(self.buy_tab)
        self.buy_id_entry.grid(row=0, column=1)

        tk.Label(self.buy_tab, text="Quantity:").grid(row=1, column=0)
        self.buy_quantity_entry = tk.Entry(self.buy_tab)
        self.buy_quantity_entry.grid(row=1, column=1)

        tk.Button(self.buy_tab, text="Buy Cloth", command=self.on_buy_cloth).grid(row=2, columnspan=2)

        # Remove Cloth Tab
        self.remove_tab = tk.Frame(self.notebook)
        self.notebook.add(self.remove_tab, text="Remove Cloth")
        tk.Label(self.remove_tab, text="Cloth ID:").grid(row=0, column=0)
        self.remove_id_entry = tk.Entry(self.remove_tab)
        self.remove_id_entry.grid(row=0, column=1)

        tk.Button(self.remove_tab, text="Remove Cloth", command=self.on_remove_cloth).grid(row=1, columnspan=2)

    # Event handlers for GUI buttons
    def on_add_cloth(self):
        name = self.name_entry.get()
        size = self.size_entry.get()
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price and quantity must be numbers.")
            return
        add_cloth(self.db_connection, name, size, price, quantity)

    def on_view_cloths(self):
        view_cloths(self.db_connection, self.cloths_text)

    def on_buy_cloth(self):
        try:
            cloth_id = int(self.buy_id_entry.get())
            quantity = int(self.buy_quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Cloth ID and quantity must be integers.")
            return
        buy_cloth(self.db_connection, cloth_id, quantity)

    def on_remove_cloth(self):
        try:
            cloth_id = int(self.remove_id_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Cloth ID must be an integer.")
            return
        remove_cloth(self.db_connection, cloth_id)

if __name__ == "__main__":
    app = ClothShopApp()
    app.mainloop()
