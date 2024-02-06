#define _POSIX_C_SOURCE 200809L
#include "mysync.h"
#include <regex.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Convert a glob pattern to a regex pattern
char* convert_glob_to_regex(const char *glob) {
    char regex[1024];
    int j = 0;

    regex[j++] = '^'; // Start of the string

    for (int i = 0; glob[i] != '\0'; i++) {
        switch (glob[i]) {
            case '*':
                regex[j++] = '.';
                regex[j++] = '*';
                break;
            case '?':
                regex[j++] = '.';
                break;
            case '.':
            case '\\':
            case '+':
            case '^':
            case '$':
            case '|':
            case '(':
            case ')':
            case '{':
            case '}':
            case '[':
            case ']':
                // Escape special regex characters
                regex[j++] = '\\';
                regex[j++] = glob[i];
                break;
            default:
                regex[j++] = glob[i];
        }
    }

    regex[j++] = '$'; // End of the string
    regex[j] = '\0';

    return strdup(regex);
}

// Check if a filename matches a given pattern
bool matches_pattern(const char *filename, const char *pattern) {
    if (!pattern || !filename) {
        return false; // If either the pattern or filename is NULL, return false.
    }
    
    regex_t regex;
    char *regex_pattern = convert_glob_to_regex(pattern);

    if (regcomp(&regex, regex_pattern, REG_NOSUB) != 0) {
        fprintf(stderr, "Failed to compile regex for pattern: %s\n", pattern);
        free(regex_pattern);
        return false;
    }

    int status = regexec(&regex, filename, 0, NULL, 0);
    regfree(&regex);
    free(regex_pattern);

    return status == 0; // Return true if the filename matches the pattern
}