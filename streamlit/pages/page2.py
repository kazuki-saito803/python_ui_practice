import streamlit as st

st.title("💬 簡易チャットボット")

# セッション状態に会話履歴を保持
if "messages" not in st.session_state:
    st.session_state.messages = []

# これまでの会話を表示
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def bot_response(prompt):
    return f"『{prompt}』って言いましたね！！"

# ユーザー入力
if prompt := st.chat_input("メッセージを入力してください"):
    # 履歴に追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Botの応答（ここではダミー）
    response = bot_response(prompt)
    st.session_state["messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)