#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void handler(int sig)
{
    if (sig == SIGALRM)
        printf("Alarm is fired! (SIGALRM received)\n");
}

int main()
{
    signal(SIGALRM, handler);

    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) { 
        // Child Process
        sleep(2);  // wait before sending
        kill(getppid(), SIGALRM);
        printf("Child sent SIGALRM to parent\n");
    }
    else {
        // Parent Process
        printf("Parent waiting for SIGALRM...\n");
        pause();  // wait for signal
    }

    return 0;
}
