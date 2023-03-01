#!/usr/bin/node
const fs = require('fs');

const argv = process.argv;
const fileA = fs.readFileSync(argv[2]);
const fileB = fs.readFileSync(argv[3]);

fs.writeFile(argv[4], fileA + fileB, 'utf8', err => {
  if (err) throw err;
});
