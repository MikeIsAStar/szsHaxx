#pragma once

#include "os/alloc.h"
#include "os/audioSystem.h"
#include "os/cache.h"

#include "gx/struct.h"

[[noreturn]] void OSFatal(GXColor foregroundColor, GXColor backgroundColor, const char *message);
