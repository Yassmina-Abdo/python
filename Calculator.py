import tkinter as tk


class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Calcuator")

        self.buttons = {}
        ################################ Button equal ################################################################
        self.calculator_output = tk.Label(
            width=25, relief=tk.FLAT, bd=1, justify=tk.RIGHT, font="Helvetica 16")
        self.calculator_output.grid(columnspan=5, row=0)

        self.buttons['button_equals'] = tk.Button(
            self, text='=', font="Helvetica 16")
        self.buttons['button_equals'].config(height=6)
        self.buttons['button_equals'].config(
            command=lambda button='=': self.button_action(button))
        self.buttons['button_equals'].grid(column=4, row=1, rowspan=4)
        ################################ Button equal ################################################################

        ################################ List Of Buttons #############################################################

        self.controls = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '. ', '+'],
        ]

        for i in range(0, len(self.controls)):
            for j in range(0, len(self.controls[i])):
                button_label = self.controls[i][j]
                self.buttons['button_' + str(i) + '_' + str(j)] = tk.Button(
                    self, text=button_label, font="Helvetica 16")
                self.buttons['button_' + str(i) + '_' + str(j)].config(
                    command=lambda button=button_label: self.button_action(button))
                self.buttons['button_' +
                             str(i) + '_' + str(j)].grid(column=j, row=i+1)

        ################################ List Of Buttons #############################################################

    def button_action(self, button_pressed):

        if button_pressed == '=':
            current_value = self.calculator_output.cget('text')
            try:
                result = eval(current_value)
                if result != '':
                    file = open("Calc_Result.txt", "w")
                    file.write(result)
                    file.close()
                    self.calculator_output.config(text=result)
            except:
                self.calculator_output.config(text=current_value)
        elif button_pressed == 'C':
            self.calculator_output.config(text='')
        else:
            current_value = self.calculator_output.cget('text')
            self.calculator_output.config(
                text=str(current_value) + button_pressed)


# -----------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
