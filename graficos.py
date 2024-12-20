# -*- coding: utf-8 -*-
"""GRAFICOS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PmxFIAk-bMTMkdtRkqfFENPgrF9RvmmO
"""

#import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# REFs:
# https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
# https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
# https://www.w3schools.com/python/matplotlib_pie_charts.asp

def Grafico_Pizza(Rotulos, Quantias, Legenda, posExplode, LocLEG, Larg = 16, Alt = 9, Titulo_Grafico = 'Título da Legenda', Titulo_legenda = 'Título da Legenda'):
    # Rotulos: etiquetamento dos dados
    # Quantias: dados numéricos referente a cada rótulo
    # Legenda: etiquetamento da legenda
    # posExplode: posição na qual se encontra a fatia da pizza que se deseja ressaltar (explodir)
    # LocLEG: Localização onde será posicionada a Legenda do Gráfico (Ref: https://www.geeksforgeeks.org/change-the-legend-position-in-matplotlib/)

    #fig, ax = plt.subplots(figsize =(16, 9))
    fig, ax = plt.subplots(figsize =(Larg, Alt))
    explode = []
    for i in range(len(Rotulos)):
        if i !=posExplode:
            explode.append(0)
        else:
            explode.append(0.1)
    ax.pie(Quantias,
        explode=explode,
        labels=Legenda,
        autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title(Titulo_Grafico)

    ax.legend(title=Titulo_legenda,
            loc=LocLEG,
            bbox_to_anchor=(1, 0, 0.5, 1))
    #fig
    st.pyplot(fig)

def Grafico_Barra_Horizontal(Rotulos, Quantias, Legenda, Largura = 16, Altura = 9, Titulo_Grafico = 'Título do Gráfico', Titulo_x = 'Titulo do Eixo x', Titulo_y = 'Titulo do Eixo y'):
    if len(Rotulos)==15:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime', 'teal', 'navy', 'gold']
    elif len(Rotulos)==14:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime', 'teal', 'navy']
    elif len(Rotulos)==13:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime', 'teal']
    elif len(Rotulos)==12:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime']
    elif len(Rotulos)==11:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink']
    elif len(Rotulos)==10:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown']
    elif len(Rotulos)==9:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey']
    elif len(Rotulos)==8:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
    elif len(Rotulos)==7:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta']
    elif len(Rotulos)==6:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']
    elif len(Rotulos)==5:
        colors = ['red', 'green', 'blue', 'orange', 'purple']
    elif len(Rotulos)==4:
        colors = ['red', 'green', 'blue', 'orange']
    elif len(Rotulos)==3:
        colors = ['red', 'green', 'blue']
    elif len(Rotulos)==2:
        colors = ['red', 'green']
    elif len(Rotulos)==1:
        colors = ['black']
    else:
        colors = 'blue'

    # Criar o gráfico de barras horizontal
    fig, ax = plt.subplots(figsize =(Largura, Altura))
    bars = ax.barh(Rotulos, Quantias, color=colors)

    # Adicionar rótulos e título aos eixos
    ax.set_ylabel(Titulo_y)
    ax.set_xlabel(Titulo_x)
    ax.set_title(Titulo_Grafico)

    # Adicionar legenda
    ax.legend(bars, Rotulos)

    # Adicionar os valores ao lado das barras
    for bar, value in zip(bars, Quantias):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

    # Exibir o gráfico no Streamlit
    #fig
    st.pyplot(fig)
