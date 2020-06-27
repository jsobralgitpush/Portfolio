import React, { Component } from 'react';
import MontanteInicial from './components/ProjetoBase/MontanteInicial';
import PeriodoMes from './components/ProjetoBase/PeriodoMes';
import TaxaDeJuros from './components/ProjetoBase/TaxaDeJuros';
import BlocoJuros from './components/ProjetoBase/BlocoJuros';
import jurosCompostos from './components/ProjetoBase/JurosCompostos'

export default class App extends Component {
  constructor() {
    super()

    this.state = {
      valor: 0,
      tempo: 0,
      taxa: 0
    }
  }

  handleChangeMontante = (event) => {
    this.setState({ valor: event.target.value })
  }

  handleChangeTempo = (event) => {
    this.setState({ tempo: event.target.value })
  }

  handleChangeJuros = (event) => {
    this.setState({ taxa: event.target.value })
  }


  renderRow = (montante) => {
    for (let i = 0; i <= montante.length; i++) {
      return (<BlocoJuros
        numParcela={montante[i]['numParcela']}
        montanteTotal={montante[i]['montanteTotal']}
        ganhoMes={montante[i]['ganhoMes']}
        ganhoPercentual={montante[i]['ganhoPercentual']} />)
    }
  }


  render() {
    const { valor, tempo, taxa } = this.state

    const montanteFinal = jurosCompostos(valor, tempo, taxa)

    return (
      <div>
        <div className='default-flex-row'>
          <MontanteInicial value={valor} changeValue={this.handleChangeMontante} />
          <PeriodoMes value={tempo} changeValue={this.handleChangeTempo} />
          <TaxaDeJuros value={taxa} changeValue={this.handleChangeJuros} />
        </div>
        <div className='default-flex-row'>
          {montanteFinal.map((item) => {
            const { numParcela, montanteTotal, ganhoMes, ganhoPercentual } = item

            return (
              < BlocoJuros
                numParcela={numParcela}
                montanteTotal={montanteTotal}
                ganhoMes={ganhoMes}
                ganhoPercentual={ganhoPercentual} />
            )

          })}
        </div>
      </div >
    )
  }
}
