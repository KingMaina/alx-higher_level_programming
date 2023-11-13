#!/usr/bin/node

const { argv } = require('process');

const isNotANumber = isNaN(argv[2]);

if (isNotANumber) {
  console.log('Not a number');
} else {
  console.log('My number:', Number(argv[2]));
}
