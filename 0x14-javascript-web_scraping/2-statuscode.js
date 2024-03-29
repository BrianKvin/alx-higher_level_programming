#!/usr/bin/node
// Displays the status of a GET request
//const request = require('request');
//const url = process.argv[2];

//request.get(url).on('response', function (response) => {
//	console.log(`code: ${response.statusCode}`);
//});

const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
