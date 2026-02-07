![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-0-0.png)
## Opcenter Reporting 2401.0001

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


20240409_161610



Copyright © Siemens AG 2024


Technical data subject to change


## Table of Contents

###### 1 Before you Start .....................................................................................................5 2 How to Manage Access Control.............................................................................7

2.1 Configuring Users and Roles .......................................................................................................7


2.2 Checking License Seats................................................................................................................8

###### 3 Quick Start to Using Opcenter Reporting .............................................................9 4 How to Create a Data Source...............................................................................10


4.1 Creating a SQL Server Data Source...........................................................................................10


4.2 Creating an Oracle Data Source ................................................................................................12


4.3 Importing Custom Relations .....................................................................................................12


4.4 How to Create Custom Entities .................................................................................................13


4.4.1 Creating a Custom Entity......................................................................................................................................... 14


4.4.2 Editing a Custom Entity ........................................................................................................................................... 14

###### 5 Creating Folders...................................................................................................16 6 How to Create Reports.........................................................................................17


6.1 Adding Reports...........................................................................................................................17


6.2 Authoring Reports......................................................................................................................18


6.2.1 Limitations ............................................................................................................................................................... 18

###### 7 Cloning Reports....................................................................................................20 8 Moving Reports to a Different Folder..................................................................21 9 Editing Data Sources............................................................................................22 10 Exporting or Importing Reports ..........................................................................23 11 How to Embed Reports in a Custom Application ...............................................24


11.1 SWAC Integration Methods........................................................................................................24


11.2 Embedding Reports in a Custom Application...........................................................................28


Opcenter Reporting 2401.0001 - User Manual iii


![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-3-0.png)



4 Opcenter Reporting 2401.0001 - User Manual


_Before you Start_

## 1 Before you Start

###### Accessing the Application


For security reasons, the first access to Opcenter Reporting is only granted to the user who has been configured in
Opcenter Reporting under the **Insert the UMC user who will have the Administrator role for Opcenter**
**Reporting** section.


This user must perform the following operations:



1.


2.



Double-click the Opcenter Reporting desktop icon.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-4-0.png)

Assign roles to other users in the Access Control page.






###### The Home Page

The **Home** page is made up of the following cards. Some of the cards may be displayed or not depending on the role
of the logged-in user.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-4-1.png)


###### The Primary Navigation Bar

The Primary Navigation Bar is displayed on the left-hand side of each page and includes the following commands:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-4-2.png)



Opcenter Reporting 2401.0001 - User Manual 5


_Before you Start_

![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-5-0.png)

###### User Commands


When you click a panel opens, where you can execute the following operations. You can pin or unpin the panel
to the current page.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-5-1.png)








###### Page Visualization Modes

The pages where items are saved and managed can be displayed in the two following modes:









**List with Summary** : the list of existing items is shown on the left-hand side of the page. When you select an
item, details about it are shown in the **Overview** section in the right-hand side of the page.
**List** : only the list of existing items in alphabetical order is displayed.


###### Naming Convention

When you name an item, you must follow these rules:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-5-2.png)



















6 Opcenter Reporting 2401.0001 - User Manual


_How to Manage Access Control_


_Configuring Users and Roles_


## 2 How to Manage Access Control

###### Accessing the Page

To access the **Access Control** page, click the **Access Control** card in the **Home** page.




###### Available Operations








Configure users and roles
Check the number of available seats for the existing users


### 2.1 Configuring Users and Roles

In this page you can grant users access to the Opcenter Reporting application functionalities by assigning them a
predefined role.

###### Procedure



1.

2.


3.


4.


5.



In the **Access Control** page, click **Add user or group** .
In the **Add user or group** panel, insert the user or group name in the format used during User Management
Component configuration. For more details, see _Opcenter Reporting Installation Manual_ .



Select the **Can perform administrative functions** check box if you want this user to have the permission of
assigning roles to users and manage data sources.
Select one of the following roles:

![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-6-3.png)


Click **Save** .





Opcenter Reporting 2401.0001 - User Manual 7


_How to Manage Access Control_


_Checking License Seats_

### 2.2 Checking License Seats


This page shows the number of total and available seats for each role and each user. Seats correspond to the
number of users that can access the application at the same time, depending on the type of license you have
purchased. A seat is consumed for each logged-in user, unless this user has been assigned the **No role** role in the
**Access Control** page.

###### Checking the number of available seats


In the **License Management** tab, check the following information:

![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-7-0.png)

###### Releasing Seats


Seats are released only when:








You log out of Opcenter Reporting by clicking the **Logout** button.
The session expires due to user inactivity (maximum inactivity duration is 120 minutes).




##### Updating the license

If you have updated your license, for example to add more seats, perform the following operations:



1.

2.



Click **Reload license information** to update the application with the information about the new license.
Update the license server: for more details see _Opcenter Reporting_ _Installation Manual_ .



8 Opcenter Reporting 2401.0001 - User Manual


_Quick Start to Using Opcenter Reporting_


_Checking License Seats_

## 3 Quick Start to Using Opcenter Reporting


This workflow provides a general outline of the main steps that must be executed to use Opcenter Reporting.

###### Workflow



1.

2.

3.

4.



Create Data Sources

Create Folders

Create Reports
Author Reports


###### Additional Operations

**On Reports**









Clone Reports
Export or Import Reports
Embed Reports in a Custom Application



**On Data Sources**







Create Custom Entities


###### Batch Operations








Move Reports to a Different Folder
Edit Data Sources



Opcenter Reporting 2401.0001 - User Manual 9


_How to Create a Data Source_


_Creating a SQL Server Data Source_

## 4 How to Create a Data Source


In this step, authorized users can define the Siemens MOM sources that supply data for reports by creating data
source connections to be used when they create a report.




###### Accessing the Page

To access the **Data Sources** page, click the **Data Sources** card in the Home page.

###### Available Operations


You can create two types of data sources depending on your requirements and on the data management system
installed on your machine. If both SQL Server and Oracle systems are present, this option is marked by a small


triangle on the left side of the command.








Create a SQL Server Data Source
Create an Oracle Data Source


###### Additional Operations on Data Sources

On existing data sources you can perform a number of additional operations. The toolbar is displayed on the right
side of the page and includes the following commands:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-9-2.png)


### 4.1 Creating a SQL Server Data Source

Follow this procedure to create a data source for a Siemens MOM product using a SQL Server database.


10 Opcenter Reporting 2401.0001 - User Manual


_How to Create a Data Source_


_Creating a SQL Server Data Source_


###### Procedure



1.

2.


3.



In the **Data sources** page, click **Create data source** .
In the **Create a SQL Server data source** panel, insert the following details:

![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-10-1.png)


Click **Save** .



Opcenter Reporting 2401.0001 - User Manual 11


_How to Create a Data Source_


_Creating an Oracle Data Source_

### 4.2 Creating an Oracle Data Source


Follow this procedure to create a data source for a Siemens MOM product using an Oracle database.

###### Procedure



1.

2.

3.


4.



In the **Data sources** page, click **Create data source** .
Select the **Create an Oracle data source** option from the drop-down menu.
In the **Create an Oracle data source** panel, insert the following details:

![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-11-1.png)


Click **Save** .


### 4.3 Importing Custom Relations

The Designer automatically recognizes the relations natively present in the database. If you need to define further
relations which are not present, you can use the **Import custom relations** command.


To perform this operation, you need to define a script in which the relation between parent and child entities is
defined. This relation can be applied to more than one field. Relations can refer to tables or views.

###### Prerequisites


You have defined the custom relation script.

###### Procedure


12 Opcenter Reporting 2401.0001 - User Manual


_How to Create a Data Source_


_How to Create Custom Entities_



1.


2.

3.


4.



In the **Data sources** page, select an existing data source.


Click **Import custom relation** .
In the **Custom relation script** area, insert the script (see an example below).



Click **Save** .




###### Example of custom relation script



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-12-3.png)


### 4.4 How to Create Custom Entities

You can define custom queries in order to expose new data sets in the Designer. When you create a report using the
Designer, the custom entities you have created will be included in the list of available tables and views.

###### Accessing the Page


To access the **Custom entities** page, in the **Data sources** page select the data source for which you want to create a


custom entity and click .

###### Workflow



1.

2.



Create a custom entity
Edit a custom entity


###### Additional Operations on Custom Entities

On existing custom entities you can perform a number of additional operations. The toolbar includes the following
commands:


Opcenter Reporting 2401.0001 - User Manual 13


_How to Create a Data Source_


_How to Create Custom Entities_

![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-13-0.png)

#### 4.4.1 Creating a Custom Entity

###### Prerequisites


You have created a data source.

###### Limitations


You cannot use custom entities within a custom relation script.

###### Procedure



1.

2.

3.



In the **Custom entities** page, click **Create custom entity** .
In the **Create custom entity** panel, insert a meaningful name for the custom entity.
Click **Save** .


#### 4.4.2 Editing a Custom Entity

###### Prerequisites

You have created a custom entity.

###### Procedure



1.


2.

3.


4.


5.



In the **Custom Entities** page, select a custom entity.


Click **Edit** .

Build your query starting with the SELECT statement. For your statement to be valid, you must be able to
include it within another statement, for example:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-13-2.png)

If the script is valid, click **Save** .




###### Server-side Filtering and Sorting

Server-side filtering and sorting can be performed. The supported keywords for filtering are:


14 Opcenter Reporting 2401.0001 - User Manual


_How to Create a Data Source_


_How to Create Custom Entities_

























= <= => <>

not

and or

isnull

startswith

endswith

contains

dateinrange
numinrange
LEN

MID$
LEFT$
RIGHT$

YEAR

MONTH

DAY

UPPER$
LOWER$

EMPTY


###### Example of Custom Entity

![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-14-0.png)

Opcenter Reporting 2401.0001 - User Manual 15


_Creating Folders_


_How to Create Custom Entities_

## 5 Creating Folders


In this step, you can create folders to organize and manage your reports. Folders can be created in the root folder or
within any other folder.

###### Accessing the Page


To access the **Reports** page, click the **Reports** card in the Home page.

###### Procedure



1.

2.

3.


4.

5.



In the **Reports** page, select **Create** .
Select the **Create folder** option from the drop-down menu.
In the **Create folder** panel, insert the following details:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-15-1.png)

Click **Create** .
Repeat steps 1 to 4 to create more folders. You can also create folders within another folder. To do so, select


a folder and click **Open** near the folder name, then repeat steps 1 to 4.




###### Additional Operations on Folders

On existing folders you can perform a number of additional operations. The toolbar is displayed on the right side of
the page and includes the following commands:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-15-3.png)



16 Opcenter Reporting 2401.0001 - User Manual


_How to Create Reports_


_Adding Reports_


## 6 How to Create Reports

###### Accessing the Page

To access the **Reports** page, click the **Reports** card in the Home page.

###### Workflow



1.

2.



Add a Report
Author a Report using Combit® List & Label Designer


###### Additional Operations on Reports

On existing reports you can perform a number of additional operations. The toolbar is displayed on the right side of
the page and includes the following commands:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-16-0.png)




### 6.1 Adding Reports

In this step you can create reports either in the root folder or from within another existing folder.

###### Procedure



1.

2.



In the **Reports** page, select **Create** and the **Create report** option from the drop-down menu.
In the **Create report** panel, insert the following details:



Opcenter Reporting 2401.0001 - User Manual 17


_How to Create Reports_


_Authoring Reports_



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-17-0.png)



3.



Click **Create** . The newly-created report is added to the list of folders and reports on the left-hand side of the
page. New reports are marked with a red icon, which means that they need to be edited with the Designer
tool.


### 6.2 Authoring Reports

After you have created a report, you need to design its structure and choose how to show the information that
originates either from a database or another data source. To this end, you can use Combit® List & Label Designer.




##### Prerequisites

The Combit® List & Label Designer must be installed on your local machine. The first time you want to design a
report, you can download the executable file to be launched for the tool installation.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-17-2.png)




###### Procedure



1.


2.

3.

4.



Select a report.


Click **Open Report using Report Designer** .
Click **Open Web Designer** .
Create a report using the Designer according to your requirements.


###### Result

After a report has been designed and saved, it is marked with a green icon. To view it in Opcenter Reporting


environment, click **Open** on the report.




#### 6.2.1 Limitations

There are limitations set by the target format. The most important are:


18 Opcenter Reporting 2401.0001 - User Manual


_How to Create Reports_


_Authoring Reports_


Rows that are anchored to each other are not correctly exported.
Overlapping objects (except rectangles) are not supported.
Rectangles cannot have any frames. Transparent rectangles will be ignored.
Decimal tabs will be transformed to right-aligned tabs.
Any other tabs will be transformed to a blank.
'Paragraph spacing' and 'Line distance' in text objects are not supported.
The option 'Line break' in text objects and table columns is always active in the export result.
The option 'Separators fixed' in table objects is not supported.
The left offset in the first column of a table line will be ignored.
The list object option "fixed size" is not supported.
The chart object is exported as a picture and thus cannot appear transparently.
The transformation of RTF text to HTML code is carried out by an RTF parser. This parser interprets the basic
RTF formatting. Extended RTF functionality such as embedded objects will be ignored.
Rotated RTF text is not supported.
Spacing before table lines is not supported.
Horizontal and vertical lines are exported as images; all other lines are ignored.
Gradient fills are not supported.
Rotated text (RTF and plain) is not supported.
Custom drawings in callbacks are not supported.
Objects to be exported as picture should not overlap the object frame.
Table frames of neighboring cells are not drawn so that they overlap each other, but discretely. This can
double the frame width and needs to be taken into account during the design.
Offset of table lines is not supported.
TotalPages$() may not be used in rotated text objects.
Shadow Pages are not supported.
The wrapping option 'Minimum Size' in the crosstab object is not supported.
The property "Link" is not supported.



The following tags or attributes superseding HTML 4.01 standard will be used:









Ending the page frame for HTML pages will use browser specific tags.
Setting line color for the table grid (<table BORDERCOLOR="#ff0000">) is browser specific.
Setting line color for horizontal table lines (<hr COLOR="#ff0000">) is browser specific.



If the HTML object is not exported as picture but as HTML text, the part of the stream between the <body> and </
body> tags will be embedded. This by definition leads to the following limitations:














Cascading Style Sheets are not completely supported.
Page formatting such as background color, margins etc. is lost.
HTML does not allow scaling. The exported result may thus differ from the layout in the Designer, especially
when the HTML object contains the contents of a whole website.
Even if the HTML object wraps over several pages, it will be exported in one stream, i.e. no page wrap will

occur.
Embedded scripting functionalities may be lost.
Issue print is not supported.





Preserving the text rendering in XHTML while activating the "shrink" option for text is not supported. XHTML has a
number of restrictions compared to other formats as there are not always corresponding CSS styles to support
certain features. Automatically shrinking font sizes to match a given box is one of them. While there are
workarounds like viewport based font sizes or script based DOM manipulations, there is no secure way that works
equally well in all scenarios and browsers. Thus, usage of the shrink option is discouraged when printing to XHTML.


Opcenter Reporting 2401.0001 - User Manual 19


_Cloning Reports_


_Authoring Reports_

## 7 Cloning Reports


Follow this procedure to create the copy of an existing report. You can clone either reports that have already been
authored using the Designer tool (marked with a green icon) or reports that have not yet been edited (marked with
a red icon).

###### Procedure



1.

2.



In the **Reports** page, select the report you want to copy and click **Clone Report** .
A new report named < _Report name_1_ - is automatically created in the same folder.



20 Opcenter Reporting 2401.0001 - User Manual


_Moving Reports to a Different Folder_


_Authoring Reports_

## 8 Moving Reports to a Different Folder


Once you have created a report, either in the root folder or within another folder, you can move it to another folder
to better organize your reports.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-20-0.png)




###### Procedure



1.

2.


3.



Select the report you want to move and click **Move** .
In the **Move items to folder** panel, the folders tree is shown. Select the folder where you want to move the
report.
Click **Move** and then **Confirm** .



Opcenter Reporting 2401.0001 - User Manual 21


_Editing Data Sources_


_Authoring Reports_

## 9 Editing Data Sources


You can modify the data source for an existing report or for more than one reports at the same time.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-21-0.png)


###### Procedure



1.


2.

3.

4.



In the **Reports** page, select one or more reports for which you want to modify the data source.


Click **Edit data source** .

In the **Edit reports data source** panel, select the new data source from the drop-down menu.
Click **Save** .



22 Opcenter Reporting 2401.0001 - User Manual


_Exporting or Importing Reports_


_Authoring Reports_

## 10 Exporting or Importing Reports


You can export and import reports, but remember that reports are unique within the system: therefore you cannot
reimport a report you have previously exported if you have not previously deleted the report in your system.
For example, if you have exported one or more reports in a .zip file you cannot reimport them (neither by changing
their name nor by creating a new folder) unless you have deleted them from the system.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-22-0.png)




###### Limitations

The images used in reports are not exported nor imported with the reports. As a result, after you have imported a
report, you must open it and add the missing images again.

###### Exporting Reports



1.


2.

3.



In the **Reports** page, select one or more reports from the required folder. To select more reports, press the
SHIFT key.


Click **Export** .
A .zip file containing the exported reports is downloaded by the system. The reports are saved in:
**ProgramData\Siemens\Opcenter\Intelligence\Report\Server\App_Data\**


###### Importing Reports



1.

2.

3.

4.

5.



In the **Reports** page, click **Import** .
In the **Import report** panel, browse for the file(s) to be imported.
From the drop-down list, select an existing data source.
Select the folder where you want to store the imported report(s).
Click **Import** .



Opcenter Reporting 2401.0001 - User Manual 23


_How to Embed Reports in a Custom Application_


_SWAC Integration Methods_

## 11 How to Embed Reports in a Custom Application


You can embed the Opcenter Reporting reports directly into your custom application using the Siemens Web
Application Collaboration (SWAC) library.


For more information on the SWAC Library, see _SWAC_ _Documentation_, available at https://code.siemens.com/swac/
sdk/development/-/tree/master/documentation




##### Prerequisites










The SWAC Library has been imported. For more information on how to import and integrate a SWAC
component in a Siemens Web Framework (SWF) project, see _SWAC Documentation_ .
You have used User Management Component (UMC) authentication to log in to Opcenter Reporting.
You have created at least one report in Opcenter Reporting.



For information on other SWAC prerequisites, see _SWAC Documentation_ .

###### Available Operations








Integration Methods
Embed Reports


### 11.1 SWAC Integration Methods

The SWAC Component provides the following methods to retrieve the folder tree hierarchy and the report list.

###### getFolderStructure()


Retrieves the folder tree hierarchy in Opcenter Reporting.


The return type is for example:



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-23-1.png)



24 Opcenter Reporting 2401.0001 - User Manual


_How to Embed Reports in a Custom Application_


_SWAC Integration Methods_


}

]

}

]

},
{
"RepositoryItemId":"fb0b4b8c-f6eb-43db-bc88-6f3766f163de",
"Name":"TEST Custom Entities",
"Children":[

]

},
{

"RepositoryItemId":"74496140-e613-4e5d-89c8-3bae93189975",
"Name":"TEST Custom Entities Easy",
"Children":[

]

},
{
"RepositoryItemId":"bdecabbd-af79-44aa-b8df-0820c63c9e35",
"Name":"TEST Custom Entities Northwind",
"Children":[

]

},
{
"RepositoryItemId":"d00044e9-2864-4f56-ae89-426d617152c1",
"Name":"TestImage",
"Children":[

]

},
{
"RepositoryItemId":"584bdc3a-e7ef-42db-b463-6c24b98f292c",
"Name":"FOLDER",
"Children":[

]

},
{

"RepositoryItemId":"37b346ca-82b2-4859-917d-a55ecb7c2b83",
"Name":"ReferenceReport",
"Children":[

{
"RepositoryItemId":"6e344501-19d2-4b9e-b145-de81e3adaf6f",
"Name":"SQLSERVER",
"Children":[

]

},
{
"RepositoryItemId":"7aff6dcb-5a23-4b3a-9d31-82ef002f0ca5",


Opcenter Reporting 2401.0001 - User Manual 25


_How to Embed Reports in a Custom Application_


_SWAC Integration Methods_



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-25-0.png)




###### getReportsList(parentItemId)

Shows the list of items (reports/folders) included in a folder.


The **parentItemId** argument is the **Item Id** of the folder where the reports you want to display are contained.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-25-1.png)



26 Opcenter Reporting 2401.0001 - User Manual


_How to Embed Reports in a Custom Application_


_SWAC Integration Methods_



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-26-0.png)



Opcenter Reporting 2401.0001 - User Manual 27


_How to Embed Reports in a Custom Application_


_Embedding Reports in a Custom Application_




###### getReportCbId(itemId, parentItemId)

Returns the **CbId** if you input the **ItemId** and **ParentItemId** that can be retrieved using the previous methods.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-27-1.png)




###### setRepositoryId(itemId, reportQueryParams)

Loads the report into the SWAC Component. You have to input the **repository Id**, which is the **CbId** of the report,
and the **reportQueryParams** . For the latter, null or empty values are accepted. If some parameters have been
configured for the report, the following types are allowed:











**string**
**date** : JSON format ISO 8601

**bool** : true or false
**numeric** : using decimal point as separator
**array** : separated by **;**



**Example**


Create a report that contains the parameters:









**@EmployeeID**
**@City**
**@BirthDate**



In List & Label Designer, set the visibility of these parameters to **False** .
Pass the **reportParams** argument as in this example:




### 11.2 Embedding Reports in a Custom Application

###### Procedure



1.


2.



Create an HTML file and refer to the SWAC libraries. You can use script tags in HTML to add references.



![](mds/opint/v2401.0001/Opcenter_Reporting_UserManual_images/Opcenter_Reporting_UserManual.pdf-27-3.png)

Configure the necessary SWAC library properties. Example: SWAC.Config.LevelLog = 1;
SWAC.Config.TimeOuts.Enabled = false.





28 Opcenter Reporting 2401.0001 - User Manual


3.


4.

5.

6.


7.


8.



_How to Embed Reports in a Custom Application_


_Embedding Reports in a Custom Application_


(Optional) Specify the path of the SWAC base library, which permits the execution of SWAC code and
communication between SWAC container and SWAC component. Example:
SWAC.Config.Container.URLs.BaseLibrary = < _URL_ Initialize the SWAC component object by configuring the necessary properties.
Create the SWAC component by calling the **beginCreate** method in the SWAC library.
Subscribe to the **onReady** event to call exposed SWAC component methods. Only after the **onReady** event
has been fired, it is possible to call all the SWAC component methods.
Fetch the SWAC component object by component name and call the necessary method exposed by the
SWAC component.
In the callback function, use the **beginShow** ( **true** ) method to display the SWAC component.





Opcenter Reporting 2401.0001 - User Manual 29


