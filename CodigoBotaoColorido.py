def Botao_Colorido(rotulo, cor = "#7e7b7b"):
    Botao_Colorido.cor = cor
    st.markdown("""<style>  .element-container:has(style){display: none;} #button-after {display: none;}
                            .element-container:has(#button-after) {display: none;}
                            .element-container:has(#button-after) + div button {background-color: %s;font-weight: bolder; color:black;}
                </style>"""%(Botao_Colorido.cor), unsafe_allow_html=True)
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
    respBTNColor = st.button(rotulo)
    return respBTNColor
