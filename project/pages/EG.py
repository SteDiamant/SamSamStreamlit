from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

class E_G:
    def add_eg_form():
        st.header("EG Form")
        EG_dranken_hoog = st.number_input("EG Dranken Hoog")
        EG_dranken_laag = st.number_input("EG Dranken Laag")
        EG_Koffie = st.number_input("EG Koffie")
        EG_Grote_kaart = st.number_input("EG Grote Kaart")
        EG_Kleine_kaart = st.number_input("EG Kleine Kaart")
        EG_Dagschotels = st.number_input("EG Dagschotels")
        EG_Nagerechten = st.number_input("EG Nagerechten")
        EG_Gebak = st.number_input("EG Gebak")

        if st.button("Submit EG"):
            eg = EG(EG_dranken_hoog=EG_dranken_hoog, EG_dranken_laag=EG_dranken_laag, EG_Koffie=EG_Koffie, EG_Grote_kaart=EG_Grote_kaart, EG_Kleine_kaart=EG_Kleine_kaart, EG_Dagschotels=EG_Dagschotels, EG_Nagerechten=EG_Nagerechten, EG_Gebak=EG_Gebak)
            session.add(eg)
            session.commit()
            st.success("EG added successfully!")

    def update_eg_form():
        def parse_response(response):
            if len(response) == 0:
                return "No EG found"
            elif len(response) == 1:
                eg = response[0]
                data = [(eg.id, eg.EG_dranken_hoog, eg.EG_dranken_laag, eg.EG_Koffie, eg.EG_Grote_kaart, eg.EG_Kleine_kaart, eg.EG_Dagschotels, eg.EG_Nagerechten, eg.EG_Gebak, eg.date)]
                eg_df = pd.DataFrame(data=data, columns=['id', 'EG_dranken_hoog', 'EG_dranken_laag', 'EG_Koffie', 'EG_Grote_kaart', 'EG_Kleine_kaart', 'EG_Dagschotels', 'EG_Nagerechten', 'EG_Gebak', 'date'])
                return eg_df
            else:
                data = [(eg.id, eg.EG_dranken_hoog, eg.EG_dranken_laag, eg.EG_Koffie, eg.EG_Grote_kaart, eg.EG_Kleine_kaart, eg.EG_Dagschotels, eg.EG_Nagerechten, eg.EG_Gebak, eg.date) for eg in response]
                eg_df = pd.DataFrame(data=data, columns=['id', 'EG_dranken_hoog', 'EG_dranken_laag', 'EG_Koffie', 'EG_Grote_kaart', 'EG_Kleine_kaart', 'EG_Dagschotels', 'EG_Nagerechten', 'EG_Gebak', 'date'])
                return eg_df
        st.header("Update EG Form")
        filter_date = st.date_input("Filter by Date")
        if st.button("Return EG by date"):
            eg = session.query(EG).filter(func.date(EG.date) == filter_date).all()
            st.dataframe(parse_response(eg), use_container_width=True)
            st.success("EG returned successfully!")

def main():
    tab1,tab2=st.tabs(["Add EG","Update EG"])
    with tab1:
        E_G.add_eg_form()
    with tab2:
        E_G.update_eg_form()


if __name__=="__main__":
    main()