import gradio as gr

def respond(message, chat_history):
    response = f"「{message}」とおっしゃいましたね。"
    chat_history.append((message, response))
    return chat_history, ""

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="メッセージを入力", placeholder="ここに入力...")
    send = gr.Button("送信")

    send.click(respond, inputs=[msg, chatbot], outputs=[chatbot, msg])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[chatbot, msg])

demo.launch()
