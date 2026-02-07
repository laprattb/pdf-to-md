![](mds/opint/v2401.0001/OpcenterIN_ProductOverview_images/OpcenterIN_ProductOverview.pdf-0-0.png)
## Opcenter Intelligence 2401.0001

# Product Overview

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


20240409_163146



Copyright © Siemens AG 2024


Technical data subject to change


## Table of Contents

###### 1 Introduction to the Journey ................................................................................ 6 2 Where Are We Starting From and Where are We Going? .................................... 7

2.1 What is the Manufacturing Operations Management?.............................................................7


2.2 What is Business Intelligence?...................................................................................................8


2.3 What is a Data Warehouse? .....................................................................................................10


2.4 What are Measures and KPIs?..................................................................................................10


2.5 What is a Star Schema?............................................................................................................10


2.6 What is Scale Up? .....................................................................................................................10


2.7 What is a Columnstore Data Engine? ......................................................................................11


2.8 What is an Analytical Tool?......................................................................................................11


2.9 What is Operational Reporting? ..............................................................................................11

###### 3 What is Opcenter Intelligence Composed of?................................................... 12 4 What is Opcenter Reporting Composed of?...................................................... 13 5 Overview of Opcenter Intelligence Main Components .................................... 14 6 Who are we traveling with? ............................................................................... 15 7 Deep Dive into Opcenter Intelligence Concepts............................................... 16


7.1 What is a Manufacturing Analytical Model?............................................................................16


7.2 What is an Opcenter Intelligence Solution?............................................................................16


7.2.1 What is a Project?...................................................................................................................................................16


7.2.1.1 What are Functionalities?......................................................................................................................................17


7.2.1.2 What are Sources?..................................................................................................................................................18


7.2.1.3 What are Extensions?.............................................................................................................................................18


7.2.1.4 What are Schedules?..............................................................................................................................................18


7.2.2 What is a Smart View..............................................................................................................................................18


7.2.2.1 Smart View Types...................................................................................................................................................19


7.2.2.2 Smart View Measures and Attributes....................................................................................................................19


7.2.2.3 Smart View Contexts..............................................................................................................................................20


7.2.2.4 Smart View Deploy.................................................................................................................................................20


7.2.3 What is a Scenario? ................................................................................................................................................20


7.3 What are Opcenter Reporting Concepts? ...............................................................................21


7.3.1 Reports ...................................................................................................................................................................21


7.3.2 Data Sources ..........................................................................................................................................................22


Opcenter Intelligence 2401.0001 - Product Overview iii


7.3.3 Custom Relations...................................................................................................................................................22


7.3.4 Designer..................................................................................................................................................................22


7.3.5 Custom Entities......................................................................................................................................................22


iv Opcenter Intelligence 2401.0001 - Product Overview


![](mds/opint/v2401.0001/OpcenterIN_ProductOverview_images/OpcenterIN_ProductOverview.pdf-4-0.png)



Opcenter Intelligence 2401.0001 - Product Overview 5


_Introduction to the Journey_

## 1 Introduction to the Journey


In this guide you will discover Opcenter Intelligence (Opcenter IN) through increasingly in-depth steps, starting
from a general architectural overview to the description of the single components that make it up.
You are going to learn how this product fits into the latest technological innovations and proposes a highly flexible
and extensible solution to retrieve data from heterogeneous systems, which can either be members of the Opcenter
family or third-party products.


This guide does not aim to describe how operations can be performed, or how things are developed, or how the
system can be installed and configured. It rather wants you to discover what can be achieved and through which
technologies.

###### Who is coming with us on the journey?


This document has been written for business analysts and software architects who are in charge of making
important evaluations or decisions about business solutions, process methodologies and technological changes.


6 Opcenter Intelligence 2401.0001 - Product Overview


_Where Are We Starting From and Where are We Going?_


_What is the Manufacturing Operations Management?_

## 2 Where Are We Starting From and Where are We Going?


Let’s start with an overview on the destination of our journey: where is Opcenter Intelligence heading, what are the
latest market changes and needs and which manufacturing trends does it fit into.
As a consequence of the deep influence of the latest technologies and trends on the business landscape, a more
flexible solution is required to satisfy new customer requirements.
Flexibility means that our product must be able to interface with different technologies, which might rapidly
change, and give the users the chance to easily customize the product so that it always stays in line with the
manufacturing reality.


In this journey step we will concentrate on:











The manufacturing software trends that drive software design and the concept of Manufacturing Operations
Management (MOM).
All the functionalities required to develop, deploy and maintain an Opcenter Intelligence Solution, in order
to analyze manufacturing data according to standard and custom analytical contexts.
The main concepts and features applied to provide a business intelligence ecosystem, where you can easily
manage and analyze structured data and where the main ingested MOM data can be displayed and analyzed
thanks to Opcenter Intelligence Solution Management.


### 2.1 What is the Manufacturing Operations Management?

To meet the latest software manufacturing trends, Siemens delivers a product based on a core of business
operations and entities that can be modularly used and combined to model your IT manufacturing plant. These
operations are identified as Manufacturing Operations and are used to model a custom logic that effectively
interacts with Manufacturing Execution System (MES) level.


Manufacturing Operations Management (MOM) can be viewed as a manufacturing software layer which is placed on
top of the traditional MES layer. This additional layer is designed to be highly configurable and flexible in order to
quickly adapt to the rapid business changes required by the new plant models.


Opcenter Intelligence delivers a solution to analyze MOM data. This solution is deeply integrated with MES systems.

###### From Manufacturing Execution Systems (MES) to MOM Systems


In the early Nineties, industries acknowledged the need for a layer to integrate and link Business Systems with
Control Systems. The term Manufacturing Execution Systems (MES) has been used from the start to specify all those
functions and products that satisfy this need.


Initially, MES indicated an area where almost every application or product could not be clearly assigned to either
the Business System or the Control System layer. Most of these products were spin-offs of applications developed
by a System Integrator for a particular customer and were generally focused on a very specific area (for example,
scheduling, laboratory, quality or tracking).


After some time, international organizations realized that a clearer definition of MES was required: MESA
(Manufacturing Enterprise Solutions Association) and, as a consequence, ISA (Instrumentation System and
Automation Society) later developed models that describe these levels and seek to standardize them.


Opcenter Intelligence 2401.0001 - Product Overview 7


_Where Are We Starting From and Where are We Going?_


_What is Business Intelligence?_

![](mds/opint/v2401.0001/OpcenterIN_ProductOverview_images/OpcenterIN_ProductOverview.pdf-7-0.png)


Under the pressure of new business-driving forces that have been emerging in recent decades, Manufacturing
Plants continue to play a major role. The globalization of both companies and production processes makes it
necessary to create new models. Manufacturing is not a process that can be completed by a single self-enclosed
entity, but extends beyond the bounds of the plant, the country and the business enterprise.


Therefore, MES cannot act simply as an interface between Business and Process layers, but requires a substantial
number of functions that are crucial to a Company’s success. Rather than remaining distinct from one another,
connected solely by a data exchange layer, these functions need to be coordinated, in adherence to the Business
and Production strategy.


ISA-95 documents point this out very clearly, describing the MES process in terms of both data and interaction
between functions (for example, Order Dispatching or Resource Management).


The result is a new approach to MES, based on an architecture that makes it possible to describe business processes
that orchestrate functionalities provided by a set of specialized and affordable components.


At the same time, this orchestration must also involve the automation and control level, thereby making both MES
and control part of the same collaborative production management system.


Many early MES systems were not sufficiently configurable and flexible to quickly adapt to the changes of business
models brought about by new market conditions. Consequently many vendors tried to differentiate themselves
from MES by adopting the new Manufacturing Operations Management (MOM).


Manufacturing Operation Management (MOM) can be described as an approach which oversees all aspects of the
manufacturing process, with a particular focus on increasing efficiency.


This approach aims to orchestrate all those activities that establish work unit definition and control, in the form of
workflow or recipe control, to produce the desired end products. MOM systems, as a development of MES systems,
analyze work data, maintain records and optimize the production process.


Service orientation offers great benefits to the retail enterprise in incrementally changing systems to meet business
demands.

### 2.2 What is Business Intelligence?


Managers need to make quick and effective decisions, and to do this they need the right information at the right
time, but they are often overwhelmed by data, which is scattered across different sources. For quick and effective
decision-making, data must be:







integrated into one place (a data warehouse)



8 Opcenter Intelligence 2401.0001 - Product Overview


_Where Are We Starting From and Where are We Going?_


_What is Business Intelligence?_







turned into clear and actionable information.



Business Intelligence systems typically supply dedicated client-side tools, which make easier the navigation
between data and make analysis easy for non-technical users. One of the features of a BI system are for example
dashboards, which provide an at-a-glance overview of key business data.


The general styles of Business Intelligence reporting are:















Self-Service Analysis: it is dedicated to non-technical users that want to integrate data from different
sources and perform drill-down operations in order to find the reason of data anomalies. It does not require
a fixed-form reporting and analysis system, and consequently no IT involvement.
Business Reporting: it is based on a set of formatted reports showing consolidated corporate data. These
reports are created by advanced business users or analysts that are shared with managers and teams. In this
case, the IT involvement is moderate.
Operational Reporting: it is similar to the Business Reporting style, but is it based on fixed-format reports
created and managed by IT. The main characteristics of this style are: consistency, scalability, manageability
and automated distribution.
Performance Monitoring: it is based on dashboards that allow executive users to monitor the business
performances, providing them with an at-a-glance visibility on the business status.
Scorecarding: it is based on a set of KPIs, meaningful for the business activity, which are measured against
predefined targets. If necessary, this style can also be used to evaluate operational performances, but it
usually belongs to a performance management program.


###### What is manufacturing intelligence?

In today’s economic environment manufacturers are under constant pressure to optimize plant performance and
consequently to reduce operating costs.
To accomplish this objective many manufacturers have installed Manufacturing Execution Systems (MES) that have
proven to streamline production processes and facilitate the flow of information between the shop-floor and the
rest of the enterprise.
As a result, every day Manufacturing Execution Systems process a very large amount of data. But, typically, this data
is difficult to interpret, and must be accessed and transformed thus becoming understandable and actionable to
users in a format they can use to optimize operations.


Manufacturing intelligence transforms plant floor data into key performance indicators and metrics that managers
use to monitor and improve the manufacturing operations performance.
In this way, manufacturing Intelligence enables manufacturers to close the performance loop by gaining visibility
across the production, inventory, assets and quality management aspects of manufacturing operations.


A manufacturing intelligence system enables close-loop performance management by:













Aggregating data gathered from many sources.
Contextualizing the data through a data model that will help users find what they need.
Providing appropriate analytics that enable users to analyze data across sources and especially across
production sites.
Providing tools to create visual summaries of the data to alert decision makers and call attention to the most
important information of the moment.
Automating the transfer of the collected data from the plant-floor up to business systems such as SAP.



The main benefits of manufacturing Intelligence are:











More Intelligence; Integration of analytical and visualization tools makes possible to monitor data in real
time and inform appropriate decision-makers in case of non-conforming incident.
Less Variability; Using manufacturing intelligence systems, manufacturers can better understand sources of
variability in their production process and operate to improve process stability, plant capacity, and quality
compliance.
Less Costs; Reducing variability in the production process manufacturers can decrease operating costs.



Opcenter Intelligence 2401.0001 - Product Overview 9


_Where Are We Starting From and Where are We Going?_


_What is a Data Warehouse?_

### 2.3 What is a Data Warehouse?


A Data Warehouse is a repository that contains the data of a company or organization and is used to easily produce
analysis and relations to support business decision-making.


In our context, the structure of the data warehouse conforms to international standards such as ISA-95 and is
moving toward Industry 4.0 models.


This repository collects most relevant business data from the data model. It stores business information instead of
detailed production data to allow the personnel responsible for plant and line operations to easily access business
reports, providing constantly updated information.


Data provided by Siemens and third-party products can be read, injected or stored in the data warehouse by means
of miscellaneous data processing systems, such as stream processing or the ETL (Extract, Transform and Load)
system to update data model implementation and fit the data model of new data.


Data can also be exposed in order to enable KPI reporting and advanced analytical functions.

### 2.4 What are Measures and KPIs?


KPIs (Key Performance Indicators) are defined as quantifiable and strategic measurements that reflect the critical
success factors of each organization. They are calculated comparing a measure against a target.
The main concepts relative to KPIs are the following:









Measures (or Facts), which are properties that identify numeric values contained in the fact tables to provide
the user with quantitative evaluations of business events (for example Produced Quantity, Scraps, Broken
Bottles etc.). Measures can be combined in a formula to define other measures. Measures can only be
expressed by numbers.
Dimensions, which represent production entities that are typically used to contextualize the Facts (for
example Equipment, Shifts, Products, Orders etc.). Dimensions show how the user wants to analyze data.
They are always expressed by strings and can also be called contexts or attributes.


### 2.5 What is a Star Schema?

From a functional perspective, a star schema can be defined as a model used to organize information in a data
warehouse for the purpose of allowing information to be viewed from many perspectives. The middle of the star
consists of the basic, factual information. The points of the star represent various perspectives from which the
factual information can be viewed.
From a technical point of view, a star schema is a database design that consists of: a fact table, which contains
measurable, quantitative data about the business, and two, or more, dimension tables, which contain descriptive
attributes. Each dimension table has a single field primary key (PK) which has a one-to-many relationship with a
foreign key (FK) in the fact table.

### 2.6 What is Scale Up?


Vertical Scaling (Scale-up) refers to adding more power (processors and RAM) to an existing computer. It can
improve the capabilities of a node or a server by giving greater capacity to the node but does not decrease the
overall load on existing members of the cluster. That is, the ability for the improved node to handle existing load is
increased, but the load itself is unchanged.


In a database where data resides on a single node, vertical scaling is done by spreading the load between the CPU
and RAM resources of the machine.


10 Opcenter Intelligence 2401.0001 - Product Overview


_Where Are We Starting From and Where are We Going?_


_What is a Columnstore Data Engine?_

### 2.7 What is a Columnstore Data Engine?


A columnstore is data that is logically organized as a table with rows and columns, and physically stored in a
column-wise data format. It is a new way to store relational table data as opposed to a rowstore, where data is
logically organized as a table with rows and columns, and then physically stored in a row-wise data format.


A columnstore index is normally used to store and query large fact tables in a data warehouse to enhance
performance. In Opcenter Intelligence the data warehouse has been designed to support the columnstore method,
which is automatically managed by the system.

### 2.8 What is an Analytical Tool?


An analytical tool is business intelligence software that allows small and big businesses to easily connect
to qualitative and quantitative data by means of delivery and analysis services to visualize and create interactive,
shareable dashboards.


The information gathered via these services can then be applied to customers, whether new or existing. Finally,
data can circle back to meet the company's business objectives.


These tools provide “speed of thought” analysis, conforming to the way business analysts want to consume and
interact with data. Applications built with these tools are useful for point-and-click filtering and drill-down to detail.


Opcenter Intelligence is natively integrated with a number of reporting applications in terms of data transfer and
visualization capability.

### 2.9 What is Operational Reporting?


Operational reporting focuses on producing detailed reports of day-to-day organizational operations. These reports
include data pertaining to production costs, records, resource availability and expenditures, in-depth examinations
of manufacturing processes, personnel and equipment actually used to produce product, material consumed,
material produced, and other relevant production data such as costs and performance results.
They come in different time intervals, but generally focus on the short-term. Operational reports can also be
modified by specific stakeholders and tailored to their needs to provide clearer insights and are also used by
personnel responsible for plant and line operations.


Opcenter Intelligence 2401.0001 - Product Overview 11


_What is Opcenter Intelligence Composed of?_


_What is Operational Reporting?_

## 3 What is Opcenter Intelligence Composed of?


Opcenter Intelligence provides you with all the following basic functionalities:











A Manufacturing Analytical Model (MAM) based on the international standard ISA-95 for entity definition.
All the features required to extend and customize models and metrics.
A smart support for semantic data mapping between the sources and the MAM.
An application designed to manage and maintain an Opcenter Intelligence Solution.
A presentation/collaboration layer where you can perform and share data analysis.



12 Opcenter Intelligence 2401.0001 - Product Overview


_What is Opcenter Reporting Composed of?_


_What is Operational Reporting?_

## 4 What is Opcenter Reporting Composed of?


Opcenter Reporting is integrated in the Opcenter Intelligence solution package and is the most cost-effective
visualization tool supported by Opcenter Intelligence in order to easily benefit from the built-in reports provided by
Siemens MOM products, like for example Opcenter Execution Core, Opcenter Execution Discrete or Opcenter
Execution Process, for which out-of-the-box reports designed using Opcenter Reporting are available and where
Opcenter Reporting can be embedded.

###### Installation Options


Opcenter Reporting installation options can be either of the following:








As a stand-alone application.
After the installation of Opcenter Intelligence, whose ISO root folder contains the **OpcenterReport** subfolder
including Opcenter Reporting setup files.


###### Basic Functionalities

Opcenter Reporting provides you with all the following basic functionalities:













Multiple data source connections: both SQL Server and Oracle server types are supported.
Integration with Siemens User Management Component for user authentication and login management.
Report structure design and selection of how to show the information that originates either from a source
database structure relation or user-defined custom relations.
Organization of reports within folders.
Report cloning.
Report export and import.



For more details on Opcenter Reporting installation, configuration and usage, see _Opcenter Reporting Installation_
_Manual_ and _User Manual_ .


Opcenter Intelligence 2401.0001 - Product Overview 13


_Overview of Opcenter Intelligence Main Components_


_What is Operational Reporting?_

## 5 Overview of Opcenter Intelligence Main Components

###### Opcenter Intelligence Internal Components











Opcenter Intelligence Core includes the business logic to interact with the User Management Component
(UMC) and redistributes the calls to the Application Server.
Opcenter Intelligence Web API is a Web API self-hosted server that includes the business logic.
Opcenter Intelligence Application Client represents the Single Page Application Client.
Opcenter Intelligence Configurator is the stand-alone application that performs all the post-setup
configuration actions.


###### Databases

The following databases can be created and managed:









Engineering Database
Manufacturing Data Warehouse (MDW)
Production Interfaces, i.e. third-party Relational Database Management Systems (RDBMS), Opcenter
Sources, etc.



Opcenter Intelligence can also interact with other sources by creating views or by implementing the
communication with additional interfaces.

###### External Engines


Opcenter Intelligence interacts with the following external engines:









Data Engine: the storage for the data warehouse or its sources.
Ingestion Engine: provides the APIs to transform data into information.
Scheduler Engine: provides the APIs to schedule a data flow, including its data transformation.



14 Opcenter Intelligence 2401.0001 - Product Overview


_Who are we traveling with?_


_What is Operational Reporting?_

## 6 Who are we traveling with?


Opcenter Intelligence supports different sources, which can be divided into the following groups.


For more details on the functionalities supported by these sources, see _Opcenter Intelligence Reference Manual_ .


Entity Mapping Files for each data source are provided with the user documentation. These files contain the name
of the source database and its physical tables, the entities and attributes of the manufacturing data warehouse and
the corresponding source entities and UI items, as well as related mapping information.

###### Opcenter Products













Opcenter Execution Discrete (Opcenter EX DS)
Opcenter Execution Process (Opcenter EX PR)
Opcenter Execution Core (Opcenter EX CR)
Opcenter Execution Electronics (Opcenter EX EL)
Opcenter Execution Pharma (Opcenter EX PH)
Opcenter Quality (Opcenter QL)
Opcenter Intra Plant Logistics (Opcenter IPL)


###### SIMATIC IT Unified Architecture Products








SIMATIC IT Unified Architecture Discrete Manufacturing (UADM)
SIMATIC IT Unified Architecture Process Industries (UAPI)


###### SIMATIC IT Products











SIMATIC IT Line Monitoring System (LMS)
SIMATIC IT Production Suite (PRS)
SIMATIC IT Historian
SIMATIC IT Reporting Framework (RF)
SIMATIC IT Electronic Batch Recording (eBR)


###### CAMSTAR Products







Camstar Enterprise Platform (CEP) Core


###### QMS Products







QMS Professional


###### Third-Party Systems Products








SQL-based Systems
Oracle-based Systems



Opcenter Intelligence 2401.0001 - Product Overview 15


_Deep Dive into Opcenter Intelligence Concepts_


_What is a Manufacturing Analytical Model?_

## 7 Deep Dive into Opcenter Intelligence Concepts


In this step of our journey we want to present the main concepts of Opcenter Intelligence.
We will see how the product organizes its data model, how it executes commands at runtime, and how you can
create your own data model entities and business logic in order to develop and deploy a manufacturing solution.

### 7.1 What is a Manufacturing Analytical Model?


The Manufacturing Analytical Model defines the analysis model (i.e. entities and relationships), which is based on
ISA-95 International industry standard.


The analytical model makes the best use of the BI paradigms provided by Kimball and Inmon, in particular by taking
advantage of the development speed of Kimball's approach and of the stability of Inmon's model. The
manufacturing analytical model can manage information consistently and univocally and can expose it as a
dimensional model when the user needs it, providing a view of the data based on specific data structures such as
star schemas. Each is modeled with a central table, known as the fact table, surrounded by a set of dimension
tables.


The MDW data model represents the physical implementation of the Manufacturing Analytical Model (MAM).
The data model uses the vocabulary of the domain. That is a key point of the architecture, because it allows any
third-party software to connect and retrieve data from the MDW data model without any additional knowledge but
the domain model semantics.

### 7.2 What is an Opcenter Intelligence Solution?


A Solution is a container of objects that allow the user to perform information ingestion (that is the process of
obtaining and importing data for immediate use or storage in a database) in one or more data warehouses. It can
be composed of:











Projects
Scenarios

Flows

Environments

Smart Views



The Solution describes the entire project and includes:









A definition of data sources

A data collection approach
A selected smart view



The virtual solution can be deployed on multiple physical systems (for example test and production) after defining
the real system nodes (for example, the server name or the database name). You can therefore create different
technological scenarios (for example SQL Server and Oracle) and then you can tailor each scenario to development,
test, QA or production.

#### 7.2.1 What is a Project?


A Project is a set of different configurations whose execution results in information ingestion, that is the process of
obtaining and importing data for immediate use or storage in a database. Every part of this project manages the
transformation of information and does not depend on the scenario (for example on the number of servers, the
server types or the hardware distribution).


A Project represents the metadata integration rules of the project. To define these rules, the following items should
be determined:


16 Opcenter Intelligence 2401.0001 - Product Overview


_Deep Dive into Opcenter Intelligence Concepts_


_What is an Opcenter Intelligence Solution?_










A set of project functionalities.
One or more sites.
A set of project sources.
One or more timeline schedules.


##### 7.2.1.1 What are Functionalities?

Functionalities are user-functional concepts, that is the functions that the user is configuring regardless of how they
are implemented. Once you have selected the component to be used as a data source, the system can
automatically configure the internal tables and data mapping according to the selected functionalities.


For more details on each functionality, see _Opcenter Intelligence Reference Manual_ .


Data source configuration is based on the following functionalities:

































Certification Management
Completed WIP
Container Management
Context Management
Defect and Non Conformance

Device History
Downtime Management
Equipment Capacity
Equipment Management
Equipment Performance
Inventory Management
Labor Management
Labor Performance

Location Management
Maintenance Management
Material Consumption
Material Container History
Material Management
Operational Performance and Quality
Product and Material Traceability
Production Definition

Production Execution

Production Scheduling
Quality APC
Quality SPC
Sampling Management
Tag Management


##### 7.2.1.1.1 What are Models?

Data modeling is an abstract representation of the data structures to be used in the tables of a database to easily
organize the data you have to store and the data you want to retrieve and show.


A data model organizes entities and their relationships, standardizes how these elements relate to one another and
provides a way to access them without directly writing on the database or reading from it.


Models describe specific MOM functionalities and refer to ISA-95 standard.


For a list of the models and more details on each model, see _Opcenter Intelligence Reference Manual_ .


Opcenter Intelligence 2401.0001 - Product Overview 17


_Deep Dive into Opcenter Intelligence Concepts_


_What is an Opcenter Intelligence Solution?_

##### 7.2.1.2 What are Sources?


A source is the entity that supplies data. Manufacturing data is collected from a variety of data sources, including:









MOM Platform

Historian system
Third-party and legacy systems



As data is collected from multiple sources, Opcenter Intelligence provides the structure and context to help users
retrieve the required information regardless of where it comes from. Manufacturing data can be collected onschedule.

##### 7.2.1.3 What are Extensions?


Adding an extension means adding information to the out-of-the-box data warehouse. All entities in the data
warehouse are described by means of a metamodel. Therefore, adding entities means adding entities or
information to the metamodel.


Knowledge can be added in the form of a new entity or by adding properties to already existing entities. In both
cases, you can add simple information like new alphanumeric properties or complex information such as relations
with other entities.


The entity description requires the definition of the columns that make up the entity. Each column can have a
semantic type that does not specify the data type used by the system to store the information, but the meaning of
that data for the user during the analysis phase.


The purpose of extension modeling is to create data marts if the customer wants to extend the analytical system,
that is create business intelligence analyses based on data or hybrid relational tables if extensions are created to
generate reports. This type of modeling leads to limitations for the entities that can be created as model extensions.
The following types are possible:











**Analytical Facts** : a fact table, which contains measurable, quantitative data about the business. The fact
table can only include numerical data.
**Analytical Contexts** : dimension tables, which contain descriptive attributes. Each dimension table has a
single field primary key (PK) which has a one-to-many relationship with a foreign key (FK) in the fact table. As
a consequence, dimensions can only contain textual data.
**Generic Entity** : entity type that is not strictly related to star schema modeling but that permits to model
entities that contain both numeric and textual information useful for the generation of reports.


##### 7.2.1.4 What are Schedules?

A schedule is the planning for loading data into a data warehouse according to flows based on ETLs.


You can generate one or more periodic schedules in order to run ETL incremental load to keep the data warehouse
aligned with the sources.

#### 7.2.2 What is a Smart View


A Smart View is the representation of manufacturing entities, ideas and events, along with their properties and
relations, according to a system of categories. In many fields it can be created to limit complexity and help organize
manufacturing information. At data warehouse level, a smart view is a constellation schema, that is a collection of
star schemas.

Smart Views:








Aim at simplifying the complexity of relationships among entities.
Translate the system data vision into one that is more comprehensible to data analysts.



18 Opcenter Intelligence 2401.0001 - Product Overview


_Deep Dive into Opcenter Intelligence Concepts_


_What is an Opcenter Intelligence Solution?_


Simplify the data warehouse model by producing a usable format for data analysts and their tools.
Provide the formal naming and definition of properties and relationships within each specific industry
domain.



In our context, given the manufacturing data warehouse provided out of the box, a smart view is a part or a
projection of the data warehouse content specified to facilitate a particular purpose or user activity. It is, basically,
a partial and/or redefined visualization of the logical schema of the data warehouse.

###### Smart View Concepts


In the following linked pages you can find some important concepts you need to know to properly configure smart
views:










Smart View Types
Measures and Attributes

Contexts

Smart View Deploy


##### 7.2.2.1 Smart View Types

A smart view can be of type:









**Physical** : data warehouse tables are physically created in columnstore mode and the schema has the same
name as the view.
**Virtual** : the information is managed by creating SQL views on top of the data warehouse. This mode
involves transformations each time the user makes a query, and is therefore demanding in terms of
resources and possible system slowdowns. It should therefore be used responsibly, in particular when
prototyping scenarios are involved or if the data warehouse does not contain a huge amount of data.



If you want to change the smart view type, the structures that have already been created will not be changed. This
means that the model remains the same for the user and if any reports or dashboards have been created using one
type or the other, they will still be available after the change. If you change the type from virtual to physical, an
initial load will be necessary: this operation will require a long time.

##### 7.2.2.2 Smart View Measures and Attributes


The smart view reflects the star schema concept in common BI scenarios. This means that to simplify the analysis
and the usage of market BI tools, like Amazon QuickSight (on cloud), Tableau® (on-premises) and others, data is
organized in fact tables, where there are all the aggregable numbers and typically contain a large amount of data
(numbers can be called measures) and dimensions or contexts where you can find all the filtering or grouping labels
and typically contain less data (labels are called attributes).


To produce a set of star schemas, where every star schema is useful to calculate a set of KPIs or to display related
data in a dashboard, we provide the creation of the smart view, a simplified way to select meaningful information
that the user wants to use to calculate KPIs or display in dashboards. The first step is to choose the required
measures. This means that all the numbers he wants to aggregate, display, or use in KPI formulas need to be
selected. This selection leads to the creation of fact tables (one for each card) in the star schema, which will include
all the selected measures in columns. However, to create a complete star schema the dimensions/context are also
required.


To do so, the user has to perform a selection on the **Attributes** tab, where the system automatically displays all the
available dimensions/contexts related to the selected measures. Not all the dimensions/contexts are available for
every fact table and this is not so evident in the page, because all the dimensions/contexts are shown together and
when measures that belong to different cards are selected, in the selection of attributes no hint is given to
understand which measures those dimensions/contexts can be associated with.


Opcenter Intelligence 2401.0001 - Product Overview 19


_Deep Dive into Opcenter Intelligence Concepts_


_What is an Opcenter Intelligence Solution?_





After you have selected the attributes, the system can create the “beam” of the star schema, where the name of the
dimension/context is the name of the card and the columns are the selected attributes. The result is a
“constellation schema” (smart view), i.e. a set of star schemas where measures are used to perform aggregations
and attributes are used to filter or group information.


The names of the single measures, attributes, fact tables and dimensions/contexts can be customized by the user.

##### 7.2.2.3 Smart View Contexts


The **Contexts** tab is located between the **Measures** and the **Attributes** tabs on the **Smart View** page. In the
**Contexts** tab you can add dimensions/contexts that the system cannot automatically relate to the fact table. Every
card is made up of two sections:








**Standard** includes all the dimension/context automatically related by the system.
**Custom** include the dimension/context that you can manually relate to the fact table. “Manually” relate
means that you need to customize the scripts in the **Scenario >Database** to link the information to the fact
table.




##### 7.2.2.4 Smart View Deploy

The deployment of the smart view creates all the entities of the smart view: fact tables, all the dimensions/contexts
tables (star schema) related to the fact tables and the infrastructure required to load them. Smart view data is
loaded starting from the base entities (bm20) and for smart views of type Physical the load starts immediately after
the deployment. When you create a smart view of Physical type, you can choose how often it will be updated
incrementally (only new data or modified data is loaded). For Virtual smart views, on the contrary, no data load is
performed, so this configuration is not required as data is available in real-time.


The smart view deploy is based on the difference between existing and new data, so existing data is maintained.
Any new measures/attributes selected before the current deploy are filled as soon as the deploy is completed.
However, if you deliberately want to destroy and recreate the smart view with the consequent new data load, you
have to undeploy the smart view and deploy it again. Consequently, if the deploy of a Physical smart view is
executed again and a big amount of data was stored in the system, the duration of the data load will last a long
time.


You have to deploy a smart view every time any changes are made to the smart view configuration: schedule time,
smart view type, measures/attributes selection.




#### 7.2.3 What is a Scenario?

A scenario is the model of hardware and software resources for the project. This model is the abstract
representation of the distribution of servers, services, databases and flows in a network. A solution can have more
scenarios. In a scenario the user can design the resource architecture without assigning Domain Names or IP


20 Opcenter Intelligence 2401.0001 - Product Overview


_Deep Dive into Opcenter Intelligence Concepts_


_What are Opcenter Reporting Concepts?_


addresses. The definition of a scenario starts with the selection of a Project and the definition of a number of
services made up of databases and flows. A scenario can be associated with one or more environments.

###### What is a Flow?


A flow allows loading data from a source database to a data warehouse in either Initial or Incremental mode.
The initial load must be run once when the target database is empty. The incremental load is run periodically to
load all the changes which occur in the source database. To perform these operations, dedicated ETLs (Extract,
Transform, Load) are provided. After populating an empty database with data (initial load), it is necessary to
schedule a periodic run of ETL incremental loads in order to keep the data warehouse aligned with the sources.
Initial loads are specifically designed to move very large amounts of data in a quick and optimized manner, whereas
incremental loads move moderate amounts of data.

###### What is an Environment?


An environment represents the physical implementation of a scenario. While configuring an environment, all items
included in the scenario are mapped on real items that exist in a physical environment. Each physical machine to be
associated with those configured within the scenario requires specific services (that vary according to its role). The
configured scenario is then mapped on a real environment to which it will be deployed in order to make it
operational.

###### What is a Deploy?


The deploy of a solution or of a smart view is a set of operations performed to make operational all the items
included in the project, according to the details defined during the creation of the environment or of the smart
view. The deploy engine performs the two following actions:








Deploy of all project items.
Update of existing items.


### 7.3 What are Opcenter Reporting Concepts?

In this step of our journey we want to present the main concepts which are considered prerequisites to
understanding how to work efficiently with Opcenter Reporting.











Reports
Data Sources

Custom Relations

Designer
Custom Entities


#### 7.3.1 Reports

Reports provide a high-level and detailed view of a company's present assets, which is useful for rapid decisionmaking. Reports are most beneficial when they provide granular data in real time, as outdated information would
make them less effective. A manufacturing firm, for instance, can measure several key aspects of its production
chain to make daily improvements. An operational report in this case could include data on resource costs and
usage, production efficiency and equipment status.


In Opcenter Reporting reports are typically produced in tabular format and include some charts. They can be easily
retrieved and printed, organized in a hierarchical folder structure and exported and reimported into another
system.


Opcenter Intelligence 2401.0001 - Product Overview 21


_Deep Dive into Opcenter Intelligence Concepts_


_What are Opcenter Reporting Concepts?_

#### 7.3.2 Data Sources


Users can define the sources that supply data for reports by creating data source connections that they can use
when they create a report. Opcenter Reporting can only be connected to the databases of Siemens MOM products.
The connection to third-party databases is not allowed.


In Opcenter Reporting:










Multiple data sources can be configured (both SQL Server and Oracle are supported).
Either Windows authentication (only for SQL Server sources) or Database authentication are available.
Data sources can be validated by testing the connection.
Relations between tables or views (not already available in the source database) can be added.


#### 7.3.3 Custom Relations

Reports are created or modified by using the source database structure relation. Further relations between tables
or views which are not present in the source database can also be defined and imported in Opcenter Reporting. A
script to be imported for a specific data source must be defined.

#### 7.3.4 Designer


Combit® List & Label Designer is the tool integrated into the application to author and modify reports created in
Opcenter Reporting. The first time the Designer is launched, the user is prompted to download and install it.


In the Designer you can add simple tables, comprehensive master-detail reports/subreports, charts, RTF text,
barcodes, graphics, PDF objects, user-defined objects etc. You can also employ a wide variety of charts and gauges
to enhance reports with professional-quality visuals and drill down the hierarchy from summary information to
more detailed data.


For information and instructions on how to use the Designer, see _List & Label® Designer Manual_ provided
with _Opcenter Reporting_ _Documentation_ .

#### 7.3.5 Custom Entities


In Opcenter Reporting, a custom entity represents report data that is returned from running a query on an external
data source. The custom entity depends on the data connection that contains information about the external data
source. The data itself is not included in the report definition. The custom entity contains a query command.


22 Opcenter Intelligence 2401.0001 - Product Overview


