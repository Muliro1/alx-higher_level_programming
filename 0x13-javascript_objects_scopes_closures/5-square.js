#!/usr/bin/node
export default class Square extends require('./4-rectangle.js').default {
  constructor (size) {
    super(size, size);
  }
};
