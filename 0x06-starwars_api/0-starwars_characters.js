#!/usr/bin/node
/* prints all characters of a Star Wars movie */

const request = require('request');
const util = require('util');

// Promisify the request function to use it with async/await
const requestPromise = util.promisify(request);

// Async function to fetch characters in order
async function fetchCharactersInOrder (url) {
  try {
    const response = await requestPromise(url);
    if (response.statusCode === 200) {
      const charactersUrls = JSON.parse(response.body).characters;

      // Fetch character names in sequence to maintain order
      for (const url of charactersUrls) {
        try {
          const characterResponse = await requestPromise(url);
          if (characterResponse.statusCode === 200) {
            const character = JSON.parse(characterResponse.body);
            console.log(character.name);
          } else {
            console.error(`Error fetching character: Status code ${characterResponse.statusCode}`);
          }
        } catch (error) {
          console.error('Error fetching character:', error);
        }
      }
    } else {
      console.error(`Error fetching film data: Status code ${response.statusCode}`);
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
fetchCharactersInOrder(filmUrl);
