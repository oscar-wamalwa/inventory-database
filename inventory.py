#-----------------------***INVENTORY DATABASE SET UP,CONNECTION TO DB SET UP, TABLES CREATION***-------------
import mysql.connector
inventory_db_config = mysql.connector.connect(
    host="127.0.0.1",
    user="Ericadeshh",
    password="404-found-#"
    #database="stock"
)
cursor = inventory_db_config.cursor()
cursor.execute("DROP DATABASE IF EXISTS stock")
cursor.execute("CREATE DATABASE stock")
#cursor.execute("SHOW DATABASES")
#print(cursor.fetchall())
cursor.execute("USE stock")
cursor.execute("set foreign_key_checks = 0")#disabling foreign keys

#database set-up tables
product_table = '''
    CREATE TABLE PRODUCT_MANAGEMENT_TABLE(
        PRODUCT_NAME VARCHAR(255),
        PRODUCT_ID INT AUTO_INCREMENT PRIMARY KEY, 
        PRICE INT,
        QUANTITY INT
    )
'''
cursor.execute(product_table)
cursor.execute("CREATE INDEX idx_PRODUCT_ID ON PRODUCT_MANAGEMENT_TABLE(PRODUCT_ID)")
print("Product Table Created")

purchase_table = '''
    CREATE TABLE PURCHASE_MANAGEMENT_TABLE(
        SUPPLIER VARCHAR(255),
        PRODUCT_NAME VARCHAR(255),
        PRODUCT_ID INT,
        PRICE INT,
        QUANTITY INT,
        FOREIGN KEY(PRODUCT_ID) REFERENCES PRODUCT_MANAGEMENT_TABLE(PRODUCT_ID)
    )
'''
cursor.execute(purchase_table)
print("Purchase Table Created")

sale_table = '''
    CREATE TABLE SALES_TABLE(
       CUSTOMER_NAME VARCHAR(255),
       PRODUCT_NAME VARCHAR(255),
       PRODUCT_ID INT,
       PRICE INT,
       QUANTITY INT,
       FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCT_MANAGEMENT_TABLE(PRODUCT_ID)
    )
'''
cursor.execute(sale_table)
print("Sales Table Created")

user_table = '''
    CREATE TABLE USER_TABLE(
        USERNAME VARCHAR(255),
        USER_ID INT AUTO_INCREMENT PRIMARY KEY,
        PASSWORD VARCHAR(255)
    )'''
cursor.execute(user_table)
print("User Table Created")

inventory_db_config.commit()
#cursor.execute("DESC PRODUCT_MANAGEMENT")
#print(cursor.fetchall())

#--------------------------------***FUNCTIONS OF PRODUCT MANAGEMENT***-----------------------------------------
#Function to ADD a new  product into the database
def add_product():
    print("\nADDING A PRODUCT...\n")
    product_name = input("\nEnter Product Name: ")
    product_id = int(input(f"Enter {product_name}'s ID: "))
    price= input(f"Enter {product_name}'s Price: ")
    quantity = int(input(f"Enter {product_name}'s Quantity: "))

    product_query = '''
        INSERT INTO PRODUCT_MANAGEMENT_TABLE(PRODUCT_NAME, PRODUCT_ID, PRICE, QUANTITY)
        VALUES(%s, %s, %s, %s)
    '''
    product_values = (product_name,product_id,price,quantity)
    cursor.execute(product_query,product_values)
    print('Product added')
    inventory_db_config.commit()  
#add_product()

#func to update a product
def update_product():
    print("\nUPDATING A PRODUCT...\n")
    pick_id_to_change = input("Enter The Product's ID to change it's values : ")
    product_name = input("\nEnter Product Name: ")
    product_id = int(input(f"Enter {product_name}'s ID: "))
    price= input(f"Enter {product_name}'s Price: ")
    quantity = int(input(f"Enter {product_name}'s Quantity: "))

    update_query = "UPDATE PRODUCT_MANAGEMENT_TABLE SET PRODUCT_NAME=%s,PRODUCT_ID=%s,PRICE= %s,QUANTITY=%s WHERE PRODUCT_ID = %s"
    update_values = (product_name,product_id,price,quantity,pick_id_to_change)
    cursor.execute(update_query,update_values)
    print("Product updated")
    inventory_db_config.commit()
#update_product()

#function to delete a product
def delete_product():
    print("\nDELETING A PRODUCT....\n")
    del_product = input("Enter Product Name to delete: ")
    delete_query = "DELETE FROM PRODUCT_MANAGEMENT_TABLE WHERE PRODUCT_NAME = %s"
    delete_value= (del_product,)
    cursor.execute(delete_query,delete_value)
    print("Product deleted")
    inventory_db_config.commit()
#delete_product()

#---------------------------***PURCHASE MANAGEMENT FUNCTIONS***---------------------------
#FUNCTIONS FOR PURSCHASE MANAGEMENT
#func to add purchase record
def add_purchase():
    print("\n--------------PURCHASE MANAGEMENT FUNCTION(ADD PURCHASE)-------------------\n")
    supplier = input("Enter Supplier Name : ")
    product_name = input("\nEnter Product Name: ")
    product_id = int(input(f"Enter {product_name}'s ID: "))
    price= input(f"Enter {product_name}'s Price: ")
    quantity = int(input(f"Enter {product_name}'s Quantity: "))

    purchase_query = '''
        INSERT INTO PURCHASE_MANAGEMENT_TABLE(SUPPLIER,PRODUCT_NAME,PRODUCT_ID,PRICE,QUANTITY) 
        VALUES(%s, %s, %s, %s, %s)
    '''
    purchase_value = (supplier,product_name,product_id,price,quantity)
    cursor.execute(purchase_query,purchase_value)
    inventory_db_config.commit()
    print(f"{product_name}- Purchase Added")
#add_purchase()


#-----------------------------***SALES MANAGEMENT FUNCTIONS***--------------------------------------
def add_sale():
    print("\n-------------ADDING SALES FUNCTION--------------\n")
    customer_name = input("Enter Customer Name : ")
    product_name = input("\nEnter Product Name: ")
    product_id = int(input(f"Enter {product_name}'s ID: "))
    price= input(f"Enter {product_name}'s Price: ")
    quantity = int(input(f"Enter {product_name}'s Quantity: "))

    
    sales_query = '''
    INSERT INTO SALES_TABLE(CUSTOMER_NAME,PRODUCT_NAME,PRODUCT_ID,PRICE,QUANTITY)
    VALUES(%s,%s,%s,%s,%s)
    '''
    sales_values = (customer_name,product_name,product_id,price,quantity)
    cursor.execute(sales_query,sales_values)
    inventory_db_config.commit()
    print(f"{product_name} Sold to {customer_name}--- Added to Sales")
#add_sale()

#-------------------------------***USER MANAGEMENT FUNCTIONS***---------------------------
#FUNCTIONS OF USER MANAGEMENT
def add_user():
    #function to add a user
    NEW_USERNAME = input("\nEnter User Name: ")
    NEW_USER_ID = int(input("Enter User ID : "))
    NEW_PASSWORD = input("Enter User Password :")

    user_query = "INSERT INTO USER_TABLE (USERNAME,USER_ID,PASSWORD) VALUES(%s,%s,%s)"
    user_query_values = (NEW_USERNAME,NEW_USER_ID,NEW_PASSWORD)
    cursor.execute(user_query,user_query_values)
    inventory_db_config.commit()
    print(f"\n{NEW_USERNAME}- user added successfully") 
#add_user()

#func to update a product
def update_user():
    print("\nUPDATING A USER...\n")
    pick_id_to_change = input("Enter The User's ID to change details : ")
    new_user_name = input("\nEnter new UserName: ")
    new_user_id = int(input(f"Enter {new_user_name}'s ID: "))
    new_user_password= input(f"Enter {new_user_name}'s Password: ")

    update_query = "UPDATE USER_TABLE SET USERNAME=%s,USER_ID=%s,PASSWORD= %s WHERE USER_ID = %s"
    update_values = (new_user_name,new_user_id,new_user_password,pick_id_to_change)
    cursor.execute(update_query,update_values)
    print("User updated")
    inventory_db_config.commit()
#update_product()
    
#function to delete a user
def delete_user():
   user_to_delete = input("\nPick User to DELETE : ")
   del_query = "DELETE FROM USER_TABLE WHERE USERNAME= %s"
   del_value = (user_to_delete, )
   cursor.execute(del_query, del_value)
   inventory_db_config.commit()
   print(f"\n{user_to_delete} - deleted successfully")
   cursor.close()
   inventory_db_config.close()
#delete_user()
# The above line will throw an error if the product with ID 44 does not exist in the database. To avoid this use try-
#print(get_all_products())
   

#------------------------------***MENU INTERFACE***------------------------
class Menu:
    def __init__(self):
        print("\n---------------STOCK INVENTORY MANAGEMENT---------------\n")
        print("*********GROUP S MEMBERS*********")

        group_S_members = ["Daisy Chebet","Evelyn Akinyi","Oscar Wamalwa"]
        for person in group_S_members:
            if person == "Daisy Chebet":
                print(f"{person}-database Dev")
            else:
                 print(f"{person}-Group Member")

    #function to display menu
    def display_menu(self):
        print("\nMain Menu: ")
        print("1. Product Management Functions")
        print("2. Purchase Management Functions")
        print("3. Sales Management Functions")
        print("4. User Management")
        print("5. Exit")

    def run_choice(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")
            if choice == "1":
                print("\nProduct Management Module Selected\n")
                choose_prod_management_func = '''
                    1.Add a New Product
                    2.Update a Product
                    3.Delete a Product
                '''
                print(choose_prod_management_func)
                choose_prod_management_func_input = input(">>>: ")
                if choose_prod_management_func_input =="1":
                    add_product()
                    continue
                elif choose_prod_management_func_input =="2":
                    update_product()
                    continue
                elif choose_prod_management_func_input =="3":
                    delete_product()
                    continue

            elif choice == "2":
                print("\nPurchase Management Module Selected!")
                add_purchase()
                continue
            elif choice == "3":
                print("\nSales Management Module Selected!")
                add_sale()
                continue
            
            elif choice == "4":
                print("\nUser Management Module Selected!")
                choose_user_management_func = '''
                    1.Add a New User
                    2.Update a Current User
                    3.Delete a User
                '''
                print(choose_user_management_func)
                choose_user_management_func_input = input(">>>: ")
                if choose_user_management_func_input =="1":
                    add_user()
                    continue
                elif choose_user_management_func_input =="2":
                    update_user()
                elif choose_user_management_func_input =="3":
                    delete_user()
                    continue
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option")

menu = Menu()
menu.run_choice()

'''if __name__ =="__main__":
    menu = Menu()
    menu.run_choice()
    '''