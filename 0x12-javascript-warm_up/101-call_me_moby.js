#!/usr/bin/node
exports.callMeMoby = (x, aFunction) => {
  for (let i = 0; i < x; i++) {
    aFunction();
  }
};
