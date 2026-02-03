import gradio as gr
from datetime import datetime

def greet(name):
    if not name:
        return "Please enter your name!"
    return f"Hello {name}! Welcome to the updated HF Sync Test Space! 🚀✨"

def reverse_text(text):
    return text[::-1] if text else ""

def shake_it(text):
    if not text:
        return "Give me something to shake!"
    return " ".join(reversed(text.split()))

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

    # Shake words around — reverses word order instead of characters
    with gr.Tab("Word Shaker"):
        shake_input = gr.Textbox(label="Enter a sentence", placeholder="The sync is working great")
        shake_output = gr.Textbox(label="Shaken words")
        shake_btn = gr.Button("Shake it!")
        shake_btn.click(shake_it, inputs=shake_input, outputs=shake_output)

    # Tab to confirm sync worked
    with gr.Tab("Sync Check"):
        gr.Markdown(f"✅ Synced at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")
        gr.Markdown("If you see this tab, the sync is working!")

    gr.Markdown("---")
    gr.Markdown("*This Space is auto-synced from GitHub using huggingface-sync-action*")

demo.launch()