/*
ESTE SCRIPT DEVE SER RODADO UMA INVÉS SÓ, ELE INSERE TODOS OS DADOS DO ARQUIVO
'accounts.js' NA COLLECTION 'accounts'. CUIDADO!!!
*/

// inital imports
import mongoose from 'mongoose'
import { accountsModel } from '../Schema/schemaAccount.js'
import { accountsMacete as jsonFile } from './accounts.js'

// insertion
accountsModel.insertMany(jsonFile)


//mongoDB connection
mongoose.connect('mongodb+srv://admin:zezao123@cluster0.aqohu.mongodb.net/contas_banco?retryWrites=true&w=majority',
  {
    useNewUrlParser: true,
    useUnifiedTopology: true
  }).then(console.log('Conectado ao banco'))
