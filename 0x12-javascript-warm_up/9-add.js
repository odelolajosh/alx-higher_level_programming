#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const [a, b] = process.argv.slice(2);
console.log(add(+a, +b));
