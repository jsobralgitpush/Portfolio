import { accountsModel } from '../Schema/schemaAccount.js'

async function deposit(req, res) {

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
  var query = { conta: conta, agencia: agencia }
  var toUpdate = { $inc: { balance: value } }

  // query
  const accountDeposit = await accountsModel.findOneAndUpdate(query, toUpdate)

  // checking the new account detail
  const accountDetail = await accountsModel.find(query)

  res.send(accountDetail)
}

export { deposit }