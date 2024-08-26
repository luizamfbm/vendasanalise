import pandas as pd
from twilio.rest import Client

#your account SID from twilio.com/console
account_sid = ""
#your auth token from twilio.com/console
auth_token = ""
client = Client(account_sid, auth_token)


# abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+", #seu numero
            from_="+", #twilio phone number
            body=f'no mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
        print(message.sid)
# para cada arquivo: verificar se algum valor na coluna vendas naquele arquivo é maior que 55 mil

# se for maior que 55 mil - enviar um sms com o nome, o mês e as vendas do vendedor
# se não for maior que 55 mil, não fazer nada




