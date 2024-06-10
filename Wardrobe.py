import mysql.connector as sq
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk

con = sq.connect(host='localhost', user='root', passwd='', database='wardrobe', port=3306)
cur = con.cursor()


frame = tk.Tk()
frame.title('YOUR WARDROBE')
width_value = frame.winfo_screenwidth()
height_value = frame.winfo_screenheight()
frame.geometry('%dx%d+0+0' % (width_value, height_value))

# Make sure the image files exist in the correct path
render1 = ImageTk.PhotoImage(Image.open('bg.jpg'))
img_center = tk.Label(frame, image=render1)
img_center.place(x=0, y=0)
original = Image.open('home.png')
resized = original.resize((50, 50),)
render2 = ImageTk.PhotoImage(resized)

original = Image.open('delete_logo.png')
resized = original.resize((50, 50),)
render3 = ImageTk.PhotoImage(resized)
original_plus = Image.open('plus.png')
resized_plus = original_plus.resize((50, 50),)  # Adjust the size (50, 50) as needed
render4 = ImageTk.PhotoImage(resized_plus)

def cmd1():
    cur.execute('SELECT * FROM wardrobe')
    rows = cur.fetchall()
    top = tk.Toplevel(frame)
    top.title('All Records')
    # Set the dimensions for the Toplevel window (80% of the main window)
    width = frame.winfo_screenwidth() * 0.8
    height = frame.winfo_screenheight() * 0.8
    top.geometry('%dx%d' % (width, height))

    frm1 = tk.Frame(top)
    frm1.pack(fill='both', expand=True)

    tv = ttk.Treeview(frm1, columns=(1, 2, 3, 4), show='headings', height='20')
    tv.pack(expand=True, fill='both')

    tv.heading(1, text='code')
    tv.heading(2, text='type')
    tv.heading(3, text='brand')
    tv.heading(4, text='colour')

    for i in rows:
        tv.insert('', 'end', values=i)

    # Use the already resized image for the button
    bt1_back = tk.Button(frm1, command=top.destroy, image=render2)
    bt1_back.image = render2  # Keep a reference to the image
    bt1_back.pack(side='bottom')

def cmd2():
    top = tk.Toplevel(frame)
    top.title('Search Records')
    # Adjust the size of the window as needed or use the full screen
    top.geometry('%dx%d+0+0' % (width_value, height_value))

    frm2 = tk.Frame(top)
    frm2.pack(fill='both', expand=True)  # This should make frm2 fill the entire Toplevel window

    s1 = tk.Entry(frm2, font=('Arial', 25))
    s1.pack(pady=20)

    tv = ttk.Treeview(frm2, columns=(1, 2, 3, 4), show='headings')
    tv.pack(expand=True, fill='both')
    tv.heading(1, text='Code')
    tv.heading(2, text='Type')
    tv.heading(3, text='Brand')
    tv.heading(4, text='Colour')

    def search_db(column, val):
        cur.execute(f'SELECT * FROM wardrobe WHERE {column}=%s', (val,))
        rows = cur.fetchall()
        tv.delete(*tv.get_children())  # Clear the current view
        for i in rows:
            tv.insert('', 'end', values=i)

    def cmd2_1():
        val = s1.get()
        search_db('code', val)

    def cmd2_2():
        val = s1.get()
        search_db('type', val)

    def cmd2_3():
        val = s1.get()
        search_db('brand', val)

    def cmd2_4():
        val = s1.get()
        search_db('colour', val)

    cmd2b1 = tk.Button(frm2, text='SEARCH BY CODE', command=cmd2_1, font=("Arial", 20))
    cmd2b1.pack(fill='x', pady=10)
    cmd2b2 = tk.Button(frm2, text='SEARCH BY TYPE', command=cmd2_2, font=("Arial", 20))
    cmd2b2.pack(fill='x', pady=10)
    cmd2b3 = tk.Button(frm2, text='SEARCH BY BRAND', command=cmd2_3, font=("Arial", 20))
    cmd2b3.pack(fill='x', pady=10)
    cmd2b4 = tk.Button(frm2, text='SEARCH BY COLOUR', command=cmd2_4, font=("Arial", 20))
    cmd2b4.pack(fill='x', pady=10)
    back = tk.Button(frm2, text='BACK', command=top.destroy, font=("ArialBlack", 25))
    back.pack(pady=20)

def cmd3():
    top = tk.Toplevel(frame)
    top.title('Delete Record')
    # Adjust the size of the window as needed or use the full screen
    top.geometry('%dx%d+0+0' % (width_value, height_value))

    frm3 = tk.Frame(top)
    frm3.pack(fill='both', expand=True)  # This should make frm3 fill the entire Toplevel window

    lbl = tk.Label(frm3, text='Code of item to be deleted', font=('Arial', 25))
    lbl.pack(padx=10, pady=20)

    s2 = tk.Entry(frm3, font=('Arial', 25))
    s2.pack(padx=10, pady=20)

    def cmd3_1():
        val = s2.get()
        cur.execute('DELETE FROM wardrobe WHERE code=%s', (val,))
        con.commit()
        messagebox.showinfo('Success', 'Deleted successfully.')
        top.destroy()  # Close the Toplevel window after deleting

    delete = tk.Button(frm3, command=cmd3_1, image=render3)
    delete.image = render3  # Keep a reference to the image
    delete.pack(pady=20)

    back = tk.Button(frm3, image=render2, command=top.destroy)
    back.image = render2  # Keep a reference to the image
    back.pack(pady=20)


def cmd4():
    top = tk.Toplevel(frame)
    top.title('Add New Record')
    # Adjust the size of the window as needed or use the full screen
    top.geometry('%dx%d+0+0' % (width_value, height_value))

    frm4 = tk.Frame(top)
    frm4.pack(fill='both', expand=True)  # This should make frm4 fill the entire Toplevel window
    
    # Create and grid the labels and entries with padding for better layout
    lbl1 = tk.Label(frm4, text='Enter code', font=("Arial", 25))
    lbl1.grid(row=0, column=0, padx=10, pady=10)
    e1 = tk.Entry(frm4, font=('Arial', 25))
    e1.grid(row=0, column=1, padx=10, pady=10)

    lbl2 = tk.Label(frm4, text='Enter type', font=("Arial", 25))
    lbl2.grid(row=1, column=0, padx=10, pady=10)
    e2 = tk.Entry(frm4, font=('Arial', 25))
    e2.grid(row=1, column=1, padx=10, pady=10)

    lbl3 = tk.Label(frm4, text='Enter brand', font=("Arial", 25))
    lbl3.grid(row=2, column=0, padx=10, pady=10)
    e3 = tk.Entry(frm4, font=('Arial', 25))
    e3.grid(row=2, column=1, padx=10, pady=10)

    lbl4 = tk.Label(frm4, text='Enter colour', font=("Arial", 25))
    lbl4.grid(row=3, column=0, padx=10, pady=10)
    e4 = tk.Entry(frm4, font=('Arial', 25))
    e4.grid(row=3, column=1, padx=10, pady=10)

    def cmd4_1():
        val1 = e1.get()
        val2 = e2.get()
        val3 = e3.get()
        val4 = e4.get()
        qry = "INSERT INTO wardrobe (code, type, brand, colour) VALUES (%s, %s, %s, %s)"
        cur.execute(qry, (val1, val2, val3, val4))
        con.commit()
        messagebox.showinfo('Success', 'Record added successfully.')

    # Place the 'plus' button for submitting the form
    done = tk.Button(frm4, command=cmd4_1, image=render4)
    done.image = render4  # Keep a reference to the image
    done.grid(row=4, column=1, padx=10, pady=10)

    # Place the 'home' button
    home_button = tk.Button(frm4, image=render2, command=lambda: top.destroy())  # Closes the Toplevel window
    home_button.image = render2  # Keep a reference to the image
    home_button.grid(row=4, column=2, padx=10, pady=10)

AB = 'ArialBlack'
MSB = 'mediumslateblue'
LV = 'lavender'
bt1 = tk.Button(frame, text='ALL RECORDS', command=cmd1, font=(AB, 25), bg=MSB, fg=LV)
bt1.pack(side='top', pady=25)
bt2 = tk.Button(frame, text='SEARCH', command=cmd2, font=(AB, 25), bg=MSB, fg=LV)
bt2.pack(side='bottom', pady=40)
bt3 = tk.Button(frame, text='DELETE RECORDS', command=cmd3, font=(AB, 25), bg=MSB, fg=LV)
bt3.pack(side='right', padx=25)
bt4 = tk.Button(frame, text='ADD NEW RECORD', command=cmd4, font=(AB, 25), bg=MSB, fg=LV)
bt4.pack(side='left', padx=25)

frame.mainloop()
