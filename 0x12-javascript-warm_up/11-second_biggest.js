#!/usr/bin/node

const { argv } = require('process');

const integers = Object.values(argv).splice(2);

if (integers.length <= 1) {
  console.log(0);
} else {
  const numbers = integers.map((integer) => {
    return Number(integer);
  });
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
