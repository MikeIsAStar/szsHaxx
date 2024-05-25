#pragma once

#include <egg/core/video.hpp>

namespace mkw::HostSystem {

class System {
public:
    EGG::Video *video() {
        return m_video;
    }

    static System &Instance() {
        return s_instance;
    }

private:
    /* 0x00 */ unsigned char _00[0x44 - 0x00];
    /* 0x44 */ EGG::Video *m_video;
    /* 0x48 */ unsigned char _48[0x74 - 0x48];

    static System &s_instance;
};
static_assert(sizeof(System) == 0x74);

} // namespace mkw::HostSystem
