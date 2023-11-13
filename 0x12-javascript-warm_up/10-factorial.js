#!/usr/bin/node

const { argv } = require('process');

function factorial (factor) {
  if (isNaN(factor)) {
    return 1;
  }
  if (factor === 1) {
    return factor;
  }
  return factor * factorial(factor - 1);
}
console.log(factorial(argv[2]));
