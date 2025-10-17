import tkinter as tk
from PIL import ImageTk, Image

bg_color = '#3d6466'

def load_frame_home():
    # child label element overwritting parent frame element
    frame.pack_propagate(False)

    ## --frame widgets

    ## logo image
    img = Image.open('assets/sql_dockter.png')

    img_size = (200,200)
    img.thumbnail(img_size)

    logo_img = ImageTk.PhotoImage(img)
    logo_widget = tk.Label(frame, image=logo_img, bg=bg_color,
                        justify='center')
    logo_widget.image = logo_img
    logo_widget.pack(expand=True)

    ## fonts
    tk.Label(
        frame, text='Meow Meow',
        bg=bg_color, fg='white',
        font=('TkMenuFont', 14)
    ).pack()

    ## button
    tk.Button(
        frame, text='Press Meow',
        font=('TkHeadingFont', 20),
        bg='#28393a', fg='white',
        cursor='hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:load_frame1()
    ).pack(pady=20)

def load_frame1():
    print('Meow Neow!')

root = tk.Tk()

root.title('SQLDock')

## position of the window
# root.eval('tk::PlaceWindow . center')
# x = root.winfo_screenwidth() // 2
# y = int(root.winfo_screenheight() * 0.1)
# root.geometry('300x300+' + str(x) + '+' + str(y))


## frame creation
frame = tk.Frame(root, width=600, height=500, bg=bg_color)
frame1 = tk.Frame(root, bg=bg_color)
frame.grid(row=0, column=0)
frame1.grid(row=0, column=0)

# for frame in (frame, frame1):
#     frame.grid(row=0, column=0)

load_frame_home()

root.mainloop()