ifeq ($(strip $(DEVKITPPC)),)
$(error "In order to build this program, please install devkitPPC.")
endif

include $(DEVKITPPC)/wii_rules

# Build directory
BUILDDIR := build

# Output directory
OUTDIR := out

# Include directory
INCLUDEDIR := include

# Source directory
SOURCEDIR := source

# Compiler flags
CXXFLAGS := -I$(INCLUDEDIR) -Oz -Wall -Werror -Wextra -ffreestanding -fno-asynchronous-unwind-tables -fno-exceptions -fno-rtti -fshort-wchar -nostdlib -std=c++23 $(MACHDEP)

# Linker editor
LD := $(DEVKITPPC)/bin/powerpc-eabi-ld

# Linker flags
LDFLAGS := -n

.PHONY: all
all: RMCP RMCE RMCJ RMCK

.PHONY: RMCP
RMCP: $(OUTDIR)/RMCP/loader.bin

.PHONY: RMCE
RMCE: $(OUTDIR)/RMCE/loader.bin

.PHONY: RMCJ
RMCJ: $(OUTDIR)/RMCJ/loader.bin

.PHONY: RMCK
RMCK: $(OUTDIR)/RMCK/loader.bin

.PHONY: clean
clean:
	@echo Cleaning...
	@rm -rf $(BUILDDIR) $(OUTDIR)

$(BUILDDIR)/RMCP/loader.o: $(SOURCEDIR)/loader.cpp
	@mkdir -p $(BUILDDIR)/RMCP

	@echo Compiling $<...
	@$(CXX) $(CXXFLAGS) -DREGION=P -c $< -o $@

$(BUILDDIR)/RMCE/loader.o: $(SOURCEDIR)/loader.cpp
	@mkdir -p $(BUILDDIR)/RMCE

	@echo Compiling $<...
	@$(CXX) $(CXXFLAGS) -DREGION=E -c $< -o $@

$(BUILDDIR)/RMCJ/loader.o: $(SOURCEDIR)/loader.cpp
	@mkdir -p $(BUILDDIR)/RMCJ

	@echo Compiling $<...
	@$(CXX) $(CXXFLAGS) -DREGION=J -c $< -o $@

$(BUILDDIR)/RMCK/loader.o: $(SOURCEDIR)/loader.cpp
	@mkdir -p $(BUILDDIR)/RMCK

	@echo Compiling $<...
	@$(CXX) $(CXXFLAGS) -DREGION=K -c $< -o $@

$(OUTDIR)/RMCP/loader.bin: $(BUILDDIR)/RMCP/loader.o
	@mkdir -p $(OUTDIR)/RMCP

	@echo Linking $<...
	@$(LD) $(LDFLAGS) -T loader_p.ld $(BUILDDIR)/RMCP/loader.o -o $(OUTDIR)/RMCP/loader.bin

$(OUTDIR)/RMCE/loader.bin: $(BUILDDIR)/RMCE/loader.o
	@mkdir -p $(OUTDIR)/RMCE

	@echo Linking $<...
	@$(LD) $(LDFLAGS) -T loader_e.ld $(BUILDDIR)/RMCE/loader.o -o $(OUTDIR)/RMCE/loader.bin

$(OUTDIR)/RMCJ/loader.bin: $(BUILDDIR)/RMCJ/loader.o
	@mkdir -p $(OUTDIR)/RMCJ

	@echo Linking $<...
	@$(LD) $(LDFLAGS) -T loader_j.ld $(BUILDDIR)/RMCJ/loader.o -o $(OUTDIR)/RMCJ/loader.bin

$(OUTDIR)/RMCK/loader.bin: $(BUILDDIR)/RMCK/loader.o
	@mkdir -p $(OUTDIR)/RMCK

	@echo Linking $<...
	@$(LD) $(LDFLAGS) -T loader_k.ld $(BUILDDIR)/RMCK/loader.o -o $(OUTDIR)/RMCK/loader.bin
