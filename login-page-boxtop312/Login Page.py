from tkinter import *

root = Tk()
root.title("Login Page")
root.geometry("300x300")
# MODEL #
login_dict = {"AlexM": "password321", "shoan": "shoan", "username": "password", "password": "password",
              "username1": "username"}
incorrect_counter = 0


def comparer():
    global incorrect_counter
    username = str(username_entry.get())
    password = str(password_entry.get())
    if username in login_dict and password == login_dict[username] and incorrect_counter <= 3:
        login_label.config(text="Correct")
    elif incorrect_counter >= 3:
        login_label.config(text="3 tries used locked out")
        root.config(background="red")
        login_label.config(background="red")
        username_entry.config(bg="red")
        password_entry.config(bg="red")
        username_label.config(bg="red")
        password_label.config(bg="red")
        login_butt.config(bg="red")
    else:
        login_label.config(text="Incorrect")
        incorrect_counter += 1


# CONTROLLER #
username_entry = Entry(root, fg="black", font=("Lobster 1.4", 15))
username_entry.place(x=75, y=100, width=150)

password_entry = Entry(root, fg="black", font=("Lobster 1.4", 15), show="*")
password_entry.place(x=75, y=150, width=150)

login_butt = Button(root, fg="black", font=("Lobster 1.4", 13), text="log in", command=comparer)
login_butt.place(x=100, y=201, width=100)

# VIEW #
username_label = Label(root, fg="black", font=("Lobster 1.4", 10), text="username")
username_label.place(x=55, y=78, width=100)

password_label = Label(root, fg="black", font=("Lobster 1.4", 10), text="password")
password_label.place(x=55, y=128, width=100)

login_label = Label(root, fg="black", font=("Lobster 1.4", 10), text="")
login_label.place(x=21, y=179, width=150)

root.mainloop()
