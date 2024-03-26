**Cloth Shop Management System**

**Introduction:**
This project is a Cloth Shop Management System developed using Python's Tkinter library for the GUI, MySQL for the database, and various functionalities for managing cloth inventory including adding, viewing, buying, and removing cloths.

**Features:**
1. **Add Cloth:** Allows users to add new cloths to the inventory by entering details such as name, size, price, and quantity.
2. **View Cloths:** Displays a list of all cloths in the inventory including their ID, name, size, price, and quantity.
3. **Buy Cloth:** Enables users to purchase cloths by specifying the cloth ID and the quantity they wish to buy. Checks for available stock before proceeding with the purchase.
4. **Remove Cloth:** Allows users to remove a cloth from the inventory by entering the cloth ID.

**Requirements:**
- Python 3.x
- Tkinter library
- MySQL
- mysql-connector-python library

**Installation and Setup:**
1. Clone the repository to your local machine.
   ```
   git clone <repository-url>
   ```
2. Install Python if not already installed. You can download it from [Python's official website](https://www.python.org/downloads/).
3. Install the required dependencies using pip:
   ```
   pip install mysql-connector-python
   ```
4. Set up a MySQL database:
   - Install MySQL on your machine if not already installed. You can download it from [MySQL's official website](https://dev.mysql.com/downloads/).
   - Create a new database named `clothing_shop_db`.
   - Create a table named `cloths` with columns `id` (auto-increment), `name`, `size`, `price`, and `quantity`.
5. Modify the database connection details in the script if necessary:
   ```python
   host="localhost",
   user="your_username",
   password="your_password",
   database="clothing_shop_db"
   ```
6. Run the script:
   ```
   python cloth_shop_management.py
   ```

**Usage:**
- Upon running the script, the GUI of the Cloth Shop Management System will open.
- Navigate through the tabs to perform various operations such as adding, viewing, buying, and removing cloths.
- Input necessary details in the fields and click on corresponding buttons to execute actions.
- View the list of available cloths and their details in the "View Cloths" tab.

**Contributing:**
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

**License:**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Authors:**
[Atharv Pathak] - Initial work - [GitHub Profile](https://github.com/pathakjiop)

**Acknowledgments:**
- [Tkinter documentation](https://docs.python.org/3/library/tkinter.html)
- [MySQL Documentation](https://dev.mysql.com/doc/)
