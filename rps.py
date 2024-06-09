from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("Vinay's ROCK,PAPER&SCISSOR")
root.configure(background="grey")

#import PICTURES
rock_img = ImageTk.PhotoImage(Image.open("hrock.png"))
paper_img = ImageTk.PhotoImage(Image.open("hpapper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("hscissor.png")) 
rock1_img = ImageTk.PhotoImage(Image.open("crock.png")) 
paper1_img = ImageTk.PhotoImage(Image.open("cpaper.png")) 
scissor1_img = ImageTk.PhotoImage(Image.open("cscissor.png")) 

#insert PICTURES
user_label = Label(root, image=paper_img,bg="grey")
bot_label  = Label(root,image=scissor1_img,bg="grey")
bot_label.grid(row=1,column=4)
user_label.grid(row=1,column=0)

#scores
playerScore = Label(root, text=0, font=100, bg="grey", fg="black")
bot_Score = Label(root, text=0, font=100, bg="grey", fg="black")
bot_Score.grid(row=1, column=3)
playerScore.grid(row=1, column=1)

#indicators
user_indicator = Label(root, font=50, text="USER")
bot_indicator = Label(root, font=50, text="BOT")
user_indicator.grid(row=0, column=1)
bot_indicator.grid(row=0, column=3)

#updatechoices
choices = ["rock", "paper", "scissor"]
def updateChoices(x):

#for computer
    bot_choice = choices[randint(0,2)]
    if bot_choice == "rock":
        bot_label.configure(image=rock1_img)
    elif bot_choice == "paper":
        bot_label.configure(image=paper1_img)
    else:
        bot_label.configure(image=scissor1_img)




#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    
    winner(x,bot_choice)

# #buttons
rock  = Button(root, width=20, height=2, text="ROCK",bg="grey", fg="black",command= lambda:updateChoices("rock")).grid(row=2,column=1)
paper = Button(root, width=20, height=2, text="PAPER",bg="grey", fg="black",command= lambda:updateChoices("paper")).grid(row=2,column=2)
scissor  = Button(root, width=20, height=2, text="SCISSOR",bg="grey", fg="black",command= lambda:updateChoices("scissor")).grid(row=2,column=3)
#messages
msg = Label(root, font=50,bg="black", fg="white")
msg.grid(row=5, column=2)

#update message
def update_message(x):
    msg['text'] = x

#update userscore   
def update_user_score():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
#update botscore
def update_bot_score():
    score = int(bot_Score["text"])
    score += 1
    bot_Score["text"] = str(score)

#check winner
def winner(player,bot):
    if player == bot :
        update_message("IT'S A TIE!!!")
    elif player == "rock":
        if bot == "paper":
            update_message("YOU LOOSE!")
            update_bot_score()
        else:
            update_message("YOU WIN!")
            update_user_score()
    elif player == "paper":
        if bot == "scissor":
            update_message("YOU LOOSE!")
            update_bot_score()
        else:
            update_message("YOU WIN!")
            update_user_score()
    elif player == "scissor":
        if bot == "rock":
            update_message("YOU LOOSE!")
            update_bot_score()
        else:
            update_message("YOU WIN!")
            update_user_score()
    else:
        pass        





root.mainloop()
