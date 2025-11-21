import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    try:
        nilai = float(entry_suhu.get())
        jenis = combo.get()

        if jenis == "Celsius ke Fahrenheit":
            hasil = (nilai * 9/5) + 32
            label_hasil.config(text=f"{hasil:.2f} °F")
        elif jenis == "Fahrenheit ke Celsius":
            hasil = (nilai - 32) * 5/9
            label_hasil.config(text=f"{hasil:.2f} °C")
        elif jenis == "Celsius ke Kelvin":
            hasil = nilai + 273.15
            label_hasil.config(text=f"{hasil:.2f} K")
        elif jenis == "Kelvin ke Celsius":
            hasil = nilai - 273.15
            label_hasil.config(text=f"{hasil:.2f} °C")
        else:
            label_hasil.config(text="Pilih jenis konversi!")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid!")

# --- GUI Setup ---
window = tk.Tk()
window.title("Konverter Suhu")
window.geometry("350x250")
window.resizable(False, False)

label_judul = tk.Label(window, text="Konversi Suhu", font=("Arial", 16))
label_judul.pack(pady=10)

entry_suhu = tk.Entry(window, font=("Arial", 12))
entry_suhu.pack(pady=5)

combo = ttk.Combobox(window, font=("Arial", 11), state="readonly")
combo['values'] = [
    "Celsius ke Fahrenheit",
    "Fahrenheit ke Celsius",
    "Celsius ke Kelvin",
    "Kelvin ke Celsius"
]
combo.pack(pady=5)
combo.current(0)

btn = tk.Button(window, text="Konversi", font=("Arial", 12), command=konversi_suhu)
btn.pack(pady=10)

label_hasil = tk.Label(window, text="", font=("Arial", 14), fg="blue")
label_hasil.pack(pady=10)

window.mainloop()
