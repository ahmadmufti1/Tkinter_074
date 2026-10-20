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

# Membuat 10 Input Nilai Mata Pelajaran
for i, mapel in enumerate(mapel_list):
    lbl = tk.Label(
        frame_input,
        text=f"{mapel}:",
        font=("Helvetica", 9),
        anchor="w",
        bg="#f0f4f8",
        width=18,
    )
    lbl.grid(row=i, column=0, padx=5, pady=4, sticky="w")

    entry = ttk.Entry(frame_input, width=15)
    entry.grid(row=i, column=1, padx=5, pady=4)
    entries.append(entry)

# Tombol "Hasil Prediksi"
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    command=prediksi_prodi,
    font=("Helvetica", 10, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    padx=15,
    pady=5,
    relief="flat",
    cursor="hand2",
)
btn_prediksi.pack(pady=15)

# Label Luaran Hasil Prediksi
label_hasil = tk.Label(
    root,
    text="Hasil Prediksi: -",
    font=("Helvetica", 11, "bold"),
    fg="#0f766e",
    bg="#f0f4f8",
)
label_hasil.pack(pady=(0, 20))
