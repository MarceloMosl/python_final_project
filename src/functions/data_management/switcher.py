from functions import add_transaction, view_transactions_by_date, \
    view_all_transactions, edit_transaction, remove_transaction


def data_management_switch(value, df):
    switcher = {
        "1" : lambda: view_all_transactions(df),
        "2" : view_transactions_by_date(df),
        "3" : add_transaction(df),
        "4" : edit_transaction(df),
        "5" : remove_transaction(df),
        #"6" : ,
        #"7" : ,
        #"8" : ,
        #"9" : ,
        #"10" : ,
    }
    switcher.get(value, lambda: print("Data Management - Related functions."))()
