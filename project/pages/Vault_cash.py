
from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

class VAULT_CASH:
    def add_vault_cash_form():
        st.header("Vault Cash Form")
        amount100 = st.number_input("Amount 100")
        amount50 = st.number_input("Amount 50")
        amount20 = st.number_input("Amount 20")
        amount10 = st.number_input("Amount 10")
        amount5 = st.number_input("Amount 5")
        amount2 = st.number_input("Amount 2")
        amount1 = st.number_input("Amount 1")
        amount050 = st.number_input("Amount 0.50")
        amount020 = st.number_input("Amount 0.20")
        amount010 = st.number_input("Amount 0.10")
        amount005 = st.number_input("Amount 0.05")
            

        if st.button("Submit Vault Cash"):
            vault_cash = VaultCash(amount100=amount100, amount50=amount50, amount20=amount20, amount10=amount10, amount5=amount5, amount2=amount2, amount1=amount1, amount050=amount050, amount020=amount020, amount010=amount010, amount005=amount005)
            session.add(vault_cash)
            session.commit()
            st.success("Vault Cash added successfully!")

    def update_vault_cash_form():

        def parse_response(response):
            if len(response) == 0:
                return "No vault cash found"
            elif len(response) == 1:
                vault_cash = response[0]
                data = [(vault_cash.id, vault_cash.amount100, vault_cash.amount50, vault_cash.amount20, vault_cash.amount10, vault_cash.amount5, vault_cash.amount2, vault_cash.amount1, vault_cash.amount050, vault_cash.amount020, vault_cash.amount010, vault_cash.amount005, vault_cash.date, vault_cash.updated_date)]
                vault_cash_df = pd.DataFrame(data=data, columns=['id', 'amount100', 'amount50', 'amount20', 'amount10', 'amount5', 'amount2', 'amount1', 'amount050', 'amount020', 'amount010', 'amount005', 'date', 'updated_date'])
                return vault_cash_df
            else:
                data = [(vault_cash.id, vault_cash.amount100, vault_cash.amount50, vault_cash.amount20, vault_cash.amount10, vault_cash.amount5, vault_cash.amount2, vault_cash.amount1, vault_cash.amount050, vault_cash.amount020, vault_cash.amount010, vault_cash.amount005, vault_cash.date, vault_cash.updated_date) for vault_cash in response]
                vault_cash_df = pd.DataFrame(data=data, columns=['id', 'amount100', 'amount50', 'amount20', 'amount10', 'amount5', 'amount2', 'amount1', 'amount050', 'amount020', 'amount010', 'amount005', 'date', 'updated_date'])
                return vault_cash_df
            
        st.header("Update External Payment Form")
        filter_date = st.date_input("Filter by Date")
        if st.button("Return gift card by source"):
                gift_card = session.query(VaultCash).filter(func.date(VaultCash.date) == filter_date).all()
                st.dataframe(parse_response(gift_card), use_container_width=True)
                st.success("Gift card returned successfully!")

    def delete_vault_cash_form():
        st.header("Delete Vault Cash Form")
        id = st.number_input("ID that will be deleted", step=1, min_value=0)
        if st.button("Delete Vault Cash",disabled=False):
            vault_cash = session.query(VaultCash).filter(VaultCash.id == id).first()
            if vault_cash:
                session.delete(vault_cash)
                session.commit()
                st.success("Vault Cash deleted successfully!")

def main():
    tab1,tab2 = st.tabs(["Add Vault Cash","Update Vault Cash"])
    with tab1:
        VAULT_CASH.add_vault_cash_form()
    with tab2:
        c1,c2 = st.columns([1,1])
        with c1:
            VAULT_CASH.update_vault_cash_form()
        with c2:
            VAULT_CASH.delete_vault_cash_form()
        

if __name__ == "__main__":
    main()