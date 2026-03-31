#include <stdio.h>
#define MAX 100

int main() {
    int arr[MAX], n, key, found = 0;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    if(n <= 0 || n > MAX) {
        printf("Invalid number of elements\n");
        return 1;
    }

    printf("Enter the elements:\n");
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the key to search: ");
    scanf("%d", &key);

    for(int i = 0; i < n; i++) {
        if(arr[i] == key) {
            printf("Element found at position %d\n", i+1);
            found = 1;
            break;
        }
    }

    if(!found) {
        printf("Element not found in the array\n");
    }

    return 0;
}