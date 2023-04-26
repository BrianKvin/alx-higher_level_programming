#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) { console.log(err); }

  const completed = {};
  const jsonBody = JSON.parse(body);
  for (const task of jsonBody) {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});

//const request = require('request');
//request(process.argv[2], function (error, response, body) {
//  if (!error) {
//    const todos = JSON.parse(body);
//    const completed = {};
//    todos.forEach((todo) => {
//      if (todo.completed && completed[todo.userId] === undefined) {
//        completed[todo.userId] = 1;
//      } else if (todo.completed) {
//        completed[todo.userId] += 1;
//      }
//    });
//   console.log(completed);
//  }
//});
