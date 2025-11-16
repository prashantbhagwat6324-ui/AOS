#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("Usage: %s <file1> <file2> ...\n", argv[0]);
        exit(1);
    }

    DIR *dp;
    struct dirent *entry;

    dp = opendir(".");
    if (dp == NULL) {
        perror("opendir");
        exit(1);
    }

    while ((entry = readdir(dp)) != NULL) {
        for (int i = 1; i < argc; i++) {
            if (strcmp(entry->d_name, argv[i]) == 0) {
                printf("File '%s' is PRESENT in current directory.\n", argv[i]);
            }
        }
    }

    closedir(dp);
    return 0;
}
