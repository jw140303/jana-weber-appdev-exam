from deta import Deta
import streamlit as st
import pandas as pd

def connect_to_deta(db_name):
    deta = Deta(st.secrets["data_key"])

    # create a database
    db = deta.Base(db_name)

    return db


def fetch_data(db):
    return pd.DataFrame(db.fetch().items)