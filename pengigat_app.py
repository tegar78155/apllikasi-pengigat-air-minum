import tkinter as tk
from tkinter import messagebox

# List jadwal minum
jadwal_minum = []

# Fungsi untuk menambahkan jadwal
def tambah_jadwal():
    waktu = entry_waktu.get()
    if waktu:
        jadwal_minum.append(waktu)  # append()
        jadwal_minum.sort()         # sort()
        update_listbox()
        entry_waktu.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Masukkan waktu terlebih dahulu!")

# Fungsi untuk menyisipkan jadwal di posisi tertentu
def sisipkan_jadwal():
    waktu = entry_waktu.get()
    try:
        posisi = int(entry_posisi.get())
        jadwal_minum.insert(posisi, waktu)  # insert()
        jadwal_minum.sort()                 # sort()
        update_listbox()
        entry_waktu.delete(0, tk.END)
        entry_posisi.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Posisi harus berupa angka!")

# Fungsi untuk menghapus jadwal terpilih
def hapus_jadwal():
    selected = listbox.curselection()
    if selected:
        waktu = listbox.get(selected)
        jadwal_minum.remove(waktu)  # remove()
        update_listbox()
    else:
        messagebox.showwarning("Peringatan", "Pilih jadwal yang ingin dihapus!")

# Fungsi untuk menghapus jadwal terakhir
def hapus_terakhir():
    if jadwal_minum:
        jadwal_minum.pop()  # pop()
        update_listbox()

# Fungsi untuk memperbarui listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for waktu in jadwal_minum:
        listbox.insert(tk.END, waktu)

# Fungsi untuk simulasi pengingat
def mulai_pengingat():
    if jadwal_minum:
        message = "Pengingat minum air:\n"
        for waktu in jadwal_minum:
            message += f"⏰ {waktu}\n"
        messagebox.showinfo("Pengingat Minum", message)
    else:
        messagebox.showwarning("Kosong", "Tidak ada jadwal untuk diingatkan.")

# === GUI SETUP ===
root = tk.Tk()
root.title("💧 Pengingat Minum Air Harian")

# Entry waktu
tk.Label(root, text="Masukkan Waktu (HH:MM):").grid(row=0, column=0, sticky="w")
entry_waktu = tk.Entry(root)
entry_waktu.grid(row=0, column=1)

# Entry posisi untuk insert
tk.Label(root, text="Posisi (opsional untuk sisip):").grid(row=1, column=0, sticky="w")
entry_posisi = tk.Entry(root)
entry_posisi.grid(row=1, column=1)

# Tombol-tombol
tk.Button(root, text="Tambah Jadwal", command=tambah_jadwal).grid(row=2, column=0, pady=5)
tk.Button(root, text="Sisipkan Jadwal", command=sisipkan_jadwal).grid(row=2, column=1, pady=5)
tk.Button(root, text="Hapus Terpilih", command=hapus_jadwal).grid(row=3, column=0)
tk.Button(root, text="Hapus Terakhir", command=hapus_terakhir).grid(row=3, column=1)
tk.Button(root, text="Mulai Pengingat", command=mulai_pengingat).grid(row=4, column=0, columnspan=2, pady=10)

# Listbox jadwal
listbox = tk.Listbox(root, width=30)
listbox.grid(row=5, column=0, columnspan=2)

# Jalankan GUI
root.mainloop()
