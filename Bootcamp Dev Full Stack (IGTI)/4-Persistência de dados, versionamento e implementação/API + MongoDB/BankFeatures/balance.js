import { accountsModel } from '../Schema/schemaAccount.js'

async function balanceValue(req, res) {

  const agencia = req.params.agencia;
  const conta = req.params.conta;

  // Checking if the account exists
  accountsModel.find({ agencia: agencia, conta: conta }, function (err, user) {
    if (err) {
      res.send('Account does not exists')
    }
  })

  // query details
  var query = { conta: conta, agencia: agencia }

  // checking the new account detail
  const accountDetail = await accountsModel.find(query, { _id: 0, balance: 1 })

  res.send(accountDetail[0])
}

export { balanceValue }