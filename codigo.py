import streamlit as st 
from openai import OpenAI

modelo_ia = OpenAI
api_key = "SUA_CHAVE_API_AQUI"
# Titulo
# Input do chat (Campo de mensagem)
# A cada mensagem enviada:  
    # Exibir a mensagem no chat (Área de mensagens)
    # Pegar a pergunta e mandar para uma IA responder
    # Resposta da IA na tela (Área de mensagens):

st.write("### Chat com IA") # Markdown

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem:") 

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content =  mensagem["content"]
    st.chat_message(role).write(content)

if(texto_usuario):
    st.chat_message("user").write(texto_usuario) 
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)


    #IA respondendo
    resposta_ia = modelo_ia.chat.completions.create(
        messages = st.session_state["lista_mensagens"],
        model ="gpt-4o"
    )
    texto_resposta_ia = resposta_ia.choices[0].message.content
    
   
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


    
