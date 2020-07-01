import { accountsModel } from '../Schema/schemaAccount.js'

async function transfer(req, res) {

  const contaOrigem = req.params.contaOrigem;
  const contaDestino = req.params.contaDestino;
  const valueTransfer = req.params.valueTransfer

  // Checking if the account exists (from)
  accountsModel.find({ conta: contaOrigem }, function (err, user) {
    if (err) {
      res.send('Account does not exists')
    }
  })

  // Checking if the account exists (to)
  accountsModel.find({ conta: contaDestino }, function (err, user) {
    if (err) {
      res.send('Account does not exists')
    }
  })

  // query details (account from)
  var query = { conta: contaOrigem, balance: { $gte: valueTransfer } }
  var toUpdate = { $inc: { balance: -valueTransfer } }


  // Checking if the balance > transfer (account from)
  const accountCheck = await accountsModel.find(query)
  if (accountCheck.length == 0) {
    res.send('Saldo Insuficiente, meu irmão')
  }

  // query
  await accountsModel.findOneAndUpdate(query, toUpdate)

  // query details
  var newQuery = { conta: contaDestino }
  var newToUpdate = { $inc: { balance: valueTransfer } }

  // query
  const accountDeposit = await accountsModel.findOneAndUpdate(newQuery, newToUpdate)

  // checking the new account detail
  const accountDetail = await accountsModel.find(newQuery)

  res.send(accountDetail)


}

export { transfer }