// callbackfunction example
function fetchData(callback){
    const data = "Data fetched via callback!";
    callback(data);
}
fetchData((result) => {
    console.log(result);
});

setTimeout(function() {
    console.log("hi");
    setTimeout(function() {
        console.log("hello");
    setTimeout(function() {
        console.log("welcome");
    }, 1000);
    }, 3000);
}, 5000);