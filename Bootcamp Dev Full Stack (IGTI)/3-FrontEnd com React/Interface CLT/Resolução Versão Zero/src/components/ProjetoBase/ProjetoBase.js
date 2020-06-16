import React, { Component } from 'react';
import { calculateSalaryFrom } from './salary'

export default class ProjetoBase extends Component {
  constructor(props) {
    super(props)

    this.state = {
      valueSalario: 0,
      baseInss: 0,
      descontoInss: 0,
      baseIrpf: 0,
      descontoIrpf: 0,
      netSalary: 0
    }

    this.handleSalario = this.handleSalario.bind(this);


  }

  handleSalario(event) {
    this.setState({ valueSalario: event.target.value })

    const { valueSalario, baseInss, descontoInss, baseIrpf, descontoIrpf, netSalary } = this.state

    this.setState({
      baseInss: calculateSalaryFrom(valueSalario)['baseINSS'],
      descontoInss: calculateSalaryFrom(valueSalario)['discountINSS'],
      baseIrpf: calculateSalaryFrom(valueSalario)['baseIRPF'],
      descontoIrpf: calculateSalaryFrom(valueSalario)['discountIRPF'],
      netSalary: calculateSalaryFrom(valueSalario)['netSalary']
    })

  }


  render() {

    const { valueSalario, baseInss, descontoInss, baseIrpf, descontoIrpf, netSalary } = this.state

    return (
      <div className="padding default-flex-row">

        <h1>React Salary</h1>

        <form>
          <label>Salário Bruto</label>
          <input className='valorSalario' type='number' onDoubleClick={this.handleSalario}></input>
          <label>Base INSS</label>
          <input readOnly

            value={new Intl.NumberFormat('pt-BR', {
              style: 'currency', currency: 'BRL'
            }).format(baseInss)}>

          </input>

          < label > Desconto INSS</label>
          <input readOnly


            value={`${new Intl.NumberFormat('pt-BR', {
              style: 'currency', currency: 'BRL'
            }).format(descontoInss)} (${Math.round(descontoInss / valueSalario * 100)} %)`}>


          </input>

          <label>Base IRPF</label>
          <input readOnly


            value={new Intl.NumberFormat('pt-BR', {
              style: 'currency', currency: 'BRL'
            }).format(this.state.baseIrpf)}>


          </input>

          <label>Desconto IRPF</label>
          <input readOnly

            value={`${new Intl.NumberFormat('pt-BR', {
              style: 'currency', currency: 'BRL'
            }).format(this.state.descontoIrpf)} (${Math.round(descontoIrpf / baseIrpf * 100)} %)`}>


          </input>

          <label>Salário Líquido</label>
          <input readOnly

            value={new Intl.NumberFormat('pt-BR', {
              style: 'currency', currency: 'BRL'
            }).format(this.state.netSalary)}>


          </input>
        </form>

      </div >

    );
  }
}
