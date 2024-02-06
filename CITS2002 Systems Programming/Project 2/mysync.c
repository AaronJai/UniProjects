#include "mysync.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <getopt.h>

void usage() {
    fprintf(stderr, "Usage: mysync [options] directory1 directory2 [directory3 ...]\n");
    exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) {
    Options options = {0};

    int opt;
    while ((opt = getopt(argc, argv, "aino:prv")) != -1) {
        switch (opt) {
            case 'a':
                options.all_files = true;
                break;
            case 'i':
                options.ignore_pattern = true;
                options.pattern = optarg;
                optind++;   // Increment to skip the pattern in the next loop
                break;
            case 'n':
                options.no_act = true;
                options.verbose = true; // -n sets -v
                break;
            case 'o':
                options.only_pattern = true;
                options.pattern = optarg;
                break;
            case 'p':
                options.preserve = true;
                break;
            case 'r':
                options.recursive = true;
                break;
            case 'v':
                options.verbose = true;
                break;
            default:
                usage();
        }
    }

    if (argc - optind < 2) {
        fprintf(stderr, "At least two directories must be provided.\n");
        usage();
    }

    // Synchronize the directories in a pairwise manner
    for (int i = optind; i < argc - 1; i++) {
        for (int j = i + 1; j < argc; j++) {
            sync_directories(argv[i], argv[j], &options);
        }
    }

    return 0;
}
