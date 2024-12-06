require recipes-st/images/st-image-weston.bb

SUMMARY = "OpenSTLinux AWS Greengrass image based on weston image"

# Define ROOTFS_MAXSIZE
IMAGE_ROOTFS_MAXSIZE = "2097152"

#
# INSTALL addons
#

CORE_IMAGE_EXTRA_INSTALL += " \
     packagegroup-x-linux-aws \
     "

IMAGE_INSTALL:remove = " \
     acl-dev \
     attr-dev \
     bash-completion-dev \
     bash-dev \
     cracklib-dev \
     cryptodev-linux-dev \
     gawk-dev \
     libc6-dev \
     libcap-dev \
     libcrypt-dev \
     libgcc-s-dev \
     libgmp-dev \
     libgpg-error-dev \
     libpam-dev \
     libreadline-dev \
     libstdc++-dev \
     libz-dev \
     linux-libc-headers-dev \
     ncurses-dev \
     openssl-dev \
     perl-dev \
     shadow-dev \
     tpm2-tss-engine-dev \
     "