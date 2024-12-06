DESCRIPTION += "\
Customized by X-LINUX-AZURE \
to fix memory leakage on template serialization."

FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI += " \
    file://0001-libckteec-fix-memory-allocation-leakage-on-template-serialization.patch \
"

PR = "r1"
