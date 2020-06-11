
botao = document.querySelector('.botao');
campoTexto = document.querySelector('.inner');

botao.addEventListener('click', imprimirData)

listaData = []

function imprimirData() {
  tempo = Date()
  listaData.push(tempo)
  textoExibido = ''
  for (let i = 0; i < listaData.length; i++) {
    textoExibido = `
    <p>${listaData[i]}</p>
    <p>${textoExibido}</p>
    `
  }

  campoTexto.innerHTML = textoExibido;
}
