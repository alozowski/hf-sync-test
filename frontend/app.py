"""Frontend Gradio app for subdirectory sync test"""
import gradio as gr

def greet(name):
    return f"Hello {name} from the frontend subdirectory!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your name"),
    title="Frontend Subdirectory Test",
    description="This app is synced from the frontend/ subdirectory only"
)

if __name__ == "__main__":
    demo.launch()
