#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

/** if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
} */

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
