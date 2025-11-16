#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

pid_t child_pid;

void child_handler(int sig)
{
    printf("Child process has terminated.\n");
}

void alarm_handler(int sig)
{
    printf("Child did not finish in 5 seconds... Killing child!\n");
    kill(child_pid, SIGKILL);
}

int main()
{
    signal(SIGCHLD, child_handler);
    signal(SIGALRM, alarm_handler);

    child_pid = fork();

    if (child_pid < 0) {
        perror("fork");
        exit(1);
    }

    if (child_pid == 0) {
        // Child – Run a command (example: sleep 10)
        execl("/bin/sleep", "sleep", "10", NULL);
        perror("execl");
        exit(1);
    }
    else {
        // Parent
        printf("Parent: Child PID = %d\n", child_pid);
        alarm(5);  // 5-second timer

        wait(NULL);   // Wait for child (may be interrupted by alarm)
    }

    return 0;
}
