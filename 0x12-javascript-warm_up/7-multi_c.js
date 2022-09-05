#!/usr/bin/node
const occurrence = process.argv[2];
if (!occurrence || isNaN(occurrence)) {
  console.log('Missing number of occurrences');
  process.exit(0);
}
for (let i = 0; i < +occurrence; i++) {
  console.log('C is fun');
}
