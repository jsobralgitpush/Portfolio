//initial imports
import express from 'express'
import mongoose from 'mongoose'

// Routes function imports
import { deposit } from './BankFeatures/deposit.js'
import { withdraw } from './BankFeatures/withdraw.js'
import { balanceValue } from './BankFeatures/balance.js'
import { deleteAccount } from './BankFeatures/delete.js'
import { average } from './BankFeatures/average.js'
import { lowerBalance } from './BankFeatures/lowerBalance.js'
import { higherBalance } from './BankFeatures/higherBalance.js'
import { transfer } from './BankFeatures/transfer.js'
import { privateAccount } from './BankFeatures/privateAccount.js'


//initial configs
const port = 8080
const app = express()
app.use(express.json());

// Calling routes
app.get('/teste', (req, res) => {
  res.send('working :)')
})

// Rota para depósito
app.post('/deposit/:agencia/:conta/:value', async (req, res) => {
  deposit(req, res)
})

// Rota para saque
app.post('/withdraw/:agencia/:conta/:value', async (req, res) => {
  withdraw(req, res)
})

// Rota para saldo
app.get('/balance/:agencia/:conta', async (req, res) => {
  balanceValue(req, res)
})

// Rota para excluir a conta
app.post('/delete/:agencia/:conta', async (req, res) => {
  deleteAccount(req, res)
})

// Rota consulta média
app.get('/media/:agencia', async (req, res) => {
  average(req, res)
})

// Rota clientes com menor saldo
app.get('/menorsaldo/:qtdClientes', async (req, res) => {
  lowerBalance(req, res)
})

// Rota clientes com maior saldo
app.get('/maiorsaldo/:qtdClientes', async (req, res) => {
  higherBalance(req, res)
})

// Rota transferência de saldo
app.post('/transferencia/:contaOrigem/:contaDestino/:valueTransfer', async (req, res) => {
  transfer(req, res)
})

// Rota clientes private
app.post('/private', async (req, res) => {
  privateAccount(req, res)
})


//mongoDB connection
mongoose.connect('mongodb+srv://admin:zezao123@cluster0.aqohu.mongodb.net/contas_banco?retryWrites=true&w=majority',
  {
    useNewUrlParser: true,
    useUnifiedTopology: true
  }).then(console.log('Conectado ao banco'))


//turning on the API
app.listen(port, () => console.log('Conectado'))