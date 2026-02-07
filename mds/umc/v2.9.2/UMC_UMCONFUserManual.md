# s

###### **User Management Component 2.9.2**

### **UMCONF User Manual**


#### Commands for Binding/Unbinding 6

###### Commands for Centralized
#### **7**
###### Configuration Management

#### Commands for Upgrading Entities 8

###### Commands for Deleting a UM
#### **9**
###### Configuration

#### Commands for Importing Packages 10

###### Commands for the Management of
#### **11**
###### Whitelist Entries Commands for the Management of
#### **12**
###### Plugins Commands for the Management of
#### **13**
###### Logs Commands for Renewing
#### **14**
###### Certificates Commands for Launching UMConf
#### **15**
###### in Interactive Mode

#### Commands for Purging Roles 16 Commands for Displaying Lists 17 Commands for dSSO functionality 18 Error Codes 19

###### Commands for the Management of
#### **20**
###### the GUM server list

**09/2020**

**A5E50361206-AA**


User Management Component 2.9.2 - UMCONF User Manual
2

A5E50361206-AA


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



A5E50361206-AA
20200903_45718



Copyright © Siemens AG 2020
Technical data subject to change


### **Contents**

**1 UMCONF Overview ................................................................................................................. 6**


**2 Concepts You Need to Know About...................................................................................... 8**

2.1 User Manager Domain...................................................................................................... 8

2.2 User Manager User........................................................................................................... 9

2.3 Built-in User Roles .......................................................................................................... 10

2.4 Claim Key........................................................................................................................ 10

2.5 User Manager Function Rights ........................................................................................11


**3 Commands for Listing a Summary of UMCONF Commands ........................................... 13**

3.1 Help................................................................................................................................. 13


**4 Commands for Creating UM Entities .................................................................................. 14**

4.1 Create Domain................................................................................................................ 14

4.2 Create UM Administrator User........................................................................................ 15

4.3 Create Claim Key............................................................................................................ 16


**5 Commands for the Management of UM Services .............................................................. 17**

5.1 Associate Active Directory Windows User with Provisioning Service............................. 17

5.2 Associate User with UM Service..................................................................................... 18


**6 Commands for Binding/Unbinding ..................................................................................... 19**

6.1 Attach Agent ................................................................................................................... 19

6.2 Join Server...................................................................................................................... 20

6.3 Unjoin Server .................................................................................................................. 21

6.4 Retrieve Fingerprint ........................................................................................................ 22


**7 Commands for Centralized Configuration Management .................................................. 24**

7.1 Get Default Centralized Configuration ............................................................................ 25
7.2 Set Centralized Configuration......................................................................................... 25
7.3 Get Centralized Configuration......................................................................................... 26


**8 Commands for Upgrading Entities ..................................................................................... 27**

8.1 Upgrade Domain............................................................................................................. 27


**9 Commands for Deleting a UM Configuration ..................................................................... 28**

9.1 Delete Configuration ....................................................................................................... 28


**10 Commands for Importing Packages ................................................................................. 29**

10.1 Import Package - UMC Partially Configured................................................................. 29


**11 Commands for the Management of Whitelist Entries...................................................... 30**

11.1 Create Whitelist Entry ................................................................................................... 30

11.2 List Whitelist Entries...................................................................................................... 31

11.3 Remove Whitelist Entry................................................................................................. 31


**12 Commands for the Management of Plugins..................................................................... 33**


User Management Component 2.9.2 - UMCONF User Manual
iv

A5E50361206-AA


12.1 Register Custom Plugin ................................................................................................ 33
12.2 Register Cookie Adapter............................................................................................... 34

12.3 List Registered Plugins ................................................................................................. 35

12.4 Deregister Plugin .......................................................................................................... 36


**13 Commands for the Management of Logs ......................................................................... 38**

13.1 Archive logs .................................................................................................................. 38

13.2 Extract logs ................................................................................................................... 38


**14 Commands for Renewing Certificates.............................................................................. 40**

14.1 Renew Certificate.......................................................................................................... 40

14.2 Renew Network Certificates.......................................................................................... 41


**15 Commands for Launching UMConf in Interactive Mode................................................. 42**

15.1 Launch Interactive Mode............................................................................................... 42


**16 Commands for Purging Roles ........................................................................................... 44**

16.1 Purge Role IDs.............................................................................................................. 44


**17 Commands for Displaying Lists........................................................................................ 45**

17.1 Display Server List........................................................................................................ 45


**18 Commands for dSSO functionality ................................................................................... 46**

18.1 Enable or disable dSSO................................................................................................ 46


**19 Error Codes ......................................................................................................................... 47**


**20 Commands for the Management of the GUM server list................................................. 48**

20.1 Create GUM list entry ................................................................................................... 48
20.2 List GUM list entry......................................................................................................... 49
20.3 Remove GUM list entry................................................................................................. 49


User Management Component 2.9.2 - UMCONF User Manual
v
A5E50361206-AA


## **1 UMCONF Overview**

The **umconf** utility can be used to perform the basic configuration of the User Management
Component (UMC). basic configuration steps can be performed using the guided interactive mode
(recommended) or by using a range of switches and parameters. Additionally, depending on the
options selected (switches) and the related parameters, the utility allows you to execute various
configuration commands. Note that the execution of the **umconf** utility with no switches is identical to
the execution of the utility in interactive mode ( **umconf -i** ).


This utility, which is distributed with UMC, is installed in the subdirectory \BIN (for example C:\Program
Files\Siemens\UserManagement\BIN) and must be executed from a command prompt within this
directory or in the C:\Program Files\Siemens\UserManagement\WOW\BIN folder. The execution of
**umconf** is allowed by a Windows user with Administrative rights ( elevated user if User Account
Control (UAC) is enabled) or any users belonging to the um_config group.


**CAUTION:**


             - The **umconf** utility must be used with care. Incorrect usage can cause system
unavailability.


             - Stop all of the applications that use UMC before launching umconf and making
changes to the machine configuration.


**UMC Basic Configuration**


The basic configuration consists of:


             - Creating the User Manager Domain;


             - Creating the User Manager user with administrator role;


             - Specifying the Windows user that is associated with the User Manager core service; this user
must be either in the UM Service Accounts group or have Administrative rights.


             - the Windows user with Active Directory access rights that is associated with the provisioning
service - mandatory if you need Active Directory Provisioning. This option is not enabled if you
create a Standalone Domain.


After the first installation it is necessary to perform the configuration steps above to run UMC on a
machine that, once configured, will be promoted to UM ring server.


**Important:**


We strongly suggest using the command **umconf -i** to perform all the configuration steps.


**Configuration Options**


The following options are supported:


             - fresh configuration: it is the first time that you are configuring UMC;


             - overwrite an existing configuration: you have already configured UMC and you want to modify
the configuration;


User Management Component 2.9.2 - UMCONF User Manual
6

A5E50361206-AA


_1 UMCONF Overview_


             - upgrade an existing configuration from a previous version: you have already configured UMC,
you have installed a newer version of UMC and you have to upgrade the configuration.


The different options are offered when running umconf interactively.


User Management Component 2.9.2 - UMCONF User Manual
7
A5E50361206-AA


## **2 Concepts You Need to Know About**

The following concepts are the basics you need to know before you start configuring UMC:


             - User Manager Domain


             - User Manager User


             - Built-in User Roles


             - Claim Key


             - User Manager Function Rights

##### **2.1 User Manager Domain**


A User Manager domain (UM domain) is a collection of computers defined by the administrator of a
network that shares a common directory database. A UM domain provides access to the centralized
user accounts and group accounts maintained by the UM domain administrator.


**Important:**


UM domains are different entities with respect to Windows domains that are defined at
operating system level.


**UMC Computer Roles**


In a typical UMC scenario there are three computer roles:


             - **UM ring server** : the owner of the UM configuration, which is responsible for managing the
domain, and provides full implementation of authentication and user management features. The
_priority_ ring server is the one which is configured first, running the **umconf** utility. If more than
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


User Management Component 2.9.2 - UMCONF User Manual
8

A5E50361206-AA


_2 Concepts You Need to Know About_


_2.2 User Manager User_


**CAUTION:**


If you want to manage Active Directory users, the UM ring server and the UM server
machines have to be joined to the AD Windows domain.

##### **2.2 User Manager User**


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


User Management Component 2.9.2 - UMCONF User Manual
9
A5E50361206-AA


_2 Concepts You Need to Know About_

_2.3 Built-in User Roles_


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


##### **2.3 Built-in User Roles**


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

##### **2.4 Claim Key**


A claim is a statement that one subject, such as a person or organization, makes about itself or
another subject. The subject making the claim or claims is the provider. We use this mechanism to
provide web authentication. When the user authenticates himself against the identity provider, it
receives a claim. This claim is signed using the private claim key. Once a relying party needs to verify
the claim, it uses the corresponding public claim key (previously installed on the relying party). It is up
to the relying party how this public claim key is installed.


User Management Component 2.9.2 - UMCONF User Manual
10

A5E50361206-AA


_2 Concepts You Need to Know About_


_2.5 User Manager Function Rights_

##### **2.5 User Manager Function Rights**


Function rights are the capabilities to perform operations. They are associated with roles so that the
set of UM users having a specific UM role is allowed to perform the set of operations associated with it.
The following table contains a list of UM Function Rights:

|Name|Description|
|---|---|
|UM_ADMIN|Allows you to display the UMC database data and to configure the UMC<br>database, that is to create users, groups and so on, to import and export data<br>via file, to register UMC station clients. This function right allows you to execute<br>all** umx** commands.|
|UM_VIEW|Allows you to display the UMC database data related to users, groups, roles<br>and account policies.|
|UM_RESETPWD|The user can reset the password of another user. The user must also have<br>associated the** UM_VIEW** function right.|
|UM_UNLOCKUSR|The user can unlock any other user_._ The user must also have associated the<br>**UM_VIEW** function right.|
|UM_ATTACH|The user can attach a machine to a UM domain, the machine is promoted to the<br>_UM agent role_.|
|UM_JOIN|The user can promote a machine to a_ UM server role_. If the machine is not yet<br>attached to the UM domain, it is attached. This function right incorporates the<br>**UM_ATTACH** function right_._|
|UM_RESETJOIN|The user can downgrade a machine from the UM ring server or UM server role<br>to the UM agent role.|
|UM_IMPORT|The user can import the UM Configuration via package. The user must also<br>have associated the** UM_VIEW** function right.|
|UM_EXPORT|The user can export the UM Configuration into a package_._ The user must also<br>have associated the** UM_VIEW** function right.|
|UM_BACKUP|The user can back up the UM Configuration (Full backup)_. This function right is_<br>_not used, as the functionality controlled by it has not yet been implemented._|
|UM_EXPORTCK|The user can export Claim Key_. This function right is not used, as the_<br>_functionality controlled by it has not yet been implemented._|
|UM_EXPORTDK|The user can export Domain Key_. This function right is not used, as the_<br>_functionality controlled by it has not yet been implemented._|
|UM_RA|Login from Remote Authentication_. This function right is not used, as the_<br>_functionality controlled by it has not yet been implemented._|
|UM_RINGMNG|The user can promote a machine to a_ UM ring server role_. If the machine is not<br>yet attached to the UM domain, it is attached.|
|UM_ADSYNC|The user can perform the background AD provisioning synchronization.|
|UM_VIEWELG|The user can display event logging data. The user must also have associated<br>the** UM_VIEW** function right.|
|UM_CLAIMAUTH|The user can create an identity from a valid claim.|



User Management Component 2.9.2 - UMCONF User Manual
11
A5E50361206-AA


_2 Concepts You Need to Know About_

_2.5 User Manager Function Rights_

|Name|Description|
|---|---|
|UM_REGCLIENT|The user can register UMC station clients.|



User Management Component 2.9.2 - UMCONF User Manual
12

A5E50361206-AA


## **3 Commands for Listing a Summary of UMCONF** **Commands**

The following command can be used to display a summary of UMCONF commands:


             - Help

##### **3.1 Help**


This command displays a brief summary of the different commands with their parameters and

switches.


**Syntax**





User Management Component 2.9.2 - UMCONF User Manual
13
A5E50361206-AA


## **4 Commands for Creating UM Entities**

The following commands can be used to create UMC entities:


             - Create Domain


             - Create UM Administrator User


             - Create Claim Key

##### **4.1 Create Domain**


This command creates a UM Domain named as the input parameter if no domain exists. If a domain
has already been defined, use the -f switch to overwrite the existing domain. If you are working with a
distributed scenario with an active firewall, the inbound and outbound connections through the 4002
port must be allowed. The command creates also the private claim key, which is necessary for correct
system functioning.


**CAUTION:**


Overwriting an existing domain can cause possible data loss.


**Syntax**





**Parameters**


**Switches**




  - _name_ is the string representing the UM Domain name, only alphanumeric characters are

allowed.


|Switch|Description|
|---|---|
|-e|Sets the number of days before the network certificate expiration.|
|-f|Forces the creation of a new UM Domain. If a domain with the same name is present it is<br>overwritten.|



User Management Component 2.9.2 - UMCONF User Manual
14

A5E50361206-AA


**Example #1**


**Example #2**



_4 Commands for Creating UM Entities_


_4.2 Create UM Administrator User_


umconf -c -d mydomain


umconf -c -d mydomain -e 7300


It creates a umc domain "mydomain" with network certificate expiration after 7300 days.


##### **4.2 Create UM Administrator User**

This command creates the UM Administrator user. This user can be created only once.


**CAUTION:**


Using umconf you can create only one UM user with Administrator role and neither the
user nor the password can be changed. The password can be changed via **umx**

command or via Web UI.


**General Recommendations**


It is strongly recommend that you comply with the password policies of your organization in order to
grant password strength for the UM Administrator user. For example, a password policy may impose
that your password meets the following requirements:


            - be at least 8 characters long;


            - contain characters from three of the following four categories:

– uppercase characters of European languages (A through Z, with diacritic marks, Greek and

Cyrillic characters);


– lowercase characters of European languages (a through z, sharp-s, with diacritic marks,

Greek and Cyrillic characters);


– base 10 digits (0 through 9);


– nonalphanumeric characters: ~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/


When creating the UM Administrator User, if you are using the command via script, add a warning that
suggests to insert a password that complies with the password policies of your organization.


**Syntax**





User Management Component 2.9.2 - UMCONF User Manual
15
A5E50361206-AA


_4 Commands for Creating UM Entities_
_4.3 Create Claim Key_


**Parameters**


             - _name_ is the string representing the user name, only alphanumeric characters and the special
character '_' are allowed.


             - _password_ is the password associated to the user. An empty password is not accepted.


**Example #1**


umconf -c –u administrator -p 123

##### **4.3 Create Claim Key**


This command creates a new private claim key and generates the corresponding public key. The new
private claim key becomes the current one used by the Identity Provider to sign the claims provided to
the relying parties.It can be run only on a ring server that is master. This command cannot be run on a
master ring server machine that is running in safe mode (writing is not enabled).


The public key of the claim can be found in %programdata%\Siemens\UserManagement\CERT\CLAIM
and the filename is **key.pub** . The key can be exported. During the create domain operation a claim key
is created, this new claim key overwrites the existing one. If needed the relying party applications
should be updated with the new claim key.


**CAUTION:**


In case of a distributed scenario, once you have created a new claim key on a UM master
ring server/UM server, to align the keys, the **UMCService** of the other UM ring server/UM
server machine has to be manually restarted.


**Syntax**





User Management Component 2.9.2 - UMCONF User Manual
16

A5E50361206-AA


## **5 Commands for the Management of UM Services**

The following commands can be used to associate users to UM Services:


             - Associate Active Directory Windows User with Provisioning Service


             - Associate User with UM Service

##### **5.1 Associate Active Directory Windows User with Provisioning Service**


This command associates the Windows user identified by the parameter _name_ with the UM service
**UPService.exe** . In order to associate the Windows user with the service, the password must be
inserted as input parameter.


This Windows user must have the following rights:


             - Active Directory access rights;


             - write access on the UMC folder C:\ProgramData\Siemens\UserManagement\CONF or
alternatively he must belong to the Windows group **UM Service Accounts** .


This command also creates the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\User
Management\WebUI\Settings\domains_support and sets it to "yes", which enables the Web UI import
user and group functionalities.


**Important:**


In order to disable the Active Directory provisioning, you have to set to "no" the value of
the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\User Management\
WebUI\Settings\domains_support and stop the UM service **UPService.exe** .


**Syntax**





**Parameters**


**Switches**




  - _name_ is the string representing the user name preceded by the domain.


  - _password_ is the password associated with the user.


**Switch** **Description**



User Management Component 2.9.2 - UMCONF User Manual
17
A5E50361206-AA


_5 Commands for the Management of UM Services_

_5.2 Associate User with UM Service_

##### **5.2 Associate User with UM Service**


This command associates the Windows user identified by the parameter _name_ with the UM service
**UMCService.exe** . In order to associate the Windows user with the service, the password must be
given as input parameter. This user must be either in the UM Service Accounts group or have
Administrative rights. In case you want to associate a built-in Windows local user, you have to use the
Windows Services configuration tool.


**CAUTION:**


The user associated to UM service must only be changed via UMConf.


**Syntax**





**Parameters**


**Switches**




  - _name_ is the string representing the user name preceded by the domain. If the user is local, the
name must be preceded by the string ".\" or _machinename\._ For Example: .\administrator,
mydomain\myuser.


  - _password_ is the password associated with the user. If the virtual account NT SERVICE\UMC
Service has been specified, the password will not be prompted.


|Switch|Description|
|---|---|
|-f|If the services are running and have been already configured, this switch allows you to<br>overwrite the existing configuration.|



User Management Component 2.9.2 - UMCONF User Manual
18

A5E50361206-AA


## **6 Commands for Binding/Unbinding**

The following commands can be used to perform binding or unbinding actions:


             - Attach Agent


             - Join Server


             - Unjoin Server


             - Retrieve Fingerprint

##### **6.1 Attach Agent**


This command attaches a machine to a UM domain and promotes it to the UM agent role. All the
parameters of the command are optional. If a parameter is not inserted when launching the command,
you will be prompted to insert it. The _serviceUserName_ and _servicePassword_ parameters are an
exception to this behavior: if not inserted the default is the built-in Windows user _Local System_ .


The command installs the network and machine certificates on your machine. In presence of an active
firewall, the inbound and outbound connections through the 4002 port must be allowed. In an agent
machine you can run an application developed using the UMC API, see the _User Management_
_Component API SDK Developer Manual_ for more details.


**Syntax**



![](mds/umc/v2.9.2/UMC_UMCONFUserManual_images/UMC_UMCONFUserManual.pdf-18-0.png)



**Parameters**


             - _computerName_ is the name of one of the UM ring servers or UM servers of the domain you
want to be attached to. Both NetBIOS or FQDN name can be used.


             - _userName_ is the name of a UM user having the **UM_ATTACH** function right or the

**Administrator** role.


             - _password_ is the password of the UM user associated with the parameter _userName._ When the
switch -t is present, _password_ is a ticket generated for that user.


             - _serviceUserName_ is the name of a Windows Local/domain user (who is either a member of the
UM Service Accounts group or has Administrative rights) that you want to associate with the
User Manager services.


             - _servicePassword_ is the password of the Windows user associated with the parameter

_serviceUserName_ .


             - _fingerprint_ is the fingerprint of the UMC domain.


User Management Component 2.9.2 - UMCONF User Manual
19
A5E50361206-AA


_6 Commands for Binding/Unbinding_

_6.2 Join Server_


**Switches**

|Switch|Description|
|---|---|
|-f|If the machine has already been configured, the existing configuration is overwritten.|
|-v|If this switch is present, the installation of the certificates is not interactive. The -v switch is<br>mandatory if the fingerprint is specified.|
|-t|If this switch is present, a ticket generated for the user must be provided instead of the<br>password.|


##### **6.2 Join Server**


This command promotes the machine to a UM server or UM ring server machine. If the machine is not
yet attached to the UM domain, the command attaches it. All the parameters of the command are
optional. If a parameter is not inserted when launching the command, you will be prompted to insert it.
The _serviceUserName_ and _servicePassword_ parameters are an exception to this behavior: if not
inserted the default is the built-in Windows user _Local System_ .


The command installs:


             - the network and machine certificates on your machine;


             - the ticket and claim keys.


In presence of an active firewall, the inbound and outbound connections through the 4002 port must be

allowed.


**CAUTION:**


Consider that if you have configured the AD provisioning on the priority ring server you
must configure it also in the machine you are joining. See the -b switch below to exclude
the AD provisioning configuration. If you want to use this command via script, the use of b is mandatory and to configure the provisioning you have to use the umconf command to
associate the Active Directory Windows user with the Provisioning Service.


**Syntax**



![](mds/umc/v2.9.2/UMC_UMCONFUserManual_images/UMC_UMCONFUserManual.pdf-19-0.png)



**Parameters**


             - _serverType_ determines the type of the server that will be joined to the ring:

– 0 the machine will be a UM server, in this case the provisioning is not configured;


– 1 the machine will be a UM ring server.


User Management Component 2.9.2 - UMCONF User Manual
20

A5E50361206-AA


**Switches**



_6 Commands for Binding/Unbinding_

_6.3 Unjoin Server_


  - _computerName_ is the name of one of the UM ring servers of the domain you want to be joined
to. Both NetBIOS or FQDN name can be used.


  - _userName_ is the name of a UM user having the **UM_RINGMNG** function right (to create a UM
ring server) or **UM_JOIN** function right (to create a UM server) or having the **Administrator**
role. For more details see User Manager Function Rights.


  - _password_ is the password of the UM user associated with the parameter _userName._ When the
switch -t is present, _password_ is a ticket generated for that user.


  - _serviceUserName_ is the name of a Windows Local/domain user (who is either a member of the
UM Service Accounts group or has Administrative rights) that you want to associate with the
User Manager services.


  - _servicePassword_ is the password of the Windows user associated with the parameter

_serviceUserName_ .


  - _fingerprint_ is the fingerprint of the UMC domain.


|Switch|Description|
|---|---|
|-f|Forces the services stop.|
|-m|This switch determines the type of server that will be joined to the ring:<br>•<br>0: the machine will be a UM server;<br>•<br>1: the machine will be a UM ring server.|
|-v|If this switch is present, the installation of the certificates is not interactive. The -v switch is<br>mandatory if the fingerprint is specified.|
|-fp|If the switch -v and -fp are present, the fingerprint specified is used for validation.|
|-b|The Active Directory provisioning configuration is not performed. This switch is relevant only<br>for UM ring server configuration. In case of UM server the provisioning is never configured.|
|-t|If the switch -t is present, a ticket generated for the user must be provided instead of the<br>password.|


##### **6.3 Unjoin Server**

This command downgrades a machine having the UM ring server/UM server role to a UM agent role.
The parameters _userName_ and _password_ of the command are optional. If the parameter is not inserted
when launching the command, you will be prompted to insert it, whereas, if you do not insert the
parameter _computerName,_ by default the command is executed for the machine on which you are
launching it. If you unjoin a priority ring server, the system dynamically elects a new priority ring server.


In presence of an active firewall, the inbound and outbound connections through the 4002 port must be

allowed.


User Management Component 2.9.2 - UMCONF User Manual
21
A5E50361206-AA


_6 Commands for Binding/Unbinding_

_6.4 Retrieve Fingerprint_


**CAUTION:**


If you perform the unjoin remotely (parameter _computerName_ is present) of a machine
that is disconnected from the network and the unjoined machine returns connected after a
while, you have to delete the UMC configuration before joining it again.


**Syntax**





**Parameters**


**Switches**




  - _userName_ is the name of a UM user having the **UM_RESETJOIN** function right or having the

**Administrator** role.


  - _password_ is the password of the UM user associated with the parameter _userName_ or a ticket
generated for that user.


  - _computerName_ is the NetBIOS name of the machine having the UM ring server/UM server role
that you are unjoining. This parameter must be used only if the UMC services of the machine
you are running the command cannot communicate with the UMC services of the machine you
are unjoining. This happens for instance when the unjoining machine is no more available.


|Switch|Description|
|---|---|
|-f|Forces the services stop.|


##### **6.4 Retrieve Fingerprint**

This command retrieves the fingerprint (net id) of the UMC domain from the specified computer. To
obtain the fingerprint from a configured machine for a machine which has not been configured, the [-c
computerName] parameter can be used. If you do not specify the computer name, the fingerprint is
retrieved locally.


Since in UMC 2.8, this command is allowed only in a not configured machine. On a joined/attached
machine, umconf -fingerprint would fail with the message "UM configuration command forbidden from
a configured machine".


User Management Component 2.9.2 - UMCONF User Manual
22

A5E50361206-AA


_6 Commands for Binding/Unbinding_


_6.4 Retrieve Fingerprint_



**Syntax**


**Parameters**






             - _computerName_ is the name of the machine from which you want to obtain the fingerprint. When
remote, both NetBIOS or FQDN name can be used.


User Management Component 2.9.2 - UMCONF User Manual
23
A5E50361206-AA


## **7 Commands for Centralized Configuration** **Management**

The following commands can be used to manage the UMC centralized configuration:


             - Get Default Centralized Configuration


             - Set Centralized Configuration


             - Get Centralized Configuration


**Set Initial Central Configuration**


To set a centralized configuration you must:


1. Execute get default configuration.


2. Modify the file .json file as required for your centralized configuration, see the _User Manager_

_Installation Manual_ .


3. Set the centralized configuration.


**Update Central Configuration**


To update the current centralized configuration you must:


1. Execute get configuration in order to retrieve the current version of centralized configuration.


2. Modify the current configuration as required, see the _User Manager Installation Manual_ .


3. Set the centralized configuration.


**Note:** To check if the configuration has been previously updated at least once, you can
Execute get configuration.


             - If the command succeeds, this means that the configuration has been previously
modified, so you have to follow the "Update Central Configuration" instructions

above.


             - If the command fails, this means that no modification has been previously done
and there is only the Default Configuration. In this case you have to follow the "Set
Initial Central Configuration" instructions above.


For information on the contents of the default, central and local configuration files see the Identity
provider configuration section in the _User Manager Installation Manual._


User Management Component 2.9.2 - UMCONF User Manual
24

A5E50361206-AA


_7 Commands for Centralized Configuration Management_

_7.1 Get Default Centralized Configuration_

##### **7.1 Get Default Centralized Configuration**


This command retrieves the default configuration .json file. The file can be used as a template from
which you can copy the keys for the values to set in the local or central configuration.


**Syntax**





**Parameters**


            - _fullpath_ the path and the name of file in which the default configuration is to be saved.

##### **7.2 Set Centralized Configuration**


This command sets the file specified as the centralized configuration. The configuration file has a
specific version, which is incremented every time a set operation is performed, you must perform a get
before setting a configuration, in order to retrieve the latest version.


**Syntax**





**Parameters**


             - _userName_ is the name of a UM user who has the **UM_ADMIN** function right or the

**Administrator** role.


             - _password_ is the password of the UM user associated with the parameter _userName._ When the
switch -t is present, _password_ is a ticket generated for that user.


             - _fullpath_ is the complete path of the .json file which contains the UMC configuration that is to be

set.


             - _labelName_ is the name that identifies the configuration.

|Switch|Description|
|---|---|
|-label|(for future use only) Optional, allows you to specify a label in order to identify each specific<br>configuration.|



User Management Component 2.9.2 - UMCONF User Manual
25
A5E50361206-AA


_7 Commands for Centralized Configuration Management_
_7.3 Get Centralized Configuration_

##### **7.3 Get Centralized Configuration**


This command retrieves the centralized configuration file which is currently set and saves it to the file
and location specified.


**Syntax**





**Parameters**


             - _full_path_ the full path of the file which is to be retrieved.


             - _labelName_ is the name that identifies the configuration.

|Switch|Description|
|---|---|
|-label|(for future use only) Optional, allows you to specify a label in order to identify each specific<br>configuration.|



User Management Component 2.9.2 - UMCONF User Manual
26

A5E50361206-AA


## **8 Commands for Upgrading Entities**

The following command can be used to upgrade a UM domain:


             - Upgrade Domain

##### **8.1 Upgrade Domain**


This command upgrades an existing UM Domain. It can be used after installing UMC on a machine
where a previous version was installed and configured.


**CAUTION:**


We strongly suggest to use the command **umconf -i** to perform all the upgrade steps that
include this domain upgrade operation.


**CAUTION: Certificate renewal**


If the network or machine certificates validity is close to the expiration date, the Upgrade
Domain command will start the automatic procedure for the certificate renewal. See the
Appendix in the _UMC Installation Manual_ for details.


**Syntax**





**Switches**

|Switch|Description|
|---|---|
|-f|Forces the services stop.|



User Management Component 2.9.2 - UMCONF User Manual
27
A5E50361206-AA


## **9 Commands for Deleting a UM Configuration**

The following commands can be used to delete a UM configuration:


             - Delete Configuration

##### **9.1 Delete Configuration**


This command deletes UMC configuration, restoring the system as if it was just installed. The
command has to be run after the UMC services has been stopped or using the -f switch to stop them
automatically. After executing the command, it is necessary to perform the **Recycle** of the following
application pools in **IIS Manager** :


             - Web UI pool ( **umc_pool**, for configuration via script);


             - Identity Provider pool ( **SimaticLogonPool**, for configuration via script).


In case you want to remove a UM ring server/UM server from the UMC system you have also to
perform the unjoin operation of the machine _before_ executing this command.


**CAUTION:**


Performing the restart of a UMC service and/or the **Recycle** of the application pool can
cause service interruption.


**Syntax**





**Switches**

|Switch|Description|
|---|---|
|-f|Forces the UMC services to stop before deleting all data.|



User Management Component 2.9.2 - UMCONF User Manual
28

A5E50361206-AA


## **10 Commands for Importing Packages**

The following commands can be used to import a UM package:


             -             Import Package UMC Partially Configured

##### **10.1 Import Package - UMC Partially Configured**


This command imports a UMC configuration via an input UMC package on a machine where the UMC
domain has been already created. To run this command the **only configuration step** that you must
have performed on the system is the domain creation. If UMC is configured, to import a package you
must use the corresponding umx command. For more details see the _UMX User Manual_ .


UMC package is a UMC proprietary format, zipped and encrypted. If not inserted, you will be prompted
to insert a password for the decryption that has to be the same as the one used in the export package

umx command. For more details see the _UMX User Manual_ .


The effects of this operation are:


             - the creation of the UMC user with administrator role;


             - the import of all the users, groups and roles that are part of the package.


For more information on the import/export/update package usage see the _Standalone Engineering_
_Station Scenario_ in the _User Management Component Installation Manual_ .


**Syntax**





**Parameters**


**Switches**




  - _file_ is the path and name of the file to be imported, for instance C:\temp\myPackage;


  - _password_ is the archive password.


|Switch|Description|
|---|---|
|-f|Forces the services to stop.|



User Management Component 2.9.2 - UMCONF User Manual
29
A5E50361206-AA


## **11 Commands for the Management of Whitelist Entries**

The following commands can be used to manage Whitelist Entries:


             - Create Whitelist Entry


             - List Whitelist Entries


             - Remove Whitelist Entry

##### **11.1 Create Whitelist Entry**


This command adds a host to the Identity Provider whitelist. Whitelisting allows you to maintain a list of
hosts that are granted some privileges. If present in the list:


             - the host can call the IdP (service validation);


             - the host can create an iFrame embedding the IdP (iFrame validation).


If the host is not present in the list, the call is rejected. In case of service validation, we log a warning
message on UMC event log and, if enabled, we log also a message on the Identity Provider log file.


After executing the command, for each machine where the Identity Provider is installed, it is necessary:


             - to restart the **UMCService** ;


             - to perform the **Recycle** of the application pool of the Identity Provider ( **SimaticLogonPool**, for
configuration via script) in **IIS Manager** .


**CAUTION:**


Performing the restart of a UMC service and/or the **Recycle** of the application pool can
cause service interruption.


**Syntax**





**Parameters**


             - _name_ is the string that represents the host according to URL standard format, and must specify
the exact path of the relying party. It can be:

– localhost;


– machine name (e.g. myMachine);


– internet domain name (e.g. www.myDomain.net);


– IP address (e.g. 172.23.1.48).


User Management Component 2.9.2 - UMCONF User Manual
30

A5E50361206-AA


_11 Commands for the Management of Whitelist Entries_


_11.2 List Whitelist Entries_


– or to whitelist the service layer:

             - computername/UMC/slwapi/service


             - computername/UMC/slwapi/service and computername.userdnsdomain/UMC/slwapi/


service.


Remember to recycle the application pool of the Identity Provider to apply all pending modifications.

##### **11.2 List Whitelist Entries**


This command lists the hosts of the Identity Provider whitelist. The only default value present in the
whitelist is the hostname of the machine; this value is added to the whitelist when the UMC domain is

created.


**Syntax**





**Example**

```
        umconf -l -w

```

**Example output:**


whitelist contains the following domains:


localhost


myMachine


170.23.1.48

##### **11.3 Remove Whitelist Entry**


This command removes a host from the Identity Provider whitelist.


After executing the command, for each machine where the Identity Provider is installed, it is necessary:


             - to restart the **UMCService** ;


             - to perform the **Recycle** of the application pool of the Identity Provider ( **SimaticLogonPool**, for
configuration via script) in **IIS Manager** .


**CAUTION:**


Performing the restart of a UMC service and/or the **Recycle** of the application pool can
cause service interruption.


User Management Component 2.9.2 - UMCONF User Manual
31
A5E50361206-AA


_11 Commands for the Management of Whitelist Entries_

_11.3 Remove Whitelist Entry_


**Syntax**





**Parameters**


**Example**




   - _name_ is the string representing the host according to URL standard format. It can be:

– localhost;


– machine name (e.g. myMachine);


– domain name (e.g. www.myDomain.net);


– IP address (e.g. 172.23.1.48).

```
umconf -d -w -d 175.22.3.55

```

**Output:**


domain 175.22.3.55 successfully removed from whitelist.


Remember to restart UMC service to apply all pending modifications.



User Management Component 2.9.2 - UMCONF User Manual
32

A5E50361206-AA


## **12 Commands for the Management of Plugins**

The following commands can be used to manage UM plugins:


             - Register Plugin


             - Register Cookie Adapter


             - List Registered Plugins


             - Deregister Plugin

##### **12.1 Register Custom Plugin**


This command registers a custom plugin. It can only be executed on a master ring server.


After executing the command, for each machine where the Identity Provider is installed, it is necessary
to perform the **Recycle** of the application pool of the Identity Provider ( **SimaticLogonPool**, for
configuration via script) in **IIS Manager** .


**CAUTION:**


Performing the **Recycle** of the application pool can cause service interruption.


**Syntax**



![](mds/umc/v2.9.2/UMC_UMCONFUserManual_images/UMC_UMCONFUserManual.pdf-32-0.png)



**Parameters**


             - _userName_ is the name of a UM user who has the **UM_ADMIN** function right or the

**Administrator** role.


             - _password_ is the password of the UM user associated with the parameter _userName._ When the
switch -t is present, _password_ is a ticket generated for that user.


             - _plugin_path_ is the path and name of the dll plugin to be registered, for instance C:\temp\
myPlugin.dll;


             - _plugin_description_ is the string that will appear in the drop-down menu on the right of the Idp
login page on the client machine;


             - _plugin_name_ specifies the unique name of the plugin. Note that the following names are
reserved: iwa, pki, desktop, web, web_cors, hybrid, hybrid_cors and ":".


             - _response format_ for future use.


User Management Component 2.9.2 - UMCONF User Manual
33
A5E50361206-AA


_12 Commands for the Management of Plugins_
_12.2 Register Cookie Adapter_


             - _securitylevel_ defines the type of authentication. This information is passed in the IdP claim so
that the third party application can determine the authentication security level; in UMC Web UI
can only be used if the authentication is **standard** or **strong** .The security level can only be
specified for web and hybrid plugins. The possible values are:


– **weak**


– **standard**


–
**strong**


             - _languagefile_ not used.






|Switch|Description|
|---|---|
|-w|For future use. Specifies that the plug in is a web plugin, if this switch is used you must<br>use -pk, see below.|
|-pk|For future use. Specifies a public key associated to the plugin.|
|-w2|For future use. Specifies that the plug in is a hybrid plugin.|
|-<br>usealias|Specifies that the alias of the user is to be used instead of the username.|


##### **12.2 Register Cookie Adapter**

This command registers a cookie adapter. It can be executed only on a master ring server.


After executing the command, for each machine where the Identity Provider is installed, it is necessary
to perform the **Recycle** of the application pool of the Identity Provider ( **SimaticLogonPool**, for
configuration via script) in **IIS Manager** .


**CAUTION:**


Performing the **Recycle** of the application pool can cause service interruption.


**Syntax**



![](mds/umc/v2.9.2/UMC_UMCONFUserManual_images/UMC_UMCONFUserManual.pdf-33-0.png)



**Parameters**


             - _userName_ is the name of a UM user having the **UM_ADMIN** function right or having the

**Administrator** role.


             - _password_ is the password of the UM user associated with the parameter _userName._ When the
switch -t is present, _password_ is a ticket generated for that user.


User Management Component 2.9.2 - UMCONF User Manual
34

A5E50361206-AA


**Switches**



_12 Commands for the Management of Plugins_


_12.3 List Registered Plugins_


  - _url_ is the url of the cookie adapter to be registered;


  - _plugin_description_ is the string that will appear in the drop-down menu on the right of the Idp
login page on the client machine;


  - _public_key_path_ is the public key generated at the setup of cookie-adapter


  - _securityLevel_ defines the type of authentication. This information is passed in the IdP claim so
that the third party application can determine the authentication security level; in UMC Web UI
authentication is performed in case of **standard** and **strong** . The possible values are:


– **weak**


– **standard**


–
**strong**


  - _languagefile - not used_ .


|Switch|Description|
|---|---|
|-w|Specifies that you are registering a cookie adapter.|
|-pk|Specifies a public key associated to the plugin.|


##### **12.3 List Registered Plugins**

This command can be be executed on any server and lists the plugins which are registered on the
master ring server, along with their:


            - **Plugin Uid** : the unique id of the plugin which is necessary to activate plugins on clients.


            - **Path:** the path of the plugin.


            - **Description:** the description of the plugin.


            - **Class** : Specifies the type of plugin: desktop, web or hybrid.


            - **Pub keyid:** the public key id.


            - **Security Level:** Weak, Standard and Strong, see register custom plugin for more information.


            - **Plugin Name:** the unique the name of the plugin, this field is empty in plugins which were
created prior to UMC 1.9.1.


            - **Use alias:** Authentication with alias (enabled or disabled).


            - **Config data:** Adapter configuration information.


**Syntax**





User Management Component 2.9.2 - UMCONF User Manual
35
A5E50361206-AA


_12 Commands for the Management of Plugins_

_12.4 Deregister Plugin_


**Example**


An example of the command output follows:


#1 Plugin Uid: 889f1341-0260-4f77-81fd-ceadf8f56c4fPath: C:\Users\Administrator\Desktop\
Test_plugins\Bin\PluginTAF.dllDescription: Plugin Desktop Stateful Class: desktopPub keyid:Security
level: weakUse alias: enabled Plugin name: my desktop plugin Config data: #2 Plugin Uid:
3c179694-e5ed-4225-b064-eb01b981251bPath: C:\Users\Administrator\Desktop\Test_plugins\Bin\
PluginTAF2.dllDescription: Plugin Desktop Stateless Class: desktopPub keyid:Security level: weakUse
alias: disabled Plugin name:my plugin Config data:

##### **12.4 Deregister Plugin**


This command deregisters a plugin on a master ring server.


After executing the command, for each machine where the Identity Provider is installed, it is necessary
to perform the **Recycle** of the application pool of the Identity Provider ( **SimaticLogonPool**, for
configuration via script) in **IIS Manager** .


**CAUTION:**


Performing the **Recycle** of the application pool can cause service interruption.


**Syntax**





**Parameters**


**Example**




   - _userName_ is the name of a UM user having the **UM_ADMIN** function right or having the

**Administrator** role.


   - _password_ is the password of the UM user associated with the parameter _userName._ When the
switch -t is present, _password_ is a ticket generated for that user.


   - _pluginname_ is the name of the plugin alternatively you can use _pluginId._


   - _pluginId_ is the position of the plugin in the list of registered plugins. See example below.


If the command:

```
umconf -l -P

```


User Management Component 2.9.2 - UMCONF User Manual
36

A5E50361206-AA


_12 Commands for the Management of Plugins_


_12.4 Deregister Plugin_


returns:#2 Plugin Uid: 5a25fc03-3bd1-479b-9b02-2dcb9f6f60f3Path: [https://mymachine/](https://vm-chessa/tcss_web)
[tcss_webDescription: Teamcenter Web Class: webPub keyid:](https://vm-chessa/tcss_web)
88FACEFCD6ED416BC6D516D10E09ABBBDA85FDC6Security level: strongUse alias: enabledPlugin

                                                                          name: Teamcenter Web#3 Plugin Uid: 113dc9ec-ada6-4f61-b938-9bf2a50b1401Path: [https://vm](https://vm-chessa/tcss_hybrid)
[chessa/tcss_hybridDescription: Teamcenter Hybrid Class: hybrid_corsPub keyid:](https://vm-chessa/tcss_hybrid)
88FACEFCD6ED416BC6D516D10E09ABBBDA85FDC6Security level: strongUse alias: enabledPlugin
name: Teamcenter Hybrid

```
        pluginlist contains 2 plugins correctly registered.

```

the command:

```
        umconf -dP -u myUser -p 098P@ssword! -name Teamcenter Hybrid

```

deregisters the Windows plugin.


User Management Component 2.9.2 - UMCONF User Manual
37
A5E50361206-AA


## **13 Commands for the Management of Logs**

The following commands can be used to manage logs:


             - Archive logs


             - Extract logs

##### **13.1 Archive logs**


This command archives the system log folder into a UMC package. UMC package is a UMC
proprietary format, zipped and encrypted. The exported package is the input of the extract logs

command.


**Syntax**





**Parameters**


            - _file_ is the path and name of the package file, for instance C:\temp\myLogs;


            - _password_ is the package password. If not provided, the user will be prompted to insert the
password.

##### **13.2 Extract logs**


This command extracts the system logs previously archived into a UMC package. UMC package is a
UMC proprietary format, zipped and encrypted. If the password is not inserted when launching the
command, you will be prompted to insert it. The input password has to to be the same of the one used
in the archive logs command.


**Syntax**





User Management Component 2.9.2 - UMCONF User Manual
38

A5E50361206-AA


**Parameters**



_13 Commands for the Management of Logs_


_13.2 Extract logs_


- _file_ is the path and name of the package file, for instance C:\temp\myLogs;


- _password_ is the package password.



User Management Component 2.9.2 - UMCONF User Manual
39
A5E50361206-AA


## **14 Commands for Renewing Certificates**

The following commands allow to update machine certificates, which are created when a agent is
attached or a server is joined. The machine certificate is x.509 certificate which allows SSL
communications between UMC machines.


**CAUTION:**


Network and Machine certificates can be automatically renewed when close to the
expiration date: see the Appendix in the _UMC Installation Manual_ for details about the
certificate renewal procedure. The following commands therefore can be used only in
some particular cases. See the Appendix in the _UMC Installation Manual_ (paragraph
Exceptions) for the list of the allowed use cases.


             - Renew Certificate


             - Renew Network Certificate (Primary Ring Server only)

##### **14.1 Renew Certificate**


This command updates the expiration date of the machine certificate of a UMC machine, the renewed
certificate has the same expiration date as the network certificate.


**CAUTION:**


When performing this operation from a machine which is not ring server, if the operation
fails the machine will be detached and must be re-attached in order to attempt the
operation again.


**Syntax**



![](mds/umc/v2.9.2/UMC_UMCONFUserManual_images/UMC_UMCONFUserManual.pdf-39-0.png)



**Parameters**


             - _computerName_ is the name of one of the UM server on which the certificate is located. When
remote, Both NetBIOS or FQDN name can be used.


             - _userName_ is the name of a UM user who has the UM_ATTACH function right or the
**[Administrator](https://wemes.siemens.com/wiki/display/UMC/Built-in+User+Roles+UMCONF)** role. For more details see [User Manager Function Rights.](https://wemes.siemens.com/wiki/display/UMC/User+Manager+Function+Rights_umconf)


             - _password_ is the password of the UM user associated with the parameter _userName_ .


             - _fingerprint_ is the fingerprint of the UMC domain.


User Management Component 2.9.2 - UMCONF User Manual
40

A5E50361206-AA


_14 Commands for Renewing Certificates_


_14.2 Renew Network Certificates_


**Switches**

|Switch|Description|
|---|---|
|-f|Forces the UMC services to stop before renewing the<br>certificate.|
|-v|If this switch is present, the installation of the certificates is<br>not interactive. The -v switch is mandatory if the fingerprint is<br>specified.|


##### **14.2 Renew Network Certificates**


This command updates the expiration date of the network certificate and machine certificate of a UMC
Primary Ring Server.


**CAUTION:**


When performing this operation from a machine which is not the primary ring server, if the
operation fails.


**Syntax**





**Switches**

|Switch|Description|
|---|---|
|-f|Forces the UMC services to stop before renewing the<br>certificate.|



User Management Component 2.9.2 - UMCONF User Manual
41
A5E50361206-AA


## **15 Commands for Launching UMConf in Interactive** **Mode**

The following command can be used to execute the umconf utility in interactive mode:


             - Launch Interactive Mode

##### **15.1 Launch Interactive Mode**


This command executes the **umconf** utility in interactive mode. The following configuration steps are
performed launching the interactive mode:


             - the User Manager Domain;


             - the User Manager user with administrator role, the password for this user should be at least 8
characters long and contain characters from three of the following four categories:

– uppercase characters of European languages (A through Z, with diacritic marks, Greek and

Cyrillic characters);


– lowercase characters of European languages (a through z, sharp-s, with diacritic marks,

Greek and Cyrillic characters);


– base 10 digits (0 through 9);


– nonalphanumeric characters: ~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/


             - the Windows user that is associated with the **UMCService.exe** service; if the virtual account NT
SERVICE\UMC Service has been specified, the password will not be prompted.


             - the Windows user that is associated with the **UPService.exe** service - mandatory only if you
need to import Active Directory users via the **umx** tool or via the Web UI;


             - the private claim key.


The following options are supported:


             - fresh configuration: it is the first time that you are configuring UMC;


             - overwrite an existing configuration: you have already configured UMC and you want to modify
the configuration;


             - upgrade an existing configuration from a previous version: you have already configured UMC,
you have installed a newer version of UMC and you have to upgrade the configuration.


**Syntax**





Or alternatively:


User Management Component 2.9.2 - UMCONF User Manual
42

A5E50361206-AA


_15 Commands for Launching UMConf in Interactive Mode_


_15.1 Launch Interactive Mode_





User Management Component 2.9.2 - UMCONF User Manual
43
A5E50361206-AA


## **16 Commands for Purging Roles**

The following command can be used to purge UM role IDs:


             - Purge Role IDs

##### **16.1 Purge Role IDs**


This command purges the roles identifiers. Role identifiers are generated incrementally, until the
maximum value of 32600 is reached. Once this value is reached it is no longer possible to insert any
new role (regardless of the maximum roles number) until you make the purge of the roles previously

deleted.


**CAUTION:**


This command stops the **UMCService** and restarts it after the execution. The stop can
cause service interruption.


**Syntax**





User Management Component 2.9.2 - UMCONF User Manual
44

A5E50361206-AA


## **17 Commands for Displaying Lists**

The following commands can be used to display the list of servers:


             - Display Server List

##### **17.1 Display Server List**


This command displays the list of the servers with their machine role. The command can be executed
only on a server or ring server machine.


**Syntax**





**Example**

```
        umconf -t

```

**Output**


The server list contains:


servername: myname1 ring server
servername: myname2 ring server
servername: myname3 server


User Management Component 2.9.2 - UMCONF User Manual
45
A5E50361206-AA


## **18 Commands for dSSO functionality**

The following commands can be used to enable or disable dSSO functionality:


             - Enable or disable dSSO

##### **18.1 Enable or disable dSSO**


This command enables or disables the dSSO functionality.


**Syntax**

```
       umconf -dsso [enable|disable] [-f(orce)]

```

**Switches**


**Examples**

|Switch|Description|
|---|---|
|-f|Forces the UMC Secure Communication to restart.|


```
        umconf -dsso enable

```

**Output**


dSSO functionality successfully enabled.
UMC Secure Communication Service need to be restarted manually.

```
        umconf -dsso disable -f

```

**Output**


dSSO functionality successfully disabled.
UMC Secure Communication Service has been restarted.


User Management Component 2.9.2 - UMCONF User Manual
46

A5E50361206-AA


## **19 Error Codes**

|Value|Description|
|---|---|
|0|Success.|
|1|The user launching the command does not have the proper administrative rights.|
|10|Initialization error, for instance a registry key is missing.|
|50|Command syntax error.|
|100|Command execution error.|



User Management Component 2.9.2 - UMCONF User Manual
47
A5E50361206-AA


## **20 Commands for the Management of the GUM server** **list**

A record in the GUM server list has the following fields:


             - url.


             - the server machine that can be reached using the url.


             - the fingerprint of the server machine.


An entry in the GUM server list is identified by the url. The url is case insensitive and unique in the list.


The GUM protocol supports a discovery command that provides a list of url. A client can use one of
them to invoke further GUM commands.


The list of url in the discover result is retrieved by marging the GUM server list and the server list of the

current domain.


The discovery result contains only url of GUM server list whose server machine is present in the server
list of the current domain.


Such server machines (of GUM server list and server list of the current domain) are case insensitive.


The following commands can be used to manage GUM server list:

##### **20.1 Create GUM list entry**


This command creates an entry in the GUM list. An entry in GUM list is unique and it is identified by
the url parameter which is case insensitive.
The url is associated to its server machine (that is case insensitive). The server parameter is used by
the GUM discovery to check (by using the server list) the list of url available for the GUM protocol. The
fingerprint parameter is related to the server machine in the list.


**Syntax**





**Parameters**


             - **url** : url of the gum service. The url is the unique identifier of the entry in the list. Two entries with
the same url in the GUM list cannot be inserted (umconf fails in that case). The url parameter is

case insensitive.


             - **servername** : hostname of the machine to which the url is related. The server name is used by
the GUM discovery service to build the list of url supported by the GUM checking which entry in


User Management Component 2.9.2 - UMCONF User Manual
48

A5E50361206-AA


**Example**



_20 Commands for the Management of the GUM server list_

_20.2 List GUM list entry_


the GUM list is present also in the UMC server list. For this check the server name is considered

case insensitive.


   - **fingerprint** : fingerprint of the UMC domain to which the server belongs.


umconf -c -g -u [https://myprs/gumtest](http://myprs/gumtest) -s vm-prs -fp
FDD47C931853722CCD6595A404EA47476793A235


##### **20.2 List GUM list entry**

This command shows the content of the GUM list.


**Syntax**





**Example**


umconf -l -g


**Output**


gumlist contains the following values:
url: [http://myserver/gumtest](http://myserver/gumtest) server: vm-server fingerprint:
FDD47C931853722CCD6595A404EA47476793A235

##### **20.3 Remove GUM list entry**


This command removes a entry in the GUM list. The entry is removed by url which is the unique
identifier of a entry in the list.


**Syntax**





User Management Component 2.9.2 - UMCONF User Manual
49
A5E50361206-AA


_20 Commands for the Management of the GUM server list_
_20.3 Remove GUM list entry_


**Parameters**


**url** : url of the gum service. The url is the unique identifier of the entry in the list. Two entries with the
same url in the GUM list cannot be inserted (umconf fails in that case). The url parameter is case

insensitive.


**Example**


umconf -d -g -u [https://myprs/gumtest](http://myprs/gumtest)


User Management Component 2.9.2 - UMCONF User Manual
50

A5E50361206-AA


