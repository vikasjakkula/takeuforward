//Menu-driven using arrow keys
// #include<stdio.h>
// #include<conio.h>
// #include<windows.h>

// #define BLACK 0
// #define RED 4
// #define WHITE 15

// void gotoxy(int x, int y) {
//     COORD coord;
//     coord.X = x - 1;
//     coord.Y = y - 1;
//     SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
// }

// void clrscr() {
//     system("cls");
// }

// void setcolor(int text, int bg) {
//     WORD wColor = (bg << 4) | (text & 0x0F);
//     SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), wColor);
// }

// void disp(int n)
// {
// int i=0;
// char menu[4][20]={"PRINT","1","2","EXIT"};

// clrscr();
// gotoxy(1,1);
// for(i=0;i<4;i++){

//     if(i==n){
//     setcolor(RED, WHITE);
//     gotoxy(1,i+1);
//     printf("%s\n",menu[i]);
//     setcolor(WHITE, BLACK);
//     }else{
//     gotoxy(1,i+1);
//     setcolor(WHITE, BLACK);
//     printf("%s\n",menu[i]);
//     }
//         }

// }

// int main()
// {
//  int i=2;
//  int ch;
//  disp(1);
//  gotoxy(1,i);

//  while(1)
//  {
//     ch = _getch();
//     if(ch == 0 || ch == 0xE0) {
//         ch = _getch();
//         if(ch == 80){ // Down
//         if(i<=3){
//             i=i+1;
//             disp(i-1);
//             gotoxy(1,i);
//             }else{}
//     }else if(ch == 72){ // Up
//             if(i==2){}else{
//         i=i-1;
//             disp(i-1);
//             gotoxy(1,i);
//             }
//     }else if(ch == 75){ // Left Arrow
//         break;
//     }else{
//         disp(i-1);
//         gotoxy(1,i);
//     }
//     }else if(ch==13){ // Enter
//         clrscr();
//             if(i==2){
//             printf("ONE");
//             }else if(i==3){
//             printf("TWO");
//             }else{
//             printf("Thank You");
//             _getch();
//             return 0;
//             }
//     }else{
//     disp(i-1);
//     gotoxy(1,i);
//     }
//  }

// return 0;
// }
   

#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Number of arguments: %d\n", argc);
    for (int i = 0; i < argc; i++)
        printf("Argument %d: %s\n", i, argv[i]);
    return 0;
}
