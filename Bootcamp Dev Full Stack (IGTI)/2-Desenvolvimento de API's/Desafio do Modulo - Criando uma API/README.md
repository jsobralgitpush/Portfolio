# Desafio do Módulo 2

- Entrega 12 jun em 19:30

## Instruções

**Informações sobre o Desafio**

**[grades.json](https://igti.instructure.com/courses/2935/files/193807/download?wrap=1 'grades.json')**

**[](https://igti.instructure.com/courses/2939/files/191351/download?wrap=1 'Script.sql')**

O Desafio do Módulo 2 está disponível! Consulte a data de entrega no
teste e em seu calendário.

**[](https://igti.instructure.com/courses/2939/files/191351/download?wrap=1 'Script.sql')**

Reserve um tempo para realizar a atividade, leia as orientações e
enunciados com atenção. Em caso de dúvidas utilize o "Fórum de dúvidas
do Desafio".

**[](https://igti.instructure.com/courses/2939/files/191351/download?wrap=1 'Script.sql')**

Para iniciá-lo clique em "Fazer teste". Você tem somente **uma**
tentativa e não há limite de tempo definido para realizá-lo. Caso
precise interromper a atividade, apenas deixe a página e, ao retornar,
clique em "Retomar teste".

**[](https://igti.instructure.com/courses/2939/files/191351/download?wrap=1 'Script.sql')**

Clique em "Enviar teste" **somente** quando você concluí-lo. Antes de
enviar confira todas as questões.

**[](https://igti.instructure.com/courses/2939/files/191351/download?wrap=1 'Script.sql')**

O gabarito será disponibilizado partir de sexta-feira, **12/06/2020**,
às 21h.

**[](https://igti.instructure.com/courses/2939/files/191351/download?wrap=1 'Script.sql')**

Bons estudos!

**Objetivos**

Exercitar os conceitos trabalhados no módulo para criação de uma API,
criando endpoints utilizando Node.js e Express.

**Enunciado**

Desenvolver uma API chamada “grades-control-api” para controlar notas de
alunos em matérias de um curso.

**Atividades**

O desafio final consiste em desenvolver uma API chamada
“grades-control-api” para controlar notas de alunos em matérias de um
curso.  Você deverá desenvolver endpoints para criação, atualização,
exclusão e consulta de notas, aqui chamadas de grades. As grades deverão
ser salvas em um arquivo json, chamado “grades.json”. Esse arquivo será
previamente fornecido e seus endpoints devem atuar considerando os
registros já existentes.

Uma grade deve possuir os campos abaixo:

- id (int): identificador único da grade. Deve ser gerado
  automaticamente pela API e garantir que não se repita.

- student (string): nome do aluno. Exemplo: “Guilherme Assis”.

- subject (string): nome da matéria. Exemplo: “Matemática”.

- type (string): nome da atividade. Exemplo: “Prova final”.

- value (float): nota da atividade. Exemplo: 10.

- timestamp (string): horário do lançamento. Exemplo:
  2020-05-19T18:21:24.964Z. Dica: utilizar o “new Date()” do JavaScript.

O arquivo grades.json será previamente fornecido com alguns registros
inseridos, seus endpoints devem trabalhar considerando a existência
deles, não devendo criar um arquivo limpo para utilização. A estrutura
do arquivo é a seguinte:

A propriedade nextId deve armazenar sempre o próximo id que será
utilizado na criação de uma nova grade. A propriedade grades possui um
array com várias grades, cada uma sendo representada por um objeto com
os campos descritos anteriormente.

Você deverá desenvolver os endpoints descritos abaixo:

1.  Crie um endpoint para criar uma grade. Este endpoint deverá receber
    como parâmetros os campos student, subject, type e value conforme
    descritos acima. Essa grade deverá ser salva no arquivo json
    grades.json, e deverá ter um id único associado. No campo timestamp
    deverá ser salvo a data e hora do momento da inserção. O endpoint
    deverá retornar o objeto da grade que foi criada. A API deverá
    garantir o incremento automático desse identificador, de forma que
    ele não se repita entre os registros. Dentro do arquivo grades.json
    que foi fornecido para utilização no desafio, o campo nextId já está
    com um valor definido. Após a inserção é preciso que esse nextId
    seja incrementado e salvo no próprio arquivo, de forma que na
    próxima inserção ele possa ser utilizado.
2.  Crie um endpoint para atualizar uma grade. Esse endpoint deverá
    receber como parâmetros o id da grade a ser alterada e os campos
    student, subject, type e value. O endpoint deverá validar se a grade
    informada existe, caso não exista deverá retornar um erro. Caso
    exista, o endpoint deverá atualizar as informações recebidas por
    parâmetros no registro, e realizar sua atualização com os novos
    dados alterados no arquivo grades.json.
3.  Crie um endpoint para excluir uma grade. Esse endpoint deverá
    receber como parâmetro o id da grade e realizar sua exclusão do
    arquivo grades.json.
4.  Crie um endpoint para consultar uma grade em específico. Esse
    endpoint deverá receber como parâmetro o id da grade e retornar suas
    informações.
5.  Crie um endpoint para consultar a nota total de um aluno em uma
    disciplina. O endpoint deverá receber como parâmetro o student e o
    subject, e realizar a soma de todas as notas de atividades
    correspondentes àquele subject, para aquele student. O endpoint
    deverá retornar a soma da propriedade value dos registros
    encontrados.
6.  Crie um endpoint para consultar a média das grades de determinado
    subject e type. O endpoint deverá receber como parâmetro um subject
    e um type, e retornar a média. A média é calculada somando o
    registro value de todos os registros que possuem o subject e type
    informados, dividindo pelo total de registros que possuem este mesmo
    subject e type.
7.  Crie um endpoint para retornar as três melhores grades de acordo com
    determinado subject e type. O endpoint deve receber como parâmetro
    um subject e um type, e retornar um array com os três registros de
    maior value daquele subject e type. A ordem deve ser do maior para o
    menor.\

    **Respostas Finais**

    Os alunos deverão desenvolver a prática e, depois, responder às
    seguintes questões objetivas.

    **IMPORTANTE:** responda as questões na ordem, e com o arquivo JSON
    do jeito que foi fornecido, sem efetuar alterações prévias, de forma
    a evitar dados inconsistentes.
