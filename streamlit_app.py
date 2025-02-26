import streamlit as st

pages = {
    "Obsah": [
        st.Page("Subpages/create_account.py", title="Create your account"),
        st.Page("Subpages/manage_account.py", title="Manage your account"),
        st.Page("Subpages/Pozor tlacitka - sequnce.py", title="POZOR tlacitka sequence"),
        st.Page("Subpages/CSV_to_XML.py", title="CSV to XML"),
        st.Page("Subpages/ATM.py", title="ATM"),
        st.Page("Subpages/ATM_2.py", title="ATM_2")
    ]
}

pg = st.navigation(pages)
pg.run()

