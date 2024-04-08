
from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

class INVOICE:
    def add_invoice_form():
            st.header("Invoice Form")
            contact = st.text_input("Contact",key="contact")
            email = st.text_input("Email")
            amount = st.number_input("Amount",key="invoice_amount")
            bussiness_name = st.text_input("Business Name")
            bussiness_code = st.text_input("Business Code")
            description = st.text_area("Description",key="invoice_description")
            status = st.selectbox("Status", ["Pending", "Paid"], index=0)

            if st.button("Submit Invoice"):
                invoice = Invoice(contact=contact, email=email, amount=amount, bussiness_name=bussiness_name, bussiness_code=bussiness_code, description=description, status=status)
                session.add(invoice)
                session.commit()
                st.success("Invoice added successfully!")
    
    def update_invoice_form():

        def parse_response(response):
            if len(response) == 0:
                return "No invoices found"
            elif len(response) == 1:
                invoice = response[0]
                data = [(invoice.id, invoice.contact, invoice.email, invoice.amount, invoice.bussiness_name, invoice.bussiness_code, invoice.description, invoice.status, invoice.date, invoice.updated_date)]
                invoices_df = pd.DataFrame(data=data, columns=['id', 'contact', 'email', 'amount', 'bussiness_name', 'bussiness_code', 'description', 'status', 'date', 'updated_date'])
                return invoices_df
            else:
                data = [(invoice.id, invoice.contact, invoice.email, invoice.amount, invoice.bussiness_name, invoice.bussiness_code, invoice.description, invoice.status, invoice.date, invoice.updated_date) for invoice in response]
                invoices_df = pd.DataFrame(data=data, columns=['id', 'contact', 'email', 'amount', 'bussiness_name', 'bussiness_code', 'description', 'status', 'date', 'updated_date'])
                return invoices_df
                    
        st.header("Update Invoice Form")
        filter_date = st.date_input("Filter by Date")
    
        if st.button("Return invoice by date"):
            invoice = session.query(Invoice).filter(func.date(Invoice.date) == filter_date).all()
            st.dataframe(parse_response(invoice),use_container_width=True) 
            st.success("Invoice returned successfully!")

    def delete_invoice_form():
        st.header("Delete Invoice Form")
        id = st.number_input("ID that will be deleted", step=1, min_value=0)
        if st.button("Delete Invoice",disabled=False):
            invoice = session.query(Invoice).filter(Invoice.id == id).first()
            if invoice:
                session.delete(invoice)
                session.commit()
                st.success("Invoice deleted successfully!")
def main():
    tab1,tab2 = st.tabs(["Add Invoice","Update Invoice"])
    with tab1:
        INVOICE.add_invoice_form()
    with tab2:
        c1,c2 = st.columns([1,1])
        with c1:
            INVOICE.update_invoice_form()
        with c2:
            INVOICE.delete_invoice_form()

if __name__ == "__main__":
    main()