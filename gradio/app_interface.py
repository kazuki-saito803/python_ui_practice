import gradio as gr

## Symple
# def greet(name):
#     return f"こんにちは、{name}さん！"

# gr.Interface(fn=greet, inputs="text", outputs="text").launch()

## Chatbot
# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot()
#     msg = gr.Textbox()

#     def respond(message, chat_history):
#         bot_message = f"あなたは「{message}」と言いましたね。"
#         chat_history.append((message, bot_message))
#         return chat_history, ""

#     msg.submit(respond, [msg, chatbot], [chatbot, msg])

# demo.launch()

## slider dropdown checkbox
def customize(text, uppercase, repeat):
    if uppercase:
        text = text.upper()
    return text * repeat

gr.Interface(
    fn=customize,
    inputs=[
        gr.Textbox(label="テキスト"),
        gr.Checkbox(label="大文字にする"),
        gr.Slider(1, 5, step=1, label="繰り返し回数")
    ],
    outputs="text"
).launch()
