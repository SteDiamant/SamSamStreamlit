import streamlit as st
from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
import project.pages.Invoices as Invoices
import project.pages.PIN_Payments as PIN_Payments
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


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
      page=st.selectbox(label='Navigation',options=['Payments','Invocies'])
      if page == 'Invoices':
         Invoices.main()
      else:
         PIN_Payments.main()
if __name__ == "__main__":
    main()