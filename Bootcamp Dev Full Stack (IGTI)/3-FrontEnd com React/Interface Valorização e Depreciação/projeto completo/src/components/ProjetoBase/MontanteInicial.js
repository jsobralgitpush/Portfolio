import React, { Component } from 'react';

export default class MontanteInicial extends Component {
  render() {
    const { value, changeValue } = this.props

    return (
      <div className="input-field col s6" >
        <form>
          <label >Montante Inicial</label>
          <input type='number' onChange={changeValue} value={value} min={1000} step={100}></input>
        </form>
      </div >
    );
  }
}

