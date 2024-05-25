#pragma once

typedef struct {
    /* 0x00 */ unsigned char r;
    /* 0x01 */ unsigned char g;
    /* 0x02 */ unsigned char b;
    /* 0x03 */ unsigned char a;
} GXColor;

typedef struct {
    /* 0x00 */ unsigned char _00[0x04 - 0x00];
    /* 0x04 */ unsigned short framebufferWidth;
    /* 0x06 */ unsigned char _06[0x3C - 0x06];
} GXRenderModeObject;

#define GXCOLOR_SKY_BLUE \
    (GXColor) { \
        0xAA, 0xD9, 0xEE, 0xFF \
    }

#define GXCOLOR_PINK \
    (GXColor) { \
        0xFF, 0x00, 0xFF, 0xFF \
    }
