#!/usr/bin/node
const request = require('request');

const api = process.argv[2];
request(api, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film in films) {
    const characters = films[film].characters;
    for (const character in characters) {
      if (characters[character].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
