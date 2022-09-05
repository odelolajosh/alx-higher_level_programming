#!/usr/bin/node

const argv = process.argv.slice(2);
const numbersInArgv = argv.filter(arg => !isNaN(arg));
const args = numbersInArgv.map(arg => parseInt(arg));
let biggest = 0;

if (args.length > 1) {
  biggest = Math.max(...args);
  const index = args.indexOf(biggest);
  args.splice(index);
  biggest = Math.max(...args);
}

console.log(biggest);
