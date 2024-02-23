import winshell
import tkinter as tk
import customtkinter



class Recycle_Bin:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x150")
        self.window.resizable(0, 0)
        self.window.title("Empty Recycle Bin")
        self.window.configure(bg='#222831')
        self.empty()
        self.button()

    def button(self):
        button_ok = customtkinter.CTkButton(master=self.window, corner_radius=10, bg="#3A1078", text="ok", width = 110, command=self.close)
        button_ok.pack(padx=10, pady=10)
    
    def close (self):
        self.window.destroy()
        
    def empty (self):
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            label = customtkinter.CTkLabel(master=self.window, text_color="white", text="Recycle bin is emptied Now" , width = 300)
            label.pack(padx=20, pady=20)
        except:
            label = customtkinter.CTkLabel(master=self.window, text_color="white", text="Recycle bin already empty", width = 300)
            label.pack(padx=20, pady=20)
    
    def run(self):
        self.window.mainloop()
    
    
    
if __name__ == "__main__":
    Empty = Recycle_Bin()
    Empty.run()