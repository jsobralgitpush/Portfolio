fetchCountries();

// Setup de variáveis
tabCountries = document.querySelector('#tab-countries');
tabFavorites = document.querySelector('#tab-favorites');
countryContainer = document.querySelector('.country-container');
countryList = document.querySelector('.country-list');
favoriteList = document.querySelector('.favorite-list');
botaoPais = document.querySelector('#botao');

async function fetchCountries() {
  res = await fetch('https://restcountries.eu/rest/v2/all');
  json = await res.json();
  mapedJson = await json.map((data) => {
    return {
      nome: data.translations.pt,
      bandeira: data.flag,
      populacao: data.population,
      id: data.numericCode,
    };
  });

  render();
}

function render() {
  renderFav();
  renderAll();
}

function renderAll() {
  divCompleta = '';

  for (let i = 0; i < mapedJson.length; i++) {
    divIncompleta = `
    <div class = "country">
      <div>
        <input id='botao' type ='button' class=${mapedJson[i].id} value='+'></input>
      </div>
        <img id=${mapedJson[i].id} src=${mapedJson[i].bandeira}></img>
      <div>
        <ul>
          <li id=${mapedJson[i].id}> ${mapedJson[i].nome} </li>
          <li id=${mapedJson[i].id}> ${mapedJson[i].populacao} </li>
        </ul>
      </div>
    </div>
    `;

    divCompleta += divIncompleta;
  }

  tabCountries.innerHTML = `${divCompleta}`;
}

function renderFav() {
  divFavoritosComp = '';
  divFavoritosIncomp = '';
  botaoPais.addEventListener('click', () => {
    divFavoritosComp = `
    <div class = "country">
      <div>
        <input id='botao' type ='button' class=${mapedJson[mapedJson.find(botaoPais.class)].id} value='-'></input>
      </div>
        <img id=${mapedJson[i].id} src=${mapedJson[i].bandeira}></img>
      <div>
        <ul>
          <li id=${mapedJson[i].id}> ${mapedJson[i].nome} </li>
          <li id=${mapedJson[i].id}> ${mapedJson[i].populacao} </li>
        </ul>
      </div>
    </div>
  });
}
