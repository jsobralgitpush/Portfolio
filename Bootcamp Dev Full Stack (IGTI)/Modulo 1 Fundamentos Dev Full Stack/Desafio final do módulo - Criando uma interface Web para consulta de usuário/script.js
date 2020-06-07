window.addEventListener('load', start);

var caixaTexto = document.querySelector('#barra-texto');
var botaoSelec = document.querySelector('#botao-selec');
var campoFiltrado = document.querySelector('#show-data');
var campoEstatistica = document.querySelector('#show-stats');
var listaVazia = [];

function start() {
  botaoSelec.addEventListener('click', showPeople);
}

function showPeople() {
  let valorTexto = caixaTexto.value;

  const procura = users.results.map((person) => {
    return {
      nome: person.name.first,
      sobrenome: person.name.last,
      idade: person.dob.age,
      sexo: person.gender,
      foto: person.picture.thumbnail,
    };
  });

  function procuraTexto() {
    listaVazia = [];
    for (let i = 0; i < procura.length; i++) {
      if (procura[i].nome.indexOf(valorTexto) > -1) {
        listaVazia.push({
          nome: procura[i].nome,
          sobrenome: procura[i].sobrenome,
          idade: procura[i].idade,
          sexo: procura[i].sexo,
          foto: procura[i].foto,
        });
      }
    }
  }

  procuraTexto();

  console.log(listaVazia);

  function printaNaTela() {
    campoFiltrado.innerHTML = '';
    campoFiltrado.innerHTML = `<h2>${listaVazia.length} usuário(s) encontrado(s)</h2>`;
    for (let i = 0; i < listaVazia.length; i++) {
      var textNode = document.createTextNode(
        `${listaVazia[i].nome} ${listaVazia[i].sobrenome}, ${listaVazia[i].idade} anos`
      );

      var quebraLinha = document.createElement('br');
      var imagem = document.createElement('img');

      imagem.src = listaVazia[i].foto;

      campoFiltrado.appendChild(imagem);
      campoFiltrado.appendChild(textNode);
      campoFiltrado.appendChild(quebraLinha);
    }
  }

  printaNaTela();

  // Contadores
  var sexoMasculino = 0;
  var sexoFeminino = 0;
  var somaIdades = 0;

  function estatisticas() {
    // Fazendo o cálculo das estatísticas
    // a) sexo masculino e feminino
    for (let i = 0; i < listaVazia.length; i++) {
      if (listaVazia[i].sexo === 'female') {
        sexoFeminino = sexoFeminino + 1;
      } else if (listaVazia[i].sexo === 'male') {
        sexoMasculino = sexoMasculino + 1;
      }

      // b) Soma idades
      somaIdades = somaIdades + listaVazia[i].idade;
    }
  }

  // Gerando as estatisticas
  estatisticas();

  // c) Media de idades
  var mediaIdades = somaIdades / listaVazia.length;

  function criandoCampoEstatistiacas() {
    // a) limpando os dados
    campoEstatistica.innerHTML = ``;

    // b) Colocando os novos
    campoEstatistica.innerHTML = `
    <h2>Estatísticas</h2>
    <p>Sexo Masculino: ${sexoMasculino}</p>
    <br>
    <p>Sexo Feminino: ${sexoFeminino}</p>
    <br>
    <p>Soma idades: ${somaIdades}</p>
    <br>
    <p>Média das idades: ${Math.round(mediaIdades)}</p>`;
  }

  criandoCampoEstatistiacas();
}
