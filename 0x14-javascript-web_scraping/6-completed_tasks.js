#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const items = JSON.parse(body);
  const result = items.reduce((acc, item) => {
    if (item.completed) {
      if (acc[item.userId]) {
        acc[item.userId] += 1;
      } else {
        acc[item.userId] = 1;
      }
    }
    return acc;
  }, {});
  console.log(result);
});
