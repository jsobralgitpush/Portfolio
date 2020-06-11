fetchCountries();

// Setup de variáveis
tabCountries = document.querySelector('#tab-countries');
tabFavorites = document.querySelector('#tab-favorites');
countryContainer = document.querySelector('.country-container');
countryList = document.querySelector('.country-list');
favoriteList = document.querySelector('.favorite-list');
botaoPais = document.querySelector('#botao');
listOfFavorites = [];
countAll = document.querySelector('#count-countries');
countFavorites = document.querySelector('#count-favorites');
totalPopulationAll = document.querySelector('#total-population-list');
totalPopulationFav = document.querySelector('#total-population-favorites');

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
  renderSummary();
  handleButtons();
}

function renderAll() {
  let divCompleta = '';

  for (let i = 0; i < mapedJson.length; i++) {
    let divIncompleta = `
    <div class = "country">
      <div>
        <a id=${mapedJson[i].id} class="waves-effect waves-light btn">+</a>
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
  divCompleta = '';

  listOfFavorites.forEach((country) => {
    divIncompleta = `
      <div class = "country">
        <div>
          <a id=${country.id} class="waves-effect waves-light btn red darken-4">-</a>
        </div>
          <img id=${country.id} src=${country.bandeira}></img>
        <div>
          <ul>
            <li id=${country.id}> ${country.nome} </li>
            <li id=${country.id}> ${country.populacao} </li>
          </ul>
        </div>
      </div>
      `;

    divCompleta += divIncompleta;
  });

  tabFavorites.innerHTML = divCompleta;
}

function renderSummary() {
  countAll.textContent = mapedJson.length;
  countFavorites.textContent = listOfFavorites.length;

  totalPopulationAll.textContent = mapedJson.reduce((counter, current) => {
    return (counter = counter + current.populacao);
  }, 0);

  totalPopulationFav.textContent = listOfFavorites.reduce(
    (counter, current) => {
      return (counter = counter + current.populacao);
    },
    0
  );
}

function handleButtons() {
  countryButtons = Array.from(tabCountries.querySelectorAll('.btn'));
  favoriteButtons = Array.from(tabFavorites.querySelectorAll('.btn'));

  countryButtons.forEach((button) =>
    button.addEventListener('click', () => {
      addToFav(button.id);
    })
  );

  favoriteButtons.forEach((button) =>
    button.addEventListener('click', () => {
      removeFromFav(button.id);
    })
  );
}

function addToFav(id) {
  countryToAdd = mapedJson.find((button) => button.id === id);
  listOfFavorites = [...listOfFavorites, countryToAdd];

  listOfFavorites.sort((a, b) => {
    return a.nome.localeCompare(b.nome);
  });

  mapedJson = mapedJson.filter((country) => country.id !== id);

  render();
}

function removeFromFav(id) {
  countryToRemove = listOfFavorites.find((country) => country.id === id);
  listOfFavorites = listOfFavorites.filter((country) => country.id !== id);

  mapedJson = [...mapedJson, countryToRemove];

  listOfFavorites.sort((a, b) => {
    return a.nome.localeCompare(b.nome);
  });

  render();
}
