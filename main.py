import tkinter as tk
from tkinter import messagebox

# Görevleri saklamak için liste
tasks = []

# Görev ekleme fonksiyonu
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
    else:
        messagebox.showwarning("Uyarı", "Boş görev ekleyemezsiniz!")
    task_entry.delete(0, tk.END)

# Görev listesi güncelleme fonksiyonu
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Görev silme fonksiyonu
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Uyarı", "Seçili görev yok!")

# Uygulama penceresi oluşturma
root = tk.Tk()
root.title("Yapılacaklar Listesi")

# Giriş alanı ve düğme
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Görev Ekle", command=add_task)
add_task_button.pack(pady=5)

# Görev listesi
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Silme düğmesi
delete_task_button = tk.Button(root, text="Seçili Görevi Sil", command=delete_task)
delete_task_button.pack(pady=5)

# Uygulama döngüsünü başlatma
root.mainloop()
