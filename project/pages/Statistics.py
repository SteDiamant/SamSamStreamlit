import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from project.models import Payment, Invoice, GiftCard, ExternalPayment, VaultCash, KassaStrook, EG, REPR
from functools import reduce
import seaborn as sns
import matplotlib.pyplot as plt  # Add this import statement


def read_data():
    engine = create_engine('sqlite:///samsam.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve data from each table
    payment_records = session.query(Payment).all()
    invoice_records = session.query(Invoice).all()
    gift_card_records = session.query(GiftCard).all()
    external_payment_records = session.query(ExternalPayment).all()
    vault_cash_records = session.query(VaultCash).all()
    kassa_strook_records = session.query(KassaStrook).all()
    eg_records = session.query(EG).all()
    repr_records = session.query(REPR).all()

    # Convert each set of records into a DataFrame
    payment_df = pd.DataFrame([vars(record) for record in payment_records])
    st.write(payment_df)
    payment_df['date'] = payment_df['date'].apply(lambda x: x.date())
    payment_df = payment_df.drop(columns=['id', '_sa_instance_state', 'updated_date'])

    invoice_df = pd.DataFrame([vars(record) for record in invoice_records])
    invoice_df['date'] = invoice_df['date'].apply(lambda x: x.date())
    invoice_df = invoice_df.drop(columns=['id', '_sa_instance_state', 'updated_date'])

    gift_card_df = pd.DataFrame([vars(record) for record in gift_card_records])
    gift_card_df['date'] = gift_card_df['date'].apply(lambda x: x.date())
    gift_card_df = gift_card_df.drop(columns=['id', '_sa_instance_state', 'updated_date'])

    external_payment_df = pd.DataFrame([vars(record) for record in external_payment_records])
    external_payment_df['date'] = external_payment_df['date'].apply(lambda x: x.date())
    external_payment_df = external_payment_df.drop(columns=['id', '_sa_instance_state', 'updated_date'])

    vault_cash_df = pd.DataFrame([vars(record) for record in vault_cash_records])
    vault_cash_df = vault_cash_df.drop(columns=['id', '_sa_instance_state', 'updated_date'])
    

    kassa_strook_df = pd.DataFrame([vars(record) for record in kassa_strook_records])
    kassa_strook_df['date'] = kassa_strook_df['date'].apply(lambda x: x.date())
    kassa_strook_df = kassa_strook_df.drop(columns=['id', '_sa_instance_state', 'updated_date'])

    eg_df = pd.DataFrame([vars(record) for record in eg_records]).drop(columns=['id', '_sa_instance_state'])

    repr_df = pd.DataFrame([vars(record) for record in repr_records]).drop(columns=['id', '_sa_instance_state'])

    #Payment_Cards SUM
    payment_df['Daily_payments'] = payment_df['visa'] + payment_df['mastercard'] + payment_df['maestro'] + payment_df['mastercard'] + payment_df['vpay'] 
    invoice_df['Daily_invoices'] = invoice_df['amount']
    gift_card_df['Daily_gift_cards'] = gift_card_df['amount']
    external_payment_df['Daily_external_payments'] = external_payment_df['amount']
    vault_cash_df['Daily_vault_cash'] = vault_cash_df['amount100']+vault_cash_df['amount50']+vault_cash_df['amount20']+vault_cash_df['amount10']+vault_cash_df['amount5']+vault_cash_df['amount2']+vault_cash_df['amount1']+vault_cash_df['amount050']+vault_cash_df['amount020']+vault_cash_df['amount010']+vault_cash_df['amount005']
    kassa_strook_df['Daily_kassa_strook'] = kassa_strook_df['Hoofdgerechten_8000']+kassa_strook_df['Nagerechten_8030']+kassa_strook_df['Gebak_8040']+kassa_strook_df['Kleine_kaart_8010']+kassa_strook_df['Dagschotels_8020']+kassa_strook_df['Dranken_hoog_8100']+kassa_strook_df['Frisdranken_overig_8200']+kassa_strook_df['Koffie_8300']+kassa_strook_df['Cultuurkaarten_4760']+kassa_strook_df['Dagschotelabonnementer_2200']+kassa_strook_df['Omzet_kadobonnen_2220']+kassa_strook_df['Catering_8050']+kassa_strook_df['Zaalhuur_8400']
    eg_df['Daily_eg'] = eg_df['EG_dranken_hoog']+eg_df['EG_dranken_laag']+eg_df['EG_Koffie']+eg_df['EG_Grote_kaart']+eg_df['EG_Kleine_kaart']+eg_df['EG_Dagschotels']+eg_df['EG_Nagerechten']+eg_df['EG_Gebak']
    repr_df['Daily_repr'] = repr_df['REPR_dranken_hoog']+repr_df['REPR_dranken_laag']+repr_df['REPR_Koffie']+repr_df['REPR_Grote_kaart']+repr_df['REPR_Kleine_kaart']+repr_df['REPR_Dagschotels']+repr_df['REPR_Nagerechten']+repr_df['REPR_Gebak']
    
    data_frames = [payment_df[['Daily_payments','date']], invoice_df[['Daily_invoices','date']], gift_card_df[['Daily_gift_cards','date']], external_payment_df[['Daily_external_payments','date']], vault_cash_df[['Daily_vault_cash','date']], kassa_strook_df[['Daily_kassa_strook','date']], eg_df[['Daily_eg','date']], repr_df[['Daily_repr','date']]]

    return data_frames


def plot_bar_chart(merged_df):
    dates = merged_df.index
    categories = merged_df.columns[:-1]
    values = merged_df.iloc[:, :-1].values
    merged_df.index = merged_df.index.map(str)
    st.bar_chart(merged_df, use_container_width=True,height=700)
    

    

def main():
        engine = create_engine('sqlite:///samsam.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        data_frames = read_data() 
        merged_df1 = data_frames[0]  
        merged_df2 = data_frames[0]
        for df in data_frames[1:]:
            merged_df1 = pd.merge(merged_df1, df, on='date', how='left') 
            merged_df2 = pd.merge(merged_df2, df, on='date', how='right')
        merged_df=merged_df1.combine_first(merged_df2)
        merged_df['Daily_total_ZITA']=merged_df['Daily_payments']+merged_df['Daily_invoices']+merged_df['Daily_gift_cards']+merged_df['Daily_external_payments']+merged_df['Daily_vault_cash']+merged_df['Daily_kassa_strook']+merged_df['Daily_eg']+merged_df['Daily_repr']
        merged_df=merged_df.set_index('date')
        st.title("Daily Total ZITA")
        plot_bar_chart(merged_df.drop(columns=['Daily_total_ZITA']))
        
            
if __name__ == "__main__":
    main()