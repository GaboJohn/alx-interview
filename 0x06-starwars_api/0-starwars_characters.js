#!/usr/bin/node

const request = require('request');

const fetchJson = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const getCharacterNames = async (urls) => {
  const characterPromises = urls.map(url => fetchJson(url));
  const characters = await Promise.all(characterPromises);
  return characters.map(character => character.name);
};

const printMovieCharacters = async (movieId) => {
  try {
    const film = await fetchJson(`https://swapi-api.hbtn.io/api/films/${movieId}/`);
    const characterNames = await getCharacterNames(film.characters);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error);
  }
};

const movieId = process.argv[2];
if (movieId) {
  printMovieCharacters(movieId);
} else {
  console.error('Please provide a Movie ID');
}
