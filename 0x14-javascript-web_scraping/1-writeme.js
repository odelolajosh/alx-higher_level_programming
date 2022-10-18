#!/usr/bin/node
const fs = require('fs');

const [file, content] = process.argv.slice(2);
try {
  fs.writeFileSync(file, content, 'utf8');
} catch (err) {
  console.error(err);
}
