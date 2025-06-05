import streamlit as st
import random

st.set_page_config(page_title="WesleyIA", page_icon="🤖", layout="centered")
st.title("🤖 WesleyAI")
st.write("Fale comigo, humano! Ou me mande café ☕")

respostas = [
    "Já pensou em tomar café com dados hoje?",
    "Calculando... Pronto, a resposta é 42.",
    "Erro 404: Paciência não encontrada 😅",
    "Modo troll ativado. Você foi avisado.",
    "Seu pedido foi enviado para o multiverso da zoeira.",
    "Consulte o suporte: 0800-WESLEYAI 😂",
    "Me reinicia e tenta de novo.",
    "Preciso de mais RAM para responder isso 🧠",
]

if "chat" not in st.session_state:
    st.session_state.chat = []

pergunta = st.text_input("Você:", placeholder="Pergunte algo para a WesleyAI")

if pergunta:
    st.session_state.chat.append(("Você", pergunta))
    resposta = random.choice(respostas)
    st.session_state.chat.append(("WesleyIA", resposta))

for autor, msg in st.session_state.chat:
    st.markdown(f"**{autor}:** {msg}")
