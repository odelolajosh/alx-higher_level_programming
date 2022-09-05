#!/usr/bin/node
const args = process.argv.slice(2);
const [first] = args;
if (isNaN(first)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(first));
}
