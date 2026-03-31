// asynawait.js
async function fetchData() {
    return "Data fetched successfully!";
  }
  
  (async () => {
    try {
      const data = await fetchData();
      console.log(data);
    } catch (error) {
        setTimeout(() => {
            console.log("Error fetching data:", error);},1000);
    } finally {
        console.log("stop");
    }
  })();

async function userLogin() {
  return new Promise((resolve, reject)=>{
    setTimeout(()=> {
      resolve("User logged in successfully!");
    }, 1000);
    setTimeout(()=> {
      reject("User logged in failed!");
    }, 2000);
  })
}

(async () => {
  try {
    const result = await userLogin();
    console.log(result);
  } catch(error) {
    console.log("Error logging in:", error);
  }
  finally {
    console.log("stop");
  }
  })();