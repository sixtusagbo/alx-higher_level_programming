#!/usr/bin/node
const factor = require('./100-data').list;
const mapped = factor.map((element, index) => element * index);
console.log(factor);
console.log(mapped);
