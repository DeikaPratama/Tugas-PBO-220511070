import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from login import *
from rental import *

class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('')
        # Load background image
        self.background_image = Image.open("foto.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.root.geometry("{}x{}".format(self.background_image.width, self.background_image.height))
        
        self.__data = None
        self.__level = None
        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menus
        self.file_menu = Menu(self.menubar)
        self.guest_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.karyawan_menu = Menu(self.menubar)

        # add menu items to File menu
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # add menu items to menu Admin
        self.admin_menu.add_command(label='Sewa Hajatan', command=lambda: self.new_window("Penyewaan Hajatan", Rental))

        # add menu items to menu Karyawan
        self.karyawan_menu.add_command(label='Sewa Hajatan', command=lambda: self.new_window("Penyewaan Hajatan", Rental))

        # add menus to the menubar
        self.menubar.add_cascade(label="Home", menu=self.file_menu)

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            # tambahkan menu sesuai level
            if(level=='admin'): 
                self.menubar.add_cascade(label="Sewa Hajatan", menu=self.admin_menu)
                self.__level = 'Admin'
            elif(level=='Karyawan'): 
                self.menubar.add_cascade(label="Sewa Hajatan", menu=self.karyawan_menu)
                self.__level = 'Karyawan'
            
            else:
                pass

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
