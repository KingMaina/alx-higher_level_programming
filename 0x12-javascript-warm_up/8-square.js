#!/usr/bin/node

const { argv } = require('process');

const size = argv[2];
const isSizeNaN = isNaN(size);

if (isSizeNaN) {
  console.log('Missing size');
} else {
  let square = '';
  for (let row = 0; row < size; row++) {
    for (let column = 0; column < size; column++) {
      square += 'X';
    }
    if (row !== size - 1) {
      square += '\n';
    }
  }
  if (size > 0) {
    console.log(square);
  }
}
