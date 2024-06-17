# X-LINUX-AWS License

## Software bill of materials

List of software brought by X-LINUX-AWS expansion package, installed on image **st-image-aws-openstlinux-weston-stm32mp1** in addition to image **st-image-weston-openstlinux-weston-stm32mp1**

| Recipe Name     |  Package Name  | Version  | Copyright  | License  | Description  
|----------       |----------      |--------  |--------    |--------  |--------
| aws-c-auth| libaws-c-auth1.0.0 | 0.7.4|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| C99 library implementation of AWS client-side authentication: standard credentials providers and signing
| aws-c-cal| libaws-c-cal1.0.0| 0.6.2|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography primitives.
| aws-c-common | libaws-c-common1 | 0.9.4|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| Core c99 package for AWS SDK for C. Includes cross-platform primitives, configuration, data structures, and error handling.
| aws-c-compression | libaws-c-compression1.0.0 | 0.2.17|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| C99 implementation of huffman encoding/decoding| aws-c-event-stream| libaws-c-event-stream1.0.0| 0.3.2|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| C99 implementation of the vnd.amazon.eventstream content-type| aws-c-http | libaws-c-http1.0.0 | 0.7.13|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| C99 implementation of the HTTP/1.1 and HTTP/2 specifications
| aws-c-event-stream | libaws-c-event-stream1.0.0  | 0.3.2| Amazon.com, Inc. or its affiliates |[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|C99 implementation of the vnd.amazon.eventstream content-type
| aws-c-io | libaws-c-io1.0.0 | 0.13.32|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| This is a module for the AWS SDK for C. It handles all IO and TLS work for application protocols.
| aws-c-mqtt | libaws-c-mqtt1.0.0 | 0.9.6|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| C99 implementation of the MQTT 3.1.1 specification
| aws-crt-python | aws-crt-python | 0.19.2|Amazon.com, Inc. or its affiliate|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| Python bindings for the AWS Common Runtime
| aws-c-s3 | libaws-c-s3-0unstable| 0.13.17|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| C99 library implementation for communicating with the S3 service, designed for maximizing throughput on high bandwidth EC2 instances.
| aws-c-sdkutils | libaws-c-sdkutils1.0.0 | 0.1.12|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| C99 library implementing AWS SDK specific utilities. Includes utilities for ARN parsing, reading AWS profiles, etc...
| aws-checksums | libaws-checksums1.0.0 | 0.1.17|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations. C interface with language bindings for each of our SDKs
| aws-iot-device-sdk-python-v2| aws-iot-device-sdk-python-v2| 1.19.0|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| AWS IoT Client SDK for Python using the AWS Common Runtime
| corretto-11-bin| corretto-11-bin| 11.0.20.9.1|Oracle and/or its affiliates. <br><br>And contributors. |  [Annex 1](#annex-1)| Amazon Corretto 11 is a no-cost, multi-platform, production-ready distribution of OpenJDK 11.
| demo-application-aws | demo-application-aws | 5.0|STMicroelectronics|[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| Demonstration application of X-LINUX-AWS
| greengrass-bin | greengrass-bin | 2.9.6-r1|Amazon.com, Inc. or its affiliates| [Apache-2.0](https://opensource.org/licenses/Apache-2.0)| AWS IoT Greengrass Nucleus - Binary Distribution<br><br>Customized by *meta-st-x-linux-aws* to add Amazon Root CA, configuration file and Greengrass PKCS#11 provider component 2.0.6.
| pkcs11-provider | pkcs11-provider  | 0.3|simo@redhat.com|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| A PKCS#11 provider for OpenSSL 3.0+
| s2n| libs2n1 | 1.3.51|Amazon.com, Inc. or its affiliates|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)| An implementation of the TLS/SSL protocols
| tpm2-abrmd | tpm2-abrmd  | 3.0.0| Intel Corporation |[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)| TPM2 Access Broker & Resource Manager
| tpm2-pkcs11 | tpm2-pkcs11  | 1.9.0-r1|g10 Code GmbH<br><br>Andreas Jellinghaus<br><br> Red Hat, Inc. |[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)| A PKCS#11 interface for TPM2 hardware.<br><br>Customized by *meta-st-x-linux-aws* to store TPM2 PKCS#11 context in /etc/tpm2_pkcs11
| tpm2-tools | tpm2-tools  | 5.5| Alibaba Group<br><br>Atom Software Studios, s.r.o.<br><br>Emmanuel Deloget <logout@free.fr><br><br>Fraunhofer SIT<br><br>Fraunhofer SIT sponsored by Infineon Technologies AG<br><br>GlovePuppet<br><br>Intel Corporation<br><br>Massachusetts Institute of Technology<br><br>National Instruments<br><br>Red Hat, Inc.<br><br>Sebastien LE STUM<br><br>SUSE GmbH<br><br>Wind River Systems |[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| Tools for TPM2.
| tpm2-totp | tpm2-totp  | 0.3.0|Behdad Esfahbod<br><br>Fraunhofer SIT<br><br>Jonas Witschel<br><br>Linux TPM2 & TSS2 Software<br><br>Red Hat Inc. |[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| Attest the trustworthiness of a device against a human using time-based one-time passwords
| tpm2-tss-engine | tpm2-tss-engine  | 1.1.0| Fraunhofer SIT sponsored by Infineon<br><br>Fraunhofer SIT sponsored by Infineon Technologies AG<br><br>Wind River Systems. |[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| Cryptographic engine implementation for OpenSSL for TPM2
| tpm2-tss | libtss2<br><br>libtss2-mu0<br><br>libtss2-tcti-device0<br><br>libtss2-tcti-mssim0<br><br>tpm2-tss  | 4.0.1|  Andreas Droescher<br><br>Behdad Esfahbod<br><br>Facebook, Inc. and its affiliates<br><br>Fraunhofer SIT<br><br>Fraunhofer SIT sponsored by Infineon Technologies AG<br><br>Intel<br><br>Intel Corporation<br><br>Infineon Technologies AG<br><br>Red Hat Inc.<br><br>Wind River Systems  |[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)| OSS implementation of the Trusted Computing Group TPM2 Software Stack
| trousers_git | trousers  | 0.3.15+git0+94144b0a1d|Christian Kummer<br><br>TrouSerS Project<br><br>International Business Machines Corp<br><br>Intel Corporation |[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| TrouSerS - An open-source Trusted Computing Group Software Stack Implementation.
|



List of software needed by X-LINUX-AWS expansion package, installed on image **st-image-aws-openstlinux-weston-stm32mp1**, available on ST package repository.

| Recipe Name     |  Package Name  | Version | License  | Description  
|----------       |----------      |-------- |--------  |--------
| ccid | ccid  | 1.5.2|[LGPL-2.1-or-later](https://opensource.org/license/lgpl-2-1)|Generic USB CCID smart card reader driver
| libtasn1 | libtasn1-6  | 4.19.0|[LGPL-2.1-or-later](https://opensource.org/license/lgpl-2-1)|A highly portable C library that encodes and decodes
| libusb-compat | libusb-0.1-4  | 0.1.8|[LGPL-2.1-or-later](https://opensource.org/license/lgpl-2-1)| libusb-0.1 compatibility layer for libusb1
| opensc | opensc | 0.23.0 |[LGPL-2.1](https://opensource.org/license/lgpl-2-1)| Smart card library and applications.
| optee-client| optee-client | 3.19.0+git0+140bf46304-r1 |[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause) | Normal World Client side of the TEE<br><br>Customized by *meta-st-x-linux-aws* to bring fix PKCS#11 Trusted Application token information support on 64bit architecture.
| optee-os-stm32mp| optee-os-stm32mp | 3.19.0-stm32mp-r2|[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)| OPTEE TA development kit for stm32mp<br><br>Customized by *meta-st-x-linux-aws* to bring PKCS#11 Trusted Application for OP-TEE.
| p11-kit | p11-kit | 0.24.1|[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| Provides a way to load and enumerate PKCS#11 modules
| pcsc-lite | libpcsclite1  | 1.9.9|[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)|PC/SC Lite smart card framework and applications
| pkgconfig_git | pkgconfig  | 0.29.2+git0+d97db4fae4|[GPL-2.0-or-later](https://opensource.org/license/gpl-2-0)|  Tool used when compiling applications and libraries. It helps determined the correct compiler/link options. It is also language-agnostic.
| python3-cffi | python3-cffi  |1.15.1|[MIT](https://opensource.org/license/mit)| Foreign Function Interface for Python calling C code
| python3-cryptography | python3-cryptography | 39.0.2| [Annex 2](#annex-2) | Provides cryptographic recipes and primitives to python developers
| python3-ply | python3-ply  | 3.11|[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| Python Lex and Yacc implementation
| python3-pyasn1 | python3-pyasn1  | 0.4.8|[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)| A collection of ASN.1-based protocols modules.
| python3-pyasn1-modules | python3-pyasn1-modules  | 0.2.8|[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)| A collection of ASN.1 modules expressed in form of pyasn1 classes. Includes protocols PDUs definition (SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).
| python3-pycparser | python3-pycparser  | 2.21|[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)| Parser of the C language, written in pure Python
|

## Annexes

### Annex 1

<u>Corretto 11 license terms: GPL-2.0-only + Classpath exception claimed license</u>

> The GNU General Public License (GPL)
> 
> Version 2, June 1991
> 
> Copyright (C) 1989, 1991 Free Software Foundation, Inc. 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
> 
> Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
> 
> Preamble
> 
> The licenses for most software are designed to take away your freedom to share and change it. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change free software--to make sure the software is free for all its users. This General Public License applies to most of the Free Software Foundation's software and to any other program whose authors commit to using it. (Some other Free Software Foundation software is covered by the GNU Library General Public License instead.) You can apply it to your programs, too.
> 
> When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for this service if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs; and that you know you can do these things.
> 
> To protect your rights, we need to make restrictions that forbid anyone to deny you these rights or to ask you to surrender the rights. These restrictions translate to certain responsibilities for you if you distribute copies of the software, or if you modify it.
> 
> For example, if you distribute copies of such a program, whether gratis or for a fee, you must give the recipients all the rights that you have. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.
> 
> We protect your rights with two steps: (1) copyright the software, and (2) offer you this license which gives you legal permission to copy, distribute and/or modify the software.
> 
> Also, for each author's protection and ours, we want to make certain that everyone understands that there is no warranty for this free software. If the software is modified by someone else and passed on, we want its recipients to know that what they have is not the original, so that any problems introduced by others will not reflect on the original authors' reputations.
> 
> Finally, any free program is threatened constantly by software patents. We wish to avoid the danger that redistributors of a free program will individually obtain patent licenses, in effect making the program proprietary. To prevent this, we have made it clear that any patent must be licensed for everyone's free use or not licensed at all.
> 
> The precise terms and conditions for copying, distribution and modification follow.
> 
> TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
> 
> 0. This License applies to any program or other work which contains a notice placed by the copyright holder saying it may be distributed under the terms of this General Public License. The "Program", below, refers to any such program or work, and a "work based on the Program" means either the Program or any derivative work under copyright law: that is to say, a work containing the Program or a portion of it, either verbatim or with modifications and/or translated into another language. (Hereinafter, translation is included without limitation in the term "modification".) Each licensee is addressed as "you".
> 
> Activities other than copying, distribution and modification are not covered by this License; they are outside its scope. The act of running the Program is not restricted, and the output from the Program is covered only if its contents constitute a work based on the Program (independent of having been made by running the Program). Whether that is true depends on what the Program does.
> 
> 1. You may copy and distribute verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice and disclaimer of warranty; keep intact all the notices that refer to this License and to the absence of any warranty; and give any other recipients of the Program a copy of this License along with the Program.
> 
> You may charge a fee for the physical act of transferring a copy, and you may at your option offer warranty protection in exchange for a fee.
> 
> 2. You may modify your copy or copies of the Program or any portion of it, thus forming a work based on the Program, and copy and distribute such modifications or work under the terms of Section 1 above, provided that you also meet all of these conditions:
> 
> a) You must cause the modified files to carry prominent notices stating that you changed the files and the date of any change.
> 
> b) You must cause any work that you distribute or publish, that in whole or in part contains or is derived from the Program or any part thereof, to be licensed as a whole at no charge to all third parties under the terms of this License.
> 
> c) If the modified program normally reads commands interactively when run, you must cause it, when started running for such interactive use in the most ordinary way, to print or display an announcement including an appropriate copyright notice and a notice that there is no warranty (or else, saying that you provide a warranty) and that users may redistribute the program under these conditions, and telling the user how to view a copy of this License. (Exception: if the Program itself is interactive but does not normally print such an announcement, your work based on the Program is not required to print an announcement.)
> 
> These requirements apply to the modified work as a whole. If identifiable sections of that work are not derived from the Program, and can be reasonably considered independent and separate works in themselves, then this License, and its terms, do not apply to those sections when you distribute them as separate works. But when you distribute the same sections as part of a whole which is a work based on the Program, the distribution of the whole must be on the terms of this License, whose permissions for other licensees extend to the entire whole, and thus to each and every part regardless of who wrote it.
> 
> Thus, it is not the intent of this section to claim rights or contest your rights to work written entirely by you; rather, the intent is to exercise the right to control the distribution of derivative or collective works based on the Program.
> 
> In addition, mere aggregation of another work not based on the Program with the Program (or with a work based on the Program) on a volume of a storage or distribution medium does not bring the other work under the scope of this License.
> 
> 3. You may copy and distribute the Program (or a work based on it, under Section 2) in object code or executable form under the terms of Sections 1 and 2 above provided that you also do one of the following:
> 
> a) Accompany it with the complete corresponding machine-readable source code, which must be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or,
> 
> b) Accompany it with a written offer, valid for at least three years, to give any third party, for a charge no more than your cost of physically performing source distribution, a complete machine-readable copy of the corresponding source code, to be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or,
> 
> c) Accompany it with the information you received as to the offer to distribute corresponding source code. (This alternative is allowed only for noncommercial distribution and only if you received the program in object code or executable form with such an offer, in accord with Subsection b above.)
> 
> The source code for a work means the preferred form of the work for making modifications to it. For an executable work, complete source code means all the source code for all modules it contains, plus any associated interface definition files, plus the scripts used to control compilation and installation of the executable. However, as a special exception, the source code distributed need not include anything that is normally distributed (in either source or binary form) with the major components (compiler, kernel, and so on) of the operating system on which the executable runs, unless that component itself accompanies the executable.
> 
> If distribution of executable or object code is made by offering access to copy from a designated place, then offering equivalent access to copy the source code from the same place counts as distribution of the source code, even though third parties are not compelled to copy the source along with the object code.
> 
> 4. You may not copy, modify, sublicense, or distribute the Program except as expressly provided under this License. Any attempt otherwise to copy, modify, sublicense or distribute the Program is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance.
> 
> 5. You are not required to accept this License, since you have not signed it. However, nothing else grants you permission to modify or distribute the Program or its derivative works. These actions are prohibited by law if you do not accept this License. Therefore, by modifying or distributing the Program (or any work based on the Program), you indicate your acceptance of this License to do so, and all its terms and conditions for copying, distributing or modifying the Program or works based on it.
> 
> 6. Each time you redistribute the Program (or any work based on the Program), the recipient automatically receives a license from the original licensor to copy, distribute or modify the Program subject to these terms and conditions. You may not impose any further restrictions on the recipients' exercise of the rights granted herein. You are not responsible for enforcing compliance by third parties to this License.
> 
> 7. If, as a consequence of a court judgment or allegation of patent infringement or for any other reason (not limited to patent issues), conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot distribute so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not distribute the Program at all. For example, if a patent license would not permit royalty-free redistribution of the Program by all those who receive copies directly or indirectly through you, then the only way you could satisfy both it and this License would be to refrain entirely from distribution of the Program.
> 
> If any portion of this section is held invalid or unenforceable under any particular circumstance, the balance of the section is intended to apply and the section as a whole is intended to apply in other circumstances.
> 
> It is not the purpose of this section to induce you to infringe any patents or other property right claims or to contest validity of any such claims; this section has the sole purpose of protecting the integrity of the free software distribution system, which is implemented by public license practices. Many people have made generous contributions to the wide range of software distributed through that system in reliance on consistent application of that system; it is up to the author/donor to decide if he or she is willing to distribute software through any other system and a licensee cannot impose that choice.
> 
> This section is intended to make thoroughly clear what is believed to be a consequence of the rest of this License.
> 
> 8. If the distribution and/or use of the Program is restricted in certain countries either by patents or by copyrighted interfaces, the original copyright holder who places the Program under this License may add an explicit geographical distribution limitation excluding those countries, so that distribution is permitted only in or among countries not thus excluded. In such case, this License incorporates the limitation as if written in the body of this License.
> 
> 9. The Free Software Foundation may publish revised and/or new versions of the General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.
> 
> Each version is given a distinguishing version number. If the Program specifies a version number of this License which applies to it and "any later version", you have the option of following the terms and conditions either of that version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of this License, you may choose any version ever published by the Free Software Foundation.
> 
> 10. If you wish to incorporate parts of the Program into other free programs whose distribution conditions are different, write to the author to ask for permission. For software which is copyrighted by the Free Software Foundation, write to the Free Software Foundation; we sometimes make exceptions for this. Our decision will be guided by the two goals of preserving the free status of all derivatives of our free software and of promoting the sharing and reuse of software generally.
> 
> NO WARRANTY
> 
> 11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
> 
> 12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
> 
> END OF TERMS AND CONDITIONS
> 
> How to Apply These Terms to Your New Programs
> 
> If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms.
> 
> To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively convey the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found.
> 
>    One line to give the program's name and a brief idea of what it does.
> 
>    Copyright (C) <year> <name of author>
> 
>    This program is free software; you can redistribute it and/or modify it
>    under the terms of the GNU General Public License as published by the Free
>    Software Foundation; either version 2 of the License, or (at your option)
>    any later version.
> 
>    This program is distributed in the hope that it will be useful, but WITHOUT
>    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
>    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
>    more details.
> 
>    You should have received a copy of the GNU General Public License along
>    with this program; if not, write to the Free Software Foundation, Inc.,
>    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
> Also add information on how to contact you by electronic and paper mail.
> 
> If the program is interactive, make it output a short notice like this when it starts in an interactive mode:
> 
>    Gnomovision version 69, Copyright (C) year name of author Gnomovision comes
>    with ABSOLUTELY NO WARRANTY; for details type 'show w'.  This is free
>    software, and you are welcome to redistribute it under certain conditions;
>    type 'show c' for details.
> The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, the commands you use may be called something other than 'show w' and 'show c'; they could even be mouse-clicks or menu items--whatever suits your program.
> 
> You should also get your employer (if you work as a programmer) or your school, if any, to sign a "copyright disclaimer" for the program, if necessary. Here is a sample; alter the names:
> 
>    Yoyodyne, Inc., hereby disclaims all copyright interest in the program
>    'Gnomovision' (which makes passes at compilers) written by James Hacker.
> 
>    signature of Ty Coon, 1 April 1989
> 
>    Ty Coon, President of Vice
> This General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Library General Public License instead of this License.
> 
> 
> "CLASSPATH" EXCEPTION TO THE GPL
> 
> Certain source files distributed by Oracle America and/or its affiliates are subject to the following clarification and special exception to the GPL, but only where Oracle has expressly included in the particular source file's header the words "Oracle designates this particular file as subject to the "Classpath" exception as provided by Oracle in the LICENSE file that accompanied this code."
> 
> Linking this library statically or dynamically with other modules is making a combined work based on this library. Thus, the terms and conditions of the GNU General Public License cover the whole combination.
> 
> As a special exception, the copyright holders of this library give you permission to link this library with independent modules to produce an executable, regardless of the license terms of these independent modules, and to copy and distribute the resulting executable under terms of your choice, provided that you also meet, for each linked independent module, the terms and conditions of the license of that module. An independent module is a module which is not derived from or based on this library. If you modify this library, you may extend this exception to your version of the library, but you are not obligated to do so. If you do not wish to do so, delete this exception statement from your version.

<u>Additonnal information about Corretto 11 licensing</u>

>Certain files distributed by Oracle America, Inc. and/or its affiliates are subject to the following clarification and special exception to the GPLv2, based on the GNU Project exception for its Classpath libraries, known as the GNU Classpath Exception.
>
>Note that Oracle includes multiple, independent programs in this software package. Some of those programs are provided under licenses deemed incompatible with the GPLv2 by the Free Software Foundation and others. For example, the package includes programs licensed under the Apache License, Version 2.0 and may include FreeType. Such programs are licensed to you under their original licenses.
>
>Oracle facilitates your further distribution of this package by adding the Classpath Exception to the necessary parts of its GPLv2 code, which permits you to use that code in combination with other independent modules not licensed under the GPLv2. However, note that this would not permit you to commingle code under an incompatible license with Oracle's GPLv2 licensed code by, for example, cutting and pasting such code into a file also containing Oracle's GPLv2 licensed code and then distributing the result.
>
>Additionally, if you were to remove the Classpath Exception from any of the files to which it applies and distribute the result, you would likely be required to license some or all of the other code in that distribution under the GPLv2 as well, and since the GPLv2 is incompatible with the license terms of some items included in the distribution by Oracle, removing the Classpath Exception could therefore effectively compromise your ability to further distribute the package.
>
>Failing to distribute notices associated with some files may also create unexpected legal consequences.
>
>Proceed with caution and we recommend that you obtain the advice of a lawyer skilled in open source matters before removing the Classpath Exception or making modifications to this package which may subsequently be redistributed and/or involve the use of third party software.


### Annex 2

<u>python3-cryptography license terms:</u>

> This software is made available under the terms of *either* of the licenses
found in [Apache-2.0](https://opensource.org/licenses/Apache-2.0) or [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause). Contributions to cryptography are made
> under the terms of *both* these licenses.
>  
> The code used in the OS random engine is derived from CPython, and is licensed
under the terms of the [PSF-2.0](https://opensource.org/license/python-2-0).


