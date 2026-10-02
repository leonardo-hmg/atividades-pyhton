import streamlit as st

# ----------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ----------------------------------------

st.set_page_config(
    page_title="Expresso Mobilidade",
    page_icon="🚌",
    layout="wide"
)

# ----------------------------------------
# CABEÇALHO
# ----------------------------------------

st.title("🚌 Expresso Mobilidade")
st.header("Painel do Operador de Transporte")

st.markdown(
    """
    Bem-vindo ao painel operacional da **Expresso Mobilidade**.
    
    Utilize as opções abaixo para consultar linhas, selecionar
    múltiplas rotas e simular o cálculo de demanda e distribuição
    de frota.
    """
)

# ----------------------------------------
# IDENTIFICAÇÃO DO OPERADOR
# ----------------------------------------

st.subheader("👤 Identificação do Operador")

nome = st.text_input("Digite seu nome:")

if nome:
    st.write(f"Olá, **{nome}**! Seja bem-vindo ao painel operacional. 👋")
else:
    st.write("Digite seu nome para começar.")

# ----------------------------------------
# CONSULTA DE ROTA
# ----------------------------------------

st.subheader("🚌 Consulta de Rota")

linha = st.selectbox(
    "Escolha uma linha para consultar:",
    ["510", "520", "550", "620"]
)

st.write(f"**Linha selecionada:** {linha}")

# Informações fictícias das linhas
horarios = {
    "510": "05:30, 07:00, 08:30, 10:00, 12:00, 14:00, 16:30, 18:00",
    "520": "06:00, 07:30, 09:00, 11:00, 13:00, 15:00, 17:30, 19:00",
    "550": "05:45, 07:15, 08:45, 10:30, 12:30, 14:30, 17:00, 19:30",
    "620": "06:15, 08:00, 09:30, 11:30, 13:30, 15:30, 18:00, 20:00"
}

st.info(f"🕐 Horários previstos da linha {linha}: {horarios[linha]}")

# ----------------------------------------
# SELEÇÃO DE MÚLTIPLAS LINHAS
# ----------------------------------------

st.subheader("📊 Relatório Consolidado")

linhas = st.multiselect(
    "Escolha as linhas para o relatório:",
    ["510", "520", "550", "620"]
)

if linhas:
    st.write("**Linhas selecionadas:**")
    st.write(linhas)

    st.success(
        f"{len(linhas)} linha(s) selecionada(s) para geração do relatório."
    )
else:
    st.warning("Selecione pelo menos uma linha para gerar o relatório.")

# ----------------------------------------
# CÁLCULO DE DEMANDA E FROTA
# ----------------------------------------

st.subheader("🚍 Cálculo de Demanda e Frota")

if st.button("Calcular demanda e distribuição da frota"):
    
    if linhas:
        st.write("⏳ Calculando...")
        
        st.success("✅ Cálculo realizado com sucesso!")

        st.write("### Resultado da simulação")

        for rota in linhas:
            st.write(
                f"🚌 **Linha {rota}** → "
                f"demanda estimada: **{len(rota) * 150} passageiros** "
                f"| frota recomendada: **{len(rota)} ônibus**"
            )
    else:
        st.error(
            "⚠️ Selecione pelo menos uma linha antes de realizar o cálculo."
        )

# ----------------------------------------
# RODAPÉ
# ----------------------------------------

st.markdown("---")

st.markdown(
    "🚌 **Expresso Mobilidade** | Painel Operacional "
    "| Protótipo desenvolvido com Streamlit"
)
