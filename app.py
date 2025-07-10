import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Carregar config dos usuários
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Autenticação
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.sidebar.success(f"Bem-vindo, {name}!")
    authenticator.logout("Sair", "sidebar")

    st.header("📊 Dashboards Power BI")

    # Exemplo de acesso por usuário
    if username == "cassio":
        st.markdown("[Dashboard de Operações](https://app.powerbi.com/view?r=LINK_DO_DASH_1)")
    elif username == "maria":
        st.markdown("[Dashboard Financeiro](https://app.powerbi.com/view?r=LINK_DO_DASH_2)")
    else:
        st.info("Nenhum dashboard disponível para seu usuário.")

elif authentication_status is False:
    st.error("Usuário ou senha incorretos")

elif authentication_status is None:
    st.warning("Por favor, insira suas credenciais.")
