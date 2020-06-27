import React, { Component } from 'react';

export default class BlocoJuros extends Component {
  render() {
    const { numParcela, montanteTotal, ganhoMes, ganhoPercentual } = this.props

    return (
      <div className='default-flex-row-border'>
        <p>{numParcela}</p>
        <div className='default-flex-row-border-2'>
          <p>{montanteTotal}</p>
          <p>{ganhoMes}</p>
          <p>{ganhoPercentual}</p>
        </div>
      </div>
    )
  }
}

