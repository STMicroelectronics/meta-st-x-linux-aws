DESCRIPTION+="\
This package has been patched by X-LINUX-AWS to \
install PKCS#11 Trusted Application (patched to \
improve PIN counter handling robustness) into \
file system."

B = "${WORKDIR}/build"

FILESEXTRAPATHS:prepend := "${THISDIR}/optee-os:"

SRC_URI += "file://0001-ta-pkcs11-Improve-PIN-counter-handling-robustness.patch "

do_install:append() {
    BOARD_NAME=$(echo ${STM32MP_DT_FILES_SDCARD} | awk -F" " '{print $1}')
    TA_PKCS11="${B}/${BOARD_NAME}/ta/pkcs11/fd02c9da-306c-48c7-a49c-bbd827ae86ee.ta"

    if [ -f "${TA_PKCS11}" ]
    then
        mkdir -p ${D}${nonarch_base_libdir}/optee_armtz/
        install -D -p -m 0444 ${TA_PKCS11} ${D}${nonarch_base_libdir}/optee_armtz/
    fi
}

FILES:${PN} += "${nonarch_base_libdir}/optee_armtz/"

PR = "r1"
