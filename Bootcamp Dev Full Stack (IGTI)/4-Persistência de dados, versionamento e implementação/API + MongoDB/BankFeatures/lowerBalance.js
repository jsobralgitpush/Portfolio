import { accountsModel } from '../Schema/schemaAccount.js'

async function lowerBalance(req, res) {

  const qtdClientes = req.params.qtdClientes;

  const accountNumbers = await accountsModel.find({}, { name: 0, _id: 0, __v: 0 }).sort({ balance: 1 }).limit(parseInt(qtdClientes));

  res.send(accountNumbers)
}

export { lowerBalance }