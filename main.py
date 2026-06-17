import os
from datetime import datetime
import tkinter as tk



disallow = [";", ":", "&", "*", "$"]
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"  # Этот код сбрасывает цвет обратно на стандартный

# while True:
# 	hostname = str(input("Введите сайт для проверки, либо введите exit для выхода: "))
# 	if hostname == "exit":
# 		exit()
def check():
	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	site = entry.get()
	print(site)
	if any(symbol in site for symbol in disallow):
	 	status.config(text="Укажите существующий сайт!", fg="red")
	 	return
	response = os.system("ping -c 1 " + site)

	if response == 0:
		with open("ping.log", "a") as file:
			file.write(f"[{current_time}] {site} - OK\n")
		# print(GREEN + "Все работает стабильно!" + RESET)
		status.config(text="Все работает стабильно!", fg="green")
	else:
		with open("ping.log", "a") as file:
			file.write(f"[{current_time}] {site} - DOWN\n")
		# print(RED + "Нет связи с сайтом" + RESET)
		status.config(text="Нет связи с сайтом", fg="red")
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
mainloop()