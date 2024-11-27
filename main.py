import streamlit as st 

# 1) crear las paginas 

uno = st.Page("paginas/uno.py", title = "Algebra Lineal", icon = ":material/star:")  
dos = st.Page("paginas/dos.py", title = "Dos") 

pg = st.navigation([uno, dos,])   
#pg = st.navigation({"prueba":[uno], "ecua":[dos]})

pg.run()



