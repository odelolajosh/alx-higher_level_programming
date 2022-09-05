#!/usr/bin/node
const args = process.argv.slice(2);
const [first] = args;
if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
