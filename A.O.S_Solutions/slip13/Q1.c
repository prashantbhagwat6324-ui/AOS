#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

int main()
{
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) {
        // Child process
        while (1) {
            printf("Child running...\n");
            sleep(1);
        }
    }
    else {
        // Parent process
        sleep(3);

        printf("Parent: Sending SIGSTOP to suspend child\n");
        kill(pid, SIGSTOP);

        sleep(3);

        printf("Parent: Sending SIGCONT to resume child\n");
        kill(pid, SIGCONT);

        sleep(3);

        printf("Parent: Sending SIGKILL to terminate child\n");
        kill(pid, SIGKILL);
    }

    return 0;
}
