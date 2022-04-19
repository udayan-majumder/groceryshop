import mysql.connector as db

# Constants
CUSTOMER_TABLE = 'customer_details'
PRODUCT_TABLE = 'product_details'
WORKER_TABLE = 'worker_details'
DATABASE = 'grocery_shop'

check = []

mydb = db.connect(
    host='localhost',
    user='root',
    password='Nancymomoland3000@'
)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")
for database in cursor:
    check.append(database[0])

if DATABASE not in check:
    cursor.execute(f"CREATE DATABASE {DATABASE}")
    print("Database created")
    check.clear()

cursor.execute(f"SHOW TABLES FROM {DATABASE}")

for table in cursor:
    check.append(table[0])

if CUSTOMER_TABLE not in check:
    cursor.execute(
        f"CREATE TABLE {DATABASE}.{CUSTOMER_TABLE} (customer_name VARCHAR(255) NOT NULL, gender CHAR(1), phone_no VARCHAR(255), due_amount FLOAT unsigned NOT NULL)")
    print(f'Table {CUSTOMER_TABLE} created')

if PRODUCT_TABLE not in check:
    cursor.execute(
        f"CREATE TABLE {DATABASE}.{PRODUCT_TABLE} (product_name VARCHAR(255) NOT NULL, product_cost FLOAT unsigned NOT NULL, in_stock INT NOT NULL)")
    print(f'Table {PRODUCT_TABLE} created')

if WORKER_TABLE not in check:
    cursor.execute(f"CREATE TABLE {DATABASE}.{WORKER_TABLE} (worker_name VARCHAR(255) NOT NULL, worker_work VARCHAR(255) NOT NULL, gender CHAR(1), worker_age INT(3) NOT NULL, worker_salary INT(5) unsigned NOT NULL, phone_no VARCHAR(255) NOT NULL)")
    print(f'Table {WORKER_TABLE} created')

# Close
mydb.close()
print("Server closed successfully")
