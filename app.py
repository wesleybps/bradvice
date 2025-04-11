import streamlit as st

st.title("Calculadora de Soma")

valor1 = st.number_input("Digite o primeiro número", step=1.0)
valor2 = st.number_input("Digite o segundo número", step=1.0)

if st.button("Calcular"):
    resultado = valor1 + valor2
    st.success(f"Resultado da soma: {resultado}")