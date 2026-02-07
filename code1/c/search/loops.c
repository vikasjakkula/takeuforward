// // prime number in a range
// #include <stdio.h>
// void isPrime(int n) {
//     if(n<=1) {
//         printf("Not a prime number");
//     }
//     for(int i=2; i*i<=n; i++) {
//         if(n%i==0) {
//             printf("Not a prime number");
//         }
//     }
//     printf("Prime number");
// }
// int main() {
//     int n;
//     printf("Enter the number: ");
//     scanf("%d", &n);
//     isPrime(n);
//     return 0;
// }

// // lcm
// #include <stdio.h>
// int main() {
//     int a, b;
//     printf("Enter the two numbers: ");
//     scanf("%d %d", &a, &b);
//     int lcm = (a>b)?a:b;
//     while(1) {
//         if(lcm%a==0 && lcm%b==0) {
//             printf("The LCM of %d and %d is %d", a, b, lcm);
//             break;
//         }
//         lcm++;
//     }
//     printf("The LCM of %d and %d is %d", a, b, lcm);
//     return 0;
// }
// // gcd
// #include <stdio.h>
// void gcd(int a, int b) {
//     if(b==0) {
//         return a;
//     }
//     else {
//         return gcd(b, a%b);
//     }
// }
// int main() {
//     int a, b;
//     printf("Enter the two numbers: ");
//     scanf("%d %d", &a, &b);
//     gcd(a, b);
//     return 0;
// }