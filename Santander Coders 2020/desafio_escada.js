function escada(num) {
  var list_resultado = [];

  for (let i = 1; i < num + 1; i++) {
    list_resultado.push(' '.repeat(num - i) + '#'.repeat(i));
  }

  return list_resultado;
}
