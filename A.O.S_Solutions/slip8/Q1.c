#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main()
{
    int fd = open("output.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);

    if (fd < 0) {
        perror("open");
        exit(1);
    }

    // Duplicate fd to STDOUT
    dup2(fd, STDOUT_FILENO);

    printf("This output is redirected to output.txt\n");
    printf("Redirection done using dup and open system calls.\n");

    close(fd);
    return 0;
}
