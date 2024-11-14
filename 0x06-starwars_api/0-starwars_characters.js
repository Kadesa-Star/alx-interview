#!/usr/bin/node
/**
 * Wrapper function for request object that allows it
 * to work with async and await
 * @param   {String} url - site url
 * @returns {Promise}    - promise object that resolves
 *                         with parsed JSON response
 *                         and rejects with the request error.
 */
function makeRequest(url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * Entry point - makes requests to Star Wars API
 * for movie info based on movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 * in order of appearance in the initial response.
 */
async function main() {
  const args = process.argv;

  // Ensure a movie ID is passed as a command-line argument
  if (args.length < 3) return;

  // Construct the URL for the film's data
  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

  try {
    // Fetch movie data
    const movie = await makeRequest(movieUrl);

    // Ensure characters exist in the movie data
    if (!movie.characters || movie.characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    // For each character URL, fetch and print the character's name
    for (const characterUrl of movie.characters) {
      const character = await makeRequest(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    // Handle any errors (API call or others)
    console.error(error);
  }
}

// Invoke the main function
main();
