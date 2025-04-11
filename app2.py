import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Cálculo Estimativo", layout="wide")
st.title("📊 Cálculo Estimativo - São Paulo")

tabs = st.tabs(["🔵 Mercado Endereçável", "📈 Market Share", "⬇️ Exportar"])

with tabs[0]:
    st.header("🔵 Mercado Endereçável")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Crédito")
        ativos_credito = st.number_input("Ativos classificados", value=245, key="ac1")
        valor_medio_credito = st.number_input("Valor médio (R$ Milhões)", value=20.0, key="vmc")
        fee_medio_credito = st.number_input("FEE médio (%)", value=3.0, key="fmc")

        fee_credito = ativos_credito * valor_medio_credito * (fee_medio_credito / 100)
        st.markdown(
            f"💰 <b>FEE Crédito:</b> <b>R$ {fee_credito:,.1f} Milhões</b>",
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("M&A")
        ativos_ma = st.number_input("Ativos classificados", value=245, key="am1")
        valor_medio_ma = st.number_input("Valor médio EV (R$ Milhões)", value=50.0, key="vmm")
        fee_medio_ma = st.number_input("FEE médio (%)", value=4.0, key="fmm")

        fee_ma = ativos_ma * valor_medio_ma * (fee_medio_ma / 100)
        st.markdown(
            f"💰 <b>FEE M&A:</b> <b>R$ {fee_ma:,.1f} Milhões</b>",
            unsafe_allow_html=True
        )

with tabs[1]:
    st.header("📈 Market Share")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Crédito")
        sucesso_credito = st.number_input("% de Sucesso", value=20.0, key="psc")
        ativos_ms_credito = ativos_credito * (sucesso_credito / 100)
        fee_ms_credito = ativos_ms_credito * valor_medio_credito * (fee_medio_credito / 100)
        st.markdown(
            f"💼 <b>FEE Market Share Crédito:</b> <b>R$ {fee_ms_credito:,.1f} Milhões</b>",
            unsafe_allow_html=True
        )

    with col4:
        st.subheader("M&A")
        sucesso_ma = st.number_input("% de Sucesso", value=10.0, key="psm")
        ativos_ms_ma = ativos_ma * (sucesso_ma / 100)
        fee_ms_ma = ativos_ms_ma * valor_medio_ma * (fee_medio_ma / 100)
        st.markdown(
            f"💼 <b>FEE Market Share M&A:</b> <b>R$ {fee_ms_ma:,.1f} Milhões</b>",
            unsafe_allow_html=True
        )

with tabs[2]:
    st.header("⬇️ Exportar para Excel")

    df_export = pd.DataFrame({
        "Categoria": ["Crédito", "M&A", "Market Share Crédito", "Market Share M&A"],
        "FEE (Milhões R$)": [fee_credito, fee_ma, fee_ms_credito, fee_ms_ma]
    })

    def to_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="FEE")
        return output.getvalue()

    excel_data = to_excel(df_export)

    st.download_button(
        label="📥 Baixar FEE em Excel",
        data=excel_data,
        file_name="calculo_estimativo.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
