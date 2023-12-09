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

    removeCustomerButton = gui.Button(source, text="Remove Customer", command=openRemoveCustomerPrompt)
    removeCustomerButton.pack()

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

def openRemoveCustomerPrompt():
    
    removeCustomerPromptWindow = gui.Toplevel()
    removeCustomerPromptWindow.title("Remove Customer")
    removeCustomerPromptWindow.geometry("300x150")

    def submitCustomerRemoval():
        cID = CustomerIDBox.get()

        try:
            outp = execute(f"delete from customer where c_id={cID};")
            print(outp)
            removeCustomerPromptWindow.destroy()
            
        except Exception as e:
            
            print(e)

    CustomerIDBox = gui.Entry(removeCustomerPromptWindow)
    CustomerSubmit = gui.Button(removeCustomerPromptWindow, text="Submit", command=submitCustomerRemoval)

    CustomerIDBox.insert(0, "Enter ID")

    CustomerIDBox.pack()    
    CustomerSubmit.pack()

createGUI()