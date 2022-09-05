#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  theFunction && theFunction(++number);
}

module.exports = { addMeMaybe };
