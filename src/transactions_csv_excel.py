import pandas as pd


def transactions_csv():
    """Функция для считывания финансовых операций из CSV"""
    df = pd.read_csv('../transactions.csv', delimiter=';')
    dict_data = df.to_dict(orient='records')
    return dict_data
#print(transactions_csv())

def transactions_excel():
    """Функция для считывания финансовых операций из Excel"""
    df = pd.read_excel('transactions_excel.xlsx')
    dict_dada = df.to_dict(orient='records')
    return dict_dada
#print(transactions_excel())

