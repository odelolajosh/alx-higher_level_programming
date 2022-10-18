#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];
try {
  const content = fs.readFileSync(file, 'utf8');
  console.log(content);
} catch (err) {
  console.error(err);
}
