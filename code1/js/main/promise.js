setTimeoutPromisified(1000)
  .then(function () {
    console.log("hi");
    return setTimeoutPromisified(3000);
  })
  .then(function () {
    console.log("hello");
    return setTimeoutPromisified(5000);
  })
  .then(function () {
    console.log("hello there");
  });

function run() {
	console.log("I will run after 1s");
}

setTimeout(run, 1000);
console.log("I will run immedietely");

function first() {
    console.log("First");
  }
  function second() {
    first();
    console.log("Second"); setTimeout(function() {
        console.log("Third");
    }, 1000);
  }
  second();