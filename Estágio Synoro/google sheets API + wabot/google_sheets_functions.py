import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys


class Google_sheets_API():

    def __init__(self, ID_plan, nome_aba=None, num_aba=None):
        self.ID_plan = ID_plan
        self.nome_aba = nome_aba
        self.num_aba = num_aba

        #Autenticação
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'CREDENCIAL.json', scope)
        gc = gspread.authorize(credentials)
        auth = gc

        #Selecionando a planilha pelo ID
        wks = auth.open_by_key(self.ID_plan)

        #Selecionando a aba da planilha
        if num_aba == None:
            worksheet_nome_aba = wks.worksheet(nome_aba)
            self.worksheet =  worksheet_nome_aba

        elif nome_aba == None:
            worksheet_num_aba = wks.get_worksheet(num_aba)
            self.worksheet =  worksheet_num_aba

        else:
            print('Usage: diga apenas o nome da aba que voce deseja selecionar como uma string ou o número do index dela')
            sys.exit()


    def select_data(self, cell: object = None, index_cell: object = None, find_cell: object = None) -> object:

        if cell == None and index_cell == None:
            selection = self.worksheet.find(find_cell)
            return selection

        elif cell == None and find_cell == None:
            selection = self.worksheet.cell(index_cell[0], index_cell[1]).value
            return selection

        elif index_cell == None and find_cell == None:
            selection = self.worksheet.acell(cell).value
            return selection

        else:
            print("""Usage: Selecione apenas uma
                    1-cell: Diga uma célula que você deseja selecionar Ex: 'A1'
                    2-index_cell: Diga o index da célula que deseja selecionar num array Ex: [0,1]
                    3-find_cell: Diga o nome do conteúdo da célula que deseja selecionar Ex: 'Telefone' """)
            sys.exit()

    def update_cell(self,  index_cell, new_value):
        try:
            self.worksheet.update_cell(index_cell[0], index_cell[1], new_value)
        except:
            print("""Usage:
                    1-index_cell: Diga o index da célula que deseja selecionar num array Ex: [0,1]
                    2-new_value: Diga a string que você quer atualizar
            """)
            sys.exit()



