import { accountsModel } from '../Schema/schemaAccount.js'

async function privateAccount(req, res) {

  // Pegando todas as agencias
  var groupQuery = [
    {
      $group:
      {
        _id: "$agencia",
      }
    }
  ]

  // Procurando todas as agencias
  const allAgencies = await accountsModel.aggregate(groupQuery)

  // Criando um array com o numero das agencias
  var agenciasCadastradas = []
  for (let i = 0; i < allAgencies.length; i++) {
    agenciasCadastradas.push(allAgencies[i]['_id'])
  }

  // Procurando a pessoa com maior saldo em cada agencia
  var maiorSaldo = []
  for (let i = 0; i < agenciasCadastradas.length; i++) {
    var pessoaMaiorSaldo = await accountsModel.find({ agencia: agenciasCadastradas[i] }).sort({ balance: -1 }).limit(1)
    maiorSaldo.push(pessoaMaiorSaldo)
  }

  // Transferindo cada uma dessas pessoas para agencia private
  for (let i = 0; i < maiorSaldo.length; i++) {
    var queryFilter = maiorSaldo[i]
    var toUpdate = { $set: { agencia: 99 } }
    await accountsModel.findByIdAndUpdate(queryFilter, toUpdate)

  }

  const newFilter = { agencia: 99 }

  const privateAccounts = await accountsModel.find(newFilter)

  res.send(privateAccounts);
}

export { privateAccount }