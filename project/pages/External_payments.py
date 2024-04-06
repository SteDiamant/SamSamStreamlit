

from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

class EXTERNAL_PAYMENT:
    def add_external_payment_form():
        st.header("External Payment Form")
        source = st.text_input("Source", key="external_payment_source")
        amount = st.number_input("Amount",key="external_payment_amount")
        description = st.text_area("Description",key="external_payment_description")

        if st.button("Submit External Payment"):
            external_payment = ExternalPayment(source=source, amount=amount, description=description)
            session.add(external_payment)
            session.commit()
            st.success("External Payment added successfully!")

    def update_external_payment_form():

        def parse_response(response):
            if len(response) == 0:
                return "No external payments found"
            elif len(response) == 1:
                external_payment = response[0]
                data = [(external_payment.id, external_payment.source, external_payment.amount, external_payment.description, external_payment.date, external_payment.updated_date)]
                external_payments_df = pd.DataFrame(data=data, columns=['id', 'source', 'amount', 'description', 'date', 'updated_date'])
                return external_payments_df
            else:
                data = [(external_payment.id, external_payment.source, external_payment.amount, external_payment.description, external_payment.date, external_payment.updated_date) for external_payment in response]
                external_payments_df = pd.DataFrame(data=data, columns=['id', 'source', 'amount', 'description', 'date', 'updated_date'])
                return external_payments_df

        st.header("Update External Payment Form")
        filter_date = st.date_input("Filter by Date")
        if st.button("Return gift card by source"):
            gift_card = session.query(ExternalPayment).filter(func.date(ExternalPayment.date) == filter_date).all()
            st.dataframe(parse_response(gift_card), use_container_width=True)
            st.success("Gift card returned successfully!")

def main():
    tab1,tab2 = st.tabs(["Add External Payment","Update External Payment"])
    with tab1:
        EXTERNAL_PAYMENT.add_external_payment_form()
    with tab2:
        EXTERNAL_PAYMENT.update_external_payment_form()