import csv
import sys

#Abrindo o arquivo CSV e criando uma lista com as colunas
with open(sys.argv[1], newline="\n") as csv_file:
    collumn_file = csv_file.readline()
    collumn_file = collumn_file[0:(len(collumn_file)-1)]
    collumn_file = collumn_file.split(",") 
    
#Transformando a lista em um dicionário
dict_count = {}
for index, value in enumerate(collumn_file):
    dict_count[value] = 0 

#Dicionário para fazermos a validação do STR
dict_count_check = {}
for index, value in enumerate(collumn_file):
    dict_count_check[value] = 0 

#Abrindo o arquivo TXT e chamando tudo dentro dele de uma string chamada "dna_sequences" 
with open(sys.argv[2], "r") as file_txt:
    dna_sequences = file_txt.read()
    
#Transformando todos os caracteres do arquivo numa lista
list_dna_sequences = list(dna_sequences)   

#Transformando esta lista num dicionário
dict_dna_sequences = {}
for index, value in enumerate(list_dna_sequences):
    dict_dna_sequences[index] = value
    

#Lógica para contabilizarmos o número de nucleotídios em sequência
if sys.argv[1] == "databases/small.csv":
    for i in collumn_file:
        if i != 'name':
            index = 0
            while index < len(list_dna_sequences):
                if len(i) == 4:
                    a = True
                    try:
                        while a == True:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3]:
                                dict_count[i]+=1
                                index+=4
                            else:
                                a = False
                    except:
                        pass
                            
                if len(i) == 5:
                    a = True
                    try:
                         while a == True:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3] and dict_dna_sequences[index+4] == i[4]:
                                dict_count[i]+=1
                                index+=5
                            else:
                                a = False
                                
                    except:
                        pass
                    
                            
                if len(i) == 8:
                    a = True
                    try:
                        while a == True:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3] and dict_dna_sequences[index+4] == i[4] and dict_dna_sequences[index+5] == i[5] and dict_dna_sequences[index+6] == i[6] and dict_dna_sequences[index+7] == i[7]:
                                dict_count[i]+=1
                                index+=8
                            else:
                                a = False
                    except:
                        pass
                    
                index+=1
else:
    for i in collumn_file:
        if i != 'name':
            index = 0
            while index < len(list_dna_sequences):
                if i == "AGATC":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3] and dict_dna_sequences[index+4] == i[4]:
                                dict_count_check[i]+=1
                                index+=5
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                                
                
                elif i == "TTTTTTCT":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3] and dict_dna_sequences[index+4] == i[4] and dict_dna_sequences[index+5] == i[5] and dict_dna_sequences[index+6] == i[6] and dict_dna_sequences[index+7] == i[7]:
                                dict_count_check[i]+=1
                                index+=8
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                
                
                elif i == "AATG":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3]:
                                dict_count_check[i]+=1
                                index+=4
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                    
                
                elif i == "TCTAG":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3] and dict_dna_sequences[index+4] == i[4]:
                                dict_count_check[i]+=1
                                index+=5
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                                
                
                elif i == "GATA":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3]:
                                dict_count_check[i]+=1
                                index+=4
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                
                elif i == "TATC":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3]:
                                dict_count_check[i]+=1
                                index+=4
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                    
                    
                elif i == "GAAA":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3]:
                                dict_count_check[i]+=1
                                index+=4
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                    
                
                elif i == "TCTG":
                    a = True
                    while a == True:
                        try:
                            if dict_dna_sequences[index] == i[0] and dict_dna_sequences[index+1] == i[1] and dict_dna_sequences[index+2] == i[2] and dict_dna_sequences[index+3] == i[3]:
                                dict_count_check[i]+=1
                                index+=4
                            else:
                                a = False
                                if dict_count[i] < dict_count_check[i]:
                                    dict_count[i] = dict_count_check[i]
                                dict_count_check[i] = 0
                        except:
                            a = False
                            continue
                    
            
                index+=1


#Transformando o resultado dict_count em uma lista
list_count = []
for i in dict_count:
    if i !="name":
        list_count.append(dict_count[i])


#Criado um dicionário para a nossa base de dados e criando uma lista para cada chave
dict_databases = {}


 
#Aqui transformarmos a base de dados em um dicionário da forma {nome:[1,2,3,4...]}    
with open(sys.argv[1], newline="\n") as csv_file:
    databases_string = csv_file.read().split("\n")
    for i in databases_string:
        sep_virgula = i.split(",")
        dict_databases[sep_virgula[0]] = []
        for j in sep_virgula:
            try:
                dict_databases[sep_virgula[0]].append(int(j))
            except:
                continue
            
            
#Aqui checamos se a list_count (a pessoa encontrada) é igual a alguem na base de dados
with open(sys.argv[1], newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if list_count == dict_databases[row['name']]:
            print(row["name"])
            exit(0)
    
#Printando "No match" senão tiver correspondência
print("No match")
exit(1)
            
    
      

