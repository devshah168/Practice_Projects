import tkinter


def set_tile(row,column):
    global currplay
    if game_over:
        return
    
    if board[row][column]["text"] !="":
        return
    board[row][column]["text"]=currplay
    if currplay==playero:
        currplay=playerx
    else:
        currplay=playero
    label["text"]=currplay+"'s turn"  
    check_winner()

def check_winner():
    global turns,game_over
    turns+=1
    # for rows
    for row in range(3):
        if (board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"]
            and board[row][0]["text"]!=""):
            label.config(text=board[row][0]["text"]+" is the winner",foreground=color1)
            for column in range (3):
                board[row][column].config(foreground=color1,background=color4)
            game_over=True
            return

    # for columns
    for column in range(3):
        if (board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"]
            and board[0][column]["text"]!=""):
            label.config(text=board[0][column]["text"]+" is the winner",foreground=color1)
            for row in range (3):
                board[row][column].config(foreground=color1,background=color4)
            game_over=True
            return

    # for diagonal
    if (board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]
        and board[0][0]["text"]!=""):
        label.config(text=board[0][column]["text"] + " is the winner", foreground=color1)
        for i in range (3):
            board[i][i].config(foreground=color1,background=color4)
        game_over=True
        return

    if (board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"]
        and board[0][2]["text"]!=""):
        label.config(text=board[0][0]["text"] + " is the winner", foreground=color1)
        board[0][2].config(foreground=color1,background=color4)
        board[1][1].config(foreground=color1, background=color4)
        board[2][0].config(foreground=color1, background=color4)
        game_over=True
        return
    
    if turns==9:
        game_over=True
        label.config(text="It's a tie",foreground=color1)

def new_game():
    global turns,game_over
    turns=0
    game_over=False
    
    label.config(text=currplay+"'s turn",foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",foreground=color2,background=color3)

playerx='X'
playero='O'
currplay='X'

board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

color1 = "#b2b04e"
color2 = "#1d1ff1"
color3 = "#000000"
color4 = "#c42929"
turns=0
game_over=False

window=tkinter.Tk()
window.title("Tic Tac Toe")
# window.resizable(False,False)

frame=tkinter.Frame(window)
label=tkinter.Label(frame,text=currplay+"'s turn",font=("Consolas",20),background=color3,foreground="white")
label.grid(row=0,columnspan=3,sticky='we')
for row in range(3):
    for column in range(3):
        board[row][column]=tkinter.Button(frame,text="",font=('Consolas',50,"bold"),background=color3,foreground=color2,width=4,height=1,command=lambda row=row,column=column: set_tile(row,column))
        board[row][column].grid(row=row+1,column=column)

button=tkinter.Button(frame,text="Restart",font=("Consolas",20),background=color3,foreground="white",command=new_game)
button.grid(row=4,columnspan=3,sticky="we")
frame.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
