function fatorial(num) {
  var counter = 1;

  for (let i = 1; i < num + 1; i++) {
    counter = counter * i;
  }

  return counter;
}
