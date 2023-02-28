#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  let lastIndex = list.length - 1;

  while (lastIndex >= 0) {
    reversedList.push(list[lastIndex]);
    lastIndex--;
  }

  return reversedList;
};
