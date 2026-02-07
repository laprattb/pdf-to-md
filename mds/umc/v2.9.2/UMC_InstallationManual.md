# s

###### **User Management Component 2.9.2**

### **UMC Installation Manual**

**09/2020**

**A5E50361197-AA**


###### Contents

#### Concepts You Need to Know About 1 Supported Browsers 2 Prerequisites 3 How to Configure UMC 4

###### Configuring the Identity Provider in


###### a High Availability/Reliability Scenario


#### **5**


#### How to Upgrade to UMC 2.9 SP2 6 How to Uninstall UMC 7 Troubleshooting 8 Appendix 9


**Guidelines**


This manual contains notes of varying importance that should be read with care; i.e.:


**Important:**


Highlights key information on handling the product, the product itself or to a particular part of the documentation.


**Note:** Provides supplementary information regarding handling the product, the product itself or a specific part of

the documentation.


**Trademarks**


All names identified by ® are registered trademarks of Siemens AG.


The remaining trademarks in this publication may be trademarks whose use by third parties for their own purposes

could violate the rights of the owner.


**Disclaimer of Liability**


We have reviewed the contents of this publication to ensure consistency with the hardware and software

described. Since variance cannot be precluded entirely, we cannot guarantee full consistency. However, the

information in this publication is reviewed regularly and any necessary corrections are included in subsequent

editions.


**Security information**


Siemens provides products and solutions with industrial security functions that support the secure operation of

plants, systems, machines and networks. In order to protect plants, systems, machines and networks against

cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial

security concept. Siemens’ products and solutions only form one element of such a concept.


Customer is responsible to prevent unauthorized access to its plants, systems, machines and networks. Systems,

machines and components should only be connected to the enterprise network or the internet if and to the extent

necessary and with appropriate security measures (e.g. use of firewalls and network segmentation) in place.


Additionally, Siemens’ guidance on appropriate security measures should be taken into account. For more

information about industrial security, please visit [https://www.siemens.com/industrialsecurity.](https://www.siemens.com/industrialsecurity)


Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly

recommends to apply product updates as soon as available and to always use the latest product versions. Use of

product versions that are no longer supported, and failure to apply latest updates may increase customer’s

exposure to cyber threats.


To stay informed about product updates, subscribe to the Siemens Industrial Security RSS Feed under [https://](https://www.siemens.com/industrialsecurity)

[www.siemens.com/industrialsecurity.](https://www.siemens.com/industrialsecurity)



Siemens AG
Digital Industries
Postfach 48 48
90026 NÜRNBERG
GERMANY



A5E50361197-AA
20200910_42680



Copyright © Siemens AG 2020
Technical data subject to change


### **Contents**

**1 Concepts You Need to Know About...................................................................................... 5**

1.1 User Manager Domain...................................................................................................... 5

1.2 User Manager User........................................................................................................... 5
1.3 User Manager Group ........................................................................................................ 6

1.4 Machine Roles .................................................................................................................. 7

1.5 Deployment Scenarios.................................................................................................... 10

1.6 Built-in User Roles ...........................................................................................................11


**2 Supported Browsers ............................................................................................................ 12**


**3 Prerequisites ......................................................................................................................... 14**

3.1 IIS Prerequisites.............................................................................................................. 16

3.2 Configuring Https Protocol in Microsoft IIS ..................................................................... 18


**4 How to Configure UMC......................................................................................................... 20**

4.1 Quick Configuration - Standalone UMC Scenario........................................................... 20
4.2 How to Configure a UMC Scenario................................................................................. 22

4.2.1 Configuring UM Priority Ring Server....................................................................... 22
4.2.2 Configuring UM Secondary Ring Server................................................................. 23
4.2.3 How to Configure UMC Web Components ............................................................. 24

4.2.3.1 Configuring UMC Web Components Via Script .............................................. 25
4.2.3.2 How to Configure UMC Web Components Manually...................................... 26

4.2.3.2.1 Configuring Identity Provider................................................................... 27
4.2.3.2.2 Configuring Web UI and Service Layer API ............................................ 28
4.2.3.2.3 Configuring Remote Authentication ........................................................ 30
4.2.3.2.4 Configuring URL Rewrite Rules .............................................................. 32
4.2.3.2.5 Adding the ServiceLayer to Whitelist ...................................................... 35
4.2.3.2.6 Configuring the Identity Provider Local Configuration............................. 36


4.2.3.3 Configuring Integrated Windows Authentication ............................................. 36
4.2.3.4 Configuring Firefox for Integrated Windows Authentication............................ 39
4.2.3.5 Identity Provider Configuration Management.................................................. 39

4.2.3.5.1 Local Configuration File .......................................................................... 40
4.2.3.5.2 Default Configuration File........................................................................ 43
4.2.3.5.3 Central Configuration File ....................................................................... 48


4.2.3.6 How to Configure Smart Card (PKI) Authentication........................................ 49

4.2.3.6.1 Configuring Smart Card Authentication Infrastructure ............................ 49
4.2.3.6.2 Configuring Smart Card Web Application ............................................... 50
4.2.3.6.3 Setting Account Policy for Smart Card Authentication ............................ 52


4.2.3.7 Enabling HTTPS in a HTTP UMC Scenario.................................................... 53
4.2.3.8 How to Configure Two Factor Authentication by time-based one-time
password..................................................................................................................... 54

4.2.3.8.1 Enabling Two Factor Authentication........................................................ 54


User Management Component 2.9.2 - UMC Installation Manual
iii
A5E50361197-AA


4.2.3.8.2 Using Two Factor Authentication ............................................................ 55


4.2.4 Installing and Configuring UMC Station Client........................................................ 56
4.2.5 Configuring SLRA support ...................................................................................... 57
4.2.6 Configuring Desktop Single Sign On ...................................................................... 59


**5 Configuring the Identity Provider in a High Availability/Reliability Scenario ................. 60**

5.1 High Availability/Reliability General Issues..................................................................... 60

5.2 Health State Service ....................................................................................................... 61

5.3 NLB and Health State Integration ................................................................................... 62


**6 How to Upgrade to UMC 2.9 SP2......................................................................................... 64**

6.1 General Recommendations ............................................................................................ 64

6.1.1 Migrating IdP Configurations................................................................................... 65


6.2 Upgrading UM Secondary Ring Server........................................................................... 66
6.3 Upgrading UM Priority Ring Server................................................................................. 67
6.4 Restarting UM Secondary Ring Server........................................................................... 68
6.5 Upgrading UM Server ..................................................................................................... 68

6.6 Upgrading UM Agent ...................................................................................................... 69
6.7 Upgrading UMC Station Client........................................................................................ 69
6.8 Upgrading the Web Components Manually .................................................................... 69

6.8.1 Upgrade - Configuring Identity Provider.................................................................. 70
6.8.2 Upgrade - Configuring Web UI................................................................................ 71
6.8.3 Upgrade - Configuring Remote Authentication ....................................................... 73
6.8.4 Upgrade - Configuring URL Rewrite Rules ............................................................. 75

6.8.4.1 Upgrade - URL Rewrite Rules......................................................................... 78


6.8.5 Upgrade - Adding the IdP to Whitelisting ................................................................ 79
6.8.6 Upgrade - Configuring the Identity Provider............................................................ 80


**7 How to Uninstall UMC .......................................................................................................... 81**

7.1 Uninstalling Full UMC ..................................................................................................... 81
7.2 Uninstalling UMC Station Client...................................................................................... 81


**8 Troubleshooting.................................................................................................................... 82**


**9 Appendix ............................................................................................................................... 85**

9.1 Importing a Windows Local User on an Agent................................................................ 85

9.2 UMC Processes.............................................................................................................. 86

9.3 Event Logging................................................................................................................. 86

9.3.1 Event Logging Security Notes................................................................................. 88


9.4 Additional Provisioning Configuration ............................................................................. 89
9.5 Performing the Automatic Certificates Renewal ............................................................. 93


User Management Component 2.9.2 - UMC Installation Manual
iv

A5E50361197-AA


## **1 Concepts You Need to Know About**

The following concepts are considered prerequisites to understand how to configure UMC:


             - User Manager Domain


             - User Manager User


             - User Manager Group


             - Machine Roles


             - Deployment Scenarios


             - Built-in User Roles

##### **1.1 User Manager Domain**


A User Manager domain (UM domain) is a collection of computers defined by the administrator of a
network that shares a common directory database. A UM domain provides access to the centralized
user accounts and group accounts maintained by the UM domain administrator.


**Important:**


UM domains are different entities with respect to Windows domains that are defined at
operating system level.

##### **1.2 User Manager User**


A User Manager user (UM user in what follows) is a user in the User Manager Component database,
identified by a user name. Note that UM users are different entities with respect to Windows users,
which are defined at operating system level.


Custom attributes can be associated with UM users. Example of custom attributes are common user
properties such as phone number, department, and so on.
To apply Secure Application Data Support (SADS), access to encrypted application data can be
granted to authorized users to allow them to decrypt it using specific Subject Keys.


**UM User Types**


You can distinguish three types of UM users:


             - **users created from scratch** in UMC or created via csv file;


             - **Windows local users** that are imported into UMC (via umx): in this case the user name follows
the pattern _<machineName>\<localUserName>_ ;


             - **Active Directory users** that are imported into UMC (via umx or via Web UI): in this case the
user name follows the pattern _<ADdomainName>\<ADuserName>_ .


User Management Component 2.9.2 - UMC Installation Manual
5
A5E50361197-AA


_1 Concepts You Need to Know About_

_1.3 User Manager Group_


**UM User Passwords**


Users created within UMC have also an associated password. Empty passwords are not allowed.
Users imported from Windows authenticate against Windows and do not have a UMC password.
Imported Windows local users authenticate **only** locally against Windows on the machine where they
are present. They can be used **only** for configuration purposes, for instance to be associated with a
Windows service running on the machine.


**Offline Users**


When you create a UMC user you can flag the user as _offline_ . UMC provisioning service checks if the
offline user exists in Active Directory:


             - if the user is present, user data are synchronized and the user becomes online,


             - otherwise the user remains offline.


**Important:**


Users created as _offline_ are enabled by design: they can therefore perform the actions
allowed by their function rights.


The user name of offline users must follow the AD pattern _<domainName>\<ADuserName>_ . They do
not have a UMC password, as they cannot authenticate until they become online. The User Security
Identifier (SID, see [Microsoft Documentation on Security Identifiers](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379571%28v=vs.85%29.aspx) for more details) property is set to a
default value (S-1-0-0) that is synchronized with the actual AD value by the UMC provisioning service.


Users are also flagged _offline_ if they are deleted from AD. In this case users are permanently deleted
from UMC database after an amount of time that can be configured (default is12 hours). See the
additional provisioning configuration in the _User Management Component Installation Manual_ for more

details.


**User Limits**

|Description|Maximum|
|---|---|
|Number of groups assigned to a user|50|
|Number of roles assigned to a user|50|


##### **1.3 User Manager Group**


A User Manager group (UM group in what follows) is a container of users and is identified by a name.
Note that UM groups are different entities with respect to Windows groups that are defined at operating
system level.


To apply Secure Application Data Support (SADS), access to encrypted application data can be
granted to authorized groups to allow them to decrypt it using specific Subject Keys.


User Management Component 2.9.2 - UMC Installation Manual
6

A5E50361197-AA


_1 Concepts You Need to Know About_


_1.4 Machine Roles_


**UM Group Types**


There are two types of UM groups:


             - **groups created from scratch** in UMC or created via csv file;


             - **Active Directory groups** that are imported into UMC (via umx or via Web UI).


**Offline Groups**


When creating a UMC group, you can flag the group as _offline_ . UMC provisioning service checks if the
offline group exists in Active Directory:


             - if the group is present, group data are synchronized, the AD users members of the groups are
imported into UMC and the group becomes online,


             - otherwise the group remains offline.


The group name of offline users must follow the AD pattern _<ADdomainName>\<ADgroupName>_ . The
UMC provisioning service searches for the AD group by its Common Name (CN).


If required, the description field of the created group can be used to configure how the UMC
provisioning service must query the AD group and import its users into UMC. In this case the
description must follow the pattern:


{{Q=<ldap query>


where {{Q= is a fixed prefix and <ldap query> is the query to be applied. The group name in this case
can be _<ADdomainName>\<GroupName>_, where GroupName can be chosen by the user.


**Group Limits**

|Description|Maximum|
|---|---|
|number of groups assigned to a user|50|
|number of roles assigned to a group|50|
|number of users bound to a group|1000|


##### **1.4 Machine Roles**


**UMC Computer Roles**


In a typical UMC scenario there are three computer roles:


             - **UM ring server** : the owner of the UM configuration, which is responsible for managing the
domain, and provides full implementation of authentication and user management features. The
_priority_ ring server is the one which is configured first, running the **umconf** utility. If more than


User Management Component 2.9.2 - UMC Installation Manual
7
A5E50361197-AA


_1 Concepts You Need to Know About_

_1.4 Machine Roles_


one ring server is available, if you unjoin the priority ring server, the system dynamically elects a
new priority ring server.


             - **UM server** : provides full implementation of authentication features, the UM server is in
_degraded mode_ if it is not connected to any UM ring server.


             - **UM agent** : works as a client of the UM server/UM ring server to which it is attached, which can
be used to run an application developed using the UMC API. See the _User Management_
_Component API SDK Developer Manual_ for more details. In order to import Windows Local
Users, see **Importing a Windows Local User on an Agent** in the _UMC Installation Manual_ .


**Important:**


Engineering operations are not allowed on the UM Agent except for encryption

enablement.


The main differences between the three aforementioned machine roles are listed in the table below.


The ring server to which the other ring servers send the request to write on the UMC database (the
candidate for writing) is called _master ring server_ . Both the priority and secondary ring server can be

master.

If the priority server is master, writing is enabled and the machine can write on the UMC database.


In case of failure, the secondary ring server becomes a master ring server with no writing enabled
( _safe mode on_ ). If the safe mode is switched off using the appropriate umx command, the secondary
ring server becomes a master with writing enabled. Consider that some operations on the UMC system
configuration are not allowed in this case, e. g. modifying the whitelist (see _UMCONF User Manual_ for
more details).


**UMC Station Client**


A machine role orthogonal to the previous ones is _UMC station client_ . A UMC station client is a
machine where UMC station client software has been installed and that has been registered to be a
trusted machine. A UMC station client provides a claim in which certified logon station information is
included. These details can be used to associate authorization rights with a machine, which must not
be a ring server, server or agent, using the client product.


UMC installation includes the UMC station client installation, thus, UM ring servers, UM servers and
UM agents need only to register to become UMC station clients, whereas a machine that is not part of
the UMC domain has to install the UMC station client software first and then has to register to become
a UMC station client.


**CAUTION:**


If you want to manage Active Directory users, the UM ring server and the UM server
machines have to be joined to the AD Windows domain.


**Machine Role Functionalities**


The table below provides the functionality mapping against the machine roles. For each functionality:


denotes that the functionality has been fully implemented;


User Management Component 2.9.2 - UMC Installation Manual
8

A5E50361197-AA


_1 Concepts You Need to Know About_


_1.4 Machine Roles_


denotes that the functionality is not available.


only available when the system is connected to the UM Server

|Col1|UM Server|UM Ring Server|UM<br>Agent|
|---|---|---|---|
|Perform TIA User authentication||||
|Local single modifications||||
|Change password||||
|Authentication against Active Directory||||
|Manage Domain attach/join|(acts as proxy for<br>agents)|||
|Potential Master||||
|Can sign authentication object||||
|Propagate UM configuration||||
|Can host Identity Provider /Remote<br>Authentication or<br>UMC Web UI||||
|Number of instances|max 4|1-2|max 25|
|Off Line Authentication/Read-Only on the<br>configuration||||
|Ring Failover - recovery||(merge missing)||
|Electronic Log Store&Forward||||
|Log Forwarding||||
|Import Windows Local Users||||
|Import AD Users/Group||||



User Management Component 2.9.2 - UMC Installation Manual
9
A5E50361197-AA


_1 Concepts You Need to Know About_

_1.5 Deployment Scenarios_


**Propagation of UM configuration**


The UM configuration is distributed from the master ring server to the UM servers, in order to allow a
faster local authentication. Any configuration change is performed on the primary master ring server
and then propagated to the connected UM servers. The synchronization of the configuration starts
when at least 30 seconds from the last modification are passed. This “stabilization” time is required for
avoiding too many alignments in case many close changes are performed. After that time the
propagation of the configuration starts, which means that some other time (typically from few seconds
to few minutes) is required before the configuration alignment is completed on all the UM servers.


**Offline availability**


As the UM configuration is distributed from the master ring server to the UM servers, the authentication
of UMC users is performed locally. Therefore, authentication of UMC users is available on UM servers
also when the UM server is disconnected from the ring server, provided that the configuration has been
propagated before the disconnection occurs.


Authentication of AD users is performed by Windows, therefore the alignment of UM configuration is
not sufficient for providing an offline authentication. In this case, authentication must occur at least
once to allow a user to authenticate when offline, through the usage of a temporary cache.


The configuration of Secure Application Data Support is not aligned by default on UM servers. As a
consequence, Secure Application Data Support is not available when the UM server is disconnected
from the ring server. It is possible to configure on a Group that the users of this group are allowed to
use Secure Application Data Support also when offline. For the configured group the needed Secure
Application Data Support configuration is propagated from the ring server to the UM servers, therefore
allowing a local usage.

##### **1.5 Deployment Scenarios**


We support the following deployment scenarios:


             - **standalone scenario** : one ring server where UMC and all its Web components are installed
and configured. A quick configuration guide is available for this scenario.


             - **redundant scenario** :


– 2 UM ring server machines, one ring server is configured first and is called _priority ring_

_server_, the secondary one is added to the ring using the join command;


– up to 4 UM servers


             - **distributed scenario** :


– 1 or 2 UM ring server machines, one ring server is configured first and is called _priority ring_

_server_, the secondary one is added to the ring using the join command;


– up to 4 UM servers


– up to 25 UM agents.


Each UMC Web component can be installed and configured on any UM ring server and/or on any UM
server. If you install the UMC Web UI on a UM server, you cannot import AD users via UMC Web UI.


NLB redundancy is supported only for Identity Provider.


User Management Component 2.9.2 - UMC Installation Manual
10

A5E50361197-AA


_1 Concepts You Need to Know About_


_1.6 Built-in User Roles_


**Standalone engineering station**


UMC allows you to prepare configuration data (users, groups and so on) in a standalone engineering
station, export this data in a UMC configuration package which can then be imported into a production
target system. The two commands involved are the umx export and import package commands. If you
want to overwrite the configuration of the target production system with that of the source engineering
machine the update command can be used instead of the import command. For more information on
these command and how they impact the target machine, see the _UMX User Manual_ .


If the target system is not configured, you can import a package using the umconf import package
command. For more information see the _UMCONF User Manual_ .

##### **1.6 Built-in User Roles**


A User Manager role groups a set of function rights. Function rights are the capabilities to perform
operations. They are associated with roles so that the set of UM users with a specific UM role is
allowed to perform the set of operations associated with it. UM roles can be associated with UM users
or with UM groups so that all the users belonging to such groups inherit the UM role function rights.
UM roles are used to define the function rights within UMC, for instance, to define whether a user can
configure UMC or not.


The following roles are automatically created by the system while configuring UMC:


             - **Administrator** : built-in "root" role, can perform any operation. The user that has this role is a
root user that can perform any operation. This role cannot be associated with any group. It can
be associated with a user if the user performing the association has in turn the **Administrator**
role. The **Administrator** role cannot be deleted. Only users having the **Administrator** role can
modify other users having this role.


             - **UMC Admin** : can manage users, groups and all the other UMC entities.


             - **UMC Viewer** : can access the user management configuration without making modifications.


User Management Component 2.9.2 - UMC Installation Manual
11
A5E50361197-AA


## **2 Supported Browsers**

The following browsers are supported either by the Identity Provider and by the Web UI.


**General Recommendations**


             - For security reasons, we suggest that you set the browser cookie policy management so that
cookies are not maintained after the browser is closed. In this way you can disable the
possibility that a user reopens a browser and is logged in without providing the credentials
again.


             - The browser used to display the UMC Web UI must allow the pop-up display.


             - While using the UMC Web UI do not select the option **Prevent this page from creating**
**additional dialogs** . The selection of this option causes Web UI malfunctions.


             - Disable the **Autocomplete** option in your browser settings.


             - Disable the password saving option in your browser settings.


**Identity Provider**


             - Internet Explorer 8


             - Internet Explorer 9


             - Internet Explorer 10


             - Internet Explorer 11


             - Chrome 32.0.1700.107 m or higher


             - Firefox 31.0 or higher


             - Microsoft Edge 25.10586.0.0 or higher


             - Microsoft Edge 83.0.478.58 (Chromium based)


**UMC Web UI**


The Web UI is based on HTML5. For this reason it is supported only on:


             - Internet Explorer 11


             - Chrome 32.0.1700.107 m or higher


             - Firefox 31.0 or higher


             - Microsoft Edge 25.10586.0.0 or higher


             - Microsoft Edge 83.0.478.58 (Chromium based)


User Management Component 2.9.2 - UMC Installation Manual
12

A5E50361197-AA


_2 Supported Browsers_

_1.6 Built-in User Roles_


**Important:**


The following resolutions are supported:


             - 1280x800


             - 1920x1200


User Management Component 2.9.2 - UMC Installation Manual
13
A5E50361197-AA


## **3 Prerequisites**

The following lists the prerequisites for UMC divided by:


             - General Recommendations


             - Supported Operating Systems


             - Microsoft Visual C++ Packages


             - Identity Provider Prerequisites


             - IIS Configuration


             - If you wish to use HTTPS instead of HTTP you must configure IIS for HTTPS


**General Recommendations**


             - **Operating Systems:** The operating system must be updated to the latest security patches in
order to improve system reliability and security,
The Windows Security Patch KB2532445 must be installed on the following OS:

– Windows Server 2008 R2 SP1(Professional, Enterprise, Datacenter Edition)


– Windows 7 SP1 (x86, x64)


             - **Computer Naming Conventions:** The computer name of the machines on which you will install
UMC must only contain alphanumeric characters and not exceed 15 characters. See host name
limitations in [Microsoft Support Documentation](https://support.microsoft.com/en-us/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and) for more information.


**Note:** If the configuration of Windows is such that the temp files are deleted when the
system is restarted, the installation will fail if the system is restarted by the setup. Should
this occur you must launch the setup again.


**Supported Operating Systems**


UMC can be installed on the following Operating Systems:


             - Windows Server 2019 (Standard)


             - Windows Server 2016 (Standard)


             - Windows Server 2012 R2 (Standard, Datacenter Edition)


             - Windows Server 2008 R2 SP1 (Standard, Enterprise, Datacenter Edition)


             - Windows 8.1 (x86, x64)


             - Windows 7 SP1 (x86, x64)


             - Windows 10 Version 1511 (OS Build 10586.0) or subsequent (x86, x64)


The following table lists the UMC components which can run on 32 or 64 bit machines.


User Management Component 2.9.2 - UMC Installation Manual
14

A5E50361197-AA


_3 Prerequisites_

_1.6 Built-in User Roles_

|Component|32 bit|64 bit|
|---|---|---|
|UMCONF|||
|UMX|||
|Identity Provider|||
|Web UI|||
|Remote Authentication|||
|Integrated Windows Authentication|||
|Service Layer API|||
|API SDK|||



**Microsoft Visual C++**


In order to install UMC, the following redistributable packages have to be installed on Windows
server 2008 R2, Windows 7, Windows 8.1, Windows server 2012 R2, Windows Server 2016,
Windows Server 2019, Windows 10:


             - Microsoft Visual C++ 2015 Redistributable - x86 14.0.23026.00


             - Microsoft Visual C++ 2015 Redistributable - x64 14.0.23026.00


**Important:**

             - For 32-bit operating system versions only the 32-bit redistributable packages have
to be installed, whereas for 64-bit operating system versions all the redistributable
packages have to be installed.


             - In the BUNDLE and SIWA installers the redistributable packages are automatically

installed.


**Identity Provider Prerequisites**


             - The machine has to be a 64 bit machine.


             - Microsoft Framework:


– Microsoft .NET Framework 4 Client Profile


– Microsoft .NET Framework 4 Extended


             - Microsoft Internet Information Services:


– Internet Information Services 7.5, 8, 8.5, or 10. Note that in the case of IIS 7.5 you must

add .json to the MIME types.


             - IIS extension: Application Request Routing 3.0 and its prerequisites have been downloaded and
installed (you can download and install web platform from here: [http://www.microsoft.com/web/](http://www.microsoft.com/web/downloads/platform.aspx)


User Management Component 2.9.2 - UMC Installation Manual
15
A5E50361197-AA


_3 Prerequisites_

_3.1 IIS Prerequisites_


[downloads/platform.aspx, launch it on the machine and search for Application Request Routing](http://www.microsoft.com/web/downloads/platform.aspx)
3.0).


**CAUTION:**


UMC Web services use cookies to guarantee the correct functioning. We do not
display any warning related to cookie usage, as our application must not be used as
an open Web service, available, for instance, on the Internet.

##### **3.1 IIS Prerequisites**


IIS configuration verification steps vary depending on the version of Windows on which it is being
performed. The following verification procedures are based on: Windows Server 2016 and Windows 10


In order to harden your system it is recommended you install the minimum set of IIS features possible,
see _UMC Security Concept_ for more information on system hardening.


**Windows Server 2016**


Verify the following features and roles are installed for Windows Server 2016.


1. On the start page click **Server Manager.**


2. Click **Dashboard** on the left pane.


3. Click **2 Add Roles and Features.**


4. Click **Role-based or feature-based installation** and click **Next** .


5. Select a server from the list and click **Next** .


6. Verify the following **Roles** are selected under **Web Server (12 of 34):**


–
**Common HTTP Features (4 of 6)**

                     - **Default Document**


                     **Directory Browsing**


                     - **HTTP Errors**


                     - **Static Content**


–
**Health and Diagnostics (1 of 6)**


                     **HTTP Logging**


–
**Performance (1 of 2)**


                     **Static Content Compression**


–
**Security (2 of 9 )**


                     **Request Filtering**


                     - **Windows Authentication**


–
**Application Development (4 of 11)**


                     **.Net Extensibility 4.6**


                     - **ASP.NET 4.6**


                     - **ISAPI Extensions**


User Management Component 2.9.2 - UMC Installation Manual
16

A5E50361197-AA


_3 Prerequisites_

_3.1 IIS Prerequisites_


                     - **ISAPI Filters**


7. Verify the following **Roles** are selected under **Management Tools (3 of 7):**


–
**IIS Management Console**


–
**IIS Management Scripts and Tools**


–
**Management Service**


8. Click **Next.**


9. Verify the following **Features** are selected:


–
**.Net Framework 3.5 Features (1 of 3)**


                     **.Net Framework 3.5 (includes .net 2.0 and 3.0)**


–
**.Net Framework 4.6 Features (3 of 7)**


                     - **.NET Framework 4.6**


                     - **ASP.NET 4.6**


                     **WCF Services (1 of 5)**


                        **TCP Port Sharing**


–
**Windows Defender Features and WoW64 Support**


                     - **Windows Defender**


                     - **GUI for windows Defender**


–
**Windows PowerShell (3 of 5)**

                     - **Windows PowerShell 5.1**


                     **Windows PowerShell 2.0 Engine**


                     - **Windows PowerShell ISE**


10. Close **Windows Server Manager** .


**Windows 10**


Verify the following features and roles are installed for Windows 10.


1. Type " _Turn Windows Features on and off"_ in the **Search Windows** search box.


2. Click **Turn Windows Features on and off** in the result pane, a windows is displayed.


3. Verify the following are installed under **Internet Information Services** :


–
**Web Management Tools:**


                     **IIS Management Console**


                     **IIS Management Scripts and Tools**


                     - **IIS Services**


– **World Wide Web Services:**


                     **Application Development Features**


                        **.Net Extensiblity 4.6**


                        - **ASP.NET 4.6**


                        - **ISAPI Extensions**


                        - **ISAPI Filters**


                     - **Common HTTP Features**


User Management Component 2.9.2 - UMC Installation Manual
17
A5E50361197-AA


_3 Prerequisites_

_3.2 Configuring Https Protocol in Microsoft IIS_


                        - **Default Document**


                        **Directory Browsing**


                        - **HTTP Errors**


                        - **Static Content**


                     **Health and Diagnostics**


                        **HTTP Logging**


                     - **Performance Features**


                        **Static Content Compression**


                     **Security**


                        **Request Filtering**


                        - **Windows Authentication**


– **.Net Framework 3.5 Features**


– **.Net Framework 4.6 Advanced Features**


                     - **ASP.NET 4.6**


                     - **WCF Services**


                        **TCP Port Sharing**


– **Windows PowerShell 2.0**


                     **Windows PowerShell 2.0 Engine**


4. Click **Cancel** to close the window.

##### **3.2 Configuring Https Protocol in Microsoft IIS**


This procedure allows you to configure IIS to work with HTTPS protocol and is only required if you wish
to use HTTPS protocol, which is strongly recommended in plant environments.


**Prerequisites**


A valid SSL certificate has been acquired from a Certification Authority or a self-signed SSL certificate

has been created.


**Procedure**


1. Open **IIS Manager** .


2. In the tree on the left go to the node of the site which you have configured.


3. Right click on the node and select **Edit Bindings** .


User Management Component 2.9.2 - UMC Installation Manual
18

A5E50361197-AA


_3 Prerequisites_

_3.2 Configuring Https Protocol in Microsoft IIS_


4. Click **Add** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-18-0.png)


5. Insert the parameters as displayed in the previous image and click **OK** . The **SSL certificate**
parameter has to be the acquired certificate name.


6. Click **OK** and then **Close** .


User Management Component 2.9.2 - UMC Installation Manual
19
A5E50361197-AA


## **4 How to Configure UMC**

The UMC can be configured in a:


             standalone scenario by configuring only a priority ring server,


             - redundant scenario by adding a secondary ring server,


             - distributed scenario with multiple servers, agents and station clients.


Depending on your scenario you can use one of the following workflows:


             - For a simple standalone UMC installation on 64bit machine with HTTPS you can follow the
Quick Configuration - Standalone UMC Scenario,


             - For distributed and redundant scenarios or additional configurations, for example if you wish to
install UMC on a 32 bit machine follow How to Configure a UMC Scenario.


**HTTP Configuration**


**CAUTION:**


We strongly suggest that you enable HTTPS in plant environments.


If HTTPS protocol has been configured HTTP cannot be used.


If IIS is not configured to work with https protocol, you can configure UMC both manually and via script,
but secure protocol is not enabled. In this scenario:


             - If UMC Web UI does not work, verify that the value of the registry key
HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\User Management\WebUI\Settings\secure is

set to 0.


             - Smart card authentication does not work.

##### **4.1 Quick Configuration - Standalone UMC Scenario**


The following procedure describes the minimum steps required to configure a UMC standalone
scenario, therefore a machine which has the role priority ring server. The procedure does not endeavor
to document all the possible configuration options, however some additional configurations which can
be applied to this scenario are listed in additional configurations, for more complex configurations and
scenarios, see How to Configure a UMC Scenario.


**Prerequisites**


             - Full UMC installation has been installed.


             - IIS has been configured to work with the HTTPS protocol.


             - The operating system is 64 bit.


User Management Component 2.9.2 - UMC Installation Manual
20

A5E50361197-AA


**Procedure**


**Result**



_4 How to Configure UMC_
_4.1 Quick Configuration - Standalone UMC Scenario_


   - (only required to manage Active Directory users) the Windows user specified at step 2
(managing Active directory users) must have:

– Active Directory access rights;


– Write access on the UMC program data subfolder \CONF( for example C:\ProgramData\

Siemens\UserManagement\CONF) or alternatively belong to the Windows group **UM**
**Service Account;**


1. Right-click **UMConf,** which can be found in the subdirectory in Bin or Wow\bin, for example; C:
\Program Files\Siemens\UserManagement\Wow\Bin, and select **Run As Administrator.**


2. Following the guided configuration in UMConf Interactive mode:

– Create a User Management Domain, by specifying a name using only alphanumeric


characters.


– Create a User Management User with administrator role, by specifying the username

using only alphanumeric characters, and a password which complies with your
organization's password policy.


– Associate a Windows user who is either a member of **UM Service Accounts** group or

who has administrative rights to the **UMCService,** by inserting . _\ username_ and the
corresponding password.


– (optional) To manage Active Directory users, specify a Windows user as described in

prerequisites, by inserting _domain\username_ and password.


3. Right-click **IdP_WebUI_configurator.bat,** which can be found in C:\Program Files\SIEMENS\
UserManagement\BIN, if the default installation folder is selected, and select **Run as**

**Administrator.**


UMC and the identity provider web are configured.



**Additional Configurations**


             Configure Firefox for Integrated Windows Authentication, this procedure is not required for other

browsers.


             - Perform Additional Identity Provider Configuration.


             - If SADS (Secure Application Data Support) is required, it must be enabled via the UMX utility, by
running the command: umx -AP -setakp, for more information see the _UMX User Manual._


             - If SLRA support is required, see Configure SLRA support.


             - If Desktop Single Sign on is required, see Configure Desktop Single Sign On.


User Management Component 2.9.2 - UMC Installation Manual
21
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_

##### **4.2 How to Configure a UMC Scenario**


**Prerequisites**


             - If you want to manage Active Directory users, the UM ring server and the UM server machines
have to be joined to the AD Windows domain.


             - Check that the connectivity to TCP/4002 is enabled on all machines (or disable firewall on **um.**
**Ris.exe**, the UM process responsible for UM machines communications).


             - The firewall configuration on UMC Servers and Ring Servers must be configured to allow
inbound access on either the port which is used for HTTP (by default 80) or, the port that is used
for HTTPS (by default 443).


**Workflow**


1. Configure the machine you have elected as priority master.


2. Configure the machine you have elected as secondary master (only for redundant scenario).


3. (Optional) Configure one or more machines as UM servers, using the **UMConf.exe** program
on the User Management, to join the server to the domain ( **serverType** parameter equals to 0)
. Refer to the _UMCONF User Manual_ for more details.


4. (Optional) Configure one or more machines as agents, using the **UMConf.exe** program on the
User Management, to attach the agent to the domain. Refer to the _UMCONF User Manual_ for

more details.


5. Configure the web components.


6. (Optional) Install and configure UMC station clients.


7. (Optional) Configure SLRA support.


8. (Optional) Configure Desktop Single Sign On.


**Additional Operations**


             - The following optional step can be performed on one of the previous machines:
Associate an administrative Role with a user, so that this user can run the **umx.exe** command
or can log in to the Web UI to manage UM users and groups.


**4.2.1 Configuring UM Priority Ring Server**


Once UMC has been installed the configuration must be performed via UMConf **.** The steps are
described using UMConf in interactive mode. **UMConf.exe** is distributed with UMC and installed in the
subdirectory \BIN(64bit) or Wow\Bin (32bit). If you need to import an existing configuration import
command must be executed via a **UMConf.exe**, for more information on UMconf see the _UMCONF_

_User Manual._


User Management Component 2.9.2 - UMC Installation Manual
22

A5E50361197-AA


**Prerequisites**


**Procedure**



_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


- Full UMC installation has been installed.


- (only required to manage Active Directory users) the Windows user specified at step 2
(Managing Active directory users) must have:

– Active Directory access rights;


– Write access on the UMC folder C:\ProgramData\Siemens\UserManagement\CONF or

alternatively they must belong to the Windows group **UM Service Account** .


1. Right-click **UMConf,** which can be found in the sub-directory Wow\bin, for example; C:\
Program Files\Siemens\UserManagement\Wow\Bin, and select **Run As Administrator.**


2. Following the guided configuration in UMConf Interactive mode:

– Create a User Management Domain, by specifying a name using only alphanumeric


characters.


– Create a User Management User with administrator role, by specifying the username

using only alphanumeric characters, and a password which complies with your
organization's password policy see _UMC Security Concepts_ for more information;


– Associate a Windows user who is either a member of **UM Service Accounts** group or

who has administrative rights to the **UMCService,** by inserting . _\ username_ and the
corresponding password.


– (optional) To manage Active Directory users, specify a Windows user as described in

prerequisites, by inserting _domain\username_ and password.


**Note:**

 - If SADS (secure application data support) is required see the _UMX User Manual_ .


 - the user which is assigned to the UMCService must only be modified via UMConf.



**Additional Operations**


Additional provisioning configurations can also be performed.


**4.2.2 Configuring UM Secondary Ring Server**


**Prerequisites**


             - You must have created the main ring server machine.


             - A full UMC Installation has been installed on the machine.


             - If https is required you must configure https in IIS.


User Management Component 2.9.2 - UMC Installation Manual
23
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**Procedure**


To create another ring server machine:


1. Join the server using the **umconf.exe** program. See _UMCONF User Manual_ for more details.


2. If you have configured the AD provisioning on the priority ring server, you have to configure it
also in the secondary ring server.


**Additional Operations**


             - Additional Provisioning Configuration can also be performed.


             - In order to add the Service Layer to whitelisting login to the WEB UI using the Administrator
user created during the initial configuration.


**4.2.3 How to Configure UMC Web Components**


Once UMC has been installed if required you can configure the web components as described below.


**Prerequisites**


             - The machine is configured as a UMC ring server or server


             - if the machine is not primary ring server you must add the service layer to white-listing by
logging in to the Web UI with the Administrator user or via umconf on the primary ring server.


             - The firewall configuration on UMC Servers and Ring Servers must be configured to allow
inbound access on either the port which is used for HTTP (by default 80) or, the port that is used
for HTTPS (by default 443).


             - If you are using HTTPS protocol IIS must have been configured to work with the HTTPS
protocol.


**Configuration Types**


             - via script: 64bit and HTTPS only. The script configures the web components automatically.


             - manually: The manual method can be used for HTTP or HTTPS. You can also use the method
in order to structure your own custom configuration script.


**Web Components Configuration Reset**


UMC provides a script, **REMOVE_IdP_WebUI_configurator.bat**, to reset the configuration of the Web
Components. The batch file can be found in C:\Program Files\SIEMENS\UserManagement\BIN, if the
default installation folder is selected, and can only be used on a 64 bit machine.


User Management Component 2.9.2 - UMC Installation Manual
24

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**CAUTION:**


If you perform any modification to the IIS configuration after launching the configuration
script **IdP_WebUI_configurator.bat** or you have configured UMC without using this
script **,** you have to reset the Web components configuration and, only afterwards,
configure the system again .


**4.2.3.1 Configuring UMC Web Components Via Script**


To configure all the Web components on the same UM ring server/UM server, UMC provides the script
**IdP_WebUI_configurator.bat** which allows you to configure them to work with the HTTPS protocol
and to configure the integrated Windows authentication (except the Firefox configuration that has to be
performed manually).


The batch file can be found in **C:\Program Files\SIEMENS\UserManagement\BIN**, if the default
installation folder is selected. If IIS has been previously configured to work with the HTTPS protocol,
the script configures the Web components accordingly.


**Note:**

             - If the user which is used to run the script is a Windows local user, the FQDN
cannot be retrieved, this results in the registry key of the IDP being configured with
only the machine name and not the domain name.


             - If you have configured a site in IIS with a name which is not **Default Web Site,** you
must open a command prompt as administrator from the installation folder of the .
bat file. and specify the name of the site as first parameter: for example, C:\
Program Files\Siemens\UserManagement\BIN>IdP_WebUI_configurator.bat "your

web site name".


             - If you want to specify a specific "reverseProxy" value, different from the one
retrieved automatically in the script and you want to use it in the Identity Provider
configuration, you can set it as second parameter when launching the
**IdP_WebUI_configurator.bat** script: for example, C:\Program Files\Siemens\
UserManagement\BIN>IdP_WebUI_configurator.bat "your web site name" "your
reverse proxy address".


             - By default the Identity Provider node.exe process is listening on port 8443. If you
want to modify this default value you can set the desired port value as third
parameter when launching the **IdP_WebUI_configurator.bat** script: for example,
C:\Program Files\Siemens\UserManagement\BIN>IdP_WebUI_configurator.bat
"your web site name" "your reverse proxy address" "port number".


             - If you want to specify a certain parameter keeping the default values of the
previous parameters it is necessary to pass an empty string for the parameters that
you don't want to customize. For example, to specify only a certain port number
without modifying the IIS site name and the reverse proxy address, you have to
call the **IdP_WebUI_configurator.bat** script in this way: C:\Program Files\
Siemens\UserManagement\BIN>IdP_WebUI_configurator.bat "" "" "port number".
The empty double quotes specify an empty value for the parameters that will be
passed to the script.


User Management Component 2.9.2 - UMC Installation Manual
25
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**General Recommendations**


The Web components can be configured in any UM ring server and/or in any UM server. In order to
guarantee IdP high availability and reliability, we suggest that you install and configure it on more than
one machine and configure the IdP high availability/reliability.


**Prerequisites**


             - IIS has been previously configured to work with the HTTPS protocol.


             - The operating system must be 64 bit


             - The machine is configured as a UMC ring server or server.


**Workflow**


1. On all the servers on which you want to configure the Web components, right-click
**IdP_WebUI_configurator.bat,** which for example can be found in C:\Program Files\
SIEMENS\UserManagement\BIN, if the default installation folder is selected, and select **Run**

**as Administrator** .


2. Configure Firefox for Integrated Windows Authentication (optional).


3. Configure smart card authentication (optional).


4. Perform Additional Identity Provider Configuration (optional).


**4.2.3.2 How to Configure UMC Web Components Manually**


**General Recommendations**


The Web components can be configured in any UM ring server and/or in any UM server. In order to
guarantee IdP high availability and reliability, we suggest that you install and configure it on more than
one machine and configure the IdP high availability/reliability.


**Prerequisites**


If required IIS has been previously configured to work with the HTTPS protocol.


**Workflow**


1. Configure the following:


–
Identity Provider in IIS


–
Web UI and Service Layer API


– Remote Authentication


– URL Rewrite Rules


–
Adding the ServiceLayer to Whitelist


User Management Component 2.9.2 - UMC Installation Manual
26

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


– Identity Provider .json file;


2. Perform the following additional Web configuration steps:

– configure Integrated Windows Authentication;


– configure Firefox for Integrated Windows Authentication;


– configure Smart Card Authentication;


**4.2.3.2.1 Configuring Identity Provider**


**Prerequisites**


             - The Identity Provider prerequisites are installed.


             - The machine is a 64 bit UM ring server or UM server.


**Procedure**


1. Open **IIS Manager** .


2. In the tree on the left select the **Application Pools** node.


3. Right click on the node and select **Add Application Pool** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-26-0.png)


4. Insert the parameters as displayed in the previous image and click **OK** .


5. In the tree on the left select the **Default Web Site** node.


User Management Component 2.9.2 - UMC Installation Manual
27
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


6. Right click on the node and select **Add Application** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-27-0.png)


7. Insert the parameters as displayed in the previous image and click **OK** . The path varies
depending on where UMC is installed, for example C:\Program Files\Siemens\
UserManagement\web\ipsimatic-logon.


8. On the applications pool page select the newly created application pool, and click **Manage**
**Application**            - **Advanced Settings** .


9. Set to 0 the field **Regular Time Interval (minutes)** and click **OK** .

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-27-1.png)


**4.2.3.2.2 Configuring Web UI and Service Layer API**


**Important:**


UMC contains two IIS 64 bit Native Modules: **um.ra.dll** and **um.slvm64.dll**


User Management Component 2.9.2 - UMC Installation Manual
28

A5E50361197-AA


**Prerequisites**


**Procedure**



_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


 - The prerequisites are installed.


 - The machine is a 64 bit UM ring server or UM server.


 - The Identity Provider (IdP) is correctly configured.


1. Open the **Registry Editor** .


2. In the tree on the left go to the **HKLM\SOFTWARE\SIEMENS\User Management\WebUI\**
**Settings** node.


3. Right click on the node, select **New > Key** and insert the **WebUI** key.


4. Right click on the **WebUI** node, select **New > Key** and insert the **Settings** key.


5. Right click on the **Settings** node, select **New > String Value** .


6. Double click on the newly inserted value and set as **Value name** the string **idpaddress** and as
**Value data** the complete IdP URL, for example if the IdP is located on the local machine:
[https://FQDNmachinename/umc-sso](https://FQDNlocalmachinename/umc-sso) or [https://reverseproxyadress/umc-sso](https://reverseproxyadress/umc-sso) for complex
scenarios like NLB scenarios. Depending on the IdP configuration the URL may start with **http**
or **https** .


7. In the tree on the left go to the **HKLM\SOFTWARE\SIEMENS\User Management\CERT**
**Library\Domain** node.


8. Right click on the **Domain** node, select **New > String Value** and insert the name **Web** .


9. Close the **Registry Editor** .


10. Open **IIS Manager** .


11. In the tree on the left select the **Application Pools** node.


12. Right click on the node and select **Add Application Pool** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-28-0.png)


13. Insert the parameters as displayed in the previous image and click **OK** .


14. In the tree on the left go to the **Default Web Site** node.



User Management Component 2.9.2 - UMC Installation Manual
29
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


15. Right click on the node and select **Add Application** : the following dialog opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-29-0.png)


16. Insert the parameters as displayed in the previous image and click **OK** . The path of the
application is, for example C:\Program Files\Siemens\UserManagement\WEB\Umc.


17. To verify that the application works properly, in the tree on the left go to the **UMC** node.


18. Right click on the node and select **Manage Application > Browse** . The Web UI application
opens displaying the login page.


**4.2.3.2.3 Configuring Remote Authentication**


**Prerequisites**


             - The general UMC prerequisites have been satisfied.


             - The machine must be a 64 bit UM ring server or UM server.


**Procedure**


1. Open **IIS Manager** .


2. In the tree on the left go to the root node.


3. On the right area of the screen double click on **Modules** .


User Management Component 2.9.2 - UMC Installation Manual
30

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


4. On the top right corner click on **Configure Native Modules** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-30-0.png)


5. Click on **Register** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-30-1.png)


6. Insert the parameters as displayed in the previous image and click **OK.**


7. Click on **Register** again: the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-30-2.png)


8. Insert the parameters as displayed in the previous image.


9. Once you have added the module make sure they are not selected and click **OK.**


10. Click **Modules** under the **UMC** application.


11. On the top right corner click on **Configure Native Modules.**


12. Select the **UserManagementServiceLayer module** checkbox then click **OK** .


13. Click **Modules** under the **ra** application, if ra is not present see note.


14. On the top right corner click on **Configure Native Modules** .


15. Select the **ra module** checkbox then click **OK.**


User Management Component 2.9.2 - UMC Installation Manual
31
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**Note:** If the ra application is not already present:


1. create a folder under the WEB ( for example C:\Program Files\Siemens\
UserManagement\WEB folder called _ra._


2. add an application to the default site called "ra" specifying the path of the folder
created in the previous step.


**4.2.3.2.4 Configuring URL Rewrite Rules**


You must manually configure the following URL rewrite rules in IIS.


**Procedure**


1. Go to **IIS Manager** .


2. In the **Connections** pane, select your server and then the top level site.


3. In the **Site** pane, double-click **URL rewrite.**


4. In the **Actions** pane, click **View Server Variables.**


5. Click **Add...** and specify _[http cookie]._


6. Go to the **Server** pane, double-click **Application Request Routing Cache** .


7. In the **Actions** pane, click **Server Proxy Settings** .


8. On the **Application Request Routing** page, select **Enable proxy** .


9. Check that the **Reverse rewrite host in response header** flag is false. It is recommended to
set it as false in the case of a physics reverse proxy or in case you want to define a specific
domain of the cookies.


10. In the **Actions** pane, click **Apply** .


11. In the **Server pane**, double-click **URL Rewrite** .


12. In the **Actions pane** on the right-hand side, click **Add rules** .


13. In the **Add Rules** dialog box, select **Blank Rule** and click **OK** .


14. In the **Edit inbound rule** pop-up, specify the following:

– Name of the rule: UMC SSO Static


– Pattern to use for matching the URL string: Matches the Pattern.


– Using: Regular Expressions.


– Pattern: (.*)


– Specify the action type: Rewrite


– Action properties Rewrite URL: The URL to rewrite, either http or https, local address 127.

0.0.1, the port of reverse proxy, and /umc-sso for example: [http://127.0.0.1:8443/umc-sso](http://vmwin2016rox-0:8443/umc-sso%7BC:2)
[{C:2} (8443 is the standard port to be changed if idp listener port is customized).](http://vmwin2016rox-0:8443/umc-sso%7BC:2)


User Management Component 2.9.2 - UMC Installation Manual
32

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


15. Click **Add** in the conditions area and specify the values in the image below.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-32-0.png)


16. Click **OK** .The pop-up is closed.


17. Click **Add** in the **Server Variables** area.


18. Select the **HTTP_COOKIE** server variable from the drop down list and insert {HTTP_COOKIE}
;ReverseProxyHost={SERVER_NAME};ReverseProxyPort={SERVER_PORT} in the value
field.


19. Check the **Replace the existing value** checkbox, then click **OK** .The pop-up is closed.


20. In the action pane click **Apply** .


**Procedure: ADD IDP Legacy rule**


1. In the **Server pane**, double-click **URL Rewrite** .


2. In the **Actions pane** on the right-hand side, click **Add rules** .


3. In the **Add Rules** dialog box, select **Blank Rule** and click **OK** .


4. In the **Edit inbound rule** pop-up, specify the following:

– Name of the rule: UMC IDP NODE SWITCH OFF


– Pattern to use for matching the URL string: Matches the Pattern.


– Using: Regular Expressions.


– Pattern: (.*)


– Specify the action type: Rewrite


– Action properties Rewrite URL: The URL to rewrite, either http or https, local address 127.

0.0.1, the port of reverse proxy, and /umc-sso for example: [http://127.0.0.1:8443/umc-sso](http://vmwin2016rox-0:8443/umc-sso%7BC:2)
[{C:2} (8443 is the standard port to be changed if idp listener port is customized)](http://vmwin2016rox-0:8443/umc-sso%7BC:2)


5. Click **Add** in the conditions area and specify the following conditions in the image below.


User Management Component 2.9.2 - UMC Installation Manual
33
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-33-0.png)


1. Click **OK** .The pop-up is closed.


2. Click **Add** in the **Server Variables** area.


3. Select the **HTTP_COOKIE** server variable from the drop down list and insert {HTTP_COOKIE}
;ReverseProxyHost={SERVER_NAME};ReverseProxyPort={SERVER_PORT} in the value
field.


4. Check the **Replace the existing value** checkbox, then click **OK** .The pop-up is closed.


5. In the action pane click **Apply** .


**Procedure: ADD SWAC Legacy rule**


1. In the **Server pane**, double-click **URL Rewrite** .


2. In the **Actions pane** on the right-hand side, click **Add rules** .


3. In the **Add Rules** dialog box, select **Blank Rule** and click **OK** .


4. In the **Edit inbound rule** pop-up, specify the following:

– Name of the rule: UMC IDP NODE SWITCH OFF (SWAC)


– Pattern to use for matching the URL string: Matches the Pattern.


– Using: Regular Expressions.


– Pattern: (.*)


– Specify the action type: Rewrite


– Action properties Rewrite URL: The URL to rewrite, either http or https, local address 127.

0.0.1, the port of reverse proxy, and /umc-sso for example: [http://127.0.0.1:8443/umc-sso](http://vmwin2016rox-0:8443/umc-sso%7BC:2)
[{C:2} (8443 is the standard port to be changed if idp listener port is customized)](http://vmwin2016rox-0:8443/umc-sso%7BC:2)


5. Click **Add** in the conditions area and specify the following conditions in the image below.


User Management Component 2.9.2 - UMC Installation Manual
34

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-34-0.png)


1. Click **OK** .The pop-up is closed.


2. Click **Add** in the **Server Variables** area.


3. Select the **HTTP_COOKIE** server variable from the drop down list and insert {HTTP_COOKIE}
;ReverseProxyHost={SERVER_NAME};ReverseProxyPort={SERVER_PORT} in the value
field.


4. Check the **Replace the existing value** checkbox, then click **OK** .The pop-up is closed.


5. In the action pane click **Apply** .


**4.2.3.2.5 Adding the ServiceLayer to Whitelist**


In order for the WebUi to function correctly you must whitelist the URL of the Service Layer.


**Note:** The computer name, which is case sensitive, must be the same as that which is
specified in the registry key.


**Procedure**


1. Whitelist the URL of the relying party using the **umconf.exe** program. Using either the
_computername/UMC/slwapi/service_ or _computername/UMC/slwapi/service_ and
_computername.userdnsdomain/UMC/slwapi/service._ See _UMCONF User Manual_ for more

details _._


User Management Component 2.9.2 - UMC Installation Manual
35
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-35-0.png)


2. Restart the **UMC Service** .


**4.2.3.2.6 Configuring the Identity Provider Local Configuration**


You must set the values of UMCDllFolderPath, reverseProxy and idpListenerPort in the Identity
Provider local configuration file in order for the identity provider to work.


See Local Configuration File for more information on the configuration file.


**Note:** In order for modifications made to the Local configuration file to take effect you
must restart the UMC Service.


**4.2.3.3 Configuring Integrated Windows Authentication**


The following procedures allows you to configure Integrated Windows Authentication of the Identity
Provider (IdP) so that you can login on the Web UI using the current Windows session (see the _User_
_Management Component Web User Interface Manual_ ). You have to:


1. Enable the Windows Authentication on IIS.


2. Install the Windows Authentication Role Service.


If you want to use Firefox, you must also perform some manual browser configurations.


**Prerequisites**


             - The Identity Provider prerequisites have been satisfied.


             - The machine must be a 64 bit UM ring server or UM server.


**Enabling the Windows Authentication on IIS**


1. Open **IIS Manager** .


2. In the tree on the left select the **IPSimatic-Logon** node.


User Management Component 2.9.2 - UMC Installation Manual
36

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


3. Double click on **Authetication** .

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-36-0.png)


4. Verify that the authentication settings are the following:

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-36-1.png)


5. Right click on the **IPSimatic-Logon** node and select **Add Application** to add the
**WinAuthSite** application, the path is for instance C:\Program Files\Siemens\
UserManagement\web\ipsimatic-logon\WinAuthSite. Then click **OK** .


User Management Component 2.9.2 - UMC Installation Manual
37
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


6. In the tree on the left select the **WinAuthSite** node and set the following authentication
settings.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-37-0.png)


**Installing the Windows Authentication Role Service**


1. Open **Server Manager** .


2. In the tree on the left select the **Web Server (IIS)** node.


3. Install the **Windows Authentication** Role Service.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-37-1.png)


User Management Component 2.9.2 - UMC Installation Manual
38

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**4.2.3.4 Configuring Firefox for Integrated Windows Authentication**


The following procedure allows you to configure Firefox to work with the Integrated Windows
Authentication of the Identity Provider (IdP) so that you can login on the Web UI using the current
Windows session (see the _User Management Component Web User Interface Manual_ ). The string

_<domain>_ can be:


             - equal to the computer name, if the machine on which the IdP is installed does not belong to an
Active Directory domain (example: _myMachine_ );


             - equal to a FQDN (Fully Qualified Domain Name) such as _<computerName>.<domainName>._
_<extension>_, if the machine on which the IdP is installed belongs to an Active Directory domain
(example: _myMachine.siemens.com_ ).


**Prerequisites**


The configurations of IIS for the Integrated Windows Authentication have been performed.


**Procedure**


1. Navigate to the URL **about:config** in Firefox. Click the **I'll be careful, I promise!** button.


2. In the **Search** dialog box, search for the preference **network.negotiate-auth.allow-non-fqdn** .


3. Double click on the property to set the value to **true** and close the window.


**4.2.3.5 Identity Provider Configuration Management**


The following configurations can be specified either locally, or centrally using the set configuration
functionality in UMConf, see the _UMConf User Manual_ for more information on managing the
centralized configuration.


If the IdP has been configured via script these configurations are optional, however if it has been
configured manually you must specify some values in the local configuration file.


Three configuration files are used by UMC Identity Provider:


             - local configuration file: contains a set of data relative to the IdP instance, which must either be
set by running the web configuration .bat or manually, this file can also be used to specify, any
machine specific central configuration overrides.


             - default configuration file: contains the default configuration for the IdP, which is installed by UMC
and cannot be modified, these configurations are used when the configuration is not specified in
either the local or central configuration file.


             - central configuration file: contains the set of configurations which are to be applied to multiple
servers and should be used to set any variations to the default file. Most of the settings present
can be overridden by the local configuration file, if necessary.


Any local or central configuration modification is automatically loaded by the Identity Provider with a
delay of less than 1 minute.


User Management Component 2.9.2 - UMC Installation Manual
39
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-39-0.png)


**Diagram Notes**


             - **Note 1** Some values are only present in the Local Configuration file.


             - **Note 2** Some Central Configurations values cannot be overidden by the Local Configuration

File.


**4.2.3.5.1 Local Configuration File**


The local configuration file allows you to specify the settings which must only be applied to that specific
machine. The file can be found in the subfolder WEB\umc-sso\config and is called configuration.json,
for example: C:\Program Files\Siemens\UserManagement\WEB\umc-sso\config\configuration.json.


You can specify any of the attributes that are present in the default file in the local file. You can also set
override to true to use the configuration specified locally instead of the central configuration.


User Management Component 2.9.2 - UMC Installation Manual
40

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**Note:**

- The values of **clusters**, **enableWhitelist**, **reverseproxy** and **reverseproxyPort**
cannot be overridden by the local configuration if specified in the central
configuration.


- To manually configure the IdP you must set the value of the fields:
**UMCDllFolderPath, reverseProxy** and **idpListenerPort** .


- In order for modifications made to the local configuration file to take effect you
must restart the UMC Service.



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-40-0.png)














|Field|Description|Value|
|---|---|---|
|UMCDllFolderPath|The path of the user management installation, for<br>example "C:/Program Files/Siemens/<br>UserManagement/bin"|This value is propagated<br>by the bat file and must<br>only be modified in the<br>case of manual IdP<br>configuration.|
|useHttps|Specifies whether the HTTPS or HTTP protocol is<br>to be used.|Set to false by default and<br>is for future use only.|
|httpsServerKey|The public key of the https server.|For future use only.|
|httpsServerCert|The public cert of the https server.|For future use only.|
|configurationInterval|Specifies the poling interval on the central<br>configuration and whitelisting. Internal use only.|Default 60000ms and<br>must not be modified.|



User Management Component 2.9.2 - UMC Installation Manual
41
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_












|Field|Description|Value|
|---|---|---|
|idpListenerPort|Specifies the port number of the IDP node.js<br>listener.|Default port number is<br>8443. To modify this<br>option, just pass the<br>custom port number to the<br>**IdP_WebUI_configurator.**<br>**bat** as third parameter.<br>(Configuring UMC Web<br>Components Via Script )|
|reverseProxy|The address of the reverse proxy.||
|reverseProxyPort|The port of the reverse proxy.|Default 443.|
|override|Specifies if the value of the local configuration<br>overwrites the central configuration.|Default is False. Possible<br>values true or false.|



The "logs" section is used to provide a unique point of configuration for the log systems. In the
"Winston" section the configuration for the identity provider **node.js** server log is provided. It logs its
messages in the file called **umc_sso_server.log** . The relative properties are described in the following

table:


**Winston**



|Field|Description|Value|
|---|---|---|
|maxFiles|Maximum number of files generated for this log|The default value is 2|
|maxSize|Maximum dimension of the files that are generated by<br>the log|The value is defined in<br>bytes. The default value<br>is 1000000 bytes ≃ 1<br>Mbytes|
|traceLevel|Minimum severity level of messages to be recorded<br>by the log|The value accepted can<br>be in form of string or ID<br>number:<br>`{`<br>`error: 0,`<br>`warn: 1,`<br>`info: 2,`<br>`verbose: 3,`<br>`debug: 4,`<br>`silly: 5`<br>`}`<br>The logging level are<br>described at the winston<br>page:<br>https://github.com/<br>winstonjs/<br>winston#logging-levels<br>The default value is<br>"error".|


The following is an example of a configured local configuration file.





User Management Component 2.9.2 - UMC Installation Manual
42

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-42-0.png)



**4.2.3.5.2 Default Configuration File**


The default file contains the default configurations which are used if the configurations are not
specified in the central or local files. A copy of this file can created via the UMConf **getdefaultconfig**
command, see _UMConf User Manual_ for more information.



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-42-1.png)





User Management Component 2.9.2 - UMC Installation Manual
43
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-43-0.png)



User Management Component 2.9.2 - UMC Installation Manual
44

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-44-0.png)



User Management Component 2.9.2 - UMC Installation Manual
45
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-45-0.png)




















|Field|Description|Value|
|---|---|---|
|**disclaimerContent**|Contains the text to be<br>displayed for each<br>language.|The disclaimer text for each<br>language. It consists in two letter<br>language code and culture code, for<br>example "de-DE": example text, "en-<br>US": example.|
|**disclaimerEnabled**|Enables the visualization of<br>disclaimers at login.|If set to true the disclaimer is<br>visualized, if set to false (default) the<br>disclaimer is not disabled.|
|**enableWhitelist**|Enables UMC whitelisting.|If set to true (default) whitelisting is<br>enabled, if set to false whitelisting is<br>disabled.|
|**sessionAge**|Specifies the amount of<br>time that passes before the<br>sessions expires.|It is set to 1800000 ms by default.|
|**reverseProxy**|The address of the reverse<br>proxy.|If this value is set on the central<br>configuration the local value is<br>ignored even if the override is set to<br>true.|
|**reverseProxyPort**|The port of the reverse<br>proxy.|443 by default. If this value is set on<br>the central configuration, the local<br>value is ignored even if override is set<br>to true.|
|**ssoService**|The endpoint of the single<br>sign on protocol.|/umc-sso|
|**idpUI**|The address of the IDP UI.|Set to a default value " /ipsimatic-<br>logon/idpauthsite"|
|**maxCachedSessionsPerUser**|The number of sessions<br>which are logged in the<br>cache for each users.<br>When the number of<br>sessions cached exceed<br>the limit the oldest entry is<br>removed.|Set to default value 100. value range<br>from 10-1000.|
|**cookiePath**|The path of the domain in<br>which the cookie is valid.<br>This value must be set in<br>the case of reverse proxy.|Default value "/umc-sso".|



User Management Component 2.9.2 - UMC Installation Manual
46

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_



|Field|Description|Value|
|---|---|---|
|**clusters**|Defines how many node<br>process must be launched.|1 min and the max value should<br>reflect the total number of processor<br>cores.|
|**cookieFlags**|The security level of the<br>session cookies.|•<br>httponly: Internal use only.<br>•<br>secure: Internal use only.<br>•<br>domain: the validity domain of<br>the cookies|
|**languages**|The language which can be<br>selected on the login page.<br>Internal use only.||
|**Authentication options**|(see table below)||
|**Version**|Internal use only.||
|**Label**|Internal use only.||


**Authentication options**










|Field|Description|Value|
|---|---|---|
|**authenticationLevelCredentialsLogin**|Specifies the<br>security level of<br>credential based<br>authentication.|•<br>Weak,<br>•<br>Medium<br>•<br>Strong (by default)|
|**authenticationLevelWindowsLogin**|Specifies the<br>security level of<br>Windows<br>authentication.|•<br>Weak,<br>•<br>Medium<br>•<br>Strong (by default)|
|**enableIWA**|Enables Windows<br>authentication on<br>IdP.|True or false (default).|
|**enablePKI**|Enables Smart<br>Card<br>authentication.|True or false (default).|
|**enableFlexAuth**|Enables Flexible<br>authentication.|True or false (default).|
|**enable2FactorAuth**|Enables two factor<br>authentication.|True or false (default).|



User Management Component 2.9.2 - UMC Installation Manual
47
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_







|Field|Description|Value|
|---|---|---|
|**disableCredentialsLogin**|If set to true the<br>credentials fields<br>are hidden on the<br>IDP page so that<br>only integrated<br>authentication like<br>Teamcenter,<br>Windows or smart<br>card<br>authentication can<br>be used.|True or false (default).|
|**autoLogin**|Enables Autologin.|•<br>Windows authentication: "iwa"<br>•<br>Smart Card authentication:<br>"pki"<br>•<br>Desktop <desktop|<plugin_id><br>•<br>Web <web|<plugin_id><br>•<br>Flex authentication <flexauth:<br><pluginname><br>Multiple authentication methods can<br>be used by dividing each method with<br>"||".<br>"<desktop|<plugin_id>||<desktop|<br><plugin_id>"|


**4.2.3.5.3 Central Configuration File**


The central configuration file contains the configurations that can be applied to multiple machines, any
settings which are set in the central file are used by all the machines in the scenario, unless override is
set to true in the local file.


You can use a UMConf command to retrieve the current central configuration and set a central
configuration. The values which can be set in the central configuration are detailed in the description of
the fields of the default configuration file.


A centralized configuration is set via UMConf or when certain configuration are performed via Web UI,
for example configuring a disclaimer or authentication options.


The following json is an example of central configuration with some configurations which can be set
centrally.



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-47-0.png)







User Management Component 2.9.2 - UMC Installation Manual
48

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-48-0.png)



**4.2.3.6 How to Configure Smart Card (PKI) Authentication**


The following configuration steps must be performed to enable authentication via smart card.


The operations can be performed in any order.


**Workflow**


             - Configure Smart Card Authentication Infrastructure.


             - Configure Smart Card Web Application (not needed if you configure UMC via script).


             - Enable Login via Smart Card Authentication either locally on centrally.


             - Set Account Policy for Smart Card Authentication.


**4.2.3.6.1 Configuring Smart Card Authentication Infrastructure**


**Server side**


The Smart Card Authentication can only be configured on machines where the Identity Provider has
been configured. IIS authentication via certificate must be correctly configured in order for it to function.


User Management Component 2.9.2 - UMC Installation Manual
49
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**Important:**


The following IIS configuration recommendations must be taken into account:


             - checks on the revocation list must be supported;


             - Client Authentication Issuer certificate in the Certificate Manager has to be
installed;


             - the Trusted Root Certification Authorities store has to contain only self signed
certificates;


             - the use of the Client Authentication Issuer on 443 port or on the IdP port has to be

enabled.


**Client side**


The following steps are needed to configure client side Smart Card authentication:


             - smart card drivers must be installed on each client machine;


             - if you use Firefox, the additional configuration for Security Devices must be performed.


**4.2.3.6.2 Configuring Smart Card Web Application**


This procedure is not needed if you have used the **IdP_WebUI_configurator.bat** script to configure
UMC.


**Procedure**


1. Open **IIS Manager** .


2. Right click on the **IPSimatic-Logon** node and select **Add Application** to add the **PkiAuthSite**
application, the path is for instance C:\Program Files\Siemens\UserManagement\web\
ipsimatic-logon\PkiAuthSite. Then click **OK** .


User Management Component 2.9.2 - UMC Installation Manual
50

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


3. In the tree on the left select the **PkiAuthSite** node.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-50-0.png)


4. Double click on **SSL Settings** and set the values as follows.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-50-1.png)


5. To verify that the smart card authentication application is correctly configured, open a browser

instance.


6. Insert a smart card in the smart card reader.


7. Open the page at the following address: https://<address>/umc-idp/pkiauthsite/info.aspx; a
json file opens displaying smart card information.


In case the json file is not correctly displayed, we suggest that you enable on IIS the detailed error
responses and carefully verify smart card authentication infrastructure configuration.


User Management Component 2.9.2 - UMC Installation Manual
51
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**4.2.3.6.3 Setting Account Policy for Smart Card Authentication**


The smart card authentication mechanism is based on a matching between the user data stored on the
smart card and the data stored in UMC.


**Procedure**


1. To configure the data matching, go to the UMC Web UI account policy page with the proper
access rights.


2. Define the field to be retrieved from the smart card to identify the user in UMC.


3. Select either of the following authentication options:


–
**simple authentication (no alias)** : in this case the selected field, CN (Common Name),

Subject, Alternate Subject, is compared with the UMC user name; if they correspond the

user is authenticated.


– **alias authentication** : in this case you have to define an alias for a user in the user detail

dialog; the value stored in the field is compared with the UMC alias, if they correspond the

user is authenticated.


For more information see the account policy documentation in the _User Management Component Web_
_User Interface Manual_ .

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-51-0.png)


**Alternative Operations**


             - You can also define an alias using the dedicated UMX command. See _UMX User Manual_ for

more details.


             - For AD users the alias can be set in the importing phase, for more information see Additional
Provisioning Configuration.


User Management Component 2.9.2 - UMC Installation Manual
52

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**Example**


Consider the following user with the following values:


**User name** = John_Brown


**Alias** = john.brown@mycompany.com


For instance, the following two cases can occur depending on the account policy selection:


             - **Authenticate using CN** : if value stored in the CN in the smart card is John_Brown (UMC user
name value), the user is authenticated; otherwise authentication fails;


             - **Alias Authentication using CN:** if value stored in the CN in the smart card is john.
brown@mycompany.com (UMC alias value), the user is authenticated; otherwise authentication
fails.


**4.2.3.7 Enabling HTTPS in a HTTP UMC Scenario**


Depending on the configurations you have made on the UMC Web components, you have to perform
one of the following alternative procedures:


             - Configure UMC Web components via script ( **IdP_WebUI_configurator.bat** ).


             - Configure UMC Web components manually or customize them.


**Prerequisites**


A UMC Web component is installed and configured on your machine and IIS is **not** configured for
HTTPS.


**Configuring UMC Web components via script (no customization)**


1. Configure IIS for the HTTPS protocol.


2. Launch the script **REMOVE_IdP_WebUI_configurator.bat** . The batch file can be found in C:\
Program Files\SIEMENS\UserManagement\BIN, if the default installation folder is selected.
Note that the script works on a 64 bit machine only.


3. Launch the configuration script **IdP_WebUI_configurator.bat** to configure UMC Web
Components.


**Configuring UMC Web components manually or customizing their configuration**


1. Configure IIS for the HTTPS protocol.


2. If you have performed any modification to the IIS configuration after launching the
configuration script **IdP_WebUI_configurator.bat** or you have configured UMC not using this
script **,** you have to enable HTTP protocol manually .


User Management Component 2.9.2 - UMC Installation Manual
53
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**4.2.3.8 How to Configure Two Factor Authentication by time-based one-time password**


The following configuration steps must be performed to enable two factor authentication by TOTP
(time-based one-time password). It can be used to increase the security level of an authentication

method that would otherwise be standard or weak.


UMC two factor authentication consists in an initial authentication method: Windows or Password

authentication, and token (TOTP), which is encrypted using the user's secret key, in order to elevate
the user's security level to strong.


Two Factor Authentication allows the user to log in with limited access after it has been enabled, so
that the user can generate the initial Secret Key.


**Note:** Two factor authentication by TOTP cannot be enabled for the built-in Administrator
user from the Web UI. It can only be enabled via UMX commands.


**Workflow**


             - Enabling Two Factor Authentication


             - Using Two Factor Authentication


**4.2.3.8.1 Enabling Two Factor Authentication**


The two factor authentication by TOTP can be enabled from the WEB UI or UMX and UMConf.


**Note:** The two factor authentication cannot be enabled for the built-in Administrator user

from the Web UI, it can only be Enabled via UMX commands. In the case of the built-in
Administrator you must generate the first secret via the umx resettotp the command.


**Workflow**


             - SADS has been enabled in Account Policies via WEB UI or UMX.


             - Enable the two factor authentication in authentication options via WEB UI or centralized
configuration management.


             - Two Factor authentication has enabled for the user in their account policies via Web or
encryption has been enabled for the user from UMX.


**Enabling SADS from the Web UI**


1. Login to UMC Web with user who has UM admin role.


2. From the menu on the upper right-hand corner of **UMC Home page**, select **Account Policies** .
The **Account Policies** page is displayed.


3. In the **Advanced** tab, select the **Enable secure application data support for users and**
**groups** check box to enable the SADS functionality. SADS capabilities at application level can


User Management Component 2.9.2 - UMC Installation Manual
54

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


be enabled via **umx** or Web UI by modifying an account policy. For more details, see _UMX_

_User Manual_ .


4. Click **Save** .


**Enabling Two Factor Authentication as an Authentication method**


1. Login to UMC Web with user who has UM admin role.


2. Select the **Authentication Options** tab.


3. Select the enable two factor authentication check box.


4. Click **Save all changes to configuration settings** .


**Enabling Two Factor Authentication for a user**


1. From the **Users** page, select a row and click **Details** in the upper left-hand corner of the grid.


2. Select the **Account Policies** tab.


3. Select the **Enable 2FA** checkbox.


4. Click **Save** .


**4.2.3.8.2 Using Two Factor Authentication**


Two factor authentication by TOTP allows you to increase the security level of a login which has been
performed using a method that would otherwise be weak or medium.


When 2FA is enabled the user is prompted to provide a token after logging in the second time, the first
time the user logs in they are granted access in order to retrieve the secret key.


**Workflow**


1. Log in using an authentication methods which is either weak or standard.


2. The second time you login the you will be asked for a TOTP (time-based one-time password).


3. Generate a TOTP (time-based one-time password) using the previously retrieved secret key.


4. Insert the password and click **Sign in.**


**Generating and Resetting Secret Keys**


Access the Web UI, then from the menu on the upper right-hand corner of **UMC Home page**, select
**User Profile** or click **User Profile** link button on the welcome page. The **User Profile** page is
displayed.


User Management Component 2.9.2 - UMC Installation Manual
55
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-55-0.png)


**Prerequisites**


             - SADS has been enabled in Account Policies via Web (see How to Manage Account Policies in
the _UMC Web UI User Manual_ ) or UMX.


             - The Two Factor Authentication has been enabled as an authentication method via Web (see
Configuring Authentications Options in the _UMC Web UI User Manual_ ) or UMConf centralized
configuration management.


             - The Two Factor authentication has enabled for the user in their account policies via Web (see
Editing User Account Policies in the _UMC Web UI User Manual_ ) or Encryption has been
enabled for the user from UMX.


**Procedure**


1. Click the **Manage 2FA** tab.


2. Click **Display QR Code.**


3. If required, click **Show Secret Key** or **Reset Secret Key.**


**4.2.4 Installing and Configuring UMC Station Client**


**CAUTION:**


No checks are currently performed at setup level on the UMC station client installation.
Over-installation of the UMC station client causes serious system malfunction. In
particular you must not install the UMC station client on a machine where you have
already installed full UMC.


UMC Station Client can be configured:


             - via script.


User Management Component 2.9.2 - UMC Installation Manual
56

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**Prerequisites**


             - The Windows user logged in must have administrative rights.


             - Full UMC installation or UMC station client has been executed on your machine. During the
installation you have simply to proceed with the wizard.


             - The UMC Web UI has to be properly configured for the UMC system in HTTPS, see Configuring
Web UI. HTTPS is mandatory, therefore a valid SSL certificate must have been acquired from a
Certification Authority or a self-signed SSL certificate has been created.


**Configuring UMC Station Client via Script**


1. Launch the **regx.ps1** script located in the subdirectory \BIN of the 32 bit installation folder.


2. The script requires the following parameters:

– **UMC Server name** (only a ring master);


– **user** (who must own the **UM_REGCLIENT** function right);


– **password** .


3. The script additionally supports the following optional parameters:

– **workstationAlias** (alias used in registration phase, instead of hostname; alias cannot

contain special characters)


– **force** (force registration for an alias already registered)


–
**update** (update registration for a client already registered)


**Result**


The system registers the machine as a UMC station client machine that provides a claim in which
certified logon station details are included.


**4.2.5 Configuring SLRA support**


UMC provides Simatic Logon Remote Authentication support.


**Prerequisites**


             - The machine is configured as a UMC ring server or server.


**Procedure**


1. Open the Registry Editor, navigate to **HKLM\SOFTWARE\SIEMENS\User Management.**


2. Right-click on the node, select **New > Key** and insert the **slra** key.


3. Right-click on the **slra** node, select **New > Key** and insert the **settings** key .


4. Right-click on the **settings** node, select **New > DWORD Value.**


User Management Component 2.9.2 - UMC Installation Manual
57
A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


5. Double-click on the newly inserted value and set as Value name the string **enabled** and as
**Value data 1 to enable SLRA.**

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-57-0.png)


6. Right-click on the **slra** node, select **New > Key** and insert the **communication** key .


7. Right-click on the **communication** node, select **New > DWORD Value**


8. Double-click on the newly inserted value and set as Value name the string **secure** and as
**Value data 1 to enable secure communication via TLS** or **0 if TLS is not required**


9. Right-click on the **communication** node, select **New > DWORD Value**


10. Double-click on the newly inserted value and set as Value name the string **localonly** and as
**Value data 0 for enabling remote communication**, **1 if no remote communication must**

**be allowed** .

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-57-1.png)


**Note: Certificates**


In case TLS is required, create the certificates ad save them in the default certificate
folder **CERT/SLRAUTH** under C:\ProgramData\Siemens\UserManagement.


The default certificate path folder **CERT/SLRAUTH** inherits the access rights of parent
**CERT** folder. The folder permissions must be modified if required.


User Management Component 2.9.2 - UMC Installation Manual
58

A5E50361197-AA


_4 How to Configure UMC_
_4.2 How to Configure a UMC Scenario_


**Certificates path and names**


Additionally, you can override the folder path and the certificate name using the following settings:


1. Right-click on the **communication** node, select **New > STRING Value** .


2. Double-click on the newly inserted value and set as Value name the string **certAbsolutePath**
and as **Value the path where certificates are stored** .


3. Right-click on the **communication** node, select **New > STRING Value** .


4. Double-click on the newly inserted value and set as Value name the string **certFileName** and
as **Value the certificate file name** .


5. Right-click on the **communication** node, select **New > STRING Value** .


6. Double-click on the newly inserted value and set as Value name the string **certKeyFileName**
and as **Value the certificate file name** .

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-58-0.png)


**4.2.6 Configuring Desktop Single Sign On**


**Prerequisites**


             - The machine is configured as a UMC ring server or server .


             - UMC Web components are configured on the machine with HTTPS.


**Procedure**


To enable Desktop Single Sign On:


             - Use the UMCONF utility, s ee _UMCONF User Manual_ for more details.


User Management Component 2.9.2 - UMC Installation Manual
59
A5E50361197-AA


## **5 Configuring the Identity Provider in a High** **Availability/Reliability Scenario**

The high availability and reliability of the Identity Provider (IdP) is supported thanks to the Network
Load Balancing (NLB) technology. Network Load Balancing is a clustering technology that enhances
the scalability and availability of TCP/IP-based services such as Web applications (i.e. UMC Identity
Provider). To scale performance, the NLB distributes the incoming IP traffic over several web servers
by using a virtual IP address, and a reverse proxy which must be specified in the UMC central
configuration, for the entire Web server group and rerouting client requests to the servers of the group.
Each server is characterized by a network address that identifies the entire group and a dedicated
network address. It also ensures high availability by detecting host failures and automatically
redistributing traffic to the surviving hosts.


UMC specific information on NLB configuration can be found in the following sections:


             - High Availability/Reliability General Issues


             - NLB and Health State Integration

##### **5.1 High Availability/Reliability General Issues**


             - The level of availability/reliability of the system depends on many factors, such as the IT
infrastructure, the redundancy of the UMC architecture, the adopted NLB service and session
state provider.


             - The choices related to the previous factors have a deep impact on the system security. The triad
of the security quality attributes is granted as follows:


–
_integrity_, the assurance that the information is trustworthy and accurate, is granted by our

system;


–
_confidentiality_, a set of rules that limits access to information, is granted thanks to third party

software that manage redundancy, such as NLB;


–
_availability_, the reliable access to the system by authorized people, is granted thanks to

third party software that manage redundancy, such as NLB.


             - If you want to have the Integrated Windows Authentication mechanism working properly without
asking user credentials, you have to use Kerberos in order to authenticate against IIS. Kerberos
requires a specific configuration in an NLB scenario. Refer to Microsoft Technical documentation

                                                                             for more details (see for instance [http://blogs.msdn.com/b/vivekkum/archive/2008/06/15/step](http://blogs.msdn.com/b/vivekkum/archive/2008/06/15/step-by-step-kerberos-in-nlb-with-shared-content.aspx)
[by-step-kerberos-in-nlb-with-shared-content.aspx).](http://blogs.msdn.com/b/vivekkum/archive/2008/06/15/step-by-step-kerberos-in-nlb-with-shared-content.aspx)


User Management Component 2.9.2 - UMC Installation Manual
60

A5E50361197-AA


_5 Configuring the Identity Provider in a High Availability/Reliability Scenario_


_5.2 Health State Service_


            - If you configure a Reverse Proxy in order to use multiple web servers you must increase the
value of the query string length on all the web servers, via IIS Manager to the values specified in


the following screenshot.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-60-0.png)


            - UMC WEB UI does not support NLB with more than one node, except if you use session affinity.

##### **5.2 Health State Service**


UMC Health State is an HTTP/HTTPS service that provides information on the health state of the
authentication via UMC Identity Provider. The protocol depends on IIS configuration.


The value of the health state is contained in the field **status** of the HTTP response header:


            - **status** = 200, the authentication can be performed successfully;


            - **status** = 404, the authentication cannot be performed.


The health state information is derived from the one provided by the Health Check Service described in
UMC Release Notes.


**Example URL**





User Management Component 2.9.2 - UMC Installation Manual
61
A5E50361197-AA


_5 Configuring the Identity Provider in a High Availability/Reliability Scenario_
_5.3 NLB and Health State Integration_

##### **5.3 NLB and Health State Integration**


UMC health state service can be used in a high availability/reliability scenario based on NLB
technology to start/stop the use of UMC machines running the Identity Provider according to the result
provided by the health state. We here provide an example script developed in PowerShell that queries
the status of a node and stops or starts it according to UMC status using Microsoft Windows Server
NLB powershell commands. The script can be scheduled to run periodically via Windows task

scheduler.


**PowerShell Script Example**


**CAUTION:**


The sample code is provided for illustrative purposes only. It has not been thoroughly
tested under all conditions. Therefore, we cannot guarantee or imply its reliability,
serviceability, or function.


In the example two machines VM-UMC-N1 and VM-UMC-N2 are configured in NLB and their status is
checked via the PowerShell function **CheckNodeHS** . According to the status, the node is stopped or

started.


**CheckNodeHS**



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-61-0.png)



User Management Component 2.9.2 - UMC Installation Manual
62

A5E50361197-AA


_5 Configuring the Identity Provider in a High Availability/Reliability Scenario_

_5.3 NLB and Health State Integration_



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-62-0.png)



**Script**



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-62-1.png)





User Management Component 2.9.2 - UMC Installation Manual
63
A5E50361197-AA


## **6 How to Upgrade to UMC 2.9 SP2**

The following describes how to upgrade to the latest version of UMC from all previous versions of
UMC, see the version specific notes as some versions require additional steps.


A prior version of UMC is installed and configured on all the machines in the scenario you need to
upgrade. If a previous version of UMC is only installed and not configured, you simply have to install
and configure UMC as if it were the first installation.


**Prerequisites**


             - Follow the general recommendations for UMC upgrade.


**Workflow**


1. Upgrade UM secondary ring server.


2. Upgrade UM priority ring server.


3. Upgrade all the UM servers giving precedence to the ones belonging to the NLB cluster.


4. Upgrade all the UM agents.


5. Upgrade all the UMC station clients.


**Note:** If you use Web UI, you must clear the browser cache on all the machines which

access the web UI.

##### **6.1 General Recommendations**


In this page you can find a set of notes guidelines which must be followed to upgrade UMC correctly.


**Before You Start**


             - To check the machine role you can use the umconf **Show Status** command. See the _UMCONF_
_User Manual_ for more details.


             - During the upgrade procedure, no UMC commands can be executed except those which are
part of the procedure.


**Version Specific Notes**


This section contains a list of notes which only apply when upgrading from specific versions of UMC.


User Management Component 2.9.2 - UMC Installation Manual
64

A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_


_6.1 General Recommendations_


            - Upgrading from 1.0: If you have installed and configured UMC 1.0, you have first to upgrade to
UMC 1.1 (see UMC 1.1 Release Notes) and then upgrade the system.


            - Upgrading from 1.1: If you have installed UMC 1.1 in a HTTP scenario, you have to convert the
scenario from HTTP to HTTPS after upgrading.


            - Upgrading from versions prior to 1.6: Mixed version scenarios may encounter issues if a user
name which is longer than 30 characters is used. We strongly suggest that you align the
installations to the most recent UMC version.


            - Upgrading from versions prior to 1.9.1: As of 1.9.1 the value of the global account policy
Password Expiration cannot exceed 1827 days. If the value was set in excess of 1827, you
must re-set the value after upgrading.


            - Upgrading from versions prior to 2.0: As the IdP underwent substantial changes, once you have
upgraded your installation you must redo any settings which were performed on the webconfig,
see Migrating IdP Configurations.


            - Upgrading from versions prior to 2.0 on UM servers and the secondary ring server the Web
Component configuration script cannot update the whitelisting. UM Servers and the secondary
rings server must be added to whitelisting using UMConf on the primary ring server.


            - Upgrading from versions prior to 2.0 verify the prerequisites are met: Application Request
Routing and its prerequisites have been downloaded and installed (For iis 8 and above: [https://](https://www.microsoft.com/en-us/download/details.aspx?id=47332)
[www.microsoft.com/en-us/download/details.aspx?id=47332).](https://www.microsoft.com/en-us/download/details.aspx?id=47332)


**Long Term Mixed Version Scenarios**


The following notes are relative to long term mixed version scenarios, which is a scenario where the
version of UMC installed is not the same on all the machines in the scenario:


            - As of UMC 1.9 we support long-term mixed distributed scenarios. If you have a scenario with a
version which is prior to 1.9, you must upgrade all the UMC installations to at least UMC 1.9.


            - Long term mixed versions are not supported on ring severs, therefore the version of UMC
installed on ring servers must be aligned as quickly as possible.


**6.1.1 Migrating IdP Configurations**


When migrating from versions prior to UMC 2.0, as the IdP underwent substantial changes, once you
have upgraded your installation you must redo any settings which were performed on the webconfig.


Where the following configurations correspond to configurations which are present in the new IdP.






|Functionality|Old web config|New IdP json file|
|---|---|---|
|Enable Login via Smart Card<br>Authentication|EnablePKI|(Disabled by<br>default) see,<br>Identity Provider<br>Configuration<br>Management.|
|Enable Login via Cookie Adapter or<br>Custom Plugin|EnableFlexAuth|(Disabled by<br>default) see,<br>Identity Provider<br>Configuration<br>Management.|



User Management Component 2.9.2 - UMC Installation Manual
65
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.2 Upgrading UM Secondary Ring Server_


















|Functionality|Old web config|New IdP json file|
|---|---|---|
|Disable and Hide Window Authentication<br>Link|EnableIWA|(Enabled by<br>default) see,<br>Identity Provider<br>Configuration<br>Management.|
|Enable the Automatic Login|AutoLoginMode|See, Identity<br>Provider<br>Configuration<br>Management.|
|Disable the use of the Logon Station in<br>Claims|EnableLogonStation|N/A it is now<br>always enabled.|
|Enable the Identity Provider Log|LogFileName|N/A it is now<br>always enabled<br>and saved in the<br>um-sso log which<br>can be found, for<br>example, in C:\<br>ProgramData\<br>Siemens\<br>UserManagement\<br>Log|
|Enable the Use of Paths in Cookies|ClaimIssuerAuthority|N/A it is now<br>always enabled.|
|Enable the Use of Whitelisting|EnableWhitelistMembershipService|It is now enabled<br>by default, see<br>Identity Provider<br>Configuration<br>Management.|
|Enabling Anti Forgery Token|UseAntiForgeryToken|N/A|
|Disable the Display of the Security<br>Disclaimer|UseDisclaimerMessage|N/A|


##### **6.2 Upgrading UM Secondary Ring Server**

**General Recommendations**


             - During the upgrading procedure only the priority ring server is available; thus, for a minimum
amount of time, you do not have system redundancy support.


             - During the upgrading procedure, session loss may occur.


             - The Primary Ring Server and Secondary Ring Server do not support long term mixed version,
and therefore the installations must be aligned as soon as possible.


User Management Component 2.9.2 - UMC Installation Manual
66

A5E50361197-AA


**Procedure**



_6 How to Upgrade to UMC 2.9 SP2_
_6.3 Upgrading UM Priority Ring Server_


1. If NLB is configured, remove the secondary ring server from the NLB cluster.


2. If UMC Web components were configured on the machine, run the
**Remove_IdP_WebUI_configuration.bat.**


3. Close all the running applications.


4. Launch the installer and select to upgrade the system. In case the installation asks you to
reboot the system, perform the system reboot. When the system reboots the installer
automatically starts.


5. Run the command **umconf -U** to upgrade the system. Refer to the _UMCONF User Manual_ for

more details


6. If UMC Web components were configured on the machine:

– Run the **IdP_WebUI_configurator.bat** or manually configure the IdP.


– Manually perform Identity Provider **web.config** customization on the .json configuration

file,


7. If NLB was configured:

– reconnect the machine to the NLB cluster;


– remove the priority ring server and all the other UM servers (if any) from the NLB cluster.


8. if an upgrade is made to version 2.7 SP1, run the command: **sc config "up service"**
**depend="UMC service"** to add the correct dependency to the UPSERVICE.


**Note:** If you use Web UI clear the browser cache on all the machines which access the

web UI.


##### **6.3 Upgrading UM Priority Ring Server**

**General Recommendations**


             - During the upgrading procedure only the secondary ring server is available; thus, for a minimum
amount of time, you do not have system redundancy support and UMC database modifications
are not possible.


             - During the upgrading procedure, session loss may occur.


             - The Primary Ring Server and Secondary Ring Server do not support long term mixed versions,
and therefore the installations must be aligned as soon as possible.


**Procedure**


1. If UMC Web components were configured on the machine run the
**Remove_IdP_WebUI_configuration.bat.**


2. Close all the running applications.


3. Launch the installer and select to upgrade the system. The system may ask you to reboot
before or after upgrading UMC, in which case you must perform the system reboot. If the


User Management Component 2.9.2 - UMC Installation Manual
67
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.4 Restarting UM Secondary Ring Server_


reboot is performed before upgrading the installer will automatically starts when the system

reboots.


4. Run the command **umconf -U** to upgrade the system. Refer to the _UMCONF User Manual_ for

more details.


5. If UMC 1.1 is installed in a standalone scenario in HTTP and you want to enable HTTPS
upgrading to UMC 1.4, then you have to perform this additional procedure.


6. If UMC Web components were configured on the machine:

– Run the **IdP_WebUI_configurator.bat** or manually configure the IdP.


– Manually perform Identity Provider **web.config** customizations on the .json configuration

file,


7. If NLB was configured, reconnect the machine to the NLB cluster.


8. If an upgrade is made to version 2.7 SP1, run the command: **sc config "up service"**
**depend="UMC service"** to add the correct dependency to the UPSERVICE.


If you use Web UI clear the browser cache on all the machines which access the web UI.

##### **6.4 Restarting UM Secondary Ring Server**


If the certificates validity is already closer than two years to the expiration date, a restart of UM
Secondary Ring Server is needed after the upgrade of UMC Primary Ring server, in order to execute
the automatic certificate renewal in the right order. See Performing the Automatic Certificates Renewal
for details.

##### **6.5 Upgrading UM Server**


**General Recommendations**


             - During the upgrading procedure, session loss may occur.


**Procedure**


1. If UMC Web components were configured on the machine, stop the application pools of the
UMC applications in **IIS Manager** and run the **Remove_IdP_WebUI_configuration.bat.**


2. Close all the running applications.


3. Launch the installer and select to upgrade the system. In case the installation prompts you to
reboot the system, perform the system reboot. When the system reboots, the installer
automatically starts.


4. Run the command **umconf -U** to upgrade the system. Refer to the _UMCONF User Manual_ for

more details.


5. If UMC Web components were configured on the machine:

– Run the **IdP_WebUI_configurator.bat** or manually configure the IdP.


User Management Component 2.9.2 - UMC Installation Manual
68

A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_


_6.6 Upgrading UM Agent_


– Manually perform Identity Provider **web.config** customizations on the .json configuration

file,


6. If the UM server was connected to NLB cluster, reconnect the machine to the cluster.


7. if an upgrade is made to version 2.7 SP1, run the command: **sc config "up service"**
**depend="UMC service"** to add the correct dependency to the UPSERVICE.

##### **6.6 Upgrading UM Agent**


**Procedure**


1. Close all the running applications.


2. Launch the installer and select to upgrade the system. In case the installation prompts you to
reboot the system, perform the system reboot. When the system reboots the installer
automatically starts.


3. Run the command **umconf -U** to upgrade the system. Refer to the _UMCONF User Manual_ for

more details.

##### **6.7 Upgrading UMC Station Client**


**Procedure**


1. Close all the running applications.


2. Launch the installer and select to upgrade the system. In case the installation prompts you to
reboot the system, perform the system reboot. When the system reboots the installer
automatically starts.


**Result**


The machine is automatically registered and no additional steps are needed.

##### **6.8 Upgrading the Web Components Manually**


To configure the web components manually after an upgrade you must perform the configurations

described below.


**Workflow**


1. Configuring Identity Provider


User Management Component 2.9.2 - UMC Installation Manual
69
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


2. Configuring Web UI and Service Layer API


3. Configuring Remote Authentication


4. Configuring URL Rewrite Rules


5. Configure Upgrade-Specific URL Rewrite Rules


6. Adding the IdP to Whitelisting


7. Configuring the Identity Provider


**6.8.1 Upgrade - Configuring Identity Provider**


**Prerequisites**


             - The Identity Provider prerequisites have been satisfied.


             - The machine must be a 64 bit UM ring server or UM server.


**Procedure**


1. Open **IIS Manager** .


2. In the tree on the left select the **Application Pools** node.


3. Right click on the node and select **Add Application Pool** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-69-0.png)


4. Insert the parameters as displayed in the previous image and click **OK** .


5. In the tree on the left select the **Default Web Site** node.


User Management Component 2.9.2 - UMC Installation Manual
70

A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


6. Right click on the node and select **Add Application** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-70-0.png)


7. Insert the parameters as displayed in the previous image and click **OK** . The path varies
depending on where UMC is installed, for example C:\Program Files\Siemens\
UserManagement\web\ipsimatic-logon.


8. On the applications pool page select the newly created application pool, and click **Manage**
**Application**            - **Advanced Settings** .


9. Set to 0 the field **Regular Time Interval (minutes)** and click **OK** .

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-70-1.png)


**6.8.2 Upgrade - Configuring Web UI**


**Important:**


UMC contains two IIS 64 bit Native Modules: **um.ra.dll** and **um.slvm64.dll**


User Management Component 2.9.2 - UMC Installation Manual
71
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


**Prerequisites**


             - The prerequisites have been satisfied.


             - The machine must be a 64 bit UM ring server or UM server.


             - The Identity Provider (IdP) has been correctly configured.


**Procedure**


1. Open the **Registry Editor** .


2. In the tree on the left go to the **HKLM\SOFTWARE\SIEMENS\User Management\WebUI\**
**Settings** node.


3. Double click on idpaddress and change **Value data** to the complete IdP URL, for example if
the IdP is located on the local machine: [https://FQDNmachinename/umc-sso](https://FQDNlocalmachinename/umc-sso) or [https://](https://reverseproxyadress/umc-sso)
[reverseproxyadress/umc-sso](https://reverseproxyadress/umc-sso) for complex scenarios like NLB scenarios. Depending on the IdP
configuration the URL may start with **http** or **https** .


4. In the tree on the left go to the **HKLM\SOFTWARE\SIEMENS\User Management\CERT**
**Library\Domain** node.


5. Right click on the **Domain** node, select **New > String Value** and insert the name **Web** .


6. Close the **Registry Editor** .


7. Open **IIS Manager** .


8. In the tree on the left select the **Application Pools** node.


9. Right click on the node and select **Add Application Pool** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-71-0.png)


10. Insert the parameters as displayed in the previous image and click **OK** .


11. In the tree on the left go to the **Default Web Site** node.


User Management Component 2.9.2 - UMC Installation Manual
72

A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


12. Right click on the node and select **Add Application** : the following dialog opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-72-0.png)


13. Insert the parameters as displayed in the previous image and click **OK** . The path of the
application is, for example C:\Program Files\Siemens\UserManagement\WEB\Umc.


14. To verify that the application works properly, in the tree on the left go to the **UMC** node.


15. Right click on the node and select **Manage Application > Browse** . The Web UI application
opens displaying the login page.


**6.8.3 Upgrade - Configuring Remote Authentication**


**Prerequisites**


             - The general UMC prerequisites have been satisfied.


             - The machine must be a 64 bit UM ring server or UM server.


**Procedure**


1. Open **IIS Manager** .


2. In the tree on the left go to the root node.


3. On the right area of the screen double click on **Modules** .


User Management Component 2.9.2 - UMC Installation Manual
73
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


4. On the top right corner click on **Configure Native Modules** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-73-0.png)


5. Click on **Register** : the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-73-1.png)


6. Insert the parameters as displayed in the previous image and click **OK.**


7. Click on **Register** again: the following dialog box opens.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-73-2.png)


8. Insert the parameters as displayed in the previous image.


9. Once you have added the module make sure they are not selected and click **OK.**


10. Click **Modules** under the **UMC** application.


11. On the top right corner click on **Configure Native Modules.**


12. Select the **UserManagementServiceLayer module** checkbox then click **OK** .


13. Click **Modules** under the **ra** application, if ra is not present see note.


14. On the top right corner click on **Configure Native Modules** .


15. Select the **ra module** checkbox then click **OK.**


User Management Component 2.9.2 - UMC Installation Manual
74

A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


**Note:** If the ra application is not already present:


1. create a folder under the WEB ( for example C:\Program Files\Siemens\
UserManagement\WEB folder called _ra._


2. add an application to the default site called "ra" specifying the path of the folder
created in the previous step.


**6.8.4 Upgrade - Configuring URL Rewrite Rules**


You must manually configure the following URL rewrite rules in IIS.


**Procedure**


1. Go to **IIS Manager** .


2. In the **Connections** pane, select your server and then the top level site.


3. In the **Site** pane, double-click **URL rewrite.**


4. In the **Actions** pane, click **View Server Variables.**


5. Click **Add...** and specify _[http cookie]._


6. Go to the **Server** pane, double-click **Application Request Routing Cache** .


7. In the **Actions** pane, click **Server Proxy Settings** .


8. On the **Application Request Routing** page, select **Enable proxy** .


9. Check that the **Reverse rewrite host in response header** flag is false. It is recommended to
set it as false in the case of a physics reverse proxy or in case you want to define a specific
domain of the cookies.


10. In the **Actions** pane, click **Apply** .


11. In the **Server pane**, double-click **URL Rewrite** .


12. In the **Actions pane** on the right-hand side, click **Add rules** .


13. In the **Add Rules** dialog box, select **Blank Rule** and click **OK** .


14. In the **Edit inbound rule** pop-up, specify the following:

– Name of the rule: UMC SSO Static


– Pattern to use for matching the URL string: Matches the Pattern.


– Using: Regular Expressions.


– Pattern: (.*)


– Specify the action type: Rewrite


– Action properties Rewrite URL: The URL to rewrite, either http or https, local address 127.

0.0.1, the port of reverse proxy, and /umc-sso for example: [http://127.0.0.1:8443/umc-sso](http://vmwin2016rox-0:8443/umc-sso%7BC:2)
[{C:2} (8443 is the standard port to be changed if idp listener port is customized).](http://vmwin2016rox-0:8443/umc-sso%7BC:2)


User Management Component 2.9.2 - UMC Installation Manual
75
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


15. Click **Add** in the conditions area and specify the values in the image below.

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-75-0.png)


16. Click **OK** .The pop-up is closed.


17. Click **Add** in the **Server Variables** area.


18. Select the **HTTP_COOKIE** server variable from the drop down list and insert {HTTP_COOKIE}
;ReverseProxyHost={SERVER_NAME};ReverseProxyPort={SERVER_PORT} in the value
field.


19. Check the **Replace the existing value** checkbox, then click **OK** .The pop-up is closed.


20. In the action pane click **Apply** .


**Procedure: ADD IDP Legacy rule**


1. In the **Server pane**, double-click **URL Rewrite** .


2. In the **Actions pane** on the right-hand side, click **Add rules** .


3. In the **Add Rules** dialog box, select **Blank Rule** and click **OK** .


4. In the **Edit inbound rule** pop-up, specify the following:

– Name of the rule: UMC IDP NODE SWITCH OFF


– Pattern to use for matching the URL string: Matches the Pattern.


– Using: Regular Expressions.


– Pattern: (.*)


– Specify the action type: Rewrite


– Action properties Rewrite URL: The URL to rewrite, either http or https, local address 127.

0.0.1, the port of reverse proxy, and /umc-sso for example: [http://127.0.0.1:8443/umc-sso](http://vmwin2016rox-0:8443/umc-sso%7BC:2)
[{C:2} (8443 is the standard port to be changed if idp listener port is customized)](http://vmwin2016rox-0:8443/umc-sso%7BC:2)


5. Click **Add** in the conditions area and specify the following conditions in the image below.


User Management Component 2.9.2 - UMC Installation Manual
76

A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-76-0.png)


1. Click **OK** .The pop-up is closed.


2. Click **Add** in the **Server Variables** area.


3. Select the **HTTP_COOKIE** server variable from the drop down list and insert {HTTP_COOKIE}
;ReverseProxyHost={SERVER_NAME};ReverseProxyPort={SERVER_PORT} in the value
field.


4. Check the **Replace the existing value** checkbox, then click **OK** .The pop-up is closed.


5. In the action pane click **Apply** .


**Procedure: ADD SWAC Legacy rule**


1. In the **Server pane**, double-click **URL Rewrite** .


2. In the **Actions pane** on the right-hand side, click **Add rules** .


3. In the **Add Rules** dialog box, select **Blank Rule** and click **OK** .


4. In the **Edit inbound rule** pop-up, specify the following:

– Name of the rule: UMC IDP NODE SWITCH OFF (SWAC)


– Pattern to use for matching the URL string: Matches the Pattern.


– Using: Regular Expressions.


– Pattern: (.*)


– Specify the action type: Rewrite


– Action properties Rewrite URL: The URL to rewrite, either http or https, local address 127.

0.0.1, the port of reverse proxy, and /umc-sso for example: [http://127.0.0.1:8443/umc-sso](http://vmwin2016rox-0:8443/umc-sso%7BC:2)
[{C:2} (8443 is the standard port to be changed if idp listener port is customized)](http://vmwin2016rox-0:8443/umc-sso%7BC:2)


5. Click **Add** in the conditions area and specify the following conditions in the image below.


User Management Component 2.9.2 - UMC Installation Manual
77
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-77-0.png)


1. Click **OK** .The pop-up is closed.


2. Click **Add** in the **Server Variables** area.


3. Select the **HTTP_COOKIE** server variable from the drop down list and insert {HTTP_COOKIE}
;ReverseProxyHost={SERVER_NAME};ReverseProxyPort={SERVER_PORT} in the value
field.


4. Check the **Replace the existing value** checkbox, then click **OK** .The pop-up is closed.


5. In the action pane click **Apply** .


**6.8.4.1 Upgrade - URL Rewrite Rules**


Following the procedure described above repeat from step 8 adding two rules with their relative

conditions:


**UMC IDP Node Switch Off Rule**


             - Name of the rule: UMC IDP Node switch off


             - Pattern to use for matching the URL string: Matches the Pattern.


             - Using: Regular Expressions.


             - Pattern: (.*)


             - Specify the action type: Rewrite


             - Action properties Rewrite URL: The url to rewrite, either https or https, the FQDN or machine
name, the port of reverse proxy, the port of the reverse proxy, and /umc-sso for example: [http://](http://vmwin2016rox-0:8443/umc-sso%7BC:2)


User Management Component 2.9.2 - UMC Installation Manual
78

A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


[mymachine-0:8443/umc-sso{C:2}](http://vmwin2016rox-0:8443/umc-sso%7BC:2)

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-78-0.png)


**UMC IDP Node Switch Off Rule (SWAC)**


             - Name of the rule: UMC IDP Node switch off (swac)


             - Pattern to use for matching the URL string: Matches the Pattern.


             - Using: Regular Expressions.


             - Pattern: (.*)


             - Specify the action type: Rewrite


             - Action properties Rewrite URL: The url to rewrite, either https or https, the FQDN or machine
name, the port of reverse proxy, the port of the reverse proxy, and /umc-sso for example: [http://](http://vmwin2016rox-0:8443/umc-sso%7BC:2)
[mymachine-0:8443/umc-sso{C:2}](http://vmwin2016rox-0:8443/umc-sso%7BC:2)

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-78-1.png)


**6.8.5 Upgrade - Adding the IdP to Whitelisting**


For the WebUI to function correctly you must whitelist the URL of the Service Layer.


The computer name, which is case sensitive, must be the same as that which is specified in the
registry key.


User Management Component 2.9.2 - UMC Installation Manual
79
A5E50361197-AA


_6 How to Upgrade to UMC 2.9 SP2_
_6.8 Upgrading the Web Components Manually_


**Note:** When upgrading from versions prior to 2.0 you must add the Service Layer of the
secondary ring server and any UM servers to whitelisting on the Primary Ring Server.


**Procedure**


1. Whitelist the URL of the relying party using the **umconf.exe** program. Using either the
_computername/UMC/slwapi/service_ or _computername/UMC/slwapi/service_ and
_computername.userdnsdomain/UMC/slwapi/service._ See _UMCONF User Manual_ for more

details _._



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-79-0.png)



2. Restart the **UMC Service** .


**6.8.6 Upgrade - Configuring the Identity Provider**


You must set the values of UMCDllFolderPath, reverseProxy and idpListenerPort in the Identity
Provider local configuration file in order for the identity provider to work.


See Local Configuration File for more information on the configuration file.


**Note:** In order for modifications made to the Local configuration file to take effect you
must restart the UMC Service.


User Management Component 2.9.2 - UMC Installation Manual
80

A5E50361197-AA


## **7 How to Uninstall UMC**

Depending on the UMC installation, follow either of these procedures:


             - Uninstall Full UMC


             - Unistall UMC Station Client

##### **7.1 Uninstalling Full UMC**


**CAUTION:**


If UMC is also configured, the database files are not removed by the uninstallation
procedure. This procedure has to be performed on all the machines, UM ring servers, UM
servers and agents. We suggest that you perform the procedure on the UM agents first.


**Procedure**


1. If the machine is a 64 bit ring server where the Web Components have been configured,
launch the script **REMOVE_IdP_WebUI_configurator.bat** . The batch file can be found in C:\
Program Files\SIEMENS\UserManagement\BIN, if the default installation folder is selected.
Note that the script works on a 64 bit machine only.


2. Delete the database files, the registry entries and so on by executing the **umconf** -D -f
command, installed in the subdirectory **\BIN** (for example C:\Program Files\Siemens\
UserManagement\BIN). Please refer to the _UMCONF User Manual_ for more details.


3. Open **Program and Features** from the **Control Panel** .


4. Select the **UMC** entry and right click.


5. Select **Uninstall** .


6. The uninstall setup is launched: proceed with the uninstallation steps.

##### **7.2 Uninstalling UMC Station Client**


**Procedure**


1. Open **Program and Features** from the **Control Panel** .


2. Select the **UMC Station Client** entry and right click.


3. Select **Uninistall** .


4. The uninstall setup is launched: proceed with the uninstallation steps.


User Management Component 2.9.2 - UMC Installation Manual
81
A5E50361197-AA


## **8 Troubleshooting**

**General**












|Problem Description|Solution|
|---|---|
|Cannot Authenticate with<br>unexpected problem. umtracer<br>gpclib shows a tentative to use<br>pipes to open a connection to<br>local machine.|Give access to the user that is launching the command to the<br>CONF directory of UMC (auth. users, for example).|
|IdP shows a compilation error<br>and raises an error while trying<br>to access a temp folder<br>(windows temp or temporary<br>asp.net files)|IIS_IUSRS has no access to windows TEMP folder.|
|Web UI: cannot enter a UMC<br>web application with error<br>"Cannot connect to server"|**umc_pool** application pool was configured to run in 32 bit mode.<br>Set the flag "Enable 32 bit" to FALSE in** umc_pool** configuration.|
|UMC Web UI shows the<br>following error Error on Login:<br>_An error occurred during_<br>_communication with the server_.|IIS features missing: Basic authentication, Windows authentication,<br>asp.net 4.5 was not installed.|
|Identity Provider Login pages<br>shows error related to<br>unknown Keys or security error<br>related to webconfig.|IIS features missing: Basic authentication, Windows authentication,<br>asp.net 4.5 was not installed.<br>Relaunch Idp_webui_, and so on.|
|UMCONF error 4 while joining.|The list of UMC rings is already full - check on ring master with<br>umconf -t and unjoin the secondary ring.|
|Windows 7 OS, Authentication<br>error (4 or 1) while trying to<br>auth, crash of um.server.exe,<br>errors on LadLibraryEX()|Security KB missing - see_ User Management Component_<br>_Installation Manual_.|
|Windows Integrated<br>Authentication. IdP page ask<br>for credential even if the user is<br>correctly logged in the AD (the<br>client is joined to the same AD<br>than the web server).|The AD (kerberos) is misconfigured. See the link below to prevent<br>issues in our test domain controller: https://blogs.msdn.microsoft.<br>com/chiranth/2014/04/17/setting-up-kerberos-authentication-for-a-<br>website-in-iis/<br>set the IIS authenticated user override to "useauthenticatedUser as<br>described here https://docs.microsoft.com/en-us/iis/configuration/<br>system.webServer/serverRuntime with this command : " appcmd.<br>exe set config "Default Web Site" -section:system.webServer/<br>serverRuntime /authenticatedUserOverride:<br>"UseAuthenticatedUser" /commit:apphost"|



User Management Component 2.9.2 - UMC Installation Manual
82

A5E50361197-AA


_8 Troubleshooting_
_7.2 Uninstalling UMC Station Client_





|Problem Description|Solution|
|---|---|
|SMART CARD: Error 403.7<br>forbidden when trying to open<br>info.aspx page and / or trying<br>to authenticate.|Enable CRL (Client Revocation List), refer to your IT department<br>for details.|
|The server error "Maximum<br>request length exceeded" is<br>raised.|A request exceeding the maximum IIS configuration limits has been<br>sent to the server. You can modify IIS configuration if needed.|
|UMC operations hangs and<br>return a generic or wrong error<br>message.|Check is the umc processes are all active.|
|Operations that requires<br>changes on UM configuration<br>fails with error<br>SL_NOTAMASTER.|Please check if the UM primary master is correctly running and<br>reacheable. If the problem occurs also on the primary ring server,<br>please restart um.ring.exe service.|
|Some operation fails<br>sporadically with generic error.|um.racrmtsrv.log file contains UMC DB files access error. Please<br>check the root cause of filesystem error (antivirus, backup, etc.).|
|Error on login " The validation<br>of the parameter 'service' failed<br>"|The service is not in the whitelist (service is a parameter passed to<br>the login request and identify who is the caller) use umconf to add<br>whitelist entry or login with umc admin user the first time (this add<br>service in whitelist automatically)<br>Same error appear if user try to open directly idp page : https://vm-<br>umc6.umdom1.net/umc-idp/idpauthsite/index.html without start<br>from https://vm-umc6.umdom1.net/umc|
|Problem on visualization of<br>login screen (2.x)|Check if ARR is installed and also ciis component url rewrite if yes<br>check the address and of redirection inside the rule, it must be<br>coherent with registry entry for websettings|


**Provisioning**












|Problem Description|Solution|Additional Links|
|---|---|---|
|You cannot configure the<br>provisioning.|Verify that the ring server machine is joined to<br>the Windows domain.|NA|
|In the UMC Web UI you<br>display_ undefined_ in the<br>domain drop down list to<br>import users/groups.|Verify that the ring server machine is joined to<br>the Windows domain, that you have configured<br>the UMC Provisioning service** UPService.exe**<br>and that the Windows user associated to the<br>service has Active Directory access rights.|NA|
|The import buttons do not<br>appear in the UMC Web<br>UI.|Verify that you have configured the UMC<br>Provisioning service** UPService.exe** and check<br>that the value of the registry key<br>HKEY_LOCAL_MACHINE\SOFTWARE\<br>Siemens\User Management\WebUI\Settings\<br>domains_support is set to** yes**.|See the Basic Post<br>Setup Instructions of<br>the_ Release Notes,_<br>the_ UMCONF User_<br>_Manual_ and_ UMX_<br>_User Manual_ for the<br>commands_._|



User Management Component 2.9.2 - UMC Installation Manual
83
A5E50361197-AA


_8 Troubleshooting_
_7.2 Uninstalling UMC Station Client_














|Problem Description|Solution|Additional Links|
|---|---|---|
|You perform the import of<br>an AD group and the<br>members are not<br>imported.|Verify that you have configured the UMC<br>Provisioning service UPService.exe with the<br>user that has write access on the UMC folder<br>**C:\ProgramData\Siemens\UserManagement\**<br>**CONF**. Alternatively the user must belong to<br>the Windows group UM Service Accounts.|See Associate Active<br>Directory Windows<br>User with Provisioning<br>Service.|
|You perform the import of<br>an AD group and the<br>members are not<br>imported.|Verify that the** Group scope** is** Universal**.|See the_ UMCONF_<br>_User Manual._|
|The search to import AD<br>users/groups returns 0<br>and you presume that your<br>search criteria will return<br>many data.|You may have to modify the Active Directory<br>administration limit** MaxPageSize**. Consider<br>that the AD default is 1000, if your search<br>returns more that 1000 results you have to<br>modify this value to a value higher then the<br>number of search results.|See the_ Functional_<br>_Limitations_ of the<br>_Release Notes._|
|The import of an AD group<br>having a high number of<br>associated -users is not<br>successful.|You may have to modify the Active Directory<br>administration limit** MaxValRange**.|See the_ Functional_<br>_Limitations_ of the<br>_Release Notes._|
|You experience an<br>excessive slowness in<br>operations involving AD<br>provisioning (such as the<br>import of users, the<br>alignment of AD<br>modifications and so on).|Check the CPU workload of your antivirus<br>program as the antivirus can influence the AD<br>provisioning performances.|NA|



**Using HealthState service for troubleshooting**


[Starting from UMC 1.8 it's possible to use a local endpoint to check umc health status (https://](https://localhost:16/healthcheck)
[localhost:16/healthcheck). Please check HealthState documentation for more information.](https://localhost:16/healthcheck)


User Management Component 2.9.2 - UMC Installation Manual
84

A5E50361197-AA


## **9 Appendix**

In this section you can find the following information:


             - Importing a Windows Local User on an Agent


             - UMC Processes


             - Event Logging


             - Additional Provisioning Configuration


             - Performing the Automatic Certificates Renewal

##### **9.1 Importing a Windows Local User on an Agent**


Windows local user can be imported on an agent machine using a Powershell script called Siemens.
UMC.ImportUser.ps1 which can be found in %ProgramFiles%\Siemens\UserManagement\BIN.


1. Run Powershell as Administrator.


2. Insert -server followed by the UMC server name.


3. Insert -user followed by username of the UMC user running the command, the user specified
must have the UM_Admin function right.


4. Insert -pwd followed by password of the UMC user running the command.


5. Insert -username followed by the username of the windows local user to import. The
username of the windows local user to import must be composed with one of the following
patterns:

– <computer name\name of the windows local user to import> in case of a Windows local


user


– " NT SERVICE\<SERVICE NAME>" in case of a Windows Virtual Service Account


6. Click **Enter** .



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-84-0.png)

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-84-1.png)



User Management Component 2.9.2 - UMC Installation Manual
85
A5E50361197-AA


_9 Appendix_

_9.2 UMC Processes_

##### **9.2 UMC Processes**



































|Service Display Name|Service Description|Process<br>Name|Process Description|
|---|---|---|---|
|UMC Secure<br>Communication Service|Implements<br>Communications for UMC|IPCSecCom.<br>exe|UMC Secure<br>Communication Service|
|||um.Ris.exe|UMC RIS Server|
|||um.ffsyssrv.<br>exe|UMC FFSYS Server|
|||um.kei.exe|UMC Certification Server|
|||um.sso.exe|UMC Single SignOn<br>Server|
|||um.jei.exe|UMC Join Server|
|UMCService|UMC Core Service|UMCService.<br>exe|UMC Core Service|
|||um.server.exe|UMC Agent Server|
|||um.<br>RACRMSRV.<br>exe|UMC RACRM Server|
|||um.ring.exe|UMC Ring Server|
|||um.ELGSrv.<br>exe|UMC Event Log Server|
|UPService|UMC Provisioning Service|UPService.<br>exe|UMC Provisioning Service|
|||um.piisrv.exe|UMC Provisioning Server|

##### **9.3 Event Logging**

UMC provides event logging. UMC event logging provides a mechanism to store the history of events
that has been raised using the UMC component. Event data will be stored in one or more files. The
**um.ELGSrv.exe** server is available to manage the event logging.


The following table summarizes logged events.

|Col1|Event|Logged|
|---|---|---|
|Authentication|||
||Successful login||
||Unsuccessful Login||



User Management Component 2.9.2 - UMC Installation Manual
86

A5E50361197-AA


_9 Appendix_

_9.3 Event Logging_


|Col1|Event|Logged|
|---|---|---|
||Change Password||
||Ticket Validation||
|Session Management|||
||Session Creation||
||Session Deletion||
|Configuration|||
||User Create/Delete/Modify|(only from<br>WEBUI)|
||Role Create/Delete/Modify|(only from<br>WEBUI)|
||Group Create/Delete/Modify|(only from<br>WEBUI)|
||Unlock User|(only from<br>WEBUI)|
||User Locked (when automatic unlock configured)||
||Global Account Policies changes||
|Two Factor<br>Authentication|||
||Secret key Creation|(only from<br>WEBUI)|
||Secret key Reset|(only from<br>WEBUI)|
||Time-based-one-time-password (TOTP) successfully<br>checked||
||Time-based-one-time-password (TOTP) unsuccessfully<br>checked||
|SADS|||
||Encryption enabled on Subject (User or Group)||
||Application Key Decryption failure due to an error in<br>User Authentication||
|Identity Provider|||
||Host automatically added to the Identity Provider<br>whitelist||



User Management Component 2.9.2 - UMC Installation Manual
87
A5E50361197-AA


_9 Appendix_

_9.3 Event Logging_

|Col1|Event|Logged|
|---|---|---|
||Identity Provider starts||
||Identity Provider stops||



Event logging offers the following features.


             - In a redundant scenario, log files can potentially be generated from different servers.
Mechanisms to manage reconciliation of data produced by different servers are available.


             - Internal APIs allows one to write UMC events and to search UMC events related to a given

date.


             - A UMC Web UI page (with limited reading capabilities) has been created to display event data
and to search them according to an input date. The old value and the new value of UMC data
related to the event are displayed.


             - A UMX command to list event log records is provided.


**9.3.1 Event Logging Security Notes**


The following security strategies have been implemented to grant system integrity for each server

machine:


             - Automatic cleanup of archive folder, to remove old archives before filling up the hard drive.


             - Protection against excessive log activity, to avoid that archive size could increase too fast.


**Automatic cleanup of archive folder**


The archive folder contains a list of archive files, each of which has a maximum size equal to **1GB**
(~500000 records). Every time this limit is reached, a new archive file is created and the files older
than **30 days** will be deleted. This implies that archive files will be deleted only when log activity is
really present and needs space disk.


To change the limit of 30 days:


1. Go to the **ELG** registry key: _HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\User_
_Management\ELG\Settings._


2. Add or update DWORD value **max_archive_time** with the new duration in seconds.


**Protection against excessive log activity**


Excessive log activity can be generated by an attempt to fill up server hard drive and make the system

unavailable.


To manage this attack, archive files cannot store more than **100000** records by day (but log forwarding
keeps on working).


When this limit is reached, an event log with action ELG CLOSE is written and any subsequent event
logs will no longer be archived.


User Management Component 2.9.2 - UMC Installation Manual
88

A5E50361197-AA


_9 Appendix_

_9.4 Additional Provisioning Configuration_


To recover the log archiving:


1. Go to the **ELG** registry key: _HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\User_
_Management\ELG\Settings._


2. Delete the DWORD value **num_archive_records_in_last_day** .


3. Restart the UMC service.


In the case the excess of log activity is generated on a disconnected server, event log ELG CLOSE is
written and subsequent (local) event logs will no longer be archived.


To recover the (local) log archiving:


1. Go to the **ELG** registry key: _HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\User_
_Management\ELG\Settings._


2. Delete the DWORD value **num_archive_records_in_last_day_no_index** .


3. Restart the UMC service.


To change the limit of 100000 records by day:


1. Go to the **ELG** registry key: _HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\User_
_Management\ELG\Settings._


2. Add or update DWORD value **max_archive_records_by_day** with the new number of

records.

##### **9.4 Additional Provisioning Configuration**


In order to make the import of Active Directory users and groups configurable, a file named
**piisrv_config.json** is created in %program data%\siemens\usermanagement\conf.


The editing of this file is optional. The following rules apply in computing the list of the domains from
which users and/or groups can be imported:


            - if the property **domains** is not empty, this list is considered for import, otherwise


            - the field **query_for_domains** defines the AD input query to compute the domain list.


After modifying the file, you have to:


            - copy the file in each machine where the provisioning is configured and


            - manually restart the **UPService** .


The file must have the following JSON format.


**Configuration JSON example**



![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-88-0.png)



User Management Component 2.9.2 - UMC Installation Manual
89
A5E50361197-AA


_9 Appendix_

_9.4 Additional Provisioning Configuration_

![](mds/umc/v2.9.2/UMC_InstallationManual_images/UMC_InstallationManual.pdf-89-0.png)


**Important:**

             - If polling_umc and polling_ad are missing, by default the polling values are:

– polling_umc 60 sec


– polling_ad 600 sec


             - "update_mode":"noupdate": (optional) If it is set to noupdate, no update will be
performed from AD.


**JSON description**

|Property|Type|Description|
|---|---|---|
|**add_alias_to**|string|The name of the AD field that has to be used as<br>alias.|
|**domains**|string|It is an array of domains where each domain object<br>contains the name. Formatted as follows: [{"name":<br>"domain1"},{"name":"domain2"}] }, note that the<br>domain suffix must not be used. By default the array<br>is empty.|
|**purge_time**|string|If a user is deleted from AD, it is flag as_ offline_.<br>Offline users are permanently deleted from UMC<br>database, after a number of minutes indicated in this<br>field. The default is 24 hours (720 minutes). The<br>following constraint must be valid:** purge_time**<br><**recycle_time.**|
|**query_for_domains**|string|AD query, see Microsoft documentation for more<br>details. The query "(objectcategory=crossref)" is the<br>default one. If the query in the file contains an error,<br>the default query is executed.|
|**query_for_users**|string|_Not used._|
|**query_for_groups**|string|_Not used._|
|**query_for_user**|string|_Not used._|



User Management Component 2.9.2 - UMC Installation Manual
90

A5E50361197-AA


_9 Appendix_

_9.4 Additional Provisioning Configuration_

|Property|Type|Description|
|---|---|---|
|**recycle_time**|string|Number of minutes before provisioning server restart.<br>The default is 24 hours (1440 minutes). The following<br>constraint must be valid:** purge_time**<**recycle_time.**|
|**polling_umc**|string|The interval at which polling is performed on the<br>UMC (default is 60 seconds )|
|**polling_ad**|string|The interval at which polling is performed on the AD<br>(default is 600 seconds)|
|**update_mode**|string|Update mode for imported users and groups. The<br>possible values are :** noremove, noupdate** or an<br>empty string (the default)|
|**import_users_from_nested_groups**|string|Allowed values are yes or no. If the property is not<br>present the default is no. If the property value is yes,<br>the Provisioning looks for all the users in the<br>subgroups of the group, imports them and associates<br>them to the parent group.|



**Update behaviour**
















|update_mode|Object|AD<br>command|UMC<br>command|Result|
|---|---|---|---|---|
|not present or<br>empty string|user<br>imported<br>manually|rename /<br>remove<br>user from<br>AD|na|The user is online but authentication fails.|
|not present or<br>empty string|users<br>import by<br>group|unbinding<br>user from<br>group|na|The user is put offline, authentication fails.|
|not present or<br>empty string|users<br>import by<br>group|rename /<br>delete<br>group|na|The user is put offline, authentication fails.|
|not present or<br>empty string|users<br>import by<br>group|remove<br>user from<br>AD|na|The user is put offline, authentication fails.|
|not present or<br>empty string|users<br>import by<br>group|rename<br>user from<br>AD|na|The user is put offline and authentication fails,<br>a new renamed user is imported in UMC and<br>authentication is available.|
|noremove \<br>noupdate|user<br>imported<br>manually|rename /<br>remove<br>user from<br>AD|na|The user is online but authentication fails.|



User Management Component 2.9.2 - UMC Installation Manual
91
A5E50361197-AA


_9 Appendix_

_9.4 Additional Provisioning Configuration_
















|update_mode|Object|AD<br>command|UMC<br>command|Result|
|---|---|---|---|---|
|noremove \<br>noupdate|user<br>imported<br>manually|rename /<br>remove<br>user from<br>AD|umx -sync|The user is online but authentication fails.|
|noremove \<br>noupdate|users<br>import by<br>group|unbindig<br>user group|na|The user remains online and the authentication<br>is successful.|
|noremove \<br>noupdate|users<br>import by<br>group|unbindig<br>user group|umx -sync|The user is put offline, authentication fails.|
|noremove \<br>noupdate|users<br>import by<br>group|rename /<br>delete<br>group||The user is online the authentication is<br>successful.|
|noremove \<br>noupdate|users<br>import by<br>group|rename /<br>delete<br>group|umx -sync|The user is put offline, authentication fails.|
|noremove \<br>noupdate|users<br>import by<br>group|remove<br>user from<br>AD||The user is online the authentication fails.|
|noremove \<br>noupdate|users<br>import by<br>group|remove<br>user from<br>AD|umx -sync|The user is put offline, authentication fails.|
|noremove \<br>noupdate|users<br>import by<br>group|rename<br>user from<br>AD||The user is onine the authentication fails, a<br>new renamed user is imported in UMC and<br>authentication is successful.|
|noremove \<br>noupdate|users<br>import by<br>group|rename<br>user from<br>AD|umx -sync|The user is put offline the authentication fails, a<br>new renamed user is imported in UMC and<br>authentication is successful.|
|noremove|users<br>import by<br>group /<br>manually|update<br>user||The user is updated.|
|noupdate|users<br>import by<br>group /<br>manually|update<br>user||The user is not updated.|
|noupdate|users<br>import by<br>group /<br>manually|updated<br>user|umx -sync|The user is updated.|



User Management Component 2.9.2 - UMC Installation Manual
92

A5E50361197-AA


_9 Appendix_

_9.5 Performing the Automatic Certificates Renewal_

##### **9.5 Performing the Automatic Certificates Renewal**


**UMC Domain Certificates**


In a UMC Domain the secure channel between UM machines is granted by means of two types of
certificates managed by the communication system:


             - The Network Certificate: It is created on the UM Ring master when the UMC domain is created.
By default, its validity is 10 years, but it can be configured at the domain creation (see the
_UMCONF User Manual_ for details). The network certificate is distributed in the UM domain
whenever a UM server/agent is joined/attached to the UMC domain.


             - The Machine Certificate: It is assigned to every machine when it is joined/attached to the UMC
domain. The machine certificate validity lasts until the Network certificate is valid.


Notes for the previous versions:


             - UMC V 2.7


– Network certificate validity = 10 years, it cannot be configured


– Machine certificate validity = 5 years, it cannot be configured.


             - UMC V<2.7:


– Network certificate validity = 10 years, it cannot be configured


– Machine certificate validity = 2 years, it cannot be configured.


             - UMC V < 1.9 SP1 Upd2

– Network certificate validity = 10 years, it cannot be configured


– Machine certificate validity = 1 years, it cannot be configured.


**Effects of Certificates expiration**


When a TCP connection between UMC servers is already established, as long as it remains up the
certificates expiration has no effect on the system. This behavior applies for both the certificate types
(Network or Machine).


As soon as a disconnection occurs after a certificate expiration, or as soon as the UM RIS module of
one of the connected machines is restarted, the communication is not established anymore.


In particular:


             - In case of expiration of the machine certificate (for an UM ring server, UM server, UM Agent),
the communication between this machine and the machines connected to it are affected.


             - In case of expiration of the network certificate, this issue applies to all the UM servers and UM
Agents in the UMC domain (the expiration of the network certificate corresponds to the
contemporary invalidity of all the machine certificates).


User Management Component 2.9.2 - UMC Installation Manual
93
A5E50361197-AA


_9 Appendix_

_9.5 Performing the Automatic Certificates Renewal_


**Procedure for Certificates Renewal**


The certificate renewal procedure is executed on a machine when less than two years are left until
certificate expiration. The procedure starts automatically at the machine reboot. At the first reboot of
the machines inside the two years from the certificates expiration date the following operations are
performed:


             - On the primary ring master, a new Network certificate and the ring Machine certificate are
created and saved. Communication with the other machines continues by means of the
previous certificates.


             - On the secondary ring, the network certificate is propagated and saved, a new machine
certificate is assigned, and the communication can use the new certificates.


             - On the other servers and on the agents the network certificate is propagated and saved, and the
new machine certificate is assigned. The communication with the ring master and with the other
servers can use the new certificates.


Until the ring master reboot, the reboot of all the other machines of the UMC domain has no effect.


The required reboot order is the following: primary ring, secondary ring, servers, agents.


It is assumed that at least one reboot in the required order is done within two years from the certificate
expiration dates.


In case only the machine certificate is expiring on a UMC machine (for example when coming from an
UMC version inferior or equal to 2.7), the certificate renewal procedure must be executed only on that
machine, by performing the machine reboot.


**Result of certificate renewal**


After the certificate renewal the following applies:


             - The new Network and Machine Certificates have a 10 year validity.


             - The NETID of every UM machine is changed, therefore the fingerprint is changed.


             - The domain ID of the UMC domain is not changed.


The certificate renewal has no impact on the Identity Provider claim Key.


**UMC Version Upgrade**


When a UMC domain is upgraded to UMC V2.8 SP2 from a previous version, it is possible the
certificates validity is already closer than two years to the expiration date. In this case the automatic
procedure for the certificates renewal will start as soon as the domain is upgraded by means of the
appropriate UMCONF -U command (see How to upgrade to UMC 2.8.2 in the _UMC Installation Guide_
for details). Any reboot, if required, during the installation phase will not trigger the renew procedure.


**CAUTION:**


If the upgrade command UMCONF -U is not performed on the machine after a UMC
upgrade, the automatic certificates renewal is disabled and a machine restart will never
trigger the certificate renewal


User Management Component 2.9.2 - UMC Installation Manual
94

A5E50361197-AA


**Exceptions**



_9 Appendix_

_9.5 Performing the Automatic Certificates Renewal_


- If the certificates are already expired, the automatic renewal cannot be performed and it is
necessary to perform a manual procedure.



User Management Component 2.9.2 - UMC Installation Manual
95
A5E50361197-AA


