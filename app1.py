
from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

st.set_page_config(page_title="Streamlit Forms for Models", page_icon="🧊",layout='wide')
# Initialize SQLAlchemy engine and session

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
                payments_df=pd.DataFrame(data=data,columns=['id','pinnumber','visa','vpay','mastercard','maestro','registration_date'])
                return payments_df
            else:
                data = [(payment.id, payment.pinnumber, payment.visa, payment.vpay, payment.mastercard, payment.maestro, payment.registration_date) for payment in response]
                payments_df=pd.DataFrame(data=data,columns=['id','pinnumber','visa','vpay','mastercard','maestro','registration_date'])
                return payments_df
            
        st.header("Update Payment Form")
        filter = st.date_input("Filter by Date")
        if st.button("Return payment by date"):
            payment = session.query(Payment).filter(func.date(Payment.registration_date) == filter).all()
            st.dataframe(parse_response(payment),use_container_width=True) 
            st.success("Payment returned successfully!")
            

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

class GIFT_CARD:

    def add_gift_card_form():
        st.header("Gift Card Form")
        source = st.text_input("Source")
        amount = st.number_input("Amount")
        description = st.text_area("Description")

        if st.button("Submit Gift Card"):
            gift_card = GiftCard(source=source, amount=amount, description=description)
            session.add(gift_card)
            session.commit()
            st.success("Gift Card added successfully!")
    
    def update_gift_card_form():

        def parse_response(response):
            if len(response) == 0:
                return "No gift cards found"
            elif len(response) == 1:
                gift_card = response[0]
                data = [(gift_card.id, gift_card.source, gift_card.amount, gift_card.description, gift_card.date, gift_card.updated_date)]
                gift_cards_df = pd.DataFrame(data=data, columns=['id', 'source', 'amount', 'description', 'date', 'updated_date'])
                return gift_cards_df
            else:
                data = [(gift_card.id, gift_card.source, gift_card.amount, gift_card.description, gift_card.date, gift_card.updated_date) for gift_card in response]
                gift_cards_df = pd.DataFrame(data=data, columns=['id', 'source', 'amount', 'description', 'date', 'updated_date'])
                return gift_cards_df

        st.header("Update Gift Card Form")
        filter_date = st.date_input("Filter by Date")
        if st.button("Return gift card by source"):
            gift_card = session.query(GiftCard).filter(func.date(GiftCard.date) == filter_date).all()
            st.dataframe(parse_response(gift_card), use_container_width=True)
            st.success("Gift card returned successfully!")

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

# @st.cache
# def login_form():
#     st.title("Login Form")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "admin":
#             st.success("Logged in as admin")
#             return True
#         else:
#             st.error("Invalid credentials")


def main():
    st.title("Streamlit Forms for Models")

    # Create tabs for navigation
    tabs = ["Payment", "Invoice", "Gift Card", "External Payment", "Vault Cash", "Kassa Strook", "EG", "REPR"]
    selected_tab = st.sidebar.radio("Select Form", tabs)

    if selected_tab == "Payment":
        tab1,tab2 = st.tabs(["Add Payment","Update Payment"])
        with tab1:
            PAYMENT.add_payment_form()
        with tab2:
            PAYMENT.add_update_payment_form()

        
    elif selected_tab == "Invoice":
        tab1,tab2 = st.tabs(["Add Invoice","Update Invoice"])
        with tab1:
            INVOICE.add_invoice_form()
        with tab2:
            INVOICE.update_invoice_form()
        
    elif selected_tab == "Gift Card":
        tab1,tab2 = st.tabs(["Add Gift Card","Update Gift Card"])
        with tab1:
            GIFT_CARD.add_gift_card_form()
        with tab2:
            GIFT_CARD.update_gift_card_form()

    elif selected_tab == "External Payment":
        tab1,tab2 = st.tabs(["Add External Payment","Update External Payment"])
        with tab1:
            EXTERNAL_PAYMENT.add_external_payment_form()
        with tab2:
            EXTERNAL_PAYMENT.update_external_payment_form()

    elif selected_tab == "Vault Cash":
        tab1,tab2 = st.tabs(["Add Vault Cash","Update Vault Cash"])
        with tab1:
            VAULT_CASH.add_vault_cash_form()
        with tab2:
            VAULT_CASH.update_vault_cash_form()

    elif selected_tab == "Kassa Strook":
        tab1,tab2=st.tabs(["Add Kassa Strook","Update Kassa Strook"])
        with tab1:
            KASSA_STROOK.add_kassa_strook_form()
        with tab2:
            KASSA_STROOK.update_kassa_strook_form()
        
    elif selected_tab == "EG":
        tab1,tab2=st.tabs(["Add EG","Update EG"])
        with tab1:
            E_G.add_eg_form()
        with tab2:
            E_G.update_eg_form()
    elif selected_tab == "REPR":
        tab1,tab2=st.tabs(["Add REPR","Update REPR"])
        with tab1:
            R_E_P_R.add_repr_form()
        with tab2:
            R_E_P_R.update_repr_form()
    else:
        st.error("Invalid tab selection")


    

# Add forms for other models similarly

if __name__ == "__main__":
    main()
