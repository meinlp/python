from tkinter import *

window = Tk()
window.title('Music library exporter')
window.config(padx=20, pady=30)

label = Label()
label.config(text='Choose source\nand destination')
label.grid(column=1, row=0)

arrow = Label()
arrow.config(text='➔')
arrow.grid(column=1, row=2)


# Radiobutton
def music_from():
    print(from_state.get())


def music_to():
    print(to_state.get())


# Variable to hold on to which radio button value is checked.
from_state = IntVar()
spotify_from = Radiobutton(text="spotify", value=1, variable=from_state, command=music_from)
apple_music_from = Radiobutton(text="apple_music", value=2, variable=from_state, command=music_from)
yandex_music_from = Radiobutton(text="yandex_music", value=3, variable=from_state, command=music_from)

spotify_from.grid(column=0, row=1, sticky='w')
apple_music_from.grid(column=0, row=2, sticky='w')
yandex_music_from.grid(column=0, row=3, sticky='w')

to_state = IntVar()
spotify_to = Radiobutton(text="spotify", value=1, variable=to_state, command=music_to)
apple_music_to = Radiobutton(text="apple_music", value=2, variable=to_state, command=music_to)
yandex_music_to = Radiobutton(text="yandex_music", value=3, variable=to_state, command=music_to)

spotify_to.grid(column=2, row=1, sticky='w')
apple_music_to.grid(column=2, row=2, sticky='w')
yandex_music_to.grid(column=2, row=3, sticky='w')

get_playlists = Button(text='Get playlists', command=music_from, width=35)
get_playlists.grid(column=0, row=4, columnspan=3, sticky='w')


def listbox_used(event):
    if listbox_playlists.get(listbox_playlists.curselection()):
        print(listbox_playlists.get(listbox_playlists.curselection()))


listbox_playlists = Listbox(height=7, width=38)
playlists = []
for item in playlists:
    listbox_playlists.insert(playlists.index(item), item)
listbox_playlists.bind("<<ListboxSelect>>", listbox_used)
listbox_playlists.grid(column=0, row=5, columnspan=3, sticky='w', pady=5)

space = Label()
space.config(text='')
space.grid(column=0, row=6)

get_songs = Button(text='Get songs', command=music_from, width=35)
get_songs.grid(column=0, row=7, columnspan=3, sticky='w')


def listbox_used(event):
    if listbox_songs.get(listbox_playlists.curselection()):
        print(listbox_songs.get(listbox_playlists.curselection()))


listbox_songs = Listbox(height=7, width=38)
songs = []
for item in songs:
    listbox_songs.insert(playlists.index(item), item)
listbox_songs.bind("<<ListboxSelect>>", listbox_used)
listbox_songs.grid(column=0, row=8, columnspan=3, sticky='w', pady=5)

space = Label()
space.config(text='')
space.grid(column=0, row=9)

get_songs = Button(text='Transfer', command=music_from, width=35)
get_songs.grid(column=0, row=10, columnspan=3, sticky='w')
