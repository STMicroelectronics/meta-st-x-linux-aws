DESCRIPTION += "\
This package has been patched by X-LINUX-AWS to provide \
Greengrass PKCS#11 provider component, \
configuration file and AmazonRootCA1."
GG_BASE = "opt/greengrass"
GG_BASENAME = "${GG_BASE}/v2"
GG_ROOT = "${D}/${GG_BASENAME}"
S = "${WORKDIR}"

FILESEXTRAPATHS:prepend := "${THISDIR}:"
SRC_URI += " \
    file://files/config_pkcs11.yaml \
    https://www.amazontrust.com/repository/AmazonRootCA1.pem;name=AmazonRootCA1.pem; \
    https://d2s8p88vqu9w66.cloudfront.net/releases/Pkcs11Provider/aws.greengrass.crypto.Pkcs11Provider-2.0.6.jar;name=Pkcs11Provider.jar;downloadfilename=Pkcs11Provider.jar;unpack=0 \
    "

SRC_URI[AmazonRootCA1.pem.md5sum] = "7095142f080d1d25221eec161ff14223"
SRC_URI[Pkcs11Provider.jar.md5sum] = "a6058b389f56f3eae83a9acbcac0be76"

# greengrass-bin needs a correct clock, that should be done by any NTP client.
# nooelint: oelint.vars.dependsordered
RRECOMMENDS:${PN} += "\
    ${@bb.utils.contains('DISTRO_FEATURES', 'systemd', 'ntp-systemd', '', d)} \
    "

DEPENDS += " \
    aws-iot-device-sdk-python-v2 \
    "

do_install:append() {
    install -d ${GG_ROOT}/auth
    install -d ${GG_ROOT}/bin
    
    mv ${GG_ROOT}/config/config.yaml.clean ${GG_ROOT}/config/config.yaml

    install -m 0440 ${S}/AmazonRootCA1.pem    ${GG_ROOT}/auth/AmazonRootCA1.pem
    install -m 0740 ${S}/Pkcs11Provider.jar   ${GG_ROOT}/bin/aws.greengrass.crypto.Pkcs11Provider.jar

    sed -i -e '/services:/r ${S}/files/config_pkcs11.yaml' ${GG_ROOT}/config/config.yaml
    sed -i -e "s,##root_ca##,/${GG_BASENAME}/auth/AmazonRootCA1.pem,g" ${GG_ROOT}/config/config.yaml
    sed -i -e "s,##posixUser##,ggc_user:ggc_group,g" ${GG_ROOT}/config/config.yaml
    
    sed -i 's/OPTIONS="--setup-system-service false"/OPTIONS="--setup-system-service false --trusted-plugin $GG_ROOT\/bin\/aws.greengrass.crypto.Pkcs11Provider.jar"/g' ${GG_ROOT}/alts/init/distro/bin/loader
}

pkg_prerm:${PN}:append() {
rm -f /${GG_BASENAME}/config/*.tlog
rm -f /${GG_BASENAME}/config/effectiveConfig.yaml*
rm -f /${GG_BASENAME}/alts/init/launch.params
}

pkg_postrm:${PN}:append() {
rm -rf /${GG_BASE}
}

RDEPENDS:${PN} += "\
    aws-iot-device-sdk-python-v2 \
    "

PR = "r1"
