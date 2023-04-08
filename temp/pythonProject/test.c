#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {
    char userInput[50];
    int isInt = 1;

    printf("Enter a value: ");
    scanf("%s", userInput);

    printf("%s\n", userInput);
}