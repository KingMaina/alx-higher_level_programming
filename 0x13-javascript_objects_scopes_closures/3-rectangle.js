#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shape = '';
    for (let row = 0; row < this.height; ++row) {
      for (let column = 0; column < this.width; ++column) {
        shape += 'X';
      }
      if (row !== this.height - 1) shape += '\n';
    }
    if (shape.length > 0) console.log(shape);
  }
}

module.exports = Rectangle;
