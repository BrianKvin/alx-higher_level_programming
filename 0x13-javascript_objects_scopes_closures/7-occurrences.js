#!/usr/bin/node
//exports.nbOccurrences = function (list, searchElement) {
//	return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
// };

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.map(
    (x) => {
      if (x === searchElement) {
        count += 1;
        return 1;
      } else {
        return 0;
      }
    }
  );
  return count;
};
