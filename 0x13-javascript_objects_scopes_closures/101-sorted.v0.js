#!/usr/bin/node
const { dict = {} } = require('./101-data.js');
const newDict = {};
const values = new Set(Object.values(dict));
const keys = Object.keys(dict)
values.forEach((value) => {
  newDict[value + ''] = keys.filter((key) => dict[key] === value);
})
console.log(newDict)