import streamlit as st
import pandas as pd
import csv
import re


# data import for visualization in streamlit app

def load_data():
    df = pd.read_csv("Data/CSV_entry_data.csv")
    return df

df_csv = load_data()
st.write(df_csv)


# data import for translation

def import_for_cycle_csv():
    with open("Data/CSV_entry_data.csv", newline="\n") as csv_soubor_input:
        reader = csv.reader(csv_soubor_input, delimiter=",")
        for line in reader:
            yield line
        
# object from data 
object_data_from_csv = import_for_cycle_csv()

st.write(object_data_from_csv)
