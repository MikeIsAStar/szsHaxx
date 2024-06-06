OUTPUT_FORMAT("binary")
OUTPUT_ARCH(powerpc:common);

ENTRY(start);

MEMORY {
    cluster (rx) : ORIGIN = 0x80388C10, LENGTH = 0x000001F0
}

SECTIONS {
    .first : {
        *(.first)
    } > cluster
    .text : {
        *(.text)
    } > cluster
    .rodata : {
        *(.rodata)
    } > cluster
}

memcpy = NETMemCpy;
snprintf = 0x800119A0;
ARCInitHandle = 0x80124578;
ARCOpen = 0x80124618;
GXAbortFrame = 0x8016E8E4;
__OSStopAudioSystem = 0x801A187C;
DCFlushRange = 0x801A1988;
OSFatal = 0x801A5220;
VIWaitForRetrace = 0x801B9D48;
VIFlush = 0x801BAD00;
VISetBlack = 0x801BAE88;
NETMemCpy = 0x801D1B54;
_ZN3EGG5Video9configureEPK18GXRenderModeObjectPKS3_ = 0x802440E0;
_ZN3mkw10HostSystem6System10s_instanceE = 0x80373FE8;
__OSAllocArenaEnd = 0x803748C8;
__OSAllocArenaStart = 0x803748CC;
