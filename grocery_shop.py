import mysql.connector as connector
from prettytable import PrettyTable

# Constants
CUSTOMER_TABLE = 'customer_details'
PRODUCT_TABLE = 'product_details'
WORKER_TABLE = 'worker_details'
DATABASE = 'grocery_shop'

sql_add_cd = f"INSERT INTO {CUSTOMER_TABLE} (customer_name, gender, phone_no, due_amount) VALUES"
sql_add_pd = f"INSERT INTO {PRODUCT_TABLE} (product_name, product_cost, in_stock) VALUES"
sql_add_wd = f"INSERT INTO {WORKER_TABLE} (worker_name, worker_work, gender, worker_age, worker_salary, phone_no) VALUES"

# Connecting to my server
mydb = connector.connect(
    host="localhost",
    user="root",
    password="Nancymomoland3000@",
    database=DATABASE
)

# Creating a cursor
cursor = mydb.cursor()

# for adding values in all table
def addCustomer(customer_name: str, gender: str, customer_phone_no, due_amount: float = 0):
    cursor.execute(
        f'{sql_add_cd} ("{customer_name}", "{gender[0].upper()}", "{str(customer_phone_no)}", {due_amount})')
    mydb.commit()


def addProduct(product_name: str, product_cost: float, in_stock: bool):
    cursor.execute(
        f'{sql_add_pd} ("{product_name}", {product_cost}, {in_stock})')
    mydb.commit()


def addWorker(worker_name: str, worker_work: str, worker_gender: str, worker_age: int, worker_salary: int, worker_phone_no):
    cursor.execute(
        f'{sql_add_wd} ("{worker_name}", "{worker_work}", "{worker_gender[0].upper()}", {worker_age}, {worker_salary}, "{str(worker_phone_no)}")')
    mydb.commit()

# for displaying all tables
def displayAllCustomer():
    cursor.execute(f'SELECT * FROM {CUSTOMER_TABLE}')
    record = cursor.fetchall()
    if record:
        mTable = PrettyTable(
            ['Customer Name', 'Gender', 'Phone No.', 'Due Amount'], align='l')
        mTable.add_rows(record)
        print(mTable)
    else:
        print('\n\033[31m' +
              'Result: No data found by the given query' + '\033[0m\n')


def displayAllProduct():
    cursor.execute(f'SELECT * FROM {PRODUCT_TABLE}')
    record = cursor.fetchall()
    if record:
        mTable = PrettyTable(
            ['Product Name', 'Product cost', 'In Stock'], align='l')
        mTable.add_rows(record)
        print(mTable)
    else:
        print('\n\033[31m' +
              'Result: No data found by the given query' + '\033[0m')


def displayAllWorker():
    cursor.execute(f'SELECT * FROM {WORKER_TABLE}')
    record = cursor.fetchall()
    if record:
        mTable = PrettyTable(
            ['Worker Name', 'Work', 'Gender', 'Age', 'Salary', 'Phone No.'], align='l')
        mTable.add_rows(record)
        print(mTable)
    else:
        print('\n\033[31m' +
              'Result: No data found by the given query' + '\033[0m')



def customer_table_display():
    print("\n1:for adding details \n2:for showing details \n3:for delete all \n4:for exit")
    option_customer_table=int(input("option(customer):"))
    if option_customer_table==1:
        customer_name=input("enter customer name:")
        gender=input("enter your gender:")
        phone_no=int(input("enter ph no number:"))
        due_amount=int(input("enter amount to be paid:"))
        addCustomer(customer_name,gender,phone_no,due_amount)
        customer_table_display()
    elif option_customer_table==2:
        displayAllCustomer()   
        customer_table_display() 
    elif option_customer_table==3:
        cursor.execute(f'delete from {CUSTOMER_TABLE}')
        mydb.commit()
        customer_table_display()
    elif option_customer_table==4:
        pass 
    else:
        print("\n(select option from 1 to 4)\n")
        customer_table_display()



def products_table_display():
    print("\n1:for adding details \n2:for showing details \n3:for delete all \n4:for exit")
    option_products_table=int(input("option(product):"))
    if option_products_table==1:
        product_name=input("enter product name:")
        product_cost=int(input("enter product cost:"))
        in_stock=input("enter quantity in stock:")
        addProduct(product_name,product_cost,in_stock)
        products_table_display()
    elif option_products_table==2:
        displayAllProduct() 
        products_table_display() 
    elif option_products_table==3:
       cursor.execute(f'delete from {PRODUCT_TABLE}')
       mydb.commit()
       products_table_display()
    elif option_products_table==4:
        pass   
    else:
        print("\n(select option from 1 to 4)\n")
        products_table_display()    


def wokers_table_display():
    print("\n1:for adding details \n2:for showing details \n3:for delete all \n4:for exit")
    option_workers_display=int(input("option(worker):"))
    if option_workers_display==1:
        worker_name=input("enter worker name:")
        worker_work=input("enter worker work:")
        worker_gender=input("enter worker gender:")
        worker_age=int(input("enter worker age:"))
        worker_salary=int(input("enter worker salary:"))
        worker_phone_no=int(input("enter ph no:"))

        addWorker(worker_name,worker_work,worker_gender,worker_age,worker_salary,worker_phone_no)
        wokers_table_display()
    elif option_workers_display==2:
        displayAllWorker() 
        wokers_table_display() 
    elif option_workers_display==3:
       cursor.execute(f'delete from {WORKER_TABLE}')
       mydb.commit()
    elif option_workers_display==4:
        pass   
    else:
        print("\n(select option from 1 to 4)\n")
        wokers_table_display()    


def display_loop():
    main_table = PrettyTable(["shop_entry"])
    cursor.execute("show tables")
    data = cursor.fetchall()
    main_table.add_rows(data)
    print(main_table)

#for searching
def search_table():
    print("\n1:search for customer \n2:search for products \n3:search for worker \n4:for exit")
    search_input=int(input("option(search):"))  
    if search_input==1:
        print("customer ph no pls!")
        customer_search=int(input("ph no:"))  
        cursor.execute(f'select * from customer_details where phone_no={customer_search}')
        search_data_customer=cursor.fetchall()
        if search_data_customer==[]:
            print("\ncustomer not exsist")
            search_table() 
        elif search_data_customer!=[]:     
            search_table_customer=PrettyTable(
            ['Customer Name', 'Gender', 'Phone No.', 'Due Amount'], align='l')
            search_table_customer.add_rows(search_data_customer)
            print(search_table_customer)
            search_table()
    elif search_input==2:
        print("product name  pls!")
        product_search=input("name:")
        cursor.execute(f'select * from product_details where product_name="{product_search}"')
        search_data_product=cursor.fetchall()
        if search_data_product==[]:
            print("\nproduct not exsist")
            search_table()  
        elif search_data_product!=[]:   
            search_table_product=PrettyTable(
            ['Product name', 'Product cost', 'Product quantity'], align='l')
            search_table_product.add_rows(search_data_product)
            print(search_table_product)
            search_table()
    elif search_input==3:
        print("worker ph no pls!")
        worker_search=int(input("ph no:"))  
        cursor.execute(f'select * from worker_details where phone_no={worker_search}')
        search_data_worker=cursor.fetchall()
        if search_data_worker==[]:
            print("\nwoker not exsist")
            search_table() 
        elif search_data_worker!=[]:     
            search_table_worker=PrettyTable(
            ['Worker Name', 'Worker Work', 'Worker Gender ', 'Worker Age','Worker Salary','Woker Phone No'], align='l')
            search_table_worker.add_rows(search_data_worker)
            print(search_table_worker)
            search_table()

    elif search_input==4:
        pass    
    else:
        print("select option from 1 to 4")
        search_table()

#main logic

def logic():
    display_loop()
    print("1:for customer_details \n2:for product_details \n3:for worker_details \n4:for search \n5:for exit")
    option_main_table=int(input("enter your option:"))
    if option_main_table==1:
        customer_table_display()
        logic()
    elif option_main_table==2:
        products_table_display()
        logic()
    elif option_main_table==3:
        wokers_table_display()
        logic()
    elif option_main_table==4:
        search_table()
        logic()
    elif option_main_table==5:
        print("Made By \nUdayan Majumder(Roll No:13) \nSarthak Biswas(Roll No:12) \nAvirup Paul(Roll No:10)")
        exit()    
       
    else:
        print("\nselect from option 1 to 4\n")
        logic()    

logic()
mydb.close()

