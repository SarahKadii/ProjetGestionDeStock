import tkinter # conda install -c anaconda tk
from tkinter import filedialog
import main
receipt = None
def get_all_products(window, label_desc):
    names = ["Number  ", " Product Name ", "    Quantity     ", "   Price    "]
    products = main.displayBDD()
    #display all products
    display_datas(window, label_desc, products, names)
    
                #print(products)
def charge_data_from_file(window, label_desc):
    global receipt
    names = [" Product Name ", "    Number     "]
    path = tkinter.filedialog.askopenfilename(parent=window, title='Please select a directory')
    receipt = main.openingFile(path)
    receipts = []
    for i in range(0,len(receipt),2):
        receipts.append([receipt[i], receipt[i+1]])
    #display receipt articles
    display_datas(window, label_desc, receipts, names)

def update_data_by_receipt(window, label):
    for widget in label.winfo_children():
            widget.destroy()
    if receipt not None:
        print(receipt)
    print(receipt)

def display_datas(window, label, products, names):
    if len(products) == 0:
        label = tkinter.Label(window, text="No product is present", font=("helvetica", 15, "bold"), bg="white", fg="red", borderwidth=5)
        label.place(relx=0.25, rely=0.43)
        window.after(2000, label.destroy) 
    else:
        products.insert(0,names)
        for widget in label.winfo_children():
            widget.destroy()

        for i in range(len(products)): #Rows
            for j in range(len(products[0])):
                if i == 0:
                    b = tkinter.Label(label, text=products[i][j], font=("Times New Roman", 12, "bold"), bg="#0066CC", fg="white", borderwidth=4)
                elif i > 0 and j==3:
                    b = tkinter.Label(label, text=str(products[i][j])+"€", font=("Times New Roman", 11, "bold"), bg="#ECF5FF", fg="#272727", borderwidth=2)
                else:
                    b = tkinter.Label(label, text=products[i][j], font=("Times New Roman", 11, "bold"), bg="#ECF5FF",borderwidth=2)

                b.grid(row=i, column=j)
