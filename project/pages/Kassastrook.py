
from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

class KASSA_STROOK:
    def add_kassa_strook_form():
        st.header("Kassa Strook Form")
        Hoofdgerechten_8000 = st.number_input("Hoofdgerechten 8000")
        Nagerechten_8030 = st.number_input("Nagerechten 8030")
        Gebak_8040 = st.number_input("Gebak 8040")
        Kleine_kaart_8010 = st.number_input("Kleine kaart 8010")
        Dagschotels_8020 = st.number_input("Dagschotels 8020")
        Dranken_hoog_8100 = st.number_input("Dranken hoog 8100")
        Frisdranken_overig_8200 = st.number_input("Frisdranken overig 8200")
        Koffie_8300 = st.number_input("Koffie 8300")
        Cultuurkaarten_4760 = st.number_input("Cultuurkaarten 4760")
        Dagschotelabonnementer_2200 = st.number_input("Dagschotelabonnementer 2200")
        Omzet_kadobonnen_2220 = st.number_input("Omzet kadobonnen 2220")
        Catering_8050 = st.number_input("Catering 8050")
        Zaalhuur_8400 = st.number_input("Zaalhuur 8400")

        if st.button("Submit Kassa Strook"):
            kassastrook=KassaStrook(Hoofdgerechten_8000=Hoofdgerechten_8000, Nagerechten_8030=Nagerechten_8030, Gebak_8040=Gebak_8040, Kleine_kaart_8010=Kleine_kaart_8010, Dagschotels_8020=Dagschotels_8020, Dranken_hoog_8100=Dranken_hoog_8100, Frisdranken_overig_8200=Frisdranken_overig_8200, Koffie_8300=Koffie_8300, Cultuurkaarten_4760=Cultuurkaarten_4760, Dagschotelabonnementer_2200=Dagschotelabonnementer_2200, Omzet_kadobonnen_2220=Omzet_kadobonnen_2220, Catering_8050=Catering_8050, Zaalhuur_8400=Zaalhuur_8400)
            session.add(kassastrook)
            session.commit()
            st.success("Kassa Strook added successfully!")
        
    def update_kassa_strook_form():
        def parse_response(response):
            if len(response) == 0:
                return "No kassa strook found"
            elif len(response) == 1:
                kassastrook=response[0]
                data = [(kassastrook.id, kassastrook.Hoofdgerechten_8000, kassastrook.Nagerechten_8030, kassastrook.Gebak_8040, kassastrook.Kleine_kaart_8010, kassastrook.Dagschotels_8020, kassastrook.Dranken_hoog_8100, kassastrook.Frisdranken_overig_8200, kassastrook.Koffie_8300, kassastrook.Cultuurkaarten_4760, kassastrook.Dagschotelabonnementer_2200, kassastrook.Omzet_kadobonnen_2220, kassastrook.Catering_8050, kassastrook.Zaalhuur_8400, kassastrook.date, kassastrook.updated_date)]
                kassastrook_df=pd.DataFrame(data=data,columns=['id','Hoofdgerechten_8000','Nagerechten_8030','Gebak_8040','Kleine_kaart_8010','Dagschotels_8020','Dranken_hoog_8100','Frisdranken_overig_8200','Koffie_8300','Cultuurkaarten_4760','Dagschotelabonnementer_2200','Omzet_kadobonnen_2220','Catering_8050','Zaalhuur_8400','date','updated_date'])
                return kassastrook_df
            else:
                data = [(kassastrook.id, kassastrook.Hoofdgerechten_8000, kassastrook.Nagerechten_8030, kassastrook.Gebak_8040, kassastrook.Kleine_kaart_8010, kassastrook.Dagschotels_8020, kassastrook.Dranken_hoog_8100, kassastrook.Frisdranken_overig_8200, kassastrook.Koffie_8300, kassastrook.Cultuurkaarten_4760, kassastrook.Dagschotelabonnementer_2200, kassastrook.Omzet_kadobonnen_2220, kassastrook.Catering_8050, kassastrook.Zaalhuur_8400, kassastrook.date, kassastrook.updated_date) for kassastrook in response]
                kassastrook_df=pd.DataFrame(data=data,columns=['id','Hoofdgerechten_8000','Nagerechten_8030','Gebak_8040','Kleine_kaart_8010','Dagschotels_8020','Dranken_hoog_8100','Frisdranken_overig_8200','Koffie_8300','Cultuurkaarten_4760','Dagschotelabonnementer_2200','Omzet_kadobonnen_2220','Catering_8050','Zaalhuur_8400','date','updated_date'])
                return kassastrook_df
        st.header("Update Kassa Strook Form")
        filter_date = st.date_input("Filter by Date")
        if st.button("Return kassa strook by date"):
            kassastrook = session.query(KassaStrook).filter(func.date(KassaStrook.date) == filter_date).all()
            st.dataframe(parse_response(kassastrook),use_container_width=True) 
            st.success("Kassa Strook returned successfully!")

    def delete_kassa_strook_form():
        st.header("Delete Kassa Strook Form")
        id = st.number_input("ID that will be deleted", step=1, min_value=0)
        if st.button("Delete Kassa Strook",disabled=False):
            kassastrook = session.query(KassaStrook).filter(KassaStrook.id == id).first()
            if kassastrook:
                session.delete(kassastrook)
                session.commit()
                st.success("Kassa Strook deleted successfully!")
def main():
    tab1,tab2=st.tabs(["Add Kassa Strook","Update Kassa Strook"])
    with tab1:
        KASSA_STROOK.add_kassa_strook_form()
    with tab2:
        c1,c2=st.columns([1,1])
        with c1:
            KASSA_STROOK.update_kassa_strook_form()
        with c2:
            KASSA_STROOK.delete_kassa_strook_form()