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