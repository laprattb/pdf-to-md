# s

###### **User Management Component 2.9.2**

### **UMC Service Layer API** **Developer Manual**

**09/2020**

**A5E50361214-AA**


###### Contents

#### What is UMC Service Layer? 1 Common Response Information 2 Authentication 3 Users 4 Groups 5 Roles 6 UMC APIs Error Codes 7 Account Policies 8 Function Rights 9 Change Password 10

###### Authentication IISAPPPOOL
#### **11**
###### identity - only for test

#### Set Identity Property 12


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



A5E50361214-AA
20200903_46856



Copyright © Siemens AG 2020
Technical data subject to change


### **Contents**

**1 What is UMC Service Layer? ................................................................................................. 5**


**2 Common Response Information ........................................................................................... 6**


**3 Authentication......................................................................................................................... 7**


3.1 Login ................................................................................................................................. 7

3.2 Authentication from Claim................................................................................................. 9

3.3 Identity .............................................................................................................................. 9


**4 Users...................................................................................................................................... 13**


4.1 Get All Users................................................................................................................... 13

4.2 Get User Details.............................................................................................................. 15

4.3 Create User..................................................................................................................... 20

4.4 Update User - Basic........................................................................................................ 22

4.5 Update User - Full........................................................................................................... 23

4.6 Unlock User .................................................................................................................... 25

4.7 Delete Users ................................................................................................................... 26

4.8 Browse AD Users............................................................................................................ 27

4.9 Import Users ................................................................................................................... 29

4.10 Reset Password............................................................................................................ 30

4.11 Get All System Users .................................................................................................... 31


**5 Groups ................................................................................................................................... 34**

5.1 Get All Groups ................................................................................................................ 34

5.2 Get Group Details ........................................................................................................... 35

5.3 Create Group .................................................................................................................. 37

5.4 Update Group - Basic ..................................................................................................... 38

5.5 Update Group - Full ........................................................................................................ 40

5.6 Delete Groups................................................................................................................. 41

5.7 Browse AD Groups ......................................................................................................... 43

5.8 Import Groups from AD................................................................................................... 43


**6 Roles ...................................................................................................................................... 45**


6.1 Get All Roles................................................................................................................... 45

6.2 Get Role Details.............................................................................................................. 47

6.3 Create Role..................................................................................................................... 47

6.4 Update Role.................................................................................................................... 48

6.5 Delete Roles ................................................................................................................... 50


**7 UMC APIs Error Codes......................................................................................................... 52**


**8 Account Policies................................................................................................................... 59**


8.1 Read Account Policies.................................................................................................... 59

8.2 Set Account Policies ....................................................................................................... 59


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
iii
A5E50361214-AA


8.3 Restore Default Account Policies.................................................................................... 60


**9 Function Rights .................................................................................................................... 62**

9.1 List Function Rights ........................................................................................................ 62


**10 Change Password............................................................................................................... 63**


**11 Authentication IISAPPPOOL identity - only for test ........................................................ 64**


**12 Set Identity Property........................................................................................................... 65**


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
iv

A5E50361214-AA


## **1 What is UMC Service Layer?**

UMC Service Layer (SL) is the UMC Open Development Kit (ODK) to develop an application that
needs to manage authentication, UMC users, groups and roles. Refer to the _User Management_
_Component Installation Manua_ l for more details on the UMC Service Layer configuration.


UMC SL is based on HTTP services that reach a broad range of clients, including browsers and mobile
devices. It can be used to develop Web pages and is also a powerful platform for exposing APIs
providing services and data. HTTP is simple, flexible and ubiquitous. Almost any platform that you can
think of has an HTTP library.


The data exchange is based on JSON format. Any call to the UMC SL include the requested "method"
in the uri or the HTTP request. The response format is composed of:


             - a common part that includes operation and protocol information;


             - a detailed part that is described in each API.


For a complete list of the exposed APIs see:


             - authentication APIs;


             - user management APIs;


             - group management APIs.


Any request except the ones necessary to login, needs authorization. Authorization session is created
using one of the "authentication" methods and transmitted by the browser in the request header
(cookie authentication).


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
5
A5E50361214-AA


## **2 Common Response Information**

The answer for every response (except the service for WebSSO) has the following format.


**Response Header Fields**

|Field|Value|
|---|---|
|**status**|•<br>200 in case of success;<br>•<br>4xx otherwise.|
|**Content-Type**|application/json|



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-5-0.png)



**Response JSON Description**

|Property|Type|Description|
|---|---|---|
|**version**|integer|Protocol version. Consider that can vary depending on the API. See each API<br>section for the value.|
|**operation**|string|Represents the invoked operation. See each API section for the value.|
|**result**|integer|Returns the last error code (decimal format) returned by the UMC APIs invoked<br>during the command execution. See UMC APIs Error Codes for more details.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
6

A5E50361214-AA


## **3 Authentication**

The following APIs are dedicated to authentication:


             - Login


             - Authentication from Claim


             - Identity

##### **3.1 Login**


Performs user authentication providing a user name and password.

|example URL|https://localhost/UMC/slwapi/login|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/x-www-form-urlencoded|
|**Request Parameters**|The following parameters must be provided.<br>**Name**<br>**Type**<br>**Description**<br>**user**<br>string<br>User name.<br>**password**<br>string<br>User password.<br>**Example**:<br>https://localhost/UMC/slwapi/login?user=myuser&password=mypsw|



**Response JSON Example**


|Name|Type|Description|
|---|---|---|
|**user**|string|User name.|
|**password**|string|User password.|



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-6-0.png)





**Response JSON Description**


For the common properties see Common Response Information.


**Example: REST call**


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
7
A5E50361214-AA


_3 Authentication_

_3.1 Login_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-7-0.png)

**Input Parameters**


The input parameters of this function are the following:


             - the **http** or **https** protocol,


             - the server to be used for the REST call,


             - the user name and password for the login.


**Return Values**


             - NULL if the login is not successful,


             - the cookie if the login is successful.


The function also writes the result JSON shown in the example.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
8

A5E50361214-AA


_3 Authentication_

_3.2 Authentication from Claim_

##### **3.2 Authentication from Claim**


**This method is provided only for test purpose. Compatibility is not warrantied and may be**

**removed in a next version.**


Performs the authentication of a user providing a claim. The user and the signature that guarantee
claim validity are given in input. This user must have the proper function right ( **UM_ADMIN** or
**UM_CLAIMAUTH** ). The name and the password in input are the credentials of the user that
guarantees the claim validity and NOT the one of the user requesting authentication.



|example URL|https://localhost/UMC/slwapi/pswclaimlogin|
|---|---|
|**Request**<br>**HTTP Verb**|POST|
|**Request**<br>**Content-**<br>**Type**|application/x-www-form-urlencoded|
|**Request**<br>**Parameters**|The following parameters must be provided.<br>**Name**<br>**Type**<br>**Description**<br>**name**<br>string<br>Name of the guaranteeing user.<br>**password**<br>string<br>Password of the guaranteeing user.<br>**claim**<br>string<br>Claim of the authenticating user.<br>**signature**<br>string<br>Claim signature.<br>**keyid**<br>string<br>The identifier of the key used to sign the claim.<br>**Example**:<br>https://localhost/UMC/slwapi/pswclaimlogin?name=myuser&password=<br>mypsw&claim=myclaim&signature=mysignature&keyid=mykeyid|

##### **3.3 Identity**




|Name|Type|Description|
|---|---|---|
|**name**|string|Name of the guaranteeing user.|
|**password**|string|Password of the guaranteeing user.|
|**claim**|string|Claim of the authenticating user.|
|**signature**|string|Claim signature.|
|**keyid**|string|The identifier of the key used to sign the claim.|



Provides information about the authenticated user.

|example URL|https://localhost/UMC/slwapi/identity|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
9
A5E50361214-AA


_3 Authentication_

_3.3 Identity_


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-9-0.png)







**Response JSON Description**


For the common properties see Common Response Information.


**Example: REST call**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-9-1.png)



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
10

A5E50361214-AA


_3 Authentication_


_3.3 Identity_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-10-0.png)





**Properties**

|Property|Type|Description|
|---|---|---|
|domains_support|integer|Yes when the provisioning service is configurator (on the machine which<br>exposes the identity service), otherwise no.|
|issuer|string|The address of the identity provider, which is configured on the machine<br>that exposes the identity .|
|**language**|string|It is the user language and has the format <langcode>-<countrycode>,<br>where<br>•<br>langcode is the language code according to the ISO 639<br>standard; we accept both two-letter codes (ISO 639-1) and three-<br>letter codes (ISO 639-2);<br>•<br>countrycode is the country code according to the ISO 3166<br>standard.<br>An example is en-GB.|
|results|integer|See Common Response Information.|
|session_id|integer|The identifier of the current session.|
|validity|string|The validity of the current session.|
|version|integer|See Common Response Information.|



**Domaininfo Object**


The Domaininfo object has the following properties:

|Property|Type|Description|
|---|---|---|
|**domainid**|integer|The identifier of the UMC domain.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
11
A5E50361214-AA


_3 Authentication_

_3.3 Identity_

|Property|Type|Description|
|---|---|---|
|**domainname**|string|The name of the UMC domain.|



**Rights Object**


Each rights object has the following properties:


**User object**

|Property|Type|Description|
|---|---|---|
|**can_modify**|string|If set to true the user can modify the umc configuration. If set to false the<br>user cannot make modifications.|
|**can_read**|string|If set to true the user can view the configuration. If set to false the user<br>cannot access the configuration.|
|**can_register**|string|If set to true the user can register a machine as a client. If set to false the<br>user cannot register a client.|
|**can_resetpwd**|string|If set to true the user can reset thier password. If set to false the user cannot<br>reset their password.|
|**can_unlock**|string|If set to true the user can unlock locked users. If set to false the user cannot<br>unlock locked users.|
|**can_viewlog**|string|If set to true the user can view the umc log. If set to false the user cannot<br>view the umc log.|
|**is_admin**|string|If set to true the user is a umc administrator. If set to false the user is not<br>configured as administrator.|



Each user object has the following properties:

|Property|Type|Description|
|---|---|---|
|**Fullname**|string|The full name of the authenticated user.|
|**Username**|string|The username of the authenticated user.|



**Return Values**


             - NULL if the login is not successful,


             - the cookie if the login is successful.


The function also writes the result JSON shown in the example.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
12

A5E50361214-AA


## **4 Users**

The following APIs are dedicated to user management:


             - Get All Users


             - Get User Details


             - Create User


             - Update User - Basic


             - Update User - Full


             - Unlock User


             - Delete Users


             - Browse AD Users


             - Import Users

##### **4.1 Get All Users**


Returns data related to all UMC users.

|example URL|https://localhost/UMC/slwapi/users|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-12-0.png)





User Management Component 2.9.2 - UMC Service Layer API Developer Manual
13
A5E50361214-AA


_4 Users_

_4.1 Get All Users_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-13-0.png)

**Response JSON Description**


For the common properties see Common Response Information.


**users property Array**


Each user object has the following properties:

|Property|Type|Description|
|---|---|---|
|**id**|integer|User identifier, it is a 32 bit number greater than zero where the 31st bit is used<br>to store the information if the user is imported or not. If the 31st bit is equal to 1<br>the user is imported from Active Directory, 0 otherwise. The ID ranges are as<br>follows:<br>•<br>1-20: reserved for UMC built in users;<br>•<br>21- 1073741844: UMC users created from scratch;<br>•<br>1073741845 to 2147483647: Imported users.|
|**objver**|integer|This is an integer that is incremented at each user modification.|
|**name**|string|User name.|
|**fullname**|string|User full name.|
|**comment**|string|A note that can be added to the user (optional).|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
14

A5E50361214-AA


_4 Users_

_4.2 Get User Details_

|Property|Type|Description|
|---|---|---|
|**userflags**|integer|It is a 16 bit number bit mask representing the following flags, the order is from<br>the LSB (less significant bit) to the MSB (most significant bit) :<br>1.<br>User Must Change Password: it is equal to 1 if the user must change<br>password, 0 otherwise.<br>2.<br>User Can Change Password: it is equal to 1 if the user can change<br>password, 0 otherwise.<br>3.<br>User Locked: it is equal to 1 if the user is locked, 0 otherwise.<br>4.<br>User Enabled: it is equal to 1 if the user can authenticate into UMC, 0<br>otherwise.<br>5.<br>User imported from AD: it is equal to 1 if the user has been imported<br>from Active Directory domain users, 0 otherwise.<br>6.<br>User imported from Local: it is equal to 1 if the user has been imported<br>from Windows local users, 0 otherwise.<br>7.<br>User imported from group: it is equal to 1 if the user has been imported<br>through imported Active Directory group, 0 otherwise.<br>8.<br>User offline: it is equal to 1 if the user is offline, 0 otherwise. See Get<br>User Details for additional information.<br>9.<br>_Not used._<br>10.<br>_Not used_.<br>11.<br>_Not used._<br>12.<br>_Not used._<br>13.<br>_Not used._<br>14.<br>_Not used._<br>15.<br>_Not used._<br>16.<br>_Not used._|


##### **4.2 Get User Details**


Returns all the details related to the user associated with the input id.

|example URL|https://localhost/UMC/slwapi/users{/id}|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Response JSON Example**





User Management Component 2.9.2 - UMC Service Layer API Developer Manual
15
A5E50361214-AA


_4 Users_

_4.2 Get User Details_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-15-0.png)



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
16

A5E50361214-AA


_4 Users_

_4.2 Get User Details_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-16-0.png)





**Response JSON Description**


For the common properties see Common Response Information.


**users Object**


The user object has the following properties:


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
17
A5E50361214-AA


_4 Users_

_4.2 Get User Details_

|Property|Type|Description|
|---|---|---|
|**id**|integer|User identifier, it is a 32 bit number greater than<br>zero where the 31st bit is used to store the<br>information if the user is imported or not. If the 31st<br>bit is equal to 1 the user is imported from Active<br>Directory, 0 otherwise. The ID ranges are as<br>follows:<br>•<br>1-20: reserved for UMC built in users;<br>•<br>21- 1073741844: UMC users created from<br>scratch;<br>•<br>1073741845 to 2147483647: Imported users.|
|**objver**|integer|This is an integer that is incremented at each user<br>modification.|
|**name**|string|User name.|
|**fullname**|string|User full name.|
|**comment**|string|A note that can be added to the user (optional).|
|**firstname**|string|User first name.|
|**lastname**|string|User last name.|
|**initials**|string|User initials.|
|**language**|string|It is the user language and has the format<br><langcode>-<countrycode>, where<br>•<br>langcode is the language code according to<br>the ISO 639 standard; we accept both two-<br>letter codes (ISO 639-1) and three-letter<br>codes (ISO 639-2);<br>•<br>countrycode is the country code according to<br>the ISO 3166 standard.<br>An example is en-GB.|
|**datalanguage**|string|It is the language in which are displayed the user<br>data, see above for the language.|
|**phone**|string|User phone number.|
|**mobile**|string|User mobile phone number.|
|**email1**|string|First user email address.|
|**email2**|string|Additional email address for the user.|
|**email3**|string|Additional email address for the user.|
|**sid**|string|User Security Identifier (SID). See Microsoft<br>Documentation on Security Identifiers for more<br>details.|
|**expirationdate**|string|The date in which the user expires.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
18

A5E50361214-AA


_4 Users_

_4.2 Get User Details_

|Property|Type|Description|
|---|---|---|
|**alertsbeforeexpirationdate**|string|It is the number of days from which a warning<br>appears to the user notifying him/her about the user<br>expiration.|
|**passwordexpirationdays**|string|It is the number of days for which the password is<br>valid.|
|**alertbeforepasswordexpirationdays**|string|It is the number of days from which a warning<br>appears to the user notifying him/her about the<br>password expiration.|
|**autologoff**|string|It is equal to TRUE if the user automatic logoff is<br>enabled, FALSE otherwise.|
|**timebeforeautologoff**|string|It is the number of minutes that must elapse before<br>a user is automatically logged off from the system<br>(session-based).|
|**imported**|integer|It is equal to 1 if the user has been imported from<br>Windows local users, 0 otherwise.|
|**enabled**|integer|It is equal to 1 if the user can authenticate into<br>UMC, 0 otherwise.|
|**locked**|integer|It is equal to 1 if the user is locked, 0 otherwise.|
|**mustchange**|integer|It is equal to 1 if the user must change password, 0<br>otherwise.|
|**offline**|integer|It is equal to 1 if the user is offline, 0 otherwise.<br>When creating a user, you can flag it as_ offline_.<br>UMC provisioning service checks if the offline user<br>exists in Active Directory:<br>•<br>if the user is present, user data are<br>synchronized and the user becomes online,<br>•<br>otherwise the user remains offline.<br>The user name of offline users must follow the AD<br>pattern_ <domainName>\<ADuserName>_ . They do<br>not have a UMC password, as they cannot<br>authenticate until they become online.|
|**importedfromgroup**|integer|It is equal to 1 if the user has been imported<br>through imported Active Directory group, 0<br>otherwise.|
|**importedfromad**|integer|It is equal to 1 if the user has been imported from<br>Active Directory domain users, 0 otherwise.|
|**canchange**|integer|It is equal to 1 if the user can change password, 0<br>otherwise.|



**attributes property Array**


Each attribute object has the following properties:


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
19
A5E50361214-AA


_4 Users_

_4.3 Create User_

|Property|Type|Description|
|---|---|---|
|**name**|string|Attribute name.|
|**value**|string|Attribute value.|



**roles property Array**


Each role object has the following properties:

|Property|Type|Description|
|---|---|---|
|**name**|string|Role name.|
|**id**|string|Role identifier.|
|**description**|string|Role description.|



**groups property Array**


Each group object has the following properties:

|Property|Type|Description|
|---|---|---|
|**name**|string|Group name.|
|**id**|string|Group identifier.|
|**imported**|integer|It is equal to 1 if the group is imported, 0 otherwise.|
|**objver**|integer|This is an integer that is incremented at each user modification.|
|**sid**|NA|Group Security Identifier (SID). See Microsoft Documentation on Security<br>Identifiers for more details|
|**description**|string|Group description.|


##### **4.3 Create User**


Creates a new user. In case of success the object is returned including the assigned id. Note that the
password specified for the user is not bound to password policies.

|example URL|https://localhost/UMC/slwapi/users/add|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
20

A5E50361214-AA


_4 Users_

_4.3 Create User_


**Request JSON Example**


It is optional. It is mandatory only if parameters in the query string are not present.


If the user is offline, the value of the **offline** property assumes the value **true** that corresponds to 1. If
the user is not offline, the **offline** property is not part of the JSON file. The meaning is the same as
described in Get User Details. Empty passwords are not allowed.



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-20-0.png)



**Request JSON Description**


For the description of the single user properties see [Get User Details.](https://wemes.siemens.com/wiki/display/UMC/Get+User+Details)


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-20-1.png)



**Response JSON Description**


For the common properties see Common Response Information. For the description of the single user
properties see Get User Details. See above for the management of the **offline** property.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
21
A5E50361214-AA


_4 Users_

_4.4 Update User - Basic_

##### **4.4 Update User - Basic**


Updates the following basic user properties:


             - **fullname**


             - **password** (empty passwords are not allowed)


             - **enabled**


             - **mustchange**


             - **canchange**


Note that the password specified for the user is not bound to password policies.

|example URL|https://localhost/UMC/slwapi/users/updateinline|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Parameters**|None.|



**Request JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-21-0.png)



**Request JSON Description**


For the description of the single user properties see Get User Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-21-1.png)



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
22

A5E50361214-AA


_4 Users_

_4.5 Update User - Full_

![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-22-0.png)


**Response JSON Description**


For the common properties see Common Response Information. For the description of the single user
properties see Get User Details.

##### **4.5 Update User - Full**


Performs a full update of a user. All the modifiable user properties can be updated.

|example URL|https://localhost/UMC/slwapi/users/update|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-22-1.png)







User Management Component 2.9.2 - UMC Service Layer API Developer Manual
23
A5E50361214-AA


_4 Users_

_4.5 Update User - Full_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-23-0.png)



**Request JSON Description**


For the description of the single user properties see Get User Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-23-1.png)





User Management Component 2.9.2 - UMC Service Layer API Developer Manual
24

A5E50361214-AA


_4 Users_

_4.6 Unlock User_

![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-24-0.png)


**Response JSON Description**


For the common properties see Common Response Information. For the description of the single user
properties see Get User Details.

##### **4.6 Unlock User**


Unlocks a user.

|example URL|https://localhost/UMC/slwapi/users/unlock|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Parameters**|None.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
25
A5E50361214-AA


_4 Users_

_4.7 Delete Users_


**Request JSON Example**

![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-25-0.png)


**Request JSON Description**


For the description of the single user properties see Get User Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-25-1.png)



**Response JSON Description**


For the common properties see Common Response Information.

##### **4.7 Delete Users**


Deletes a list of users.

|example URL|https://localhost/UMC/slwapi/users/delete{/id}|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example**


Optional. Mandatory only if id is not present.



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-25-2.png)





User Management Component 2.9.2 - UMC Service Layer API Developer Manual
26

A5E50361214-AA


_4 Users_

_4.8 Browse AD Users_





**Request JSON Description**


For the description of the single user properties see Get User Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-26-1.png)



**Response JSON Description**


For the common properties see Common Response Information.


**deleted property Array**


Each deleted object has the following properties:

|Property|Type|Description|
|---|---|---|
|**id**|integer|Identifier of the user that has been deleted.|
|**result**|N/A|See Common Response Information.|


##### **4.8 Browse AD Users**


Browses the users in the UMC database that have been imported from Active Directory (AD).






|example URL|https://localhost/UMC/slwapi/adusers{/s*}|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-**<br>**Type**|application/json|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
27
A5E50361214-AA


_4 Users_

_4.8 Browse AD Users_

|example URL|https://localhost/UMC/slwapi/adusers{/s*}|
|---|---|
|**Request Parameters**|The search string.<br>**Example**: https://localhost/UMC/slwapi/adusers/user*<br>The service finds all users that match the string** user*** in the username<br>field.|



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-27-0.png)



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
28

A5E50361214-AA


_4 Users_

_4.9 Import Users_


**Response JSON Description**


In case of success an array of user objects, including the assigned identifiers, is returned. For the
common properties see Common Response Information. For the description of the single user
properties see Get User Details.

##### **4.9 Import Users**


Imports Active Directory (AD) or Windows local users.

|example URL|https://localhost/UMC/slwapi/users/import|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example Version 190 valid from UMC 1.9.1**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-28-0.png)



**Request JSON Example Version 0 valid prior to UMC 1.9.1**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-28-1.png)



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
29
A5E50361214-AA


_4 Users_

_4.10 Reset Password_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-29-0.png)



**Request JSON Description**


For the description of the single user properties see Get User Details.


**Response JSON Example**




##### **4.10 Reset Password**

Performs the password reset of a specified user. The new password must not necessarily conform to
the Global Account Policy Properties. For more details on these properties, see _User Management_
_Component API SDK Developer Manual_ .


The user performing the action is represented by the input identity handle parameter and must have
the function right **UM_ADMIN** or both the function rights **UM_VIEW** and **UM_RESETPSW** . For a
detailed list of UM function rights, see the Appendix of _User Management Component API SDK_
_Developer Manual_ .


Empty passwords are not allowed.

|example URL|https://localhost/UMC/slwapi/resetpsw|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-29-2.png)



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
30

A5E50361214-AA


_4 Users_

_4.11 Get All System Users_


**Request JSON Description**

|Property|Type|Description|
|---|---|---|
|**usertoreset**|string|Name of the user whose password has to be reset.|
|**pswtoreset**|string|The new value of the password.|



**Response JSON Example**

![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-30-0.png)


**Response JSON Description**


For the common properties see Common Response Information.

##### **4.11 Get All System Users**


Returns data related to all imported windows local users and all imported virtual service account users.


For a description of this kind of users and how to import them into UMC see [Import Windows Local](https://momwiki01.industrysoftware.automation.siemens.com/display/UMC/Import+Windows+Local+Users)

[Users or Virtual User Accounts.](https://momwiki01.industrysoftware.automation.siemens.com/display/UMC/Import+Windows+Local+Users)

|example URL|https://localhost/UMC/slwapi/systemusers|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-30-1.png)



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
31
A5E50361214-AA


_4 Users_

_4.11 Get All System Users_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-31-0.png)



**Response JSON Description**


For the common properties see Common Response Information.


**users property Array**


Each user object has the following properties:

|Property|Type|Description|
|---|---|---|
|**id**|integer|User identifier, it is a 32 bit number greater than zero where the 31st bit is used<br>to store the information if the user is imported or not. If the 31st bit is equal to 1<br>the user is imported from Active Directory, 0 otherwise. The ID ranges are as<br>follows:<br>•<br>1-20: reserved for UMC built in users;<br>•<br>21- 1073741844: UMC users created from scratch;<br>•<br>1073741845 to 2147483647: Imported users.|
|**objver**|integer|This is an integer that is incremented at each user modification.|
|**name**|string|User name.|
|**fullname**|string|User full name.|
|**comment**|string|A note that can be added to the user (optional).|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
32

A5E50361214-AA


_4 Users_

_4.11 Get All System Users_

|Property|Type|Description|
|---|---|---|
|**userflags**|integer|It is a 16 bit number bit mask representing the following flags, the order is from<br>the LSB (less significant bit) to the MSB (most significant bit) :<br>1.<br>User Must Change Password: it is equal to 1 if the user must change<br>password, 0 otherwise.<br>2.<br>User Can Change Password: it is equal to 1 if the user can change<br>password, 0 otherwise.<br>3.<br>User Locked: it is equal to 1 if the user is locked, 0 otherwise.<br>4.<br>User Enabled: it is equal to 1 if the user can authenticate into UMC, 0<br>otherwise.<br>5.<br>User imported from AD: it is equal to 1 if the user has been imported<br>from Active Directory domain users, 0 otherwise.<br>6.<br>User imported from Local: it is equal to 1 if the user has been imported<br>from Windows local users, 0 otherwise.<br>7.<br>User imported from group: it is equal to 1 if the user has been imported<br>through imported Active Directory group, 0 otherwise.<br>8.<br>User offline: it is equal to 1 if the user is offline, 0 otherwise. See Get<br>User Details for additional information.<br>9.<br>_Not used._<br>10.<br>_Not used_.<br>11.<br>_Not used._<br>12.<br>_Not used._<br>13.<br>_Not used._<br>14.<br>_Not used._<br>15.<br>_Not used._<br>16.<br>_Not used._|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
33
A5E50361214-AA


## **5 Groups**

The following APIs are dedicated to group management:


             - Get All Groups


             - Get Group Details


             - Create Group


             - Update Group - Basic


             - Update Group - Full


             - Delete Groups


             - Browse AD Groups


             - Import Groups from AD

##### **5.1 Get All Groups**


Returns data related to all UMC groups.

|example URL|https://localhost/UMC/slwapi/groups|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-33-0.png)







User Management Component 2.9.2 - UMC Service Layer API Developer Manual
34

A5E50361214-AA


_5 Groups_

_5.2 Get Group Details_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-34-0.png)



**Response JSON Description**


For the common properties see Common Response Information.


**groups property Array**


Each group object has the following properties:

|Property|Type|Description|
|---|---|---|
|**description**|string|Group description.|
|**id**|integer|Group identifier.|
|**imported**|integer|It is equal to 1 if the group is imported from Active Directory, 0 otherwise.|
|**name**|string|Group name.|
|**objver**|integer|This is an integer that is incremented at each modification.|
|**offline**|integer|It is equal to 1 if the group is offline, 0 otherwise.<br>When creating a group, you can flag it as_ offline_. UMC provisioning service<br>checks if the offline group exists in Active Directory:<br>•<br>if the group is present, group data are synchronized, the AD users<br>members of the groups are imported into UMC and the group becomes<br>online,<br>•<br>otherwise the group remains offline.<br>The group name of offline users must follow the AD pattern_ <domainName>\_<br>_<ADgroupName>_ .|
|**sid**|string|N/A This string is always empty.|


##### **5.2 Get Group Details**


Returns all the details related to the group associated to the input id.

|example URL|https://localhost/UMC/slwapi/groups/{/id}|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/url-encoding|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
35
A5E50361214-AA


_5 Groups_

_5.2 Get Group Details_


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-35-1.png)



**Response JSON Description**


For the common properties see Common Response Information.


**Group Object**


The group object has the following properties:

|Property|Type|Description|
|---|---|---|
|**name**|string|Group name.|
|**id**|integer|Group identifier.|
|**imported**|integer|It is equal to 1 if the group is imported from Active Directory, 0 otherwise.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
36

A5E50361214-AA


_5 Groups_

_5.3 Create Group_

|Property|Type|Description|
|---|---|---|
|**offline**|integer|It is equal to 1 if the group is offline, 0 otherwise.<br>When creating a group, you can flag it as_ offline_. UMC provisioning service<br>checks if the offline group exists in Active Directory:<br>•<br>If the group is present, group data are synchronized, the AD users<br>members of the groups are imported into UMC and the group becomes<br>online,<br>•<br>Otherwise the group remains offline.<br>The group name of offline users must follow the AD pattern_ <domainName>\_<br>_<ADgroupName>_.|
|**objver**|integer|This is an integer that is incremented at each modification.|
|**description**|string|Group description.|
|**lastsync**|N/A|_Not used_.|
|**syncstatus**|N/A|_Not used_.|
|**sadsstatus**|string|SADS offline synchronization.<br>Possible string values:<br>"**SADS_NOSTATUS**", "**SADS_EMPTY**", "**SADS_SYNC**"<br>See Group SADS Syncronization Status Values for more details.|
|**sid**|string|Group Security Identifier (SID). See Microsoft Documentation on Security<br>Identifiers for more details.|



**roles property Array**


Each role object has the following properties:

|Property|Type|Description|
|---|---|---|
|**name**|string|Role name.|
|**id**|string|Role identifier.|
|**description**|string|Role description.|


##### **5.3 Create Group**


Creates a new group. In case of success the object is returned including the assigned id.

|example URL|https://localhost/UMC/slwapi/groups/add|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
37
A5E50361214-AA


_5 Groups_

_5.4 Update Group - Basic_


**Request JSON Example**

![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-37-0.png)


**Request JSON Description**


For the description of the single group properties see Get Group Details.


If the group is offline, the value of the **offline** property assumes the value **true** that corresponds to 1. If
the group is not offline, the **offline** property is not part of the JSON file. The meaning is the same as
described in Get Group Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-37-1.png)





**Response JSON Description**


For the common properties see Common Response Information. For the description of the single user
properties see Get Group Details. See above for the management of the **offline** property.

##### **5.4 Update Group - Basic**


Updates the following basic user properties:


             - **name**,


             - **domain**,


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
38

A5E50361214-AA


_5 Groups_

_5.4 Update Group - Basic_




            - **description** .

|example URL|https://localhost/UMC/slwapi/groups/updateinline|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-38-0.png)



**Request JSON Description**


For the description of the single group properties see Get Group Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-38-1.png)





**Response JSON Description**


In case of success the object is returned including the assigned id. For the common properties see
Common Response Information. For the description of the single group properties see Get Group

Details.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
39
A5E50361214-AA


_5 Groups_

_5.5 Update Group - Full_

##### **5.5 Update Group - Full**


Performs a full update of a group. All the modifiable group properties can be updated.

|example URL|https://localhost/UMC/slwapi/groups/update|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-39-0.png)



**Response JSON Description**


For the description of the single user properties see Get Group Details.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
40

A5E50361214-AA


_5 Groups_

_5.6 Delete Groups_



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-40-0.png)



**Response JSON Description**


For the common properties see Common Response Information. For the description of the single user
properties see Get Group Details.

##### **5.6 Delete Groups**


Deletes a list of groups.

|example URL|https://localhost/UMC/slwapi/groups/delete|
|---|---|
|**Request HTTP Verb**|POST|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
41
A5E50361214-AA


_5 Groups_

_5.6 Delete Groups_

|Request Content-Type|application/json|
|---|---|
|**Request Parameters**|None.|



**Request JSON Example**

![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-41-0.png)


**Request JSON Description**


For the description of the single group properties see Get Group Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-41-1.png)





**Response JSON Description**


In case of success the object is returned including the assigned id. For the common properties see
Common Response Information.


**groups property Array**


Each groups object has the following properties:

|Property|Type|Description|
|---|---|---|
|**id**|integer|Identifier of the group that has been deleted.|
|**result**|N/A|See Common Response Information.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
42

A5E50361214-AA


_5 Groups_

_5.7 Browse AD Groups_

##### **5.7 Browse AD Groups**


Browses the groups in the UMC database that have been imported from Active Directory (AD).







|example URL|https://localhost/UMC/slwapi/adgroups{/s*}|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-**<br>**Type**|application/json|
|**Request Parameters**|The search string.<br>**Example**: https://localhost/UMC/slwapi/adgroups/umc*<br>The service finds all groups that match the string** umc*** in the** groupname**<br>field.|


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-42-0.png)







**Response JSON Description**


In case of success an array of groups objects, including the assigned identifiers, is returned. For the
common properties see Common Response Information. For the description of the single user
properties see Get Group Details.

##### **5.8 Import Groups from AD**


Imports groups from Active Directory (AD).

|example URL|https://localhost/UMC/slwapi/groups/import|
|---|---|
|**Request HTTP Verb**|POST|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
43
A5E50361214-AA


_5 Groups_

_5.8 Import Groups from AD_

|Request Content-Type|application/json|
|---|---|
|**Request Parameters**|None.|



**Request JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-43-0.png)



**Request JSON Description**


For the description of the single user properties see Get Group Details.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-43-1.png)

**JSON Description**


For the common properties see Common Response Information. For the description of the single user
properties see Get Group Details.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
44

A5E50361214-AA


## **6 Roles**

The following APIs are dedicated to role management:


             - Get All Roles


             - Get Role Details


             - Create Role


             - Update Role


             - Delete Roles

##### **6.1 Get All Roles**


Returns data related to all UMC roles.

|example URL|https://localhost/UMC/slwapi/roles|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-44-0.png)







User Management Component 2.9.2 - UMC Service Layer API Developer Manual
45
A5E50361214-AA


_6 Roles_

_6.1 Get All Roles_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-45-0.png)



**Response JSON Description**


For the common properties see Common Response Information.


**roles property Array**


Each role object has the following properties:



|Property|Type|Description|
|---|---|---|
|**id**|integer|Role identifier. 0 and negative IDs are not allowed. The ID ranges are as<br>follows:<br>•<br>1-20: reserved to system roles;<br>•<br>21-32600: UMC roles created from scratch.|
|**name**|string|Role name.|
|**description**|string|Role description.|
|**application**|-|_Not used._|
|**function_rights**|function<br>right<br>Array|The set of function rights associated to the role. If the role has no<br>associated function rights the value is** []**, if the role has all the associated<br>function rights the value is** all**, this is the case of the** Administrator** built-<br>in role. See below for the description of the function right object<br>properties.|


**function rights property Array**





Each function right object has the following properties:

|Property|Type|Description|
|---|---|---|
|**name**|string|Function right name.|
|**id**|integer|Function right identifier.|
|**description**|string|Function right description.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
46

A5E50361214-AA


_6 Roles_

_6.2 Get Role Details_


##### **6.2 Get Role Details**

Returns all the details related to the role associated with the input id.

|example URL|https://localhost/UMC/slwapi/roles/{/id}|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-46-0.png)







**Request JSON Description**


For the common properties see Common Response Information, whereas for the description of the
single role properties see Get All Roles.

##### **6.3 Create Role**


Creates a new role. In case of success the object is returned including the assigned id. The number of
roles present in the system cannot exceed 200. In addition a database constraint on the role identifiers
exists. In case you get an error message that no more role identifiers are available, to create new
roles, you have first to purge the existing one with the corresponding **umconf** command. See the
_UMCONF User Manual_ for more details.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
47
A5E50361214-AA


_6 Roles_

_6.4 Update Role_

|Request HTTP Verb|POST|
|---|---|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example**


Optional. It is mandatory only if parameters in the query string are not present.



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-47-0.png)



**Request JSON Description**


For the description of the single role properties see Get All Roles.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-47-1.png)



**Response JSON Description**


For the common properties see Common Response Information. For the description of the single user
properties see Get All Roles.

##### **6.4 Update Role**


Performs a full update of a role. All the modifiable role properties can be updated.

|example URL|https://localhost/UMC/slwapi/roles/update|
|---|---|
|**Request HTTP Verb**|POST|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
48

A5E50361214-AA


_6 Roles_

_6.4 Update Role_



|Request Content-Type|application/json|
|---|---|
|**Request Parameters**|None.|


**Request JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-48-0.png)



**Request JSON Description**


For the description of the single role properties see Get All Roles.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-48-1.png)





User Management Component 2.9.2 - UMC Service Layer API Developer Manual
49
A5E50361214-AA


_6 Roles_

_6.5 Delete Roles_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-49-0.png)



**Response JSON Description**


For the common properties see Common Response Information. For the description of the single role
properties see Get All Roles.

##### **6.5 Delete Roles**


Deletes a list of users.

|example URL|https://localhost/UMC/slwapi/roles/delete{/id}|
|---|---|
|**Request HTTP Verb**|POST|
|**Request Content-Type**|application/json|
|**Request Parameters**|None.|



**Request JSON Example**


Optional. Mandatory only if id is not present.

![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-49-1.png)


**Request JSON Description**


For the description of the single role properties see Get All Roles.


**Response JSON Example**



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-49-2.png)





User Management Component 2.9.2 - UMC Service Layer API Developer Manual
50

A5E50361214-AA


_6 Roles_

_6.5 Delete Roles_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-50-0.png)



**Response JSON Description**


For the common properties see Common Response Information, for the description of the single role
properties see Get All Roles.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
51
A5E50361214-AA


## **7 UMC APIs Error Codes**

All the UMC APIs return a boolean value or an object handle. If the API is successful, the returned
boolean value is true or the object handle is well formed; otherwise the returned boolean value is false,
or null is returned instead of the object handle. If the API fails an error code can be retrieved calling the
**SL_GetLastError** method. **SL_RESULT** defines the type of error. In what follows we list the possible

error codes.


**Generic Errors**

|Name|Hexadecimal Value|Decimal Value|Description|
|---|---|---|---|
|SL_SUCCESS|0X00|0|No errors have occurred.|
|SL_GENERROR|0X01|1|Generic error.|
|SL_BAD_HANDLE|0x114|276|Internal error for invalid handle.|
|SL_NOSESSION|0X30|48|The Web session is expired.|



**Authentication Errors**









|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_USERLOCKED|0X02|2|The user for whom you want to<br>perform the authentication is<br>locked.|
|SL_USERDISABLED|0X03|3|The user for whom you want to<br>perform the authentication is<br>disabled.|
|SL_WRONGUSERNAMEPASSWORD|0X04|4|During the authentication phase,<br>the user name or password are<br>incorrect.|
|SL_PASSWORDPOLICYVIOLATION|0X05|5|Password policy violation<br>(determined by UMC account<br>policies). For a detailed list of<br>Account Policies, see_ User_<br>_Management Component API_<br>_SDK Developer Manual_.|
|SL_USERMUSTCHANGEPASSWORD|0X06|6|The user password must be<br>changed.|
|SL_PASSWORDEXPIRED|0X07|7|The user password is expired.|
|SL_FAILED|0X0A|10|Generic operation failed.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
52

A5E50361214-AA


_7 UMC APIs Error Codes_


_6.5 Delete Roles_









|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_ALREADYLOCKED|0X0B|11|The UMC object is already<br>locked.|
|SL_COMMERR|0X0C|12|Transmission/Communication<br>error.|
|SL_NOTIMPL|0X10|16|Returned if a not implemented<br>method is invoked.|
|SL_CHANGEPSWDISABLE|0X19|25|The user cannot change the<br>password.|
|SL_USERUNKNOWN|0X20|32|The user is not present in the<br>system.|
|SL_USERNEVEREXPIRE|0X21|33|The user never expires.|
|SL_TICKETEXPIRED|0X22|34|The authentication ticket is<br>expired.|
|SL_USER_EXPIRED|0x27|39|The user is expired.|
|SL_PSWMINLEN_ERR|0x120|288|The account policy related to the<br>minimal password length has<br>been violated.|
|SL_PSW_CHANGE_FAIL|0X154|340|Password change failure.|
|SL_INVALID_NONCE|0x166|358|Login failed: invalid token. This<br>event may occur if you try to<br>access the login page directly<br>from the URL or if you leave the<br>login page open.|
|SL_WEAK_AUTH|0x167|359|Login failed: access not allowed<br>using weak authentication<br>method.|


**CRUD Operation Errors**









|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_ALREADYEXIST|0x0D|13|The UMC object already<br>exists.|
|SL_LOCK_NEEDED|0x23|35|A lock is needed to complete<br>the operation.|
|SL_NOT_LOCKED|0x24|36|The UMC object is not locked<br>so you cannot unlock it.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
53
A5E50361214-AA


_7 UMC APIs Error Codes_

_6.5 Delete Roles_







|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_OBJVERMISMATCH|0X31|49|A UMC object has been<br>simultaneously modified by<br>two Web UI instances and an<br>object version mismatch has<br>been detected.|
|SL_INVALID_OPERATION|0x103|259|The operation cannot be<br>performed on the selected<br>object.|
|SL_OBJ_DOES_NOT_EXIST|0x111|273|The UMC object does not<br>exist or has not yet been<br>saved into the UMC<br>database.|
|SL_OBJECT_LOCKED_IN_DATABASE|0X153|339|The UMC object is already<br>locked.|
|SL_FAIL_NOTAMASTER|0x160|352|An attempt has been made to<br>modify the UMC database on<br>a machine that is not a<br>master.|
|SL_FAIL_BINDING_ADMIN_ROLE|0x161|353|An attempt has been made to<br>assign the Administrator role<br>to a group or the user who<br>performed the association,<br>either a UMX user or a Web<br>UI user, does not have the<br>Administrator role.|
|SL_OBJ_OFFLINE|0x0F|15|The user/group for which you<br>want to perform an operation<br>is offline and the operation is<br>not allowed for offline objects.|
|SL_INVALID_NAME_FOR_OFFLINE_OBJ|0x165|357|The offline user/group that<br>you are creating does not<br>follow the pattern<br>_<domainName>\<objName>_.|
|SL_INVALID_SID|0x5C|92|Invalid User Security<br>Identifier (SID). See Microsoft<br>Documentation on Security<br>Identifiers for more details.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
54

A5E50361214-AA


**Provider Operation Errors**





_7 UMC APIs Error Codes_


_6.5 Delete Roles_



|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_INVALID_PROVIDER|0x100|256|Operation not provided by this<br>provider.|
|SL_INVALID_HANDLE|0x101|257|An invalid handle was passed as<br>parameter.|
|SL_ERROR_LOADING_PROVIDER|0x102|258|An error occurred when loading<br>the provider.|


**Internal or Parameter Errors**








|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_INVALID_PARAMETERS|0x104|261|The method has an incorrect<br>parameter.|
|SL_MEMORY_ERROR|0x105|262|Memory allocation error.|
|SL_INITIALIZATION_ERROR|0x106|263|Initialization error.|
|SL_INVALID_LOCK_OPTION|0x108|264|The lock option has not been defined.|
|SL_INVALID_PROPERTY|0x109|265|The property has not been defined for<br>the object.|
|SL_INVALID_CULTURE|0x17B|379|Invalid language|



**File Errors**




|Name|Hexadecimal Value|Decimal Value|Description|
|---|---|---|---|
|SL_ACCESS_FILE_ERROR|0x112|274|Access file error.|
|SL_UNKNOWN_FILE_FORMAT|0x113|275|Unknown file format.|
|SL_FILE_NOT_FOUND|0x50|80|File not found.|
|SL_PATH_NOT_FOUND|0x51|81|Path not found.|
|SL_FILE_CREATION_FAIL|0x52|82|Error during file creation.|
|SL_PATH_CREATION_FAIL|0x53|83|Error during path creation.|
|SL_INVALID_PATH|0x54|84|Invalid path.|



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
55
A5E50361214-AA


_7 UMC APIs Error Codes_

_6.5 Delete Roles_


**Function Rights Errors**







|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_RESOURCE_NOT_FOUND|0x150|336|The user does not have the correct<br>function right to perform the<br>requested operation. This error has<br>the same meaning as the<br>SL_MISSING_FUNCTION_RIGHT<br>error.|
|SL_INVALID_RESOURCE|0x151|337|The function right does not exist.|
|SL_MISSING_FUNCTION_RIGHT|0x152|338|The user does not have the correct<br>function right to perform the<br>requested operation. This error has<br>the same meaning as the<br>SL_RESOURCE_NOT_FOUND<br>error.|


**Service Layer Errors**

|Name|Hexadecimal Value|Decimal Value|Description|
|---|---|---|---|
|SL_CLAIM_EXPIRED|0X155|341|The claim is expired.|
|SL_CLAIM_INVALID|0X156|342|The claim is invalid.|
|SL_JSON_ERROR|0X157|343|The .json file is not well formed.|
|SL_MKTKT_FAILURE|0X158|344|The "make ticket" operation failed.|
|SL_ABORTED|0x159|345|Operation aborted.|



**Package Errors**









|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_PACKAGE_CREATION_FAIL|0x55|85|Package creation failed.|
|SL_PACKAGE_COMPRESSION_FAIL|0x56|86|Package compression<br>failed.|
|SL_PACKAGE_UNCOMPRESSION_FAIL|0x57|87|Package decompression<br>failed.|
|SL_PACKAGE_ENCRYPTION_FAIL|0x58|88|Package encryption<br>failed.|
|SL_PACKAGE_DECRYPTION_FAIL|0x59|89|Package decryption<br>failed.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
56

A5E50361214-AA


_7 UMC APIs Error Codes_


_6.5 Delete Roles_



|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_PACKAGE_RESTORE_FAIL|0x5A|90|Package restore failed.|
|SL_PACKAGE_WRONG_PASSWORD|0x5B|91|Wrong password for the<br>package.|


**Database Errors**









|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_DBFILE_ACCESS_DENIED|0X32|50|The user cannot access a UMC<br>database file.|
|SL_DBFILE_ERROR|0X33|51|Generic UMC database file error.|
|SL_DBFILE_OUT_OF_SPACE|0X34|52|A UMC database file is full.|
|SL_TOO_MANY_GROUPS|0X36|102|Too many groups assigned to a user.|
|SL_TOO_MANY_ROLES|0X37|103|Too many roles assigned to a user or<br>group.|
|SL_TOO_MANY_USERS|0X38|104|Too many users assigned to a group.|
|SL_ROLEIDS_OUT_OF_SPACE|0X35|53|No more role IDs are available in the<br>role database file. A purge of the roles<br>is needed.|


**User Alias Errors**









|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_INVALID_USER_ALIAS|0x5E|94|Invalid user alias name.|
|SL_USER_ALIAS_ALREADY_EXIST|0x5F|95|User alias already exists.|
|SL_BAD_PKI_FILTER_NAME|0x115|277|Invalid filter name or filter name<br>not present when authmode =<br>SL_PKI_FILTER_MASK.|


**Secure Application Data Support (SADS) Errors**









|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_INVALID_DOMAIN_NAME|0x60|96|Invalid domain name.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
57
A5E50361214-AA


_7 UMC APIs Error Codes_

_6.5 Delete Roles_







|Name|Hexadecimal<br>Value|Decimal<br>Value|Description|
|---|---|---|---|
|SL_NOT_CURRENT_DOMAIN|0x61|97|Input domain name is not the<br>current domain.|
|SL_INVALID_KEY|0x70|112|Invalid key.|
|SL_KEY_GENERATION_FAIL|0x71|113|Error during key generation.|
|SL_KEY_ENCRYPTION_FAIL|0x72|114|Error during key encryption.|
|SL_KEY_DECRYPTION_FAIL|0x73|115|Error during key decryption.|
|SL_KEY_NOT_FOUND|0x74|116|Key not found.|
|SL_KEY_ENCRYPTION_NOT_ENABLED|0x75|117|Application key protection<br>(global policies) not enabled.|
|SL_MAX_NUM_KEY|0x76|118|The maximum number of<br>allowed keys has been<br>reached.|
|SL_KEY_DECRYPTION_NO_ID_FOUND|0x77|119|No SUID of the identity has<br>been found in EAK array.|
|SL_SADS_VERSION_ERROR|0x78|120|Wrong SADS version.|
|SL_WRONG_IDENTITY|0x79|121|Ticket authentication error<br>while decrypting a key.|
|SL_EAK_BAD_FORMAT|0x80|128|Bad format of the encryption<br>application object.|
|SL_SUBJECT_NOT_ENABLED|0x81|129|Encryption not enabled for the<br>specified subject.|
|SL_SUBJECT_KEY_OBSOLETE|0x82|130|The decryption has been<br>executed using an obsolete<br>key.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
58

A5E50361214-AA


## **8 Account Policies**

##### **8.1 Read Account Policies**

|command|getglobalaccountpolicies|
|---|---|
|**example URL**|https://localhost/UMC/slwapi/getglobalaccountpolicies|
|**HTTP Verb**|POST|
|**Parameters**|none|
|**Data**||
|**Result**|`{`<br>`"version" : 0,`<br>`"operation" : "getaccountpolicyanswer",`<br>`"result" : 0,`<br>`"global_account_policies":{`<br>`"enableLockAfterNAttempts":"1",`<br>`"enablePasswordHistoryByDays":"1",`<br>`"enablePasswordHistoryByNum":"0",`<br>`"maxLoginErrors":"10",`<br>`"minDaysBeforePwdReuse":"120",`<br>`"numPwdBeforeReuse":"5",`<br>`"passwordAging":"60",`<br>`"passwordMaxLen":"120",`<br>`"passwordMinAlphaChar":"2",`<br>`"passwordMinLen":"8",`<br>`"passwordMinLowChar":"1",`<br>`"passwordMinNumericChar":"1",`<br>`"passwordMinOtherChar":"0",`<br>`"passwordMinUpChar":"1"}`<br>**Important:**<br>Status is 400 in case of error.|


##### **8.2 Set Account Policies**

User Management Component 2.9.2 - UMC Service Layer API Developer Manual
59
A5E50361214-AA


_8 Account Policies_

_8.3 Restore Default Account Policies_

|example URL|https://localhost/UMC/slwapi/setglobalaccountpolicies|
|---|---|
|**HTTP Verb**|POST|
|**Parameters**|none|
|**Data**|{<br>"passwordMinLen":"8",<br>"passwordMaxLen":"120",<br>"passwordMinLowChar":"1",<br>"passwordMinUpChar":"1",<br>"passwordMinAlphaChar":"2",<br>"passwordMinNumericChar":"1"<br>,"passwordMinOtherChar":"0",<br>"passwordAging":"60",<br>"enableLockAfterNAttempts":true,<br>"maxLoginErrors":"11",<br>"enablePasswordHistoryByDays":"1"<br>,"minDaysBeforePwdReuse":"120",<br>"enablePasswordHistoryByNum":"0",<br>"numPwdBeforeReuse":"5",<br>"passwordHistoryPolicy":"by-days" }|
|**Result**|`{`<br>`"version" : 0,`<br>`"operation" : "setaccountpolicyanswer",`<br>`"result" : 0}`<br>**Important:**<br>Status is 400 in case of error.<br>"passwordHistoryPolicy":"by-num" in Data if<br>"enablePasswordHistoryByNum":"1",|


##### **8.3 Restore Default Account Policies**

|command|restorelaccountpolicytodefault|
|---|---|
|**example URL**|https://localhost/UMC/slwapi/restorelaccountpolicytodefault|
|**HTTP Verb**|POST|
|**Parameters**|none|
|**Data**||



User Management Component 2.9.2 - UMC Service Layer API Developer Manual
60

A5E50361214-AA


_8 Account Policies_

_8.3 Restore Default Account Policies_



![](mds/umc/v2.9.2/UMC_ServiceLayerAPIDeveloperManual_images/UMC_ServiceLayerAPIDeveloperManual.pdf-60-0.png)





User Management Component 2.9.2 - UMC Service Layer API Developer Manual
61
A5E50361214-AA


## **9 Function Rights**

##### **9.1 List Function Rights**







|command|rights|
|---|---|
|**example**<br>**URL**|https://localhost/UMC/slwapi/rights|
|**HTTP Verb**|POST|
|**Parameters**|none|
|**Data**||
|**Result**|{<br>"version" : 0,<br>"operation" : "rightsresult",<br>"result" : 0,<br>"rights" : [{ "name":"UM_ADMIN", "id" : 10001, "description" : "Administer UM<br>Configuration" },<br>{"name":"UM_VIEW", "id" : 10002, "description" : "View UM Configuration" },<br>{"name":"UM_RESETPWD", "id" : 10003, "description" : "Reset user password" },<br>{"name":"UM_RA", "id" : 10004, "description" : "Login from Remote Authentication" },<br>{"name":"UM_UNLOCKUSR", "id" : 10005, "description" : "Unlock User" },<br>{"name":"UM_JOIN", "id" : 10006, "description" : "Create UM Server" },<br>{"name":"UM_ATTACH", "id" : 10007, "description" : "Create UM Agent" },<br>{"name":"UM_RINGMNG", "id" : 10008, "description" : "Join\/Revoke an UM Server<br>to the UM Ring" },<br>{"name":"UM_RESETJOIN", "id" : 10009, "description" : "Reset UM Domain Join" },<br>{"name":"UM_IMPORT", "id" : 10010, "description" : "Import UM Configuration" },<br>{"name":"UM_EXPORT", "id" : 10011, "description" : "Export UM Configuration" },<br>{"name":"UM_BACKUP", "id" : 10012, "description" : "Backup UM Configuration" },<br>{"name":"UM_EXPORTCK", "id" : 10013, "description" : "Export Claim Key" },<br>{"name":"UM_EXPORTDK", "id" : 10014, "description" : "Export Domain Key" },<br>{"name":"UM_ADSYNC", "id" : 10015, "description" : "Manage Active Directory<br>Synchronization" },<br>{"name":"UM_VIEWELG", "id" : 10016, "description" : "View ELG Events" }]}<br>**Important:**<br>Status is 400 in case of error.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
62

A5E50361214-AA


## **10 Change Password**













|command|changepassword|
|---|---|
|**example**<br>**URL**|https://localhost/UMC/slwapi/changepassword|
|**HTTP Verb**|POST|
|**Content-**<br>**Type**|application/json|
|**Parameters**||
|**Data**|`{`<br>`"old_password" = "franz",`<br>`"new_password" = "secret",`<br>`}`<br>list of users to be created|
|**Result**|In case of success the object is returned including the assigned id.<br>`{`<br>`"Version": 0 //the version of the protocol`<br>`"operation": "changepasswordanswer" // identify the`<br>`operation called by the API`<br>`"result": 0 //SL_RESULT`<br>`}`<br>**Important:**<br>Status is 400 in case of error|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
63
A5E50361214-AA


## **11 Authentication IISAPPPOOL identity - only for test**













|command|authlogged|
|---|---|
|**example**<br>**URL**|https://localhost/UMC/slwapi/authlogged|
|**HTTP Verb**|POST|
|**Content-**<br>**Type**|application/json|
|**Parameters**||
|**Data**||
|**Result**|if the apppool identity (umc_pool) is imported in UMC the authentication method return<br>success. This method is only for internal use and only for test purpose.<br>`{"version" : 0,`<br>`"operation" : "loginresult",`<br>`"result" : 0}`<br>**Important:**<br>Status is 400 in case of error.|


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
64

A5E50361214-AA


## **12 Set Identity Property**












|command|setidentityproperty|
|---|---|
|**example**<br>**URL**|https://localhost/UMC/slwapi/setidentityprop|
|**HTTP Verb**|POST|
|**Content-**<br>**Type**|application/json|
|**Parameters**||
|**Data**|`{`<br>`"propcode" = 22,`<br>`"propname" = "",`<br>`"propvalue" = "it-IT",`<br>`}`<br>This is an example to change the current logged user language property|
|**Result**|`{`<br>`"operation": "setidentitypropanswer" // identify the`<br>`operation called by the API`<br>`"result": 0 //SL_RESULT`<br>`}`<br>**Important:**<br>Status is 400 in case of error|



propcode must be one of the following values:


SL_USER_COMMENT 0x05


SL_USER_LANGUAGE 0x16
SL_USER_DATA_LANGUAGE 0x17
SL_USER_EMAIL1 0x102
SL_USER_EMAIL2 0x103
SL_USER_EMAIL3 0x104


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
65
A5E50361214-AA


_12 Set Identity Property_

_9.1 List Function Rights_


SL_USER_FIRST_NAME 0x105
SL_USER_INITIALS 0x106
SL_USER_LAST_NAME 0x107
SL_USER_PHONE 0x108
SL_USER_MOBILE 0x109


or, only for changing custom attributes:
SL_USER_CUSTOM_PROPERTY 0x2FF


The szPropName parameter must be used only when you want to set a custom attribute (it is the name
of the custom property to set), in all other cases this parameter is ignored.


User Management Component 2.9.2 - UMC Service Layer API Developer Manual
66

A5E50361214-AA


