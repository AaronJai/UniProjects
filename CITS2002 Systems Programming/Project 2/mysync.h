// mysync.h

#ifndef MYSYNC_H
#define MYSYNC_H

#include <stdbool.h>

// Struct to hold file information
typedef struct {
    char *filename;
    long modification_time;
} FileInfo;

// Struct to hold command-line options
typedef struct {
    bool all_files;      // -a
    bool no_act;         // -n
    bool only_pattern;   // -o
    bool ignore_pattern; // -i
    bool preserve;       // -p
    bool recursive;      // -r
    bool verbose;        // -v
    char *pattern;       // For -o or -i
} Options;

// Function prototypes for dir_ops.c
FileInfo* list_directory(const char *dir_path, int *num_files);
bool is_directory(const char *path);

// Function prototypes for file_ops.c
void copy_file(const char *src_path, const char *dst_path, bool preserve);
long get_file_modification_time(const char *path);

// Function prototypes for sync_ops.c
void sync_directories(const char *dir1, const char *dir2, const Options *options);

// Function prototypes for pattern_ops.c (if we decide to separate it)
bool matches_pattern(const char *filename, const char *pattern);
char* convert_glob_to_regex(const char *glob);

#endif
