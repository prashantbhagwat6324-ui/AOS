#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <fcntl.h>

int main()
{
    int fd[2];
    pipe(fd);

    // Block Ctrl-C (SIGINT) and Ctrl-\ (SIGQUIT)
    signal(SIGINT, SIG_IGN);
    signal(SIGQUIT, SIG_IGN);

    pid_t pid1 = fork();

    if (pid1 == 0) {
        // Child 1 → executes "ls -l"
        close(fd[0]);               // close read end
        dup2(fd[1], STDOUT_FILENO); // write output into pipe
        close(fd[1]);

        execl("/bin/ls", "ls", "-l", NULL);
        perror("execl ls");
        exit(1);
    }

    pid_t pid2 = fork();

    if (pid2 == 0) {
        // Child 2 → executes "wc -l"
        close(fd[1]);               // close write end
        dup2(fd[0], STDIN_FILENO);  // read from pipe
        close(fd[0]);

        execl("/usr/bin/wc", "wc", "-l", NULL);
        perror("execl wc");
        exit(1);
    }

    // Parent closes both ends
    close(fd[0]);
    close(fd[1]);

    // Wait for both children
    wait(NULL);
    wait(NULL);

    return 0;
}
