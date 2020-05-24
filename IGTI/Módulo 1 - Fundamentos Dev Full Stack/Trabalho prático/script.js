window.addEventListener('load', start);

var input_one = document.querySelector('#bt-range-one');
var input_two = document.querySelector('#bt-range-two');
var input_three = document.querySelector('#bt-range-three');

var cx_selecao_one = document.querySelector('#cx-selecao-one');
var cx_selecao_two = document.querySelector('#cx-selecao-two');
var cx_selecao_three = document.querySelector('#cx-selecao-three');

var square = document.querySelector('.square');

function start() {
  input_one.addEventListener('click', countRange);
  input_two.addEventListener('click', countRange);
  input_three.addEventListener('click', countRange);
}

function countRange() {
  const valor_one = input_one.value;
  const valor_two = input_two.value;
  const valor_three = input_three.value;

  square.style.backgroundColor =
    'rgb(' + valor_one + ',' + valor_two + ',' + valor_three + ')';

  cx_selecao_one.value = valor_one;
  cx_selecao_two.value = valor_two;
  cx_selecao_three.value = valor_three;
}
