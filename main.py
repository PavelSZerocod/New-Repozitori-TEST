import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        list_box.insert(tk.END, task)
        entry.delete(0, "end")

def delete_task():
    selected_task = list_box.curselection()
    if selected_task:
        list_box.delete(selected_task)

def mark_task():
    selected_task = list_box.curselection()
    if selected_task:
        task = list_box.get(selected_task)
        list_box2.insert(tk.END, task)
        list_box.delete(selected_task)

root = tk.Tk()

root.title("Деловой Планинг")

root.configure(background="BlanchedAlmond")

label = tk.Label(root, text="ВВЕДИТЕ ЗАДАЧИ НА СЕГОДНЯ:", bg="BlanchedAlmond", font="bold_font")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="ДОБАВИТЬ ЗАДАЧУ", width=20, command=add_task, bg="lawn green")
button.pack(pady=5)

button = tk.Button(root, text="ВЫПОЛНЕННАЯ ЗАДАЧА", width=20, command=mark_task, bg="orange")
button.pack(pady=5)

button = tk.Button(root, text="УДАЛИТЬ ЗАДАЧУ", width=20, command=delete_task, bg="red")
button.pack(pady=5)

frame_grid = tk.Frame(root, background="BlanchedAlmond")
frame_grid.pack(side="top")

frame_pack = tk.Frame(root)
frame_pack.pack()

label1 = tk.Label(frame_grid, text="Текущие задачи", font="bolt_font", background="BlanchedAlmond")
label1.grid(row=0, column=0)

list_box = tk.Listbox(frame_grid, width=30, height=20, bg="lawn green")
list_box.grid(padx=4, pady=5, row=1, column=0)

label2 = tk.Label(frame_grid, text="Выполненные задачи", font="bolt_font", background="BlanchedAlmond")
label2.grid(row=0, column=1)

list_box2 = tk.Listbox(frame_grid, width=30, height=20, bg="orange")
list_box2.grid(padx=4, pady=5, row=1, column=1)

root.mainloop()