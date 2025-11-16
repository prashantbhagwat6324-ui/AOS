#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void sighup()
{
    printf("Child: I have received SIGHUP\n");
}

void sigint()
{
    printf("Child: I have received SIGINT\n");
}

void sigquit()
{
    printf("My Papa has Killed me!!!\n");
    exit(0);
}

int main()
{
    pid_t pid;

    pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) {
        // Child process
        signal(SIGHUP, sighup);
        signal(SIGINT, sigint);
        signal(SIGQUIT, sigquit);

        while (1)
            ;   // Wait for signals
    }
    else {
        // Parent process
        sleep(3);
        for (int i = 0; i < 5; i++) {
            printf("Parent sending SIGHUP to child\n");
            kill(pid, SIGHUP);
            sleep(3);

            printf("Parent sending SIGINT to child\n");
            kill(pid, SIGINT);
            sleep(3);
        }

        printf("Parent sending SIGQUIT to child\n");
        kill(pid, SIGQUIT);
    }

    return 0;
}
