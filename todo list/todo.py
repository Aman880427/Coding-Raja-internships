 from tkinter import *
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-do-list-App', 
                           font='Arial 25 bold', width=10, bd=5, bg='pink', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', 
                            font='Arial 18 bold', width=10, bd=5, bg='pink', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', 
                            font='Arial 18 bold', width=10, bd=5, bg='pink', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font="Arial 10 bold")
        self.text.place(x=20, y=120)

        self.load_tasks()

        self.button = Button(self.root, text="Add", font='Arial 20 bold italic', 
                             width=10, bg='pink', fg='white', command=self.add_task)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='Arial 20 bold italic', 
                              width=10, bg='pink', fg='white', command=self.delete_task)
        self.button2.place(x=30, y=280)

    def add_task(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('datatodo.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)
        else:
            messagebox.showwarning('Warning', 'Please enter a task.')

    def delete_task(self):
        try:
            index = self.main_text.curselection()[0]
            self.main_text.delete(index)
            with open('datatodo.txt', 'r') as f:
                lines = f.readlines()
            with open('datatodo.txt', 'w') as f:
                for i, line in enumerate(lines):
                    if i != index:
                        f.write(line)
        except IndexError:
            messagebox.showwarning('Warning', 'Please select a task to delete.')

    def load_tasks(self):
        try:
            with open('datatodo.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            pass

def main(): 
    root = Tk()
    ui = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


