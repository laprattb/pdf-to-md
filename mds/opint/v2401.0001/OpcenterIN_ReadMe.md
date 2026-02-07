![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-0-0.png)
## Opcenter Intelligence 2401.0001

# Release Notes

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


20240409_151232



Copyright © Siemens AG 2024


Technical data subject to change


## Table of Contents

##### 1 General Notes...........................................................................................................5 2 Main Functionalities.................................................................................................8

2.1 Opcenter Intelligence Main Functionalities..................................................................................8


2.2 Opcenter Reporting Main Functionalities.....................................................................................9

##### 3 What's New.............................................................................................................10


3.1 Opcenter Intelligence What's New..............................................................................................10


3.2 Opcenter Reporting What's New.................................................................................................11

##### 4 Documentation ......................................................................................................12 5 Data Sources Compatibility...................................................................................16 6 Obsolete Functionalities........................................................................................18 7 Functional Limitations...........................................................................................19


7.1 Opcenter Intelligence Functional Limitations............................................................................19


7.2 Opcenter Reporting Functional Limitations...............................................................................22

##### 8 Known Technical Issues.........................................................................................23


Opcenter Intelligence 2401.0001 - Release Notes iii


![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-3-0.png)



4 Opcenter Intelligence 2401.0001 - Release Notes


_General Notes_

## 1 General Notes

##### Opcenter Intelligence functionalities - Scope


Siemens AG supports solely Opcenter Intelligence features that are officially documented.
Any improper use of Opcenter Intelligence not expressly described in official documentation will not be supported.


Any hardware or software configuration not expressly mentioned in the documentation is unsupported. For further
information, it is recommended that you open an Incident Request to Siemens DI SW Support Services.
As a result, users must not manually launch any executables installed by Opcenter Intelligence unless explicitly
instructed to do so by the Siemens DI SW Support Services or official Opcenter Intelligence documentation.
Likewise, users must not use any APIs exposed by DLLs installed by Opcenter Intelligence within custom
applications, unless explicitly instructed to do so by Siemens DI SW Support Services or official Opcenter
Intelligence documentation.

##### Integration of Third-Party software


Integration of third-party software with Opcenter Intelligence does not imply that the product supports all the
functionalities provided by the former. Likewise, it does not imply that those third-party software functionalities
that are supported are feasible in all possible configurations. Only those functionalities and configurations
presented and described in Opcenter Intelligence documentation are officially supported in conjunction with
Opcenter Intelligence.

##### Location of Opcenter Intelligence Configuration and Log Files


At the following paths you can find the folders where Opcenter Intelligence configuration files and logs are stored:


**Opcenter Intelligence Configurator Log File**


**File Name** : Siemens.SimaticIT.MIStudio20.PostSetup.log


**Path** : C:\ProgramData\Siemens\Opcenter\Intelligence\IN\LogFiles\SetUp\


Alternatively, if logs are not present in the default location, you can find them in C:
\Users\<username>\AppData\Local\Temp\


**Opcenter Intelligence Configurator XML Files**



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-4-0.png)



**Opcenter Intelligence Core Log File**


**File Name** : Siemens.SimaticIT.UAMI.MIStudio20.ServiceHost.log


**Path** : C:\ProgramData\Siemens\Opcenter\Intelligence\IN\LogFiles\CoreService\

#### Apache Log4j2 vulnerability (Log4shell) - Tableau Server


Some versions of Tableau Server have been affected by the vulnerabilities recently disclosed in products that use
the Log4j Apache library. For this reason, the upgrade to the newly released Opcenter Intelligence version, which
includes an upgrade to Tableau Server latest version, is mandatory. If you cannot perform this upgrade, at the


Opcenter Intelligence 2401.0001 - Release Notes 5


_General Notes_


following link you can find detailed instructions on how to mitigate this issue: https://kb.tableau.com/articles/
issue/apache-log4j2-vulnerability-log4shell-tableau-server-mitigation-steps

##### Data Protection by Design Aspects of DI SW MOM Products and Solutions


In the course of development of DI SW MOM Products and Solutions, DI SW MOM follows the “Data protection by
design” as foreseen in Article 25 of the General Data Protection Regulation (GDPR). This means that data protection
and privacy issues are taken into account starting from the commencement of product development or solution
engineering.


In general, within Siemens, the following processes are implemented:









Data Protection by Design approach is a part of the principles actively adopted by Siemens and integrated in
the secure lifecycle development of products.
Siemens solutions adopt Threat and Risk Analysis (TRA), a Siemens-wide standardized methodology that is
used for product, solution and service business during product development, engineering or service
projects. This methodology is intended to support Siemens teams in identifying typical security weaknesses
and vulnerabilities, analyzing any threats that might exploit these weaknesses or vulnerabilities and
evaluating any resulting risks.



Specifically for DI SW MOM products and solutions, in all data collection and processing activities that potentially
involve personal data in the intended customer use case, DI SW MOM considers appropriate technical and/or
organizational measures, with the goal of adequately addressing the data protection principles and safeguarding
individual rights.


For Opcenter Intelligence the following applies:







Opcenter Intelligence has obtained the TÜV SÜD certification of security in the development process (based
on IEC 62443-4-1). This standard specifies process requirements for the secure lifecycle development of
products used in an Industrial Automation and Control System (IACS). The lifecycle includes:




     
The definition of security requirements


     
Secure design


     
Secure implementation (including coding guidelines), verification and validation


     
Secure defect management, patch management, and product end-of-life



The following personal data is processed by the Opcenter Intelligence solution:










user id

user name

full name

email address



The following data can also be potentially processed depending on the data source:

















Labor (identification of a user) - for the Opcenter EX PH, Opcenter EX DS, Opcenter EX CR, Opcenter Q data

sources
LaborName (Name of labor may be in comments)
LaborClass (registry of possible categories to which a Labor can belong, e.g. line operator, manager, etc.) for the Opcenter EX PH data source
LaborLaborClass (table of relationship between Labor and its possible 1-n classes)
LaborProperty (registry of possible properties)
LaborPropertyStaticValue (value properties)
LaborHierarchy (if there is the need to trace a team)
LaborTimeModel (possible specific labor time model) - for the Opcenter EX DS data source
LaborTimeCategory (registry of time category) - for the Opcenter EX DS data source



Specific attention is dedicated to the processing of personal data belonging to special categories, relevant for the
purpose of detecting the racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union


6 Opcenter Intelligence 2401.0001 - Release Notes


_General Notes_


membership, genetic data, health, sexual orientation or conduct, criminal convictions and offenses or related
security measures of the persons concerned. No such personal data is processed by Opcenter Intelligence.














The personal data processed by Opcenter Intelligence is required for Log-In, Electronic Signature, reporting
functions and notification systems. Therefore, such personal data processed by Opcenter
Intelligence cannot be anonymized or pseudonymized. Such data is stored solely for these reasons, as it is
necessary to identification of the operating personnel, notification by email.
Opcenter Intelligence adopts hashing and encrypting (at rest and in transit).
In Opcenter Intelligence personal data can be deleted when no longer necessary for the designated purpose.
All data related to the Manufacturing Data Warehouse can be deleted by the customer by means of the undeploy operation. On the other hand, personal data may appear in the solution’s data repositories as
database’s records, product file and log files, which are necessary for diagnostic or logging purposes. This
information generated by Opcenter Intelligence is manually deleted as per the designated guidelines.
Opcenter Intelligence Solution makes use of least privilege access control and policies and using
appropriate roles and authorization concepts as individual user Read/Write permission.
Regular review is performed to validate necessity for the purposes for which the personal data was collected
and test the design against purpose limitation.



Opcenter Intelligence 2401.0001 - Release Notes 7


_Main Functionalities_


_Opcenter Intelligence Main Functionalities_

## 2 Main Functionalities


The following pages describe the main functionalities for:








Opcenter Intelligence
Opcenter Reporting


### 2.1 Opcenter Intelligence Main Functionalities

##### What is Manufacturing Intelligence?

Manufacturing Intelligence is a definition that applies to software used to integrate a company's manufacturingrelated data from many sources for the purposes of reporting, analysis and visual summaries. The primary goal is to
turn large amounts of manufacturing data into real knowledge and to consequently drive the business results.


Opcenter Intelligence supplies all the functionalities required to develop, deploy and maintain a solution in order to
analyze manufacturing data according to standard and custom analytical contexts.

##### Main Features


Opcenter Intelligence provides you with the following basic functionalities:











A Manufacturing Analytical Model (MAM) based on ISA-95 international standard for entity definition.
All the features required to extend and customize models and metrics.
A smart support for semantic data mapping between the sources and the MAM.
An application designed to manage and maintain an Opcenter Intelligence Solution.
A presentation/collaboration layer where you can perform and share data analysis.


##### What is a Solution?

A solution is a container of objects that allows you to obtain and import data for immediate use or storage in one or
more data warehouses. It can be composed of:












Projects
Scenarios

Flows

Environments

Time Definitions

Smart Views


##### What is a Project?

A project is a set of different configurations that can address information ingestion (based on complex data
transformation) in a data warehouse. A project is composed of the following items:










A set of project functionalities
One or more sites
A number of project sources
One or more timeline schedules


##### What is a Scenario?

A scenario is the model of hardware and software resources for the project. This model is the abstract
representation of the distribution of servers, services, databases and flows in a network.


8 Opcenter Intelligence 2401.0001 - Release Notes


_Main Functionalities_


_Opcenter Reporting Main Functionalities_

##### What is a Flow?


A flow allows you to load data from a source database to a data warehouse. After you have populated an empty
database (initial load), it is necessary to schedule a periodic run of ETL incremental loads to keep the data
warehouse aligned with the sources.

##### What is an Environment?


An environment represents the physical implementation of a scenario. While configuring an environment, all items
included in the scenario are mapped on real items that exist in a physical environment.

##### What is a Smart View?


A smart view is a part or a projection of the data warehouse content specified to facilitate a particular purpose or
user activity. It is, basically, a partial and/or redefined visualization of the logical schema of the data warehouse.

##### What is a Deploy?


The deploy of a solution or of a smart view is a set of operations performed to make operational all the items
included in the project, according to the details defined during the creation of the environment or of the smart
view.

### 2.2 Opcenter Reporting Main Functionalities


Opcenter Reporting allows end-users to create operational reports by connecting to the defined data sources.


Opcenter Reporting is integrated in the Opcenter Reporting solution package and is the most cost-effective
visualization tool supported by Opcenter Reporting in order to easily benefit from the built-in reports provided by
Siemens MOM products, like for example Opcenter Execution Core, Opcenter Execution Discrete or Opcenter
Execution Process, for which out-of-the-box reports designed using Opcenter Reporting are available and where
Opcenter Reporting can be embedded.


The following functionalities are available:














Define multiple data source connections to Siemens MOM products. Both SQL Server and Oracle server types
are supported. Opcenter Reporting can only be connected to the databases of Siemens MOM products. The
connection to third-party databases is not allowed.
Design reports structure and choose how to show the information that originates either from a database or
another data source by using Combit® List & Label Designer, which is integrated into the application. In the
Designer you can add simple tables, comprehensive master-detail reports/subreports, crosstabs, charts, RTF
text, barcodes, graphics, PDF objects, user defined objects etc. You can also employ a wide variety of charts,
gauges and shapefiles to enhance your reports with professional-quality visuals and drill down the hierarchy
from summary information to more detailed data.
Organize reports within folders.
Clone reports.
Export and import reports.
Define custom entities to expose new data sets in the Designer so that when you create a report the custom
entities you have created will be included in the list of available tables and views.





Opcenter Intelligence 2401.0001 - Release Notes 9


_What's New_


_Opcenter Intelligence What's New_

## 3 What's New


The following pages describe the main new functionalities for:








Opcenter Intelligence
Opcenter Reporting


### 3.1 Opcenter Intelligence What's New

The following functionalities have been released in the current version:

##### Data Sources


Opcenter Intelligence has been tested with the following new data sources:










Opcenter Execution Core 2404 as SQL Server and Oracle data source
Opcenter Execution Electronics 2404 as SQL Server data source
Opcenter Execution Pharma 2211 or higher as Oracle data source
Opcenter Intra Plant Logistics 2404 as SQL Server data source


##### Manufacturing Data Warehouse Data Model Extension

The Manufacturing Data Warehouse SQL Server data model for Opcenter Execution Electronics has been extended
to correctly calculate DPMO (Defects Per Million Opportunities) KPIs in quality dashboards for the Electronics
Industry. The relationship between the **Bill of Material** entity and the **Material Definition** entity has been changed
to support a 1-to-N relationship. To this end, the **MaterialDefinitionBillOfMaterial** entity has been added to the
**Material Model** . The **MaterialModel.pdf** MDW schema has been updated accordingly.

##### Data Mapping File Names' Simplification


The names of PDF mapping files for Opcenter Intelligence data sources have been shortened and simplified to the
format: **OpcenterIN_<product name>_<oldest supported version>_orHigher_Mapping** (for example:
**OpcenterIN_EXPR_v4.0orHigher_Mapping.pdf** ).

##### MDW Data Model Documentation


The following mapping files have been updated:



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-9-0.png)



10 Opcenter Intelligence 2401.0001 - Release Notes


_What's New_


_Opcenter Reporting What's New_

### 3.2 Opcenter Reporting What's New


No new functionalities have been released in the current version.


Opcenter Intelligence 2401.0001 - Release Notes 11


_Documentation_


_Opcenter Reporting What's New_

## 4 Documentation

##### Accessing the Documentation


English documentation files can be found in the following folders:

![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-11-0.png)


The documentation is available on **Support Center** [at the link: https://support.sw.siemens.com/en-US/](https://support.sw.siemens.com/en-US/)

##### Opcenter Intelligence Documentation


The following manuals are available for Opcenter Intelligence in PDF format:



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-11-1.png)











12 Opcenter Intelligence 2401.0001 - Release Notes


_Documentation_


_Opcenter Reporting What's New_



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-12-0.png)






##### Opcenter Reporting Documentation

The following manuals are available for Opcenter Reporting in PDF format:



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-12-1.png)


##### Common Documentation

The following common manuals are available in PDF format for Opcenter Intelligence and Opcenter Reporting:



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-12-2.png)
#### Manufacturing Data Warehouse Documentation

The following additional documents are available:


Opcenter Intelligence 2401.0001 - Release Notes 13


_Documentation_


_Opcenter Reporting What's New_



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-13-0.png)


















##### Entity Mapping Files

The mapping files are available for the following data sources:


















Opcenter Execution Discrete 3.x (SQL Server)
Opcenter Execution Discrete 4.0 (SQL Server)
Opcenter Execution Discrete 4.1-4.2-4.3 (SQL Server)
Opcenter Execution Discrete 4.4 or higher (SQL Server)
Opcenter Execution Process 3.x
Opcenter Execution Process 4.0 or higher
Opcenter Execution Core 8.7 or higher (SQL Server)
Opcenter Execution Electronics 8.9 or higher (SQL Server)
Opcenter Intra Plant Logistics 2210 or higher (SQL Server)
Opcenter Execution Pharma 2211 or higher (Oracle)
SIMATIC IT Line Monitoring System 2.3-2.4-2.5-2.6-2.7
SIMATIC IT Historian 7.2



In these files the yellow columns include an example of the name of the source database and its physical tables, the
green columns include the entities and attributes of the manufacturing data warehouse and the light blue columns
include the corresponding source entities and UI items as well as related mapping information.





14 Opcenter Intelligence 2401.0001 - Release Notes


_Documentation_


_Opcenter Reporting What's New_


##### Documentation Languages









Opcenter Intelligence documentation is available in English and Simplified Chinese.



Opcenter Reporting Installation Manual, Opcenter Reporting User Manual and Combit® List & Label Designer
Manual are available in English.




##### No Longer Released Documentation

Opcenter Intelligence Release Notes in HTML format ( **OpcenterIN_ReadMe.html** ) are no longer released.


Opcenter Intelligence 2401.0001 - Release Notes 15


_Data Sources Compatibility_


_Opcenter Reporting What's New_

## 5 Data Sources Compatibility


Opcenter Intelligence supports the following data sources:



























|Product Family|Product|Product Versions|
|---|---|---|
|**Opcenter EX**|Opcenter Execution Core as SQL Server<br>data source|•<br>•<br>8.0 - 8.1 - 8.2 - 8.3 - 8.4 - 8.5 - 8.6<br>8.7 -8.8 - 8.9 - 2210 - 2304 - 2310<br>(including updates) - 2404|
|**Opcenter EX**|Opcenter Execution Core as Oracle data<br>source|•<br>•<br>8.0 - 8.1 - 8.2 - 8.3 - 8.4 - 8.5 - 8.6<br>8.7 - 8.8 - 8.9 - 2210 - 2304 - 2310<br>(including updates) - 2404|
|**Opcenter EX**|Opcenter Execution Discrete as SQL<br>Server data source|•<br>•<br>•<br>•<br>•<br>3.0<br>3.1 - 3.2 - 3.3<br>4.0<br>4.1 - 4.2 - 4.3<br>4.4 - 2207 - 2207.0001 - 2301 -<br>2301.0001 - 2307 - 2307.0001 - 2401<br>or higher|
|**Opcenter EX**|Opcenter Execution Electronics as SQL<br>Server data source|8.9 - 2210 - 2304 - 2310 (including updates)<br>- 2404|
|**Opcenter EX**|Opcenter Execution Process|•<br>•<br>3.0 - 3.1 - 3.2 - 3.3<br>4.0 - 4.1 - 4.2 - 4.3 - 4.4 - 2207 -<br>2207.0001 - 2301 - 2301.0001 - 2307<br>- 2307.0001 - 2401 or higher|
|**Opcenter EX**|Opcenter Execution Foundation OEE|2207 - 2207.0001 - 2301 - 2301.0001 - 2307 -<br>2307.0001 - 2401 or higher|
|**Opcenter EX**|Opcenter Execution Pharma as Oracle<br>data source|2211 or higher|
|**Opcenter QL**|Opcenter Quality as SQL Server data<br>source|•<br>•<br>11.0 to 11.3<br>12.0|
|**Opcenter QL**|Opcenter Quality as Oracle data source|•<br>•<br>11.0 to 11.3<br>12.0|
|**Opcenter IPL**|Opcenter Intra Plant Logistics as SQL<br>Server data source|2210 - 2304 - 2310 (including updates) -<br>2404|
|**Opcenter IN**|Intelligence Analytical Model|2.x - 3.x (MDW 2.0)|


16 Opcenter Intelligence 2401.0001 - Release Notes


_Data Sources Compatibility_


_Opcenter Reporting What's New_
























|Product Family|Product|Product Versions|
|---|---|---|
|**SIMATIC IT UA**|Unified Architecture Discrete<br>Manufacturing|•<br>•<br>1.0 - 1.1 - 1.2 - 1.3<br>2.3 - 2.4 - 2.5|
|**SIMATIC IT UA**|Unified Architecture Process Industries|•<br>•<br>•<br>1.1 Update 1 - 1.2<br>2.3<br>2.4 - 2.5|
|**CEP**|Camstar Enterprise Platform as SQL<br>Server data source|V7 SU4 - SU5 - SU6 - SU7 - SU8|
|**CEP**|Camstar Enterprise Platform as Oracle<br>data source|V7 SU4 - SU5 - SU6 - SU7 - SU8|
|**QMS**|QMS Professional as SQL Server data<br>source|10.03 - 10.04 - 10.05 - 10.06 - 10.07|
|**QMS**|QMS Professional as Oracle data source|10.03 - 10.04 - 10.05 - 10.06 - 10.07|
|**SIMATIC IT**|Production Suite (PRS)|7.0 SPx - 7.1 - 7.2 - 8.0|
|**SIMATIC IT**|Historian (HST)|7.2|
|**SIMATIC IT**|Line Monitoring System (LMS)|•<br>•<br>2.2 SP1 HF1<br>2.3 - 2.4 - 2.5 - 2.6 - 2.7|
|**SIMATIC IT**|Reporting Framework (RF)|MDW 1.0|
|**SIMATIC IT**|Electronic Batch Recording (eBR) as<br>Oracle data source|6.1.6|
|**Third-Party**<br>**Systems**|SQL Server|2012 or higher|
|**Third-Party**<br>**Systems**|Oracle|12c or higher|



Opcenter Intelligence 2401.0001 - Release Notes 17


_Obsolete Functionalities_


_Opcenter Reporting What's New_

## 6 Obsolete Functionalities


This chapter lists the functionalities and artifacts that were deprecated in previous product versions and are no
longer supported.

#### Windows Authentication


Starting from Opcenter Intelligence 3.3 the default identity provider is the User Management Component (UMC).
Starting from version 3.5 Windows Authentication is no longer supported.


If you are upgrading from a previous version of Opcenter Intelligence, you have to migrate to UMC as Identity
Provider.


To migrate to the new mode, you have to apply specific settings in Opcenter Intelligence Configurator and a manual
operation to add the Windows Administrator user to UMC. For more details, see _Opcenter Intelligence Quick Start_
_Installation Manual_ or _Enterprise or Site Installation Manual_ depending on the license you have purchased.

##### Legacy Tableau® and Microsoft Power BI Integration


Starting from version 3.5 the integration with the following functionalities is no longer supported. For each of them
an alternative functionality is suggested.



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-17-0.png)






#### Microsoft SQL Server Reporting Services Integration

Starting from version 3.5 the integration with the following functionality is no longer supported. An alternative
functionality is suggested.



![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-17-1.png)






##### Operating Systems

Starting from version 2401, Windows Server 2012 R2 x64 is no longer supported.


18 Opcenter Intelligence 2401.0001 - Release Notes


_Functional Limitations_


_Opcenter Intelligence Functional Limitations_


## 7 Functional Limitations

The following pages describe the functional limitations for:








Opcenter Intelligence
Opcenter Reporting


### 7.1 Opcenter Intelligence Functional Limitations

##### Opcenter Intelligence Analytics (Tableau® OEM) Installation Requires Support

When you are installing Opcenter Intelligence Analytics (Tableau® OEM) please contact the Support Team.

##### Mandatory column types cannot be used to modify entity extensions


In the analytical solution project, if you modify an entity extension that was already deployed and on which data
was stored, you cannot use mandatory column types such as **Name**, otherwise the next deployment will fail
because the system will not automatically add a value for that column. The recommended alternative is to use the
**TextAttribute** or **Note** column types.

##### Opcenter Execution Electronics data source: discrepancy between versions 8.9 and 2210


Opcenter Intelligence supports versions 8.9-2210 (including updates) for the Opcenter Execution Electronics (SQL
Server) data source, as shown on the data sources pie menu. However, the 8.9 version database does not contain
the **isQty** and **ChildCount** fields that were added to version 2210. Therefore, if you are using version 8.9, the deploy
of the environment is bound to fail.


As a workaround, you can customize the script of the **SummaryTableOEERawDetails** entity in the **Operational**
**Performance and Quality** model by casting the two missing fields to NULL as in the following example. For more
details on scripts, see also the _Loading a Script_ chapter in _Opcenter Intelligence User Manual_ .


**Example**


Customize the script by replacing:


CAST(ChildCount as float) AS ChildCount,
CAST(isQty as float) AS Qty,


with:


CAST(0 as float) AS ChildCount,
CAST(0 as float) AS Qty,

##### Disabling Anti-Virus Recommended before Tableau Server Installation


Tableau Server installation may fail on a machine where an anti-virus software is installed. It is therefore
recommended you disable the anti-virus before you start installing Tableau. For more details, see https://
[kb.tableau.com/articles/issue/error-tableau-server-initialization-failed-during-installation-with-anti-virus?](https://kb.tableau.com/articles/issue/error-tableau-server-initialization-failed-during-installation-with-anti-virus?_ga=2.43810533.1336776877.1668404981-1736113883.1668148487)
_ga=2.43810533.1336776877.1668404981-1736113883.1668148487

#### Stop and Start Service before Installing Opcenter Intelligence over Previous Version


Opcenter Intelligence 2401.0001 - Release Notes 19


_Functional Limitations_


_Opcenter Intelligence Functional Limitations_


Before launching the installation of Opcenter Intelligence over the previous version, you must manually stop the
**Siemens.SimaticIT.UAMI.MIStudio20.ServiceHost** service and restart it after the installation is completed and
before running Opcenter Intelligence Configurator.

##### Supported Special Characters in Domain User field in Opcenter Intelligence Configurator


In Opcenter Intelligence Configurator, **Opcenter Intelligence Core** section, in the **Domain User** field, the following
special characters are not supported: " / [ ] : ; | =, + * ? < > @ and space.

##### Loading Opcenter Intelligence Analytics (Tableau® OEM) Dashboards in Google Chrome is not possible if protocol is HTTP


In a scenario where Opcenter Intelligence and Opcenter Intelligence Analytics are exposed with two different
domains, the Google Chrome browser cannot be used to load Opcenter Intelligence Analytics Dashboards if the
configured protocol is HTTP. To overcome this issue, you can either use the Mozilla Firefox browser or change the
protocol configuration to HTTPS.

##### Recommendation on User Management Component (UMC) Installation


For security reasons, it is strongly recommended that you install UMC under the path **C:**
**\automation\Siemens\UserManagement** and verify that file system access permissions for drive C:\ have not been
modified.

##### Microsoft SQL Server 2019 Cumulative Update 9 or higher is recommended


If you are using Microsoft SQL Server 2019 versions previous to Cumulative Update 9, random issues may occur
during flow execution. The installation of the latest SQL Server version is therefore recommended.

##### Assigning roles to user groups is no longer supported


Assigning roles to user groups is not supported anymore, as the new licensing model introduced starting from
version 3.2 requires to verify the number of configured users against the number of users allowed by the installed
licenses.

##### Run the setup as Administrator


The setup file **Start.exe** located in the ISO root folder must be executed as administrator (right-click the file and
select **Run as administrator** ).

##### Smart View Deploy fails if Measure/Attribute names differ by a space


In a smart view, if different measures/attributes have names that differ from each other only by a space, the deploy
of the smart view fails because their names must be unique within a query batch or stored procedure.


Example:
**Actual Quantity EquipmentPropertyStaticValue**
**ActualQuantity EquipmentPropertyStaticValue**
As a workaround, you can rename the measures or attributes by editing them in the smart view page.

##### Tracking of discarded records


If a record is discarded due to business logic, it is converted into xml format and included in the failed table to be
analyzed in detail at a later moment. However, some characters are not compatible with xml. They will not


20 Opcenter Intelligence 2401.0001 - Release Notes


_Functional Limitations_


_Opcenter Intelligence Functional Limitations_


therefore be included in the xml and consequently in the failed table. The system will work normally but these
records will not be tracked.

##### Maximum number of columns for a single card in a Smart View


The maximum number of columns of a single card in a Smart View can be obtained by executing the following
calculations:









For the cards in the **Measures** section: _number of selected contexts x 2 + number of selected measures + 3_
_(table key)_, where " _number of selected contexts_ " is the number of cards where one or more attributes have
been selected in the **Attributes** section.
For the cards in the **Attributes** section: _number of selected attributes + 3 (table key)._



This number must not in any case exceed 1024. Neither a warning nor a block is issued in the Smart Views Web page
if the number exceeds this limit.

##### Entities with a hierarchy might generate loop after project synchronization


When you synchronize the project in the **Smart Views** page, for the entities with a hierarchy (like for example
Equipment, OperationExecution, OperationResponse etc.) the hierarchy might generate a loop (for example,
Equipment1 → Equipment2 → Equipment1). In that case, in the **Attributes** cards of the smart view the levels
cannot be selected for that entity.

##### Merge of Measures and Attributes requires Smart View selection


In general you should be able to merge measures and attributes either before or after the creation of a smart view.
However, you must select a smart view before executing the merge operation. In any case, the merge operation will
apply to all the smart views that you have already created or that you will create afterwards.

##### Data load recommended before MDW purge operation


It is recommended that you execute at least one data load before a purge operation of the MDW database.


However, if you have performed a purge without loading data first, you should follow these steps:



1.

2.

3.



Execute a data load.

Purge the MDW again.
Execute a new data load.


##### Maximum value for the Sequence field

The value of the **Sequence** field (a number determining a hypothetical execution order of the Operation Responses
included in the same Operation Execution) in a MDW entity must not exceed 32767. If in the source entity the
sequence value exceeds this number, you should modify the contract of the entity that contains the sequence field
and execute a new calculation to bring back the sequence to the correct value. For more details on this parameter,
see the documentation of _Opcenter Execution Discrete_ and _Opcenter Execution Process_ .

#### License Check delay


When you restart the server, the license check is executed after a delay of five minutes. As a workaround, you can
restart the **Siemens.SimaticIT.UAMI.MIStudio20.ServiceHost** service.

##### UI in German/Chinese/French/Spanish may show labels in English


In the German, Chinese, French or Spanish UI some labels may be shown in English.


Opcenter Intelligence 2401.0001 - Release Notes 21


_Functional Limitations_


_Opcenter Reporting Functional Limitations_

##### Deselecting Rows in Tables


To deselect an item in tables, you have to hold down the CTRL key and click the row you want to deselect. Please
ignore the small grey square and plus sign that are shown on the bottom-right corner when you hover the mouse on
the cell.

### 7.2 Opcenter Reporting Functional Limitations

##### Run the setup as Administrator


The setup file **Start.exe** located in the ISO root folder must be executed as administrator (right-click the file and
select **Run as administrator** ).

##### Report images not exported nor imported with reports


The images used in reports are not exported nor imported with the reports. As a result, after you have imported a
report, you must open it and add the missing images again.

##### Web Designer update not possible using the Modify option


When an update of Combit® List & Label Designer is available and you open a report in Opcenter Reporting using the
Designer, you are prompted to **Modify, repair or remove the program** .
However, the **Modify** option is not visible, and the **Repair** option would not update the program. You must select
**Remove** to uninstall the Web Designer, then open the report again to be prompted to download and install the
updated version of the Web Designer.


22 Opcenter Intelligence 2401.0001 - Release Notes


_Known Technical Issues_


_Opcenter Reporting Functional Limitations_

## 8 Known Technical Issues

##### Opcenter Intelligence

![](mds/opint/v2401.0001/OpcenterIN_ReadMe_images/OpcenterIN_ReadMe.pdf-22-0.png)

#### SQL Server Known Technical Issues


**Snapshot isolation level should always be enabled for SSISDB**


When the SQL Server SSISDB is created, the snapshot isolation level is disabled by default. This can ensue a
deadlock during the parallel execution of two ETL flows. It is suggested that you enable the snapshot isolation level
on this DB and set it as default for all transactions.


**Random flow execution issues depending on the installed SQL Server version**


If you are using Microsoft SQL Server 2019 versions previous to Cumulative Update 9, random issues may occur
during flow execution. The installation of the latest SQL Server version is therefore recommended.


Opcenter Intelligence 2401.0001 - Release Notes 23


