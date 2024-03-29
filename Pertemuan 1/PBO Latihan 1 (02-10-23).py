import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    pj =float(txtpanjang.get())
    lb =float(txtlebar.get())

    L = round(pj * lb,2)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_keliling():
    pj =float(txtpanjang.get())
    lb =float(txtlebar.get())

    K = round(2 * (pj + lb),2)

    txtKeliling.delete(0,END)
    txtKeliling.insert(END,K)

def hitung():
    hitung_luas()
    hitung_keliling()

# Create tkinker object
app = tk.Tk()

#Tambahkan judul
app.title("Kalkulator Luas Dan Keliling Persegi Panjang")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang
panjang= Label(frame, text="Panjang:")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
lebar= Label(frame, text="Label:")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

# Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Keliling
keliling = Label(frame, text="Keliling: ")
keliling.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtKeliling = Entry(frame)
txtKeliling.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
