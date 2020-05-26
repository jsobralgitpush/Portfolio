function produto(array) {
  var counter = 1;

  for (let i = 0; i < array.length; i++) {
    counter = array[i] * counter;
  }

  return counter;
}
