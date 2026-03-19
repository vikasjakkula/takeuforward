// pointers main syntax and how to use
// void pointer
// pointer to pointer
// pointer to function
// pointer to array
// pointer to structure
// pointers in c
// pointer operations addition, subtraction, increment, decrement, comparison of 2 pointers

#include <stdio.h>
int main() {
    int a = 10, *ptr;
    ptr = &a;

    printf("Address in ptr = %p\n", ptr); 
    printf("Value at ptr = %d\n", *ptr);
    printf("Value of a = %d\n", a);
    printf("Address of a = %p\n", &a);
    return 0;
}