#!/usr/bin/node
import('fs');

/**
 * script that concats 2 files.
 * The first argument is the file path of the first source file.
 * The second argument is the file path of the second source file.
 * The third argument is the file path of the destination.

const fs = import('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const dataA = fs.readFileSync(fileA, { encoding: 'utf8' });
const dataB = fs.readFileSync(fileB, { encoding: 'utf8' });
fs.writeFileSync(fileC, dataA + dataB, { encoding: 'utf8' });
*/

const fs = require('fs');

const concatFiles = (sourceFilePath1, sourceFilePath2, destinationFilePath) => {
  try {
    const fileContent1 = fs.readFileSync(sourceFilePath1, 'utf-8');
    const fileContent2 = fs.readFileSync(sourceFilePath2, 'utf-8');
    const concatenatedContent = fileContent1 + fileContent2;
    fs.writeFileSync(destinationFilePath, concatenatedContent);
    // console.log('Files concatenated successfully!');
  } catch (error) {
    console.error('Error concatenating files:', error);
  }
};

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

concatFiles(fileA, fileB, fileC);
