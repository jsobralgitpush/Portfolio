import { accountsModel } from '../Schema/schemaAccount.js'

async function deleteAccount(req, res) {

  const agencia = req.params.agencia;
  const conta = req.params.conta;

  // Checking if the account exists
  accountsModel.find({ agencia: agencia, conta: conta }, function (err, user) {
    if (err) {
      res.send('Account does not exists')
    }
  })

  // query details
  var queryAll = { conta: conta, agencia: agencia }

  // deleting account
  const accountDetail = await accountsModel.deleteOne(queryAll)

  // checking the account numbers 
  var queryAgency = { agencia: agencia }
  const accountNumbers = await accountsModel.find(queryAgency)

  res.send({ contas: accountNumbers.length })
}

export { deleteAccount }