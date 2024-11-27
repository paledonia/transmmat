import streamlit as st 

st.title("PRIMERA PAGINA")

st.markdown ("""  


""") 

# Varios inputs
nombre = st.text_input("¿Cómo te llamas?", "")
if nombre:
    st.write(f"¡Hola, {nombre}! 🎈")


edad = st.slider("¿Cuál es tu edad?", 0, 100, 18)
st.write(f"Tienes {edad} años. ¡Fantástico!")


gusta_streamlit = st.checkbox("¿Te gusta Streamlit?")
if gusta_streamlit:
    st.write("¡A mí también me encanta! 😍")


st.write("Gracias por probar mi primera app. ¡Espero que te haya gustado!") 

st.slider("valor")