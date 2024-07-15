#!/usr/bin/node
/* Prints all the characters of Star Wars movie.*/


const request = require('request');
const starWarsAPI = 'https://swapi-api.alx-tools.com/api/';
const endPoint = 'films/';
const movieID = process.argv[2].toString();

request(starWarsAPI + endPoint + movieID, function (error, _, body) {
  if (error) console.error(error);
  const objects = JSON.parse(body);
  const cast = objects.characters;
  Printresult(cast);
});


function Printresult (cast, counter = 0) {
  request(cast[counter], function (error, _, body) {
    if (error) console.error(error);
    console.log(JSON.parse(body).name);
    if (++counter < cast.length) {
      Printresult(cast, counter++);
    }
  });
}
