SUMMARY = "X-LINUX-AWS full components"

PV = "6.0"

inherit packagegroup

PROVIDES = "${PACKAGES}"
PACKAGES = "                 \
    packagegroup-x-linux-aws \
    "

# Manage to provide all framework tools base packages with overall one
RDEPENDS:packagegroup-x-linux-aws = "          \
    demo-application-aws                       \
    pkcs11-provider (>= 0.5-r1)                \
    optee-os-stm32mp-ta-pkcs11                 \
    optee-client (>= 4.0.0+git0+acb0885c11-r1) \
    pcsc-lite                                  \
    opensc                                     \
    "
