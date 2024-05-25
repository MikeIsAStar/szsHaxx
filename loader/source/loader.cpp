#include <mkw.hpp>
extern "C" {
#include <revolution.h>
}

#include <cstdint>
#include <cstdio>
#include <cstring>

#ifndef REGION
#error Please define the target region for this loader build !
#endif

#define LITERAL(value) #value
#define STRING(value) LITERAL(value)

[[noreturn]] void panic(const char *verb);

extern "C" __attribute__((noreturn, section(".first"))) void start() {
    constexpr uintptr_t payloadAddress = 0x90000020;
    static_assert((payloadAddress & 0x03) == 0);

    __OSStopAudioSystem();
    GXAbortFrame();

    const unsigned char *start = reinterpret_cast<unsigned char *>(__OSAllocArenaStart);
    const unsigned char *end =
            reinterpret_cast<unsigned char *>(__OSAllocArenaEnd) - sizeof(ARCHeader);
    while (start < end) {
        const ARCHeader *header = reinterpret_cast<const ARCHeader *>(start);
        if (header->magic == ARCH_FILE_MAGIC && header->reserved[0] == ARCH_FILE_RESERVED_EVEN) {
            goto label_open_archive;
        }
        start += sizeof(unsigned int);
    }
    panic("locate");

label_open_archive:
    ARCHandle handle;
    ARCFileInfo fileInfo;
    ARCInitHandle(const_cast<unsigned char *>(start), &handle);
    if (!ARCOpen(&handle, "payload.bin", &fileInfo)) {
        panic("open");
    }

    // Savezelda necessitates a framebuffer with a width of 640 pixels
    EGG::Video *video = mkw::HostSystem::System::Instance().video();
    GXRenderModeObject renderModeObject = *video->renderModeObject();
    renderModeObject.framebufferWidth = 640;
    video->configure(&renderModeObject);
    VISetBlack(0);
    VIFlush();
    VIWaitForRetrace();
    VIWaitForRetrace();

    void *destination = reinterpret_cast<void *>(payloadAddress);
    const void *source = start + fileInfo.offset;
    memcpy(destination, source, fileInfo.length);
    DCFlushRange(destination, fileInfo.length);

    void (*payload)();
    payload = reinterpret_cast<decltype(payload)>(destination);
    (*payload)();

    panic("execute");
}

void panic(const char *verb) {
    GXColor foregroundColor = GXCOLOR_PINK;
    GXColor backgroundColor = GXCOLOR_SKY_BLUE;

    char message[100];
    snprintf(message, sizeof(message),
            "szsHaxx Loader\n"
            "By: MikeIsAStar\n"
            "\n"
            "Failed to %s the payload !\n"
            "\n"
            "Built on " __DATE__ " for " STRING(REGION) ".",
            verb);

    OSFatal(foregroundColor, backgroundColor, message);
}
