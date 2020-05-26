function alturaArvoreUtopica(qtdCiclos) {
  var tamanhoArvore = 1;

  for (let i = 1; i < qtdCiclos + 1; i++) {
    if (i % 2 === 0) {
      tamanhoArvore = tamanhoArvore + 1;
    } else {
      tamanhoArvore = tamanhoArvore * 2;
    }
  }

  return tamanhoArvore;
}
