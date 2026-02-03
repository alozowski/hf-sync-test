import gradio as gr

def greet(name):
    if not name:
        return "Please enter your name! 👋"
    return f"Hello {name}! Welcome to the updated HF Sync Test Space! 🚀✨"

def reverse_text(text):
    return text[::-1] if text else ""

# Create a tabbed interface with multiple functions
with gr.Blocks(title="HF Sync Test - Updated!") as demo:
    gr.Markdown("# 🔄 Hugging Face Sync Test")
    gr.Markdown("### Testing automatic sync from GitHub → HF Space")
    
    with gr.Tab("Greeting"):
        name_input = gr.Textbox(label="Enter your name", placeholder="Claude")
        greet_output = gr.Textbox(label="Greeting")
        greet_btn = gr.Button("Greet Me!")
        greet_btn.click(greet, inputs=name_input, outputs=greet_output)
    
    with gr.Tab("Text Reverser"):
        text_input = gr.Textbox(label="Enter text to reverse", placeholder="Hello World")
        reverse_output = gr.Textbox(label="Reversed text")
        reverse_btn = gr.Button("Reverse!")
        reverse_btn.click(reverse_text, inputs=text_input, outputs=reverse_output)
    
    gr.Markdown("---")
    gr.Markdown("*This Space is auto-synced from GitHub using huggingface-sync-action*")

demo.launch()