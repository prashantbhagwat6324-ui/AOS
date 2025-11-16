#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    pid_t pid;
    int status;

    pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) {
        // Child process
        printf("Child process running...\n");
        exit(5);    // Child exits with status 5
    }
    else {
        // Parent waits
        wait(&status);

        if (WIFEXITED(status)) {
            printf("Child exited normally.\n");
            printf("Exit status = %d\n", WEXITSTATUS(status));
        } else {
            printf("Child terminated abnormally.\n");
        }
    }

    return 0;
}
