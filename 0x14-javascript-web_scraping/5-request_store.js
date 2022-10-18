#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const [url, file] = process.argv.slice(2);
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  try {
    fs.writeFileSync(file, body);
  } catch (err) {
    console.log(err);
  }
});
