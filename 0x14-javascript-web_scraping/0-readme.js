#!/usr/bin/node
/*
 * A script that reads and prints the content of a file
 * the content must be read in utf-8
 * if an error occure, print the error object
 **/
const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (error, data) => {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});
