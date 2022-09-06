#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);
const [file1, file2, toFile] = args;

if (!file1 || !file2 || !toFile) {
  process.exit(0);
}

const content1 = fs.readFileSync(file1).toString();
const content2 = fs.readFileSync(file2).toString();
fs.writeFileSync(toFile, content1 + content2);
