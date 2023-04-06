#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const result = {};
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        const todo = data[i];
        if (result[todo.userId] === undefined) {
          result[todo.userId] = 0;
        }
        result[todo.userId]++;
      }
    }
    console.log(result);
  }
});
