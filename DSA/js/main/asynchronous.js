console.log("starting...");

function task1() {
    setTimeout(() => {
        console.log("task 1 started");}, 1000);
    
}
function task2() {
    console.log("task 2 started");
}

task1();
task2();
console.log("end");