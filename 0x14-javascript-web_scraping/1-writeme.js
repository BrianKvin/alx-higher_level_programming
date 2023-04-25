#!/usr/bin/node
/*
 * writes a string to a file
 * the second argumnet is the string to write
 * the content of the file must be written in utf-8
 * if an error occurred during writing, print the error object
 * */
//const fs = require('fs');
//const filePath = process.argv[2];
//const writeData = process.argv[3];

//fs.writeFile(filePath, writeData, 'utf-8', (error) => {
//    if (error) {
//        console.log(error);
//    }
//});

const fs = require('fs');
const filePath = process.argv[2];
const writeData = process.argv[3];

fs.writeFile(filePath, writeData, 'utf-8', (error) => {
  if (error) { console.log(error); }
});
