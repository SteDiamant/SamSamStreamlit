import streamlit as st

import project.pages.Invoices as Invoices
import project.pages.PIN_Payments as PIN_Payments
import project.pages.EG as EG
import project.pages.External_payments as External_payments
import project.pages.Gift_Cards as Gift_Cards
import project.pages.REPR as REPR
import project.pages.Vault_cash as Vault_cash
import project.pages.Kassastrook as Kassastrook

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
st.set_page_config(layout='wide')

def main():
   with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

   authenticator = stauth.Authenticate(
      config['credentials'],
      config['cookie']['name'],
      config['cookie']['key'],
      config['cookie']['expiry_days'],
      config['pre-authorized']
   )
   with st.sidebar:
      name, authentication_status, username = authenticator.login()
      if st.session_state["authentication_status"]:
         st.sidebar.write(f'Welcome *{st.session_state["name"]}*')
         authenticator.logout()
      elif st.session_state["authentication_status"] is False:
         st.error('Username/password is incorrect')
      elif st.session_state["authentication_status"] is None:
         st.warning('Please enter your username and password')
         
   if authentication_status == True:
      tabs = ["Payment", "Invoice", "Gift Card", "External Payment", "Vault Cash", "Kassa Strook", "EG", "REPR"]
      page=st.sidebar.selectbox(label='Navigation',options=tabs)
      if page == 'Payment':
         PIN_Payments.main()
      elif page == 'Invoice':
         Invoices.main()
      elif page == 'Gift Card':
         Gift_Cards.main()
      elif page == 'External Payments':
         External_payments.main()
      elif page == 'Vault Cash':
         Vault_cash.main()
      elif page == 'Kassa Strook':
         Kassastrook.main()
      elif page == 'EG':
         EG.main()
      elif page == 'REPR':
         REPR.main()
      
if __name__ == "__main__":
    main()