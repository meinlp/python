from tkinter import *
from tkinter import messagebox
import random

from data import Data
from textwrap import wrap
from card import Card

BACKGROUND_COLOR = "#B1DDC6"
TITLE_STYLE = ('Rockwell', 30, 'italic')
WORD_STYLE = ('Rockwell', 50, 'bold')


def prepare_text(text):
    chars_per_line = 20
    wrapped_text = '\n'.join(wrap(text, chars_per_line))
    return wrapped_text


class FlashyUi:
    def __init__(self, data: Data):
        self.card: Card
        self.side_of_the_card = 0
        self.data = data

        self.window = Tk()
        self.window.title('Learning English')
        self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

        # card
        self.side_of_the_card = 0
        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front = PhotoImage(file='images/card_front.png')
        self.card_back = PhotoImage(file='images/card_back.png')
        self.canvas_image = self.canvas.create_image(400, 265, image=self.card_front)
        self.card_title = self.canvas.create_text(400, 120, fill='black', font=TITLE_STYLE)
        self.card_word = self.canvas.create_text(400, 265, fill='black', font=WORD_STYLE)
        self.pick_a_word()
        self.canvas.grid(column=0, row=0, columnspan=3, rowspan=6)
        self.window.bind_all('<space>', self.space_is_pressed)

        # main buttons
        self.next_image = PhotoImage(file='images/right.png')
        self.next_button = Button(image=self.next_image, highlightthickness=0,
                                  highlightbackground=BACKGROUND_COLOR,
                                  command=self.pick_a_word)
        self.next_button.grid(column=0, row=7)

        self.move_image = PhotoImage(file='images/wrong.png')
        self.move_button = Button(image=self.move_image, highlightthickness=0,
                                  highlightbackground=BACKGROUND_COLOR,
                                  command=self.move_to_learned)
        self.move_button.grid(column=2, row=7)

        # secondary buttons
        self.flip_image = PhotoImage(file='images/flip.png')
        self.flip_button = Button(image=self.flip_image, highlightthickness=0,
                                  highlightbackground=BACKGROUND_COLOR,
                                  command=self.flip)
        self.flip_button.place(anchor=CENTER)
        self.flip_button.grid(column=1, row=7)

        self.find_button = Button(text='Find', width=3, height=1, fg='grey',
                                  highlightbackground=BACKGROUND_COLOR,
                                  command=self.find_popup)
        self.find_button.grid(column=3, row=1)

        self.change_button = Button(text='Change', width=3, height=1, fg='grey',
                                    highlightbackground=BACKGROUND_COLOR,
                                    command=self.change_popup)
        self.change_button.grid(column=3, row=2)

        self.delete_button = Button(text='Delete', width=3, height=1, fg='grey',
                                    highlightbackground=BACKGROUND_COLOR,
                                    command=self.delete_word)
        self.delete_button.grid(column=3, row=3)

        self.add_button = Button(text='Add', width=3, height=1, fg='grey',
                                 highlightbackground=BACKGROUND_COLOR,
                                 command=self.add_popup)
        self.add_button.grid(column=3, row=4)

        self.window.mainloop()

    def pick_a_word(self, word='random'):
        self.card = self.data.get_new_card(word=word)
        self.canvas.itemconfig(self.canvas_image, image=self.card_front)
        self.canvas.itemconfig(self.card_title, text=self.data.lang_from_full, fill='black')
        self.canvas.itemconfig(self.card_word, text=prepare_text(self.card.word[0]), fill='black')

    def flip(self):
        self.side_of_the_card = (self.side_of_the_card + 1) % 2  # flip side
        image = [self.card_front, self.card_back]
        lang = [self.data.lang_from_full, self.data.lang_to_full]
        color = ['black', 'white']
        self.canvas.itemconfig(self.canvas_image, image=image[self.side_of_the_card])
        self.canvas.itemconfig(self.card_title, text=lang[self.side_of_the_card], fill=color[self.side_of_the_card])
        self.canvas.itemconfig(self.card_word, text=prepare_text(self.card.word[self.side_of_the_card]),
                               fill=color[self.side_of_the_card])

    def change_popup(self):
        popup = Tk()
        popup.title('Add a word')
        popup.config(padx=20, pady=20)

        word_label = Label(popup, text='Word')
        word_label.grid(column=0, row=0)
        word_entry = Entry(popup)
        word_entry.insert(END, string=self.card.word[0])
        word_entry.grid(column=1, row=0)

        translate_label = Label(popup, text='Translation')
        translate_label.grid(column=0, row=1)
        translate_entry = Entry(popup)
        translate_entry.insert(END, string=self.card.word[1])
        translate_entry.grid(column=1, row=1)

        def change_word():
            new_word = word_entry.get()
            new_translation = translate_entry.get()
            self.data.alter(self.card, new_word, new_translation)
            self.pick_a_word(word=new_word)
            popup.destroy()

        add_word_button = Button(popup, command=change_word, width=20, text='Change the word')
        add_word_button.grid(column=1, row=2)

    def move_to_learned(self):
        self.data.move(self.card)
        self.pick_a_word()

    def add_popup(self):
        popup = Tk()
        popup.title('Add a word')
        popup.config(padx=20, pady=20)

        word_label = Label(popup, text='Word')
        word_label.grid(column=0, row=0)
        word_entry = Entry(popup)
        word_entry.grid(column=1, row=0)

        translate_label = Label(popup, text='Translation')
        translate_label.grid(column=0, row=1)
        translate_entry = Entry(popup)
        translate_entry.grid(column=1, row=1)

        def add_word():
            new_word = word_entry.get()
            new_translation = translate_entry.get()
            self.data.add(new_word, new_translation)
            self.pick_a_word(word=new_word)
            popup.destroy()

        add_word_button = Button(popup, command=add_word, width=20, text='Add the word')
        add_word_button.grid(column=1, row=2)

    def delete_word(self):
        # TODO add confirmation popup
        self.data.delete(self.card)
        self.pick_a_word()

    def space_is_pressed(self, event):
        self.pick_a_word()

    def find_popup(self):
        # TODO implement one entry for word or translation
        popup = Tk()
        popup.title('Find a word')
        popup.config(padx=20, pady=20)

        word_label = Label(popup, text='Word')
        word_label.grid(column=0, row=0)
        word_entry = Entry(popup)
        word_entry.grid(column=1, row=0)

        translate_label = Label(popup, text='Translation')
        translate_label.grid(column=0, row=1)
        translate_entry = Entry(popup)
        translate_entry.grid(column=1, row=1)

        def find_a_word():
            word = ''
            if word_entry.get():
                word = self.data.find(word=word_entry.get())

            elif translate_entry.get():
                word = self.data.find(translation=word_entry.get())
            else:
                messagebox.showerror(title='Error', message='Mate, try to type something.')

            if word == 'not_found':
                messagebox.showerror(title='Error', message="Haven't found anything :(")
            elif word == '':
                pass
            else:
                self.pick_a_word(word=word)

            popup.destroy()

        add_word_button = Button(popup, command=find_a_word, width=20, text='Find')
        add_word_button.grid(column=1, row=2)
        pass
