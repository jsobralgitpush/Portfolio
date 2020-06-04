from google_sheets_functions import Google_sheets_API
from watbot import WABot

ID_plan = 'confidencial'
worksheet = Google_sheets_API(ID_plan, None, 1)
wabot = WABot()


for i in range(100):
    #1-SELECIONANDO O TELEFONE
    telefone_field = worksheet.select_data(None, None, 'Telefone')

    #a) Numero da linha e da coluna da celula "telefone"
    row_tell = telefone_field.row
    col_tell = telefone_field.col

    #b) Index telefone
    index_tell = [row_tell+1+i, col_tell]

    #c) Valor do telefone
    client_tel = worksheet.select_data(None, index_tell, None)

    #d) Cancelado a execução se o telefone for vazia
    if client_tel == '':
        index_tell = [row_tell+2+i, col_tell]
        client_tel = worksheet.select_data(None, index_tell, None)
        if client_tel == '':
            break

    #d) Ajustando a string do telefone
    client_tel = client_tel.replace('(', '').replace(')', '').replace('-', '')
    client_tel = f'55{client_tel}'


    #2-SELECIONANDO O CORPO DA MENSAGEM
    body_field = worksheet.select_data(None, None, 'Mensagem')

    # a) Numero da linha e da coluna da celula "mensagem"
    row_mes = body_field.row
    col_mes = body_field.col

    # b) Index mensagem
    index_mens = [row_mes+1+i, col_mes]

    # c) Valor da Mensagem
    client_mensagem = worksheet.select_data(None, index_mens, None)


    #3-SELECIONANDO A FLAG
    flag = worksheet.select_data(None, None, "Flag")

    #a) Numero da linha e da coluna da celula "flag"
    row_flag = flag.row
    col_flag = flag.col

    #b) Index flag
    index_flag = [row_flag + 1 + i, col_flag]

    #c) Valor da flag
    client_flag = worksheet.select_data(None, index_flag, None)


    #4-MANDANDO A MENSAGEM
    if client_flag == '':
        if wabot.send_message(client_tel, client_mensagem)['sent'] == True:
            worksheet.update_cell(index_flag, 'Enviada')
        else:
            print('ops')
            print(client_tel)

    elif client_flag == 'Enviada':
        print('Mensagem já foi enviada')

    else:
        print('algo estranho...')

