// use npx nodemon helloworld.js to run the file
// node filename.js to run the file
// # bun --watch helloworld.js || npx nodemon helloworld.js and node helloworld.js

/* Data types in javascript let, var, const */
console.log("JS code executing...");
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

// Fix: Properly handle errors and correct missing closing bracket for .then()
// fetch('https://jsonplaceholder.typicode.com/posts')
//   .then(res => res.json())
//   .then(data => {
//     // Print only the title, userId, id for the first 6 posts
//     data.slice(0, 6).forEach(post => {
//       console.log(`title: ${post.title}, userId: ${post.userId}, id: ${post.id}`);
//     });
//   })
//   .catch(error => {
//     console.log('Error fetching posts:', error);
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

// orderfood(false).then((result) => {
//   console.log(result);
// }).catch((error) => {
//   console.log(error);
// }).catch((error) => {
//   console.log(error);
// })

//1. synchronous function
// console.log("starting...");

// function task1() {
//     console.log("Task 1 started");
// }
// function task2() {
//     console.log("Task 2 started");
// }
// task1();
// task2();
// console.log("ending...");

//2. asynchronous function
// console.log("starting...");

// function task1() {
//     setTimeout(() => {
//         console.log("task 1 started");}, 1000);
    
// }
// function task2() {
//     setTimeout(() => {
//         console.log("task 2 started");}, 1000);
// }

// task1();
// task2();
// console.log("ending...");

//3. callback function 
// callbackfunction example
// function fetchData(callback){
//   const data = "Data fetched via callback!";
//   callback(data);
// }
// fetchData((result) => {
//   console.log(result);
// });

// setTimeout(function() {
//   console.log("hi");
//   setTimeout(function() {
//       console.log("hello");
//   setTimeout(function() {
//       console.log("welcome");
//   }, 1000);
//   }, 3000);
// }, 5000);

//4. promise function
// function setTimeoutPromisified(ms) {
//   return new Promise(function(resolve) {
//     setTimeout(resolve, ms);
//   });
// }

// setTimeoutPromisified(1000)
//   .then(function () {
//     console.log("hi");
//     return setTimeoutPromisified(3000);
//   })
//   .then(function () {
//     console.log("hello");
//     return setTimeoutPromisified(5000);
//   })
//   .then(function () {
//     console.log("hello there");
//   });

// function run() {
// 	console.log("I will run after 1s");
// }

// setTimeout(run, 1000);
// console.log("I will run immedietely");

// function first() {
//     console.log("First");
//   }
//   function second() {
//     first();
//     console.log("Second"); setTimeout(function() {
//         console.log("Third");
//     }, 1000);
//   }
//   second();

//5. asynawait.js
// async function fetchData() {
//     return "Data fetched successfully!";
//   }
  
//   (async () => {
//     try {
//       const data = await fetchData();
//       console.log(data);
//     } catch (error) {
//         setTimeout(() => {
//             console.log("Error fetching data:", error);},1000);
//     } finally {
//         console.log("stop");
//     }
//   })();

// async function userLogin() {
//   return new Promise((resolve, reject)=>{
//     setTimeout(()=> {
//       resolve("User logged in successfully!");
//     }, 1000);
//     setTimeout(()=> {
//       reject("User logged in failed!");
//     }, 2000);
//   })
// }

// (async () => {
//   try {
//     const result = await userLogin();
//     console.log(result);
//   } catch(error) {
//     console.log("Error logging in:", error);
//   }
//   finally {
//     console.log("stop");
//   }
//   })();

// === JS Practice Topics ===
// | deep      | shallow      | loop
// | map       | filter       | reduce
// | async/await | promise    | fetching data from API
// | user login | user logout | user registration | user profile
// ==========================

// 6. Deep and Shallow copy

// Shallow copy example
const student = {
  name: "Alice",
  grades: { math: 90, science: 85 }
};

const shallowCopy = { ...student };
shallowCopy.grades.math = 100;

console.log("Shallow Copy Example:");
console.log("student.grades.math:", student.grades.math);      // Output: 100
console.log("shallowCopy.grades.math:", shallowCopy.grades.math); // Output: 100

// Deep copy example
const employee = {
  name: "Bob",
  address: { city: "New York", zip: 10001 }
};

const deepCopy = JSON.parse(JSON.stringify(employee));
deepCopy.address.city = "San Francisco";

console.log("\nDeep Copy Example:");
console.log("employee.address.city:", employee.address.city);         // Output: "New York"
console.log("deepCopy.address.city:", deepCopy.address.city);         // Output: "San Francisco"