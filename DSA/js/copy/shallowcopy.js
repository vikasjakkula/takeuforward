const user = {
    name: 'Charlie',
    address: {
      city: 'Mumbai',
      country: 'India'
    }
  };
  
  const shallowCopy = { ...user };
  
  // Modifying a nested property in the copy...
  shallowCopy.address.city = 'Pune';
  
  // ...also changes it in the original object!
  console.log(user.address.city); // Output: "Pune" (oops!)
  console.log(shallowCopy.address.city); // Output: "Pune"