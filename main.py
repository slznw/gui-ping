import os
import sys
from datetime import datetime
import tkinter as tk


platform = sys.platform
disallow = [";", ":", "&", "*", "$"]
# maybe i should improve disallow list xD
def check():
	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	site = entry.get()
	print(site)
	if any(symbol in site for symbol in disallow):
		status.config(text="Укажите существующий сайт!", fg="red")
		return
	if platform == "darwin":
		response = os.system("ping -c 1 " + site)
	else:
		response = os.system("ping -n 1 " + site)

	if response == 0:
		with open("ping.log", "a") as file:
			file.write(f"[{current_time}] {site} - OK\n")
		status.config(text="Все работает стабильно!", fg="green")
	else:
		with open("ping.log", "a") as file:
			file.write(f"[{current_time}] {site} - DOWN\n")
		status.config(text="Нет связи с сайтом", fg="red")
		if platform == "darwin":
			os.system("osascript -e 'display notification \"Сервер лежит, паника!\" with title \"Network Alert\" sound name \"Glass\"'")

root = tk.Tk()
root.title("Ping GUI")
root.geometry("300x200")
label = tk.Label(root, text="PING GUI")
label.pack()
status = tk.Label(root, text="Статус: ")
status.pack()
entry = tk.Entry(root,text="Введите сайт для проверки")
entry.pack()
but = tk.Button(root,text="Проверить!", command=check)
but.pack()
root.mainloop()






