#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length == 0) {
	console.log(0);
}
else if (args.length == 1) {
	console.log(0);
}
else {
	const integers = args.map(arg => parseInt(arg));
	const sortedIntegers = integers.sort((a, b) => b - a);
	console.log(sortedIntegers[1]);
}
/* if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} */
