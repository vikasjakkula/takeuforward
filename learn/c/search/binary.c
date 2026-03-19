#include <stdio.h>
#define MAX 100

int main() {
    int arr[MAX], n, search, found = 0, first, last, middle;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter the %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the key to search: ");
    scanf("%d", &search);

    first=0;
    last=n-1;

    if(arr[middle]<search) {
        first=middle+1;
    }
    else if(arr[middle]>search) {
        last=middle-1;
    }
    else {
        printf("Element found at position %d\n", middle + 1);
        found = 1;
        break;
    }
    if (found == 0) {
        printf("Not found! %d isn't present in the list.\n", search);
    }

    return 0;
}