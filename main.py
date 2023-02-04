from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from colors import*
import random

# Importing algorithms 
from bubblesort_code import bubble_sort
from insertionsort_code import insertion_sort
from selectionsort_code import selection_sort
from mergesort_code import merge_sort
from quicksort_code import quick_sort

# Main window 
window = Tk()
window.state("zoomed")
window.title("DSA Project")
window.geometry("750x600")
#bg image
bg_org=Image.open('bg.webp')
bg=ImageTk.PhotoImage(bg_org)
bglabel=Label(window,image=bg)
bglabel.place(x=0,y=0)

#global
s='Sorting Algorithm Visualiser'
text=''
count=0
def slider():
    global text,count,s
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count=count+1
    sliderLabel.after(150,slider)

#Slider
sliderLabel=Label(window,font=('arial',35,'bold','italic'),foreground='royalblue',width=30)
sliderLabel.place(x=300,y=25)
slider()
algorithm_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 360
    canvas_width = 1300
    bar_width = canvas_width / (len(data) + 1)
    border_offset = 30
    spacing = 10
    normalized_array = [ i / max(data) for i in data]
    for i, height in enumerate(normalized_array):
        #top left coordinates
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        #bottom right coordinates
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    
    window.update_idletasks()


# Randomly generate array
def generate():
    global data
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())

    data = []
    for i in range(size):
        data.append(random.randrange(lowest, highest+1))

    drawData(data,['red' for x in range(len(data))])


def sort():
    global data
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, sortingspeed.get())
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, sortingspeed.get())
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, sortingspeed.get())
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, sortingspeed.get())
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, sortingspeed.get())


### User interface ###
UI_frame = Frame(window, width= 700, height=300, bg='green')
UI_frame.place(x=450,y=95)

canvas = Canvas(window,width=1340, height=350, bg='grey')
canvas.place(x=10,y=340)

l1 = Label(UI_frame, text="Algorithm Choice : ")
l1.grid(row=0, column=0, padx=10, pady=10)

algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list,width=10) #ttk library
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

sortingspeed = Scale(UI_frame, from_=0.1, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Sorting Speed ")
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

Button(UI_frame, text="Start Sorting",font=('bold'), command=sort, bg='red',height=5).grid(row=0, column=3, padx=5, pady=5)

lowest_Entry = Scale(UI_frame, from_=5, to=20, resolution=1, orient=HORIZONTAL, label="Lower Limit")
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(UI_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="Upper Limit")
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(UI_frame, from_=5, to=25, resolution=1, orient=HORIZONTAL, label="Array size")
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Current Array",font=('bold'), command=generate, bg='blue',height=5).grid(row=1, column=3, padx=10, pady=10)

window.mainloop()