OUTPUT_FORMAT("binary")
OUTPUT_ARCH(powerpc:common);

ENTRY(start);

MEMORY {
    cluster (rx) : ORIGIN = 0x8039A570, LENGTH = 0x000001F0
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
snprintf = 0x8001185C;
ARCInitHandle = 0x80124420;
ARCOpen = 0x801244C0;
GXAbortFrame = 0x8016E768;
__OSStopAudioSystem = 0x801A1440;
DCFlushRange = 0x801A154C;
OSFatal = 0x801A4DE4;
VIWaitForRetrace = 0x801B990C;
VIFlush = 0x801BA8C4;
VISetBlack = 0x801BAA4C;
NETMemCpy = 0x801D1718;
_ZN3EGG5Video9configureEPK18GXRenderModeObjectPKS3_ = 0x80243C8C;
_ZN3mkw10HostSystem6System10s_instanceE = 0x80385948;
__OSAllocArenaEnd = 0x80386228;
__OSAllocArenaStart = 0x8038622C;
