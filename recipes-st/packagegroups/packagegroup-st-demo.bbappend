RDEPENDS:${PN} += "\
    ${@bb.utils.contains('DISTRO_FEATURES', 'wayland', 'demo-application-aws', '', d)} \
    "