#pragma once

#define ARCH_FILE_MAGIC 0x55AA382D
#define ARCH_FILE_RESERVED_EVEN 0x4D696B65
#define ARCH_FILE_RESERVED_ODD 0x53746172

typedef struct {
    /* 0x00 */ unsigned char _00[0x1C - 0x00];
} ARCHandle;

typedef struct {
    /* 0x00 */ unsigned int magic;
    /* 0x04 */ unsigned char _04[0x10 - 0x04];
    /* 0x10 */ int reserved[4];
} ARCHeader;

typedef struct {
    /* 0x00 */ ARCHandle *handle;
    /* 0x04 */ unsigned int offset;
    /* 0x08 */ unsigned int length;
} ARCFileInfo;

int ARCInitHandle(void *file, ARCHandle *handle);
int ARCOpen(ARCHandle *handle, const char *filename, ARCFileInfo *fileInfo);
int ARCClose(ARCFileInfo *fileInfo);
