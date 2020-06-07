// Puxando o arquivo de grades
const grade = require('./grades.json');

const fs = require('fs');

const express = require('express');
const app = express();
const port = 8081;

//  Sem este trecho não conseguiremos escrever no formato JSON
app.use(express.json());

// Testando a conexão
app.get('/', (req, res) => {
  a = JSON.stringify(grade['grades']);

  res.send(`${a}`);
});

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

  console.log(newGrade);

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

  console.log(newArray);
  res.send(`${somaNotas}`);
});

app.listen(port, () => {
  console.log(`Conectado na porta ${port}`);
});

/* array = grade['grades'];
newArray = array.filter((ids) => ids.id != 49);
console.log(newArray); */
