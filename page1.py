import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuizWizX - Automated Quiz System")

        # Add your GUI elements and logic here
        # For simplicity, let's create a basic login window
        self.username_label = tk.Label(root, text="Username:")
        self.username_entry = tk.Entry(root)
        self.password_label = tk.Label(root, text="Password:")
        self.password_entry = tk.Entry(root, show="*")
        self.login_button = tk.Button(root, text="Login", command=self.login)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

    def login(self):
        # Implement your login logic here
        # For simplicity, let's just show a message box
        messagebox.showinfo("Login", "Login successful!")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
