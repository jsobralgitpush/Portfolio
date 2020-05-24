# Bem-vindo ao desafio!

Olá,

Essa é parte do Desafio On-line do programa Santander Coders by
Digital House. Aqui você vai demonstrar o que aprendeu até o momento
com a resolução dos exercícios.

Você pode começar o Desafio On-line a qualquer momento, porém
recomendamos que faça primeiro os exercícios e depois o desafio.

A ordem de resolução não afetará o critério de seleção.

Boa sorte!

# Desafio

Chegou o momento de fazer o desafio. Agora é com você!

Aqui você não terá o auxílio dos professores na resolução dos exercícios.

Se ainda restou alguma dúvida acesse a documentação oficial:

https://www.w3schools.com/js/js_syntax.asp
https://www.w3schools.com/js/js_variables.asp
https://www.w3schools.com/js/js_operators.asp
https://www.w3schools.com/js/js_functions.asp
https://www.w3schools.com/js/js_arrays.asp
https://www.w3schools.com/js/js_booleans.asp
https://www.w3schools.com/js/js_if_else.asp
https://www.w3schools.com/js/js_loop_for.asp

Mas tem outros links:

http://www.javascript-tutorial.com.br/content-4.html
http://www.javascript-tutorial.com.br/content-6.html
http://www.javascript-tutorial.com.br/content-9.html

Se você não passar fique tranquilo! Vamos te ajudar novamente na resolução dos exercícios do nivelamento. Não existe um limite no número de tentativas do desafio.

Que a força esteja com você!

# Desafio - Professora Furiosa

Uma professora de programação, cansada de que os estudantes cheguem tarde, decidiu que vai cancelar a aula se há poucos presentes.

Ela representa a entrada dos estudantes como um array de tempos de chegada tarde, em minutos. Por exemplo, se um estudante chegou 10 minutos atrasado, outro 5 minutos antes da hora, outro com 3 minutos de atraso, e outro pontual, poderá representar assim:

_var alunosDaSegunda = [10, -5, 3, 0];_

Com essa informação e a quantidade mínima de estudantes para que suceda o curso, a professora quer saber se a aula acontecerá. Por exemplo, supondo que a quantidade mínima de estudantes para que a aula aconteça é de 2 alunos, então o curso da segunda-feira se realizará, porque houve um estudante que foi pontual e um estudante que chegou cedo.

_acontece(alunosDaSegunda, 2)_
**true**

Mas se a quantidade mínima fosse 3, a aula não aconteceria:

acontece(alunosDaSegunda, 3)
**false**

Escreva as seguintes funções: 1. acontece, que diz se a aula sucederá de acordo com o array dos estudantes que entraram. 2. aberturas, que utiliza um array com os arrays dos estudantes que entraram nos outros dias, e a quantidade mínima de estudantes, e diga quais os dias em que as aulas aconteceram e quais não. Por exemplo:

aberturas([alunosDaSegunda, alunosDaTerça, alunosDaQuarta], 2)
[true, false, false]
