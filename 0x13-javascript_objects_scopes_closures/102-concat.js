#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

const fileAname = argv[2];
const fileBname = argv[3];
const fileCname = argv[4];
const ENCODING = 'utf8';

let result = '';
if (fileAname) {
  try {
    result += fs.readFileSync(fileAname, ENCODING);
  } catch (error) {
    console.error(error);
  }
}
if (fileBname) {
  try {
    result += fs.readFileSync(fileBname, ENCODING);
  } catch (error) {
    console.error(error);
  }
}
if (fileCname) {
  try {
    fs.writeFileSync(fileCname, result);
  } catch (error) {
    console.error(error);
  }
}
