from deta import Deta
import streamlit as st
import pandas as pd

def connect_to_deta(db_name):
    """
    This function connects the app to a database.
    The databases are used for user data.
    """
    deta = Deta(st.secrets["data_key"])

    # create a database
    db = deta.Base(db_name)

    return db

def fetch_data(db):
    """
    This function fetches data from a dataframe and stores it as a pandas dataframe.
    This allows for the data from an online database to be used in the code.
    """
    return pd.DataFrame(db.fetch().items)