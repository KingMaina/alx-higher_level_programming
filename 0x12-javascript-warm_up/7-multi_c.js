#!/usr/bin/node

const { argv } = require('process');

const isOccurrencesNaN = isNaN(argv[2]);
if (isOccurrencesNaN) {
  console.log('Missing number of occurrences');
} else {
  let occurrences = argv[2];
  while (occurrences > 0) {
    console.log('C is fun');
    --occurrences;
  }
}
