import { accountsModel } from '../Schema/schemaAccount.js'

async function average(req, res) {

  const agencia = req.params.agencia

  // Checking if the account exists
  accountsModel.find({ agencia: agencia }, function (err, user) {
    if (err) {
      res.send('Account does not exists')
    }
  })

  // query details
  var filterToApply = { agencia: agencia }

  // query with filter
  const accountDetail = await accountsModel.find(filterToApply)

  // Getting the group to aggregate
  var groupQuery = [
    {
      $group:
      {
        _id: "$agencia",
        avg: { $avg: "$balance" }
      }
    }
  ]

  // Getting the avg
  const showAvg = await accountsModel.aggregate(groupQuery)

  res.send(showAvg)
}

export { average }