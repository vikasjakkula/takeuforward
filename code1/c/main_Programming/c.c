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

// kth max of an array
// #include <stdio.h>

// void sortDescending(int arr[], int n) {
//     for (int i = 0; i < n-1; i++) {
//         for (int j = i+1; j < n; j++) {
//             if (arr[i] < arr[j]) {
//                 int temp = arr[i];
//                 arr[i] = arr[j];
//                 arr[j] = temp;
//             }
//         }
//     }
// }

// int main() {
//     int k;
//     printf("Enter kth max index: ");
//     scanf("%d", &k);

//     int arr[5] = {1, 2, 3, 4, 5};
//     int n = 5;

//     if(k < 1 || k > n) {
//         printf("Invalid value for k. Must be between 1 and %d.\n", n);
//         return 1;
//     }

//     sortDescending(arr, n);

//     printf("%dth max of the array is: %d\n", k, arr[k-1]);

//     return 0;
// }