const fs = require('fs');

// Lendo os arquivos JSON
const fileCidades = require('./json_files/cidade_json.json');
const fileEstados = require('./json_files/estados_json.json');

// 1- Criando os arquivos JSON e passando o conteúdo para cada 1 deles
function itemUmCriandoJson() {
  for (let j = 0; j < fileEstados.length; j++) {
    for (let i = 0; i < fileCidades.length; i++) {
      // Abrindo as chaves para o arquivo JSON
      if (i === 0) {
        fs.appendFileSync(`json_files/${fileEstados[j]['Sigla']}.json`, '[');
      }

      // Passando o conteúdo de cada cidade
      if (fileCidades[i]['Estado'] === fileEstados[j]['ID']) {
        let data = JSON.stringify(fileCidades[i], null, 2);
        fs.appendFileSync(`json_files/${fileEstados[j]['Sigla']}.json`, data);
        fs.appendFileSync(`json_files/${fileEstados[j]['Sigla']}.json`, ',');
      }

      // Fechando as chaves do arquivo JSON
      if (i === fileCidades.length - 1) {
        fs.appendFileSync(`json_files/${fileEstados[j]['Sigla']}.json`, '{}');
        fs.appendFileSync(`json_files/${fileEstados[j]['Sigla']}.json`, ']');
      }
    }
  }
}

// Chamando a função para criar o arquivo de estados
// itemUmCriandoJson();

// 2- Criando a função para sabermos quantas cidades há num país
function itemDoisQtdCidades(UF) {
  try {
    estadoEscolhido = require(`./json_files/${UF}.json`);
  } catch (err) {
    console.log(`
    Tente verificar 2 coisas:
    1-Se o arquivo do estado está criado na pasta json_files
    2-Se dentro do arquivo há ao menos uma "{}" escrita`);
  }

  console.log(estadoEscolhido.length - 1);

  return estadoEscolhido.length - 1;
}

// 3-Função para sabermos os estados de maior num de cidades
function itemTresArrayEstados() {
  // Variáveis auxiliares
  var numCidades = [];
  var resultado = [];

  // Criando um array com o numero de cidades de cada estado
  for (let i = 0; i < fileEstados.length; i++) {
    nomeEstado = fileEstados[i]['Sigla'];
    arquivoEstado = require(`./json_files/${nomeEstado}.json`);
    numCidades.push({
      UF: `${fileEstados[i]['Sigla']}`,
      numCidades: `${arquivoEstado.length - 1}`,
    });
  }

  // Criando um filtro no array criado
  numCidades = numCidades.sort(function (a, b) {
    return b['numCidades'] - a['numCidades'];
  });

  // Criando um array da maneira pedida pelo enunciado
  for (let i = 0; i < 5; i++) {
    resultado.push(`${numCidades[i]['UF']} - ${numCidades[i]['numCidades']}`);
  }

  return resultado;
}

// 4- Função para sabermos os estados de menor num de cidades
function itemQuatroArrayEstados() {
  // Variáveis auxiliares
  var numCidades = [];
  var resultado = [];

  // Criando um array com o numero de cidades de cada estado
  for (let i = 0; i < fileEstados.length; i++) {
    nomeEstado = fileEstados[i]['Sigla'];
    arquivoEstado = require(`./json_files/${nomeEstado}.json`);
    numCidades.push({
      UF: `${fileEstados[i]['Sigla']}`,
      numCidades: `${arquivoEstado.length - 1}`,
    });
  }

  // Criando um filtro no array criado
  numCidades = numCidades.sort(function (a, b) {
    return a['numCidades'] - b['numCidades'];
  });

  // Criando um array da maneira pedida pelo enunciado
  for (let i = 0; i < 5; i++) {
    resultado.push(`${numCidades[i]['UF']} - ${numCidades[i]['numCidades']}`);
  }

  return resultado;
}

// 5- Função para sabermos as cidades de maior nome de cada estado
function itemCincoMaiorNome() {
  nomeCidade = [];

  // Criando um array com o numero de cidades de cada estado
  for (let i = 0; i < fileEstados.length; i++) {
    nomeCidadeTemp = [];

    nomeEstado = fileEstados[i]['Sigla'];
    arquivoEstado = require(`./json_files/${nomeEstado}.json`);

    for (let j = 0; j < arquivoEstado.length; j++) {
      // Pegando o tamanho do nome da cidade de cada estado
      try {
        tamNome = arquivoEstado[j]['Nome'].length;
      } catch (err) {
        continue;
      }

      // Colocando o UF e o tamanho do nome numa lista
      nomeCidadeTemp.push({
        UF: `${fileEstados[i]['Sigla']}`,
        nome: `${arquivoEstado[j]['Nome']}`,
        tamanhoNome: `${tamNome}`,
      });
    }
    // Fim do segundo 'for' com "j"

    // Criando um filtro no array criado para 'tamanhoNome'
    nomeCidadeTemp = nomeCidadeTemp.sort(function (a, b) {
      return b['tamanhoNome'] - a['tamanhoNome'];
    });

    // Adicionando apenas as cidades com nomes grandes
    for (let k = 0; k < 1; k++) {
      try {
        nomeCidade.push(
          `${nomeCidadeTemp[k]['nome']} - ${nomeCidadeTemp[k]['UF']}`
        );
      } catch (err) {
        continue;
      }
    }
  }

  return nomeCidade;
}

// 6- Função para sabermos as cidades de menor nome de cada estado
function itemSeisMenorNome() {
  nomeCidade = [];

  // Criando um array com o numero de cidades de cada estado
  for (let i = 0; i < fileEstados.length; i++) {
    nomeCidadeTemp = [];

    nomeEstado = fileEstados[i]['Sigla'];
    arquivoEstado = require(`./json_files/${nomeEstado}.json`);

    for (let j = 0; j < arquivoEstado.length; j++) {
      // Pegando o tamanho do nome da cidade de cada estado
      try {
        tamNome = arquivoEstado[j]['Nome'].length;
      } catch (err) {
        continue;
      }

      // Colocando o UF e o tamanho do nome numa lista
      nomeCidadeTemp.push({
        UF: `${fileEstados[i]['Sigla']}`,
        nome: `${arquivoEstado[j]['Nome']}`,
        tamanhoNome: `${tamNome}`,
      });
    }
    // Fim do segundo 'for' com "j"

    // Criando um filtro no array criado para 'tamanhoNome'
    nomeCidadeTemp = nomeCidadeTemp.sort(function (a, b) {
      return a['tamanhoNome'] - b['tamanhoNome'];
    });

    // Adicionando apenas as cidades com nomes grandes
    for (let k = 0; k < 1; k++) {
      nomeCidade.push(
        `${nomeCidadeTemp[k]['nome']} - ${nomeCidadeTemp[k]['UF']}`
      );
    }
  }

  return nomeCidade;
}

// 7- Retorna uma string que contem a cidade de maior nome em todo Brasil
function itemSeteMaiorNome() {
  // Variáveis auxiliares
  tamanhoNome = [];

  // Chamando a função com a lista de cidades de maior tamanho
  listaNomes = itemCincoMaiorNome();

  for (let i = 0; i < listaNomes.length; i++) {
    ufInicio = listaNomes[i].length - 2;
    ufFim = listaNomes[i].length;
    tamanhoNome.push({
      UF: `${listaNomes[i].slice(ufInicio, ufFim)}`,
      Cidade: `${listaNomes[i].slice(0, ufInicio - 3)}`,
      tamNome: `${listaNomes[i].slice(0, ufInicio - 3).length}`,
    });
  }

  // Criando um filtro com o maior nome de estados
  tamanhoNome.sort((a, b) => {
    return b['tamNome'] - a['tamNome'];
  });

  return `${tamanhoNome[0]['Cidade']} - ${tamanhoNome[0]['UF']}`;
}

// 8- Retorna uma string que contem a cidade de maior nome em todo Brasil
function itemOitoMenorNome() {
  // Variáveis auxiliares
  tamanhoNome = [];

  // Chamando a função com a lista de cidades de maior tamanho
  listaNomes = itemSeisMenorNome();

  for (let i = 0; i < listaNomes.length; i++) {
    ufInicio = listaNomes[i].length - 2;
    ufFim = listaNomes[i].length;
    tamanhoNome.push({
      UF: `${listaNomes[i].slice(ufInicio, ufFim)}`,
      Cidade: `${listaNomes[i].slice(0, ufInicio - 3)}`,
      tamNome: `${listaNomes[i].slice(0, ufInicio - 3).length}`,
    });
  }

  // Criando um filtro com o maior nome de estados
  tamanhoNome.sort((a, b) => {
    return a['tamNome'] - b['tamNome'];
  });

  return `${tamanhoNome[0]['Cidade']} - ${tamanhoNome[0]['UF']}`;
}
