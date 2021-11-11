from tkinter import *

root = Tk()
root.title("Basketball scoring program")
root.geometry("800x600")
root.configure(background = "teal")

# MODEL #
count = 0
name1 = "Team1"
name2 = "Team2"
first_score = 0
second_score = 0

def enter_teams(event):
    global count, name1, name2
    if count == 0:
        name1 = team_entry.get()
        team_entry.delete(0,END)
        teams.config(text = "enter the name of the second team: ")
        count +=1
    else:
        name2 = team_entry.get()
        team_entry.delete(0,END)
        team1.config(text = name1 + ": " + str(first_score))
        team2.config(text = name2 + ": " + str(second_score))


# CONTROLLER #
team_entry = Entry(root,bg = "teal", fg = "black", font = ("Lobster 1.4",15))
team_entry.place(x = 310,y = 10, width = 250, height = 50)
team_entry.bind("<Return>", enter_teams)



# VIEW #
teams = Label(root, text = "enter the name of the first team: ", fg = "black", bg = "teal", font = ("Lobster 1.4",15))
teams.place(x = 10,y = 10, width = 300, height = 50)

team1 = Label(root, bg = "teal", fg = "purple", font = ("Lobster 1.4",15), text = name1)
team1.place(x = 10, y = 210, width = 250, height = 180)

team2 = Label(root,bg = "teal", fg = "yellow", font = ("Lobster 1.4",15), text = name2)
team2.place(x = 350, y = 210, width = 250, height = 180)

root.mainloop()
