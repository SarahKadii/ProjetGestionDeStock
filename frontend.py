import tkinter# conda install -c anaconda tk
import controller 


def manage_checkout(window):
    #Erease window
    erease_window(window)
    window.title("Manage Chekout")
    screen_x = 1200
    screen_y = 720
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #labels and entry
    label_choose = tkinter.Label(window, text="Choose articles", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_choose.place(relx=0.3, rely=0.1)

    label_article_name = tkinter.Label(window, text="Product Name", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_article_name.place(relx=0.05, rely=0.2)
    entry_article_name = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_article_name.place(relx=0.2, rely=0.2)

    label_quantity = tkinter.Label(window, text="Quantity", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_quantity.place(relx=0.05, rely=0.27)
    entry_quantity = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_quantity.place(relx=0.2, rely=0.27)

    label_client_name = tkinter.Label(window, text="Client Name", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_client_name.place(relx=0.05, rely=0.5)
    entry_client_name = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_client_name.place(relx=0.2, rely=0.5)

    label_product_desc = tkinter.Label(window, text="Products Description", font=("helvetica", 15, "bold"), fg="black", borderwidth=5)
    label_product_desc.place(relx=0.7, rely=0.12)
    entry_product_desc = tkinter.Label(window, font=("helvetica", 15, "bold"), width=60, heigh=20, bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_product_desc.place(relx=0.4, rely=0.17)


    #Button ADD
    button_add =tkinter.Button(window, text="ADD", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2) # command=signup
    button_add.place(relx=0.3, rely=0.32)

    #Button Back
    button_back =tkinter.Button(window, text="Back", font=("Times New Roman", 15, "bold"), bg="#BB5E00", fg='white',
                    activebackground="#EA7500", activeforeground="white", borderwidth=2) #  command=lambda:connexion(window)
    button_back.place(relx=0.1, rely=0.9)

    #Button
    button =tkinter.Button(window, text="Display articles", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2, command=lambda:controller.get_all_products(window,entry_product_desc)) # command=signup
    button.place(relx=0.8, rely=0.9)

def erease_window(window):
    for widget in window.winfo_children():
        widget.destroy()


window = tkinter.Tk()
manage_checkout(window)

window.mainloop()

