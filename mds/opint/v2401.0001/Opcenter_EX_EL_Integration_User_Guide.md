![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-0-0.png)
## Opcenter Execution Electronics 2404

# Integration User Guide

04/2024


PL20240130632793919


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



PL20240130632793919


20240409_151128



Copyright © Siemens AG 2024


Technical data subject to change


## Table of Contents

### 1 Overview.....................................................................................................................5 2 Mandatory Modeling..................................................................................................6 3 Summary Tables Data Collection..............................................................................9 4 PCB and Panel Container Types..............................................................................10 5 Handling Duration....................................................................................................11 6 Reporting Scrap and Trash......................................................................................12 7 Supported Transactions..........................................................................................14 8 DPU, DPO, and DPMO...............................................................................................15 9 Consumption Data Collection Setting ....................................................................18

Opcenter Execution Electronics 2404 - Integration User Guide iii


![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-3-0.png)



4 Opcenter Execution Electronics 2404 - Integration User Guide


_Overview_


## 1 Overview



![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-4-0.png)





Opcenter Execution Electronics (Opcenter EX EL) is a Manufacturing Execution System (MES) service that enables
Manufacturing Operations Management (MOM) capabilities.


Opcenter Intelligence Manufacturing Data Warehouse data model for Opcenter EX EL supports descriptive analysis
and KPIs to implement the following use cases business logic in Opcenter Intelligence.










Work in Progress (WIP) to show the progress of each work order, including the number of completed operations
and their average duration.
Material Traceability to provide information on boards, work orders and material placements.
Box Build to provide a map of a genealogy of all final product related subassemblies used to build a specific box
assembly node.



The instructions described in the following sections are prerequisites to load and analyze correct data from the
Opcenter EX EL source. These instructions are relevant for both Opcenter Intelligence for Cloud and Opcenter
Intelligence on-premise.


Opcenter Execution Electronics 2404 - Integration User Guide 5


_Mandatory Modeling_

## 2 Mandatory Modeling


It is important to complete this modeling before starting Opcenter Intelligence installation.



![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-5-0.png)




### Opcenter Execution Electronics Items Configuration

The following items need to be configured in Opcenter Execution Electronics:








Resources

Resource type




      
Equipment

      - Line

      - Area

 
Parent Resource — (Line)

 - Step

 - Product

 - BOM

 - Part number

 
Mfg order

 - Defect

 
Operation

 - Workflow

### Last Step Configuration in Workflow Modeling


To correctly visualize the WIP Dashboard issued by applying the corresponding Opcenter Intelligence Dashboard
Template, you must make sure to execute the following operation in Opcenter Execution Electronics. This setting is
required to correctly calculate the completion containers number for a Mfg. Order.


6 Opcenter Execution Electronics 2404 - Integration User Guide


1.


2.



_Mandatory Modeling_


In Opcenter Execution Electronics **Workflow Modeling** page, select the last operation in the **Workflow Diagram**
and click the **Modify Element** icon (outlined in blue below).

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-6-0.png)


In the **Step Details** panel that opens, select the **Is Last Step** check box and save.



![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-6-1.png)

Opcenter Execution Electronics 2404 - Integration User Guide 7


_Mandatory Modeling_


8 Opcenter Execution Electronics 2404 - Integration User Guide


_Summary Tables Data Collection_

## 3 Summary Tables Data Collection


To enable summary tables data collection, please do not uncheck the **Disable Reporting Summaries** field on the
**Factory** page. Data will not be written to the summary tables if this field is checked. The default setting is
unchecked, meaning summary tables are written to by default.

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-8-0.png)


Opcenter Execution Electronics 2404 - Integration User Guide 9


_PCB and Panel Container Types_

## 4 PCB and Panel Container Types


In order to get an accurate and full report of work-in-progress and material traceability, it is necessary to set the
appropriate container level types.

### ES_Level_Type


These are the **ES_Level_Types** that need to be defined:










PCB

Panel

Box assembly
Raw Material


### Panels and PCBs

When defining the Panel and PCB relationship:









Begin by defining the containers as having the **Std Start Child Qty** set to 1. In this case, the container level
defined for the container can use a **Level Type** of either ‘Panel’ or ‘PCB’.
If a **Child Container Level** is set, then the parent uses a **Level Type** of ‘Panel’, and the child must use a **Level**
**Type** of ‘PCB’.



10 Opcenter Execution Electronics 2404 - Integration User Guide


_Handling Duration_

## 5 Handling Duration


In order to get an accurate handling duration, in Operation level the **Use Queue** check box must be selected.
Otherwise, the handling duration will be calculated as the difference between the Move for operation _a_ and the
Move for the next operation.

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-10-0.png)


Opcenter Execution Electronics 2404 - Integration User Guide 11


_Reporting Scrap and Trash_

## 6 Reporting Scrap and Trash


There are two ways to mark boards for scrap in the Opcenter IN EL reports:








Using the Production Client
On the Container page


### Reporting Scrap and Trash using the Production Client



1.


2.


3.



To enable the **Scrap** button in the production client, first define the Loss reasons in the specifications or
operation modeling.
In the production client, click the **Scrap** button to scrap a container.

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-11-0.png)


In the next screen, add the reason for scrapping the container.



![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-11-1.png)
### Reporting Scrap and Trash on the Container page



1.



On the left menu bar, navigate to **Container** - **Change Qty** . By default, the **Change Type** of **Loss** is selected.



12 Opcenter Execution Electronics 2404 - Integration User Guide


2.


3.

4.


5.



_Reporting Scrap and Trash_


With this dialog open, either scan the container or manually fill in the values.

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-12-0.png)


In the **Loss Reason** field drop-down menu, select **Scrap** .
Select the **Use Current Qty** check box. You can also enter the number in the **Loss Qty** field. Make sure that for
the panel the number is higher than one.
Click **Submit** .



Opcenter Execution Electronics 2404 - Integration User Guide 13


_Supported Transactions_

## 7 Supported Transactions


The table below lists all the transaction types that are supported with Opcenter Intelligence.



![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-13-0.png)











![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-13-1.png)





14 Opcenter Execution Electronics 2404 - Integration User Guide


_DPU, DPO, and DPMO_

## 8 DPU, DPO, and DPMO


DPU, DPO, and DPMO are KPI metrics that express how your product or process is performing, based on the number
of defects.

### Definitions


**DPU – Defect per Unit** — the number of defects in a sample, divided by the number of units sampled.


DPU = [Number Of Defects]/[Container Count]


**DPO – Defects per Opportunities** — the number of defects in a sample, divided by the total number of defect
opportunities.


DPO = [Number Of Defects]/[Number of Opportunities (Latest Upgrade)]


**DPMO – Defects Per Million Opportunities** — the number of defects in a sample, divided by the total number of
defect opportunities, multiplied by one million.


DPMO = [Number Of Defects]/[Number of Opportunities (Latest Upgrade)] *
1,000,000


DPMO standardizes the number of defects at the opportunity level and is useful because you can compare
processes with different complexities.


The sub-metrics used for calculating the DPO, DPMO and PU are as follows:









**Number of Opportunities** — the number of chances for a defect to occur in a given product or service. The
number of opportunities is calculated as the sum of the number of part numbers on a container, the number of
pins on the container, plus the container itself.
Number of opportunities = number of parts + number of pins + 1


Where:


    
**Number of parts** is the number of components associated with the container. This is calculated based
on the tables **Product** and **ProductMaterialListItem** .

    - **Number of pins** is the total number of pins on the container, and is taken from the **ES_PinCount** field in

the **Product** table.

    - **Number of defects** is the number of defects reported. This number is taken from the

**DefectHistorydetail** table.
**Container Count** — the number of units counted for the given time period.














### Configuration

The number of opportunities for containers needs to be defined in the modeling stage.


Opcenter Execution Electronics 2404 - Integration User Guide 15


_DPU, DPO, and DPMO_


 **Number of pins** — The information for the pins is populated automatically during the NPI import, or can be

added manually from the product modeling.

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-15-0.png)


16 Opcenter Execution Electronics 2404 - Integration User Guide


_DPU, DPO, and DPMO_


 - **Number of Parts** — the number of parts specified in the BOM.

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-16-0.png)


Opcenter Execution Electronics 2404 - Integration User Guide 17


_Consumption Data Collection Setting_

## 9 Consumption Data Collection Setting


The sending of consumption data to Opcenter Intra Plant Logistics (IPL) is controlled by the **CIO Outbound Msg Def**
for the _ComponentIssue/ComponentIssueR2/ComponentReplace_ definitions – and by default they use the following
condition expression to control whether the message is sent:





![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-17-1.png)

This means that a Factory must be assigned the Employee performing the transaction, and the option must be
enabled. You could also remove the Condition Expression and the messages would always be sent.

![](mds/opint/v2401.0001/Opcenter_EX_EL_Integration_User_Guide_images/Opcenter_EX_EL_Integration_User_Guide.pdf-17-2.png)


18 Opcenter Execution Electronics 2404 - Integration User Guide


