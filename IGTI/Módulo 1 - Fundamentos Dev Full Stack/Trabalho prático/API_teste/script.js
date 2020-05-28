window.addEventListener('load', start);

var listaPaises = document.querySelector('.data1');
var divPaises = document.querySelector('.nao-fav');

function start() {
  // Chamado da API
  fetch('https://restcountries.eu/rest/v2/all').then((res) => {
    res.json().then((data) => {
      return showData(data);
    })
  });

  console.log(newData);
}

function showData(data) {
  data.map((person) => {
    return newData =  {
      nome: person.name,
      id: person.numericCode,
      bandeira: person.flag,
      populacao: person.population,
    };
}

/* function NFavCountries() {
  for (let i = 0; i < showData(dataFromApi).length; i++) {
    var button = document.createElement('button');
    var imageCountry = document.createElement('img');
    var nameCountry = document.createElement('p');
    var populacao = documento.createElement('p');

    imageCountry.src = newData[i].bandeira;
    nameCountry.textContent = newData[i].nome;
    populacao.textContent = newData[i].populacao;

    listaPaises.appendChild(nameCountry);
    listaPaises.appendChild(populacao);
    listaPaises.appendChild(imageCountry);
    listaPaises.appendChild(button);
  }
} */
