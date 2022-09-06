#!/usr/bin/node

/**
 * returns the number of occurrences in a list
 * @param {any[]} list array to search from
 * @param {any} searchElement element to search for
 * @returns occurrence
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      count++;
    }
  }
  return count;
};
