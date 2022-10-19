#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function getCharacterByFilm (url) {
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }
    body = JSON.parse(body);
    const characters = body.results;
    characters.forEach(function (character) {
      if (character.films.includes(filmUrl)) {
        console.log(character.name);
      }
    });
    if (body.next) {
      getCharacterByFilm(body.next);
    }
  });
}

getCharacterByFilm('https://swapi-api.hbtn.io/api/people/');
