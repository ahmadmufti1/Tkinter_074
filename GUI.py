import tkinter as tk

# •Buatlah GUI dengan Tkinter yang berisi:
#    –1 label judul Aplikasi prediksi Prodi Pilihan
#    –10 input nilai mata pelajaran
#    –1 button bertuliskan Hasil Prediksi
#    –1 label luaran hasil prediksi
# •Atur posisi GUI sebaik mungkin!
# •Fungsi Hasil Prediksi menuliskan prodi TeknologiInformasi apapun input yang diberikan!
from tkinter import ttk

def prediksi_prodi():
    # untuk menampilkan "Teknologi Informasi" apa pun inputnya
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")


# Membuat Window Utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x520")
root.configure(bg="#f0f4f8")

# Label Judul
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    fg="#1e293b",
)

# Frame untuk pembungkus Input Mata Pelajaran
frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(padx=20, pady=5)

# Daftar Mata Pelajaran
mapel_list = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "IBD",
    "PM",
    "PROBSTAT",
    "Pancasila",
    "Teknologi Server",
    "Switching",
    "Informatika",
]

entries = []
