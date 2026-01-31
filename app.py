import streamlit as st
import google.generativeai as genai

# 設定大腦
genai.configure(api_key="AIzaSyBToWKFfSFom196Y9hl9xTnG29sl0u4N0E")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🐱 減肥小貓助手")

# 簡單的輸入框
weight = st.number_input("今日體重 (kg)", value=60.0)
msg = st.chat_input("跟小貓聊天...")

if msg:
    st.chat_message("user").write(msg)
    # 這裡就是妳之前在 AI Studio 寫的 System Prompt
    prompt = f"妳是一隻減肥貓。使用者目前{weight}kg。{msg}"
    response = model.generate_content(prompt)
    st.chat_message("assistant").write(response.text)
