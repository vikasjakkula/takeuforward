// #include <stdio.h>
// #include<limits.h>
// int main() {
//     int max, secondmax, i;
//     int arr[5] = {1, 2 , 3, 4, 5};
//     max= INT_MIN;
//     for(int i=0; i<5; i++) {
//         if(arr[i]>max)
//         max=arr[i];
//     }
//     secondmax=INT_MIN;
//      for(int i=0; i<5; i++){
//             if(arr[i]>secondmax && arr[i]!=max){
//             secondmax=arr[i];
//             }
//         }
    
//     printf("Max of arr: %d", max);
//     printf("Second max of arr: %d", secondmax);

//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>
// bool isPrime(int a){
//     for(int i=2; i<a; i++){
//         if(a%i==0)
//         return false;
//     }
//     return true;
// }
// bool isOdd(int a){
//     return a%2;
// }
// bool isEven(int a){
//     return !a%2;
// }

// void main(){
//     int evensum=0, oddsum=0;
//     int arr[5] = { 1, 2, 3, 4, 5};
//     for(int i=0; i<5; i++) {
//         if(isPrime(arr[i]))
//         printf("%d", arr[i]);

//         if(isOdd(arr[i])){
//         oddsum+= arr[i];
//         }

//         else{
//         evensum+=arr[i];
//     }}
//     printf("%d", oddsum);
//     printf("%d", evensum);
// }