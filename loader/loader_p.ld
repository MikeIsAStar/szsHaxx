OUTPUT_FORMAT("binary")
OUTPUT_ARCH(powerpc:common);

ENTRY(start);

MEMORY {
	cluster (rx) : ORIGIN = 0x8039ABF0, LENGTH = 0x000001F0
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
snprintf = 0x80011938;
ARCInitHandle = 0x80124500;
ARCOpen = 0x801245A0;
GXAbortFrame = 0x8016E848;
__OSStopAudioSystem = 0x801A1520;
DCFlushRange = 0x801A162C;
OSFatal = 0x801A4EC4;
VIWaitForRetrace = 0x801B99EC;
VIFlush = 0x801BA9A4;
VISetBlack = 0x801BAB2C;
NETMemCpy = 0x801D17F8;
_ZN3EGG5Video9configureEPK18GXRenderModeObjectPKS3_ = 0x80243D6C;
_ZN3mkw10HostSystem6System10s_instanceE = 0x80385FC8;
__OSAllocArenaEnd = 0x803868A8;
__OSAllocArenaStart = 0x803868AC;
