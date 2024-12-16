import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Додайте цей імпорт для роботи із зображеннями
import subprocess

# Функції для відкриття ігор
def open_game1():
    try:
        subprocess.run(['python', 'game1/game1.py'])
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відкрити гру 1: {e}")

def open_game2():
    try:
        subprocess.run(['python', 'game2/game2.py'])
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відкрити гру 2: {e}")

def open_game3():
    try:
        subprocess.run(['python', 'game3/game3.py'])
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відкрити гру 3: {e}")
        
def open_game4():
    try:
        subprocess.run(['python', 'game4/game4.py'])
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відкрити гру 4: {e}")
        
def open_game5():
    try:
        subprocess.run(['python', 'game5/game5.py'])
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відкрити гру 5: {e}")
        
def open_game6():
    try:
        subprocess.run(['python', 'game6/main.py'])
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відкрити гру 6: {e}")

# Створюємо вікно
root = tk.Tk()
root.title("Телефон")
root.geometry("300x500")

# Завантажуємо зображення для фону
background_image = Image.open('phone_screen.jpg')  # Вкажіть шлях до вашого зображення
background_photo = ImageTk.PhotoImage(background_image)

# Створюємо Label для фону
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Встановлюємо фон на всю область вікна

# Завантажуємо іконки для кнопок
game1_image = ImageTk.PhotoImage(Image.open("game1_icon.jpg").resize((50, 50)))
game2_image = ImageTk.PhotoImage(Image.open("game2_icon.png").resize((50, 50)))
game3_image = ImageTk.PhotoImage(Image.open("game3_icon.png").resize((50, 50)))
game4_image = ImageTk.PhotoImage(Image.open("game4_icon.png").resize((50, 50)))
game5_image = ImageTk.PhotoImage(Image.open("game5_icon.png").resize((50, 50)))
game6_image = ImageTk.PhotoImage(Image.open("game6_icon.jpg").resize((50, 50)))

# Іконки для запуску ігор
game1_icon = tk.Button(root, image=game1_image, command=open_game1, borderwidth=0)
game2_icon = tk.Button(root, image=game2_image, command=open_game2, borderwidth=0)
game3_icon = tk.Button(root, image=game3_image, command=open_game3, borderwidth=0)
game4_icon = tk.Button(root, image=game4_image, command=open_game4, borderwidth=0)
game5_icon = tk.Button(root, image=game5_image, command=open_game5, borderwidth=0)
game6_icon = tk.Button(root, image=game6_image, command=open_game6, borderwidth=0)

# Використовуємо place() для точного позиціонування кнопок
game1_icon.place(relx=0.35, rely=0.3, anchor="center", width=60, height=60)
game2_icon.place(relx=0.65, rely=0.3, anchor="center", width=60, height=60)
game3_icon.place(relx=0.35, rely=0.5, anchor="center", width=60, height=60)
game4_icon.place(relx=0.65, rely=0.5, anchor="center", width=60, height=60)
game5_icon.place(relx=0.35, rely=0.7, anchor="center", width=60, height=60)
game6_icon.place(relx=0.65, rely=0.7, anchor="center", width=60, height=60)

# Запуск вікна
root.mainloop()
