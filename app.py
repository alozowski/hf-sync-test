import gradio as gr
from datetime import datetime

def greet(name):
    if not name:
        return "Please enter your name!"
    return f"Hello {name}! Welcome to the updated HF Sync Test Space! 🚀✨ (your name has {len(name)} characters)"

# Create a tabbed interface with multiple functions
with gr.Blocks(title="HF Sync Test - Updated!") as demo:
    gr.Markdown("# 🔄 Hugging Face Sync Test")
    gr.Markdown("🧪 PR #8 sync test: GitHub → Hugging Face Space")

    with gr.Tab("Greeting"):
        name_input = gr.Textbox(label="Enter your name", placeholder="Claude")
        greet_output = gr.Textbox(label="Greeting")
        greet_btn = gr.Button("Greet Me!")
        greet_btn.click(greet, inputs=name_input, outputs=greet_output)

    # Tab to confirm sync worked
    with gr.Tab("Sync Check"):
        gr.Markdown(f"✅ Synced at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")
        gr.Markdown("If you see this tab, the sync is working!")

    gr.Markdown("---")
    gr.Markdown("*This Space is auto-synced from GitHub using huggingface-sync-action*")

demo.launch()
