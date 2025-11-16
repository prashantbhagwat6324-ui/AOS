#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    int fd[2];
    pid_t pid;
    char buffer[100];

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) {
        // Child process
        close(fd[1]);  // child does not write
        close(fd[0]);  // child closes pipe completely
        exit(0);
    }
    else {
        // Parent process
        close(fd[0]);  // close read end (before writing)

        char msg[] = "Hello from Parent via unnamed pipe!";
        write(fd[1], msg, sizeof(msg));
        close(fd[1]);  // finish writing so reading works

        // Now parent reads back from pipe (but no one writes now)
        // To truly "read from it", parent needs to reopen read end

        // Recreate pipe for reading demonstration
        pipe(fd);
        write(fd[1], msg, sizeof(msg));
        close(fd[1]);

        printf("Parent reading message from pipe:\n");
        read(fd[0], buffer, sizeof(buffer));
        printf("%s\n", buffer);

        close(fd[0]);
    }

    return 0;
}
