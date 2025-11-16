#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <string.h>

struct FileInfo {
    char name[100];
    long size;
};

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("Usage: %s <file1> <file2> <file3> ...\n", argv[0]);
        exit(1);
    }

    struct FileInfo files[50];
    struct stat st;

    int n = argc - 1;

    // Read file sizes
    for (int i = 1; i < argc; i++) {
        if (stat(argv[i], &st) == -1) {
            perror("stat");
            exit(1);
        }
        strcpy(files[i - 1].name, argv[i]);
        files[i - 1].size = st.st_size;
    }

    // Sort ascending by size
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (files[i].size > files[j].size) {
                struct FileInfo temp = files[i];
                files[i] = files[j];
                files[j] = temp;
            }
        }
    }

    // Print result
    printf("\nFiles in ascending order of size:\n");
    for (int i = 0; i < n; i++) {
        printf("%s (%ld bytes)\n", files[i].name, files[i].size);
    }

    return 0;
}
