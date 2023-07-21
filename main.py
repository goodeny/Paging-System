from tkinter import *
from card import Card
from datas import data_list
from center_GUI import *
import threading
import math

class Software:
    
    def __init__(self):
        self.colors = {'background': '#23274D'}
        self.window = Tk()
        center(self.window, 700, 600)
        self.window.title('Pagination')
        self.window.config(bg=self.colors['background'])
        self.window.resizable(0,0)
        #variables
        self.pages = []
        self.list_qnt = str(math.ceil(len(data_list)/8))
        #load images
        self.button_img = PhotoImage(file='./assets/button.png')
        self.button_next_img = PhotoImage(file='./assets/button2.png')
        self.button_cancel_img = PhotoImage(file='./assets/cancel.png')
        self.button_prev_cancel_img = PhotoImage(file='./assets/prev_cancel.png')
        self.top_sprite = PhotoImage(file='./assets/top_sprite.png')
        #load components
        threading.Thread(target=self.load_screen()).start()

    def div_top(self):
        self.top_frame = Frame(self.window, bg=self.colors['background'])
        self.top_frame.pack(fill=BOTH,expand=1)
        self.logo = Label(self.top_frame, bg=self.colors['background'], image=self.top_sprite)
        self.logo.pack(side=LEFT, anchor=W)

    def div_bottom(self):
        self.bottom_frame = Frame(self.window, bg=self.colors['background'], height=20)
        self.bottom_frame.pack(anchor=S, side=BOTTOM, fill=BOTH)

    def generate_buttons(self):
        self.previous_button = Button(self.bottom_frame, image=self.button_prev_cancel_img, bg=self.colors['background'], bd=0, activebackground=self.colors['background'], command=self.prev_page)
        self.previous_button.pack(side=LEFT, padx=50, pady=20)
        self.next_button = Button(self.bottom_frame, image=self.button_next_img, bg=self.colors['background'], bd=0, activebackground=self.colors['background'], command=lambda:threading.Thread(target=self.next_page).start())
        self.next_button.pack(side=RIGHT, padx=50, pady=20)
    
    def generate_number(self):
        self.number = 1
        self.label_number = Label(self.bottom_frame, text=f'{self.number}/'f'{self.list_qnt}', fg='white', font='20', bg=self.colors['background'])
        self.label_number.pack(expand=1)
 
    def generate_content(self):
        self.content_frame = Frame(self.window, bg=self.colors['background'],height=350, width=350)
        self.content_frame.pack(fill=BOTH, expand=1)

    def generate_card2(self, c, c2):
        for m in data_list:
            self.card = Card(m, c, c2)
            self.card.generate_card(self.content_frame)

    def next_page(self):
        self.previous_button.config(image=self.button_img)
        self.previous_button.config(state=NORMAL)
        from datas import data_list
        for i in range(8):
            self.pages.append(data_list[0])
            data_list.pop(0)
            if len(data_list) <= 8:
                self.next_button.config(image=self.button_cancel_img, command=...)
        self.number += 1
        self.label_number.config(text=f'{self.number}/'f'{self.list_qnt}')
        self.content_frame.destroy()
        self.generate_content()
        self.generate_card2(0, -4)
        self.window.update()

    def prev_page(self):
        if self.number > 1:
            self.previous_button.config(image=self.button_img)
            self.next_button.config(image=self.button_next_img, command=self.next_page)
            from datas import data_list
            for i in range(8):
                data_list.insert(0,self.pages[-1])
                self.pages.pop(-1)
            self.number -= 1
            self.label_number.config(text=f'{self.number}/'f'{self.list_qnt}')
            self.content_frame.destroy()
            self.generate_content()
            self.generate_card2(0, -4)
            if self.number == 1:
                self.previous_button.config(image=self.button_prev_cancel_img)

    def load_screen(self):
        self.div_top()
        self.div_bottom()
        self.generate_buttons()
        self.generate_number()
        self.generate_content()
        self.generate_card2(0,-4)

if __name__ == '__main__':
    s = Software()
    s.window.mainloop()