import tkinter as tk

class Setting:
    def font_size():
        # font size implemetation
        pass

    def gui():
        setting_root = tk.Tk()
        setting_root.title("Settings")
        setting_root.geometry("600x500")
        setting_root.resizable(False, False)
        font_size_print = tk.Label(setting_root, text="Font:", bd=0)
        font_size_print.grid(row=0, column=0, padx=10, pady=10)

if __name__ == '__main__':
    print('that`s a library a program')
