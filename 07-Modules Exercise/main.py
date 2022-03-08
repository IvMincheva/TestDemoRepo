# import json
import tkinter as tk

from screens import render_main_screen

if __name__ == '__main__':
    # obj = {
    #     "username": "aatanasov",
    #     "password": "123123",
    #     "firstName": "Atanas",
    #     "lastName": "Atanasov",
    # }
    # print(json.dumps(obj))
    window = tk.Tk()
    window.geometry("600x600")
    window.title("My cool GUI shop")
    render_main_screen(window)
    window.mainloop()

