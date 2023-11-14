#!/usr/bin/node

exports.esrever = function (list) {
  const listLen = list.length;
  const reversedList = [];
  for (let index = listLen - 1; index >= 0; --index) {
    reversedList.push(list[index]);
  }
  return reversedList;
};
