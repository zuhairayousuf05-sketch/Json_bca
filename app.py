
import gradio as gr
from json_processor import process_json

title = "JSON Refiner Advanced Edition"

description = "Clean and refine JSON automatically. Features: Key standardization, Flatten/Unflatten JSON, Validation"

interface = gr.Interface(
    fn=process_json,
    inputs=gr.Textbox(lines=20, placeholder="Paste your JSON here"),
    outputs=gr.Textbox(lines=20),
    title=title,
    description=description
)

interface.launch()
