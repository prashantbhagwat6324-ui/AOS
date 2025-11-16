#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <time.h>

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
    printf("Number of Hard Links: %ld\n", (long)st.st_nlink);
    printf("File Size: %ld bytes\n", (long)st.st_size);

    // Permissions
    printf("Permissions: ");
    printf( (st.st_mode & S_IRUSR) ? "r" : "-");
    printf( (st.st_mode & S_IWUSR) ? "w" : "-");
    printf( (st.st_mode & S_IXUSR) ? "x" : "-");
    printf("\n");

    // Times
    printf("Last Access Time: %s", ctime(&st.st_atime));
    printf("Last Modification Time: %s", ctime(&st.st_mtime));

    return 0;
}
