// Puxando o arquivo de grades
const grade = require('./grades.json');

// Puxando modulos que usaremos durante a criação da API
const fs = require('fs');
const express = require('express');
const app = express();
const port = 8081;

//  Sem este trecho não conseguiremos escrever no formato JSON
app.use(express.json());

// Testando a conexão GET
app.get('/', (req, res) => {
  teste = JSON.stringify(grade['grades']);

  res.send(`${teste}`);
});

// Testando a conexão POST
app.post('/teste/:nome', (req, res) => {
  nome = req.params.nome;

  res.send(`${nome}`);
});

// Fim dos testes

// 1- Criando um endpoint para criarmos uma nova grade
app.post('/gradenova/:student/:subject/:type/:value', (req, res) => {
  try {
    nextId = grade['nextId'];
    student = req.params.student;
    subject = req.params.subject;
    type = req.params.type;
    value = req.params.value;
    timestamp = new Date();
  } catch (err) {
    res.send(
      'Você deve digitar uma rota do tipo /gradenova/student/subject/type/value'
    );
  }

  toInsert = {
    id: nextId,
    student: student,
    subject: subject,
    type: type,
    value: value,
    timestamp: timestamp,
  };

  newGrade = grade['grades'];
  newGrade.push(toInsert);

  newJson = { nextId: nextId + 1, grades: [...newGrade] };

  insertion = JSON.stringify(newJson);

  fs.writeFileSync('grades.json', insertion);

  res.send('Done, meu filho :)');
});

// 2- Atualizar a grade
app.post('/atualizargrade/:id/:student/:subject/:type/:value', (req, res) => {
  nextId = grade['nextId'];
  id = req.params.id;
  student = req.params.student;
  subject = req.params.subject;
  type = req.params.subject;
  value = req.params.value;
  timestamp = new Date();

  arrayGrades = grade['grades'];
  newGrade = arrayGrades.filter((itens) => itens.id != id);

  toInsert = {
    id: id,
    student: student,
    subject: subject,
    type: type,
    value: value,
    timestamp: timestamp,
  };

  newGrade.push(toInsert);

  newGrade.sort((a, b) => {
    return a['id'] - b['id'];
  });

  newJson = { nextId: nextId, grades: [...newGrade] };

  insertion = JSON.stringify(newJson);

  fs.writeFileSync('grades.json', insertion);

  res.send('Updated :)');
});

// 3-Excluir da grade
app.post('deletegrade/:id', (req, res) => {
  nextId = grade['nextId'];
  id = req.params.id;

  arrayGrade = grade['grades'];
  arrayGrade.filter((notas) => notas.id != id);

  newJson = { nextId: nextId, grades: [...newGrade] };

  insertion = JSON.stringify(newJson);

  fs.writeFileSync('grades.json', insertion);

  res.send('Updated :)');
});

// 4-Consulta de grade
app.get('/consultagrade/:id', (req, res) => {
  id = req.params.id;

  arrayGrade = grade['grades'];
  newGrade = arrayGrade.filter((itens) => itens.id == id);

  res.send(`${JSON.stringify(newGrade)}`);
});

// 5-Consulta nota
app.get('/consultanota/:student/:subject', (req, res) => {
  student = req.params.student;
  subject = req.params.subject;

  somaNotas = 0;

  arrayGrade = grade['grades'];
  newArray = arrayGrade.filter(
    (itens) => itens.student == student && itens.subject == subject
  );

  for (let i = 0; i < newArray.length; i++) {
    somaNotas += parseInt(newArray[i]['value']);
  }

  res.send(`${somaNotas}`);
});

// 6-Consulta media de subject e type
app.get('/consultamedia/:subject/:type', (req, res) => {
  subject = req.params.subject;
  type = req.params.type;

  arrayGrade = grade['grades'];
  newArrayGrade = arrayGrade.filter(
    (itensArray) => itensArray.subject == subject && itensArray.type == type
  );

  somaGrade = 0;

  for (let i = 0; i < newArrayGrade.length; i++) {
    somaGrade += newArrayGrade[i]['value'];
  }

  mediaGrade = somaGrade / newArrayGrade.length;

  res.send(`A média para dada subject e type é ${mediaGrade}`);
});

// 7-Retornar as melhores notas para determinada grade
app.get('/melhoresgrade/:subject/:type', (req, res) => {
  subject = req.params.subject;
  type = req.params.type;

  arrayGrade = grade['grades'];
  newArrayGrade = arrayGrade.filter(
    (itensArray) => itensArray.subject == subject && itensArray.type == type
  );

  listaNotas = [];

  for (let i = 0; i < newArrayGrade.length; i++) {
    listaNotas.push(newArrayGrade[i]['value']);
  }

  listaNotas.sort((a, b) => {
    return b - a;
  });

  res.send([`${listaNotas[0]}`, `${listaNotas[1]}`, `${listaNotas[2]}`]);
});

app.listen(port, () => {
  console.log(`Conectado na porta ${port}`);
});
