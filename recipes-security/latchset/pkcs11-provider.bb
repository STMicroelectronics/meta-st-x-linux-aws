SUMMARY = "This is an Openssl 3.x provider to access Hardware or Software Tokens using the PKCS#11 Cryptographic Token Interface"
HOMEPAGE = "https://github.com/latchset/pkcs11-provider"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM += "file://${COMMON_LICENSE_DIR}/Apache-2.0;md5=89aea4e17d99a7cacdbeed46a0096b10"

inherit autotools pkgconfig

SRC_URI = "git://github.com/latchset/pkcs11-provider.git;protocol=https;branch=main"

FILESEXTRAPATHS:prepend := "${THISDIR}:"

SRC_URI += " \
    file://files/openssl-pkcs11-provider-optee.cnf \
    file://files/openssl-pkcs11-provider-tpm2.cnf \
    file://files/pin.txt \
"

PV = "0.3"
SRCREV = "58040b4e32975cc1d7f39e424ee7b0097cd11311"

DEPENDS = "\
    openssl \
    autoconf-archive-native \
    libtool \
    pkgconfig \
    "

S = "${WORKDIR}/git"


do_configure () {
    cd ${S}
    autoreconf -fi 
    oe_runconf
}

do_compile() {
    cd ${S}
    oe_runmake
    oe_runmake check
}

do_install() {
    cd ${S}
    oe_runmake install DESTDIR="${D}"

    install -d ${D}/etc/pki/
    install -m 0755 ${WORKDIR}/files/openssl-pkcs11-provider-optee.cnf ${D}/etc/pki/openssl-pkcs11-provider-optee.cnf
    install -m 0755 ${WORKDIR}/files/openssl-pkcs11-provider-tpm2.cnf ${D}/etc/pki/openssl-pkcs11-provider-tpm2.cnf
    install -m 0755 ${WORKDIR}/files/pin.txt ${D}/etc/pki/pin.txt
}

RDEPENDS:${PN} += "\
    openssl \
    "
    
FILES:${PN} += "\
    /usr/ \
    "
