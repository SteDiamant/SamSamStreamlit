
from project.models import Payment,Invoice,GiftCard,ExternalPayment,VaultCash,KassaStrook,EG,REPR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st
from sqlalchemy import func
import pandas as pd

engine = create_engine('sqlite:///samsam.db')
Session = sessionmaker(bind=engine)
session = Session()

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

def main():
    tab1,tab2 = st.tabs(["Add Gift Card","Update Gift Card"])
    with tab1:
        GIFT_CARD.add_gift_card_form()
    with tab2:
        GIFT_CARD.update_gift_card_form()

if __name__=="__main__":
    main()