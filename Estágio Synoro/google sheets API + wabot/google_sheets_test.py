import gspread
from oauth2client.service_account import ServiceAccountCredentials
from watbot import WABot

#---
#CREDENCIAIS
#Aqui são as API's que estamos usando
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#Credenciais que você consegue na sua pagina principal do google
credentials = ServiceAccountCredentials.from_json_keyfile_name(
         'synoromes.json', scope)

#Solicitando autorização
gc = gspread.authorize(credentials)

#---
#SELECIONANDO A PLANILHA
wks = gc.open_by_key('ID PLAN')

#---
#SELECIONANDO A ABA DA PLANILHA

#a) aqui pegamos pelo index da planilha
worksheet = wks.get_worksheet(1)

#b) aqui pegamos pelo nome da planilha
# worksheet = wks.worksheet("January")

#---
#SELECIONANDO DADOS

#a) Pela célula
val = worksheet.acell('A1').value

#b) Pelo numero da linha e coluna
val = worksheet.cell(1, 2).value

#Acessar uma célula pelo nome dela
cell = worksheet.find("Telefone")

#Podemos assim chamar uma linha ou coluna
print(cell.row)
print(cell.col)

#ACHANDO O TELEFONE
#a) Pegando a linha e a coluna de ontem temos o telefone
phone = worksheet.find("Telefone")
row_phone = phone.row
col_phone = phone.col


#b) Pegando o primeiro telefone
telefone_cliente = worksheet.cell(row_phone+1, col_phone).value #aqui estou usando "+1" mas o ideal é fazer mais i
print(telefone_cliente)

#ACHANDO O CORPO DA MENSAGEM
#a) Pegando a linha e a coluna do corpo da mensagem
body_mes = worksheet.find("Mensagem")
row_mes = body_mes.row
col_mes = body_mes.col

#b) Pegando a primeira mensagem
mensagem_cliente = worksheet.cell(row_mes+1, col_mes).value #aqui estou usando "+1" mas o ideal é fazer mais i

#MANDANDO A MENSAGEM
teste = WABot()
teste.send_message(telefone_cliente, mensagem_cliente)

#MUDANDO O TELEFONE PARA O NOSSO PADRÃO
telefone_cliente = telefone_cliente.replace('(', '').replace(')', '').replace('-', '')
telefone_cliente = f'55{telefone_cliente}'

#MARCAR CHECK NA FLAG CASO A MENSAGEM TENHA SIDO ENVIADA
#a) achando onde está a flag
flag = worksheet.find("Flag")
row_flag = flag.row
col_flag = flag.col

#b) Pegando a primeira mensagem
flag_body = worksheet.cell(row_flag+1, col_flag).value #aqui estou usando "+1" mas o ideal é fazer mais i

#c) Atualizando a celula
# worksheet.update_cell(row_flag+1,col_flag , 'Notcheck')

#MANDANDO A MENSAGEM E ATUALIZANDO A PLANILHA
telefone_cliente = telefone_cliente.replace('(', '').replace(')', '').replace('-', '')
telefone_cliente = f'55{telefone_cliente}'


if teste.send_message(telefone_cliente, mensagem_cliente)['sent'] == True:
    worksheet.update_cell(row_flag+1,col_flag , 'Voila')
else:
    print('ops')


#DEIXANDO DE MANDAR MENSAGEM CASO JÁ TENHAMOS UM PREENCHIMENTO
telefone_cliente = telefone_cliente.replace('(', '').replace(')', '').replace('-', '')
telefone_cliente = f'55{telefone_cliente}'


flag_body = worksheet.cell(row_flag+1,col_flag).value


if flag_body == '':
    if teste.send_message(telefone_cliente, mensagem_cliente)['sent'] == True:
        worksheet.update_cell(row_flag+1,col_flag , 'Voila')
    else:
        print('ops')
elif flag_body == 'Voila':
    print('ja ta preenchido')
else:
    print('algo estranho...')

