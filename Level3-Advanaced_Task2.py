# Import libraries
import string
import gradio as gr

## Encrypting function
def encrypt(plain_text, shift, operation="encrypt"):
    letters = string.ascii_uppercase
    plain_text = plain_text.upper()

    output = ""
    for item in plain_text:
        if item in letters:
            output += letters[(letters.index(item) + shift)%26] if operation == "encrypt" else letters[(letters.index(item) - shift)%26]
        else:
            output += item
    return output


# file handling with encrypting function
def file_encryption(link, shift, operation="encrypt"):
    try:
        with open(link, "r") as file:
            plain_text = file.read()

        filename = link.split(".")[0] + "_" + operation + "File.txt" 

        with open(filename, "w") as output:
            output.write(encrypt(plain_text, shift, operation))
            
        return f"Successful! Saved as {filename}"
    
    except FileNotFoundError:
        return f"No such file or directory: {link}"    


## Gradio interface
with gr.Blocks(title="Basic File Encryption/Decryption") as demo:
    gr.Markdown("##  Basic File Encryption/Decryption (Caesar cipher)")
    gr.Markdown("This program encrypt and decrpyt the content of a file and return the file using Caesar cipher.")

    with gr.Row():
        link = gr.Textbox(label = "File link")

    with gr.Row():
        shift = gr.Number(label="Enter shift")
        operation = gr.Dropdown(label="Operation", choices=["encrypt", "decrypt"])
    
    with gr.Row():
        btn = gr.Button("Run -->")

    with gr.Row():
        result_output = gr.Textbox(label="Result", interactive=False)

    
    btn.click(fn=file_encryption, inputs=[link, shift, operation], outputs=result_output)

demo.launch()           # To create a public link, set `share=True` in `launch()`.

# end of code