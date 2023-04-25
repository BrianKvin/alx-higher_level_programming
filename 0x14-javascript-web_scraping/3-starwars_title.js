#!/usr/bin/node
// prints the title where the episode number matches an integer
//
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  console.log(jsonBody.title);
});
