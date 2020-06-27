import React, { Component } from 'react';

export default class PeriodoMes extends Component {
  render() {
    const { value, changeValue } = this.props

    return (
      <div className="input-field col s6" >
        <form>
          <label >Período (meses)</label>
          <input type='number' onChange={changeValue} value={value}></input>
        </form>
      </div >
    );
  }
}