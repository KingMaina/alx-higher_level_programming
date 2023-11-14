#!/usr/bin/node

const mySquare = require('./5-square');

class Square extends mySquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let shape = '';
    for (let row = 0; row < this.size; ++row) {
      for (let column = 0; column < this.size; ++column) {
        if (c !== undefined) {
          shape += c;
        } else {
          shape += 'X';
        }
      }
      if (row !== this.size - 1) shape += '\n';
    }
    if (shape.length > 0) console.log(shape);
  }
}

module.exports = Square;
