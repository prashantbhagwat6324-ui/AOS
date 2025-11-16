#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

int count = 0;

void handler(int sig)
{
    count++;
    if (count == 1) {
        printf("\nCtrl-C pressed! Press Ctrl-C again to exit.\n");
    } else {
        printf("\nExiting program...\n");
        exit(0);
    }
}

int main()
{
    signal(SIGINT, handler);

    printf("Program running... Press Ctrl-C\n");

    while (1) {
        // infinite loop
    }

    return 0;
}
