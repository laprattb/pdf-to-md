![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-0-0.png)
## Opcenter Reporting 2401.0001

# Installation Manual

04/2024


PL20240130630874732


**Guidelines**


This manual contains notes of varying importance that should be read with care; i.e.:


Important:


Highlights key information on handling the product, the product itself or to a particular part of the documentation.


Note: Provides supplementary information regarding handling the product, the product itself or a specific part of


the documentation.


**Trademarks**


All names identified by ® are registered trademarks of Siemens AG.


Report-/Print engine List & Label ® Version 28: Copyright combit® GmbH.


The remaining trademarks in this publication may be trademarks whose use by third parties for their own purposes


could violate the rights of the owner.


**Disclaimer of Liability**


We have reviewed the contents of this publication to ensure consistency with the hardware and software


described. Since variance cannot be precluded entirely, we cannot guarantee full consistency. However, the


information in this publication is reviewed regularly and any necessary corrections are included in subsequent


editions.


**Security information**


Siemens provides products and solutions with industrial security functions that support the secure operation of


plants, systems, machines and networks.


In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement 

and continuously maintain - a holistic, state-of-the-art industrial security concept. Siemens’ products and solutions


constitute one element of such a concept.


Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks.


Such systems, machines and components should only be connected to an enterprise network or the internet if and


to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or


network segmentation) are in place.


For additional information on industrial security measures that may be implemented, please visit


[https://www.siemens.com/industrialsecurity.](https://www.siemens.com/industrialsecurity)


Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly


recommends that product updates are applied as soon as they are available and that the latest product versions


are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase


customer’s exposure to cyber threats.


To stay informed about product updates, subscribe to the Siemens Industrial Security RSS Feed under


[https://www.siemens.com/cert.](https://www.siemens.com/cert)



Siemens AG


Digital Industries


Postfach 48 48


90026 NÜRNBERG


GERMANY



PL20240130630874732


20240409_160639



Copyright © Siemens AG 2024


Technical data subject to change


## Table of Contents

###### 1 Before you Start ................................................................................................... 6

1.1 Managing Licenses, Users and Roles for Opcenter Reporting .................................................6


1.2 Prerequisites ..............................................................................................................................8


1.2.1 Software Requirements...........................................................................................................................................8


1.2.2 Hardware Requirements........................................................................................................................................10


1.3 Security Strategies...................................................................................................................10


1.3.1 Overview of Network Security...............................................................................................................................11


1.3.1.1 Security Cells and DMZs.........................................................................................................................................12


1.3.1.2 Firewall and VPN ....................................................................................................................................................14


1.3.1.3 Secure Communication between Security Cells ..................................................................................................16


1.3.2 Overview of System Integrity ................................................................................................................................17


1.3.2.1 System Hardening..................................................................................................................................................18


1.3.2.2 Patch Management................................................................................................................................................20


1.3.2.3 Malware Detection and Prevention.......................................................................................................................20


1.4 Preliminary Configurations .....................................................................................................21


1.4.1 Installing the License Server..................................................................................................................................21


1.4.2 Checking Oracle 19c Installation Requirements ..................................................................................................22


1.4.3 Checking Oracle Installation Requirements (versions previous to 19c) .............................................................25


1.4.4 Configuring IIS and ASP.NET Role Services ..........................................................................................................27


1.4.4.1 Roles .......................................................................................................................................................................27


1.4.4.2 Features..................................................................................................................................................................29

###### 2 How to Install Opcenter Reporting ................................................................... 31


2.1 Installing Opcenter Reporting Interactively ...........................................................................31


2.2 Installing Opcenter Reporting via Command Line.................................................................36


2.2.1 Examples of Automated Installation via the Command Line ..............................................................................37


2.2.2 Parameters for Automated Installation................................................................................................................38


2.2.3 Return Values from the Installation Process ........................................................................................................39


2.2.4 Customizing the Installation .................................................................................................................................41

###### 3 How to Configure Opcenter Reporting ............................................................. 43


3.1 Summary of Port Numbers required for Opcenter Reporting Configuration .......................43


3.2 Creating Opcenter Reporting Users in UMC............................................................................44


3.3 Configuring Opcenter Reporting Interactively with Opcenter Reporting Configurator.......44


3.4 Configuring Opcenter Reporting via Command Line.............................................................47


Opcenter Reporting 2401.0001 - Installation Manual iii


3.5 Performing Additional Configuration Operations..................................................................49


3.6 How to Configure Microsoft ARR as Reverse Proxy ................................................................49


3.6.1 Creating the Web Farms.........................................................................................................................................50


3.6.2 Configuring the Redirection Rules ........................................................................................................................51


3.6.3 Configuring the Redirection Rule Order................................................................................................................53


3.6.4 Increasing the Default Proxy Timeout ..................................................................................................................53


3.6.5 Configuring the Maximum Content Length Allowed for File Processing.............................................................54


3.6.6 Setting the Recycle Time to Zero ..........................................................................................................................54


3.6.7 Configuring the Connection from Web Clients.....................................................................................................54

###### 4 How to Integrate Opcenter Reporting with other Products ............................ 55


4.1 How to Integrate Opcenter Reporting with Products not supporting UMC..........................55


4.1.1 Generating Public and Private RSA Keys ..............................................................................................................55


4.1.2 Getting the One-Time Authorization Code ...........................................................................................................56


4.1.3 Getting Reports from Opcenter Reporting ...........................................................................................................59


4.1.4 Embedding Reports ...............................................................................................................................................60


4.1.5 Providing Values for Report Parameters...............................................................................................................62


4.1.6 Releasing a Seat after Report Visualization..........................................................................................................64


4.2 How to Integrate Opcenter Reporting with Products supporting UMC ................................65


4.2.1 Embedding Reports ...............................................................................................................................................66


4.3 Executing and Getting a Report as PDF without User Interaction.........................................68

###### 5 Upgrading Opcenter Reporting from version 2401 to version 2401.0001....... 72 6 Uninstalling Opcenter Reporting ...................................................................... 76 7 Troubleshooting................................................................................................. 77


iv Opcenter Reporting 2401.0001 - Installation Manual


![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-4-0.png)



Opcenter Reporting 2401.0001 - Installation Manual 5


_Before you Start_


_Managing Licenses, Users and Roles for Opcenter Reporting_

## 1 Before you Start


Before you install Opcenter Reporting, you must:












Choose the license type that better satisfies your requirements, depending on the operations you want to
execute and on the number of users who will perform them.
Verify that all prerequisites are satisfied.
Follow the suggestions on how to implement security strategies so that any risks and threats that may affect
your system are successfully mitigated.
Perform a number of preliminary configurations.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-5-0.png)




##### Installation Options

Opcenter Reporting can be installed in either of the following ways:









After the installation of Opcenter Intelligence, whose ISO root folder contains the **OpcenterReport** subfolder
including Opcenter Reporting setup files.
As a stand-alone application, directly launching the **Start.exe** program file from the **OpcenterReport**
subfolder.



For more information, see Installing Opcenter Reporting.

###### Virtual Infrastructure Support


Opcenter Reporting supports VMware ESXi 6.7 Update 3 infrastructure, although the possibility cannot be excluded
that Opcenter Reporting can run on other Cloud environment types.
For the configuration of virtual infrastructure resources there are no constraints on the type of storage, vCPU, RAM,
or network board type. However, before configuring the infrastructure, it is recommended that you keep in mind
Opcenter Reporting hardware requirements and allocate resources (RAM, vCPU and so on) to guarantee the
maximum performance level of VMWare operations.

### 1.1 Managing Licenses, Users and Roles for Opcenter Reporting


Starting from version 3.2, a new licensing model is applied. According to this new model, license types are based on
the number of users (seats) that can access the application at the same time, depending on the type of purchased
license. A seat is consumed for each logged-in user, unless this user has been assigned the **No role** role.


While in previous versions the creation of analytical solutions and the use of the Manufacturing Data Warehouse
and ETLs were allowed to customers who purchased the Opcenter Reporting license, starting from version 3.5 the
purchase of an additional Opcenter Intelligence license is required to use these functionalities.





The following licenses can be purchased for Opcenter Reporting:


6 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Managing Licenses, Users and Roles for Opcenter Reporting_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-6-0.png)






###### Users and Roles

If the **Can perform administrative functions** check box is selected for a user, he can perform the following
operations:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-6-1.png)









The following roles can be associated with users in the **Access Control** page.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-6-2.png)







Opcenter Reporting 2401.0001 - Installation Manual 7


_Before you Start_


_Prerequisites_

### 1.2 Prerequisites


The following prerequisites are required before you install Opcenter Reporting.








Software Requirements
Hardware Requirements




#### 1.2.1 Software Requirements

###### Operating Systems











Windows Server 2022

Windows Server 2019

Windows Server 2016

Windows 10

Windows 11



Maintenance services, according to General SISW Maintenance Services Terms, are extended to the updates and the
patches (excluding full Service Packs) that are officially released by Microsoft for the aforementioned Operating
Systems.

###### Source Database Management Systems


Depending on the data source version, some SQL Server versions may not be supported. For more details, see the
documentation of the data source product.





**Microsoft SQL Server**



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-7-2.png)



8 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Prerequisites_


Maintenance services, according to General SISW Maintenance Services Terms, are extended to the Successive
Service Packs of these SQL Server versions, if and only if Microsoft declares their compatibility with it.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-8-0.png)





**Oracle**



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-8-1.png)



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-8-2.png)








###### User Management Component (UMC)









Opcenter Reporting is compatible with User Management Component (UMC) 2.6 and higher.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-8-3.png)

Opcenter Reporting is not compatible with UMC 1.9.1.







For more information on UMC prerequisites, see _User Management Component Installation Manual_ .

###### Licensing software


Siemens License Server (SLS)


This software is available on Support Center at the link https://support.sw.siemens.com/en-US/product/
1586485382/downloads


It is required for Opcenter Reporting configuration and can be installed either on an Opcenter Reporting machine or
on a separate machine where Opcenter Reporting is not installed.


Siemens License Server installation and usage are documented in the following manuals:









_Siemens Digital Industries Software License Server Installation Instructions_
( **sw_siemens_license_server_install.pdf** )
_Siemens Digital Industries Software Licensing Manual for PLM Products_ ( **sw_siemens_licensing_plm.pdf** )


###### Other Third-Party Software

Opcenter Reporting 2401.0001 - Installation Manual 9


_Before you Start_


_Security Strategies_








Either Internet Information Services 8.5 or 10 enabling ASP.NET Modules and IIS Role Services
Microsoft .NET Framework 4.7.2. This software can be downloaded at https://dotnet.microsoft.com/
download/dotnet-framework/net472


###### Internet Browsers

Opcenter Reporting has been tested on the following browsers and versions:









Microsoft Edge (based on Chromium) 123
Google Chrome 123
Mozilla Firefox 124


###### No Longer Supported Software








Windows Server 2012 R2 x64
Microsoft Internet Explorer


#### 1.2.2 Hardware Requirements

The minimum hardware requirements for Opcenter Reporting are the following:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-9-0.png)







![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-9-1.png)






### 1.3 Security Strategies





Computer systems and networks are inherently vulnerable to a wide variety of security threats that can be
prevented or reduced by adopting specific security countermeasures.


Each of these technical measures is specific to a certain attack (viruses cannot be prevented with firewalls) and can
cover only a subset of the necessary protection goals. Nevertheless, only an overall strategy can provide effective
protection.
The Siemens Industrial Security concept corresponds to a multi-layer defense, known as defense-in-depth concept.
This strategy consists of several defense layers that protect a system, in this case the MOM/MES system:







**Plant Security Layer** : Plant security ensures that technical IT security measures cannot be bypassed
somehow. This includes physical-access protection measures (such as fences, turnstiles, cameras or cardreaders) and organizational measures (in particular, a security management process) for ensuring long-term
plant security.



10 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Security Strategies_


**Network Security Layer** : The core of the Industrial Security concept is network security. This includes
protecting automation networks from unauthorized access and checking all interfaces towards other
networks, such as an office network and, in particular, remote access to the Internet. Network security also
encompasses protecting communication from interception and manipulation (for example, encryption
during data transfer and authentication of the respective communication nodes). For more information, see
Overview of Network Security.
**System Integrity Layer** : Securing system integrity should be regarded as the third pillar of a balanced
security concept. This is ensured by using automation systems and controller components that are
protected against unauthorized access and malware or meet special requirements, such as know-how
protection. For more information, see _Overview of System Integrity_ .



Adopting a defense-in-depth approach allows you to achieve comprehensive and reliable protection of an
automated system.

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-10-0.png)

#### 1.3.1 Overview of Network Security


Network security represents the core of the Industrial Security concept.
This includes protecting automation networks from unauthorized access and checking all interfaces towards other
networks, such as an office network and, in particular, remote access to the Internet. Network security also
encompasses protecting communication from interception and manipulation (for example, encryption during data
transfer and authentication of the respective communication nodes).
One strategy used for increasing overall system availability that can effectively mitigate security risks is the
segmentation of the network into a set of so-called security cells.
Each cell is conceived to cover a specific business function and has a dedicated protected network.
As a result, devices within a cell can be protected from unauthorized access from the outside without affecting realtime capabilities, performance or other functions. Security threats that result in failure can thus be restricted to the
immediate area.
A particular type of security cell is the Demilitarized Zone (DMZ), which can be used to isolate certain applications
from external networks.


Opcenter Reporting 2401.0001 - Installation Manual 11


_Before you Start_


_Security Strategies_


For more information on how to set up a secure network by managing safe communications between security cells,

see:









Security Cells and DMZs
Firewall and VPN

Secure Communication between Security Cells


##### 1.3.1.1 Security Cells and DMZs

Dividing networks and connected plants into security cells consists in dividing up a large corporate network into
separate networks, each used for a specific business function. This strategy increases the availability of the overall
system and is an effective way to mitigate security risks. In the implementation of this approach parts of a network,
e.g. an IP subnet, are protected by a security appliance and the network is secured by segmentation. Thus, devices
within this 'cell' can be protected from unauthorized access from outside without affecting real-time capabilities,
performance or other
functions. Security threats that result in failure can thereby be restricted to the immediate vicinity.
The different ISA95 levels can be used to identify security cells, for example by keeping ERP (Enterprise Resource
Planning) functions separate from MES (Manufacturing Execution System) functions.

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-11-0.png)


According to the ISA-95 levels, the following levels can be identified:









Enterprise Resource Planning Level
Manufacturing Execution Systems Level
Manufacturing Control Systems Level



Each level includes one or more networks. In addition we identify also perimeter networks.
When creating security cells, you should follow some design rules.
In this section we present also the example configuration organized in different security cells.


For more information, see https://new.siemens.com/global/en/products/automation/topic-areas/industrialsecurity.html

###### Enterprise Resource Planning Level


The Enterprise Resource Planning Level is where the ERP Systems are managed. The network connecting the ERP
Systems may need to communicate with both MES and Process Control Systems located in other networks. This
network is generally the outermost network used in a plant: as a result, it is the most exposed to potential security
risks. For this reason, it is recommended to make this network to connect to other networks via Perimeter Network,
instead of direct connection.


12 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Security Strategies_

###### Manufacturing Execution System Level


The Manufacturing Execution System Level is where the data exchange among Manufacturing Execution System
devices is managed. The network includes MES/MOM servers and can be directly connected to a Process Control
Network.

###### Manufacturing Control System Level


The Manufacturing Control System Level hosts the control-layer software systems, such as generic DNC systems,
SIMATIC WinCC or SIMATIC PCS7, and is where the data exchange among Manufacturing Control System devices is
managed. Since this network is very close to the field, it is important to keep it as separate as possible from the
external networks, to mitigate security risks and to protect the plant production.

###### Perimeter Network


In addition to the networks listed above, we have also Perimeter Networks in our scenarios, sometimes called DMZs
(Demilitarized Zones). These are networks used to isolate certain applications from outside networks, thereby
mitigating security risks.
Typically, Web Servers are placed in this network, so that they can collect data from low level networks and, at the
same time, they can provide web pages to outer networks (for example an Enterprise Control Network).
If you are planning to connect using the Remote Desktop Service, the Remote Desktop Service Server should be
placed in this network.

###### Design Rules


When designing and implementing a complex network scenario, the following rules should be followed to enhance
security:











All devices and hardware that are used to run production should be physical and located in the
Manufacturing Control Systems Network.
All devices with access to external non-secure networks or that can be accessed from external non-secure

networks should be placed in a Perimeter Network.
All devices that collect data from or provide input to Manufacturing Control Systems Networks, but that
could also be disconnected for a certain time, should be placed in a Manufacturing Operations Network.



When creating security cells, you should follow some common guidelines and implementation best practices, such

as:












A security cell is an independent part of the plant.
All participants inside the cell trust each other.
Access to the security cell is permitted only through clearly-defined access points.
Access points are monitored and access is logged (data traffic, user, hardware).
All participants of a security cell are directly connected (no bypass to the outside).
Participants with a high network load will be integrated into a security cell to avoid bottlenecks.


###### Example Configuration with Security Cells

Opcenter Reporting 2401.0001 - Installation Manual 13


_Before you Start_


_Security Strategies_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-13-0.png)

##### 1.3.1.2 Firewall and VPN


In order to grant network security, access points to security cells and communication between the different access
points have to be secured.

###### Access Points to Security Cells


It is a good practice to permit access to security cells only through clearly-defined access points: security cells
should have a single access point.
The access through access points is permitted only after having verified the legitimacy of the access request (people
and/or devices must be authenticated and authorized). Furthermore, it is advisable to log any access.
Access points should prevent unauthorized data traffic to security cells while permitting authorized traffic
necessary for smooth system operation. The access point to a security cell can be designed according to
configuration and functionality requirements.
A network in which all data traffic is protected by a firewall represents an example of a security cell with a security
access point.




###### Access Points: Configuration Example

14 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Security Strategies_


In the configuration example, the access points to the different security cells are protected by firewalls.
The tables below show:








The communication direction for the machine roles in the example scenario.
The communication protocols that have to be applied in order to guarantee network security.



These tables refer only to Opcenter Reporting connections; for other products refer to their specific documentation.

###### Communication between different Security Cells



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-14-0.png)




















|Blocked<br>(*)|→ (https)|Blocked<br>(*)|Blocked<br>(*)|
|---|---|---|---|
|Not Applicable<br>(**)|← (https)|Not<br>Applicable<br>(**)|Not<br>Applicable<br>(**)|





(*) Typically the direct communication to the server has been blocked.


(**) The involved machines belong to the same security cell.

###### Communication inside a Manufacturing Security Cell


In general, a firewall is not used within a security cell, but this schema can convey an idea on the communications
and corresponding protocols between the different system components.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-14-1.png)















(*) The involved machines belong to the same security cell.





You can configure the ports used by the different protocols, but the most commonly used ports are:


Opcenter Reporting 2401.0001 - Installation Manual 15


_Before you Start_


_Security Strategies_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-15-0.png)


##### 1.3.1.3 Secure Communication between Security Cells

In order to grant network security, the access points to security cells and the communication, among the various
access points, must be rendered secure. In this section, we are going to see how this goal can be reached.
In many cases, data exchange among components, that are located in different areas, is required for the correct
operation of a plant.
The following sections illustrate how to secure communication channels between the cells.

###### Secure communication between Enterprise and MES Security Cells


The communication between ERP (enterprise) level and MES level must be filtered by using a specific security cell,
known as perimeter cell, in order to decouple the plant network from the external network.
Opcenter Reporting communications are based on HTTP protocol: therefore, in order to grant a good level of
security, it is necessary to configure the HTTPS between the ERP cell and the perimeter cell, as well as the same
protocol between the perimeter cell and the MES security cell.
It is mandatory to configure the channels between:








The Enterprise Security Cell and the Perimeter Security Cell using SSL/TLS with a server certificate.
The Perimeter Security Cell to the MES security Cell using SSL/TLS with a server and client certificate.



To enable secure communication, it is necessary to create an HTTPS protocol binding on the site hosting Opcenter
Reporting and the Virtual directories, following the relative IIS procedure at http://www.iis.net/learn/manage/
configuring-security/how-to-set-up-ssl-on-iis.

###### Secure Communication between MES and Process and Control Security Cell


Communication between applications deployed in the MES Security Cell and the Process and Control Security Cell
must be established following the guidelines provided by back-end applications.
All information required on the Siemens Process and Control system can be found at http://w3.siemens.com/
mcms/automation/en/process-control-system/Pages/Default.aspx.

###### Additional notes on MES Security Cell communication


It is highly recommended that you deploy the components related to manufacturing on the same security cell.
Furthermore, it is advisable to apply additional countermeasures to increase communication security.





16 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Security Strategies_

###### Secure communication with data sources (only for data reading)


Opcenter Reporting can be configured to resolve data queries on multiple data sources. It may be necessary to
render the communication channel with these data sources secure, according to customer requirements.

###### Secure communication between Opcenter Reporting application server and an external system


All communication that makes it possible to join Opcenter Reporting applications deployed in the Manufacturing
network with other external systems must be based on either application secure protocols that guarantee the goals
of confidentiality/integrity or alternative secure solutions provided by your IT department (not contemplated in this
document).


In case Opcenter Reporting Clients are located in different geographic areas, it is necessary to properly setup and
configure a firewall between your network and the network where the clients are located. In this scenario, it is
recommended to use VPNs (Virtual Private Networks), to protect communications between the different plants
from external attacks.

#### 1.3.2 Overview of System Integrity


System Integrity is ensured by using automation systems and controller components that are protected against
unauthorized access and malware or meet special requirements, such as know-how protection.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-16-0.png)





At the following links, you can find some general indications on how to ensure system integrity.









System Hardening
Patch Management
Malware detection and prevention



Some security configurations related to group settings and file/directory permissions will be automatically applied
by the installation (that is, from the Security Controller step of the installation wizard).

###### Access Control on Files and Directories



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-16-1.png)







![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-16-2.png)







Opcenter Reporting 2401.0001 - Installation Manual 17


_Before you Start_


_Security Strategies_

##### 1.3.2.1 System Hardening


The term _hardening_ summarizes all those measures and settings that aim to:











Reduce opportunities to exploit vulnerabilities in software.
Minimize potential methods of attack.
Limit the tools available for a successful attack.
Minimize the available rights following a successful attack.
Increase the probability of detecting a successful attack.



This is intended to increase local security and the resilience of a computer to withstand attacks.
Consequently, a system can be described as "hardened" if:










The software components and services installed are limited to those that are required for the actual
operation.
Restrictive user management is implemented.
The local Windows Firewall is enabled and is restrictively configured.


###### System Hardening Recommendations

Before installing Opcenter Reporting, you must make your system safe by hardening:












The Computer BIOS.
The Operating System by:



[For more information, see Federal Office for Information Security website.](https://www.bsi.bund.de/EN/Home/home_node.html)


The databases used in your scenario. For Microsoft SQL Server databases, refer to https://
msdn.microsoft.com/en-us/library/bb283235.aspx and https://technet.microsoft.com/en-us/library/
bb510663(v=sql.110).aspx. It is recommended that you follow a maintenance plan. In addition, it is
recommended that you make back up your databases on a regular basis, to avoid critical data loss. For the
backup-restore procedure using Microsoft SQL Server, see: https://msdn.microsoft.com/en-us/library/
ms187048.aspx.
The file system (for example, by encrypting it).










Uninstalling programs and Windows components that are not required.
Disabling unnecessary services.
Using a whitelisting application to prevent the execution of unauthorized programs.
Making backups on a regular basis.



In addition, it is recommended that you remediate the following vulnerabilities:












Prevent Microsoft IIS Tilde Directory Enumeration
Disable the SSL v3 Protocol on IIS

Install the Windows Update to Disable RC4
Disable Debugging for ASP.NET
Remove Unwanted HTTP Response Headers
Prevent Version Disclosure ASP.NET


##### 1.3.2.1.1 Security Controller

The Security Controller (SeCon) is a program, integrated by default in User Management Component (UMC) that
configures application-specific security settings during the installation.
SeCon can automatically configure the following settings:










Group settings
Registry settings
Windows Firewall exceptions
DCOM settings



18 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Security Strategies_


   - File and/or directory permissions settings


These settings are configured depending on the installation (package selection).

##### 1.3.2.1.2 Preventing Microsoft IIS Tilde Directory Enumeration


It is possible to detect short names of files and directories which have an 8.3 file naming scheme equivalent in
Windows by using some vectors in several versions of Microsoft IIS. For instance, it is possible to detect all shortnames of ".aspx" files as they have 4 letters in their extensions. This can be a major issue especially for the .Net
websites which are vulnerable to direct URL access as an attacker can find important files and folders that are not
normally visible.

###### Recommended Action


[For more details, see: https://technet.microsoft.com/en-us/library/cc959352.aspx](https://technet.microsoft.com/en-us/library/cc959352.aspx)

##### 1.3.2.1.3 Disabling the SSL v3 Protocol on IIS


Some versions of Windows Server allow SSL 2.0 and SSL 3.0 by default. Unfortunately, these are insecure protocols.
Depending on how your Windows servers are configured, you may need to disable SSL v3.

###### Recommended Action


[For more details, see: https://docs.microsoft.com/en-us/security-updates/securityadvisories/2015/3009008](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2015/3009008)

##### 1.3.2.1.4 Installing Windows Update to Disable RC4


A Windows update is available to disable RC4. It is highly recommended that you download and install this update.

###### Recommended Action


[For more details, see: https://docs.microsoft.com/en-us/security-updates/securityadvisories/2013/2868725](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2013/2868725)

##### 1.3.2.1.5 Disable Debugging for ASP.NET


ASP.NET supports compiling applications in a special debug mode that facilitates developer troubleshooting. This
mode, however, may affect the application performance.

###### Recommended Action


It is recommended that you disable ASP.NET debugging before deploying a production application on the web

server.


For more details, see: https://support.microsoft.com/en-us/help/815157/how-to-disable-debugging-for-asp-netapplications

##### 1.3.2.1.6 Remove Unwanted HTTP Response Headers


The HTTP responses returned by the web application may include a header named Server. The value of this header
includes the version of Microsoft IIS server.

###### Recommended Action


Configure Microsoft IIS to remove unwanted HTTP response headers from the response. For more details,
[see: https://blogs.msdn.microsoft.com/varunm/2013/04/23/remove-unwanted-http-response-headers/](https://blogs.msdn.microsoft.com/varunm/2013/04/23/remove-unwanted-http-response-headers/)


Opcenter Reporting 2401.0001 - Installation Manual 19


_Before you Start_


_Security Strategies_

##### 1.3.2.1.7 Prevent Version Disclosure ASP.NET


The HTTP responses returned by the web application may include a header named X-AspNet-Version.

###### Recommended Action


Apply needed changes to the web.config file to prevent information leakage. For more details, see: https://
msdn.microsoft.com/en-us/library/system.web.configuration.httpruntimesection.enableversionheader.aspx

##### 1.3.2.2 Patch Management


In general, office PC systems are protected against malware. Any weak points that are discovered in the operating
system or in the user software must be eliminated by installing updates and patches. Likewise, industrial PCs and
PC-based control systems in the plant network require corresponding protective measures.
Systems should be updated and patched on a regular basis to address potential security risks and known exploits.
To accomplish this, Microsoft removes security gaps in its products and provides these corrections to its customers
via official updates/patches.
To ensure secure and stable operation in Opcenter Reporting, the installation of "Security patches" and "Critical
patches" is recommended. Siemens will provide customer support only if these updates have been installed and
solely for problems that are unrelated to such updates.
You can find information on Microsoft updates and the Windows Server Update Services (WSUS) on the following
Microsoft pages:








[http://technet.microsoft.com/en-us/](http://technet.microsoft.com/en-us/)
[http://www.microsoft.com/wsus](http://www.microsoft.com/wsus)



The support for implementing patch management in your system is available from the Industrial Security Services.
You can find additional information and the corresponding contacts at http://www.industry.siemens.com/topics/
global/en/industrial-security/Pages/default.aspx.

##### 1.3.2.3 Malware Detection and Prevention


This section focuses on protecting the automation system and its computers against malicious software. Malicious
software and malicious programs (malware) refer to computer programs that have been developed to execute
undesirable and possible damaging functions. There are various types of malware available:










computer viruses
computer worms
trojan horses
other potentially-dangerous programs, such as:











backdoor

spyware
adware

scareware

grayware



A virus scanner or antivirus program is a software that detects, blocks and, if necessary, removes malware.
The use of a virus scanner on the computers of an automation plant must not interfere with the plant's process
mode. The following two examples illustrate two situations which may arise on a production system where a virus
scanner is used:









Even when infected with malware, a computer might not be switched off by a virus scanner, this could then
lead to losing control of the production system (for example, for an OS server).
A project file "infected" by malware (for example, a database archive) might not be automatically moved to
quarantine, blocked or deleted.



20 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Preliminary Configurations_



It is advisable to use a virus scanner with server-client configuration where:









the virus scanner server is a computer that centrally manages virus scan clients, downloads virus signature
files (virus patterns) from the virus scanner vendor sites and distributes them to the virus scanner clients;
the virus scanner client is a computer that is checked for malware and managed by the virus scanner server.



In accordance with the rules for distributing components into security cells, the virus scanner server must be
singled out in a separate network (Perimeter network / DMZ).




### 1.4 Preliminary Configurations

Before installing Opcenter Reporting, you should perform a number of preliminary steps:














Install the License Server if it is not installed on your environment yet.
Install the User Management Component (UMC) if it is not already installed on your environment. You can
also install UMC during Opcenter Reporting setup.
After UMC has been installed and before running Opcenter Reporting, you must configure UMC. For
instructions on how to execute this operation, see _UMC documentation_ .
(o _nly if you want to use Oracle database management system_ ) Install Oracle following some specific
requirements: version 19c - versions previous to 19c.
Configure IIS and ASP.NET settings




#### 1.4.1 Installing the License Server

Starting from version 2307, Opcenter Intelligence is migrating to Siemens Advanced Licensing Technology (SALT).


The License Server should be installed before installing Opcenter Reporting, either on an Opcenter Reporting
machine or on a separate machine where Opcenter Reporting is not installed.

###### Installation File and Documentation


The installation file and documentation manuals are available on Support Center at the link https://
support.sw.siemens.com/en-US/product/1586485382/downloads


Siemens License Server installation and usage are documented in the following manuals:









_Siemens Digital Industries Software License Server Installation Instructions_
( **sw_siemens_license_server_install.pdf** )
_Siemens Digital Industries Software Licensing Manual for PLM Products_ ( **sw_siemens_licensing_plm.pdf** )


###### Prerequisites

You have obtained a valid license file.

###### Procedure



1.

2.



Save the license file (with .lic extension) in a directory accessible to the license server host.
Download the Siemens License Server installation file from Support Center.



Opcenter Reporting 2401.0001 - Installation Manual 21


_Before you Start_


_Preliminary Configurations_



3.

4.

5.


6.



Copy the file to a temporary directory on your local hard drive.
Launch the setup program.
Follow the instructions contained in the _Siemens Digital Industries Software License Server Installation_
_Instructions_ manual.
In particular, do the following:









provide the location of the license file. If you are upgrading from a previous version of the product,
you do not need a new license file, you can use the same license file you used for the previous
version;
configure the correct port:




         
if you are installing the product for the first time, leave the license server default port (29000);


         
if you are upgrading from a previous version of the product, you may want to keep the
previously configured port number. For more details, see _Opcenter Intelligence Installation_
_Manual_ ;


    
specify a destination folder for the installation;

    - select the **I don't want this feature** check box.


Click **Done** to quit the installer.









      
      
7. Click




#### 1.4.2 Checking Oracle 19c Installation Requirements

For details on Oracle installation, please refer to _Oracle official documentation_ .


Starting from Opcenter Reporting 3.3, ODAC 19c is also supported.


When you install and configure Oracle, you must make sure to select the **Oracle Data Provider for .NET**
**component** check box during installation.

###### Installing Oracle using a Private Configuration


This is an example on how to install Oracle using a private configuration using version 19.3.1.0:



1.

2.


3.

4.

5.

6.


7.

8.



Install **ODT** with **ODAC 19.3.1.0** on the same machine where Opcenter Reportingis running.
In the **C:\app\client\Administrator\product\19.0.0\client_1\odp.net\managed\x64** folder, select
**configure.bat** .
Open the command prompt as Administrator.
Type **cd** C:\app\client\Administrator\product\19.0.0\client_1\odp.net\managed\x64
Launch the **configure.bat** file.
In **C:\app\client\Administrator\product\19.0.0\client_1\odp.net\managed\common\** copy the
**Oracle.ManagedDataAccess.dll** file.
Paste it to **C:\Program Files\Siemens\Opcenter\Intelligence\Report\Server\bin\**
Modify the **Web.config** file that you can find in **C:\Program**
**Files\Siemens\Opcenter\Intelligence\Report\Server\** adding the following nodes:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-21-1.png)



22 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Preliminary Configurations_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-22-0.png)



The resulting **web.config** file should look as in this example:


Opcenter Reporting 2401.0001 - Installation Manual 23


_Before you Start_


_Preliminary Configurations_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-23-0.png)


24 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Preliminary Configurations_



9.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-24-0.png)

Run **IISRESET** from the command prompt.




#### 1.4.3 Checking Oracle Installation Requirements (versions previous to 19c)

For details on Oracle installation, please refer to _Oracle official documentation_ .


Starting from Opcenter Reporting 3.2 Update1, ODAC 18 is also supported.


When you install and configure Oracle, you must make sure that the following requirements are met:








During installation, select the **Oracle Data Provider for .NET component** check box.
In the **ODP.NET** step of the installation, select the **Configure ODP.NET and/or Oracle Providers for**
**ASP.NET at machine-wide level** check box. The machine-wide configuration may cause other applications
to stop working. If that is the case, please refer to _Oracle documentation_ .
To overcome this issue, you can execute the following procedure, which is an example on how to install
Oracle using a private configuration using version 12.2.010.


###### Installing Oracle using a Private Configuration

If the machine-wide configuration is not a suitable option, you can install Opcenter Reporting using a private
configuration. To do so, perform the following procedure:



1.

2.


3.

4.

5.

6.


7.

8.



Install **ODT** with **ODAC 12.2.010** .
In the **C:\app\client\Administrator\product\12.2.0\client_1\odp.net\managed\x64** folder, select
**configure.bat** .
Open the command prompt as Administrator.
Type **cd** C:\app\client\Administrator\product\12.2.0\client_1\odp.net\managed\x64
Launch the **configure.bat** file.
In **C:\app\client\Administrator\product\12.2.0\client_1\odp.net\managed\common\** copy the
**Oracle.ManagedDataAccess.dll** file.
Paste it to **C:\Program Files\Siemens\Opcenter\Intelligence\Report\Server\bin\**
Modify the **Web.config** file that you can find in **C:\Program**
**Files\Siemens\Opcenter\Intelligence\Report\Server\** adding the following nodes:



Opcenter Reporting 2401.0001 - Installation Manual 25


_Before you Start_


_Preliminary Configurations_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-25-0.png)



9.



The resulting **web.config** file should look as in this example:

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-25-1.png)


Run **IISRESET** from the command prompt.





26 Opcenter Reporting 2401.0001 - Installation Manual


_Before you Start_


_Preliminary Configurations_

#### 1.4.4 Configuring IIS and ASP.NET Role Services


Once you have installed Internet Information Services, ASP.NET Module and IIS Roles and Features must be enabled
manually.




###### Procedure



1.

2.

3.

4.



Select: **Start > Administrative Tools > Server Manager** .
Select the **Manage > Add Roles and Features** command.
Under **Roles** install the following options.
Under **Features** install the following options.


##### 1.4.4.1 Roles



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-26-1.png)





Opcenter Reporting 2401.0001 - Installation Manual 27


_Before you Start_


_Preliminary Configurations_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-27-0.png)
_Before you Start_


_Preliminary Configurations_


##### 1.4.4.2 Features



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-28-0.png)





Opcenter Reporting 2401.0001 - Installation Manual 29


_Before you Start_


_Preliminary Configurations_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-29-0.png)


30 Opcenter Reporting 2401.0001 - Installation Manual


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting Interactively_

## 2 How to Install Opcenter Reporting


You can install Opcenter Reporting either by launching the installation file from the ISO folder or via Command Line.

###### Available Operations








Install Opcenter Reporting Interactively
Install Opcenter Reporting via Command Line


### 2.1 Installing Opcenter Reporting Interactively

###### Prerequisites

Verify that all prerequisites required by Opcenter Reporting are satisfied.

###### Where to find Opcenter Reporting Installation Folder


The **OpcenterReport** folder, which contains Opcenter Reporting installation files, is a subfolder of the **Opcenter**
**Intelligence** ISO root folder.


The path of the **Start.exe** file to be launched is: **\OpcenterReport\Start.exe**



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-30-2.png)



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-30-0.png)

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-30-1.png)
###### Procedure

Opcenter Reporting 2401.0001 - Installation Manual 31


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting Interactively_



1.


2.



Execute the **Start.exe** program located in the **OpcenterReport** folder and click **Next** .

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-31-0.png)


Select which product features you want to install and click **Next** .



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-31-1.png)





32 Opcenter Reporting 2401.0001 - Installation Manual


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting Interactively_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-32-0.png)


Opcenter Reporting 2401.0001 - Installation Manual 33


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting Interactively_


3. Accept the conditions of the license agreement and confirm the security information. **Open Source and**

**Third-Party Licenses** are selected by default. Then click **Next** .

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-33-0.png)


34 Opcenter Reporting 2401.0001 - Installation Manual


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting Interactively_


4. Accept the security and permissions settings on your computer. Click **Next** .

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-34-0.png)


Opcenter Reporting 2401.0001 - Installation Manual 35


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting via Command Line_



5.


6.



Check the **Overview** summary and click **Install** .

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-35-0.png)


When the setup is completed successfully, click **Finish** .


### 2.2 Installing Opcenter Reporting via Command Line

Opcenter Reporting allows you to install the product via command line. In this page you can find a description of
the operations to be executed when you are installing the system from scratch.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-35-1.png)




##### Prerequisites










Verify that all prerequisites required by Opcenter Reporting are satisfied.
Hardware and software of the programming device or PC meet the system requirements.
You have administrator privileges on your computer.
All running programs are closed.


###### Procedure

To start the installation with the desired options directly via the command interface, proceed as follows:



1.

2.



Open the Windows command prompt with **Start > Run > cmd** .
Switch to the directory that contains the **Start.exe** file.



36 Opcenter Reporting 2401.0001 - Installation Manual


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting via Command Line_



3.


4.



In the command prompt, enter one of the following commands:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-36-0.png)

Press the < **Return** - key to confirm your entry.








Installation with visible installation information: **Start.exe /qb <** _**Parameter**_ **>**
Installation without visible installation information: **Start.exe /qn <** _**Parameter**_ **>** or **Start.exe /silent**

**<** _**Parameter**_ **>**







![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-36-1.png)




###### Examples

See some examples of automated installation via the command line

###### Available Information








Parameters for Automated Installation

Return Values from the Installation Process


#### 2.2.1 Examples of Automated Installation via the Command Line

###### Example of a typical installation with REBOOT=AUTO

The following example shows a typical installation via the command line:





At the end of the installation, the system is restarted automatically without the request for a confirmation
("REBOOT=Auto").

###### Example of a complete installation with REBOOT=Suppress


The following example shows a complete installation via the command line:





At the end of the installation, restart of the system is suppressed ("REBOOT=Suppress"). This means that you must
evaluate the return value yourself and possibly restart the system manually.

###### Example of querying the return value per batch file


The following example shows you how to query the return value per batch file:


SET SetupSuccess=%ERRORLEVEL%


Opcenter Reporting 2401.0001 - Installation Manual 37


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting via Command Line_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-37-0.png)



The return code "1641" also documents successful completion of the installation and that restart has already been
initiated. Restart occurs, however, only if "/REBOOT=Auto" is used and for this reason was not evaluated in the
batch file. You can find all possible return values under Return Values from the Installation Process.

#### 2.2.2 Parameters for Automated Installation


The following table shows the parameters available for an automated installation:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-37-1.png)

















38 Opcenter Reporting 2401.0001 - Installation Manual


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting via Command Line_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-38-0.png)











1 Installation with the **/qb** or **/qn** parameters has the effect that no alarm windows are displayed, even if an error
occurs. You can only evaluate the results via the return value.


2 If the installation is not yet finished (return value 13010), you first need to restart the system and then the
installation in order to make evaluation of the return value possible.

#### 2.2.3 Return Values from the Installation Process


The following table shows the return values from an automated installation along with their descriptions:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-38-1.png)



Opcenter Reporting 2401.0001 - Installation Manual 39


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting via Command Line_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-39-0.png)



40 Opcenter Reporting 2401.0001 - Installation Manual


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting via Command Line_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-40-0.png)








#### 2.2.4 Customizing the Installation

If you want to customize your installation, you can save your choice using the recording functionality.

###### Prerequisites









Hardware and software of the programming device or PC meet the system requirements.
You have administrator privileges on your computer.
All running programs are closed.



Opcenter Reporting 2401.0001 - Installation Manual 41


_How to Install Opcenter Reporting_


_Installing Opcenter Reporting via Command Line_







To play the recording, the previously recorded file ("*.rec") must be present.


###### Workflow

To do so, you can execute the following operations:



1.

2.



Start Recording
Play the Recording


###### Starting Recording

To record the installation, proceed as follows:



1.

2.

3.

4.



Open the Windows command prompt with **Start > Run > cmd** .
Switch to the directory that contains the **Start.exe** file.
In the command prompt, enter the following command: **Start.exe /record**
Press the < **Return** - key to confirm your entry.


###### Result

The installation dialog opens with the information that you are in Record mode and the system will not be changed.
During the recording operation, a configuration file is generated, which can be played in the next step.

###### Playing the Recording


To play the installation, proceed as follows:



1.

2.

3.


4.



Open the Windows command prompt with **Start > Run > cmd** .
Switch to the directory that contains the **Start.exe** file.
In the command prompt, enter the following command:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-41-0.png)

Press the < **Return** - key to confirm your entry.






###### Result

Installation takes place automatically using the settings recorded in the configuration file.


42 Opcenter Reporting 2401.0001 - Installation Manual


_How to Configure Opcenter Reporting_


_Summary of Port Numbers required for Opcenter Reporting Configuration_

## 3 How to Configure Opcenter Reporting


After installing Opcenter Reporting, you must perform a number of operations before accessing the working
environment.


To help you set the configuration, at this link you can find a schema of TCP/UDP ports to be opened on Opcenter
Reporting server.

###### Workflow



1.

2.

3.



(Optional) Create the UMC user who will be used as Administrator for Opcenter Reporting.
Configure Opcenter Reporting Interactively with Opcenter Reporting Configurator
Perform Additional Configuration Operations


###### Additional Configurations









Configure Opcenter Reporting via Command Line
Integrate Opcenter Reporting with other products
Configure Microsoft ARR as Reverse Proxy


###### Backup Strategy

To prevent data loss if an incident occurs (for example a malware infection or storage device failure), an
appropriate backup strategy is highly recommended. Database backup has to be planned to save Opcenter
Reporting database, in particular because it stores the reports you have created. A regular backup of the
**ProgramData\Siemens\Opcenter\Intelligence\Report\Server\App_Data\** folder is therefore strongly
recommended.

### 3.1 Summary of Port Numbers required for Opcenter Reporting Configuration


The following schema summarizes the TCP/UDP ports to be opened on Opcenter Reporting server.


Opcenter Reporting 2401.0001 - Installation Manual 43


_How to Configure Opcenter Reporting_


_Creating Opcenter Reporting Users in UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-43-0.png)

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-43-1.png)




### 3.2 Creating Opcenter Reporting Users in UMC

You can skip this procedure if User Management Component has already been installed and configured on your
machine and you have already created one or more users in UMC.
If, on the contrary, you have installed UMC during Opcenter Reporting installation, you must previously configure
UMC (see the _How to Configure UMC_ chapter in _UMC Installation Manual_ ) and then follow this procedure.

###### Procedure



1.



From a supported browser, access UMC by entering one of the following addresses depending on the
configuration:




         
http://< _FullComputerName_ >/UMC


         
https://< _FullComputerName_ >/UMC

2. Log in with the UMC user who owns the permissions to create other users or groups.
3. In UMC **Users** page, add the user who will be the Administrator for Opcenter Reporting.

### 3.3 Configuring Opcenter Reporting Interactively with Opcenter Reporting Configurator


Opcenter Reporting is the stand-alone application that performs the post-setup configuration actions. The
Configurator can be run more than once if you want to change your settings after the first configuration.


44 Opcenter Reporting 2401.0001 - Installation Manual


_How to Configure Opcenter Reporting_


_Configuring Opcenter Reporting Interactively with Opcenter Reporting Configurator_


###### Procedure



1.

2.


3.


4.

5.


6.



Double-click the desktop icon to run the Opcenter Reporting.
Insert the required information as explained in the tables below. The fields marked with an asterisk are
mandatory.
When you have completed the configuration, click **Apply** and wait for the popup that confirms the successful
completion of the configuration.
Click **Close** .
To ensure that UMC functions correctly, add the following URL to UMC whitelist: **http(s)://<machine**
**name>/opcenterrp/Login/Login** . For more details, see _Create a Whitelist Entry_ in _UMCONF User Manual_ .
Restart IIS Application Pool.





![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-44-1.png)
###### Current Configuration

The **Current Configuration** area shows a summary of the settings you have previously applied.

###### User Management Component (UMC) Configuration


Opcenter Reporting 2401.0001 - Installation Manual 45


_How to Configure Opcenter Reporting_


_Configuring Opcenter Reporting Interactively with Opcenter Reporting Configurator_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-45-0.png)






###### License Server Configuration



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-45-1.png)


###### OpenAPI

OpenAPI Specification (formerly Swagger Specification) is an API description format for REST APIs.


Enable or disable **OpenAPI** by selecting the corresponding radio button.

###### Log Level


The Configurator log file is called **Siemens.OpcenterRP.PostSetup.log** and can be found in **Program**
**Files\Siemens\Opcenter\Intelligence\Report\Setup\**


Each log entry has a level and each logger is configured to include or ignore certain levels. In this section you can
specify the minimum level where that level and higher levels are included. For example, if the minimum level is Info,
then Info, Warning and Error are logged, but Debug and Trace are ignored.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-45-2.png)







46 Opcenter Reporting 2401.0001 - Installation Manual


_How to Configure Opcenter Reporting_


_Configuring Opcenter Reporting via Command Line_

### 3.4 Configuring Opcenter Reporting via Command Line


Opcenter Reporting allows you to customize the configuration via command line. In this page you can find a
description of the commands and a list of the operations to be executed in the described order when you are
installing and configuring the system from scratch or after an update.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-46-0.png)




###### Prerequisites

Verify that all prerequisites required by Opcenter Reporting are satisfied.

###### Procedure



1.

2.

3.



Open the **Command Prompt** with administrative privileges.
Move to **C:\Program Files\Siemens\Opcenter\Intelligence\Report\Setup\**
Run the following command line. In the next paragraphs you can find details on the configuration of the
different parameters.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-46-1.png)


###### UMC Configuration

Use the command line to specify the UMC URL.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-46-2.png)


###### Opcenter Reporting Administrator Configuration





Opcenter Reporting 2401.0001 - Installation Manual 47


_How to Configure Opcenter Reporting_


_Configuring Opcenter Reporting via Command Line_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-47-0.png)

##### License Server Configuration



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-47-1.png)






###### Sample



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-47-2.png)


###### Error Codes

The following error codes may be returned:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-47-3.png)





48 Opcenter Reporting 2401.0001 - Installation Manual


_How to Configure Opcenter Reporting_


_Performing Additional Configuration Operations_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-48-0.png)


###### Log File

A log file named **Siemens.OpcenterRP.PostSetup.log** is available in **C:\Program**
**Files\Siemens\Opcenter\Intelligence\Report\Setup\**

### 3.5 Performing Additional Configuration Operations


Perform the following operations to complete the configuration of Opcenter Reporting:









(Optional) Configure IIS Application Pool
(Optional) Configure https Protocol
Check Authentication Keys in IIS


###### Configuring IIS Application Pool to use Windows Authentication

Opcenter Reporting setup installs a default application and an IIS application pool named **opcenterrpPool** . The
user must be granted read access to SQL Server in order to use Windows Authentication to access the DB. To do so,
click on **Application Pool Identity** and insert a domain service user that can run also in remote SQL Server
machine.

###### Configuring https Protocol for Opcenter Reporting


To configure the https protocol for **opcenterrp** (application contained in IIS Default Web Site), refer to _Microsoft_
_Internet Information Services (IIS) documentation_ for instructions on how to configure a certificate on the web site.

###### Checking Authentication Keys in IIS


In IIS, follow this procedure to verify if authentication keys have been set correctly.



1.

2.

3.



In **IIS Manager > Sites > Default Web Site**, select **opcenterrp** .
Double-click **Authentication** from the area on the right.
Check that only the two following keys have been set to **Enabled** . The other keys must be set to **Disabled** .




         
**Anonymous Authentication**

         - **Forms Authentication**
4. Run **IISRESET** from the command prompt.

### 3.6 How to Configure Microsoft ARR as Reverse Proxy


These guidelines deal with Microsoft Application Request Routing (ARR) used as a reverse proxy. This application
has been officially tested: however we are not aware of any problems in using other reverse proxy/load balancing
applications, provided that they support the WebSocket protocol.







Opcenter Reporting 2401.0001 - Installation Manual 49


_How to Configure Opcenter Reporting_


_How to Configure Microsoft ARR as Reverse Proxy_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-49-0.png)


ARR exposes a unique URL that web clients use for sending and receiving requests and redirects these requests to
Opcenter Reporting and UMC hosts. Consequently web clients only need to know the ARR server to which they must

connect.


These pages describe the procedures to be followed to create a basic configuration of load balancing using
Microsoft Application Request Routing (ARR) when Opcenter Reporting is running in a DMZ network.
If you want to configure ARR in HTTPS, you must first configure Opcenter Reporting and UMC in HTTPS and then
follow the procedures to configure ARR described in these pages.

###### User Management Component Limitation


To properly configure the reverse proxy to use multiple web servers, you must increase the value of the query string
length on all web servers via IIS Manager. For more information, see _High Availability/Reliability General Issues_ in
_UMC Installation Manual_ .

###### Prerequisites











The host containing ARR is a separate host that must not contain Opcenter Reporting.
Microsoft ARR add-on is installed on IIS.
You have applied the basic endpoint configuration, which is the default in Opcenter Reporting.
If you do not configure ARR in High Availability, the host containing ARR must never be shut down.
If you want to use ARR and the entire environment using HTTPS:




         

         
###### Workflow



you must have modified the ARR default site binding and assigned a valid certificate as documented
on _Microsoft documentation_ ;
you must have configured Opcenter Reporting in HTTPS.





1.

2.

3.

4.

5.

6.

7.



Create the web farms
Configure the redirection rules
Configure the redirection rule order
Increase the default proxy timeout
Configure the maximum allowed content length for file processing
Set the recycle time to zero
Configure the connection from web clients


#### 3.6.1 Creating the Web Farms

In this step of the ARR Load Balancer configuration, you are creating the web farms and assigning the servers of
the Opcenter Reporting environment.

###### Procedure



1.



In **IIS Manager**, under **Server Farms**, create the following web farm for Opcenter Reporting:



50 Opcenter Reporting 2401.0001 - Installation Manual


_How to Configure Opcenter Reporting_


_How to Configure Microsoft ARR as Reverse Proxy_



2.


3.

4.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-50-0.png)

If the UMC web farm has not already been created and configured in another product (for example Opcenter
EX FN), create it and insert the following values:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-50-1.png)

Click **Finish** .

Click **No** to the **Rewrite Rules** request that appears.




#### 3.6.2 Configuring the Redirection Rules

In this step of the ARR Load Balancer configuration, you are configuring the rules to redirect the incoming requests
to the required farm.

###### Procedure





1.

2.

3.

4.

5.



In **IIS Manager**, select the root node.
Double-click the **URL Rewrite** option.
In the **Actions** panel, click **Add Rule(s)** **…**
Select the **Blank rule** template and click **OK** .
Create a rule by entering the parameters shown in the following table.


|Section|Parameter|Value|
|---|---|---|
||**Name**|ARR_REPORTING_SVC|
|**Match URL**|**Requested URL**|Matches the Pattern|
|**Match URL**|**Using**|Regular Expression|



Opcenter Reporting 2401.0001 - Installation Manual 51


_How to Configure Opcenter Reporting_


_How to Configure Microsoft ARR as Reverse Proxy_






|Section|Parameter|Value|
|---|---|---|
||**Pattern**|.*|
||**Ignore case**|checked|
|**Conditions**|**Logical Grouping**|Match any|
|**Conditions**|**Condition input**|{R:0}|
|**Conditions**|**Check if input string:**|Matches the Pattern|
|**Conditions**|**Pattern**|^opcenterrp|
|**Action**|**Action Type**|Route to Server Farm|
|**Action**|**Action Properties**|URL: https://reporting_svc/{R:0}|
|**Action**|**Append query string**|checked|
|**Action**|**Stop processing of subsequent**<br>**rules**|checked|



6.

7.

8.



Click **Apply** .
Click **Back to Rules** .
Repeat steps 2 to 5 to create the second rule for UMC if it has not been already created and configured for
another product.





![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-51-1.png)

|Parameter|Value|
|---|---|
|**Name**|ARR_UMC_SVC|
|**Requested URL**|Matches the Pattern|
|**Using**|Regular Expression|
|**Pattern**|.*|
|**Ignore case**|checked|


52 Opcenter Reporting 2401.0001 - Installation Manual


_How to Configure Opcenter Reporting_


_How to Configure Microsoft ARR as Reverse Proxy_






|Section|Parameter|Value|
|---|---|---|
|**Conditions**|**Logical Groupings**|Match Any|
|**Conditions**|**Condition input**|{R:0}|
|**Conditions**|**Check if input string:**|Matches the Pattern|
|**Conditions**|**Pattern**|^UMC<br>^umc-idp<br>^umc-sso|
|**Action**|**Action Type**|Route to Server Farm|
|**Action**|**Action Properties**|**Scheme**: _http://_ or_https://_|
|**Action**|**Action Properties**|**Server Farm**: UMC_SVC|
|**Action**|**Action Properties**|**Path**: /{R:0}|
|**Action**|**Stop processing of subsequent**<br>**rules**|checked|



9.



Click **Apply** and **Back to Rules** .


#### 3.6.3 Configuring the Redirection Rule Order

In this step of the ARR Load Balancer configuration, you are configuring the execution order of redirection rules.

###### Procedure



1.



In the **URL Rewrite** configuration environment, set the correct order for the rules, which must be:




         - **REPORTING_SVC**

         - **UMC_SVC**
2. To change the order, select a rule and in the **Actions** panel use the **Move Up** or **Move Down** commands.

#### 3.6.4 Increasing the Default Proxy Timeout


In this step of the ARR Load Balancer configuration, you must increase the default proxy timeout for all web farms.

###### Procedure



1.

2.

3.

4.



Select a web farm.

In the **Server Farm** pane, click **Proxy** .
In the **Timeout** (in seconds) edit box, type 10000 (instead of 30).
Select the **Reverse rewrite host in response headers** check box.



Opcenter Reporting 2401.0001 - Installation Manual 53


_How to Configure Opcenter Reporting_


_How to Configure Microsoft ARR as Reverse Proxy_



5.

6.



Click **Apply** .
Repeat steps 1 to 5 for each web farm.


#### 3.6.5 Configuring the Maximum Content Length Allowed for File Processing

In this step the ARR Load Balancer configuration, you must increase the default value for the maximum content
length allowed to allow the processing of data files with a large amount of data. By default, the limit is set to 30 MB
and you can manually modify it as follows:

###### Procedure



1.

2.

3.


4.



In the **Machine Name** pane, click **Request Filtering** .
Click the **Edit Feature** settings action link.
Set the value of the **Maximum allowed content length (bytes)** edit box according to your requirements (we
suggest a value greater than 200 MB).
Click **OK** to apply the configuration.


#### 3.6.6 Setting the Recycle Time to Zero

The recycle time of the Application Pool is set by default to 1740 minutes. When the Application Pool is recycled, all
active connections (including client-side websockets) are automatically closed. Since the Signal Manager sends
information via websocket connections, which are automatically closed after recycling and not reopened, the
recycle option may cause data loss.


To solve this problem, you must set the recycle time to zero as follows:

###### Procedure



1.

2.

3.

4.



In the **Connections** pane, select the **Application Pools** node and select the default application pool.
In the **Actions** pane, click **Recycling** .
Set the **Regular time interval (minutes)** parameter to zero, complete the wizard and save changes.
Restart IIS.


#### 3.6.7 Configuring the Connection from Web Clients

To correctly connect from the web clients to Opcenter Reporting hosts using the ARR reverse proxy, some web
browser versions need to use an FQDN name (i.e. they must contain a dot character in the URL) to make the client
affinity work properly. As a best practice we suggest that you use a DNS record for the ARR host that should be
visible from all web clients.


54 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_

## 4 How to Integrate Opcenter Reporting with other Products


If you need to embed reports in your application, you can authenticate and perform some operations in Opcenter
Reporting by applying the code provided in the following chapters.


The authentication required before the embedding operations can be done using the User Management
Component (UMC) or not.








Products not supporting UMC
Products supporting UMC


###### Additional Options

Execute a Report and Save it as PDF without User Interaction

### 4.1 How to Integrate Opcenter Reporting with Products not supporting UMC


In this scenario Opcenter Reporting trusts users of the application you want to integrate. The permissions required
to authorize users remain unchanged.
The following workflow needs to be executed each time you want to access the Opcenter Reporting application by
means of a one-time authorization code to be obtained after the generation of private and public RSA keys.

###### Workflow



1.

2.



Generate Public and Private RSA Keys
Get the One-Time Authorization Code to perform the following operations:










Get Reports from Opcenter Reporting
Embed Reports
Provide Values for Report Parameters
Release a Seat after Report Visualization


#### 4.1.1 Generating Public and Private RSA Keys

The first step to integrate Opcenter Reporting with other products is to generate public and private RSA keys.


The private key will need to be moved to the external system, while the public key will be moved to the Opcenter
Reporting machine. As a result, the external user will be able to authenticate into Opcenter Reporting.




###### Procedure



1.


2.



Run the **Digital Signature Generator** Console Application
( **Siemens.OpcenterRP.DigitalSignatureGenerator.exe** ) contained in the folder: **Program**
**Files\Siemens\Opcenter\Intelligence\Report\Setup\**
To generate a public and a private key, follow the instructions prompted by the application and provide the
following details:



Opcenter Reporting 2401.0001 - Installation Manual 55


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-55-0.png)









3.


4.

5.



The keys are generated in the following folder:
**ProgramData\Siemens\Opcenter\Intelligence\Report\DigitalSignatureGenerator** . The keys format will
be: **Realm-Scenario-** _**Public/Private**_ **-Key-Timestamp.xml** where the **Timestamp** field is a record of the time
of key generation, for example: _20190905-132018907_ .
Move the private key to the system you want to integrate with Opcenter Reporting.
Move the public key to the following folder:
**ProgramData\Siemens\Opcenter\Intelligence\Report\Server\App_Data\PKRepository\**


#### 4.1.2 Getting the One-Time Authorization Code

A one-time authorization code (OTC) is a code that is valid to authenticate the user identity for only one session. For
example, a web application can use an OTC to securely authenticate in Opcenter Reporting.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-55-1.png)







The following "usings" are required for the next code block:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-55-2.png)



56 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_


The following method is an example to get the one-time code:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-56-0.png)


###### Helper Methods

The following "usings" are required for the next code block:


Opcenter Reporting 2401.0001 - Installation Manual 57


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-57-0.png)



The following methods are used by the one-time code:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-57-1.png)



58 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-58-0.png)


#### 4.1.3 Getting Reports from Opcenter Reporting

The following example shows how to retrieve a report list through a call to the Opcenter Reporting Web API using
the one-time code.

###### Prerequisites


You have obtained a one-time authorization code.

###### GetJsonReportList Method





The following "usings" are required for the next code block:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-58-2.png)



This method is an example of how to use the OneTimeCode to call the Web API. In this particular example, the
method returns the list of reports.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-58-3.png)


###### Example of Return Values

Opcenter Reporting 2401.0001 - Installation Manual 59


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-59-0.png)








#### 4.1.4 Embedding Reports

###### Prerequisites

You have obtained a one-time authorization code.

###### Procedure


The following code can be used as an example to embed in a page of your application the reports in ASP.NET MVC
created in Opcenter Reporting.




###### ASP.NET MVC

You must insert this **iframe** tag in the View where you want to display the report:





60 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-60-0.png)



This method sets the URL of the frame specified in the **src** attributes of the above tag.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-60-1.png)


###### AngularJS + ASP.NET Web API

This method returns the URL required by the **src** attribute of the < **iframe** - tag.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-60-2.png)



The URL is retrieved by the HTTP method, for example:


Opcenter Reporting 2401.0001 - Installation Manual 61


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-61-0.png)



Once the URL has been returned, it must be processed as follows in order to make it work in the **iframe** and
generate a contextual reload:

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-61-1.png)


where **$sce** must be injected into the controller:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-61-2.png)



The HTML code of the **iframe**, must be as follows in the view:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-61-3.png)




#### 4.1.5 Providing Values for Report Parameters

In Opcenter Reporting you can create reports with specific parameters and open these reports from a hosting
application by providing the values to be used for such parameters.

###### Prerequisites








You have obtained a one-time authorization code.
You have created and saved a report in Combit® List & Label Designer and configured the following settings:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-61-4.png)

62 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-62-0.png)


###### Procedure

Call the following URL to which you have previously added the required parameters:


https://[FQDN]/opcenterrp/Reports/HTML5Viewer?otc=[ _OTCCODE_ ]&reportRepositoryID=repository://{[ _cbID_ ]}
&reportParams=[ _URLencoded keypair value separated by &_ ]



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-62-1.png)








###### Example



1.



Create a report that contains the parameters:









**@EmployeeID**
**@City**
**@BirthDate**



Opcenter Reporting 2401.0001 - Installation Manual 63


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products not supporting UMC_



2.

3.


4.



In the List & Label Designer, set the visibility of these parameters to **False** .
Encode the **reportParams** parameter as in this example. The **reportParams** string must be encoded before
calling the controller action.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-63-0.png)

Call the URL of the API:

https://FQDN/opcenterrp/Reports/HTML5Viewer?otc=5FD97E21-CCF5-4A04-8A6EE7D6ECCE6883&reportRepositoryID=repository://{D65A3C2E-A166-40CB-B503-42B9177496DF}
&reportParams=%40EmployeeID%3d0%26%40City%3dSeattle%26%40BirthDate%3d1958-09-01T00%3a00
%3a00Z





![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-63-1.png)






#### 4.1.6 Releasing a Seat after Report Visualization

The following example shows how to release a seat for a specific user before the session expiration time (120
minutes) through a call to the Opcenter Reporting Web API using the one-time code.

###### Prerequisites


You have obtained a one-time authorization code.

###### logoutFromReporting Method





The following "usings" are required for the next code block:



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-63-3.png)



This method is an example of how to use the OneTimeCode to call the Web API. In this particular example, the
method releases the seats for one or all the browsers listed in the enum for a specific user (All = 4 releases all the
seats for all browsers for a specific user).



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-63-4.png)



64 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-64-0.png)


### 4.2 How to Integrate Opcenter Reporting with Products supporting UMC

A product that uses the User Management Component (UMC) as identity provider can directly invoke the Opcenter
Reporting Web API without the need to obtain a one-time authorization code, but only by authenticating on
Opcenter Reporting. This can be an alternative for the UMC application to embed Opcenter Reporting without the
need to create and distribute the **opcenterrp** certificate.

###### Authentication


After the authentication in UMC you have to load the Opcenter Reporting URL, which must be on the same domain,
within an **iframe** not visible to the user.


**Example**



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-64-1.png)



The authentication is completed when the **MRAuth** cookie is created within the application domain. As this cookie
is set as _HttpOnly_, it is not visibile in JavaScript.


Opcenter Reporting 2401.0001 - Installation Manual 65


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products supporting UMC_

###### Available Operations


Embedding Reports

#### 4.2.1 Embedding Reports


To embed reports, you can invoke the Opcenter Reporting Web API in either of the following ways:








Client-side

Server-side




###### Invoking the Opcenter Reporting Web API Client-side

Make the call to the API after you have set:








the Web API URL;
the method corresponding to the action you want to invoke (GET, POST, PUT, DELETE, UPDATE etc.)



**Example**


In AngularJS this type of call is managed by a service. In this example, a **config** object containing the UI
configuration keys is injected into the service constructor.


The **reportingApi** key contains Opcenter Reporting Web API URL (e.g. https:// _full_computer_name_ /opcenterrp/)



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-65-1.png)



66 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_How to Integrate Opcenter Reporting with Products supporting UMC_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-66-0.png)


###### Invoking the Opcenter Reporting Web API Server-side

To make a server-side call to the Opcenter Reporting Web API, you have to insert the **MRAuth** cookie retrieved
during the call to the API of the application that needs to embed Opcenter Reporting.


**Example**



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-66-1.png)



Opcenter Reporting 2401.0001 - Installation Manual 67


_How to Integrate Opcenter Reporting with other Products_


_Executing and Getting a Report as PDF without User Interaction_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-67-0.png)


### 4.3 Executing and Getting a Report as PDF without User Interaction

In Opcenter Reporting you can execute a report and receive it in PDF format for future use, for example to send it by
email or to another application.

##### Procedure


Call the following URL to which you have previously added the required parameters:


https://FQDN/opcenterrp/api/RepositoryItemActions/ExecuteReportInPdf?cbID=&rpParams=< _encoded report_
_parameter_ >&pdfOpt=< _URLencoded pdf parameter_ 


![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-67-1.png)



68 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_Executing and Getting a Report as PDF without User Interaction_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-68-0.png)












###### Examples of pdfOpt parameter configuration



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-68-1.png)





![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-68-2.png)




###### Possible values for the Conformance parameter



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-68-3.png)



Opcenter Reporting 2401.0001 - Installation Manual 69


_How to Integrate Opcenter Reporting with other Products_


_Executing and Getting a Report as PDF without User Interaction_



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-69-0.png)


###### Limitations

Besides others, the following hints and limitations should be considered:








Fonts are automatically recognized and dynamically embedded if necessary.
Not all EMF records can be displayed accurately – if you are using complex EMFs, you should pass them as
bitmaps or choose "export as picture" in the designer.



70 Opcenter Reporting 2401.0001 - Installation Manual


_How to Integrate Opcenter Reporting with other Products_


_Executing and Getting a Report as PDF without User Interaction_


Lines/Frames that are dashed/dotted in the layout may have a different spacing.
Note for PDF/A:










When using form elements in combination with PDF/A, PDF/A conformity cannot be maintained and
the form elements are deactivated.
All fonts are always embedded.
Encryption is not supported.



Opcenter Reporting 2401.0001 - Installation Manual 71


_Upgrading Opcenter Reporting from version 2401 to version 2401.0001_


_Executing and Getting a Report as PDF without User Interaction_

## 5 Upgrading Opcenter Reporting from version 2401 to version 2401.0001


Perform the following procedure if you want to upgrade Opcenter Reporting from version 2401 to version
2401.0001.


Starting from version 3.2 a new licensing model is applied. Before upgrading from a version prior to 3.2 to a higher
version, you need to acquire the Opcenter Reporting Client license, which includes the number of allowed seats, to
be added to the Server-based license. For more details, see Managing Licenses, Users and Roles for Opcenter
Reporting.

###### User Management Component (UMC) Configuration


To configure UMC 2.9 SP2 correctly, some additional manual steps have to be executed. To do so, follow the
procedure described in the _Upgrading UM Priority Ring Server_ chapter in _UMC Installation Manual_ (point 5 and the
first command of point 6 of the procedure, as the steps described in points 1 to 4 are already executed by Opcenter
Reporting setup).


Before executing the procedure, check the compatibility of all the applications that use this instance of UMC.

###### Important Recommendations











Before proceeding with the upgrade, it it strongly recommended that you clear the cache of the Internet
browser to avoid any unpredictable errors when using Opcenter Reporting.
It is recommended that you include in your database maintenance plan a backup of the existing repository
database located in the folder: **ProgramData\Siemens\Opcenter\Intelligence\Report\Server\App_Data\**
In particular, you should make a regular backup of the **repository.db** file, which is stored in the above folder
and contains all the reports you have created.


###### Procedure



1.



Launch the installation of Opcenter Reporting 2401.0001 by executing the **Start.exe** program located in the
**OpcenterReport** subfolder contained in Opcenter Intelligence ISO root folder and follow the wizard
instructions. In particular, in the following steps select **Modify/Upgrade**, click **Next** and select the products
to be installed.



72 Opcenter Reporting 2401.0001 - Installation Manual


_Upgrading Opcenter Reporting from version 2401 to version 2401.0001_


_Executing and Getting a Report as PDF without User Interaction_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-72-0.png)


Opcenter Reporting 2401.0001 - Installation Manual 73


_Upgrading Opcenter Reporting from version 2401 to version 2401.0001_


_Executing and Getting a Report as PDF without User Interaction_

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-73-0.png)


74 Opcenter Reporting 2401.0001 - Installation Manual


2.


3.


4.


5.

6.

7.



_Upgrading Opcenter Reporting from version 2401 to version 2401.0001_


_Executing and Getting a Report as PDF without User Interaction_


Click **Modify** to start the installation.

![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-74-0.png)


After the installation is completed, run the Opcenter Reporting Configurator by double-clicking the
corresponding desktop icon.
A warning message appears to remind you that the UMC configuration needs to be completed and suggests
that you follow the instructions contained in _UMC Installation Manual_ .
Click **Apply** and wait for the pop-up message that confirms the successful completion of the configuration.
Click **Close** .

Clear the cache of the Internet browser.



Opcenter Reporting 2401.0001 - Installation Manual 75


_Uninstalling Opcenter Reporting_


_Executing and Getting a Report as PDF without User Interaction_

## 6 Uninstalling Opcenter Reporting


To completely uninstall Opcenter Reporting, you must perform the following procedure.

###### Important Recommendations











Uninstalling User Management Component requires a number of additional actions. For more details on
how to uninstall UMC properly, see _User Management Component Installation Manual_ .
If you have applied modifications to elements contained in the installation folder, remember that they will
not be removed when you uninstall Opcenter Reporting and you will need to remove them manually.
All data generated by the application (application database, log files and public keys you have used) need to
be removed from **ProgramData\Siemens\Opcenter\Intelligence\Report\Server\App_Data\** if you want to
totally uninstall Opcenter Reporting. However, if you are upgrading to a new version of the product, these
items may be maintained in the same folder.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-75-0.png)




##### Procedure



1.


2.



From **Windows Control Panel > Programs and Features** environment, select Opcenter Reporting and click
**Uninstall** .

Restart the computer.



76 Opcenter Reporting 2401.0001 - Installation Manual


_Troubleshooting_


_Executing and Getting a Report as PDF without User Interaction_

## 7 Troubleshooting


The following tips can help you overcome common issues that you may encounter during the installation or
configuration of Opcenter Reporting.



![](mds/opint/v2401.0001/Opcenter_Reporting_InstallationManual_images/Opcenter_Reporting_InstallationManual.pdf-76-0.png)

















Opcenter Reporting 2401.0001 - Installation Manual 77


