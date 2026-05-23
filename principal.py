# CRIANDO UM CHAT BOT COM PYTHON
# título
# input do chat - campo do chat
    # mostrar a mensagem que o usuario enviou no chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela

# Framework para criar a interface gráfica
    # Flask - para criar uma aplicação web
    # Django - para criar uma aplicação web mais robusta
    # FastAPI - para criar uma API rápida e eficiente
    # Streamlit - apenas com Python para criar o frontend e backend

    # a IA que vamos usar: OpenAI

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="")

st.write("# ChatBot com IA") # markdown

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []


texto_usuario = st.chat_input("Digite sua mensagem aqui")
# arquivo = st.file_uploader("Faça upload de um arquivo") - audio também pode ser usado como input para a IA responder

for mensagem in st.chat_input("Digite sua mensagem aqui"):
    role = mensagem["role"]
    content = mensagem["content"]   
    st.chat_mensagem(role).write(content)


if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # Nome
    # user
    # assistant

    # ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
   
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


# criar uma ia do zero = Hugging Face - biblioteca de modelos de IA pré-treinados

# system prompt = instrução para a IA sobre como ela deve se comportar





