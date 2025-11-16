#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

pid_t child_pid;

void alarm_handler(int sig)
{
    printf("Child did not finish within 5 seconds… Killing child!\n");
    kill(child_pid, SIGKILL);
}

void child_exit_handler(int sig)
{
    printf("Child process terminated.\n");
}

int main()
{
    signal(SIGCHLD, child_exit_handler);
    signal(SIGALRM, alarm_handler);

    child_pid = fork();

    if (child_pid < 0) {
        perror("fork");
        exit(1);
    }

    if (child_pid == 0) {
        // Child process executes command
        execl("/bin/sleep", "sleep", "10", NULL);

        // If exec fails
        perror("execl");
        exit(1);
    }
    else {
        // Parent Process
        printf("Parent started. Child PID = %d\n", child_pid);

        alarm(5);  // Set 5 second timer

        // Wait for child (but alarm may interrupt)
        wait(NULL);
    }

    return 0;
}
