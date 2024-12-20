import streamlit as st 

st.title("**Algebra Lineal:** *Multiplicacion de matrices 2x2 vista como composición de transformaciones lineales*")
st.divider()
# título de la página
st.subheader("**Un enfoque visual :** ") 
# texto
st.markdown(""" 
En Algebra Lineal comunmente se enseñan a hacer las operaciones basicas vectoriales entre las cuales estan
suma y resta de vectores, multiplicacion por un escalar, multiplicacion de matrices, determinantes...etc. 

En la mayoria de ocaciones, como estudiantes, aprendemos a dominar en su totalidad el manejo de las cuentas, ya sea
para sumar vectores; sumamos termino a termino, hallar determinantes; usamos la regla de sarrus. Pero en esa misma 
cantidad de ocaciones no ponemos en evidencia el como se manifiestan estas operaciones en el apartado grafico.   
""") 

st.image("https://img.freepik.com/vector-gratis/elementos-estadisticos-diseno-tiza_1379-11.jpg?t=st=1732678407~exp=1732682007~hmac=d8324c4154993a0ffd28570288f7dd8e606580e6e39660ad9c114d4acfe694df&w=1060")



st.markdown ("""
Seria mas provechoso para el entendimiento a un nivel superior del Algebra Lineal que comprendieramos que implocaciones 
geometricas tienen este tipo operaciones en el espacio el cual estemos trabajando. Ya que un desarrollo mayor de la intucion geometrica 
facilitara que tipo de herramientas se usaran en los problemas que comunmente encontramos no solo en Algebra, sino en el resto de aplicaciones 
bien sea en fisica, ingenieria o informatica. 
""") 

st.markdown ("""
Mi obejtivo con la creacion de esta aplicacion, no solo es aplicar los conociemientos de progrmacion adquridos durante el semestre, sino explicar 
los operanciones vistas como elemetos graficos y definir por que la mutiplicacion de matrices esta establecidad de manera en el cual la conocemos. 

Espero explicar pero sobretodo aprender como se ve nuestro mundo de una manera mas lineal. :V
""") 

st.divider()  

st.markdown("""
> *No hay casi ninguna teoría más elemental que el :green[álgebra lineal], a pesar de que generaciones de profesores 
y escritores de libros de texto han :rainbow[oscurecido] su simplicidad medianta absurdos cálculos*
>
> **- Jean Dieudonné**
""")

#st.markdown("*Streamlit* is **really** ***cool***.")
#st.markdown('''
    #:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    #:gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')



st.divider()

import numpy as np
import matplotlib.pyplot as plt

v = np.array([3,5])
v2 = np.array([2,2])

fig, ax = plt.subplots()

ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='pink', label='Vector 1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector 2 ')

# Configurar el gráfico
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')
ax.set_title("Grafica de vectores en el plano")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.legend()
ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.5)

st.pyplot(fig)