import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import openpyxl


class Rental:
    def __init__(self, root, username, on_logout):
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.append(["Tanggal", "Nama", "Nomor WhatsApp", "Alamat", "Properti", "Durasi", "Total Biaya"])
        
        self.root = root
        self.username = username
        self.on_logout = on_logout

        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack()

        self.name_label = tk.Label(self.frame, text="Nama:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()

        self.phone_label = tk.Label(self.frame, text="Nomor WhatsApp:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.pack()

        self.address_label = tk.Label(self.frame, text="Alamat:")
        self.address_label.pack()

        self.address_entry = tk.Entry(self.frame)
        self.address_entry.pack()
        self.property_label = tk.Label(self.frame, text="Pilih Properti:")
        self.property_label.pack()

        self.properties = {
            "Kursi Tamu": 1000000,
            "Tenda": 4000000,
            "Katering": 2000000,
            "Dekorasi Pelaminan": 2000000,
            "Kursi & Meja Akad": 500000
        }

        self.property_combobox = ttk.Combobox(self.frame, values=list(self.properties.keys()))
        self.property_combobox.pack()

        self.duration_label = tk.Label(self.frame, text="Durasi (hari):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(self.frame)
        self.duration_entry.pack()

        self.calculate_button = tk.Button(self.frame, text="Input Data", command=self.calculate_cost)
        self.calculate_button.pack()

        self.total_cost_label = tk.Label(self.frame)
        self.total_cost_label.pack()

        self.logout_button = tk.Button(self.frame, text="Logout", command=self.logout)
        self.logout_button.pack()

    def calculate_cost(self):
        property_name = self.property_combobox.get()
        duration = int(self.duration_entry.get())

        property_cost = self.properties[property_name]
        total_cost = property_cost * duration

        # Tanggal otomatis berdasarkan durasi
        rental_date = datetime.now().strftime('%Y-%m-%d')
        return_date = (datetime.now() + timedelta(days=duration)).strftime('%Y-%m-%d')

        # Tampilkan tanggal sewa dan kembalikan di label
        self.rental_date_label = tk.Label(self.frame, text=f"Tanggal Sewa: {rental_date}")
        self.rental_date_label.pack()
        self.return_date_label = tk.Label(self.frame, text=f"Tanggal Kembali: {return_date}")
        self.return_date_label.pack()

        # Simpan data ke dalam tabel database
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        # Menyimpan data ke dalam file notepad
        filename = f"data_{rental_date}.txt"
        with open(filename, 'a') as file:
            data_to_write = f"Nama: {name}\nNomor WhatsApp: {phone}\nAlamat: {address}\nProperti: {property_name}\nDurasi: {duration} hari\nTotal Biaya: {total_cost:,} IDR\n\n"
            file.write(data_to_write)

        self.conn.execute('''INSERT INTO Rentals (username, property_name, duration, total_cost, name, phone, address)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (self.username, property_name, duration, total_cost, name, phone, address))
        self.conn.commit()

        messagebox.showinfo("Informasi", f"Total Biaya: {total_cost:,} IDR")


    def logout(self):
        self.on_logout()
        self.destroy()

    def destroy(self):
        self.frame.destroy()
        self.conn.close()

def on_logout():
    print("Logout berhasil")

root = tk.Tk()
app = Rental(root, "Username", on_logout)
root.mainloop()


