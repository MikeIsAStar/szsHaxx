#pragma once

#include <revolution/gx/struct.h>

namespace EGG {

class Video {
public:
    const GXRenderModeObject *configure(const GXRenderModeObject *renderModeObject = nullptr,
            const GXRenderModeObject *const *renderModeObjectTable = nullptr);

    GXRenderModeObject const *renderModeObject() {
        return m_renderModeObject;
    }

private:
    /* 0x00 */ GXRenderModeObject const *m_renderModeObject;
    /* 0x04 */ unsigned char _04[0x0C - 0x04];
};
static_assert(sizeof(Video) == 0x0C);

} // namespace EGG
