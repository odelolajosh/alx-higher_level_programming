#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  /**
   * prints the rectangle using the character c
  */
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
