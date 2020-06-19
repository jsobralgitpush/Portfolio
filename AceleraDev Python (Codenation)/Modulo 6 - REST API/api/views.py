from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def lambda_function(request):

        #1-Pegando os dados da requisição
        data = request.data['question']

        #2-Preenchendo um dicionário com a regra {'valor_lista':'repetições'}
        json_to_fill = {}
        for i in data:
                try:
                        json_to_fill[i] += 1
                except:
                        json_to_fill[i] = 1

        #3-Preenchendo uma lista com os valores da lista
        # dada as suas respecticas repetições
        result_list = []
        for k in sorted(json_to_fill, key=json_to_fill.get, reverse=True):

                for i in range(json_to_fill[k]):
                        result_list.append(k)

        #4-Montando o JSON do Response
        json_answer = {"solution":result_list}

        return Response(json_answer)

