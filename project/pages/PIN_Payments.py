from project.models import Payment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

class PAYMENT:
    def add_payment_form():
        st.header("Payment Form")
        pinnumber = st.number_input("Pin Number", step=1, min_value=0, max_value=6)
        visa = st.number_input("Visa Amount")
        vpay = st.number_input("Vpay Amount")
        mastercard = st.number_input("Mastercard Amount")
        maestro = st.number_input("Maestro Amount")

        if st.button("Submit Payment"):
            payment = Payment(pinnumber=pinnumber, visa=visa, vpay=vpay, mastercard=mastercard, maestro=maestro)
            session.add(payment)
            session.commit()
            st.success("Payment added successfully!")

    def add_update_payment_form():
        
        def parse_response(response):
            if len(response) == 0:
                return "No payments found"
            elif len(response) == 1:
                print(response)
                #CONVERT Payment('4','1234', '1000.0', '2000.0', '3000.0', '4000.0', '2024-04-05 00:00:00') TO DATAFRAME
                payment = response[0]
                data = [(payment.id, payment.pinnumber, payment.visa, payment.vpay, payment.mastercard, payment.maestro, payment.registration_date)]
                payments_df=pd.DataFrame(data=data,columns=['id','pinnumber','visa','vpay','mastercard','maestro','date'])
                return payments_df
            else:
                data = [(payment.id, payment.pinnumber, payment.visa, payment.vpay, payment.mastercard, payment.maestro, payment.registration_date) for payment in response]
                payments_df=pd.DataFrame(data=data,columns=['id','pinnumber','visa','vpay','mastercard','maestro','date'])
                return payments_df
            
        st.header("Update Payment Form")
        filter = st.date_input("Filter by Date")
        if st.button("Return payment by date"):
            payment = session.query(Payment).filter(func.date(Payment.date) == filter).all()
            st.dataframe(parse_response(payment),use_container_width=True) 
            st.success("Payment returned successfully!")

def main():
    tab1,tab2 = st.tabs(["Add Payment","Update Payment"])
    with tab1:
        PAYMENT.add_payment_form()
    with tab2:
        PAYMENT.add_update_payment_form()

if __name__ == "__main__":
    main()