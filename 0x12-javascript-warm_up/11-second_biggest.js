#!/usr/bin/node

const args = process.argv.slice(2);
let biggest = 0;

if (args.length > 1) {
  biggest = Math.max(...args);
  const index = args.indexOf(biggest + '');
  args.splice(index);
  biggest = Math.max(...args);
}

console.log(biggest);
