OUTPUT_FORMAT("binary")
OUTPUT_ARCH(powerpc:common);

ENTRY(start);

MEMORY {
	cluster (rx) : ORIGIN = 0x80396870, LENGTH = 0x000001F0
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
snprintf = 0x80010DD8;
ARCInitHandle = 0x80124460;
ARCOpen = 0x80124500;
GXAbortFrame = 0x8016E7A8;
__OSStopAudioSystem = 0x801A1480;
DCFlushRange = 0x801A158C;
OSFatal = 0x801A4E24;
VIWaitForRetrace = 0x801B994C;
VIFlush = 0x801BA904;
VISetBlack = 0x801BAA8C;
NETMemCpy = 0x801D1758;
_ZN3EGG5Video9configureEPK18GXRenderModeObjectPKS3_ = 0x80242EB0;
_ZN3mkw10HostSystem6System10s_instanceE = 0x80381C48;
__OSAllocArenaEnd = 0x80382528;
__OSAllocArenaStart = 0x8038252C;
