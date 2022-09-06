#!/usr/bin/node
const { list = [] } = require('./100-data.js');
const newList = list.map((elem, index) => elem * index);
console.log(list);
console.log(newList);
