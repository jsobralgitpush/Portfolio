function maisMenos(array) {
  var count_pos = 0;
  var count_zero = 0;
  var count_neg = 0;
  var list_resultado = [];

  for (let i = 0; i < array.length; i++) {
    if (array[i] > 0) {
      count_pos += 1;
    } else if (array[i] === 0) {
      count_zero += 1;
    } else if (array[i] < 0) {
      count_neg += 1;
    }
  }

  list_resultado.push(count_pos / array.length);
  list_resultado.push(count_zero / array.length);
  list_resultado.push(count_neg / array.length);

  return list_resultado;
}
