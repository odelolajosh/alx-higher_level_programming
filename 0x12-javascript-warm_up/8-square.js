#!/usr/bin/node
let size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
  process.exit(0);
}

const row = new Array(size).fill('X').join('');

for (let i = 0; i < parseInt(size); i++) {
  console.log(row);
}
