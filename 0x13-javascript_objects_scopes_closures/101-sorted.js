#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = {};

for (const [nbOccurrences, userId] of Object.entries(dict)) {
  if (!newDict[userId]) {
    newDict[userId] = [nbOccurrences];
  } else {
    newDict[userId].push(nbOccurrences);
  }
}
console.log(newDict);
