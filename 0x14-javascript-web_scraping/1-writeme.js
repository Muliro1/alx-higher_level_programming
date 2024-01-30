#!/usr/bin/node
// Writes a string to a file

const fls = require('fs');
const argv = process.argv;
const filePath = argv[2];
const string = argv[3];

fls.writeFile(filePath, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
