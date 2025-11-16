#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>

int main()
{
    DIR *dp;
    struct dirent *entry;
    int count = 0;

    dp = opendir(".");
    if (dp == NULL) {
        perror("opendir");
        exit(1);
    }

    printf("Files in current directory:\n");

    while ((entry = readdir(dp)) != NULL) {
        printf("%s\n", entry->d_name);
        count++;
    }

    closedir(dp);

    printf("\nTotal number of files: %d\n", count);

    return 0;
}
