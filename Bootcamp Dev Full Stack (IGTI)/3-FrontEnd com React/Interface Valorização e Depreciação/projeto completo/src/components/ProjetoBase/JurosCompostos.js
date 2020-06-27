export default function jurosComposto(valorInicial, tempo, taxa) {
  var montante = []

  for (let i = 1; i <= (tempo); i++) {
    var montanteNoMes = valorInicial * ((1 + (taxa / 100)) ** i);

    montante.push({
      'montanteTotal': montanteNoMes.toFixed(2),
      'numParcela': i,
      'ganhoPercentual': `${(((montanteNoMes / valorInicial) - 1) * 100).toFixed(2)} %`,
      'ganhoMes': (montanteNoMes - valorInicial).toFixed(2)
    })

  }

  return montante
}