#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
  process.exit(0);
}

let s = '';
for (let i = 0; i < size; i++) {
  s += 'X';
}

for (let i = 0; i < size; i++) {
  console.log(s);
}
