from tkinter import *
import random 
import time 

class  Balle: 
    def  __init__(self, canvas, couleur):         
        self.canvas = canvas         
        self.id = canvas.create_oval(10, 10, 25, 25, fill=couleur)    
        self.largeur_canvas = self.canvas.winfo_width() 
        self.hauteur_canevas = self.canvas.winfo_height()
        self.canvas.move(self.id, self.largeur_canvas // 2, self.hauteur_canevas // 2)
        self.x = 0
        self.y = -1  
        self.end = False
    def stopMe(self):
        self.end = True       
    def  dessiner(self):  
        if not self.end:       
            self.canvas.move(self.id, self.x, self.y)         
            pos = self.canvas.coords(self.id) 
            if  pos[1] <= 0:             
                self.y = 1 
            if  pos[3] >= self.hauteur_canevas:             
                self.y = -1
            return True
        else:
            return False

                      
tk = Tk() 
tk.title("Jeu") 

tk.resizable(0, 0) 
tk.wm_attributes("-topmost", 1) 
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()
canvas = Canvas(tk, width=screen_width, height=screen_height - 100, bd=0, highlightthickness=0) 
canvas.pack() 
tk.update() 
balle = Balle(canvas, 'red') 

def closeWindow():
    balle.stopMe()
    tk.destroy()


Button(tk, text="Quit", command=closeWindow).pack()


while 1:     
    if balle.dessiner():
        tk.update_idletasks()     
        tk.update()     
        time.sleep(0.0001) 
    else:
        #here, quit button was pressed !
        break

