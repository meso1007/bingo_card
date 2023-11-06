import tkinter as tk
import random

def bingocard():
    Bline = random.sample(range(1, 16), 5)   # 乱数(1-15)
    Iline = random.sample(range(16, 31), 5)  # 乱数(16-30)
    Nline = random.sample(range(31, 46), 5)  # 乱数(31-45)
    Gline = random.sample(range(46, 61), 5)  # 乱数(46-60)
    Oline = random.sample(range(61, 76), 5)  # 乱数（61-75)

    for i in range(5):
        for j in range(5):
            if j == 0:
                cell_value = Bline[i]
            elif j == 1:
                cell_value = Iline[i]
            elif j == 2:
                cell_value = Nline[i]
            elif j == 3:
                cell_value = Gline[i]
            elif j == 4:
                cell_value = Oline[i]
            if i == j == 2:  # 真ん中の場合
                cell = tk.Label(frame, text="Free")
            else:
                cell = tk.Label(frame, text=f"{cell_value}")
            cell.grid(row=i, column=j, padx=10, pady=10)

root = tk.Tk()
root.title("新規カード")

frame = tk.Frame(root)
frame.pack(pady=20)

generate_button = tk.Button(root, text="新規カード", command=bingocard)
generate_button.pack()

root.mainloop()

