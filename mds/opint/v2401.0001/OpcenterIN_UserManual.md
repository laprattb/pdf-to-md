![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-0-0.png)
## Opcenter Intelligence 2401.0001

# User Manual

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


The remaining trademarks in this publication may be trademarks whose use by third parties for their own purposes


could violate the rights of the owner.


**Disclaimer of Liability**


We have reviewed the contents of this publication to ensure consistency with the hardware and software


described. Since variance cannot be precluded entirely, we cannot guarantee full consistency. However, the


information in this publication is reviewed regularly and any necessary corrections are included in subsequent


editions.


**Cybersecurity Information**


Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation


of plants, systems, machines and networks.


In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement 

and continuously maintain - a holistic, state-of-the-art industrial cybersecurity concept. Siemens products and


solutions constitute one element of such a concept.


Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks.


Such systems, machines and components should only be connected to an enterprise network or the internet if and


to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or


network segmentation) are in place.


For additional information on industrial cybersecurity measures that may be implemented, please visit


[https://www.siemens.com/cybersecurity-industry.](https://www.siemens.com/cybersecurity-industry)


Siemens products and solutions undergo continuous development to make them more secure. Siemens strongly


recommends that product updates are applied as soon as they are available and that the latest product versions


are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase


customer’s exposure to cyber threats.


To stay informed about product updates, subscribe to the Siemens Industrial Cybersecurity RSS feed under


[https://www.siemens.com/cert.](https://www.siemens.com/cert)



Siemens AG


Digital Industries


Postfach 48 48


90026 NÜRNBERG


GERMANY



PL20240130630874732


20240409_161730



Copyright © Siemens AG 2024


Technical data subject to change


## Table of Contents

###### 1 Before you Start ................................................................................................ 9 2 Quick Start to Using Opcenter Intelligence ................................................... 11 3 Managing Access Control................................................................................ 12

3.1 Resetting the Password for the Desktop Explorer Role ..................................................... 13

###### 4 Managing Licenses.......................................................................................... 14 5 How to Configure a Solution .......................................................................... 15


5.1 Creating a Solution .............................................................................................................. 15


5.2 Exporting a Solution ............................................................................................................ 16

###### 6 How to Configure a Project............................................................................. 17


6.1 Creating a Project................................................................................................................. 17


6.2 Editing a Project................................................................................................................... 18


6.3 Adding a Site......................................................................................................................... 19


6.4 Selecting Sources................................................................................................................. 20


6.4.1 Opcenter Execution Core 8.0 to 8.6 SQL Server................................................................................................23


6.4.2 Opcenter Execution Core 8.7 or higher SQL Server..........................................................................................23


6.4.3 Opcenter Execution Core 8.0 to 8.6 Oracle.......................................................................................................24


6.4.4 Opcenter Execution Core 8.7 or higher Oracle .................................................................................................25


6.4.5 Opcenter Execution Discrete SQL Server..........................................................................................................26


6.4.6 Opcenter Execution Electronics 8.9 or higher SQL Server ...............................................................................27


6.4.7 Opcenter Execution Process 3.x........................................................................................................................28


6.4.8 Opcenter Execution Process 4.0 or higher........................................................................................................28


6.4.9 Opcenter Execution Foundation OEE ...............................................................................................................29


6.4.10 Opcenter Execution Pharma Oracle..................................................................................................................30


6.4.11 Intelligence Analytical Model ............................................................................................................................31


6.4.12 Opcenter Quality SQL Server.............................................................................................................................31


6.4.13 Opcenter Quality Oracle ....................................................................................................................................32


6.4.14 Opcenter Intra Plant Logistics SQL Server........................................................................................................33


6.4.15 SIMATIC IT Unified Architecture Discrete Manufacturing ................................................................................34


6.4.16 SIMATIC IT Unified Architecture Process Industries.........................................................................................35


6.4.17 Camstar Enterprise Platform Core SQL Server.................................................................................................35


6.4.18 Camstar Enterprise Platform Core Oracle ........................................................................................................36


6.4.19 QMS Professional SQL Server source................................................................................................................37


6.4.20 QMS Professional Oracle source .......................................................................................................................38


Opcenter Intelligence 2401.0001 - User Manual iii


6.4.21 SIMATIC IT Line Monitoring System ..................................................................................................................39


6.4.22 SIMATIC IT Production Suite..............................................................................................................................39


6.4.23 SIMATIC IT Historian ..........................................................................................................................................40


6.4.24 SIMATIC IT Reporting Framework .....................................................................................................................40


6.4.25 SIMATIC IT Electronic Batch Recording Oracle.................................................................................................41


6.4.26 Third-Party Systems SQL Server source ...........................................................................................................42


6.4.27 Third-Party Systems Oracle source...................................................................................................................43


6.5 How to Configure Model Extensions ................................................................................... 44


6.5.1 Creating a Model Extension...............................................................................................................................44


6.5.2 Selecting the Model Extension Source..............................................................................................................48


6.5.3 Deleting a Model Extension ...............................................................................................................................49


6.6 How to Configure Entity Extensions.................................................................................... 49


6.6.1 Creating an Entity Extension .............................................................................................................................49


6.6.2 Selecting the Entity Extension Source ..............................................................................................................53


6.6.3 Deleting an Entity Extension .............................................................................................................................53


6.7 Planning a Schedule ............................................................................................................ 53


6.8 Displaying the MDW Data Model ......................................................................................... 54

###### 7 How to Configure the Time Definition ........................................................... 57


7.1 Time Management in Smart Views...................................................................................... 57


7.2 Creating a Time Definition................................................................................................... 58


7.3 Creating a Time Hierarchy................................................................................................... 60

###### 8 How to Configure a Scenario.......................................................................... 62


8.1 Creating a Scenario.............................................................................................................. 62


8.2 How to Configure a Server................................................................................................... 63


8.2.1 Creating a Server................................................................................................................................................63


8.2.2 Adding Services to a Server ...............................................................................................................................64


8.3 How to Configure a Database.............................................................................................. 65


8.3.1 Creating a Database...........................................................................................................................................65


8.3.2 Editing a Database .............................................................................................................................................65


8.3.3 Loading a Script .................................................................................................................................................66


8.3.3.1 Recommendations Before Getting Started ......................................................................................................68


8.3.3.2 Example of Custom Script Using the SELECT Statement (LMS source) ..........................................................69


8.3.3.3 Example of Custom Script Using the SELECT Statement (Opcenter EX DS source) .......................................69


8.3.3.4 Example of Custom Script Using a Stored Procedure......................................................................................70

###### 9 How to Configure and Manage Flows ............................................................ 72


iv Opcenter Intelligence2401.0001 - User Manual


9.1 Creating a Flow..................................................................................................................... 72


9.2 Creating a Flow Schedule .................................................................................................... 73


9.3 Editing a Flow....................................................................................................................... 73


9.4 How to Run a Flow ............................................................................................................... 74


9.4.1 Running an Initial Flow ......................................................................................................................................74


9.4.2 Running an Incremental Flow ...........................................................................................................................75


9.4.3 Running a Single Entity......................................................................................................................................75

###### 10 How to Configure and Deploy an Environment............................................. 76


10.1 Creating an Environment..................................................................................................... 76


10.2 Editing an Environment....................................................................................................... 76


10.2.1 Configuring the Properties tab..........................................................................................................................77


10.2.1.1 Opcenter Execution Discrete SQL Server..........................................................................................................78


10.2.1.2 Opcenter Execution Process..............................................................................................................................79


10.2.1.3 Opcenter Execution Foundation OEE ...............................................................................................................79


10.2.1.4 Opcenter Execution Core SQL Server................................................................................................................79


10.2.1.5 Opcenter Execution Core Oracle.......................................................................................................................80


10.2.1.6 Opcenter Execution Electronics SQL Server.....................................................................................................81


10.2.1.7 Opcenter Execution Pharma Oracle..................................................................................................................81


10.2.1.8 Opcenter Quality SQL Server.............................................................................................................................82


10.2.1.9 Opcenter Quality Oracle ....................................................................................................................................82


10.2.1.10 Opcenter Intra Plant Logistics SQL Server........................................................................................................83


10.2.1.11 SIMATIC IT Unified Architecture Discrete Manufacturing ................................................................................84


10.2.1.12 SIMATIC IT Unified Architecture Process Industries.........................................................................................84


10.2.1.13 Camstar Enterprise Platform SQL Server..........................................................................................................84


10.2.1.14 Camstar Enterprise Platform Oracle.................................................................................................................85


10.2.1.15 QMS Professional SQL Server............................................................................................................................86


10.2.1.16 QMS Professional Oracle ...................................................................................................................................86


10.2.1.17 SIMATIC IT eBR Oracle........................................................................................................................................87


10.2.1.18 SIMATIC IT Production Suite..............................................................................................................................87


10.2.1.19 SIMATIC IT Historian ..........................................................................................................................................88


10.2.1.20 SIMATIC IT Line Monitoring System ..................................................................................................................88


10.2.1.21 SIMATIC IT Manufacturing Data Warehouse .....................................................................................................89


10.2.1.22 Third-Party Systems SQL Server .......................................................................................................................90


10.2.1.23 Third-Party Systems Oracle...............................................................................................................................90


10.3 Deploying an Environment.................................................................................................. 90


Opcenter Intelligence 2401.0001 - User Manual v


10.4 Undeploying an Environment ............................................................................................. 91


10.5 Purging the Manufacturing Data Warehouse...................................................................... 91

###### 11 How to Configure Smart Views....................................................................... 93


11.1 Opcenter Intelligence Smart View Data.............................................................................. 93


11.2 Preliminary Operations........................................................................................................ 94


11.2.1 Synchronizing the Project .................................................................................................................................94


11.2.2 Cleaning the Project...........................................................................................................................................95


11.2.3 Merging Measures and Attributes......................................................................................................................95


11.3 Creating a Smart View.......................................................................................................... 96


11.4 Selecting Measures .............................................................................................................. 97


11.5 Selecting Attributes ............................................................................................................. 97


11.6 Deploying a Smart View....................................................................................................... 98


11.7 Undeploying a Smart View .................................................................................................. 99


11.8 Running a Smart View........................................................................................................ 100


11.9 Additional Operations........................................................................................................ 101


11.9.1 Managing Contexts ..........................................................................................................................................101


11.9.2 Editing a Smart View........................................................................................................................................101


11.9.3 Editing Measures, Attributes, or Contexts ......................................................................................................102


11.9.4 Purging a Smart View.......................................................................................................................................102


11.9.5 Deleting a Smart View......................................................................................................................................103


11.9.6 Renaming Measures or Attributes...................................................................................................................103

###### 12 How to Perform Runtime Operations .......................................................... 105


12.1 How to Manage Dashboards using Opcenter Intelligence Analytics............................... 105


12.1.1 Publishing Data Sources using Opcenter Analytics Desktop.........................................................................105


12.1.2 Managing Dashboards using Opcenter Intelligence Analytics ......................................................................107


12.1.3 How to Embed Opcenter IN Analytics Dashboards in a Custom Application ...............................................108


12.1.3.1 SWAC Integration Methods..............................................................................................................................108


12.1.3.2 Embedding Opcenter IN Analytics Dashboards .............................................................................................109

###### 13 Monitoring Operation Execution.................................................................. 111


13.1 Setting the Server-wide Default Logging level in the SSIS Catalog................................. 113

###### 14 How to Upgrade a Reporting Framework 7.0 Solution to Opcenter Intelligence 2401........................................................................................... 114


14.1 Importing the Solution File................................................................................................ 114


14.2 Post-Migration Check......................................................................................................... 114


vi Opcenter Intelligence2401.0001 - User Manual


14.3 Managing Overloaded Scripts ........................................................................................... 115

###### 15 How to Perform Advanced Operations........................................................ 119


15.1 How to Manage the Update of a Data Source Product Version ....................................... 119


15.1.1 Migrating the EquipmentKey in Opcenter Execution Discrete ......................................................................119


15.1.2 Updating the migrated Solution Items ...........................................................................................................121


15.1.3 Retrieving the Start Time for the New Flow....................................................................................................121


15.1.4 Starting the Flow..............................................................................................................................................122


15.2 How to manage interaction between EX FN Cleaning Rules and Opcenter IN Flow
Schedules ........................................................................................................................... 123


15.2.1 Scheduling Rules for Opcenter EX FN Online Database.................................................................................123


15.2.2 Scheduling Rules for Opcenter EX FN Archiving Database ............................................................................124


15.3 Setting Up a Maintenance Plan for the Data Warehouse................................................. 124


15.4 Enabling Change Data Capture and Change Tracking..................................................... 125


15.4.1 Change Data Capture Examples......................................................................................................................126


15.4.2 Change Tracking Examples .............................................................................................................................127


15.5 Managing the size of the SQL Server Integration Services Database SSISDB................. 129

###### 16 Example: Extending a SIMATIC IT LMS Entity .............................................. 130


Opcenter Intelligence 2401.0001 - User Manual vii


![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-7-0.png)



8 Opcenter Intelligence 2401.0001 - User Manual


_Before you Start_


## 1 Before you Start

###### Accessing the Application

To access Opcenter Intelligence, double click the desktop icon and do either of the following:









If you are logged in with the credentials specified for Opcenter Intelligence Administrator, you are directly
logged in to the application.
If the authentication is performed using UMC, you are redirected to UMC Log In page. Log in as the Administrator
user defined in Opcenter Intelligence Configurator, which is the only user who can grant access to other users.


###### The Home Page

The **Home** page is made up of the following cards. Some of the cards may be displayed or not depending on the role
of the logged-in user.

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-8-0.png)

###### The Primary Navigation Bar


The Primary Navigation Bar is displayed on the left-hand side of the page and includes the following commands:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-8-1.png)



Opcenter Intelligence 2401.0001 - User Manual 9


_Before you Start_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-9-0.png)


###### The User Commands

When you click a panel opens, where you can execute the following operations. You can pin or unpin the panel
to the current page.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-9-1.png)











10 Opcenter Intelligence 2401.0001 - User Manual


_Quick Start to Using Opcenter Intelligence_

## 2 Quick Start to Using Opcenter Intelligence


This manual provides a general outline of the main steps that must be executed to use Opcenter Intelligence. The
working environment is a web engineering client from which any authorized user can configure and deploy a
manufacturing intelligence solution.

###### Workflow



1.

2.

3.

4.

5.

6.

7.

8.



Manage Access Control
Configure a Solution
Configure a Project
Configure the Time Definition
Configure a Scenario
Configure Flows
Configure and Deploy an Environment
Perform Runtime Operations


###### Additional Operations








Configure Smart Views
Manage the Update of a Data Source Product Version



Opcenter Intelligence 2401.0001 - User Manual 11


_Managing Access Control_

## 3 Managing Access Control


In this page Administrators can grant users access to the application functionalities by assigning them a predefined
role.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-11-0.png)




###### Prerequisites

You are logged in with the credentials specified for Opcenter Intelligence Administrator.

###### Procedure



1.


2.



In the **Home** page, click the **Access Control** card.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-11-1.png)









12 Opcenter Intelligence 2401.0001 - User Manual


_Managing Access Control_


_Resetting the Password for the Desktop Explorer Role_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-12-0.png)



3.


4.





![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-12-1.png)

Click **Save** .






### 3.1 Resetting the Password for the Desktop Explorer Role

If you have been assigned the Desktop Explorer role, you need to reset your password to be able to publish data
sources in Opcenter Intelligence Analytics using Opcenter Intelligence Analytics Desktop.

###### Prerequisites


You have signed in to Tableau® Server from Tableau® Desktop. For more details, see https://help.tableau.com/
v2021.4/pro/desktop/en-us/sign_in_server.htm




###### Procedure



1.


2.

3.



In the **Roles** page, select the **Desktop Explorer** tile and click **Open** .


In the **Desktop Explorer** page, select a user and click **Reset Analytics Desktop Password** .
In the **Reset Analytics Desktop Password** panel, insert a new password, which must contain:




      
at least 1 lower-case alphabetical character,


      
at least 1 upper-case alphabetical character,


      
at least 1 numeric character,


      
at least 1 special character,

      - at least 8 characters.

4. Click **Save** .


Opcenter Intelligence 2401.0001 - User Manual 13


_Managing Licenses_


_Resetting the Password for the Desktop Explorer Role_

## 4 Managing Licenses


This page is only visible to users for which the licensing model available from version 3.2 is applied.


The page shows an up-to-date overview of the number of purchased and consumed seats for each user, as well as
the roles assigned to users. Seats correspond to the number of users that can access the application at the same
time, depending on the type of license that has been purchased. A seat is consumed for each logged-in user.


For more information on licenses, see _Opcenter Intelligence Installation Manual_ .

###### Accessing the page


To access the **License Management** page, click **License Management** on the Primary Navigation Bar.

###### Available Details

|Section|License Details|Description|
|---|---|---|
|**License Status**|**License Name**|Name of the license(s) currently in use.|
|**License Status**|**Purchased Seats**|Number of seats purchased for this license.|
|**License Status**|**Consumed Seats**|Number of seats currently consumed to<br>access the application.|
|**Users**|**User Name**|Name of the user who is using the licensing<br>model.|
|**Users**|**Consumed Licenses**|Name of the license model(s) that this user<br>has consumed.|
|**Users**|**Assigned Roles**|Name of the role(s) assigned to this user.|



14 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Solution_


_Creating a Solution_

## 5 How to Configure a Solution


A Solution is a container of objects that represent manufacturing intelligence business requirements. You can either
create a solution from scratch or import an already-existing solution.

###### Accessing the Page


To access the **Solutions** page, click the **Analytical Solutions** card in the **Home** page.

###### Workflow



1.

2.

3.

4.

5.

6.



Create a Solution

Create a Project
Configure the Time Definition
Configure a Scenario
Create an Environment

Deploy an Environment


###### Additional Operations

Export a Solution

### 5.1 Creating a Solution


A solution can be created by performing either of the following operations:








Creating a solution from scratch
Importing a solution created and exported using a previous version of the product


###### Creating a Solution From Scratch



1.

2.



In the **Solutions** page, click **Create Solution** .
Insert the following details:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-14-1.png)











Opcenter Intelligence 2401.0001 - User Manual 15


_How to Configure a Solution_


_Exporting a Solution_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-15-0.png)









3.



Click **Create** .


###### Importing an existing Solution

Follow this procedure to import a solution that has been created using a previous version of the product and
exported, or that has been duplicated using the export functionality.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-15-1.png)



2.

3.

4.


5.



Click **Choose File** and browse for the required .xml or .json file.
Select the file and click **Open** .
Insert a name for the solution in the **SOLUTION NAME** edit box.


Click the **Import** button. The new solution is displayed in the **Solutions** page.



**Import of Custom Entities**


If you are warned that the solution you are importing contains custom entities, you should verify that after the
migration they have been exposed correctly. In particular, you should check the data types to make sure that the
semantics has been properly formulated according to your requirements.




### 5.2 Exporting a Solution

Follow this procedure to export a solution. If you need to duplicate a specific solution, you can use this functionality
to export it and then import it again.

###### Procedure



1.

2.



In the **Solutions** page, select the solution you want to export and click **Export Solution** .
Click **OK** to confirm: you are prompted to save the .json file.





16 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Creating a Project_

## 6 How to Configure a Project


In this step you can create a project and select a number of functionalities, which are the first necessary items to
configure a data warehouse.

###### Prerequisites


You have created a solution.

###### Accessing the Page


To access the **Projects** page:



1.


2.

3.



Select a solution in the **Solutions** page.


Click **Open Solution** .
Click the **Projects** card.


###### Workflow



1.

2.

3.

4.

5.

6.

7.



Create a Project
(Optional) Edit a Project
Add a Site

Select Sources
(Optional) Configure Model Extensions
(Optional) Configure Entity Extensions
Plan a Schedule


###### Additional Operations

Display the Data Model

### 6.1 Creating a Project


In this step you can create a a self-consistent project whose execution results in information ingestion, that is the
process of obtaining and importing data for immediate use or storage in a database.

###### Procedure



1.

2.



In the **Projects** page, click **Create Project** .
Insert the following details:



Opcenter Intelligence 2401.0001 - User Manual 17


_How to Configure a Project_


_Editing a Project_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-17-0.png)











3.


4.


5.



In the pie menu on the left, select the slice that represents the required family. The pie will open to show more
category sub-fields. To display the parent slices again, click on the center of the pie menu.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-17-1.png)

Click **Create** .









Select one or more functionalities. You can select all the available functionalities or select a subset of them. In
the same project you cannot select functionalities belonging to different families (for example Generic MOM and
Process Industry), you can only add more functionalities for the same family after you have saved the project if
you did not select all the available ones.




### 6.2 Editing a Project

In this step you can add more functionalities if you have selected only a subset of them during the creation of the
project, but you cannot delete the functionalities you have already selected.


18 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Adding a Site_


###### Prerequisites

You have created a project.

###### Procedure



1.


2.


3.

4.


5.



In the **Projects** page, select a project.


Click **Open Project** .


Click **Edit Project** .
Modify the project details. You can add more functionalities for the same family if you did not select all the
available ones when you have created the project. You cannot select functionalities belonging to different
families (for example Generic MOM and Process Industry) in the same project.
Click **Save** .


### 6.3 Adding a Site

Opcenter Intelligence supports multi-site scenarios; a site might be a plant, department, or another physical or
logical point. In this step you must identify the sites where your working activity is carried out and choose a unique
identifier for each of them. In the following step you will then associate the sites with the data sources selected for
your project.




###### Prerequisites

You have created a project.

###### Procedure



1.


2.


3.



In the **Projects** page, select a project.


In the **Physical Sites** tab, click **Add Site** . The browser may ask you at this point the authorization to locate
your position. If you deny it, you can insert the address manually.
Insert the following details:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-18-3.png)

Opcenter Intelligence 2401.0001 - User Manual 19


_How to Configure a Project_


_Selecting Sources_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-19-0.png)









4.



Click **Save** .


### 6.4 Selecting Sources

In this step, you can select the entities that supply data. They may include Opcenter products, a data warehouse
(MDW) that has been generated by previous versions of the product or the data warehouse generated by Opcenter
Intelligence. Third-party systems, such as SQL Server or Oracle, can also be used as data sources.


20 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_


If you want to add a security encryption to enhance protection of your system, you should add a property after SQL
Server configuration. See the page on environment configuration for more details.

###### Prerequisites









Prerequisites may vary depending on the type of source database. For more details, see each source specific

page.
You must make sure that the selected source supports more than one site.


###### Procedure



1.


2.

3.



In the **Project** page, select the **Sources** tab.


Click **Create Source** .

Insert a name for the source. When you name an item, you must follow these rules:




    
The first letter of the name must be an uppercase, lowercase or numeric character.


    
For the remaining characters of the name, only alphanumeric characters, underscores and spaces should
be used.


    
Special characters (such as %, |, §, &, #, +, -, etc.) are not allowed.


    
The maximum length for names must not exceed 255 characters.
Select one or more **Physical Sites** for the source you are selecting.
In the pie menu, click on the required source family.
Select a product and a product version within the family.
Select the product functionalities in line with those you have already selected during the project creation.









      
      
4.

5.

6.

7.



8.



Click **Save** .


###### Opcenter Intelligence Sources

The following sources are available:











|Product Families|Products|Product Versions|
|---|---|---|
|**Opcenter EX**|Opcenter Execution Core (SQL Server)|•<br>•<br>8.0 to 8.6<br>8.7 or higher|
|**Opcenter EX**|Opcenter Execution Core (Oracle)|•<br>•<br>8.0 to 8.6<br>8.7 or higher|
|**Opcenter EX**|Opcenter Execution Discrete (SQL<br>Server)|•<br>•<br>•<br>•<br>•<br>3.0<br>3.1 - 3.2 - 3.3<br>4.0<br>4.1 - 4.2 - 4.3<br>4.4 or higher|
|**Opcenter EX**|Opcenter Execution Electronics (SQL<br>Server)|8.9 or higher|
|**Opcenter EX**|Opcenter Execution Process|•<br>•<br>3.0 to 3.3<br>4.0 or higher|


Opcenter Intelligence 2401.0001 - User Manual 21


_How to Configure a Project_


_Selecting Sources_













|Product Families|Products|Product Versions|
|---|---|---|
||Opcenter Execution Foundation OEE|2207 or higher|
||Opcenter Execution Pharma (Oracle)|2211 or higher|
|**Opcenter IN**|Intelligence Analytical Model|2.x - 3.x (MDW 2.0)|
|**Opcenter QL**|Opcenter Quality (SQL Server)|•<br>•<br>11.0 to 11.3<br>12.0|
|**Opcenter QL**|Opcenter Quality (Oracle)|•<br>•<br>11.0 to 11.3<br>12.0|
|**Opcenter IPL**|Opcenter Intra Plant Logistics (SQL<br>Server)|2210 or higher|
|**SIMATIC IT UA**|Discrete Manufacturing|•<br>•<br>1.0 - 1.1 - 1.2 - 1.3<br>2.3 - 2.4 - 2.5|
|**SIMATIC IT UA**|Process Industries|•<br>•<br>•<br>1.1 Update 1 - 1.2<br>2.3<br>2.4 - 2.5|
|**CEP**|Camstar Enterprise Platform Core (SQL<br>Server)|V7 SU4 - SU5 - SU6 - SU7 - SU8|
|**CEP**|Camstar Enterprise<br>Platform Core (Oracle)|V7 SU4 - SU5 - SU6 - SU7 - SU8|
|**QMS**|QMS Professional (SQL Server)|10.03 - 10.04 - 10.05 - 10.06 - 10.07|
|**QMS**|QMS Professional (Oracle)|10.03 - 10.04 - 10.05 - 10.06 - 10.07|
|**SIMATIC IT**|Line Monitoring System|•<br>•<br>2.2 SP1 HF1<br>2.3 - 2.4 - 2.5 - 2.6 - 2.7|
|**SIMATIC IT**|Production Suite|7.0 SPx - 7.1 - 7.2 - 8.0|
|**SIMATIC IT**|Historian|7.2|
|**SIMATIC IT**|Reporting Framework|MDW 1.0|


22 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_

|Products|Product Versions|
|---|---|
|Electronic Batch Recording (Oracle)|6.1.6|
|SQL Server|2012 or higher|
|Oracle|12c or higher|


#### 6.4.1 Opcenter Execution Core 8.0 to 8.6 SQL Server


The following functionalities are available for **Opcenter Execution Core (Opcenter EX CR) 8.0 to 8.6** as SQL
Server data source.


For more information on Opcenter Execution Core, see _Opcenter Execution Core Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities

The available functionalities for this source are the following:














Defect and Non Conformance

Downtime Management
Equipment Management
Labor Management
Location Management
Material Management
Production Execution

Quality APC


#### 6.4.2 Opcenter Execution Core 8.7 or higher SQL Server

The following functionalities are available for **Opcenter Execution Core (Opcenter EX CR) 8.7 or higher** as a SQL
Server data source.


For more information on Opcenter Execution Core, see _Opcenter Execution Core Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:







**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );



Opcenter Intelligence 2401.0001 - User Manual 23


_How to Configure a Project_


_Selecting Sources_







**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities




















Completed WIP
Container Management
Defect and Non Conformance

Device History
Downtime Management
Equipment Management
Equipment Performance
Labor Management
Location Management
Material Management
Operational Performance and Quality
Product and Material Traceability
Production Execution

Quality APC


#### 6.4.3 Opcenter Execution Core 8.0 to 8.6 Oracle

The following functionalities are available for **Opcenter Execution Core (Opcenter EX CR) 8.0 to 8.6** as an Oracle
data source.


Before you execute the deploy of a solution where the Opcenter Execution Core source has been selected, check
that the following requirements have been met:

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running.
The user who has been configured in Oracle for Windows Authentication must be the same user who owns the
rights to run Opcenter Intelligence service. For more information, see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected.


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;
GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;
GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;


24 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW

GRANT DROP ANY VIEW

GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities


The available functionalities for this source are the following:














Defect and Non Conformance

Downtime Management
Equipment Management
Labor Management
Location Management
Material Management
Production Execution

Quality APC


#### 6.4.4 Opcenter Execution Core 8.7 or higher Oracle

The following functionalities are available for **Opcenter Execution Core (Opcenter EX CR) 8.7 or higher** as Oracle
data source.


For more information on Opcenter Execution Core, see _Opcenter Execution Core Documentation_ .

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running.
The user who has been configured in Oracle for Windows Authentication must be the same user who owns the
rights to run Opcenter Intelligence service. For more information, see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected.


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;


Opcenter Intelligence 2401.0001 - User Manual 25


_How to Configure a Project_


_Selecting Sources_


GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;
GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW

GRANT DROP ANY VIEW

GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities


















Completed WIP
Container Management
Defect and Non Conformance

Downtime Management
Equipment Management
Equipment Performance
Labor Management
Location Management
Material Management
Operational Performance and Quality
Production Execution

Quality APC


#### 6.4.5 Opcenter Execution Discrete SQL Server

The following functionalities are available for these SQL Server data sources:











**Opcenter Execution Discrete (Opcenter EX DS) 3.0**
**Opcenter Execution Discrete (Opcenter EX DS) 3.1 - 3.2 - 3.3**
**Opcenter Execution Discrete (Opcenter EX DS) 4.0**
**Opcenter Execution Discrete (Opcenter EX DS) 4.1 - 4.2 - 4.3**
**Opcenter Execution Discrete (Opcenter EX DS) 4.4 or higher**





26 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-26-0.png)




###### Prerequisites

When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence Installation Manual_ );
**db_datareader** and **db_datawriter** Database roles for each source database you want to access and from
which you want to extract data.




###### Functionalities


















Certification Management ( _available starting from Opcenter EX DS 4.4_ )
Defect and Non Conformance

Equipment Management
Equipment Performance
Labor Management
Labor Performance

Location Management
Material Management
Production Definition

Production Execution

Production Scheduling
Quality APC


#### 6.4.6 Opcenter Execution Electronics 8.9 or higher SQL Server

The following functionalities are available for **Opcenter Execution Electronics (Opcenter EX EL) 8.9 or higher** as a
SQL Server data source.


For more information on Opcenter Execution Electronics, see _Opcenter Execution Electronics Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities







Completed WIP



Opcenter Intelligence 2401.0001 - User Manual 27


_How to Configure a Project_


_Selecting Sources_


















Container Management
Defect and Non Conformance

Downtime Management
Equipment Management
Equipment Performance
Labor Management
Location Management
Material Management
Operational Performance and Quality
Product and Material Traceability
Production Execution

Quality APC


#### 6.4.7 Opcenter Execution Process 3.x

The following functionalities are available for the **Opcenter Execution Process (Opcenter EX PR) 3.0 to 3.3** data

sources.


For more information on this product, see _Opcenter Execution Process Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.




##### Functionalities

The following functionalities are available for this source:












Equipment Management
Location Management
Material Management
Production Definition

Production Execution

Production Scheduling


#### 6.4.8 Opcenter Execution Process 4.0 or higher

The following functionalities are available for the **Opcenter Execution Process (Opcenter EX PR) 4.0 or higher**
data source.


For more information on this product, see _Opcenter Execution Process Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:


28 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_


**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-28-0.png)






###### Functionalities















Equipment Management
Labor Management
Location Management
Material Management
Production Definition

Production Execution

Production Scheduling
Sampling Management
Quality APC




#### 6.4.9 Opcenter Execution Foundation OEE

The following functionalities are available for **Opcenter Execution Foundation OEE 2207 or higher** .





For more information on this product, see _Opcenter Execution Foundation OEE documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence Installation Manual_ );
**db_datareader** and **db_datawriter** Database roles for each source database you want to access and from
which you want to extract data.


###### Functionalities

The available functionalities for this source are the following:


Opcenter Intelligence 2401.0001 - User Manual 29


_How to Configure a Project_


_Selecting Sources_











Context Management
Downtime Management
Equipment Capacity
Equipment Management
Equipment Performance


#### 6.4.10 Opcenter Execution Pharma Oracle

The following functionalities are available for **Opcenter Execution Pharma (Opcenter EX PH) 2211 or higher** as an
**Oracle** data source.


For information on the steps that involve operating directly on Opcenter EX PH, see _Opcenter Execution_
_Pharma documentation_ .


Before you execute the deploy of a solution where the Opcenter EX PH Oracle source has been selected, check that
the following requirements have been met.

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running, otherwise the error " _The OraOLEDB.Oracle provider is not registered on the local machine_ ” will be raised
during deploy.
(Only if Windows Authentication is used) The user who has been configured in Oracle for Windows
Authentication must be the same user who owns the rights to run Opcenter IN service (otherwise the error

"
_Login Failed_ " is raised). For more information, see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;
GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;
GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW


30 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_



GRANT DROP ANY VIEW

GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities












Equipment Management
Labor Management
Location Management
Material Management
Production Execution

Production Scheduling


#### 6.4.11 Intelligence Analytical Model

The following functionalities are available for **Intelligence Analytical Model 2.x - 3.x (MDW 2.0)** .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities





















Defect and Non Conformance

Downtime Management
Equipment Management
Equipment Performance
Labor Management
Labor Performance

Location Management
Maintenance Management
Material Management
Production Definition

Production Execution

Production Scheduling
Quality APC
Quality SPC
Tag Management


#### 6.4.12 Opcenter Quality SQL Server

The following functionalities are available for **Opcenter Quality (Opcenter QL) 11.0 to 11.3 - 12.0** as a **SQL Server**
data source.


For information on the steps that involve operating directly on Opcenter QL, see the _Opcenter_
_Quality documentation_ .

###### Prerequisites


Opcenter Intelligence 2401.0001 - User Manual 31


_How to Configure a Project_


_Selecting Sources_


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-31-0.png)




###### Functionalities

The available functionalities for this source are the following:











Defect and Non Conformance

Equipment Management
Labor Management
Material Management
Quality SPC


#### 6.4.13 Opcenter Quality Oracle

The following functionalities are available for **Opcenter Quality (Opcenter QL) 11.0 to 11.3 - 12.0** as an **Oracle**
data source.


For information on the steps that involve operating directly on Opcenter QL, see the _Opcenter Quality_
_documentation_ .


Before you execute the deploy of a solution where the Opcenter QL Oracle source has been selected, check that the
following requirements have been met.

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running.
The user who has been configured in Oracle for Windows Authentication must be the same user who owns the
rights to run Opcenter Intelligence service. For more information, see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected.


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;
GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;


32 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_


GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW

GRANT DROP ANY VIEW

GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities











Defect and Non Conformance

Equipment Management
Labor Management
Material Management
Quality SPC


#### 6.4.14 Opcenter Intra Plant Logistics SQL Server

The following functionalities are available for **Opcenter Intra Plant Logistics (Opcenter IPL) 2210 or higher** as a
SQL Server data source.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-32-0.png)





For information on the steps that involve operating directly on Opcenter IPL, see the _Opcenter Intra Plant Logistics_
_documentation_ .



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-32-1.png)




###### Prerequisites Prerequisites

When you create a SQL Server source, you must add a login with the following roles:


Opcenter Intelligence 2401.0001 - User Manual 33


_How to Configure a Project_


_Selecting Sources_









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities










Inventory Management
Labor Management
Material Consumption
Material Container History


###### Important recommendation on Material Consumption data load

It is strongly recommended that you do not load a high amount of data (6 months at the maximum is the
recommended amount) for the **MaterialConsumption** entity.



1.


2.

3.

4.

5.

6.



In Opcenter Intelligence Analytical Solution > Scenario > Data source server, select the data source database
and click **Open** .
In the **Scripts** page, click **Create Script** . See also Loading a Script.
Select the **Material Consumption** model.
Select the **MaterialConsumption** entity.
Select the **Delete Script** type.
Replace the default script with the following SQL Statement. This example shows how to delete 6 months of
data.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-33-0.png)


#### 6.4.15 SIMATIC IT Unified Architecture Discrete Manufacturing

The following functionalities are available for **SIMATIC IT Unified Architecture Discrete Manufacturing (SIMATIC**
**IT UADM) 1.0 - 1.1 - 1.2 - 1.3 - 2.3 - 2.4 - 2.5** .


For more information on this product, see _SIMATIC IT Unified Architecture Discrete Manufacturing Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence Installation Manual_ );
**db_datareader** and **db_datawriter** Database roles for each source database you want to access and from
which you want to extract data.



34 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_


###### Functionalities

The available functionalities for this source are the following:
















Defect and Non Conformance

Equipment Management
Labor Management
Labor Performance

Location Management
Material Management
Production Definition

Production Execution

Production Scheduling
Quality APC


#### 6.4.16 SIMATIC IT Unified Architecture Process Industries

The following functionalities are available for **SIMATIC IT Unified Architecture Process Industries (SIMATIC IT**
**UAPI) 1.1 Update 1 - 1.2 - 2.3 - 2.4 - 2.5** .


For more information on this product, see _SIMATIC IT Unified Architecture Process Industries Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities

The following functionalities are available for this source:












Equipment Management
Location Management
Material Management
Production Definition

Production Execution

Production Scheduling


#### 6.4.17 Camstar Enterprise Platform Core SQL Server

The following functionalities are available for **Camstar Enterprise Platform (CEP) Core V7 SU4-SU5-SU6-SU7-**
**SU8** as a **SQL Server** data source.


For more information on this product, see _Camstar Enterprise Platform Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:


Opcenter Intelligence 2401.0001 - User Manual 35


_How to Configure a Project_


_Selecting Sources_









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities

The available functionalities for this source are the following:














Defect and Non Conformance

Downtime Management
Equipment Management
Labor Management
Location Management
Material Management
Production Execution

Quality APC


#### 6.4.18 Camstar Enterprise Platform Core Oracle

The following functionalities are available for **Camstar Enterprise Platform (CEP) Core V7 SU4-SU5-SU6-SU7-SU8**
as an **Oracle** data source.


Before you execute the deploy of a solution where the Camstar Enterprise Platform Oracle source has been
selected, check that the following requirements have been met.

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running.
The user who has been configured in Oracle for Windows Authentication must be the same user who owns the
rights to run Opcenter Intelligence service. For more information, see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected.


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;
GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;
GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


36 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_



**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW

GRANT DROP ANY VIEW

GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities


The available functionalities for this source are the following:














Defect and Non Conformance

Downtime Management
Equipment Management
Labor Management
Location Management
Material Management
Production Execution

Quality APC


#### 6.4.19 QMS Professional SQL Server source

The following functionalities are available for **QMS Professional 10.03 - 10.04 - 10.05 - 10.06 - 10.07** as a **SQL**
**Server** data source.


For information on the steps that involve operating directly on QMS Professional, see the _QMS Professional CCM_
_(Concern and Complaint Management)_ and _SPC (Statistical Process Control)_ documentation.

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-36-0.png)




###### Functionalities

The available functionalities for this source are the following:










Defect and Non Conformance

Equipment Management
Labor Management
Material Management



Opcenter Intelligence 2401.0001 - User Manual 37


_How to Configure a Project_


_Selecting Sources_







Quality SPC


#### 6.4.20 QMS Professional Oracle source

The following functionalities are available for **QMS Professional 10.03 - 10.04 - 10.05 - 10.06 - 10.07** as an **Oracle**
data source.


For information on the steps that involve operating directly on QMS Professional, see the _QMS Professional CCM_
_(Concern and Complaint Management)_ and _SPC (Statistical Process Control)_ documentation.


Before you execute the deploy of a solution where the QMS Oracle source has been selected, check that the
following requirements have been met.

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running.
The user who has been configured in Oracle for Windows Authentication must be the same user who owns the
rights to run Opcenter Intelligence service. For more information, see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected.


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;
GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;
GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW

GRANT DROP ANY VIEW

GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities


38 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_











Defect and Non Conformance

Equipment Management
Labor Management
Material Management
Quality SPC


#### 6.4.21 SIMATIC IT Line Monitoring System

The following functionalities are available for **SIMATIC IT Line Monitoring System (SIMATIC IT LMS) 2.2 SP1 HF1 -**
**2.3 - 2.4 - 2.5 - 2.6 - 2.7** .


For more information on this product, see the _SIMATIC IT Line Monitoring System Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence Installation Manual_ );
**db_datareader** and **db_datawriter** Database roles for each source database you want to access and from
which you want to extract data.


###### Functionalities

The available functionalities for this source are the following:











Context Management
Downtime Management
Equipment Capacity
Equipment Management
Equipment Performance


#### 6.4.22 SIMATIC IT Production Suite

The following functionalities are available for **SIMATIC IT Production Suite (SIMATIC IT PRS) 7.0 SPx - 7.1 - 7.2 -**
**8.0** .


For more information on this product, see the _SIMATIC IT Production Suite Documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence Installation Manual_ );
**db_datareader** and **db_datawriter** Database roles for each source database you want to access and from
which you want to extract data.


###### Functionalities

The available functionalities for this source are the following:









Equipment Management
Labor Management
Location Management



Opcenter Intelligence 2401.0001 - User Manual 39


_How to Configure a Project_


_Selecting Sources_











Maintenance Management
Material Management
Production Definition

Production Execution

Production Scheduling


#### 6.4.23 SIMATIC IT Historian

The following functionalities are available for **SIMATIC IT Historian 7.2** .


For more information on this product, see _SIMATIC IT Historian documentation_ .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence Installation Manual_ );
**db_datareader** and **db_datawriter** Database roles for each source database you want to access and from
which you want to extract data.


###### Functionalities

The available functionality for this source is the following:







Tag Management


#### 6.4.24 SIMATIC IT Reporting Framework

The following functionalities are available for **SIMATIC IT Reporting Framework (Manufacturing Data Warehouse**
**1.0)** .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities

















Defect and Non Conformance

Downtime Management
Equipment Management
Equipment Performance
Labor Management
Labor Performance

Location Management
Maintenance Management
Material Management
Production Definition

Production Execution



40 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_









Production Scheduling
Quality APC
Quality SPC


#### 6.4.25 SIMATIC IT Electronic Batch Recording Oracle

The following functionalities are available for **SIMATIC IT Electronic Batch Recording (SIMATIC IT eBR) 6.1.6** as an
**Oracle** data source.


For information on the steps that involve operating directly on SIMATIC IT Electronic Batch Recording, see _SIMATIC_
_IT eBR documentation_ .


Before you execute the deploy of a solution where the SIMATIC IT eBR Oracle source has been selected, check that
the following requirements have been met.

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running, otherwise the error " _The OraOLEDB.Oracle provider is not registered on the local machine_ ” will be raised
during deploy.
The user who has been configured in Oracle for Windows Authentication must be the same user who owns the
rights to runOpcenter Intelligence service (otherwise the error " _Login Failed_ " is raised). For more information,
see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected.


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;
GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;
GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW

GRANT DROP ANY VIEW


Opcenter Intelligence 2401.0001 - User Manual 41


_How to Configure a Project_


_Selecting Sources_


GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities










Labor Management
Material Management
Production Execution

Production Scheduling


#### 6.4.26 Third-Party Systems SQL Server source

You can select third-party SQL Server database management system as a data source when you create a project.


Depending of the type of project, the available functionalities may vary. For example, if you have selected **Generic**
**MOM > Discrete** during the project creation, in the pie menu the **Defect and Non Conformance** functionality will be
present, while it will not be shown if the **Generic MOM > Process** slice has been chosen.


Before you execute the deploy of a solution where the third-party SQL Server source has been selected, take into
account that by default the deploy operation creates the database views in the source database. If you want to
avoid any overlap between Opcenter Intelligence database and the source database, you need to manually create a
new intermediate database and insert the name of this database in the **Databases** tab, under the column **Database**

**Name** .

###### Prerequisites


When you create a SQL Server source, you must add a login with the following roles:









**dbcreator** Server role in the SQL Server instance of the source database using the credentials of the **Domain**
**User** you inserted in the Opcenter Intelligence Configurator (Opcenter Intelligence Core section - for more
details, see _Opcenter Intelligence_ _Installation Manual_ );
**db_datareader** Database role for each source database you want to access and from which you want to extract
data.


###### Functionalities






















Defect and Non Conformance

Downtime Management
Equipment Capacity
Equipment Management
Equipment Performance
Labor Management
Labor Performance

Location Management
Maintenance Management
Material Management
Production Definition

Production Execution

Production Scheduling
Quality APC
Quality SPC
Tag Management



42 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Selecting Sources_

#### 6.4.27 Third-Party Systems Oracle source


You can select Oracle database management system as a data source when you create a project.


Depending of the type of project, the available functionalities may vary. For example, if you have selected **Generic**
**MOM > Discrete** during the project creation, in the pie menu the **Defect and Non Conformance** functionality will be
present, while it will not be shown if the **Generic MOM > Process** slice has been chosen.


Before you execute the deploy of a solution where the Oracle source has been selected, check that the following
requirements have been met.

###### Prerequisites











Oracle Data Provider for .NET (ODP.NET) must be installed on the same computer where Opcenter Intelligence is
running.
The user who has been configured in Oracle for Windows Authentication must be the same user who owns the
rights to run Opcenter Intelligence service. For more information, see _Opcenter Intelligence Installation Manual_ .
The **BM20LOAD**, **DELETEDBM20LOAD** and **BM20PRIVATE** users must have been created before you execute the
deploy of a solution where the Oracle source has been selected.


###### Role and Minimum Privileges for BM20LOAD users

The following role and system privileges are sufficient for the BM20LOAD user:


**Role**


CONNECT


**Privileges**


GRANT CREATE any type TO BM20LOAD;
GRANT CREATE type TO BM20LOAD;
GRANT DROP any type TO BM20LOAD;
GRANT ALTER any procedure TO BM20LOAD;
GRANT ALTER any type TO BM20LOAD;
GRANT CREATE procedure TO BM20LOAD;
GRANT CREATE any procedure TO BM20LOAD;

###### Role and Minimum Privileges for DELETEDBM20LOAD and BM20PRIVATE users


The following role and system privileges are sufficient for the DELETEDBM20LOAD and BM20PRIVATE users:


**Role**


CONNECT


**Privileges**


GRANT CREATE ANY VIEW

GRANT CREATE PROCEDURE

GRANT CREATE VIEW

GRANT DROP ANY VIEW

GRANT EXECUTE ANY PROCEDURE

GRANT SELECT ANY TABLE

###### Functionalities


The available functionalities for this source are the following:







Defect and Non Conformance



Opcenter Intelligence 2401.0001 - User Manual 43


_How to Configure a Project_


_How to Configure Model Extensions_





















Downtime Management
Equipment Capacity
Equipment Management
Equipment Performance
Labor Management
Labor Performance

Location Management
Maintenance Management
Material Management
Production Definition

Production Execution

Production Scheduling
Quality APC
Quality SPC
Tag Management


### 6.5 How to Configure Model Extensions

This optional step allows you to add new entities to the project, which can only be a subset of the entities managed
by the system. In this page you can add a new entity to those that already exist for the project to customize the
OOTB model. Every extension is specific to the project.

###### Workflow



1.

2.

3.

4.

5.

6.



Create a Model Extension

Select a Source for the Model Extension
(Optional) Delete a Model Extension
Load Custom Scripts
Deploy the Environment (for the first time or deploy the environment again)
Run a Flow








if the data warehouse is empty, run an initial flow to load custom entities;
if the data warehouse has already been populated (by means of an initial flow and possibly a number of
incremental flows) you can launch a Run Single Entity operation to retrieve the extension data.


#### 6.5.1 Creating a Model Extension

Follow this procedure to create a model extension.


If you create model extensions and then set a relationship between them and other extensions, when you want to
delete data please keep in mind these recommendations.

###### Procedure



1.


2.

3.



In the **Project** page, select the **Model Extensions** tab.


Click **Create Model Extension** .

Insert the following details:



44 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_How to Configure Model Extensions_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-44-0.png)















4.


5.


6.


7.



Select the **Granularity Type**, which provides the system with the information necessary to estimate space and
index requirements for the entity, together with the capacity to optimize the access to this entity. The three
following types of granularity have been defined:



Select the **Column Type**, which, depending on the entity type you have previously selected. It can be one of the
following:




    - **Small** : entities that typically amount to a few dozen/hundred records, such as classification, type or

state entities.

    - **Standard** : entities that amount to a few thousand records and that typically represent analysis contexts

such as equipment, material definition, labor, etc.


    
**Large** : entities that exceed hundreds of thousands or millions of records, typically entities that represent
facts.
Select the **Entity Type**, which can be one of the following:


    
**Analytical Context** : dimension tables, which contain descriptive attributes. Each dimension table has a
single field primary key (PK) which has a one-to-many relationship with a foreign key (FK) in the fact
table. As a consequence, dimensions can only contain textual data.


    
**Analytical Fact** : a fact table, which contains measurable, quantitative data about the business. The fact
table can only include numerical data and relationships with Analytical Context.


    
**Generic Entity** : entity type that is not strictly related to star schema modeling but that permits to model
entities that contain both numeric and textual information useful for the generation of reports. If you
select this entity type, you can add columns of any type, i.e. all the types available for Analytical Facts
and Analytical Context entity types and relationships with Analytical Context..
Insert the **Column Name** .





























Opcenter Intelligence 2401.0001 - User Manual 45


_How to Configure a Project_


_How to Configure Model Extensions_












|Entity Type|Column Type|Description|
|---|---|---|
|**Analytical Facts**and<br>**Generic Entity**|**Relationship**|To set a relationship with another entity.<br>If you have added a**Relationship** column to an<br>extension of analytical fact type, you can only set a<br>relationship with an analytical context. On the<br>contrary, if you have created an extension of<br>analytical context type, you cannot set any<br>relationship. If a**Relationship** column is added, the<br>name of the column always ends with the name of<br>the unique identifier of the target context (e.g. if the<br>target context is Equipment, the name always ends<br>with EquipmentId) and the name provided for the<br>user is used as a prefix.|
|**Analytical Facts**and<br>**Generic Entity**|**Quantity**|Numeric value (float) that can be aggregated by any<br>type of aggregation (for example by a sum, average,<br>min, max...) on the basis of a time dimension and of<br>any other type of dimension.|
|**Analytical Facts**and<br>**Generic Entity**|**Level Quantity**|•<br>•<br>Numeric value (float) that implicitly expresses the<br>Sum aggregation based on time from the moment 0<br>to NOW. Therefore it provides the total quantity<br>compared to the latest check.<br>The Sum aggregation can only be used for non-time<br>dimensions. All other aggregations can be<br>performed on the basis of all possible dimensions<br>(including time dimensions). For example, this value<br>can express the liters of liquid in a tank at a certain<br>moment.<br>**Example**<br>In a plant, two different tanks contain a liquid which<br>can be either added to the tank or removed from it.<br>_Tank 1_ contains**5** liters at 10 a.m. and<br>**7** liters at 11 a.m.<br>_Tank 2_ contains**8** liters at 10 a.m. and<br>**4** liters at 11 a.m.<br>If you add**5** to**7**, the result is not meaningful,<br>because you would aggregate the values by a sum<br>on the basis of a time dimension.<br>However, if you add**5** to**8**, you can obtain the<br>average number of liters available in the plant at 10<br>a.m., i.e. the aggregation is based on a non-time<br>dimension.|



46 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_How to Configure Model Extensions_









|Entity Type|Column Type|Description|
|---|---|---|
||**Unitary Quantity**|•<br>•<br>Numeric value (float). The two following types exist:<br>measures that express a value compared<br>to another unitary quantity (pieces per<br>second, Euros per piece, etc.)<br>measures that can never be added<br>together (for example temperature,<br>humidity, etc.)<br>These measures can never be aggregated by a sum,<br>neither for time dimensions nor for non-time<br>dimensions.<br>Other aggregation functions, such as Average, Min<br>and Max, can however be used for any type of<br>dimension (including time dimensions).<br>These types of quantity can be aggregated using a<br>Sum when they are multiplied by a numeric value<br>they have a relationship with.<br>**Example 1**<br>The unitary quantity "pieces per second" can be<br>aggregated for time and non-time dimensions after<br>you have multiplied it by the time required for the<br>analysis.<br>If a piece of equipment produces 5 items per second<br>and you multiply it by 10 seconds you obtain 50<br>pieces, which is a quantity value that can be used for<br>any type of dimension and aggregation.<br>**Example 2**<br>The temperature of two different equipment units<br>(ovens) is measured by means of two sensors. You<br>can calculate the Average, Min or Max temperature<br>at a specific time, but it would make no sense to add<br>the temperatures together.|
||**Duration**|Numeric value that contains information about the<br>duration.|
||**StartDateTime**|Starting date and time of an event. For this field the<br>UTC format must be applied. Local time columns will<br>be automatically added by the system for each UTC<br>time column.|
||**EndDateTime**|Ending date and time of an event. For this field the<br>UTC format must be applied. Local time columns will<br>be automatically added by the system for each UTC<br>time column.|


Opcenter Intelligence 2401.0001 - User Manual 47


_How to Configure a Project_


_How to Configure Model Extensions_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-47-0.png)




|Column Type|Description|
|---|---|
|**EventDateTime**|Precise date and time of an event. For this field the<br>UTC format must be applied. Local time columns will<br>be automatically added by the system for each UTC<br>time column.|
|**Name**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>255 characters in length. This field is always<br>mandatory ("not null").|
|**Description**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>1000 characters in length.|
|**Note**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>4000 characters in length.|
|**TextAttribute**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>255 characters in length.|



8.


9.



Click **Save** .


###### Deleting data when a relationship with other entities has been set

If you want to delete an extension and have previously set a relationship between this extension and other entities,
the deletion must be performed first for the entities that have a relationship with it and then for the entity itself.


**Example**


You have created a model extension for the "Manufacturer" entity and an entity extension for the "Equipment"
entity. You have then set a relationship in the "Equipment Extension" to the "Manufacturer".
If you want to delete the Manufacturer entity, you have to delete Equipment first, or remove the relationship
between Manufacturer and Equipment, and then delete Manufacturer, otherwise the deletion will fail.

#### 6.5.2 Selecting the Model Extension Source


Follow this procedure to select a model extension source.

###### Procedure



1.



In the **Model Extensions** tab, select a model extension for which you want to select a source.



48 Opcenter Intelligence 2401.0001 - User Manual


2.


3.

4.

5.



_How to Configure a Project_


_How to Configure Entity Extensions_


Click **Open** .


In the **Extension Sources** page, click **Create Extension Source** .
In the **Create Extension Source** panel, select one or more sources among those you have already created.
Click **Save** .


#### 6.5.3 Deleting a Model Extension

You can delete a model extension when it is no longer used in dashboards nor reports. Before you delete it, you can
choose whether you want to remove it permanently from the Manufacturing Data Warehouse or not. If you choose
the first option, at the next deploy of the environment the entity is physically deleted from the data warehouse and
views and stored procedures are removed from the data source contract.

###### Procedure



1.

2.


3.



In the **Model Extensions** tab, select a model extension and click **Delete Model Extension** .
In the **Delete Model Extension** panel, do either of the following:




    - leave the **Delete from Data Warehouse** check box selected if you want to remove the entity from the


MDW.

    - deselect the **Delete from Data Warehouse** check box if you only want to remove the the views from the

data source contracts.

Click **Delete** .










### 6.6 How to Configure Entity Extensions

In this step you can add a new column to those that already exist for the project entities. Every extension is specific
to the project.

###### Workflow



1.

2.

3.

4.

5.

6.



Create an Entity Extension
Select a Source for the Entity Extension
(Optional) Delete an Entity Extension
Load Custom Scripts
Deploy the Environment
Run a Flow








if the data warehouse is empty, run an initial flow to load custom entities;
if the data warehouse has already been populated (by means of an initial flow and possibly a number of
incremental flows) you can launch a Run Single Entity operation to retrieve the extension data.


#### 6.6.1 Creating an Entity Extension

Follow this procedure to create an Entity Extension.

###### Procedure



1.


2.

3.

4.

5.



In the **Project** page, select the **Entity Extensions** tab.


Click **Create Entity Extension** .
From the **Entity** drop-down list, choose an entity.
In the **Column Name** field, insert a name for the column.
Select the **Column Type** from the available list, whose elements depend on the characteristics of the entity you
have previously selected. Column types can be categorized as follows.



Opcenter Intelligence 2401.0001 - User Manual 49


_How to Configure a Project_


_How to Configure Entity Extensions_












|Entity Type|Column Type|Description|
|---|---|---|
|**Fact**and**Generic Entity**|**Relationship**|To set a relationship with another entity.<br>If you have added a**Relationship** column to an<br>extension of analytical fact type, you can only set a<br>relationship with an analytical context. On the<br>contrary, if you have created an extension of<br>analytical context type, you cannot set any<br>relationship. If a**Relationship** column is added, the<br>name of the column always ends with the name of the<br>unique identifier of the target context (e.g. if the target<br>context is Equipment, the name always ends with<br>EquipmentId) and the name provided for the user is<br>used as a prefix.|
|**Fact**and**Generic Entity**|**Quantity**|Numeric value (float) that can be aggregated by any<br>type of aggregation (for example by a sum, average,<br>min, max...) on the basis of a time dimension and of<br>any other type of dimension.|
|**Fact**and**Generic Entity**|**Level Quantity**|•<br>•<br>Numeric value (float) that implicitly expresses the<br>Sum aggregation based on time from the moment 0 to<br>NOW. Therefore it provides the total quantity<br>compared to the latest check.<br>The Sum aggregation can only be used for non-time<br>dimensions. All other aggregations can be performed<br>on the basis of all possible dimensions (including time<br>dimensions). For example, this value can express the<br>liters of liquid in a tank at a certain moment.<br>**Example**<br>In a plant, two different tanks contain a liquid which<br>can be either added to the tank or removed from it.<br>Tank 1 contains**5** liters at 10 a.m. and**7**<br>liters at 11 a.m.<br>Tank 2 contains**8** liters at 10 a.m. and**4**<br>liters at 11 a.m.<br>If you add**5** to**7**, the result is not meaningful, because<br>you would aggregate the values by a sum on the basis<br>of a time dimension.<br>However, if you add**5** to**8**, you can obtain the average<br>number of liters available in the plant at 10 a.m., i.e.<br>the aggregation is based on a non-time dimension.|



50 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_How to Configure Entity Extensions_









|Column Type|Description|
|---|---|
|**Unitary Quantity**|•<br>•<br>Numeric value (float). The two following types exist:<br>measures that express a value compared to<br>another unitary quantity (pieces per<br>second, Euros per piece, etc.)<br>measures that can never be added together<br>(for example temperature, humidity, etc.)<br>These measures can never be aggregated by a sum,<br>neither for time dimensions nor for non-time<br>dimensions.<br>Other aggregation functions, such as Average, Min and<br>Max, can however be used for any type of dimension<br>(including time dimensions).<br>These types of quantity can be aggregated using a<br>Sum when they are multiplied by a numeric value they<br>have a relationship with.<br>**Example 1**<br>The unitary quantity "pieces per second" can be<br>aggregated for time and non-time dimensions after<br>you have multiplied it by the time required for the<br>analysis.<br>If a piece of equipment produces 5 items per second<br>and you multiply it by 10 seconds you obtain 50<br>pieces, which is a quantity value that can be used for<br>any type of dimension and aggregation.<br>**Example 2**<br>The temperature of two different equipment units<br>(ovens) is measured by means of two sensors. You can<br>calculate the Average, Min or Max temperature at a<br>specific time, but it would make no sense to add the<br>temperatures together.|
|**Duration**|Numeric value that contains information about the<br>duration.|


Opcenter Intelligence 2401.0001 - User Manual 51


_How to Configure a Project_


_How to Configure Entity Extensions_











|Entity Type|Column Type|Description|
|---|---|---|
|**Context**and**Generic**<br>**Entity**|**Name**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>255 characters in length.<br>If you modify an entity extension that was<br>already deployed and on which data was<br>stored, you cannot use mandatory column<br>types such as**Name**, otherwise the next<br>deployment will fail because the system will<br>not automatically add a value for that<br>column. The recommended alternative is to<br>use the**TextAttribute**or**Note**column types.<br>|
|**Context**and**Generic**<br>**Entity**|**Description**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>1000 characters in length.|
|**Context**and**Generic**<br>**Entity**|**Note**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>4000 characters in length.|
|**Context**and**Generic**<br>**Entity**|**TextAttribute**|Field of "nvarchar" type that is used to create a<br>column in the data warehouse to manage specific<br>types of textual information. Identifies a property of<br>255 characters in length.|
|**Hybrid**|**StartDateTime**|Starting date and time of an event. For this field the<br>UTC format must be applied. Local time columns will<br>be automatically added by the system for each UTC<br>time column.|
|**Hybrid**|**EndDateTime**|Ending date and time of an event. For this field the<br>UTC format must be applied. Local time columns will<br>be automatically added by the system for each UTC<br>time column.|
|**Hybrid**|**EventDateTime**|Precise date and time of an event. For this field the<br>UTC format must be applied. Local time columns will<br>be automatically added by the system for each UTC<br>time column.|


52 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Planning a Schedule_



6.


7.


8.



Select the **Relationship** (only if the selected entity is a fact).


Click **Add Column** .


Click **Save** .



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-52-2.png)




#### 6.6.2 Selecting the Entity Extension Source

Follow this procedure to select the Entity Extension source.

###### Procedure



1.


2.


3.

4.

5.



In the **Entity Extensions** tab, select an entity extension for which you want to select a source.


Click **Open** .


In the **Extension Sources** page, click **Create Extension Source** .
In the **Create Extension Source** panel, select one or more sources among those you have already created.
Click **Save** .


#### 6.6.3 Deleting an Entity Extension

You can delete an entity extension when it is no longer used in dashboards nor reports. Before you delete it, you can
choose whether you want to remove it permanently from the Manufacturing Data Warehouse or not. If you choose
the first option, at the next deploy of the environment the entity is physically deleted from the data warehouse and
views and stored procedures are removed from the data source contract.

###### Procedure



1.

2.


3.



In the **Entity Extensions** tab, select an entity extension and click **Delete Entity Extension** .
In the **Delete Entity Extension** panel, do either of the following:




    - leave the **Delete from Data Warehouse** check box selected if you want to remove the entity from the


MDW.

    - deselect the **Delete from Data Warehouse** check box if you only want to remove the the views from the

data source contracts.

Click **Delete** .










### 6.7 Planning a Schedule

In this step you can generate one or more periodic schedules in order to run ETL incremental loads to keep the data
warehouse aligned with the sources. Subsequently, during the scenario configuration, you will be able to adapt the
template created in this step to the actual scheduling of your plant.

###### Procedure



1.


2.

3.



In the **Project** page, select the **Schedules** tab.


Click **Create Schedule** .

Insert a name for the schedule. When you name an item, you must follow these rules:







The first letter of the name must be an uppercase, lowercase or numeric character.



Opcenter Intelligence 2401.0001 - User Manual 53


_How to Configure a Project_


_Displaying the MDW Data Model_




    
For the remaining characters of the name, only alphanumeric characters, underscores and spaces should
be used.


    
Special characters (such as %, |, §, &, #, +, -, etc.) are not allowed.


    
The maximum length for names must not exceed 255 characters.
Select the **Project Source** from which data should be loaded.
In the **Frequency** area, select the frequency with which the ETL execution occurs:








      
      
4.

5. In the












|Options|Action|
|---|---|
|**Daily**|Insert the number of days in the**Recurs** every<br>box|
|**Weekly**|Insert the number of weeks in the**Recurs every**<br>box and select the day(s) of the week when the<br>ETL execution occurs|
|**Monthly**|•<br>•<br>•<br>•<br>•<br>Select the occurrence**Type**:<br>**Day**: insert a number from 1 to 31 in<br>the**Day** box and the frequency in the<br>**Recurs every** box.<br>**Custom**: select the following<br>options:<br>**First**, **Second**, **Third**, **Fourth**<br>or**Last**;<br>the corresponding day of the<br>week or weekday/weekend<br>day;<br>the frequency in the**Recurs**<br>**every** box.|



6.


7.



In the **Daily Frequency** area, from the **Frequency Mode** drop down box, select the occurrence frequency, which
can be either **Once At** or **Every** .
Depending on this selection, do one of the following:




      - set the occurrence time in the the number of **Hours** or **Minutes** in the **Occurs Every** fields

      - or set the occurrence time in the **Occurs Once At** field.
8. In the **Duration** area, set a **Start Date** and (optional) an **End Date** .
9. Click **Save** .

###### Result


A summary of your settings is shown when you select the saved schedule in the **Schedules** tab.

### 6.8 Displaying the MDW Data Model


In this page you can display a graphical visualization of the MDW data model as well as of any model extension or
entity extension you have created. The displayed entities depend on the functionalities and data source(s) you have
selected when you created the project.


A description of functionalities, models, entities and their attributes is available in _Opcenter Intelligence_ _Reference_
_Manual_ .

###### Prerequisites


54 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Project_


_Displaying the MDW Data Model_









You have created a project and selected a number of functionalities.
(Optional) You have created one or more data sources for the project.
(Optional) You have created model or entity extensions.


###### Procedure



1.

2.

3.


4.



In the **Data Model** tab, click to display the **Filters** panel.
Select a functionality: the list of associated models is displayed.
Select one or more models.



Click **Apply** .




###### Result

You can expand the single entities and display their attributes by clicking . You can also move the entities on the
page for a better visualization. If more than one model is selected, they are displayed using different colors.

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-54-2.png)

###### Other Available Operations



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-54-3.png)



Opcenter Intelligence 2401.0001 - User Manual 55


_How to Configure a Project_


_Displaying the MDW Data Model_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-55-0.png)



56 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure the Time Definition_


_Time Management in Smart Views_

## 7 How to Configure the Time Definition


In this step you can manage the time settings for your project, which means that you can decide how to aggregate
and display data based on time.


In the **Time Definitions** page, the Time Definitions are grouped according to the projects associated during their
creation.




###### Accessing the Page

To access the **Time Definition** page:



1.


2.

3.



Select a solution in the **Solutions** page.


Click **Open Solution** .
Click the **Time Definitions** card.


###### Workflow



1.

2.



Create a Time Definition

Create a Time Hierarchy


### 7.1 Time Management in Smart Views

###### How Time Definition is used in Data Storage and Smart Views

If you are going to configure a smart view, the time settings for the attributes will allow you to display a time for
each card and time hierarchies as subgroups. The attributes will include year, month, hour and minute, which
represent the possible clusters you can create and on which the data analysis can be based.


You will also be able to cluster data on the basis of a specific day, month, quarter and so on for all the years of the
database life. To this end, the fields of type **ofyear** are used, for example **monthofyearname** to analyze the plant
production in a particular month starting from the date of the database creation to the present day.


The system employs time and geographical information (provided during the site configuration) to identify the time
zone and daylight time saving to be adopted to reproduce the correct time context for the analysis phase.
Therefore, while information in the data warehouse bm20 schemas is stored in UTC format, the facts included in
smart views are transformed and contextualized on the basis of an analytical time concept linked to the perception
of a person working in a plant, regardless of where the plant is located.


This analytical time is fundamental in a comparative analysis, because it puts on the same level facts that have
taken place hours later or before the UTC due to different time zones, but from an analytical point of view generate
the same perception for the analyst or the plant manager.

###### Balancing Data Detail Level and Performance in Time Management for Smart Views


Time in smart views is managed as any other context: this means that fact tables, which natively contain
information on time (like in columns of type **StartDataTime**, **EndDateTime** and/or **EventDateTime** ), are
automatically linked to the time context.


Opcenter Intelligence 2401.0001 - User Manual 57


_How to Configure the Time Definition_


_Creating a Time Definition_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-57-0.png)









Even though the time context is totally comparable to other contexts, special attention should be paid to its
management, because linking an event to a specific point in time implies the creation of a table containing "all" the
points in time. As a consequence, the high granularity of this type of table would generate a huge table, which does
not make sense in a data mart and therefore in smart views.


Data granularity is a specific characteristic of the data warehouse that allows you to set various levels of detail for
units of data. Since granularity affects database performance, it is of paramount importance to reach a compromise
between level of detail and performance by discretizing data in order to balance the amount of records to be
processed and the storage space in use.
As a result, to guarantee an adequate performance for calculations, a common BI best practice consists in
discretizing time units to avoid an excessive amount of rows in the Time table of the data warehouse. This is the
reason why in smart views the information related to the time dimension is clustered in ten-minute intervals.
For example, if values are measured at 16.41, 16.42 and 16.43, they are clustered at 16.40, because they are included
in the 10-minute interval previous to their occurrence.

### 7.2 Creating a Time Definition


In this step you can manage the time settings for your project, which means that you can decide how to aggregate
and display data based on time.




###### Procedure



1.

2.



In the **Time Definitions** page, click **Create Time Definition** .
Insert the following details:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-57-3.png)



58 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure the Time Definition_


_Creating a Time Definition_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-58-0.png)



3.



Click **Save** .


###### Default Attributes for Time

When a Time Definition is created, the system generates additional columns that define standard attributes as well
as other attributes whose generation is based on the time definition configuration.
This table lists the default attributes:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-58-1.png)







Opcenter Intelligence 2401.0001 - User Manual 59


_How to Configure the Time Definition_


_Creating a Time Hierarchy_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-59-0.png)




### 7.3 Creating a Time Hierarchy

You can create time hierarchies to specify a calendar structure that defines how time periods are managed and
distributed in your site.

###### Procedure



1.


2.

3.



In the **Time Definitions** page, select the default time or another time definition and click **Open** .


Click **Create Time Hierarchy** .
Insert the following details:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-59-3.png)



60 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure the Time Definition_


_Creating a Time Hierarchy_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-60-0.png)











4.



Click **Save** .



Opcenter Intelligence 2401.0001 - User Manual 61


_How to Configure a Scenario_


_Creating a Scenario_

## 8 How to Configure a Scenario


In this step you can configure a scenario, which is an abstract representation of the physical distribution of servers,
services, databases and flows in a network.


You can either configure a custom scenario or you can generate a predefined scenario.


Configuring a scenario is also a prerequisite for deploying smart views.

###### Accessing the Page


To access the **Scenarios** page:



1.


2.

3.



Select a solution in the **Solutions** page.


Click **Open** .
Click the **Scenarios** card.


###### Prerequisites

You have configured a project.

###### Workflow



1.

2.

3.

4.

5.



Create or Generate a Scenario
Configure Servers
Add one or more Services
Configure Databases
Configure Flows


### 8.1 Creating a Scenario

You can either create a custom scenario or generate a predefined scenario.

###### Procedure



1.

2.



In the **Scenarios** page, click **Create Scenario** .
Insert the following details:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-61-2.png)









62 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Scenario_


_How to Configure a Server_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-62-0.png)











3.


4.


5.



From the **Project** drop-down list box, select the project you want to associate with the scenario you are
creating.
Leave the **Auto-generate** check box selected (default setting) to generate a predefined scenario, or deselect it
to create a custom scenario.

Click **Save** .


###### Result

If you have left the **Auto-generate** check box selected, the scenario that is generated will include the following
items:











A destination server of type SQL Server 2022-2019-2017-2016 Standard or Enterprise and a database of type

MDW 2.0.
A server for each project source. The server type, which contains a source database, is defined according to the
most recent version.
A flow from the source database to the destination database for each source of the project.


### 8.2 How to Configure a Server

In this step you can define the servers to be configured in the Solution.

###### Accessing the Page



1.


2.



In the **Scenarios** page, select a scenario.


Click **Open Scenario** : the list of servers for that scenario is displayed.


###### Prerequisite

You have configured a project.

###### Workflow



1.

2.



Create a Server

Add one or more Services


#### 8.2.1 Creating a Server

Follow this procedure to add a server to your scenario.

###### Procedure


Opcenter Intelligence 2401.0001 - User Manual 63


_How to Configure a Scenario_


_How to Configure a Server_



1.

2.


3.



Click **Create Server** .

Insert the following details:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-63-1.png)

Select the server **Type**, which can be one of the following:














      
      
      
4. Under



5.




    
**On-Premise SQL Server 2014 and 2012**


    
**On-Premise SQL Server 2019-2017-2016 Standard or Enterprise**

    - **Oracle**

Under **Installed Services**, select the **Databases** and/or **Flows** tile(s) if you want to add them to the server or,
alternatively, you can add these services after you have created the server.
Click **Save** .


#### 8.2.2 Adding Services to a Server

If you have not associated any Services (that is Databases and Flows) with a server during its creation, you can add
them in this step.

###### Procedure



1.


2.


3.

4.



In the **Servers** page, select a server.


Click **Open Server** .


Click **Edit Server** .

In the **Edit Server** panel, select one of the following or both to add them to the server:




      - **Databases** (the service that manages databases).

      - **Flows** (the service that manages flows).
5. Click **Save** .


64 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Scenario_


_How to Configure a Database_

### 8.3 How to Configure a Database


In this step you can configure the databases residing on the machines involved in the scenario (both DBs containing
source data and data warehouses to which data will be moved).


In the **Databases** page, the databases you have created are grouped according to the sources you have selected
during the project configuration. After you have created a database, you can load custom scripts to retrieve data
from the database.

###### Workflow



1.

2.

3.



Create a Database

Edit a Database
(Optional) Load a Custom Script


#### 8.3.1 Creating a Database

Follow this procedure to create a database.

###### Procedure



1.


2.

3.



In the **Servers** page, select a server and click **Open** .


Click **Create Database** .

In the **Create Database** panel, insert a name for the database. When you name an item, you must follow these
rules:









      
      
4.



5.




    
The first letter of the name must be an uppercase, lowercase or numeric character.


    
For the remaining characters of the name, only alphanumeric characters, underscores and spaces should
be used.


    
Special characters (such as %, |, §, &, #, +, -, etc.) are not allowed.


    
The maximum length for names must not exceed 255 characters.
Select a **Project** or **Project Source**, that is the project you have associated with the scenario during its creation
or one of the project sources. The items in this list are filtered by database type, so that server type and project
or project source type may match.
Click **Save** .


#### 8.3.2 Editing a Database

Follow this procedure to continue and complete the configuration of a database.


It is recommended that you set up a maintenance plan to manage the log file growth and fine-tune the data
warehouse configuration to provide the best performance.

##### Procedure



1.


2.

3.

4.


5.


6.



In the **Databases** tab, select a database.


Click **Edit Database** .

In the **Standard** tab, you can modify the database details.
In the **Advanced** tab, the available options vary according to the source you have selected during the creation of
the database.
(For the source database) Select the **Snapshot Enabled** check box if you want to enable the snapshot isolation
in SQL Server.
Select the **Smart Time Window Enabled** check box if you want to manage data that change rapidly (and
therefore also during ETL incremental execution) and that would be otherwise excluded from the data load.



Opcenter Intelligence 2401.0001 - User Manual 65


_How to Configure a Scenario_


_How to Configure a Database_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-65-0.png)







7.


8.



(For the destination database) Modify the following parameters or leave the default values.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-65-1.png)

Click **Save** .




#### 8.3.3 Loading a Script

When the solution is deployed, the system installs a set of objects contained in a contract layer on top of each
supported data source database or smart view involved in the solution in order to retrieve data to be loaded in the
Manufacturing Data Warehouse. These objects have been modeled according to a standard data storage pattern
which assumes that specific data has been saved in given tables within the databases. If, due to particular project
requirements, data has been stored in different tables, it is necessary to manually modify the relative objects in
order to correctly retrieve data in the MDW.


This can be done by either specifying a SELECT statement or by using a Stored Procedure.


You can load three types of scripts:









**Load Script** : to load data on the Manufacturing Data Warehouse.
**Delete Script** : to delete data from the Manufacturing Data Warehouse.
**Localize Script** : to load localized data.



If you have created extensions for your project, you need to load custom scripts to retrieve data from the database.





66 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Scenario_


_How to Configure a Database_


###### Recommendations

Before starting, please read a set of important recommendations.

###### Procedure



1.


2.

3.

4.

5.


6.


7.


8.

9.


10.


11.



In the **Databases** page, select a database and click **Open** .


In the **Custom Scripts** page, click **Create Script** .
In the **Models** drop-down list, select **Custom Model** .
In the **Model Entities** drop-down list, select one of the extensions you have previously configured.
From the **Entity Script Type** drop-down list box, select one of the following options depending on the fields
selected previously: **Load Script**, **Delete Script**, **Localize Script** . This procedure is valid for deleted and
localized scripts as well.
From the **Script Type** drop-down list box, select either **View** or **Stored Procedure** ( **View** is the default setting).
This box is enabled only for the extensions for which you have selected a **Large** granularity and only if an OOTB
script has not been provided.
In the **Entity Scripts** area, a script template is shown. Depending on the script type you have selected, you can
edit either the script or the stored procedure.
Add a **FROM** clause to specify the source database from where you want to retrieve data.
Add the mapping for the fields.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-66-2.png)

Click **Save** .


Click **Show Original** to view the original script below the one you are editing.








###### Editing scripts to retrieve context data for entities generated by a smart view

If you have added contexts to a smart view, you must edit the SQL script to retrieve their values in the MDW.



1.

2.


3.


4.



In the **Models** drop-down list, select the smart view for which you have added custom contexts.
In the **Model Entities** drop-down list, select one of the facts to which you have added custom contexts. Please
note that this list will include all the entities for that smart view, including those you have selected for contexts.
Edit the script according to your needs.


Click **Save** .



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-66-6.png)




###### Examples







Example of Custom Script for LMS source using the SELECT statement



Opcenter Intelligence 2401.0001 - User Manual 67


_How to Configure a Scenario_


_How to Configure a Database_








Example of Custom Script for Opcenter EX DS source using the SELECT statement
Example of Custom Script using a Stored Procedure


##### 8.3.3.1 Recommendations Before Getting Started

In this page you can find a set of basic recommendations to be read before you start loading scripts.

###### When a stored procedure should be used


Data load using a stored procedure is typically designed to execute paged data reading. It is recommended that you
use a stored procedure when the complexity of the load query is such that a view would not guarantee an adequate
performance, for example when you want to join multiple tables and/or temporary support tables are required.


In the script set in the stored procedure you must always sort by a unique field (source key), that is, never use the
date for ORDER BY because the date could change and therefore the sorting, so some data may not enter.

###### No fixed value in the past or equal to GetUtcDate for RowInserted and RowUpdated columns


The “RowInserted” and “RowUpdated” columns are used by ETLs to understand which data has been inserted or
modified starting from the last successful execution. If the RowUpdated column in particular has a fixed value in the
past or a value equal to the “GetUtcDate”, that data may never be loaded nor updated because the entity will
always be outside the ETL time window. This is why the real insertion and update dates of the data source must
always be retrieved to fill the RowInserted and RowUpdated columns. In particular, they need to be retrieved when
multiple joins between different entities are executed, as in that case all possible updates of all related entities have
to be considered.


Every time they are executed, ETLs define the time window to be considered at the beginning of the execution (T0,
T1) using T0 as the final date and time of the last time window completed successfully and T1 as “GetUtcDate”.


The example below shows what happens if the GetUtcDate is put in the RowUpdated column. As the two
“GetUtcDate” functions would be executed in different moments, the one inserted in the custom entity script would
always be after the one in the time window. As a consequence, data are never stored in the data warehouse or are
never updated.

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-67-0.png)

###### In the script only refer to data source entities


Custom entity scripts must not contain any reference to bm20Load entities, nor to any other structure created by in
the contract layer, but only refer to the entities of the current data source.


68 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Scenario_


_How to Configure a Database_

##### 8.3.3.2 Example of Custom Script Using the SELECT Statement (LMS source)


This example shows a custom entity script for the source LMS:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-68-0.png)


###### Important Recommendations











The FROM clause can be more complex (JOIN, GROUP etc.)
The first two columns represent the natural key. They must therefore be unique.
If the source is a product of the SIMATIC IT family, it is recommended that you use the [#SITMESDB#] [#PPADB#]

[#UAFDB#] tags instead of the real database names. If you use these tags, the system will apply the names used
in the environment.
If the source is a product of the Opcenter Execution Core family, it is recommended that you use the

[#CEPSCHEMA#] [#CEPDB#] tags instead of the real database names. If you use these tags, the system will apply
the names used in the environment.


##### 8.3.3.3 Example of Custom Script Using the SELECT Statement (Opcenter EX DS source)

This example shows a custom entity script for the source Opcenter EX DS:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-68-1.png)


###### Important Recommendations










The **RowInserted** and **RowUpdated** columns are mandatory, as the **Smart Time Window Enabled** check box
was selected by default in the **Edit Database** panel. If you do not include them in the script, the flows to load
data will not be completed correctly.
The FROM clause can be more complex (JOIN, GROUP etc.)
The first two columns represent the natural key. They must therefore be unique.



Opcenter Intelligence 2401.0001 - User Manual 69


_How to Configure a Scenario_


_How to Configure a Database_

##### 8.3.3.4 Example of Custom Script Using a Stored Procedure


This example shows a Stored Procedure written to read data in pages or windows.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-69-0.png)


###### Important Recommendations















If the **Smart Time Window Enabled** check box was selected when editing the database, the **RowInserted** and
**RowUpdated** columns are mandatory. If you do not include them in the script, the flows to load data will not be
completed correctly.
The WHERE condition must include a filter on the time interval using the **RowFrom** and **RowTo** parameters as
shown in the example.
The ORDER BY and OFFSET/FETCH instructions allow you to execute a paged load and must not be modified.
You must not modify the schema, the name or the parameters of the stored procedure.
The FROM clause can be more complex (JOIN, GROUP etc).
The first two columns represent the natural key. They must therefore be unique.
If the source is a product of the SIMATIC IT family, it is recommended that you use the [#SITMESDB#] [#PPADB#]

[#UAFDB#] tags instead of the real database names. If you use these tags, the system will apply the names used
in the environment.



70 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure a Scenario_


_How to Configure a Database_


 - If the source is a product of the Opcenter Execution Core family, it is recommended that you use the

[#CEPSCHEMA#] [#CEPDB#] tags instead of the real database names. If you use these tags, the system will apply
the names used in the environment.


Opcenter Intelligence 2401.0001 - User Manual 71


_How to Configure and Manage Flows_


_Creating a Flow_

## 9 How to Configure and Manage Flows


In the **Flows** pages, you can configure the flows involved in the scenario. You have to run an initial load when the
target database is empty, then, to keep the data warehouse aligned with the sources, you should schedule
periodical incremental loads to load all the changes which occur in the source database.

###### Accessing the Flows pages


Depending on the page from which you access flows, the operations you can perform on them vary. There are two
ways to access flows:








from within the **Scenarios** page, where you can perform all operations on flows, including creating new ones.
from the **Solutions** page, where you cannot create new flows but only run or edit existing flows.


###### From the Scenarios page



1.


2.

3.



Select a solution in the **Solutions** page.


Click **Open** **Solution** .
Click the **Flows** card.


###### From the Solutions page



1.

2.


3.


4.



Select a solution in the **Solutions** page and click **Open Solution** .
Click the **Scenarios** card.


Select the **Scenario** and click **Open Scenario** .


Click **Open Server** on the Flow Server.


###### Workflow



1.

2.

3.

4.



Create a Flow

Create a Flow Schedule

Edit a Flow

Run a Flow


### 9.1 Creating a Flow

Follow this procedure to create a flow.

###### Procedure



1.

2.



In the **Flows** page, click **Create Flow** .
Insert a name for the flow. When you name an item, you must follow these rules:




    
The first letter of the name must be an uppercase, lowercase or numeric character.


    
For the remaining characters of the name, only alphanumeric characters, underscores and spaces should
be used.


    
Special characters (such as %, |, §, &, #, +, -, etc.) are not allowed.


    
The maximum length for names must not exceed 255 characters.
From the **Project Flow** drop-down list, select one of the available sources among those you have created during
the project configuration. This list will only show the sources that have not been associated with a flow yet, as
they will disappear from the list once they have been used.









      
      
3.





72 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Manage Flows_


_Creating a Flow Schedule_



4.



Click **Save** .


### 9.2 Creating a Flow Schedule

A flow schedule is used to plan an incremental data load. If you have configured a schedule during the creation of
the project, a default flow schedule is created and displayed after you have created a flow.

###### Important Recommendation


It is strongly recommended that you avoid the overlap between data loads from any source to the data warehouse
or a smart view. To this purpose, it is advisable to distribute over time the start of each flow. The flows can be totally
or partially executed in parallel only if disk speed, RAM and CPU are sufficient to manage the requested operations,
including data reading from clients. To optimize your configurations, you should monitor the working environment
for a few weeks.


Example: if the flow duration is 3 minutes and you want to run 4 flows, schedule each flow every 16 minutes ( **Occurs**
**Every** parameter) and distribute the start time of each flow within the defined time interval in order to prevent
overlapping (e.g. at 00.00, 00.04, 00.08 and 00.12).

###### Procedure



1.


2.

3.



In the **Flows** page, click **Open Flow** .


Click **Create Flow Schedule** .

Insert a name for the Flow Schedule. When you name an item, you must follow these rules:









      
      
4. In the



5.

6.


7.

8.

9.




    
The first letter of the name must be an uppercase, lowercase or numeric character.


    
For the remaining characters of the name, only alphanumeric characters, underscores and spaces should
be used.


    
Special characters (such as %, |, §, &, #, +, -, etc.) are not allowed.


    
The maximum length for names must not exceed 255 characters.
In the **Frequency** area, select the frequency ( **Daily**, **Weekly**, **Monthly** ) with which the ETL execution occurs and
insert the number of days, weeks or months in the **Recurs Every** field.
In the **Daily Frequency** area, select the **Frequency Mode**, which can be either **Once At** or **Every** .
In the **Occurs Every** field, insert the number of hours or minutes and then set an interval, with the relative start
and end time.
In the **Duration** area, set a start date and (optional) an end date.
Click **Save** .
Deploy the Environment to physically enable the running of scheduled incremental flows.


###### Enabling or Disabling a Flow Schedule

To perform these operations, you must have deployed the environment at least once.



1.

2.



Select a flow schedule.
Do either of the following actions:









Click **Enable Flow Schedule** to enable in SQL Server the job corresponding to the selected flow
schedule.


Click **Disable Flow Schedule** to disable in SQL Server the job corresponding to the selected flow
schedule.


### 9.3 Editing a Flow

Follow this procedure to either edit a flow and/or to configure additional parameters.


Opcenter Intelligence 2401.0001 - User Manual 73


_How to Configure and Manage Flows_


_How to Run a Flow_

###### Procedure



1.


2.

3.

4.


5.



In the **Flows** page, select a flow.


Click **Edit Flow** .

In the **Standard** tab, you can modify the previously-inserted flow details.
In the **Advanced** tab, you can change the default values for the following parameters:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-73-0.png)

Click **Save** .









![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-73-1.png)




### 9.4 How to Run a Flow

In this step you can start the execution of the ETL package associated with a flow to either load initial data from the
source to the target database or to load incremental data to maintain databases aligned.

###### Prerequisites












When you run a flow, you must check that no other operation, such as a purge database or a deploy, is running
at the same time. If that is the case, wait for this operation to end before running the flow.
Before running a flow, you must have deployed the environment at least once.
It is recommended that you stop the source system before running an initial flow when you cannot determine
the adequacy of the system hardware to support the production activities generated by the flow.
If the selected source is SIMATIC IT UAPI or Opcenter Execution Process, only the following format is supported
for datetime fields: yyyy-mm-dd hh:mm:ss. Any other format will be discarded from the system. Non-standard
formats can, however, be loaded by overriding the contract layer.


###### Available Operations









Run an Initial Flow

Run an Incremental Flow

Run a Single Entity


#### 9.4.1 Running an Initial Flow

Follow this procedure to run an initial flow.

###### Important Recommendation


74 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Manage Flows_


_How to Run a Flow_


An initial load can only be executed when the target database is empty. To clean the target structure, it is suggested
that you use the purge data functionality. The purge operation must not however be executed when you are
upgrading from a previous version of the product.

###### Procedure



1.


2.

3.

4.

5.



In the **Flows** page, select the flow you want to run.


Click **Run Flow** .

In the **Execute Flow** page, select the environment where you want to execute the flow to load your data.
In the **Load Mode** drop-down list, select **Initial** .
Click the **Configuration Type Advanced** check box and select one of the following options:




      
**Rebuild Indexes after the flow has finished running**


      
**Enable Schedules after the flow has finished running**


      
**Execute Project Synchronization after the flow has finished running**

6. Select the **Start Mode**, which can be either of the following:











7.




    - **Autodetect** . If you select this option, the system considers as initial date the oldest date in the

production database.

    - **Manual** . If you select this option, you can set the loading time interval by browsing for the **Start Date**

**and Time** and **End Date and Time** in the available calendars.

Click **Start** to run the flow.


#### 9.4.2 Running an Incremental Flow

Follow this procedure to run an incremental flow.

###### Procedure



1.


2.

3.

4.

5.



In the **Flows** page, select the flow you want to run.


Click **Run Flow** .

In the **Execute Flow** page, select the environment where you want to execute the flow to load your data.
In the **Load Mode** drop-down list, select **Incremental** .
Click **Start** to run the flow.


#### 9.4.3 Running a Single Entity

Follow this procedure to run a single entity.

###### Procedure



1.


2.

3.

4.

5.

6.



In the **Flows** page, select a flow.


Click **Run Single Entity** .
In the **Run Single Entity** page, select the environment where you want the entity to be executed.
Specify a **Start Date** and an **End Date** to define the time interval for the data you want to load.
Select the entity for which you want to run the flow.
Click **Start** to run the flow.



Opcenter Intelligence 2401.0001 - User Manual 75


_How to Configure and Deploy an Environment_


_Creating an Environment_

## 10 How to Configure and Deploy an Environment


Opcenter Intelligence employs the environment to implement the concrete realization of the abstract configuration
of the scenario you have performed until now.


In this step you can map all the items included in the scenario on real items that exist in a physical environment.

###### Accessing the Page


To access the **Environments** page:



1.


2.

3.



Select a solution in the **Solutions** page.


Click **Open Solution** .
Click the **Environments** card.


###### Workflow



1.

2.

3.



Create an Environment

Edit an Environment

Deploy an Environment


###### Additional Operations








Undeploy an Environment
Purge the Manufacturing Data Warehouse


### 10.1 Creating an Environment

Follow this procedure to create an environment.


When you create the environment, you can configure the year starting from which the "Time" table of the MDW is
populated during the environment deploy. The end of the following year is assumed as ending point and the
daylight time saving table is populated as well.


This field must be configured according to the age of data in the source database. When the environment is
deployed, time is generated automatically based on the selected year. Subsequently, the future time is managed by
a scheduler that each month creates the missing rows for the corresponding month of the following year (for
example, in November 2020 the rows until November 2021 are generated).


This settings makes an impact on smart view entities, which are generated starting from the information contained
in this MDW table.

###### Procedure



1.

2.

3.


4.

5.



In the **Environments** page, click **Create Environment** .
Insert a name and a description (optional) for the environment.
In the **Generate Time From** drop-down list, select the year starting from which the Time table in the MDW will
be populated during the deploy operation. The default value is the previous year. This value can always be
changed by editing the environment.
Select the scenario with which you want to associate the new environment.
Click **Save** .


### 10.2 Editing an Environment

Follow this procedure to edit the environment and complete its configuration.


76 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Editing an Environment_


On this page you may also want to rebuild the database indexes to remove fragmentation, reclaim disk space and
reorder index rows.

###### Procedure



1.

2.


3.


4.


5.


6.

7.



In the **Environments** page, select the environment and click **Edit Environment** .
In the **Edit Environment** panel, in the **Generate Time From** drop-down list, you can select the year from which
the Time table in the MDW will be populated during the deploy operation.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-76-0.png)

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-76-1.png)

In the **Properties** tab, insert the correct parameters depending on your scenario configuration.
Click **Save** .







In the **Servers** tab, type the name or the IP address of the corresponding physical machine for each server
contained in the solution. This is the real instance of the server(s).
In the **Services** tab, type for each server the instance name of the required Microsoft Services for each item of
the column **Object Name** . This field can be empty in the case of a default instance, or can be the name of the
SQL Server instance. This instance name is the same for databases and flows.
In the **Databases** tab, for each database listed under the column **Database Name**, type the real name of the
physical database to be created or used during the deploy.








###### Rebuilding Database Indexes



1.


2.

3.



In the **Environments** page, select an environment.


Click **Rebuild Indexes** .

Click **Rebuild Indexes** .


#### 10.2.1 Configuring the Properties tab

The parameters to be inserted in the **Properties** tab may vary depending on the data sources you have selected and
your scenario configuration.





The following links contain the list of properties available for the corresponding sources:








Opcenter Execution Discrete (Opcenter EX DS) SQL Server
Opcenter Execution Process (Opcenter EX PR)



Opcenter Intelligence 2401.0001 - User Manual 77


_How to Configure and Deploy an Environment_


_Editing an Environment_



























Opcenter Execution Foundation OEE (Opcenter EX FN OEE)
Opcenter Execution Core (Opcenter EX CR) SQL Server
Opcenter Execution Core (Opcenter EX CR) Oracle
Opcenter Execution Electronics (Opcenter EX EL) SQL Server
Opcenter Execution Pharma (Opcenter EX PH) Oracle
Opcenter Quality (Opcenter QL) SQL Server
Opcenter Quality (Opcenter QL) Oracle
Opcenter Intra Plant Logistics (Opcenter IPL) SQL Server
SIMATIC IT Unified Architecture Discrete Manufacturing (UADM)
SIMATIC IT Unified Architecture Process Industries (UAPI)
Camstar Enterprise Platform (CEP) SQL Server
Camstar Enterprise Platform (CEP) Oracle
QMS Professional SQL Server
QMS Professional Oracle
SIMATIC IT eBR Oracle

SIMATIC IT Production Suite (PRS)
SIMATIC IT Historian
SIMATIC IT Line Monitoring System (LMS)
SIMATIC IT Manufacturing Data Warehouse (MDW)
Third-Party Systems SQL Server
Third-Party Systems Oracle


##### 10.2.1.1 Opcenter Execution Discrete SQL Server

The following properties must be configured for these SQL Server data sources:










Opcenter Execution Discrete (Opcenter EX DS) 3.0 - 3.1 - 3.2 - 3.3
Opcenter Execution Discrete (Opcenter EX DS) 4.0
Opcenter Execution Discrete (Opcenter EX DS) 4.1 - 4.2 - 4.3
Opcenter Execution Discrete (Opcenter EX DS) 4.4 or higher



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-77-0.png)





78 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Editing an Environment_


##### 10.2.1.2 Opcenter Execution Process

The following properties must be configured for the data sources:








Opcenter Execution Process (Opcenter EX PR) 3.0 to 3.3
Opcenter Execution Process (Opcenter EX PR) 4.0 or higher



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-78-0.png)


##### 10.2.1.3 Opcenter Execution Foundation OEE

The following properties must be configured for the Opcenter Execution Foundation OEE 2207 or higher.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-78-1.png)


##### 10.2.1.4 Opcenter Execution Core SQL Server

The following properties must be configured for the data sources:








Opcenter Execution Core (Opcenter EX CR) 8.0 to 8.6 SQL Server
Opcenter Execution Core (Opcenter EX CR) 8.7 or higher SQL Server



Opcenter Intelligence 2401.0001 - User Manual 79


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-79-0.png)


##### 10.2.1.5 Opcenter Execution Core Oracle

The following properties must be configured for the data sources:








Opcenter Execution Core (Opcenter EX CR) 8.0 to 8.6 Oracle
Opcenter Execution Core (Opcenter EX CR) 8.7 or higher Oracle



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-79-1.png)



80 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-80-0.png)




##### 10.2.1.6 Opcenter Execution Electronics SQL Server

The following properties must be configured for the Opcenter Execution Electronics 8.9 or higher SQL Server data

source:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-80-1.png)


##### 10.2.1.7 Opcenter Execution Pharma Oracle

The following properties must be configured for the data source Opcenter Execution Pharma (Opcenter EX PH) 2211
or higher Oracle:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-80-2.png)



Opcenter Intelligence 2401.0001 - User Manual 81


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-81-0.png)



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-81-1.png)




##### 10.2.1.8 Opcenter Quality SQL Server

The following properties should be configured for the data source Opcenter Quality (Opcenter QL) 11.0 to 11.3 - 12.0
SQL Server:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-81-2.png)


##### 10.2.1.9 Opcenter Quality Oracle

The following properties should be configured for the data source Opcenter Quality (Opcenter QL) 11.0 to 11.3 - 12.0
Oracle:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-81-3.png)



82 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-82-0.png)





![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-82-1.png)




##### 10.2.1.10 Opcenter Intra Plant Logistics SQL Server

The following properties must be configured for the Opcenter Intra Plant Logistics (Opcenter IPL) 2210 or higher
SQL Server data source:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-82-2.png)





Opcenter Intelligence 2401.0001 - User Manual 83


_How to Configure and Deploy an Environment_


_Editing an Environment_

##### 10.2.1.11 SIMATIC IT Unified Architecture Discrete Manufacturing


The following properties must be configured for the data source SIMATIC IT Unified Architecture Discrete
Manufacturing 1.0 - 1.1 - 1.2 - 1.3 - 2.3 - 2.4 - 2.5:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-83-0.png)
##### 10.2.1.12 SIMATIC IT Unified Architecture Process Industries

The following properties must be configured for the data source SIMATIC IT Unified Architecture Process Industries
1.1 Update 1 - 1.2 - 2.3 - 2.4 - 2.5:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-83-1.png)


##### 10.2.1.13 Camstar Enterprise Platform SQL Server

The following properties must be configured for the data source Camstar Enterprise Platform (CEP) V7 SU4-SU5SU6-SU7-SU8 SQL Server:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-83-2.png)





84 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-84-0.png)




##### 10.2.1.14 Camstar Enterprise Platform Oracle

The following properties must be configured for the data source Camstar Enterprise Platform (CEP) V7 SU4-SU5SU6-SU7-SU8 Oracle:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-84-1.png)



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-84-2.png)





Opcenter Intelligence 2401.0001 - User Manual 85


_How to Configure and Deploy an Environment_


_Editing an Environment_

##### 10.2.1.15 QMS Professional SQL Server


The following properties must be configured for the data source QMS Professional 10.03 - 10.04 - 10.05 - 10.06 SQL
Server:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-85-0.png)


##### 10.2.1.16 QMS Professional Oracle

The following properties must be configured for the data source QMS Professional 10.03 - 10.04 - 10.05 - 10.06
Oracle:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-85-1.png)







86 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-86-0.png)




##### 10.2.1.17 SIMATIC IT eBR Oracle

The following properties must be configured for the data source SIMATIC IT eBR 6.1.6 Oracle:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-86-1.png)



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-86-2.png)




##### 10.2.1.18 SIMATIC IT Production Suite

The following properties must be configured for the data source SIMATIC IT Production Suite 7.0 SPx - 7.1 - 7.2 - 8.0:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-86-3.png)





Opcenter Intelligence 2401.0001 - User Manual 87


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-87-0.png)
##### 10.2.1.19 SIMATIC IT Historian

The following properties must be configured for the data source SIMATIC IT Historian 7.2:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-87-1.png)
##### 10.2.1.20 SIMATIC IT Line Monitoring System

The following properties must be configured for the SIMATIC IT Line Monitoring System 2.2 SP1 HF1 - 2.3 - 2.4 - 2.5 2.6 - 2.7 data source.


88 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Editing an Environment_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-88-0.png)


##### 10.2.1.21 SIMATIC IT Manufacturing Data Warehouse

The following properties must be configured for the data source SIMATIC IT Manufacturing Data Warehouse 1.0 2.0:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-88-1.png)



Opcenter Intelligence 2401.0001 - User Manual 89


_How to Configure and Deploy an Environment_


_Deploying an Environment_

##### 10.2.1.22 Third-Party Systems SQL Server


The following properties must be configured for the data source Third-Party Systems SQL Server:

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-89-0.png)

##### 10.2.1.23 Third-Party Systems Oracle


The following properties must be configured for the data source Third-Party Systems Oracle:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-89-1.png)



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-89-2.png)




### 10.3 Deploying an Environment

Follow this procedure to deploy an environment. You can also undo the deploy operation, for example before
deleting a solution. The progress of this operation can be tracked on the **Monitoring Messages** page.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-89-3.png)





90 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure and Deploy an Environment_


_Undeploying an Environment_

###### Procedure



1.


2.



In the **Environments** page, select the environment.


Click **Deploy Environment** .


### 10.4 Undeploying an Environment

This operation allows you to undo the deploy, for example before deleting a solution. The progress of this operation
can be tracked on the **Monitoring Messages** page.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-90-1.png)




##### Procedure



1.


2.



In the **Environments** page, select an environment.


Click **Undeploy Environment** . All the items and associations created during the previous deploy operation
are removed.


### 10.5 Purging the Manufacturing Data Warehouse

This operation allows you to delete all or part of the data in the MDW. The progress of this operation can be tracked
on the **Monitoring Messages** page.

###### Target Users


The command is enabled only if the current user has the **Solution Engineer** role.

###### Prerequisites


You have executed a deploy of the environment.

###### Important Recommendations









When you launch a purge operation, you must check that no other operation, such as a deploy or an initial or
incremental flow, is running at the same time. If that is the case, wait for this operation to end before starting
the purge.
If you have scheduled any incremental flows, it it strongly recommended that you disable them before
launching the purge, because their execution might overlap.


###### Procedure



1.


2.

3.



In the **Environments** page, select an environment.


Click **Purge Database** .
In the **Purge Database** panel, select:







the site for which you want to clean data

or



Opcenter Intelligence 2401.0001 - User Manual 91


_How to Configure and Deploy an Environment_


_Purging the Manufacturing Data Warehouse_


      - **All Sites**

4. Click **Start** .


92 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure Smart Views_


_Opcenter Intelligence Smart View Data_

## 11 How to Configure Smart Views


A Smart View is the representation of manufacturing entities, ideas and events, along with their properties and
relations, according to a system of categories. By configuring a smart view, you can choose how to visualize the
information contained in the data warehouse. To this end, you can create more than one smart view.


The size of each smart view depends on the selected measures and attributes as well as on the size of the selected
entities in terms of disk space and computational effort.


In the **Smart Views** page, the Smart Views are grouped according to the projects associated during their creation.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-92-0.png)








##### Target Users



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-92-1.png)




###### Accessing the Page

To access the **Smart Views** page:



1.


2.

3.



Select a solution in the **Solutions** page.


Click **Open Solution** .
Click the **Smart Views** card.


###### Workflow



1.

2.

3.

4.

5.

6.

7.

8.



Perform preliminary operations
Create a Smart View

Select Measures

Select Attributes

Deploy a Smart View
(Optional) Undeploy a Smart View
Run a Smart View
Perform additional operations


### 11.1 Opcenter Intelligence Smart View Data

When you select measures and attributes in the cards of a smart view, you are choosing the information on the
basis of which you want to aggregate, filter or group data for analysis in dashboards.


When the Smart View is deployed, one or more data marts are created, which are made up of related fact tables
(measures) and dimensions/contexts (attributes). A fact table is created for each card where measures have been
selected and dimensions are created for each selected attribute card.


Opcenter Intelligence 2401.0001 - User Manual 93


_How to Configure Smart Views_


_Preliminary Operations_


The available fact tables and dimensions depend on functionalities, on available sources and on the selected
measures/attributes. Some of the displayed measures and attributes are provided out of the box, while other
depend on the data warehouse content and are loaded during a project synchronization.

###### Measures and Attributes Distribution in Cards


While measures are distributed in cards according to data warehouse entities, attributes are further subdivided
depending on the data warehouse table they belong to. The following attribute types can be present in the
corresponding cards:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-93-0.png)
### 11.2 Preliminary Operations

Before creating a smart view, the following preliminary operations are available:








Synchronize the project or Clean the project
(Optional) Merge measures and attributes


#### 11.2.1 Synchronizing the Project

The synchronization updates the metadata necessary to include in the smart view the information provided by
functionalities and the data sources that you have selected during the project configuration. In short, the project
synchronization will transform the data of the manufacturing data warehouse into measures and attributes.

###### Prerequisites


You have created and configured:









a project
a scenario

an environment



You have performed:


94 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure Smart Views_


_Preliminary Operations_








a deploy of the environment
an initial flow to load data


###### Limitations

When you synchronize the project, for the entities with a hierarchy (like for example Equipment,

→
OperationExecution, OperationResponse etc.) the hierarchy might generate a loop (for example, Equipment1
Equipment2 → Equipment1). In that case, in the **Attributes** cards of the smart view the levels cannot be selected
for that entity.

###### Procedure



1.

2.

3.

4.



In the **Smart Views** page, click **Synchronize Project** .
In the **Projects** drop-down, select a project.
In the **Environment** drop-down, select an environment.
Click **Synchronize** .


#### 11.2.2 Cleaning the Project

The cleaning operation is the opposite of synchronization, which generates measures and attributes on the basis of
MDW data (bm20 schema). The cleaning operation must be executed when the MDW content has been totally
modified, for example after a purge or an undeploy operation.

###### Important Recommendation


If you have already created one or more smart views (of any type), the cleaning operation cannot be executed,
because it might delete the measures and attributes selected for the smart view(s).

###### Prerequisites


You have created a project.

###### Procedure



1.

2.

3.



In the **Smart Views** page, click **Clean Project** .
Select the project.
Click **Clean Project** .


#### 11.2.3 Merging Measures and Attributes

Measures and attributes can be aggregated by means of the merge operation. This operation is a sort of "cleaning"
action, and is useful when, for example, the same information has been expressed with different names or when
similar items need to be clustered, for example classes. You can merge more than one item.


The system performs a check on the validity of the merge and informs the user whether the operation is possible or
not: for example when measures are included in tables with different analysis contexts and cannot therefore be
stacked.







Opcenter Intelligence 2401.0001 - User Manual 95


_How to Configure Smart Views_


_Creating a Smart View_

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-95-0.png)

###### Procedure



1.


2.

3.


4.

5.


6.


7.



In the **Smart View** page, click the **Merge** button: from the drop-down menu, select either **Merge Attributes**
or **Merge Measures** .
Select a functionality from the list on the left pane.
In the cards that are displayed, select two or more measures or attributes you want to merge.


Click **Merge** .
In the **Merge Attributes** or **Merge Measures** pane, insert a name for the new merged item and click **Merge** . A
new clustered item is shown under the **Custom** section for measures and **Standard** section for attributes.


To view the list of measures contained in the merged item, hover the mouse on the button near the item


name and click the check mark that appears on the left, then click the **Info** button on the toolbar.


To split the item into the original measures, click **Split** .


### 11.3 Creating a Smart View

###### Prerequisites







You have created and configured:




     
a project


     
a scenario including a flow

     - an environment


You have performed (strongly recommended):








an initial flow to load data

a project synchronization


###### Procedure



1.

2.



In the **Smart View** page, click **Create Smart View** .
Insert a meaningful name for the smart view. When you name an item, you must follow these rules:




    
The first letter of the name must be an uppercase, lowercase or numeric character.


    
For the remaining characters of the name, only alphanumeric characters, underscores and spaces should
be used.


    
Special characters (such as %, |, §, &, #, +, -, etc.) are not allowed.


    
The maximum length for names must not exceed 255 characters.
In the **Projects** drop-down list box, select a project.
Select a **Type**, which can be either of the following:









      
      
3. In the

4.









**Physical** : data warehouse tables are physically created in columnstore mode and the schema has the
same name as the view.
**Virtual** : information is managed by creating SQL views on top of the data warehouse.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-95-3.png)





96 Opcenter Intelligence 2401.0001 - User Manual


5.


6.



_How to Configure Smart Views_


_Selecting Measures_


If you have selected the **Physical** type, you can select the **Schedule**, which can be **Every 2, 5, 10, 30** or **60**
**minutes** depending on how frequently you want to update the database tables created by the smart view. A
flow schedule associated with the smart view is automatically created when you save the smart view.
Click **Save** . The **Deploy Info** on the smart view tile after it has been created is **NotDeployed** .


### 11.4 Selecting Measures

###### Prerequisites

You have created a smart view.

###### Limitations


If different measures have names that differ from each other only by a space, the deploy of the smart view fails
because their names must be unique within a query batch or stored procedure.
Example:
**Actual Quantity EquipmentPropertyStaticValue**
**ActualQuantity EquipmentPropertyStaticValue**
As a workaround, you can rename the measures by editing them in the smart view page.

###### Procedure



1.

2.


3.


4.

5.



In the **Smart View** page, select a smart view and click **Open Smart View** .
In the **Measures** tab a set of predefined cards is displayed according to the functionalities and the data sources
you have selected during the project configuration. Measures are also acquired (and the cards are therefore
populated) during the project synchronization.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-96-2.png)

Click **Save Measures** : the **Save operation in progress** status is shown on the smart view tile.
Wait until the **Available** status appears on the smart view tile to proceed with any other operation on the smart
view.





Select the measures you want to analyze. Depending on this choice, the attributes cards you can select will vary
accordingly. You can select a maximum number of 200 measures. A block will be issued if their number exceeds
this limit.







![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-96-4.png)




### 11.5 Selecting Attributes

###### Prerequisites








You have created a smart view.

You have selected and saved at least one measure.



Opcenter Intelligence 2401.0001 - User Manual 97


_How to Configure Smart Views_


_Deploying a Smart View_







You have checked that the measures you selected have been saved correctly, that is when the **Smart view**
**available** message is displayed on the smart view tile.


###### Limitations

If different attributes have names that differ from each other only by a space, the deploy of the smart view fails
because their names must be unique within a query batch or stored procedure.
Example:
**Actual Quantity EquipmentPropertyStaticValue**
**ActualQuantity EquipmentPropertyStaticValue**
As a workaround, you can rename the attributes by editing them in the smart view page.

###### Procedure



1.

2.


3.


4.

5.



In the **Smart View** page, select a smart view and click **Open Smart View** .
Click the **Attributes** tab. A set of predefined cards is displayed according to the measures you have selected in
the **Measures** page. Attribute cards are updated when a data load is performed. Depending on the data
warehouse table they belong to, attributes can be of the following types:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-97-1.png)

Select the attributes you want to analyze. You can select a maximum number of 200 attributes. A block will be
issued if their number exceeds this limit.


Click **Save Attributes** : the **Save operation in progress** status is shown on the smart view tile.
Wait until the **Available** status is displayed to proceed with any other operation on the smart view.




### 11.6 Deploying a Smart View

A deploy is required after you have performed one of the following operations on measures / attributes and, in
some cases, contexts:











Select

Clear

Rename

Merge
Split



98 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure Smart Views_


_Undeploying a Smart View_


The progress of this operation is tracked on the **Monitoring Messages** page.

###### Smart View Deploy Status


The deploy status of a smart view is shown on each smart view tile, followed by the name of the environment
selected when the deploy operation has been started. The possible statuses can be **NotDeployed**, **Deploying**,
**Undeploying**, **Deployed**, **Deployed with errors**, **Undeployed with errors** . To view the updated status, refresh the

page.




##### Important Recommendations

















The smart view deploy is based on the difference between existing and new data, so existing data is maintained.
Any new measures/attributes selected before the current deploy are filled as soon as the deploy is completed.
However, if you deliberately want to destroy and recreate the smart view with the consequent new data load,
you have to undeploy the smart view and deploy it again.
In the latter case, please be aware that the deploy operation takes a long time, as it deletes and recreates all
data currently stored in the Smart View.
The successful completion of neither the deploy nor the undeploy of a smart view is automatically visible.
Therefore, before starting the deploy or undeploy of a smart view you need to check on the **Monitoring**
**Messages** page that the previous deploy or undeploy of that smart view has been completed successfully. This
is particularly recommended when you want to execute one operation immediately after the other.
If you create an extension for a project for which you have already executed a deploy of the associated
environment, you must execute the deploy again before running the smart view.
If the selected source is SIMATIC IT UAPI or Opcenter Execution Process, only the following format is supported
for datetime fields: yyyy-mm-dd hh:mm:ss. Any other format will be discarded from the system. Non-standard
formats can, however, be loaded by overriding the contract layer.
The deploy of a smart view will not affect the data you have configured for environments. A specific deploy of an
environment can be executed in the corresponding page.


###### Procedure



1.


2.

3.


4.



In the **Smart View** page, select a smart view.


Click **Deploy Smart View** .
Select an environment and click **Deploy** . During the deploy operation, the **Deploy Info** on the smart view tile
shows the **Deploying on <** _**environment name**_ **>** message.
In the **Monitoring Messages** page, monitor the progress and completion of the deploy operation. When the
deploy has been completed successfully, the **Deploy Info** on the smart view tile shows the **Deployed on**
**<** _**environment name**_ **>** message. If any errors occurred during the deploy, the **Deployed with errors** message is
displayed.




### 11.7 Undeploying a Smart View

You can undo the deploy of a smart view. The undeploy operation is required before deleting a smart view to free
allocated resources in the data warehouse and avoid performance issues. The progress of this operation is tracked
on the **Monitoring Messages** page.


Opcenter Intelligence 2401.0001 - User Manual 99


_How to Configure Smart Views_


_Running a Smart View_

###### Smart View Undeploy Status


The undeploy status of a smart view is shown on each smart view tile, followed by the name of the environment
selected when the undeploy operation has been started. The possible statuses can be **NotDeployed**, **Deploying**,
**Undeploying**, **Deployed**, **Deployed with errors**, **Undeployed with errors** .. To view the updated status, refresh the

page.




##### Important Recommendations









The successful completion of neither the deploy nor the undeploy of a smart view is automatically visible.
Therefore, before starting the deploy or undeploy of a smart view you need to check on the **Monitoring**
**Messages** page that the previous deploy or undeploy of that smart view has been completed successfully. This
is particularly recommended when you want to execute one operation immediately after the other.
If by mistake you launch an undeploy operation before you have deployed the smart view, no error is returned
and the smart view remains unchanged.


###### Procedure



1.


2.

3.


4.



In the **Smart View** page, select the smart view for which you want to undo the deploy operation. The smart view
must be in **Deployed** status.


Click **Undeploy Smart View** . This button is not visible if the smart view has not been deployed before.
Select the environment and click **Undeploy** . All the structures and objects created during the previous deploy
operation are removed. During the undeploy operation, the **Deploy Info** on the smart view tile shows the
**Undeploying on <** _**environment name**_ **>** message.
In the **Monitoring Messages** page, monitor the progress and completion of the operation. When the undeploy
has been completed, the **Deploy Info** on the smart view tile shows the **NotDeployed on <** _**environment name**_ **>**
message. If any errors occurred during the deploy, the **Undeployed with errors** message is displayed.


### 11.8 Running a Smart View

In this step you can configure and run either an initial or an incremental load for the selected smart view.




###### Prerequisites










You must have deployed the environment at least once.
Check that no other operation, such as a deploy or another flow, is running at the same time. If that is the case,
wait for this operation to end before starting any other action.
To ensure an adequate performance, it is strongly recommended that you disable any flow schedule you have
planned for data sources before running an initial load for smart views.


###### Procedure



1.


2.

3.

4.



In the **Smart View** page, select a smart view. The smart view must be in **Deployed** status.


Click **Run Smart View** . This button is not visible if the smart view has not been deployed before.
In the **Run Smart View** page, select an environment.
Specify a **Start Date** and an **End Date** to define the time interval for the data you want to load.



100 Opcenter Intelligence 2401.0001 - User Manual


_How to Configure Smart Views_


_Additional Operations_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-100-0.png)





5.



Click **Start** to run the smart view.


### 11.9 Additional Operations

The following additional operations can be performed on a smart view:











Manage contexts
Edit a smart view

Purge a smart view
Delete a smart view

Rename measures or attributes


#### 11.9.1 Managing Contexts

In this step you can manually add a relationship between a fact table and a context that have not been directly
linked. After you have performed this operation, you must retrieve the context values by editing the SQL scripts for
the entities generated by smart views.


If the contexts added automatically by the system are correct and you do not want to add any additional contexts,
you can proceed to select attributes. If on the contrary you want to manage additional contexts, go to the **Contexts**

page.


Sometimes a context is associated with a fact table and therefore shown as a standard context but the system is not
able to retrieve its value. To do so, you will need to customize the SQL scripts by using a specific function.

###### Procedure



1.


2.


3.


4.



In the **Smart View** page, click the **Contexts** tab. The list of all the existing contexts is shown, depending on the
entities you have selected in the **Measures** page.
The **Standard** section of each card will contain the contexts that have already been associated with a fact table,
which cannot be deselected. The **Custom** section will show all the contexts that have not been linked to that

entity.
Add the contexts you want to link by selecting the corresponding check box(es).


Click **Save Contexts** . The database columns in the related table/view are created for the newly-added
contexts. To retrieve the value of these contexts, you must edit the SQL scripts for the entities generated by
smart views.




#### 11.9.2 Editing a Smart View

You can modify some of the options selected when you created the smart view.





Opcenter Intelligence 2401.0001 - User Manual 101


_How to Configure Smart Views_


_Additional Operations_

##### Procedure



1.

2.



In the **Smart View** page, click the smart view that you want to edit and click **Edit Smart View** .
If you want to change the smart view **Type**, the following options are available:




      - from **Physical** to **Virtual** : the associated smart view flows and flow schedule are deleted;

      - from **Virtual** to **Physical** : flows and flow schedules are automatically created.
3. You can edit the flow schedule by changing the options in the **Schedule** drop-down menu, which can be **Every**

**2, 5, 10, 30 or 60 minutes** depending on how frequently you want to update the database tables created by the
smart view. This option is enabled only when the selected smart view **Type** is **Physical** .



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-101-0.png)





4.



Click **Save** .


#### 11.9.3 Editing Measures, Attributes, or Contexts

You can edit existing smart views by modifying the options you selected when you created them.


Saving measures and/or attributes does not modify the physical structure of the manufacturing data warehouse. As
a result, a deploy of the smart view is always required after the edit operation.




##### Procedure



1.

2.

3.


4.


5.



In the **Smart View** page, click **Open Smart View** .
Click the **Measures**, **Attributes**, or **Contexts** tab.
Select or deselect measures, attributes or contexts depending on the option selected in the previous step.


Click **Save Measures** or **Save Attributes** or **Save Contexts** .


In the **Smart View** page, select the edited smart view and click **Deploy Smart View** .


#### 11.9.4 Purging a Smart View

The purge operation deletes all data for the selected smart view. Smart Views are usually loaded, updated and
deleted automatically depending on the changes to the bm20 tables of the data warehouse. However, you may
want to delete all data from a smart view in order to reload them.


After the purge of a smart view, all data contained in the smart view entities is deleted. bm20 data is maintained
and when the purge has been completed, the smart view is reloaded and populated on the basis of bm20 data,
including data in the past. Depending on the amount of data contained in the smart view, the loading operation
may take some time.

##### Prerequisites


Before you start a purge view operation, check that no other operation, such as a deploy or a flow, is running at the
same time. If that is the case, wait for this operation to end before starting any other action.

###### Procedure



1.



In the **Smart View** page, select a smart view.



102 Opcenter Intelligence 2401.0001 - User Manual


2.

3.

4.



_How to Configure Smart Views_


_Additional Operations_


Click **Purge Smart View** . This button is not visible if the smart view has not been deployed before.
In the **Purge View** page, select an environment.
Click **Start** .


#### 11.9.5 Deleting a Smart View

###### Important Recommendation

When you delete a smart view, you only delete the configuration, but the corresponding entities are not deleted
from the manufacturing data warehouse, including entities that have been deployed, or running flows (if they have
been scheduled). The manual deletion of such entities is therefore required.

###### Procedure



1.


2.

3.



In the **Smart View** page, select a smart view.


Click **Delete Smart View** .

Click **Delete** .




#### 11.9.6 Renaming Measures or Attributes

You may need to rename measures or attributes. You can change the name assigned by the product to measures
and attributes or to any type of card.




##### Renaming Convention

If you want to rename the cards displayed for measures and attributes, you must apply the following rules, which
do not allow:









All the names used for out-of-the-box functionalities.
All the names of out-of-the-box entities (which include all possible contexts).
All (context or functionality) aliases already created for that smart view.



For measures, you must apply the following rules, which do not allow:








The use of out-of-the-box (standard) measures.
The aliases of measures you have already created.



For attributes, you must apply the following rules, which do not allow:








The use of out-of-the-box (standard) attributes.
The aliases of attributes you have already created.


###### Procedure



1.

2.


3.

4.



In the **Smart View** page, select a smart view and click **Open Smart View** .
Click either the **Measures** or **Attributes** tab.


Click the **Edit Measures** / **Edit Attributes** button depending on the option selected in the previous step.
Rename card names, measure names or attribute names.



Opcenter Intelligence 2401.0001 - User Manual 103


_How to Configure Smart Views_


_Additional Operations_



5.


6.


7.



Click **Confirm Edit** .


Click **Save Measure** or **Save Attribute** .


In the **Smart View** page, select the edited smart view and click **Deploy Smart View** .



104 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Runtime Operations_


_How to Manage Dashboards using Opcenter Intelligence Analytics_

## 12 How to Perform Runtime Operations


In version 3.2 a new licensing model was introduced, which enables you to install Opcenter Intelligence Analytics
(Tableau® OEM) during Opcenter Intelligence setup and create dashboards in this embedded version.




##### Accessing the page

To access the runtime page, click the **Analytical Tools** card in the **Home** page.

###### Available Operations


Manage Dashboards using Opcenter Intelligence Analytics (Tableau® OEM)

### 12.1 How to Manage Dashboards using Opcenter Intelligence Analytics

###### Target Users










Users with the **Desktop Explorer** role can perform all operations, including creating dashboards and publishing
data sources.

Users with the **Analytics Explorer** role can create dashboards.
Users with the **Analytics Viewer** can only view dashboards.





For more details on licenses, users and roles, see _Opcenter Intelligence_ _Quick Start Installation Manual_ .

###### Workflow



1.

2.

3.



Publish Data Sources using Opcenter Intelligence Analytics Desktop
Manage Dashboards in Opcenter Intelligence Analytics
(Optional) Embed Opcenter Intelligence Analytics Dashboards


#### 12.1.1 Publishing Data Sources using Opcenter Analytics Desktop

To create dashboards based on MDW data, you must publish data sources on Opcenter Intelligence Analytics Server
using Opcenter Intelligence Analytics Desktop.




###### Authentication

Depending on the **Run as Server** configuration in Opcenter Intelligence Analytics Configurator, authentication can
be handled as follows:







if you have selected **NT AUTHORITY\Network Service** and the scenario is all-in-one, create a login for the
Network Service Windows user in Microsoft SQL Server.



Opcenter Intelligence 2401.0001 - User Manual 105


_How to Perform Runtime Operations_


_How to Manage Dashboards using Opcenter Intelligence Analytics_









if you have selected **User Account**, you need to create the appropriate logins in SQL Server and assign the
correct permissions to grant access to the data warehouse.


##### Prerequisites











You have installed Opcenter Intelligence Analytics during Opcenter Intelligence setup.
You have configured Opcenter Intelligence Analytics using Opcenter Intelligence Configurator. For more details,
see _Opcenter Intelligence Installation Manual_ .
You have reset the password for the Desktop Explorer role.
You have signed in to Tableau® Server from Tableau® Desktop. For more details, see https://help.tableau.com/
v2021.4/pro/desktop/en-us/sign_in_server.htm



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-105-1.png)








###### Important Recommendations











If the operating system on your machine is **Windows Server 2019**, you have to grant full control on the
**Siemens\Tableau\Tableau Server** folder in the **Properties\Security** tab to the user configured in Opcenter
Intelligence Analytics Configurator in the **Run As Service Account** section.


This user can be the **Network Service** user as in the example below, or a custom **User Account** . Based on this
selection, you need to make sure that folder permissions are provided with full control by adding the Network
Service user or the custom User Account.

The NT Authority\NetworkService user or the custom user needs to have proper access to Data Warehouse
databases and tables in SQL Server.



106 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Runtime Operations_


_How to Manage Dashboards using Opcenter Intelligence Analytics_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-106-0.png)


##### Procedure



1.


2.



Publish Data Sources. For more details on this operation, see https://help.tableau.com/v2021.4/pro/desktop/
en-us/publish_datasources.htm
Starting from version 3.5 of Opcenter Intelligence, when you publish data sources from Opcenter Intelligence
Analytics Desktop, you can select either **Default** project or **Opcenter Intelligence** project.




#### 12.1.2 Managing Dashboards using Opcenter Intelligence Analytics

In this page you can create, manage and view dashboards using the embedded Opcenter Intelligence Analytics
(Tableau® OEM).

###### Prerequisites


You must have published data sources on Opcenter Intelligence Analytics Server using Opcenter Intelligence
Analytics Desktop.

###### Procedure



1.



Click the **Analytical Dashboards** card.



Opcenter Intelligence 2401.0001 - User Manual 107


_How to Perform Runtime Operations_


_How to Manage Dashboards using Opcenter Intelligence Analytics_



2.



Click **Open Tableau Server** . For detailed instructions on how to operate in Tableau® OEM, go to https://
www.tableau.com/support/help and select version **2021.4** .



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-107-1.png)








###### Important Note

In case the error: "An error occurred while connecting Tableau server" is returned when you click the **Open Tableau**
**Server** command, follow these steps:



1.

2.


3.



Launch Opcenter Intelligence Configurator > **Manage Configuration** option again.
In the **Opcenter Intelligence Analytics Configuration** area, in the **Analytics Server URL** field, insert the IP
address of the machine where Tableau® server is installed.

Click **Apply** and then **Close** .


#### 12.1.3 How to Embed Opcenter IN Analytics Dashboards in a Custom Application

You can embed the Opcenter Intelligence Analytics (Tableau® OEM) dashboards directly into your custom
application using the Siemens Web Application Collaboration (SWAC) library.


For more information on the SWAC Library, see _SWAC_ _Documentation_, available at https://code.siemens.com/swac/
sdk/development/-/tree/master/documentation

##### Prerequisites











The SWAC Library has been imported. For more information on how to import and integrate a SWAC component
in a Siemens Web Framework (SWF) project, see _SWAC Documentation_ .
You have used User Management Component (UMC) authentication to log in to Opcenter Intelligence. If UMC
was installed with another product that uses UMC as Identity Provider (for example Opcenter Execution
Discrete), the same user that authenticated in Opcenter EX DS must be a user in Opcenter Intelligence too with
Desktop Explorer, Analytics Explorer or Analytics Viewer role.
You have created and published a dashboard in Opcenter Analytics (Tableau® OEM).



For information on SWAC prerequisites, see _SWAC Documentation_ .

###### Available Operations








Integration Methods
Embed Dashboards


##### 12.1.3.1 SWAC Integration Methods

The SWAC Component provides the following methods to retrieve and show the dashboard list.

###### getAllDashboards


108 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Runtime Operations_


_How to Manage Dashboards using Opcenter Intelligence Analytics_


Retrieves the list of published dashboards according to the same hierarchical structure as the UI: **Site** - **Projects** **Workbooks** - **Views** .


The return type is an array, for example:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-108-0.png)


##### showDashboard

Shows the dashboard list.


The **ContentUrl** property present on the **View** object as in the above example needs to be passed to this function in
order to display the required View (Dashboard).

##### 12.1.3.2 Embedding Opcenter IN Analytics Dashboards

###### Procedure



1.


2.


3.


4.

5.



Create an HTML file and refer to the SWAC libraries. You can use script tags in HTML to add references.



Configure the necessary SWAC library properties. Example: SWAC.Config.LevelLog = 1;
SWAC.Config.TimeOuts.Enabled = false.
(Optional) Specify the path of the SWAC base library, which permits the execution of SWAC code and
communication between SWAC container and SWAC component. Example:
SWAC.Config.Container.URLs.BaseLibrary = < _URL_ Initialize the SWAC component object by configuring the necessary properties.
Create the SWAC component by calling the **beginCreate** method in the SWAC library.





Opcenter Intelligence 2401.0001 - User Manual 109


_How to Perform Runtime Operations_


_How to Manage Dashboards using Opcenter Intelligence Analytics_



6.


7.


8.



Subscribe to the **onReady** event to call exposed SWAC component methods. Only after the onReady event has
been fired, it is possible to call all the SWAC component methods.
Fetch the SWAC component object by component name and call the necessary method exposed by the SWAC
component.
In the callback function, use the **beginShow** ( **true** ) method to display the SWAC component.





110 Opcenter Intelligence 2401.0001 - User Manual


_Monitoring Operation Execution_


_How to Manage Dashboards using Opcenter Intelligence Analytics_

## 13 Monitoring Operation Execution


In the **Monitoring** **Messages** page you can view details of command execution and history, check deploy progress,
verify schedule history and check flow progress and history. You can monitor various operations through the tabs
which provide filters to procure data on the basis of different filter criteria. The operations within each tab are
described in the sections below:










Main Command

Deploy Details
Schedule History
Flow Details


###### Target Users

Only users with the following roles can access this page and see its content:









**Administrator**
**Solution engineer**
**SmartView engineer**


###### Main Command

You can monitor the progress of a number of operations such as the deploy of an environment, an initial or
incremental load or the purge of a database. You can view the main commands filtered by **Solutions**, **Scenarios**,
**Environments**, and **Commands** . You can view the logs of commands and their status in the last 24 hours
in **Command History** . The following table lists the icons and the corresponding descriptions of the possible
command history statuses.

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-110-0.png)

###### Deploy Details


You can monitor the progress of the deploy operation filtered by deploy history.

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-110-1.png)


Opcenter Intelligence 2401.0001 - User Manual 111


_Monitoring Operation Execution_


_How to Manage Dashboards using Opcenter Intelligence Analytics_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-111-0.png)














###### Schedule History

You can view the planned schedules filtered by solution, scenario, environment and date and time. The **Schedules**
area displays the schedule history on the basis of options selected in the filter criteria.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-111-1.png)






###### Flow Details

You can view the progress of the execution of the selected flow.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-111-2.png)







112 Opcenter Intelligence 2401.0001 - User Manual


_Monitoring Operation Execution_


_Setting the Server-wide Default Logging level in the SSIS Catalog_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-112-0.png)










### 13.1 Setting the Server-wide Default Logging level in the SSIS Catalog

The SSIS catalog is a central repository for storing, configuring and executing packages. One of the catalog features
is the built-in logging, which stores information about various events and statistics in the SSISDB database. There is
a default logging level you can configure for the entire SSIS catalog that will enable you to correctly display and
monitor the progress of the flows in the **Monitoring Messages** page.

###### Procedure



1.

2.

3.

4.



Connect to the SQL Server instance using SQL Server Management Studio.
Expand the **Integration Services Catalogs** node.
Right click on the **SSISDB** node and select **Properties** .
Set the **Server-wide Default Logging Level** (under the **Operations Log** category) to **Basic** .



Opcenter Intelligence 2401.0001 - User Manual 113


_How to Upgrade a Reporting Framework 7.0 Solution to Opcenter Intelligence 2401_


_Importing the Solution File_

## 14 How to Upgrade a Reporting Framework 7.0 Solution to Opcenter Intelligence 2401


Perform the following procedure if you want to migrate a solution created in SIMATIC IT Reporting Framework 7.0
to Opcenter Intelligence 2401. The old solution items will be migrated as well as the data contained in the database.




###### Prerequisites

You have exported the SIMATIC IT RF 7.0 solution file in .xml format.

###### Workflow



1.

2.

3.



Import the Solution File
Check the Migration Results
Manage Overloaded Custom Entities Scripts


### 14.1 Importing the Solution File

Follow this procedure to import a solution created and exported using SIMATIC IT Reporting Framework 7.0
into Opcenter Intelligence.

###### Procedure



1.

2.

3.

4.


5.

6.

7.


8.


9.



In the **Solutions** page, click **Import Solution** . The **Import Solution** page is displayed.
Click **Choose File** to browse for the .xml file.

Select the file and click **Open** .
Insert a name for the solution in the **Solution Name** edit box.


Click **Import** .
Click **Ok** to save the solution.
If the source database of the solution you are importing is of type LMS, the **Edit Database Source** page is
displayed. The name of the LMS database of the RF 7.0 solution is shown under **Database Name** . Select the
**Database Type**, which can be either **Line Monitoring System 2.2 SP1** or **Line Monitoring System**
**2.3-2.4-2.5-2.6-2.7** and click **Save** .
Click **Yes** if you want to manage the flows to migrate the content of the MDW 1.0 database together with the
solution data.
If you are warned that the solution you are importing contains custom entities, you should verify that after the
import they have been exposed correctly. In particular, you should check the data types to make sure that the
semantics has been properly formulated according to your requirements.


###### Result

The imported solution is available in the **Solutions** page. Now you must perform a check and possibly modify the
flows created during the import operation and the solution environment.

### 14.2 Post-Migration Check


After the migration has been performed, you should check that a number of items of the new solution correspond
to what you configured in the old project version.


114 Opcenter Intelligence 2401.0001 - User Manual


_How to Upgrade a Reporting Framework 7.0 Solution to Opcenter Intelligence 2401_


_Managing Overloaded Scripts_


###### Procedure



1.


2.


3.


4.


5.



The source version is migrated. The old source types that are not compatible with Opcenter Intelligence are
migrated to new types. In particular:




    - replace **PPA: [** _**linkedserver name**_ **].[** _**PPAdbname**_ **]** with **PPA:** _**PPAdbname**_ and **PPA Linked Server:**

_**linkedserver name**_ (without square brackets);

    - replace **SitMes: [** _**linkedserver name**_ **].[** _**SitMesdbname**_ **]** with **SitMes:** _**SitMesdbname**_ and **SitMes Linked**

**Server:** _**linkedserver name**_ (without square brackets).
Custom entities, if present, must be checked. You must verify that after the migration they have been exposed
correctly. In particular, you must check the data type to make sure that the semantics has been properly
formulated according to your requirements. The entity type, which can be either **Analytical Context** or
**Analytical Type**, must be specified after the migration.
If the migration project contains at least a MDW 1.0 source, when all the project functionalities have been
enabled, the views that are provided after the deploy of the new solution will entirely emulate the OOTB
structures of the old MDW database. As a result, the OOTB reports you have created in SIMATIC IT Reporting
Framework 7.0 will not require any modification. Custom reports created in SIMATIC IT RF 7.0 should be
checked, as a minimum number of modifications may be required.




    
all the SIMATIC IT Production Suite versions that are not compatible with Opcenter Intelligence will be
included in the Production Suite 7.0 SPx - 7.1 - 7.2 - 8.0 source.


    
all the SIMATIC IT Line Monitoring System versions that are not compatible with Opcenter Intelligence
will be included in the SIMATIC IT LMS 2.3 - 2.4 - 2.5 - 2.6 - 2.7 source.

Two flows are created:


    
a standard flow that loads current data and must be scheduled;

    - a one-shot flow that loads the old MDW 1.0 data if you have answered **Yes** to the question made during

the import operation.
(Optional) If the source is SIMATIC IT LMS or SIMATIC IT Production Suite and you have configured a linked
server, change the values of environment properties as follows:


















### 14.3 Managing Overloaded Scripts

When you import a solution from SIMATIC IT Reporting Framework 7.0, some custom entities scripts, due to their
complexity, may not be imported automatically.
The following table contains the list of these entities. The first column lists the names of the SIMATIC IT RF 7.0
entities for which the overloaded scripts cannot be imported by the system. You must therefore modify these
scripts on the basis of the new entity form shown in the second column of the table.
Some of the entities listed in the first column may not have a corresponding item in the second column, because
they have not been deemed useful for version 2.0 of the data warehouse. As a result, these entities should be
considered as custom entities and treated accordingly.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-114-0.png)



Opcenter Intelligence 2401.0001 - User Manual 115


_How to Upgrade a Reporting Framework 7.0 Solution to Opcenter Intelligence 2401_


_Managing Overloaded Scripts_

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-115-0.png)


116 Opcenter Intelligence 2401.0001 - User Manual


_How to Upgrade a Reporting Framework 7.0 Solution to Opcenter Intelligence 2401_


_Managing Overloaded Scripts_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-116-0.png)

Opcenter Intelligence 2401.0001 - User Manual 117


_How to Upgrade a Reporting Framework 7.0 Solution to Opcenter Intelligence 2401_


_Managing Overloaded Scripts_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-117-0.png)



118 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Advanced Operations_


_How to Manage the Update of a Data Source Product Version_

## 15 How to Perform Advanced Operations


The following advanced operations can be performed on Opcenter Intelligence data warehouse:











Manage the Update of a Data Source Product Version
Manage the interaction between EX FN Cleaning Rules and OpcenterINCloud Flow Schedules
Set up a Maintenance Plan for the Data Warehouse
Enable Change Data Capture and Change Tracking
Manage the size of the SQL Server Integration Services Database SSISDB


### 15.1 How to Manage the Update of a Data Source Product Version



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-118-0.png)






##### Prerequisites








The source system has been updated.
You have installed the latest version of Opcenter Intelligence.


###### When is the execution of this workflow required?

You must execute this workflow when a new slice with a new version number is added to the pie chart.

###### Important Recommendation


Starting from Opcenter Intelligence 3.2, due to a refactoring of the data model, it is strongly recommended that you
perform a purge operation and run an initial load on the MDW if your data source is Opcenter Execution Process or
Opcenter Execution Discrete and you are upgrading from version 3.0 or higher.


However, this recommendation does not apply if you have removed obsolete data from these databases, for
example to perform long-term data archiving or if you are using Opcenter Execution Foundation Maintenance
Configuration. For more details on the latter, see the _How to Configure Maintenance_ chapter in _Opcenter Execution_
_Foundation Development and Configuration Guide_ .

###### Workflow



1.

2.

3.



Update the migrated Solution Items
Retrieve the Start Time for the New Flow

Start the Data Flow


#### 15.1.1 Migrating the EquipmentKey in Opcenter Execution Discrete

This migration procedure must be executed only when a customer using Opcenter EX DS 3.x or 4.0 upgrades to
Opcenter EX DS 4.1 or higher and Opcenter Intelligence 2401.0001.


Opcenter Intelligence 2401.0001 - User Manual 119


_How to Perform Advanced Operations_


_How to Manage the Update of a Data Source Product Version_

###### Procedure



1.


2.


3.


4.


5.

6.

7.

8.


9.



After checking on the **Monitoring Messages** page that any running flows have been completed successfully,
stop the flow schedule that loads data from Opcenter Execution Discrete 3.x or 4.0 to the MDW.
In the Solution, create the **EquipmentMigration** custom entity of type **Analytical Context** and **Standard**
granularity type. Then add a column called **NId** of type **Name** . For more details, see How to Configure Model
Extensions.

Associate the new custom entity with the Opcenter EX DS 3.x or 4.0 source. See Selecting the Model Extension
Source
In the Scenario, in the Server configured for the Opcenter EX DS 3.x or 4.0 source, open the database and create
a script. In the **Models** drop-down list, select **Custom Model** . In the drop-down list select the
**EquipmentMigration** entity. Replace the template script with the following script:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-119-0.png)

Click **Save** . For more details, see Loading a Script.
Deploy the environment.
Run the Single Entity by specifying the **EquipmentMigration** entity and selecting 2010-01-01 as **Start Date** .
In **Microsoft SQL Server Management Studio**, select the connection where the MDW is present and create a

new query.
Copy the following script to the new query and execute it.





![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-119-2.png)





120 Opcenter Intelligence 2401.0001 - User Manual


10.


11.


12.

13.



_How to Perform Advanced Operations_


_How to Manage the Update of a Data Source Product Version_


Add the new Opcenter Execution Discrete 4.1 or higher data source, as described in Updating the migrated
Solution Items.
Before starting the new flow, get the correct time window to be used as start date and time for the flow, as
described in Retrieving the Start Time for the New Flow.
Start the Flow.
If you have configured and deployed any smart view, deploy it again.




#### 15.1.2 Updating the migrated Solution Items

The following procedures must be executed to upgrade the items of the solution that has been migrated from the
previous version of Opcenter Intelligence.

###### Update the Project



1.

2.

3.



Open the migrated Solution.
Open the Project and add a new Source.
Select the existing Physical Site that has been migrated with the solution.


###### Update the Scenario



1.


2.


3.

4.



Open the Scenario and do either of the following:



In the **Flows** page, select the existing flow schedule and click **Disable Flow Schedule** to disable the
corresponding SQL Server job.
In the existing **Destination Server**, in the **Flows** tab, create a new Flow and select the new version of the source.
Open the newly-created flow and create a new Flow Schedule.








If the new source is hosted in the same server as the old source, add a new Database to the server.
If the new source is not hosted in the same server as the old source, create a new server with the new
source as project source.


###### Update and Deploy the Environment



1.


2.



Edit the Environment.




    
If the new source is hosted in the same server as the old source, copy and paste the existing parameters
(IP address, Database, Properties).


    
If the new source is hosted in a different server, you must specify the new IP address and the new
database instance. However, do not change the MDW name so that data can be written on the same
database.
Deploy the Environment. This operation will create new scripts and a new flow, which will be disabled by
default.










#### 15.1.3 Retrieving the Start Time for the New Flow

Before enabling and running the new flow, you must perform the following manual operations, otherwise the flow
would start loading the data previously loaded from the old version of the source, resulting in poor performance
(e.g. discarded data).

###### Procedure


Opcenter Intelligence 2401.0001 - User Manual 121


_How to Perform Advanced Operations_


_How to Manage the Update of a Data Source Product Version_



1.

2.


3.


4.


5.



In **SQL Server Management Studio**, connect to the SQL instance that contains the **MIStudio** database.
Use the SELECT statement to retrieve the **flowId** of the old source and jot it down.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-121-0.png)

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-121-1.png)

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-121-2.png)

Execute the query, whose purpose is to retrieve the most recent **TimeWindowTo** field to be used as **Start Date**
**and Time** for the new flow.





Use the SELECT statement to retrieve the **environmentId** and jot it down.





In the following query, replace @ **flowId** and @ **environmentId** with the values you have previously jotted down.




#### 15.1.4 Starting the Flow

Follow this procedure to start the data flow from the new source to the manufacturing data warehouse.

###### Procedure



1.

2.

3.

4.

5.


6.

7.

8.


9.



Go back to the **Scenario** and in the **Flows** tab select the flow created after the deploy operation.
Run the flow.

Select the **Initial load** mode.

Select the **Manual** start mode.
Set the **Start Date and Time** you have retrieved using the query. The date of the retrieved field is in UTC format,
you must convert it to local time.
Leave the default **End Date and Time** .

Start the flow.
In the **Monitoring Messages** page, verify that the run flow operation has been completed successfully.


In the **Flows** page, select the flow schedule and click **Enable Flow Schedule** to enable the corresponding
SQL Server job again.



122 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Advanced Operations_


_How to manage interaction between EX FN Cleaning Rules and Opcenter IN Flow Schedules_

### 15.2 How to manage interaction between EX FN Cleaning Rules and Opcenter IN Flow Schedules


When you configure maintenance in Opcenter EX FN database for Opcenter EX DS or Opcenter EX PR, you can
configure:









**Cleaning Rules**, to clean the live (runtime) database from the entities that are not needed for production

anymore.
The **Archiving Rule**, which is used to schedule the archiving of production data from the live (runtime) database
to an Archiving database.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-122-0.png)









If Opcenter Intelligence is extracting data from the Opcenter EX DS or Opcenter EX PR database, you have to
schedule Cleaning Rules appropriately to avoid that their execution overlaps with the execution of Opcenter
Intelligence Flow Schedules, which would result in an incomplete or failed update of the Manufacturing Data
Warehouse.


You can schedule cleaning rules for these databases:








Opcenter EX FN Online database
Opcenter EX FN Archiving database


#### 15.2.1 Scheduling Rules for Opcenter EX FN Online Database

When Opcenter Intelligence is extracting data from the Opcenter EX DS or Opcenter EX PR online database, you
have to make sure that cleaning rules configured on the source online database do not overlap with the data flow
schedules configured in Opcenter Intelligence, otherwise you might risk that data is cleaned from the source
database before the latest modifications are extracted by Opcenter Intelligence, causing an incomplete update of
the same data in the Manufacturing Data Warehouse.


This is the reason why, when an Opcenter Intelligence data flow is extracting data from the online database, the
cleaning rules should always be configured by adding a condition on the **Unchanged For** field and inserting a value
that must be higher than the period of the Opcenter Intelligence data flow schedule. This condition must be applied
in **AND** to the other existing conditions on the **To Be Cleaned** and/or **Is Logically Deleted** fields.


In this way, you make sure that the Opcenter Intelligence data flow is always executed at least once between the
**LastUpdateOn** time of the entity and the actual entity cleaning.

###### Example


If the ETL flow schedule has been configured to run every hour, the cleaning rule should be configured to be applied
only to those entities whose **Unchanged For** field is higher than one hour, i.e. only to those entities whose
**LastUpdateOn** property is more than one hour earlier than the execution time of the cleaning rule (for example, if
the **Unchanged For** condition is set to two hours, only the entities last updated more than two hours before the
execution of the cleaning rule are affected by the cleaning rule).



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-122-1.png)





Opcenter Intelligence 2401.0001 - User Manual 123


_How to Perform Advanced Operations_


_Setting Up a Maintenance Plan for the Data Warehouse_

#### 15.2.2 Scheduling Rules for Opcenter EX FN Archiving Database


When Opcenter Intelligence is extracting data from the Opcenter EX DS or Opcenter EX PR archiving database, you
have to make sure that SQL Jobs for removing logically deleted data from the archive do not overlap with the data
flow schedules configured in Opcenter Intelligence, otherwise you might risk that data is deleted from the archiving
database before it is also deleted from Opcenter Intelligence.


This is the reason why, when an Opcenter Intelligence data flow is extracting data from the archiving database, the
data deletion SQL Jobs should always be configured so that the condition clauses include at least a condition on
the **LastUpdatedOn** field of the entity (whose value must be older than the SQL job execution time minus the data
flow schedule period). The SQL Job scheduling must also be configured taking the data flow schedule into account.

###### Important Recommendation


It is recommended that you customize the stored procedure provided by Opcenter Execution Foundation
( **PurgeLogicallyDeletedItems** ) as follows:



1.

2.



Make a copy of the stored procedure.
Configure the SQL Job so that the copy is executed.


###### Example

If the ETL flow schedule has been configured to run every day, the customized data deletion stored procedure (SQL
Job) should be configured to be applied only to those entities whose **LastUpdatedOn** field in the condition
expression is more than one day earlier than the execution time of the stored procedure (e.g. seven days earlier, so
that only the entities deleted more than seven days before are affected).

### 15.3 Setting Up a Maintenance Plan for the Data Warehouse


A maintenance plan is made up of a sequence of tasks required to make sure that a data warehouse is optimized
and free of inconsistencies. You should define a maintenance plan to manage the log file growth and fine-tune the
data warehouse configuration to provide the best performance.


The following tasks are recommended:

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-123-1.png)

###### Backup Database (Full)


124 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Advanced Operations_


_Enabling Change Data Capture and Change Tracking_


The Backup Database (Full) task executes the **BACKUP DATABASE** statement and creates a full backup of the
database. You will probably want to run this task daily against your system and production databases. In most
cases, the databases you will be backing up with this task use the Full Recovery model, and you will also want to run
the **Backup Database (Transaction Log)** task as part of your Maintenance Plan.

###### Backup Database (Differential)


The Backup Database (Differential) task executes the **BACKUP DATABASE** statement using the **DIFFERENTIAL**
option. This task should only be used if you need to create differential backups.

###### Backup Database (Transaction Log)


The Backup Database (Transaction Log) task executes the **BACKUP LOG** statement, and, in most cases, should be
part of any Maintenance Plan that uses the **Backup Database (Full)** task. It is a common practice to run this task
every hour or so, depending upon your needs.

###### Rebuild/Reorganize Indexes and Update Statistics


To maintain index and statistics performance, it is recommended that you create a job schedule in SQL Server
Agent that executes the system commands required to rebuild/reorganize indexes and update statistics. This
procedure should be launched with at least daily frequency. For Enterprise systems the index rebuild operation can
be executed anytime, while for Standard systems you should identify a period of low or no workload of the system,
as indexes are rebuilt offline. This procedure too should be launched with daily frequency.


To simplify this process, the data warehouse contains the following native stored procedure that executes the basic
procedure to rebuild or reorganize indexes and update statistics:


[control].[USP_OptimizeIndexesAndUpdateStats


This stored procedure accepts as a parameter the name of the data warehouse you have created and for which you
want to perform the maintenance of indexes and statistics.


**Example**


exec [control].[USP_OptimizeIndexesAndUpdateStats] 'MDW_Database'


For more information on SQL Server Agent job definition and scheduling, see _Microsoft SQL Server documentation_ .

### 15.4 Enabling Change Data Capture and Change Tracking


Microsoft SQL Server provides the Change Data Capture (CDC) and Change Tracking (CT) features, which allow
applications to determine the DML (Data Manipulation Language) changes (insert, update and delete operations)
made to user tables in a database.





Two examples are provided which describe how to map a specific table to the **IndicatorValue** table (default table).
In the examples, the following tables have been created with this format:


Table name: **Counter**



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-124-1.png)



Opcenter Intelligence 2401.0001 - User Manual 125


_How to Perform Advanced Operations_


_Enabling Change Data Capture and Change Tracking_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-125-0.png)



Table name: **Machine**



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-125-1.png)





The examples show how to solve the following issues:








How to unpivot an entity: enable the Change Data Capture functionality.
How to retrieve insertion dates and record modification when they are not present natively: enable the Change
Tracking functionality.


#### 15.4.1 Change Data Capture Examples

The following scripts can be used to obtain data on Change Data Capture.


To load the scripts, follow the procedure described in the Loading a Script section.

###### Example 1 - Counter Table



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-125-2.png)



126 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Advanced Operations_


_Enabling Change Data Capture and Change Tracking_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-126-0.png)


###### Example 2 - Machine Table



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-126-1.png)


###### Results

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-126-2.png)

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-126-3.png)

#### 15.4.2 Change Tracking Examples

The following scripts can be used to obtain data on Change Tracking.


To load the scripts, follow the procedure described in the Loading a Script section.

###### Example 1 - Counter Table


Opcenter Intelligence 2401.0001 - User Manual 127


_How to Perform Advanced Operations_


_Enabling Change Data Capture and Change Tracking_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-127-0.png)


###### Example 2 - Machine Table



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-127-1.png)


###### Results

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-127-2.png)

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-127-3.png)

128 Opcenter Intelligence 2401.0001 - User Manual


_How to Perform Advanced Operations_


_Managing the size of the SQL Server Integration Services Database SSISDB_

### 15.5 Managing the size of the SQL Server Integration Services Database SSISDB

###### Keeping SSISDB size to a minimum



1.


2.



To check the settings defined when SSISDB was installed, run the following query in SQL Server Management
Studio:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-128-0.png)

In the resultset, check the values of the following properties:






      - **OPERATION_CLEANUP_ENABLED** must be TRUE.

      - **RETENTION_WINDOW** can be adjusted to user requirements (the default is 365 days).
3. Change the setting of **RETENTION_WINDOW** by executing the following stored procedure (where ## is the

number of days):





4.


5.



This operation will not reduce the database size immediately. You need to launch an SQL maintenance job
called **SSIS Server Maintenance Job** . For example, you may want to start this job every day at midnight
(default setting).
Set the **Recovery Model** property to **Simple** before scheduling a data flow.


###### Important Recommendations













If you want to obtain the same result immediately, you may decide to execute the operation manually from SQL
Server Management Studio. However, the DB space will not be freed yet, particularly if the Full Recovery Model
has been set for the database. In that case, the log file size will become too large and will therefore need to be
managed by performing the typical operations included in the maintenance plan of any DB, such as backup,
truncation and shrink.
Changing the value of the **RETENTION_WINDOW** property may result in the deletion of a high number of
gigabytes from the database. In addition, if the Full Recovery Model has been set, the log file creation will be
carried out as well. As a consequence, the operation may require a lot of effort in both time and server

resources.
It may be advisable to perform this operation gradually or to plan a specific time window when the server can be
exclusively allocated to the execution of this procedure.
The SSISDB is a database that works as any other database. Therefore, any settings of the Autogrowth and Max
size on the SSISDB files must be configured keeping in mind the number of execution frequency of ETLs and the
configured retention window.





Opcenter Intelligence 2401.0001 - User Manual 129


_Example: Extending a SIMATIC IT LMS Entity_


_Managing the size of the SQL Server Integration Services Database SSISDB_

## 16 Example: Extending a SIMATIC IT LMS Entity


The following example describes how to extend a previously-created Solution which loads data from SIMATIC IT
LMS. In detail, the steps listed below will allow you to add the following columns to the **IndicatorValue** entity in
order to contextualize the **Equipment Performance** measures for Material Definitions and Operation Executions in
addition to standard contexts:








**MaterialDefinitionId**

**OperationExecutionId**


###### Prerequisites

A Solution with the following characteristics has been configured:









The Project contains the **Equipment Performance** functionality.
The **Equipment Performance** functionality of SIMATIC IT LMS has been selected as a source.
A Scenario has been configured for the Project.


###### Workflow



1.

2.


3.

4.


5.



Extend the **IndicatorValue** entity.
Align the scenario to the new project configuration loading the custom script corresponding to the extended
entity.
Deploy the Environment.
If necessary, load earlier data relative to the new entity from the source SIMATIC IT LMS database. If this
operation is not performed, the new entity will be automatically populated with more recent data as soon as the
first incremental load is executed, but earlier data will never be loaded. If you have deployed the Environment
for the first time, you can skip this step.
If you have configured at least a smart view and you want to use new columns to contextualize data, update the
view accordingly, deploy it again and then, only for physical views, reload data. For more information, see the
chapter of this manual on how to manage smart views.


###### Extending the IndicatorValue Entity



1.

2.

3.


4.

5.

6.


7.

8.



Open the Solution of interest and then click the **Projects** card.
Open the Project you have configured to load SIMATIC IT LMS data.
Select the **Entity Extensions** tab.


Click the **Create Entity Extension** button.
From the **Entity** drop-down list, select **IndicatorValue** .
Set the available parameters as follows:

![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-129-1.png)


Click **Add Column** .
Repeat steps from 7 to 8, adding a column with the following parameters:



130 Opcenter Intelligence 2401.0001 - User Manual


_Example: Extending a SIMATIC IT LMS Entity_


_Managing the size of the SQL Server Integration Services Database SSISDB_



9.


10.


11.

12.

13.



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-130-0.png)

Click **Save** .


Select the **IndicatorValue_Extension** tile and click **Open** .


Click the **Create Extension Source** button.

Select the SIMATIC IT LMS source that had been selected within the Project.
Click **Save** .


###### Loading the Custom Script



1.

2.

3.

4.


5.

6.

7.

8.


9.

10.



In the **Solutions** page, click the **Scenarios** card.
Open the Scenario of interest.
Open the Server of interest.
Open the source LMS database.


In the **Custom Scripts** page, click the **Create Script** button.
Select **Custom Model** from the **Models** drop-down list.
Select **IndicatorValue_Extension** from the **Model Entities** drop-down list.
Replace the text displayed in the **Entity Scripts** area with the following:



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-130-4.png)

Copy the following text in the **Delete Script** area:





Opcenter Intelligence 2401.0001 - User Manual 131


_Example: Extending a SIMATIC IT LMS Entity_


_Managing the size of the SQL Server Integration Services Database SSISDB_



![](mds/opint/v2401.0001/OpcenterIN_UserManual_images/OpcenterIN_UserManual.pdf-131-0.png)



11.



Click **Save** .


###### Deploying the Environment



1.


2.



In the **Environments** page, select the Environment.


Click **Deploy Environment** .


###### Loading Earlier Data



1.

2.


3.

4.

5.

6.

7.



Open the Solution and select the **Flows** card.
Select a flow.


Click **Run Single Entity** .
Select the previously deployed environment.
Specify a **Start Date** and an **End Date** to define the time interval for the data you want to load.
Select the **IndicatorValue_Extension** entity.
Click **Start** .



132 Opcenter Intelligence 2401.0001 - User Manual


