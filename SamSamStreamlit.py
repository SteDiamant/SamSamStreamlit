import streamlit as st

import project.pages.Invoices as Invoices
import project.pages.PIN_Payments as PIN_Payments
import project.pages.EG as EG
import project.pages.External_payments as External_payments
import project.pages.Gift_Cards as Gift_Cards
import project.pages.REPR as REPR
import project.pages.Vault_cash as Vault_cash
import project.pages.Kassastrook as Kassastrook
import project.pages.Statistics as Statistics
from streamlit_option_menu import option_menu
from project.auth_ui.widgets import __login__
import warnings


#Ignore warnings from streamlit

st.set_page_config(layout='wide',)

def main():
   __login__obj = __login__(auth_token = "courier_auth_token", 
                     company_name = "SamSam",
                     width = 200, height = 250, 
                     logout_button_name = 'Logout', hide_menu_bool = False, 
                     hide_footer_bool = True,
                     ) 

   LOGGED_IN = __login__obj.build_login_ui()


   if LOGGED_IN == True:
      page=option_menu(None, ["Payment", "Invoice", "Gift Card", "External_P", "Vault Cash", "Kassa", "EG", "REPR","Statistics"],  
         menu_icon="cast", default_index=0, orientation="horizontal",
         styles={
            "container": { "background-color": "#fafafa"},
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#4BB0FF"},
            "nav-link-hover": {"background-color": "#eee"},

         }
      )
      if page == 'Payment':
         PIN_Payments.main()
      elif page == 'Invoice':
         Invoices.main()
      elif page == 'Gift Card':
         Gift_Cards.main()
      elif page == 'External_P':
         External_payments.main()
      elif page == 'Vault Cash':
         Vault_cash.main()
      elif page == 'Kassa':
         Kassastrook.main()
      elif page == 'EG':
         EG.main()
      elif page == 'REPR':
         REPR.main()
      else:
         Statistics.main()
      
if __name__ == "__main__":
    main()