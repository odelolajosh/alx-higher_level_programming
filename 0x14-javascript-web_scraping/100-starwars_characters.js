#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(function (character) {
    request(character, function (err, response, body) {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
