// Sample code for demonstating deep copy

let original = {
    name: "John",
    age: 30,
    Native: {
        Hyd: undefined,
        malkajgiri: undefined,
        telangana: undefined,
    },
    education: undefined,
}
let copy = original;
copy.name = "Jane";
copy.Native.Hyd = "Hyderabad";
copy.Native.malkajgiri = "Malkajgiri";
copy.Native.telangana = "Telangana";
copy.education = "b.tech";
console.log(original);
console.log(copy);