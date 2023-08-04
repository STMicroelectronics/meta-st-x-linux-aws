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
