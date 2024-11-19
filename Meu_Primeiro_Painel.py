import streamlit as st
from ACTlib01 import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image # Lib para carregar imagem no Streamlit
   
def main():    
    Configurar_Pagina("ACT - Soluções para Pessoas/TESTE", "amplo", "auto", "https://docs.streamlit.io", "mailto:informacoes.actsp@gmail.com", "#### **ACT - Soluções para Pessoas**. Você pode usar formatação Markdown para adicionar informações neste espaço. Para mais informações acesse *https://www.markdownguide.org*", "©️")
    Imagem(caminho='1stDashboard.png', rotulo = ' ', dimensao=760, preencher="falso", clamp = "falso", padrao_cor="RGB", formato_saida = "auto")
    
    Escrever('''
                [Matplotlib Pie Charts](https://www.w3schools.com/python/matplotlib_pie_charts.asp)
            ''')
    
    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.metric("Temperature", "70 °F", "1.2 °F")
    with col2:
        with st.container(border=True):       
            st.metric("Wind", "9 mph", "-8%")
    with col3:
        with st.container(border=True):        
            st.metric("Humidity", "86%", "4%")
    
    with st.container(border=True):
        colunas1 = st.columns(2)
        with colunas1[0]:
            Grafico_Pizza(mylabels, y, mylabels, 0, "upper left", 16, 9)
        with colunas1[1]:
            Grafico_Barra_Horizontal(mylabels, y, mylabels, Largura = 16, Altura = 9, Titulo_Grafico = 'Título do Gráfico', Titulo_x = 'Titulo do Eixo x', Titulo_y = 'Titulo do Eixo y')



if __name__ == '__main__':
    main()