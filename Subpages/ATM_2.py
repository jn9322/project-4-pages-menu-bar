import streamlit as st
import random


# random used for generating of random number on an account 
money_on_account_en = random.randint(-5_000,5_000)

# functions 

def withdrow_money_en():
    st.write("cau cau")

    to_be_withdrown_en = st.number_input("How much do you want to withdraw? 50 eur, 100 eur, 200 eur, 500 eur",
                                        max_value=500,
                                        placeholder= " "
                                 
    )
    
     

    if to_be_withdrown_en % 100 == 0:
        if to_be_withdrown_en == 100:
            st.write("cau cau cau")
            

            balance_en = money_on_account_en - to_be_withdrown_en
        
            if balance_en < 0:
                st.write("------------------")
                st.write("Not enough money on your account")
                st.write("------------------")
                

            elif balance_en >= 0:
                st.write("------------------")
                st.success(f"Money to be withdrown {to_be_withdrown_en} eur")
                st.write("Thank you - good bye")
                st.write("------------------")
                
                

                  
    else:
        st.write("------------------")
        st.warning("Not valid amount - please change it. 50 eur, 100 eur, 200 eur, 500 eur")
        st.write("------------------")
        

def select_operation_en():
    operation_en = st.selectbox("Select operation", ["", "1 - Withdraw money","2 - Input money to the account","3 - Account Balance", "4 - Return back -> Language selection","5 - Exit ATM"])

    if operation_en == "1 - Withdraw money":
        st.write("cau")
        withdrow_money_en()
    
    elif operation_en == "2 - Input money to the account":
        pass # input_money_en()

    elif operation_en == "3 - Account Balance":
        st.write("------------------")
        # st.write(f"Your actuall account balance is: {money_on_account} eur.")
        st.write("------------------")
        pass # select_operation_en()

    elif operation_en == "4 - Return back -> Language selection":
        pass # welcome()

    elif operation_en == "5 - Exit ATM":
        st.write("------------------")
        st.write("ATM exited - Good bye")
        st.write("------------------")
        exit()



# process

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('ATM - Start', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    lang_select = st.selectbox("Select language / Zvolte jazyk", ["","EN - English", "CZ - Čeština"])

    if lang_select == "EN - English":
        select_operation_en()
    
    if lang_select == "CZ - Čeština":
        pass #select_operation_cz()

if st.session_state.stage >= 2:
    pass

if st.session_state.stage >= 3:
    surname = st.text_input('Surname', on_change=set_state, args=[4])
    

if st.session_state.stage >= 4:
    st.button('Start Over', on_click=set_state, args=[0])
    