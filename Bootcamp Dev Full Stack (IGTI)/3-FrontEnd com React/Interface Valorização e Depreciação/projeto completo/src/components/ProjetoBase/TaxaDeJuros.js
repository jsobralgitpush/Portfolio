import React, { Component } from 'react';

export default class TaxaDeJuros extends Component {
  render() {
    const { value, changeValue } = this.props

    return (
      <div className="input-field col s6" >
        <form>
          <label >Taxa de Juros</label>
          <input type='number' onChange={changeValue} value={value} step={0.1}></input>
        </form>
      </div >
    );
  }
}