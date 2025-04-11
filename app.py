import streamlit as st

st.title("Cálculo Estimativo - São Paulo")

st.header("🔵 Mercado Endereçável")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Crédito")
    ativos_credito = st.number_input("Ativos classificados (Crédito)", value=245)
    valor_medio_credito = st.number_input("Valor médio (R$ Milhões)", value=20.0)
    fee_medio_credito = st.number_input("FEE médio (%)", value=3.0)

    fee_credito = ativos_credito * valor_medio_credito * (fee_medio_credito / 100)
    st.success(f"FEE Crédito: R$ {fee_credito:,.1f} Milhões")

with col2:
    st.subheader("M&A")
    ativos_ma = st.number_input("Ativos classificados (M&A)", value=245)
    valor_medio_ma = st.number_input("Valor médio EV (R$ Milhões)", value=50.0)
    fee_medio_ma = st.number_input("FEE médio (%)", value=4.0)

    fee_ma = ativos_ma * valor_medio_ma * (fee_medio_ma / 100)
    st.success(f"FEE M&A: R$ {fee_ma:,.1f} Milhões")

st.markdown("---")
st.header("📊 Market Share")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Crédito")
    sucesso_credito = st.number_input("% de Sucesso (Crédito)", value=20.0)
    ativos_ms_credito = ativos_credito * (sucesso_credito / 100)
    fee_ms_credito = ativos_ms_credito * valor_medio_credito * (fee_medio_credito / 100)
    st.success(f"FEE Market Share Crédito: R$ {fee_ms_credito:,.1f} Milhões")

with col4:
    st.subheader("M&A")
    sucesso_ma = st.number_input("% de Sucesso (M&A)", value=10.0)
    ativos_ms_ma = ativos_ma * (sucesso_ma / 100)
    fee_ms_ma = ativos_ms_ma * valor_medio_ma * (fee_medio_ma / 100)
    st.success(f"FEE Market Share M&A: R$ {fee_ms_ma:,.1f} Milhões")
