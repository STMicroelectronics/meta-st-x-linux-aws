SUMMARY = "X-LINUX-AWS full components"

PV = "5.0"

inherit packagegroup

PROVIDES = "${PACKAGES}"
PACKAGES = "                 \
    packagegroup-x-linux-aws \
    "

# Manage to provide all framework tools base packages with overall one
RDEPENDS:packagegroup-x-linux-aws = "          \
    demo-application-aws                       \
    pkcs11-provider                            \
    optee-os-stm32mp (>= 3.19.0-stm32mp-r1-r1) \
    optee-client (>= 3.19.0+git0+140bf46304-r1)\
    pcsc-lite                                  \
    opensc                                     \
    "
