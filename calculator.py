import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("180x150")
        self.root.title("calculator")
        self.expression = ""
        self.buttons = ['/', '*', '-', '+', '7', '8', '9', '0', '4', '5', '6', 
                        '.', '1', '2', '3', '=']
        self.colors = ["#B2FF66", "#8CD867", "#4CAF50", "#388E3C", "#2E7D32"]
        self.root.configure(background=self.colors[0])
        self.top_expression()
        self.create_buttons()
    
    def top_expression(self):
        self.top_label = tk.Label(self.root, text=self.expression, 
                                  font=('Arial', 20), background= self.colors[0])
        self.top_label.grid(row=0, column=0, columnspan= 4)
    
    def add_value(self, value):
        self.expression += value
        self.top_label.config(text=self.expression)
    
    def evaluate_expression(self):
        if self.expression == "":
            self.top_label.config(text="")
        try:
            answer = eval(self.expression)
            self.expression = ""
            self.top_label.config(text=str(answer))
        except:
            self.expression = ""
            self.top_label.config(text="error")
    
    def get_color(self, idx):
        return self.colors[idx]
    
    def create_buttons(self):
        idx = 0
        for i in range(1, 5):
            for j in range(4):
                if idx != 15:
                    btn = tk.Button(self.root, text=self.buttons[idx], 
                                    command=lambda idx=idx: self.add_value(self.buttons[idx]), 
                                    font=('Arial', 15), bg= self.get_color(i))
                    btn.grid(row=i, column=j)
                    idx += 1
                else:
                    btn = tk.Button(self.root, text=self.buttons[idx], 
                                    command=lambda: self.evaluate_expression(), 
                                    font=('Arial', 15), bg= self.get_color(i))
                    btn.grid(row=i, column=j)


if __name__ == "__main__":
    calculator = GUI()
    calculator.root.mainloop()
