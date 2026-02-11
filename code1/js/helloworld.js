// use npx nodemon fileName to run the file
// node filename.js to run the file
/* Data types in javascript let, var, const */
console.log("helloworld");
/*
  deep copy 
  shallow copy
  loop map books.map
  async await
  promise 
  async function
  fetching data from api
*/

// Day 1
// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// rl.question('What is your name? ', (name) => {
//   console.log(`Hello, ${name}!`);
//   rl.close();
// });
// fetch("https://jsonplaceholder.typicode.com/posts")


// fetch('https://jsonplaceholder.typicode.com/posts')
//   .then(res => res.json())
//   .then(data => {
//     console.log(data);
//   });

// let result;
// setTimeout(function() {
//   result = 5;
// }, 1000);

// let myPromise = new Promise(function(resolve, reject){
//   ok = true;
//   if(ok) {
//     resolve(ok);
//   }
//   else {
//     reject(d);
//   }
// });
// console.log(myPromise);

// function delay(ms) {
//   return new Promise(resolve => setTimeout(resolve, ms));
// }

// async function run() {
//   await delay(1000);
//   console.log("hello");

//   await delay(1000);
//   console.log("hellooo");

//   await delay(5000);
//   console.log("helloo");
// }

// run();

// function orderfood(paymentSuccess){
//   return new Promise((resolve, reject) => {
//     if(paymentSuccess) {
//       resolve("food delivered");
//      } else {
//       reject("no food is coming to your home");
//      }
//   });
// }

// orderfood(true)
//   .then(result => console.log(result))
//   .catch(error => console.log(error));