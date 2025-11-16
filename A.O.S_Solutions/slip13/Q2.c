#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: %s <prefix>\n", argv[0]);
        exit(1);
    }

    char *prefix = argv[1];
    int len = strlen(prefix);

    DIR *dp;
    struct dirent *entry;

    dp = opendir(".");
    if (dp == NULL) {
        perror("opendir");
        exit(1);
    }

    printf("Files starting with \"%s\":\n", prefix);

    while ((entry = readdir(dp)) != NULL) {
        if (strncmp(entry->d_name, prefix, len) == 0) {
            printf("%s\n", entry->d_name);
        }
    }

    closedir(dp);
    return 0;
}
