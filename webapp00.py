# MEU PRIMEIRO WEB APP
import streamlit as st

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("murilo brazuna sato")

a = float(st.text_input("Digite valor a: "))
s = float(st.text_input("Digite valor s: "))
media = (a+s)/2
if media>5:
  st.write("Aprovado")
  st.write(media)
else:
  st.write("Rec")
  st.write(media)

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Cabeçalho")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub Cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

