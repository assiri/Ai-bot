# -*- coding: utf-8 -*-
import os
import openai
import gradio as gr


openai.api_key = os.getenv("iakey")

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply



inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply")

gr.Interface(
    fn=chatbot,
    inputs=inputs,
    outputs=outputs,
    title="ChatGPT : Test!",
    description="Ask anything you want",
).launch()
