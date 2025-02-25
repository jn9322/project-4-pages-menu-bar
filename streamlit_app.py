import streamlit as st

pages = {
    "Obsah": [
        st.Page("Subpages/create_account.py", title="Create your account"),
        st.Page("Subpages/manage_account.py", title="Manage your account"),
        st.Page("Subpages/Pozor tlacitka - sequnce.py", title="POZOR tlacitka sequence"),
    ]
}

pg = st.navigation(pages)
pg.run()

