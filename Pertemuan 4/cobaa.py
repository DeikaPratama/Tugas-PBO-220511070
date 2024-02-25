import tkinter as tk
from tkinter import ttk, messagebox
import math

def hitung_luas():
    jenis_bangun_ruang = jenis_bangun_ruang_var.get()

    if jenis_bangun_ruang == "Kubus":
        rusuk = float(rusuk_entry.get())
        luas = 6 * rusuk ** 2
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")

    elif jenis_bangun_ruang == "Balok":
        panjang = float(panjang_entry.get())
        lebar = float(lebar_entry.get())
        tinggi = float(tinggi_entry.get())
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")

    elif jenis_bangun_ruang == "Limas Segiempat":
        alas = float(alas_entry.get())
        tinggi = float(tinggi_entry.get())
        luas_sisi = 4*alas*tinggi
        luas_alas = sisi*sisi
        luas =  luas_sisi + luas_sisi + luas_sisi + luas_sisi + luas_sisi
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")

    elif jenis_bangun_ruang == "Prisma Segitiga":
        alas = float(alas_entry.get())
        tinggi = float(tinggi_entry.get())
        sisi = float(sisi_entry.get())
        TinggiPrisma = float(TinggiPrisma_entry.get())
        Keliling_segitiga = (sisi+sisi+sisi)
        Luas_segitiga = alas*tinggi/2
        Luas_sisi1 = Keliling_segitiga*TinggiPrisma
        Luas_sisi2 = 2*Luas_segitiga
        luas =  Luas_sisi1 + Luas_sisi2
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")

    elif jenis_bangun_ruang == "Limas Segitiga":
        alas = float(alas_entry.get())
        tinggi = float(tinggi_entry.get())
        luas_alas = alas*tinggi/2
        luas_sisi = alas*tinggi/2
        luas = luas_sisi+luas_sisi+luas_sisi+luas_sisi
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")
        
    elif jenis_bangun_ruang == "Tabung":
        jari_jari = float(jari_jari_entry.get())
        tinggi_tabung = float(tinggi_tabung_entry.get())
        luas = 2 * math.pi * jari_jari * (jari_jari + tinggi_tabung)
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")

    elif jenis_bangun_ruang == "Kerucut":
        jari_jari = float(jari_jari_entry.get())
        s = float(s_entry.get())
        luas = (math.pi*jari_jari*jari_jari) + (math.pi*jari_jari*s)
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")

    elif jenis_bangun_ruang == "Bola":
        jari_jari = float(jari_jari_entry.get())
        tinggi = float(tinggi_entry.get())
        luas = (2*math.pi*jari_jari*jari_jari)+(2*math.pi*jari_jari*tinggi)
        hasil_label.config(text=f"Luas {jenis_bangun_ruang}: {luas:.2f} satuan persegi")

    else:
        messagebox.showwarning("Peringatan", "Pilih jenis bangun ruang terlebih dahulu.")

def hitung_volume():
    jenis_bangun_ruang = jenis_bangun_ruang_var.get()

    if jenis_bangun_ruang == "Kubus":
        rusuk = float(rusuk_entry.get())
        volume = rusuk ** 3
        hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    elif jenis_bangun_ruang == "Balok":
        panjang = float(panjang_entry.get())
        lebar = float(lebar_entry.get())
        tinggi = float(tinggi_entry.get())
        volume = panjang * lebar * tinggi
        hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    elif jenis_bangun_ruang == "Limas Segiempat":
         sisi = float(sisi_entry.get())
         tinggi = float(tinggi_entry.get)
         luas_alas = sisi ** 2
         volume = luas_alas*tinggi/3
         hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    elif jenis_bangun_ruang == "Prisma Segitiga": 
         alas = float(alas_entry.get())
         tinggi = float(tinggi_entry.get())
         TinggiPrisma = float(TinggiPrisma_entry.get())
         volume = alas*tinggi*TinggiPrisma/2
         hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    elif jenis_bangun_ruang == "Limas Segitiga":
         alas = float(alas_entry.get())
         tinggi = float(tinggi_entry.get())
         TinggiPrisma = float(TinggiPrisma_entry.get())
         luas_alas = alas*tinggi/2
         volume = luas_alas*TinggiPrisma/3
         hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    elif jenis_bangun_ruang == "Tabung":
        jari_jari = float(jari_jari_entry.get())
        tinggi_tabung = float(tinggi_tabung_entry.get())
        volume = math.pi * jari_jari ** 2 * tinggi_tabung
        hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    elif jenis_bangun_ruang == "Kerucut":
        jari_jari = float(jari_jari_entry.get())
        tinggi_tabung = float(tinggi_tabung_entry.get())
        volume = math.pi * jari_jari  *jari_jari*tinggi_tabung/3
        hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    elif jenis_bangun_ruang == "Bola":
        jari_jari = float(jari_jari_entry.get())
        volume = 4/3 * math.pi * jari_jari ** 3
        hasil_label.config(text=f"Volume {jenis_bangun_ruang}: {volume:.2f} satuan kubik")

    else:
        messagebox.showwarning("Peringatan", "Pilih jenis bangun ruang terlebih dahulu.")

# Membuat jendela utama
root = tk.Tk()
root.title("Hitung Luas dan Volume Bangun Ruang")

# Membuat frame utama
main_frame = ttk.Frame(root, padding=(20, 10))
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Membuat label dan OptionMenu untuk memilih jenis bangun ruang
jenis_label = ttk.Label(main_frame, text="Jenis Bangun Ruang:")
jenis_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

jenis_bangun_ruang_var = tk.StringVar(root)
jenis_bangun_ruang_var.set("Kubus" )  # Nilai default
jenis_bangun_ruang_options = ["Kubus", "Balok", "Limas Segiempat" , "Prisma Segitiga" , "Limas Segitiga" , "Tabung" , "Kerucut" , "Bola" ]
bangun_ruang_menu = ttk.OptionMenu(main_frame, jenis_bangun_ruang_var, *jenis_bangun_ruang_options)
bangun_ruang_menu.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

# Membuat label dan entry untuk sisi (kubus)
rusuk_label = ttk.Label(main_frame, text="Rusuk (Kubus):")
rusuk_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

rusuk_entry = ttk.Entry(main_frame)
rusuk_entry.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk panjang, lebar, dan tinggi (balok)
panjang_label = ttk.Label(main_frame, text="Panjang (Balok):")
panjang_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

panjang_entry = ttk.Entry(main_frame)
panjang_entry.grid(row=2, column=1, padx=10, pady=5)

lebar_label = ttk.Label(main_frame, text="Lebar (Balok):")
lebar_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

lebar_entry = ttk.Entry(main_frame)
lebar_entry.grid(row=3, column=1, padx=10, pady=5)

tinggi_label = ttk.Label(main_frame, text="Tinggi (Balok):")
tinggi_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

tinggi_entry = ttk.Entry(main_frame)
tinggi_entry.grid(row=4, column=1, padx=10, pady=5)

# Membuat label dan entry untuk alas dan tinggi (limas segiempat)
alas_label = ttk.Label(main_frame, text="Alas (Limas Segiempat): ")
alas_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

alas_entry = ttk.Entry(main_frame)
alas_entry.grid(row=5, column=1, padx=10, pady=5)

tinggi_label = ttk.Label(main_frame, text="Tinggi (Limas Segiempat): ")
tinggi_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

tinggi_entry = ttk.Entry(main_frame)
tinggi_entry.grid(row=6, column=1, padx=10, pady=5)

# Membuat label dan entry untuk sisi, alas dan tinggi (prisma segitiga)
sisi_label = ttk.Label(main_frame, text="Sisi (Prisma Segitiga): ")
sisi_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)

sisi_entry = ttk.Entry(main_frame)
sisi_entry.grid(row=7, column=1, padx=10, pady=5)

alas_label = ttk.Label(main_frame, text="Alas (Prisma Segitiga): ")
alas_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)

alas_entry = ttk.Entry(main_frame)
alas_entry.grid(row=8, column=1, padx=10, pady=5)

tinggi_label = ttk.Label(main_frame, text="Tinggi (Prisma Segitiga): ")
tinggi_label.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)

tinggi_entry = ttk.Entry(main_frame)
tinggi_entry.grid(row=9, column=1, padx=10, pady=5)

#Membuat label dan entry untuk alas,tinggi dan Tinggi Prisma (limas segitiga)
alas_label = ttk.Label(main_frame, text="Alas (Limas Segitiga): ")
alas_label.grid(row=10, column=0, padx=10, pady=5, sticky=tk.W)

alas_entry = ttk.Entry(main_frame)
alas_entry.grid(row=10, column=1, padx=10, pady=5)

tinggi_label = ttk.Label(main_frame, text="Tinggi (Limas Segitiga): ")
tinggi_label.grid(row=11, column=0, padx=10, pady=5, sticky=tk.W)

tinggi_entry = ttk.Entry(main_frame)
tinggi_entry.grid(row=11, column=1, padx=10, pady=5)

TinggiPrisma_label = ttk.Label(main_frame, text="Tinggi Prisma (Limas Segitiga): ")
TinggiPrisma_label.grid(row=12, column=0, padx=10, pady=5, sticky=tk.W)

TinggiPrisma_entry = ttk.Entry(main_frame)
TinggiPrisma_entry.grid(row=12, column=1, padx=10, pady=5)

# Membuat label dan entry untuk jari-jari dan tinggi (tabung)
jari_jari_label = ttk.Label(main_frame, text="Jari-Jari (Tabung): ")
jari_jari_label.grid(row=13, column=0, padx=10, pady=5, sticky=tk.W)

jari_jari_entry = ttk.Entry(main_frame)
jari_jari_entry.grid(row=13, column=1, padx=10, pady=5)

tinggi_tabung_label = ttk.Label(main_frame, text="Tinggi (Tabung): ")
tinggi_tabung_label.grid(row=14, column=0, padx=10, pady=5, sticky=tk.W)

tinggi_tabung_entry = ttk.Entry(main_frame)
tinggi_tabung_entry.grid(row=14, column=1, padx=10, pady=5)

#Membuat label dan entry untuk jari-jari,tinggi dan S (kerucut)
jari_jari_label = ttk.Label(main_frame, text="Jari-Jari (Kerucut): ")
jari_jari_label.grid(row=15, column=0, padx=10, pady=5, sticky=tk.W)

jari_jari_entry = ttk.Entry(main_frame)
jari_jari_entry.grid(row=15, column=1, padx=10, pady=5)

tinggi_tabung_label = ttk.Label(main_frame, text="Tinggi (Kerucut): ")
tinggi_tabung_label.grid(row=16, column=0, padx=10, pady=5, sticky=tk.W)

tinggi_tabung_entry = ttk.Entry(main_frame)
tinggi_tabung_entry.grid(row=16, column=1, padx=10, pady=5)

s_label = ttk.Label(main_frame, text="s (Kerucut): ")
s_label.grid(row=17, column=0, padx=10, pady=5, sticky=tk.W)

s_entry = ttk.Entry(main_frame)
s_entry.grid(row=17, column=1, padx=10, pady=5)

#Membuat label dan entry untuk jari-jari (bola)
jari_jari_label = ttk.Label(main_frame, text="Jari-Jari (Bola): ")
jari_jari_label.grid(row=18, column=0, padx=10, pady=5, sticky=tk.W)

jari_jari_entry = ttk.Entry(main_frame)
jari_jari_entry.grid(row=18, column=1, padx=10, pady=5)

# Membuat tombol untuk menghitung luas dan volume
luas_button = ttk.Button(main_frame, text="Hitung Luas", command=hitung_luas)
luas_button.grid(row=19, column=0, pady=10)

volume_button = ttk.Button(main_frame, text="Hitung Volume", command=hitung_volume)
volume_button.grid(row=19, column=1, pady=10)

# Membuat label untuk menampilkan hasil
hasil_label = ttk.Label(main_frame, text="Hasil akan muncul di sini.")
hasil_label.grid(row=20, column=0, columnspan=2, pady=5)

# Menjalankan loop utama Tkinter
root.mainloop()