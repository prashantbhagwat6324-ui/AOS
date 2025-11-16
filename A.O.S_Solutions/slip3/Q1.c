#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>

void printType(mode_t mode)
{
    if (S_ISREG(mode))
        printf("Regular File\n");
    else if (S_ISDIR(mode))
        printf("Directory\n");
    else if (S_ISCHR(mode))
        printf("Character Device\n");
    else if (S_ISBLK(mode))
        printf("Block Device\n");
    else if (S_ISFIFO(mode))
        printf("FIFO / Pipe\n");
    else if (S_ISLNK(mode))
        printf("Symbolic Link\n");
    else if (S_ISSOCK(mode))
        printf("Socket\n");
    else
        printf("Unknown Type\n");
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        exit(1);
    }

    struct stat st;

    if (stat(argv[1], &st) == -1) {
        perror("stat");
        exit(1);
    }

    printf("File: %s\n", argv[1]);
    printf("Inode Number: %ld\n", (long)st.st_ino);
    printf("File Type: ");
    printType(st.st_mode);

    return 0;
}
