#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction && theFunction();
  }
}

module.exports = { callMeMoby };
