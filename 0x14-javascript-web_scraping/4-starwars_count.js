#!/usr/bin/node
const request = require('request');

request
  .get(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const movies = JSON.parse(body).results;
      let count = 0;
      for (const i in movies) {
        const characters = movies[i].characters;
        for (const i in characters) {
          if (characters[i].includes('18')) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
