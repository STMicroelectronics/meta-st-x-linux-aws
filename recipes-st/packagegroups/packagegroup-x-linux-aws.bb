SUMMARY = "X-LINUX-AWS full components"

PV = "5.1"

inherit packagegroup

PROVIDES = "${PACKAGES}"
PACKAGES = "                 \
    packagegroup-x-linux-aws \
    "

# Manage to provide all framework tools base packages with overall one
RDEPENDS:packagegroup-x-linux-aws = "          \
    demo-application-aws                       \
    pkcs11-provider                            \
    optee-os-stm32mp-ta-pkcs11                 \
    optee-client                               \
    pcsc-lite                                  \
    opensc                                     \
    "
