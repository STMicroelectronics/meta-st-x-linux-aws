<p align="center">
    <img width="720" src="x-linux-aws-logo.png">
</p>

X-LINUX-AWS is an STM32 MPU OpenSTLinux Expansion Package that targets Amazon Web Services® AWS IoT Greengrass<sup>TM</sup> V2 for STM32MP13 and STM32MP25 product microprocessors.  

It integrates the Greengrass nucleus component to connect to AWS IoT Core<sup>TM</sup> to start and accelerate the development of an IoT solution.  

In addition, this OpenSTLinux Expansion Package provides good security practices with the integration of a secure solution for credential storage. This solution is based on the usage of OP-TEE and TPM.  

X-LINUX-AWS includes a demonstration application in which the AWS IoT Greengrass<sup>TM</sup> core device subscribes and publishes on a local MQTT network and on AWS IoT Core<sup>TM</sup>. This is achieved through the component deployment of an MQTT broker and bridge.

- AWS IoT Greengrass<sup>TM</sup> V2 integration
- Secured credential storage with OP-TEE or STPM4RasPI extension board
- Application sample based on GTK® to publish and subscribe on MQTT topics

# meta-st-x-linux-aws
X-LINUX-AWS OpenEmbedded meta layer to be integrated into OpenSTLinux distribution.
It contains recipes for Amazon Web Services® IoT Greengrass<sup>TM</sup> v2 integration with OP-TEE, TPM and application example.

## Compatibility
The X-LINUX-AWS OpenSTLinux Expansion Package is compatible with the Yocto Project™ build system and is validated over the OpenSTLinux Distribution.

| X-LINUX-AWS Version | Git Branch     | OpenSTLinux Distribution Version | Boards 
|----------           |--------        |----------                        |--------    
| v6.0.x              | scarthgap      | v6.0.x                           | STM32MP135F-DK<br>STM32MP257F-EV1<br>STM32MP257F-DK
| v5.1.x              | mickledore     | v5.1.x                           | STM32MP135F-DK<br>STM32MP257F-EV1
| v5.0.x              | mickledore_5.0 | v5.0.x                           | STM32MP135F-DK

## Versioning
Since its release v5.1.0, the major and minor versions of the X-LINUX-AWS OpenSTLinux Expansion Package are aligned on the major and minor versions of the OpenSTLinux Distribution. This prevents painful backward compatibility attempts and makes dependencies straightforward.

The X-LINUX-AWS generic versioning v**x**.**y**.**z** is built as follows:
* **x**: major version matching the OpenSTLinux Distribution major version. Each new major version is incompatible with previous OpenSTLinux Distribution versions.
* **y**: minor version matching the OpenSTLinux Distribution minor version. Each new minor version might be incompatible with previous OpenSTLinux Distribution versions.
* **z**: patch version to introduce bug fixes. A patch version is implemented in a backward compatible manner.

## Further information on X-LINUX-AWS Expansion Package
<https://wiki.st.com/stm32mpu/wiki/X-LINUX-AWS_Expansion_Package>

## Further information on how to install and how to use X-LINUX-AWS Starter package
<https://wiki.st.com/stm32mpu/wiki/X-LINUX-AWS_Starter_package>

## Further information on how to install and how to use X-LINUX-AWS Distribution package
<https://wiki.st.com/stm32mpu/wiki/X-LINUX-AWS_Distribution_package>

