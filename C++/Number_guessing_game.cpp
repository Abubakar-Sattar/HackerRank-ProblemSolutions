#include <iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
using namespace std;


void printfunc(int tries)
{



printf("\n\nFinally, you have guessed the number ");
if (tries <=2)
{
printf("you have tried %d time " ,tries);
printf("\nWell done");
}
else if (tries >2 and tries<=6)
{
printf("you have tried %d times" ,tries);
printf("\nGood");
}
else
{
printf("you have tried %d times" ,tries);
printf("\nNot bad");
}
}

int main() {
int random_number,i,guessed_number,tries = 0,arr[10];

srand(time(0));

random_number=(rand()%10)+1;


printf("Guess the number between 1 and 10: ");
scanf("%d",&guessed_number);
arr[tries] = guessed_number;
tries ++;
while (random_number != guessed_number)
{
printf("you have guessed the wrong number please try again: ");
scanf("%d",&guessed_number);
arr[tries] = guessed_number;
tries ++;
}

printfunc(tries);

return 0;
}