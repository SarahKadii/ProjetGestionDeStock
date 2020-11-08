import tkinter # conda install -c anaconda tk

import main

global products
names = ["Number  ", " Product Name ", "    Quantity     ", "   Price    "]

def get_all_products(window, label_desc):
    products = main.displayBDD()
    if len(products) == 0:
        label = tkinter.Label(window, text="No product is present", font=("helvetica", 15, "bold"), bg="white", fg="red", borderwidth=5)
        label.place(relx=0.25, rely=0.43)
        window.after(2000, label.destroy) 
    else:
        products.insert(0,names)
        for widget in label_desc.winfo_children():
            widget.destroy()

        for i in range(len(products)): #Rows
            for j in range(len(products[0])):
                if i == 0:
                    b = tkinter.Label(label_desc, text=products[i][j], font=("Times New Roman", 12, "bold"), bg="#0066CC", fg="white", borderwidth=4)
                elif i > 0 and j==3:
                    b = tkinter.Label(label_desc, text=str(products[i][j])+"€", font=("Times New Roman", 11, "bold"), bg="#ECF5FF", fg="#272727", borderwidth=2)
                else:
                    b = tkinter.Label(label_desc, text=products[i][j], font=("Times New Roman", 11, "bold"), bg="#ECF5FF",borderwidth=2)

                b.grid(row=i, column=j)
                #print(products)
