window.addEventListener('load', start) // continuar daqui => {
  fetch('https://restcountries.eu/rest/v2/all').then((res) => {
    res.json().then((data) => {
      showData(data);
      NFavCountries(showData(data));
    });
  });

  var listaPaises = document.querySelector('.data1');
  var divPaises = document.querySelector('.nao-fav');

  start();
});

function showData(data) {
  var newData = data.map((person) => {
    return {
      nome: person.name,
      id: person.numericCode,
      bandeira: person.flag,
      populacao: person.population,
    };
  });

  return newData;
}

function start() {
  function NFavCountries(newData) {
    for (let i = 0; i < newData.length; i++) {
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
  }
  NFavCountries();
}
