## Import library

import gradio as gr


## Class Calculator
class Calculator:
    def addition(self, num1, num2):
        return num1 + num2
        
    def subtraction(self, num1, num2):
        return num1 - num2
    
    def multiplication(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: You cannot divide by zero!"


##  Create an instance for a basic calculator
my_cal = Calculator()

def basic_calculator(num1, num2, operator):
    if (operator == "Add") or (operator == 'add'):
        return my_cal.addition(num1, num2)
    elif (operator == "Subtract") or (operator == 'subtract') :
        return my_cal.subtraction(num1, num2)
    elif (operator == "Multiply") or (operator == 'multiply'):
        return my_cal.multiplication(num1, num2)
    elif (operator == "Divide") or (operator == 'divide'):
        return my_cal.division(num1, num2)
    else:
        return ''


##  Create an instance for the gradio interface
calc = Calculator()


# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("##  Basic Calculator")
    gr.Markdown("Add, Subtract, Multiply or Divide two number")
    
    with gr.Row():
        num1 = gr.Number(label="Enter first number")
        num2 = gr.Number(label="Enter second number")
    
    with gr.Row():
        add = gr.Button("Add")
        subtract = gr.Button("Subtract")
        multiply = gr.Button("Multiply")
        divide = gr.Button("Divide")

    with gr.Row():
        result_output = gr.Textbox(label="Result", interactive=False)
        
    add.click(fn=calc.addition, inputs=[num1, num2], outputs = result_output)
    subtract.click(fn=calc.subtraction, inputs=[num1, num2], outputs = result_output)
    multiply.click(fn=calc.multiplication, inputs=[num1, num2], outputs = result_output)
    divide.click(fn=calc.division, inputs=[num1, num2], outputs = result_output)

# gradio launch
if __name__ == "__main__":
    demo.launch()       # To create a public link, set `share=True` in `launch()`.
