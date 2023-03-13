#!/usr/bin/node
/* console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]); */
 if (process.argv[2]) {
	 console.log(process.argv[2]);
 } else {
	 console.log("No argument");
 }
