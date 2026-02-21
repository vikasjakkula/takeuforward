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

/*
// PROGRAM 1: BINARY SEARCH
#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int n = 10, target, left = 0, right = n - 1, mid, found = 0;

    printf("Enter number to search: ");
    scanf("%d", &target);

    while (left <= right) {
        mid = (left + right) / 2;
        if (arr[mid] == target) {
            printf("Found at index %d\n", mid);
            found = 1;
            break;
        }
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    if (!found) printf("Not found\n");
    return 0;
}
*/

/*
// PROGRAM 2: SELECTION SORT
#include <stdio.h>

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = 5, i, j, min_idx, temp;

    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }

    printf("Sorted Array: ");
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}

*/
/*
// PROGRAM 3: BUBBLE SORT
#include <stdio.h>

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = 7, i, j, temp;

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    printf("Sorted Array: ");
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
*/

// 3. Quadratic Equation Roots
// #include <stdio.h>
// #include <math.h>

// int main() {
//     float a, b, c, discriminant, root1, root2;
//     printf("Enter coefficients a, b, c: ");
//     scanf("%f %f %f", &a, &b, &c);

//     discriminant = b*b - 4*a*c;

//     if (discriminant > 0) {
//         root1 = (-b + sqrt(discriminant)) / (2*a);
//         root2 = (-b - sqrt(discriminant)) / (2*a);
//         printf("Real and distinct roots: %.2f and %.2f\n", root1, root2);
//     }
//     else if (discriminant == 0) {
//         root1 = -b / (2*a);
//         printf("Real and equal roots: %.2f and %.2f\n", root1, root1);
//     }
//     else {
//         float realPart = -b / (2*a);
//         float imagPart = sqrt(-discriminant) / (2*a);
//         printf("Complex roots: %.2f + %.2fi and %.2f - %.2fi\n",
//                realPart, imagPart, realPart, imagPart);
//     }

//     return 0;
// }
