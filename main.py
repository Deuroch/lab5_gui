import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class FileDialogApp(tk.Tk):
    """Приложение для вызова диалога выбора файла (Ср. 8)."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Выбор файла")
        self.geometry("300x150")

        self.btn = tk.Button(self, text="Выбрать файл", command=self.choose_file)
        self.btn.pack(expand=True)

    def choose_file(self) -> None:
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Результат", f"Выбран файл:\n{file_path}")


class SimplePyQtApp(QWidget):
    """Простейшее окно на PyQt5 (Ср. 10)."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt5 Приложение")
        self.resize(300, 150)
        
        layout = QVBoxLayout()
        label = QLabel("Привет, PyQt5!", self)
        layout.addWidget(label)
        self.setLayout(layout)


class ListboxApp(tk.Tk):
    """Приложение со списком Listbox (Ср. 4)."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Список элементов")
        self.geometry("300x200")

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        items = ["Python", "Java", "C++", "JavaScript", "Go"]
        for item in items:
            self.listbox.insert(tk.END, item)
            
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def on_select(self, event: tk.Event) -> None:
        selection = self.listbox.curselection()
        if selection:
            item = self.listbox.get(selection[0])
            print(f"Выбран элемент: {item}")


class MultiWindowApp(tk.Tk):
    """Программа с вызовом дополнительных окон (Пов. 8)."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Главное окно")
        self.geometry("300x150")

        self.btn = tk.Button(self, text="Открыть новое окно", command=self.open_new_window)
        self.btn.pack(expand=True)

    def open_new_window(self) -> None:
        new_window = tk.Toplevel(self)
        new_window.title("Дополнительное окно")
        new_window.geometry("200x100")
        tk.Label(new_window, text="Это второе окно!").pack(expand=True)