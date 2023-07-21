from tkinter import *
from datas import data_list
import threading

class Card:
    
    list_card = []
    def __init__(self, title, c, c2):
        self.colors = {'card': '#3E487D'}

        self.title = title
        self.width = 21
        self.height = 11
        self.count = c
        self.count2 = c2

    def generate(self, window, title, x1, y1):
        self.title = title
        Card.list_card.append(self.title)
        self.card = Label(window, bg=self.colors['card'], width=self.width, height=self.height)
        self.card.place(x=x1, y=y1)

        self.title_label = Label(self.card, text=self.title, fg='white', bg=self.colors['card'])
        self.title_label.place(x=0, y=0)

    def generate_card(self, window):
        for i in data_list:
            if self.count < 4:
                try:
                    threading.Thread(target=self.generate(window, i,self.calc(25,25)[0][self.count], 30)).start() 
                except:
                    pass 
            self.count +=1
            if self.count > 4 and self.count < 9:
                try:
                    threading.Thread(target=self.generate(window, i,self.calc(25,25)[1][self.count2], 210)).start() 
                except:
                    pass 
            self.count2 += 1

    def calc(self, n1, n2):
        f = []
        g = []
        final = []
        f.append(25)
        g.append(25)
        n = n1
        n2 = n2
        for i in range(8):
            if i < 4:
                n += 164
                f.append(n)
            else:
                n2 += 164
                g.append(n2)
        final.append(f)
        final.append(g)

        return final

