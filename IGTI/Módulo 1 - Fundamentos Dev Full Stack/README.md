# Desafio do Módulo 1 {#quiz_title}

- Entrega 27 mai em 17:00

## Instruções

**Informações sobre o Desafio**

O Desafio do Módulo 1 está disponível! Consulte a data de entrega no
teste e em seu calendário.

Reserve um tempo para realizar a atividade, leia as orientações e
enunciados com atenção. Em caso de dúvidas utilize o "Fórum de dúvidas
do Desafio".

Para iniciá-lo clique em "Fazer teste". Você tem
somente **uma** tentativa e não há limite de tempo definido para
realizá-lo. Caso precise interromper a atividade, apenas deixe a página
e, ao retornar, clique em "Retomar teste".

Clique em "Enviar teste" **somente** quando você concluí-lo. Antes de
enviar confira todas as questões.

O gabarito será disponibilizado partir de sexta-feira, 29/05/2020, às
21h.

Bons estudos!

**Objetivos**

Exercitar os seguintes conceitos trabalhados no Módulo:

- Declarar elementos HTML como títulos, input, div, span, ul, li etc.
- Estilizar o app com CSS.
- Mapear elementos do DOM para serem manipulados com JavaScript.
- Formatar valores com JavaScript.
- Realizar diversos cálculos com array methods como map, filter e
  reduce.
- Realizar requisições HTTP com o comando fetch.

**Enunciado**

Criar uma aplicação para filtrar usuários e mostrar estatísticas a
partir do filtro definido.

**Atividades**

Os alunos deverão desempenhar as seguintes atividades:

1.  Na carga inicial da aplicação, obter os dados de:
    [https://randomuser.me/api/?seed=javascript&results=100&nat=BR&noinfo (Links
    para um site
    externo.)](https://randomuser.me/api/?seed=javascript&results=100&nat=BR&noinfo)
2.  Carregar os dados dos usuários em um array.
3.  Permitir a filtragem de usuários através de um input com interação
    do usuário.
4.  O usuário poderá filtrar dados quando digitar pelo menos um
    caractere no input.
5.  O usuário poderá filtrar os dados tanto digitando "Enter" quanto
    clicando no botão correspondente, conforme imagens mais abaixo.
6.  Montar dois painéis.
7.  No painel da esquerda, listar os usuários filtrados.
8.  No painel da direita, calcular e mostrar algumas estatísticas sobre
    esses usuários, conforme imagens abaixo.

**Tela inicial da aplicação (sugestão):      **

**![d1.png](imagens/d1.png)**

**Tela após filtro "santos":**

**![d2.png](imagens/d2.png)**

**Dicas**

1.  Após executar a requisição à API, filtre somente os dados
    necessários ao app. Esses são: name (first + last), picture, dob.age
    e gender.
2.  Monitore o input com o evento "keyup".
3.  Filtrem os dados a partir de qualquer posição no nome, ou seja, o
    nome "Brenda" (caso exista na API) deve ser retornado se o filtro
    for "a".
4.  Para filtrar, considere todo o texto em minúsculas. Assim, o filtro
    "E" trará tanto "Elena" quanto "Helena", caso existam na API.
5.  Dê um console.log() nos dados do evento de digitação e você
    descobrirá como "cercar" a tecla "Enter".
6.  Foque mais no código JavaScript e menos na interface. O mais
    importante é que o filtro e os cálculos estejam corretos.
7.  Quebre o seu código em funções bem definidas.
8.  Será necessária uma boa dose de manipulação manual do DOM. Isso pode
    ser feito tanto com innerHTML + string (recomendo a utilização de
    _template literals_) ou com os comandos document.createElement,
    appendChild etc.
9.  Se quiserem fazer uma interface semelhante à das imagens, utilizem o
    Materialize ([https://materializecss.com (Links para um site
    externo.)](https://materializecss.com/)).
10. Não deixem de assistir o vídeo desse desafio, onde demonstro a
    aplicação em funcionamento e dou mais algumas dicas.

\*\* \*\*

**Respostas Finais**

Os alunos deverão desenvolver a prática e, depois, responder às
seguintes questões objetivas:

[Fazer o
teste](https://igti.instructure.com/courses/2935/quizzes/34909/take?user_id=38152)

[\*\*Anterior Anterior: Informações sobre o
desafio](https://igti.instructure.com/courses/2935/modules/items/191175)
[Próximo\*\* Próximo: Segunda Aula Interativa do Módulo
1](https://igti.instructure.com/courses/2935/modules/items/190730)

32c40000-8b5f-43cb-a898-d255b170e5a6
