import psycopg2
import tkinter as gui



# Replace these with your PostgreSQL connection details
host = '192.168.1.42'  # Replace with your PostgreSQL server hostname or IP address
database_name = 'postgres'  # Replace with your database name
user = 'postgres'  # Replace with your PostgreSQL username
password = '06896#Qz1'  # Replace with your PostgreSQL password

    

database = psycopg2.connect(
    dbname=database_name,
    user=user,
    password=password,
    host=host
)

def execute(input): #simplifying the cursor.exeucte command into a simple method that creates the cursor, executes, and pushes
    
    cursor = database.cursor()
    cursor.execute(input)
    try:
        outp = cursor.fetchall()
    except Exception as e:
        print(e)
        outp = "No output"
    database.commit()
    return outp

def createGUI():
    global source
    source = gui.Tk()
    source.title("Amazon't Database")
    source.geometry("1000x800")

    addCustomerButton = gui.Button(source, text="Add Customer", command=openAddCustomerPrompt)
    addCustomerButton.pack()

    addDistributorButton = gui.Button(source, text="Add Distributor", command=openAddDistributorPrompt)
    addDistributorButton.pack()
    
    addOrderButton = gui.Button(source, text="Add Order", command=openAddOrderPrompt)
    addOrderButton.pack()

    addProductButton = gui.Button(source, text="Add Product", command=openAddProductPrompt)
    addProductButton.pack()

    addPurchaseButton = gui.Button(source, text="Add Purchase", command=openAddPurchasePrompt)
    addPurchaseButton.pack()



    removeCustomerButton = gui.Button(source, text="Remove Customer", command=removeFromCustomer)
    removeCustomerButton.pack()

    removeDistributorButton = gui.Button(source, text="Remove Distributor", command=removeFromDistributor)
    removeDistributorButton.pack()

    removeOrderButton = gui.Button(source, text="Remove Order", command=removeFromOrder)
    removeOrderButton.pack()

    removeProductButton = gui.Button(source, text="Remove Product", command=removeFromProduct)
    removeProductButton.pack()

    removePurchaseButton = gui.Button(source, text="Remove Purchase", command=removeFromPurchase)
    removePurchaseButton.pack()

    source.mainloop()





def openAddCustomerPrompt():
    
    addCustomerPromptWindow = gui.Toplevel()
    addCustomerPromptWindow.title("Add Customer")
    addCustomerPromptWindow.geometry("300x150")

    def submitCustomer():
        cID = CustomerIDBox.get()
        cFN = CustomerFNameBox.get()
        cLN = CustomerLNameBox.get()
        cAD = CustomerAdrBox.get()

        try:
            outp = execute(f"insert into customer values('{cID}','{cFN}','{cLN}','{cAD}');")
            print(outp)
            addCustomerPromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    CustomerIDBox = gui.Entry(addCustomerPromptWindow)
    CustomerFNameBox = gui.Entry(addCustomerPromptWindow)
    CustomerLNameBox = gui.Entry(addCustomerPromptWindow)
    CustomerAdrBox = gui.Entry(addCustomerPromptWindow)
    CustomerSubmit = gui.Button(addCustomerPromptWindow, text="Submit", command=submitCustomer)

    CustomerIDBox.insert(0, "Enter ID")
    CustomerFNameBox.insert(0, "Enter First Name")
    CustomerLNameBox.insert(0, "Enter Last Name")
    CustomerAdrBox.insert(0, "Enter Address")

    CustomerIDBox.pack()
    CustomerFNameBox.pack()
    CustomerLNameBox.pack()
    CustomerAdrBox.pack()
    CustomerSubmit.pack()

def openAddDistributorPrompt():
    
    addDistributorPromptWindow = gui.Toplevel()
    addDistributorPromptWindow.title("Add Distributor")
    addDistributorPromptWindow.geometry("300x150")

    def submitDistributor():
        dID = DistributorIDBox.get()
        dNA = DistributorNameBox.get()
        dAD = DistributorAdrBox.get()

        try:
            outp = execute(f"insert into distributor values('{dID}','{dNA}','{dAD}');")
            print(outp)
            addDistributorPromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    DistributorIDBox = gui.Entry(addDistributorPromptWindow)
    DistributorNameBox = gui.Entry(addDistributorPromptWindow)
    DistributorAdrBox = gui.Entry(addDistributorPromptWindow)
    DistributorSubmit = gui.Button(addDistributorPromptWindow, text="Submit", command=submitDistributor)

    DistributorIDBox.insert(0, "Enter ID")
    DistributorNameBox.insert(0, "Enter Distributor Name")
    DistributorAdrBox.insert(0, "Enter Distributor Address")

    DistributorIDBox.pack()
    DistributorNameBox.pack()
    DistributorAdrBox.pack()
    DistributorSubmit.pack()

def openAddOrderPrompt():
    
    addOrderPromptWindow = gui.Toplevel()
    addOrderPromptWindow.title("Add Order")
    addOrderPromptWindow.geometry("300x150")

    def submitDistributor():
        oID = OrderIDBox.get()
        oDA = OrderDateBox.get()
        oDT = OrderDepartBox.get()
        oDE = OrderDeliverBox.get()
        cID = CustomerIDBox.get()

        try:
            outp = execute(f"insert into order values('{oID}','{oDA}','{oDT}','{oDE}','{cID}');")
            print(outp)
            addOrderPromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    OrderIDBox = gui.Entry(addOrderPromptWindow)
    OrderDateBox = gui.Entry(addOrderPromptWindow)
    OrderDepartBox = gui.Entry(addOrderPromptWindow)
    OrderDeliverBox = gui.Entry(addOrderPromptWindow)
    CustomerIDBox = gui.Entry(addOrderPromptWindow)
    OrderSumbit = gui.Button(addOrderPromptWindow, text="Submit", command=submitDistributor)

    OrderIDBox.insert(0, "Enter ID")
    OrderDateBox.insert(0, "Enter Order Date")
    OrderDepartBox.insert(0, "Enter Departure Date")
    OrderDeliverBox.insert(0, "Enter Delivery Name")
    CustomerIDBox.insert(0, "Enter Customer ID")

    OrderIDBox.pack()
    OrderDateBox()
    OrderDepartBox.pack()
    OrderDeliverBox.pack()
    CustomerIDBox.pack()
    OrderSumbit.pack()

def openAddProductPrompt():
    
    addOrderPromptWindow = gui.Toplevel()
    addOrderPromptWindow.title("Add Product")
    addOrderPromptWindow.geometry("300x150")

    def submitProduct():
        pID = ProductIDBox.get()
        pNa = ProductNameBox.get()
        pPr = ProductPriceBox.get()
        pDi = ProductDistributorBox.get()

        try:
            outp = execute(f"insert into product values('{pID}','{pNa}','{pPr}','{pDi}');")
            print(outp)
            addOrderPromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    ProductIDBox = gui.Entry(addOrderPromptWindow)
    ProductNameBox = gui.Entry(addOrderPromptWindow)
    ProductPriceBox = gui.Entry(addOrderPromptWindow)
    ProductDistributorBox = gui.Entry(addOrderPromptWindow)
    ProductSumbit = gui.Button(addOrderPromptWindow, text="Submit", command=submitProduct)

    ProductIDBox.insert(0, "Enter ID")
    ProductNameBox.insert(0, "Enter Product Name")
    ProductPriceBox.insert(0, "Enter Price")
    ProductDistributorBox.insert(0, "Enter Product Distributor (ID)")

    ProductIDBox.pack()
    ProductNameBox()
    ProductPriceBox.pack()
    ProductDistributorBox.pack()
    ProductSumbit.pack()

def openAddPurchasePrompt():
    
    addOrderPromptWindow = gui.Toplevel()
    addOrderPromptWindow.title("Add Purchase")
    addOrderPromptWindow.geometry("300x150")

    def submitProduct():
        pID = ProductIDBox.get()
        oID = OrderIDBox.get()
        pQu = QuantityBox.get()

        try:
            outp = execute(f"insert into purchase values('{pID}','{oID}','{pQu}');")
            print(outp)
            addOrderPromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    ProductIDBox = gui.Entry(addOrderPromptWindow)
    OrderIDBox = gui.Entry(addOrderPromptWindow)
    QuantityBox = gui.Entry(addOrderPromptWindow)
    PurchaseSumbit = gui.Button(addOrderPromptWindow, text="Submit", command=submitProduct)

    ProductIDBox.insert(0, "Enter ID")
    OrderIDBox.insert(0, "Enter Product Name")
    QuantityBox.insert(0, "Enter Price")
    PurchaseSumbit.insert(0, "Enter Product Distributor (ID)")

    ProductIDBox.pack()
    OrderIDBox()
    QuantityBox.pack()
    PurchaseSumbit.pack()


def removeFrom(table, idvar):
    
    removePromptWindow = gui.Toplevel()
    removePromptWindow.title(f"Remove {table}")
    removePromptWindow.geometry("300x150")

    def submitRemoval():
        id = IDBox.get()

        try:
            outp = execute(f"delete from {table} where {idvar}={id};")
            print(outp)
            removePromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    IDBox = gui.Entry(removePromptWindow)
    Submit = gui.Button(removePromptWindow, text="Submit", command=submitRemoval)

    IDBox.insert(0, "Enter ID")

    IDBox.pack()    
    Submit.pack()

def removeFromDistributor():
    removeFrom("distributor","d_id")

def removeFromCustomer():
    removeFrom("customer", "c_id")

def removeFromOrder():
    removeFrom("order", "o_id")

def removeFromProduct():
    removeFrom("product", "p_id")

def removeFromPurchase():
    removePromptWindow = gui.Toplevel()
    removePromptWindow.title(f"Remove purchase")
    removePromptWindow.geometry("300x150")

    def submitRemoval():
        pid = pidBox.get()
        oid = oidBox.get

        try:
            outp = execute(f"delete from purchase where p_id={pid} and o_id={oid};")
            print(outp)
            removePromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    pidBox = gui.Entry(removePromptWindow)
    oidBox = gui.Entry(removePromptWindow)
    Submit = gui.Button(removePromptWindow, text="Submit", command=submitRemoval)

    pidBox.insert(0, "Enter Product ID")
    oidBox.insert(0, "Enter Order ID")

    pidBox.pack()  
    oidBox.pack()  
    Submit.pack()

createGUI()