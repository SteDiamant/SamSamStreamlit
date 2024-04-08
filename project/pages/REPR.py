from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

class R_E_P_R:
    def add_repr_form():
        st.header("REPR Form")
        REPR_dranken_hoog = st.number_input("REPR Dranken Hoog")
        REPR_dranken_laag = st.number_input("REPR Dranken Laag")
        REPR_Koffie = st.number_input("REPR Koffie")
        REPR_Grote_kaart = st.number_input("REPR Grote Kaart")
        REPR_Kleine_kaart = st.number_input("REPR Kleine Kaart")
        REPR_Dagschotels = st.number_input("REPR Dagschotels")
        REPR_Nagerechten = st.number_input("REPR Nagerechten")
        REPR_Gebak = st.number_input("REPR Gebak")

        if st.button("Submit REPR"):
            repr = REPR(REPR_dranken_hoog=REPR_dranken_hoog, REPR_dranken_laag=REPR_dranken_laag, REPR_Koffie=REPR_Koffie, REPR_Grote_kaart=REPR_Grote_kaart, REPR_Kleine_kaart=REPR_Kleine_kaart, REPR_Dagschotels=REPR_Dagschotels, REPR_Nagerechten=REPR_Nagerechten, REPR_Gebak=REPR_Gebak)
            session.add(repr)
            session.commit()
            st.success("REPR added successfully!")

    def update_repr_form():
        def parse_response(response):
            if len(response) == 0:
                return "No REPR found"
            elif len(response) == 1:
                repr = response[0]
                data = [(repr.id, repr.REPR_dranken_hoog, repr.REPR_dranken_laag, repr.REPR_Koffie, repr.REPR_Grote_kaart, repr.REPR_Kleine_kaart, repr.REPR_Dagschotels, repr.REPR_Nagerechten, repr.REPR_Gebak, repr.date)]
                repr_df = pd.DataFrame(data=data, columns=['id', 'REPR_dranken_hoog', 'REPR_dranken_laag', 'REPR_Koffie', 'REPR_Grote_kaart', 'REPR_Kleine_kaart', 'REPR_Dagschotels', 'REPR_Nagerechten', 'REPR_Gebak', 'date'])
                return repr_df
            else:
                data = [(repr.id, repr.REPR_dranken_hoog, repr.REPR_dranken_laag, repr.REPR_Koffie, repr.REPR_Grote_kaart, repr.REPR_Kleine_kaart, repr.REPR_Dagschotels, repr.REPR_Nagerechten, repr.REPR_Gebak, repr.date) for repr in response]
                repr_df = pd.DataFrame(data=data, columns=['id', 'REPR_dranken_hoog', 'REPR_dranken_laag', 'REPR_Koffie', 'REPR_Grote_kaart', 'REPR_Kleine_kaart', 'REPR_Dagschotels', 'REPR_Nagerechten', 'REPR_Gebak', 'date'])
                return repr_df
            
        st.header("Update REPR Form")
        filter_date = st.date_input("Filter by Date")
        if st.button("Return REPR by date"):
            repr = session.query(REPR).filter(func.date(REPR.date) == filter_date).all()
            st.dataframe(parse_response(repr), use_container_width=True)
            st.success("REPR returned successfully!")

    def delete_repr_form():
        st.header("Delete REPR Form")
        id = st.number_input("ID that will be deleted", step=1, min_value=0)
        if st.button("Delete REPR", disabled=False):
            repr = session.query(REPR).filter(REPR.id == id).first()
            if repr:
                session.delete(repr)
                session.commit()
                st.success("REPR deleted successfully!")

def main():
    tab1,tab2=st.tabs(["Add REPR","Update REPR"])
    with tab1:
        R_E_P_R.add_repr_form()
    with tab2:
        c1,c2 = st.columns([1,1])
        with c1:
            R_E_P_R.update_repr_form()
        with c2:
            R_E_P_R.delete_repr_form()

if __name__=="__main__":
    main()