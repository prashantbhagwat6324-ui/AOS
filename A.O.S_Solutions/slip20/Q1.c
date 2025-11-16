#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

int main()
{
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) {
        // Child Process
        while (1) {
            printf("Child is running...\n");
            sleep(1);
        }
    }
    else {
        // Parent Process
        sleep(3);  
        printf("Parent: Sending SIGSTOP (suspend child)\n");
        kill(pid, SIGSTOP);   // suspend child

        sleep(3);
        printf("Parent: Sending SIGCONT (resume child)\n");
        kill(pid, SIGCONT);   // resume child

        sleep(3);
        printf("Parent: Sending SIGKILL (terminate child)\n");
        kill(pid, SIGKILL);   // kill child

        wait(NULL);
    }

    return 0;
}
