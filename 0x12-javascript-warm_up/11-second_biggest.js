#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3 || process.argv.length === 1) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
console.log(process.argv.length);