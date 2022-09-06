#!/usr/bin/node

/**
 * reversed version of a list
 */
exports.esrever = function (list) {
  let left = 0; let right = list.length - 1;
  for (; left < right; left++, right--) {
    const temp = list[left];
    list[left] = list[right];
    list[right] = temp;
  }
  return list;
};
