SUMMARY = "Add basic support of AWS IoT Greengrass on Demo Launcher"
HOMEPAGE = "wiki.st.com"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/BSD-3-Clause;md5=550794465ba0ec5312d6919e203a55f9"

DEPENDS = "\
    demo-launcher \
    sudo \
    "

PV = "5.0"

SRC_URI = " \
    file://__init__.py \
    file://070-aws.yaml \
    file://connected-cloud.png \
    file://aws.py \
    file://sudoers.d/demo-application-aws \
    "

do_configure[noexec] = "1"
do_compile[noexec] = "1"

do_install() {
    install -d ${D}${prefix}/local/demo/application/aws/pictures

    # install yaml file
    install -m 0644 ${WORKDIR}/*.yaml ${D}${prefix}/local/demo/application/
    # install pictures
    install -m 0644 ${WORKDIR}/*.png ${D}${prefix}/local/demo/application/aws/pictures
    # python script
    install -m 0755 ${WORKDIR}/*.py ${D}${prefix}/local/demo/application/aws/

    # add priviledges to application:
    install -d ${D}/${sysconfdir}/sudoers.d
    chmod 0750 ${D}/${sysconfdir}/sudoers.d
    install -m 0644 ${WORKDIR}/sudoers.d/demo-application-aws ${D}/${sysconfdir}/sudoers.d/demo-application-aws    
}

RDEPENDS:${PN} += "\
    python3-core \
    python3-pygobject \
    gtk+3 \
    python3-threading \
    demo-launcher \
    greengrass-bin \
    sudo \
    "

FILES:${PN} += "\
    ${prefix}/local/demo/application/ \
    ${sysconfdir}/sudoers.d/demo-application-aws \
    "
    
