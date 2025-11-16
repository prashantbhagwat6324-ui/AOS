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

    // Redirect STDOUT to file
    dup2(fd, STDOUT_FILENO);

    printf("This text goes into output.txt\n");
    printf("Standard output successfully redirected!\n");

    close(fd);
    return 0;
}
