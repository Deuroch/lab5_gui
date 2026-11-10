import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class FileDialogApp(tk.Frame):
    """Приложение для вызова диалога выбора файла (Ср. 8)."""

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master.title("Выбор файла")
        self.master.geometry("300x150")
        self.pack(expand=True, fill=tk.BOTH)

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


class ListboxApp(tk.Frame):
    """Приложение со списком Listbox (Ср. 4)."""

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master.title("Список элементов")
        self.master.geometry("300x250")
        self.pack(expand=True, fill=tk.BOTH)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        items = ["Python", "Java", "C++", "JavaScript", "Go"]
        for item in items:
            self.listbox.insert(tk.END, item)

        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.result_label = tk.Label(self, text="Ничего не выбрано")
        self.result_label.pack(pady=5)

    def on_select(self, event: tk.Event) -> None:
        selection = self.listbox.curselection()
        if selection:
            item = self.listbox.get(selection[0])
            self.result_label.config(text=f"Выбран элемент: {item}")


class MultiWindowApp(tk.Frame):
    """Программа с вызовом дополнительных окон (Пов. 8)."""

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master.title("Главное окно")
        self.master.geometry("300x150")
        self.pack(expand=True, fill=tk.BOTH)

        self.btn = tk.Button(self, text="Открыть новое окно", command=self.open_new)
        self.btn.pack(expand=True)

    def open_new(self) -> None:
        new_window = tk.Toplevel(self.master)
        new_window.title("Дополнительное окно")
        new_window.geometry("200x100")
        tk.Label(new_window, text="Это второе окно!").pack(expand=True)


class NotesApp(tk.Frame):
    """Программа 'Заметки' с сохранением в файл (Пов. 1)."""

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master.title("Заметки")
        self.master.geometry("400x300")
        self.pack(expand=True, fill=tk.BOTH)

        self.text_area = tk.Text(self, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.save_btn = tk.Button(self, text="Сохранить в файл", command=self.save)
        self.save_btn.pack(pady=5)

    def save(self) -> None:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    text_content = self.text_area.get("1.0", tk.END).rstrip("\n")
                    file.write(text_content)
                messagebox.showinfo("Успех", "Заметка сохранена!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Укажите номер задания (1-5) в качестве аргумента:")
        print("python main.py 1 - Диалог выбора файла")
        print("python main.py 2 - Простейший GUI PyQt5")
        print("python main.py 3 - Список Listbox")
        print("python main.py 4 - Несколько окон")
        print("python main.py 5 - Заметки")
        sys.exit(0)

    task_num = sys.argv[1]

    if task_num == "2":
        app = QApplication(sys.argv)
        window = SimplePyQtApp()
        window.show()
        sys.exit(app.exec_())
    else:
        root = tk.Tk()
        if task_num == "1":
            app = FileDialogApp(root)
        elif task_num == "3":
            app = ListboxApp(root)
        elif task_num == "4":
            app = MultiWindowApp(root)
        elif task_num == "5":
            app = NotesApp(root)
        else:
            print("Неизвестный номер задания.")
            sys.exit(1)
        root.mainloop()