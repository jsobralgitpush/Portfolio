import { accountsModel } from '../Schema/schemaAccount.js'

async function withdraw(req, res) {

  const agencia = req.params.agencia;
  const conta = req.params.conta;
  const value = req.params.value

  // Checking if the account exists
  accountsModel.find({ agencia: agencia, conta: conta }, function (err, user) {
    if (err) {
      res.send('Account does not exists')
    }
  })

  // query details
  var query = { conta: conta, agencia: agencia, balance: { $gte: value } }
  var toUpdate = { $inc: { balance: -value } }


  // Checking if the balance > withdraw
  const accountCheck = await accountsModel.find(query)
  if (accountCheck.length == 0) {
    res.send('Saldo Insuficiente, meu irmão')
  }

  // query
  const accountDeposit = await accountsModel.findOneAndUpdate(query, toUpdate)

  // checking the new account detail
  const accountDetail = await accountsModel.find(query)

  res.send(accountDetail)
}

export { withdraw }