
import random
import streamlit as st

# random used for generating of random number on an account 
money_on_account = random.randint(-10_000,10_000)


# Step 3.2 EN - step of inserting money + account balance after the insert
def input_money_en():
    to_be_inserted_en = int(input("How much do you insert?"))
    balance_money_en = money_on_account + to_be_inserted_en
    print(f"{to_be_inserted_en} eur has been inserted to your account. Actuall balance: {balance_money_en} eur.")

# Step 3.1 EN - withdraw money + comparison if there is enough money on account
def withdrow_money_en():
    print("------------------")
    to_be_withdrown_en = int(input("How much do you want to withdraw ?\n * 100\n * 200\n * 500\n * other (amount divadable by 100)\n * Return to menu - 999 \n"))
    balance_en = money_on_account - to_be_withdrown_en
    
    if to_be_withdrown_en % 100 == 0:
        if balance_en < 0:
            print("------------------")
            print("Not enough money on your account")
            print("------------------")
            select_operation_en()

        elif balance_en >= 0:
            print("------------------")
            print(f"Money to be withdrown {to_be_withdrown_en} eur")
            print("Thank you - good by")
            print("------------------")
            exit()

        else:
            print("Unexpected error")
            select_operation_en()

    else:
        print("------------------")
        print("Not valid amount / Return to menu")
        print("------------------")
        select_operation_en()

# Step 3.2 CZ - step of inserting money + account balance after the insert
def input_money_cz():
    to_be_inserted_cz = int(input("Kolik chcete vlozit?"))
    balance_money = money_on_account + to_be_inserted_cz
    print("------------------")
    print(f"Na Vas ucet bylo vlozeno: {to_be_inserted_cz} Kc. Vas aktualni zustatek je: {balance_money} Kc.")
    print("------------------")
    select_operation_cz()

# Step 3.1 CZ - withdrow money + comparison if there is enough money on account
def withdrow_money_cz():
    print("------------------")
    to_be_withdrown_cz = int(input("Kolik chcete vybrat?\n * 500\n * 1000\n * 2000\n * Jina castka (zadejte castku delitelnou 500)\n * Pro navrat do menu: 999  \n"))
    balance = money_on_account - to_be_withdrown_cz

    if to_be_withdrown_cz % 500 == 0:
        
        if balance < 0:
            print("------------------")
            print("Neni dostatek penez na uctu")
            print("------------------")
            select_operation_cz()

        elif balance >= 0:
            print("------------------")
            print(f"Castka {to_be_withdrown_cz} Kc byla vybrana")
            print("Dekujeme - hezky den")
            print("------------------")
            exit()

        else:
            print("------------------")
            print("Neocekavany error")
            print("------------------")
        
    else:
        print("------------------")
        print("Neplatna castka zadana / navrat do menu")
        print("------------------")
        select_operation_cz()



# Step 3 CZ - menu options
def select_operation_cz():
    operation_cz = input(str(("Vyberte:\n1 - Vyber hotovosti \n2 - Vklad na ucet \n3 - Stav uctu \n4 - Krok zpet -> Vyber jazyku \n5 - Konec\n")))

    if operation_cz == "1":
        withdrow_money_cz()
    
    elif operation_cz == "2":
        input_money_cz()

    elif operation_cz == "3":
        print("------------------")
        print(f"Vas zustatek je: {money_on_account} Kc.")
        print("------------------")
        select_operation_cz()

    elif operation_cz == "4":
        welcome()
    
    elif operation_cz == "5":
        print("------------------")
        print("Program ukoncen - pekny den")
        print("------------------")
        exit()

    else:
        print("------------------")
        print("Nesxistujici krok")
        print("------------------")
        select_operation_cz()
        
# Step 3 EN - menu options
def select_operation_en():
    operation_en = st.selectbox("Select operation", ["", "1 - Withdraw money","2 - Input money to the account","3 - Account Balance", "4 - Return back -> Language selection","5 - Exit ATM"])

    if operation_en == "1 - Withdraw money":
        withdrow_money_en()
    
    elif operation_en == "2 - Input money to the account":
        input_money_en()

    elif operation_en == "3 - Account Balance":
        st.write("------------------")
        st.write(f"Your actuall account balance is: {money_on_account} eur.")
        st.write("------------------")
        select_operation_en()

    elif operation_en == "4 - Return back -> Language selection":
        welcome()

    elif operation_en == "5 - Exit ATM":
        st.write("------------------")
        st.write("ATM exited - Good bye")
        st.write("------------------")
        exit()

# Step 2 - Language selection
def welcome():
    st.write("------------------")
    st.write("Vitejte u KB! / Welcome to KB ATM!")
    st.write("------------------")
    
    st.write("Select language/ Zvolte jazyk")

    lang_select = st.selectbox("", ["","EN - English", "CZ - Čeština"])
    
    if lang_select == "EN - English":
        select_operation_en()
    
    if lang_select == "CZ - Čeština":
        select_operation_cz()

 
           
      
# Step 1 - Execution
if st.button("ATM start"):
    welcome()
