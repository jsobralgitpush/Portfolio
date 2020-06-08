from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    return resultado_ordenado(records)


def dic_resultado(records):
    # ***** 1-Criar um dicionário com o gabarito *****

    # a) listando todos os telefones diferentes
    telefones = set()
    for i in records:
        telefones.add(i['source'])

    # b) criando o dicionário com o gabarito
    resultado = []
    for i in telefones:
        resultado.append({"source": i, "total": 0})

    return resultado


def calculo_minutos_e_valor(records):

    #Chamando função anterior para criar dic com result
    resultado = dic_resultado(records)

    # ***** 2-Calculando minutos e valor de cada telefone *****
    # a) criando uma lista identica a records
    records_time = []
    for i in records:
        records_time.append(i)

    # Descrições do que acontece em cada passo abaixo
    for i in range(len(records_time)):

        # b) tirando o timestamp de cada telefone
        try:
            records_time[i]['end'] = \
                datetime.fromtimestamp(records_time[i]['end'])

            records_time[i]['start'] = \
                datetime.fromtimestamp(records_time[i]['start'])
        except:
            pass

        # Chamando chaves de auxílio
        records_time[i]['total_diurno'] = 0
        records_time[i]['total_noturno'] = 0
        records_time[i]['a pagar'] = 0

        # Chamando uma variável que sera uma barreira de horarios
        dez_horas_noite = \
            records_time[i]['end'].replace(hour=22, minute=0, second=0)
        seis_horas_manha = \
            records_time[i]['end'].replace(hour=6, minute=0, second=0)

        # c) calculando o total de minutos de uma ligação
        # 1)ligação comecou antes das 6 e terminou antes das 22
        if records_time[i]['start'] < seis_horas_manha \
                and records_time[i]['end'] < dez_horas_noite \
                and records_time[i]['end'] > seis_horas_manha:

            records_time[i]['total_noturno'] = \
                seis_horas_manha - records_time[i]['start']

            records_time[i]['total_diurno'] = \
                dez_horas_noite - records_time[i]['end']

            # Calculando os gastos
            gasto_matinal = records_time[i]['total_diurno'].seconds
            records_time[i]['a pagar'] += 0.36 + 0.09*(int(gasto_matinal / 60))
            records_time[i]['a pagar'] += 0.36


        # 2)ligação comecou depois das 6 e terminou antes das 22
        elif records_time[i]['start'] > seis_horas_manha \
                and records_time[i]['end'] < dez_horas_noite:

            records_time[i]['total_diurno'] = \
                records_time[i]['end'] - records_time[i]['start']

            # Calculando os gastos
            gasto_matinal = records_time[i]['total_diurno'].seconds
            records_time[i]['a pagar'] += 0.36 + 0.09*(int(gasto_matinal / 60))


        # 3)ligação comecou antes das 6 e terminou depois das 22
        elif records_time[i]['start'] < seis_horas_manha \
                and records_time[i]['end'] > dez_horas_noite:

            records_time[i]['total_noturno'] = \
                (seis_horas_manha - records_time[i]['start']) \
                + (dez_horas_noite - records_time[i]['end'])

            records_time[i]['total_diurno'] = datetime.timedelta(seconds=57600)

            # Calculando os gastos
            gasto_matinal = records_time[i]['total_diurno'].seconds
            records_time[i]['a pagar'] += 0.36 + 0.09*(int(gasto_matinal / 60))
            records_time[i]['a pagar'] += 0.36


        # 4)ligação comecou depois das 6 e terminou depois das 22
        elif records_time[i]['start'] > seis_horas_manha \
                and records_time[i]['end'] > dez_horas_noite \
                and records_time[i]['start'] < dez_horas_noite:

            records_time[i]['total_diurno'] = \
                dez_horas_noite - records_time[i]['start']

            records_time[i]['total_noturno'] = \
                records_time[i]['end'] - dez_horas_noite

            # Calculando os gastos
            gasto_matinal = records_time[i]['total_diurno'].seconds
            records_time[i]['a pagar'] += 0.36 + 0.09*(int(gasto_matinal / 60))
            records_time[i]['a pagar'] += 0.36


        # 5)ligação comecou antes das 6 e terminou antes das 6
        # 6)ligação comecou depois das 22
        elif records_time[i]['start'] < seis_horas_manha and \
                records_time[i]['end'] < seis_horas_manha \
                or records_time[i]['start'] > dez_horas_noite:

            records_time[i]['total_noturno'] = \
                records_time[i]['end'] - records_time[i]['start']

            # Calculando os gastos
            records_time[i]['a pagar'] += 0.36

    # *****3-Colocando os valores a pagar dentro de "resultados *****
    for dic in resultado:
        for i in range(len(records_time)):
            if dic['source'] == records_time[i]['source']:
                dic['total'] += records_time[i]['a pagar']

        dic['total'] = round(dic['total'], 2)

    return resultado


def resultado_ordenado(records):

    # Chamando funções anteriores para chegarmos ao resultado desordenado
    resultado_desordenado = calculo_minutos_e_valor(records)

    # ***** 4-Ordernando a lista *****
    list_ordenado = []
    resultado_ordenado = []
    for i in resultado_desordenado:
        list_ordenado.append(i['total'])

    list_ordenado.sort(reverse=True)

    for i in list_ordenado:
        j = 0
        a = True
        while a:
            if resultado_desordenado[j]['total'] == i:
                resultado_ordenado.append(resultado_desordenado[j])
                a = False
            else:
                j += 1

    return resultado_ordenado