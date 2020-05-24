function acontece(arrayEstudantes, minEstudantes) {
  var qtdAlunos = 0;
  for (let i = 0; i < arrayEstudantes.length; i++) {
    if (arrayEstudantes[i] <= 0) {
      qtdAlunos = qtdAlunos + 1;
    }
  }

  if (qtdAlunos >= minEstudantes) {
    return true;
  } else {
    return false;
  }
}

function aberturas(arrayDias, minAlunos) {
  var listaFinal = [];
  for (let i = 0; i < arrayDias.length; i++) {
    var j = acontece(arrayDias[i], minAlunos);
    listaFinal.push(j);
  }

  return listaFinal;
}
