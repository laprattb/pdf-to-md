|Opcenter Execution Pharma|Col2|Col3|Opcenter Intelligence Model Entities|Col5|Opcenter Execution Pharma Model Entities|Col7|
|---|---|---|---|---|---|---|
|~~**DB Name**~~|~~**Entity**~~|~~**Attribute**~~|~~**Entity**~~<br>|~~**Attribute - Tables**~~|~~**Entity exposed by EX PH**~~<br>|~~**Mapping Info**~~<br>|
||||~~**ActionTrace**~~||**Electronic Signature**||
|----|----|smallint||ActionTraceSiteId|||
|eBRdb|XFP_ACTIONSTRACES|ACTIONID||ActionTraceKey||Action id|
|eBRdb|XFP_ACTIONSTRACES|ACTION||Name||The action<br>Example:<br>- Lot Modification<br>- OF Launching<br>- Item Validation|
|eBRdb|XFP_ACTIONSTRACES|DTDATEDEBUT||StartDateTime||Beginning date|
|eBRdb|XFP_ACTIONSTRACES|DTDATEFIN||EndDateTime||End date|
|----|----|smallint||LaborId||Identity of the user that performed the action.|
|eBRdb|XFP_ACTIONSTRACES|SIGNATAIRE1|SIGNATAIRE1|SIGNATAIRE1|SIGNATAIRE1|SIGNATAIRE1|
|eBRdb|XFP_ACTIONSTRACES|COMMENTAIRE1||Comment||First comment|
|----|XFP_ACTIONSTRACES|VALIDE||Valid||Flag indicating if the action is valid (1 or 0)|
||||~~**Container**~~||**Container**||
|----|----|smallint||ContainerSiteId|||
|eBRdb|XFP_CONTENANTS|CONCAT(CONCAT(CONCAT(CONCAT(TRIM(CODEART),'_'),TRIM(CODELOT)),'_'),TRIM<br>(CONTENANT))||ContainerKey|||
|eBRdb|XFP_CONTENANTS|CONTENANT||Name||Container|
|eBRdb|XFP_CONTENANTS|IDENTIFIANT||Description||Container code from which material was picked|
|----|----|----||ContainerStatusId||Id of the container status|
|eBRdb|XFP_CONTENANTS|STATUTCONT|STATUTCONT|STATUTCONT|STATUTCONT|STATUTCONT|
||||~~**ContainerStatus**~~||**Container status**||
|----|----|smallint||ContainerStatusSiteId|||
|eBRdb|XFP_CONTENANTS|STATUTCONT||ContainerStatusKey|||
|eBRdb|XFP_CONTENANTS|STATUTCONT||Name||Status of container when it was used for consumption|
||||~~**Equipment**~~||**Equipment**||
|----|----|smallint||EquipmentSiteId|||
|eBRdb|EQP_EQUIPMENT|CODE||EquipmentKey||Code of the equipment|
|eBRdb|EQP_EQUIPMENT|COALESCE(NAME, CODE)||Name||Name or code of equipment|
||||~~**EquipmentClass**~~||**Equipment Class**||
|----|----|smallint||EquipmentClassSiteId|||
|eBRdb|EQP_EQPCLASS|CODE||EquipmentClassKey||Code of the equipment class|
|eBRdb|EQP_EQPCLASS|NAME||Name||Name of the equipment class<br>|
||||~~**EquipmentEquipmentClass**~~||~~**Relationship between Equipment and Equipment Class**~~|~~**Relationship between Equipment and Equipment Class**~~|
|----|----|smallint||EquipmentEquipmentClassSiteId|||
|eBRdb|EQP_EQUIPMENT|concat(concat(CODE,'_'),EQUIPMENTCLASS)||EquipmentEquipmentClassSiteKey|||
|eBRdb|----|smallint||EquipmentClassId||Class of the equipment|
|----|EQP_EQUIPMENT|EQUIPMENTCLASS|EQUIPMENTCLASS|EQUIPMENTCLASS|EQUIPMENTCLASS|EQUIPMENTCLASS|
|eBRdb|----|smallint||EquipmentId||Code of the equipment|
|----|EQP_EQUIPMENT|CODE|CODE|CODE|CODE|CODE|
||||~~**EquipmentProperty**~~||**Equipment Property**||
|----|----|smallint||EquipmentPropertySiteId|||
|eBRdb|EQP_PROPERTY|'Status' OR PK_OBJECTID OR PK_OBJECTID+'_MinimalValue' OR<br>PK_OBJECTID+'_MaximalValue'||EquipmentPropertyKey|||
|eBRdb|EQP_PROPERTY|'Status' OR CODE OR CODE+' (MinimalValue)' OR CODE+' (MaximalValue)'||Name||Status / Property code|
|eBRdb|EQP_PROPERTY|NAME OR NAME+' (MinimalValue)' OR NAME+' (MaximalValue)'||Description|||
|eBRdb|EQP_PROPERTY|'String' OR 'Numeric'||PropertyTypeId<br>||Type (String / Numeric)|
||||~~**EquipmentPropertyStaticValue**~~|~~**EquipmentPropertyStaticValue**~~|**Value of equipment property**||
|----|----|smallint||EquipmentPropertyStaticValueSiteId|||
|eBRdb|EQP_EQUIPMENT,<br>EQP_EQPEXE_PTYVAL|concat(CODE,'_Status') OR PK_ID OR concat(PROP.PK_ID,'_MinimalValue') OR<br>concat(PROP.PK_ID,'_MaximalValue') OR||EquipmentPropertyStaticValueKey|||
|----|----|smallint||EquipmentId||Id of the equipment|
|eBRdb|EQP_EQUIPMENT|CODE|CODE|CODE|CODE|CODE|


|----|----|smallint|Col4|EquipmentPropertyId|Col6|Id of the equipment property|
|---|---|---|---|---|---|---|
|eBRdb|EQP_EQPEXE_PTYVAL|'Status' OR PROPERTYID OR concat(PROPERTYID,'_MinimalValue') OR<br>concat(PROPERTYID,'_MaximalValue')|'Status' OR PROPERTYID OR concat(PROPERTYID,'_MinimalValue') OR<br>concat(PROPERTYID,'_MaximalValue')|'Status' OR PROPERTYID OR concat(PROPERTYID,'_MinimalValue') OR<br>concat(PROPERTYID,'_MaximalValue')|'Status' OR PROPERTYID OR concat(PROPERTYID,'_MinimalValue') OR<br>concat(PROPERTYID,'_MaximalValue')|'Status' OR PROPERTYID OR concat(PROPERTYID,'_MinimalValue') OR<br>concat(PROPERTYID,'_MaximalValue')|
|eBRdb|EQP_EQUIPMENT,<br>EQP_EQPEXE_PTYVAL,<br>EQP_EQPEXE_LISTITEM|In Progress' OR 'Archived' OR 'Obsolet' OR 'Out of site' OR<br>STRINGVALUE OR NULL||StringValue||Value (if it is a string property)|
|----|EQP_EQUIPMENT,<br>EQP_EQPEXE_PTYVAL,<br>EQP_EQPEXE_LISTITEM|NULL OR NUMAVLUE OR NUMMINIMUM OR NUMMAXIMUM||FloatValue||Value (if it is a numerical property)|
|----|----|timestamp||DatetimeValue||Value timestamp<br>|
||||~~**EquipmentStatusSnapshot**~~||~~**Equipment snapshots about status properties**~~|~~**Equipment snapshots about status properties**~~|
|----|----|smallint||EquipmentStatusSnapshotSiteId|||
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL,<br>EQP_EQPEXE_SNAPSHOT|concat(concat(concat(concat(FK_SNAPSHOT,'_'),PROPERTYCODE),'_'),STATUSCODE)||EquipmentStatusSnapshotKey|||
|----|----|smallint||EquipmentPropertyId||Identity of the property concerned by the snapshot|
|eBRdb|EQP_PROPERTY|PK_OBJECTID|PK_OBJECTID|PK_OBJECTID|PK_OBJECTID|PK_OBJECTID|
|----|----|smallint||EquipmentId||Code of the equipment concerned by the snapshot|
|eBRdb|EQP_EQPEXE_SNAPSHOT|CODEEQUIP|CODEEQUIP|CODEEQUIP|CODEEQUIP|CODEEQUIP|
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL|STATUSLABEL||StatusLabel||Status label of the status property|
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL|CURRENTROTATION||CurrentRotation||Number of the rotation actually occurred|
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL|MAXROTATION||MaxRotation||Max rotation of the status property|
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL|TOTALROTATION||TotalRotation||Total rotation of the status property|
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL|TOTALCYCLE||TotalCycle||Total number of the cycle for the property|
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL|CURRENTVALUE||CurrentValue||Defines if the Status code is the current value of the status property|
|eBRdb|EQP_EQPEXE_SNAPSHOTDETAIL|PEREMPTION||PeremptionDate||Peremption date of the status property|
||||~~**EquipmentTrace**~~||**Equipment Trace**||
|----|----|smallint||EquipmentTraceSiteId|||
|eBRdb|EQP_EQPEXE_TRAIL|PK_TRAILID||EquipmentTraceSiteKey||Unique identification of trails|
|----|----|smallint||EquipmentStatusSnapshotId||Identity of the snapshot which describes the different values of Status<br>properties|
|eBRdb|EQP_EQPEXE_TRAIL,<br>EQP_EQPEXE_SNAPSHOTDETAIL|concat(concat(concat(concat(FK_SNAPHOT,'_'),PROPERTYCODE),'_'),STATUSCODE)|concat(concat(concat(concat(FK_SNAPHOT,'_'),PROPERTYCODE),'_'),STATUSCODE)|concat(concat(concat(concat(FK_SNAPHOT,'_'),PROPERTYCODE),'_'),STATUSCODE)|concat(concat(concat(concat(FK_SNAPHOT,'_'),PROPERTYCODE),'_'),STATUSCODE)|concat(concat(concat(concat(FK_SNAPHOT,'_'),PROPERTYCODE),'_'),STATUSCODE)|
|----|----|smallint||EquipmentPropertyId||Identity of the property concerned by the trail|
|eBRdb|EQP_PROPERTY|PK_OBJECTID|PK_OBJECTID|PK_OBJECTID|PK_OBJECTID|PK_OBJECTID|
|eBRdb|EQP_EQPEXE_TRAIL|PROPERTYATTRIBUT||PropertyAttribute||Attribute of the property concerned by the trail|
|----|----|smallint||EquipmentId||Identity of the equipment concerned by the trail|
|eBRdb|EQP_EQPEXE_TRAIL|EQUIPMENT|EQUIPMENT|EQUIPMENT|EQUIPMENT|EQUIPMENT|
|eBRdb|EQP_EQPEXE_TRAIL|FK_PARENT_TRAILID||ParentEquipmentTrace||Trail id of the parent trail|
|eBRdb|EQP_EQPEXE_TRAIL|FK_ORIGIN_TRAILID||OriginEquipmentTrace||Trail id of the first parent trail|
|eBRdb|EQP_EQPEXE_TRAIL|FUNCTION||Function||Description of the action tracked by the trail. The functions are predefined<br>and allow to define the different uses of the equipment|
|eBRdb|EQP_EQPEXE_TRAIL|FUNCTION_ORIGIN||OriginFunction||Description of the action tracked by the original trail. The functions are<br>predefined and allow to define the different uses of the equipment.|
|eBRdb|EQP_EQPEXE_TRAIL|DATEHOUR||CreationDatetime||Date and time of the trail creation|
|----|----|smallint||WorkstationId||Workstation used in the action tracked|
|eBRdb|EQP_EQPEXE_TRAIL|WORKSTATION|WORKSTATION|WORKSTATION|WORKSTATION|WORKSTATION|
|----|----|smallint||WorkcenterId||Workcenter concerned by the trail|
|eBRdb|EQP_EQPEXE_TRAIL|WORKCENTER|WORKCENTER|WORKCENTER|WORKCENTER|WORKCENTER|
|----|----|smallint||LaborId||User log in during the trail|
|eBRdb|EQP_EQPEXE_TRAIL|USERLOGIN|USERLOGIN|USERLOGIN|USERLOGIN|USERLOGIN|
|----|----|smallint||SignedLaborId||Signed user|
|eBRdb|EQP_EQPEXE_TRAIL|SIGNEDUSERLOGIN|SIGNEDUSERLOGIN|SIGNEDUSERLOGIN|SIGNEDUSERLOGIN|SIGNEDUSERLOGIN|


|eBRdb|EQP_EQPEXE_TRAIL|ENVIRONMENT|Col4|Environment|Col6|XFP Environment|
|---|---|---|---|---|---|---|
|eBRdb|EQP_EQPEXE_TRAIL|WORKORDER||OperationExecutionNumber||Number of the workorder used in the action tracked|
|----|----|smallint||OperationExecutionMaterialLotId||The workorder lot number used in the action tracked|
|eBRdb|XFP_LOTS|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|
|----|----|smallint||ProducedMaterialDefinitionId||The workorder product number used in the action tracked|
|eBRdb|EQP_EQPEXE_TRAIL|TRIM(WORKORDER_PRODUCT)|TRIM(WORKORDER_PRODUCT)|TRIM(WORKORDER_PRODUCT)|TRIM(WORKORDER_PRODUCT)|TRIM(WORKORDER_PRODUCT)|
|eBRdb|EQP_EQPEXE_TRAIL|BATCHID||Batch||Unique identifier of the batch that generated the data|
|----|----|smallint||OperationResponseId||Unique identifier of the task that generated the data|
|eBRdb|EQP_EQPEXE_TRAIL|TASKID|TASKID|TASKID|TASKID|TASKID|
|eBRdb|EQP_EQPEXE_TRAIL|PICODE||PICode||Process instructions code used for record of the data|
|----|----|smallint||RefEquipmentId||Equipment code of a piece of equipment to which the trail referred. For<br>instance, if a combination occurred, the field will contain the source<br>equipment or destination equipment|
|eBRdb|EQP_EQPEXE_TRAIL|EQUIPMENT_REF|EQUIPMENT_REF|EQUIPMENT_REF|EQUIPMENT_REF|EQUIPMENT_REF|
|----|----|smallint||AssemblyEquipmentId||Equipment code assembled with the equipment that generated the data|
|eBRdb|EQP_EQPEXE_TRAIL|EQUIPMENT_ASSEMBLY|EQUIPMENT_ASSEMBLY|EQUIPMENT_ASSEMBLY|EQUIPMENT_ASSEMBLY|EQUIPMENT_ASSEMBLY|
|eBRdb|EQP_EQPEXE_TRAIL|DIRECTION||Direction||Direction of the action concerned by the trail|
|----|----|smallint||MaterialDefinitionId||Identity of the item concerned by the trail|
|eBRdb|EQP_EQPEXE_TRAIL|TRIM(ITEM)|TRIM(ITEM)|TRIM(ITEM)|TRIM(ITEM)|TRIM(ITEM)|
|----|----|smallint||MaterialLotId||Identity of the lot concerned by the trail|
|eBRdb|XFP_LOTS|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|
|----|----|smallint||LocationId||Location of the equipment.|
|eBRdb|EQP_EQPEXE_TRAIL|TRIM(LOCATION)|TRIM(LOCATION)|TRIM(LOCATION)|TRIM(LOCATION)|TRIM(LOCATION)|
|eBRdb|EQP_EQPEXE_TRAIL|QUANTITY||CombiningQuantity||Quantity for combining|
|eBRdb|EQP_EQPEXE_TRAIL|UNIT||CombiningQuantityUomId||Quantity for combining|
|eBRdb|EQP_EQPEXE_TRAIL|DLU||LDU||Time limit to use the property|
|eBRdb|EQP_EQPEXE_TRAIL|DLUUNIT||LDUUomId||Time unit limit to use the property|
|eBRdb|EQP_EQPEXE_TRAIL|MAXROTATION||MaxRotation||Maximum rotations for the property concerned by the trail|
|eBRdb|EQP_EQPEXE_TRAIL|VALUE||PropertyAttributeValue||Value of the property concerned by the trail regardless of the property type.<br>If the property type is different from String, the value is also available in<br>other fields|
|eBRdb|EQP_EQPEXE_TRAIL|VALUE_BEFORE||PropertyAttributeValueBefore||Old value of the property concerned by the trail|
|eBRdb|EQP_EQPEXE_TRAIL|ID_IN_LIST||PropertyListValue||Current value of the list property for the equipment concerned by the trail|
|eBRdb|EQP_EQPEXE_TRAIL|EPE||EPE||EPE used by the equipment that generated the data|
|eBRdb|EQP_EQPEXE_TRAIL|EPE_RETURN||EPEValue||Value returned by the EPE during a process|
|eBRdb|EQP_EQPEXE_TRAIL|MESSAGE||Message||Message which describes the trail|
|eBRdb|EQP_EQPEXE_TRAIL|COMMENTS||Comment||Comments for the trail|
|eBRdb|EQP_EQPEXE_TRAIL|ISMAIN||IsMain||Defines if the trail is the origin trail|
||||~~**Labor**~~||**Person**||
|----|----|smallint||LaborId||User login|
|eBRdb|acc_person|LOGIN|LOGIN|LOGIN|LOGIN|LOGIN|
|eBRdb|acc_person|FULLNAME||Name||User full name|
||||~~**LaborClass**~~||**Personnel class**||
|----|----|smallint||LaborId|||
|eBRdb|PERSONNELCLASSNAME|----|----|----|----|----|
|eBRdb|PERSONNELCLASSNAME|----||Name||Personnel class name<br>|
||||~~**LaborLaborClass**~~||~~**Relationship between Person and Personnel class**~~|~~**Relationship between Person and Personnel class**~~|
|----|----|smallint||LaborLaborClassSiteId|||
|eBRdb|ACC_PERSON ,<br>ACC_PERSONNELCLASS|ACC_PERSON.LOGIN + '_' + ACC_PERSONNELCLASS.PERSONNELCLASSNAME||LaborLaborClassKey|||
|----|----|smallint||LaborId||User login|
|eBRdb|ACC_PERSON|LOGIN|LOGIN|LOGIN|LOGIN|LOGIN|
|----|----|smallint||LaborClassId||Personnel class name|
|eBRdb|ACC_PERSONNELCLASS|PERSONNELCLASSNAME|PERSONNELCLASSNAME|PERSONNELCLASSNAME|PERSONNELCLASSNAME|PERSONNELCLASSNAME|
||||~~**Location**~~||**Location**||


|----|----|smallint|Col4|LocationSiteId|Col6|Col7|
|---|---|---|---|---|---|---|
|eBRdb|XFP_EMPLACEMENTS|TRIM(CODEEMPL)||LocationKey|||
|eBRdb|XFP_EMPLACEMENTS|TRIM(CODEEMPL)||Name||Code of the location|
|eBRdb|XFP_EMPLACEMENTS|LIBEMPL||Description||Description of the location|
||||~~**MaterialDefinition**~~||**Material**||
|----|----|smallint||MaterialDefinitionSiteId|||
|eBRdb|XFP_ARTICLES|TRIM(CODEART)||MaterialDefinitionKey||Item code of the consumed material|
|eBRdb|XFP_ARTICLES|nvl(DESIGNPRINCIPALE,TRIM(CODEART)||Name||Description (if not null), or Item code|
|eBRdb|XFP_ARTICLES|DESIGNLONGUE||Description||Item long description of the consumed material|
||||~~**MaterialLot**~~||**Lot**||
|----|----|smallint||MaterialLotSiteId|||
|eBRdb|XFP_LOTS|IDENTIFIANT||MaterialLotKey||Number of the lot|
|eBRdb|XFP_LOTS|CODELOT||Name||Identifier of the lot|
|eBRdb|XFP_LOTS|UNITEPOIDSUNITAIRE||UomId||Lot unitary weight unit|
|----|----|smallint||MaterialDefinitionId||Code of the item concerned by the lot|
|eBRdb|XFP_LOTS|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|
|eBRdb|XFP_LOTS|DTDATERECEPTION||ValidFromDateTime||Receipt date of the lot|
|eBRdb|XFP_LOTS|DTDATELIMITEUTILISATION||ValidToDateTime||Limit date to use the lot|
|eBRdb|XFP_LOTS|POIDSUNITAIRE||Quantity||Lot unitary weight|
|----|----|smallint||MaterialLotStatusId||Status|
|eBRdb|XFP_LOTS|STATUS|STATUS|STATUS|||
||||**MaterialLotStatus**||**Lot Status**||
|----|----|smallint||MaterialLotStatusSiteId|||
|eBRdb|XFP_LOTS|STATUS||MaterialLotStatusKey|||
|eBRdb|XFP_LOTS|STATUS||Name|||
|----|----|----||Description|||
||||~~**MaterialProperty**~~||**Lot property**||
|----|----|smallint||MaterialPropertySiteId|||
|eBRdb||PeremptionDate||MaterialPropertyKey|||
|eBRdb||DateTime||PropertyTypeId|||
|eBRdb||Peremption Date||Name<br>|||
||||~~**MaterialLotPropertyStaticValue**~~|~~**MaterialLotPropertyStaticValue**~~|**Lot property value**||
|----|----|smallint||MaterialLotPropertyStaticValueSiteId|||
|eBRdb|XFP_LOTS|IDENTIFIANT+'_PeremptionDate'||MaterialLotPropertyStaticValueKey||Possible values: "Peremption Date"|
|----|----|smallint||MaterialLotId||Number of the lot|
|eBRdb|XFP_LOTS|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|
|----|----|smallint||MaterialPropertyId||Possible values:  "Peremption Date"|
|eBRdb|XFP_LOTS|PeremptionDate|PeremptionDate|PeremptionDate|PeremptionDate|PeremptionDate|
|----|----|----||StringValue|||
|----|----|DTDATEPEREMPT||DatetimeValue|||
|----|----|----||FloatValue|||
|----|----|----||Sequence|||
||||~~**OperationExecution**~~||**Work Order**||
|----|----|smallint||OperationExecutionSiteId|||
|eBRdb|XFP_OFENTETE|TRIM(NUMOF)+ '_' + TRIM(INDICEOF)||OperationExecutionKey||Concatenation of Work order number and work index number|
|eBRdb|XFP_OFENTETE|TRIM(NUMOF)||Name||Work order number|
|eBRdb|XFP_OFENTETE|TRIM(NUMOF)+ '_' + TRIM(INDICEOF)||Description||Concatenation of Work order number and work index number|
|----|----|smallint||OperationExecutionStatusId||Work order status|
|eBRdb|XFP_OFENTETE|ETAT|ETAT|ETAT|ETAT|ETAT|
|----|----|smallint||MaterialDefinitionId||The code of the product manufactured by the work order|
|eBRdb|XFP_OFENTETE|TRIM(CODEPRODUIT)|TRIM(CODEPRODUIT)|TRIM(CODEPRODUIT)|TRIM(CODEPRODUIT)|TRIM(CODEPRODUIT)|


|eBRdb|XFP_OFENTETE|QUANTITEOF|Col4|ProducedQuantity|Col6|Quantity launched for the WO. This quantity will be simply mentioned on<br>the WO header. It does not<br>have to correspond to the sum of the used material quantities.<br>The system also checks that the input quantity is an integer number if the<br>selected unit is displayed<br>among the indivisible units.|
|---|---|---|---|---|---|---|
|eBRdb|XFP_OFENTETE|UNITEOF||UomId||Launched quantity unit|
|eBRdb|XFP_OFENTETE|DTDATECREAPARSYST||StartDateTime||Creation date|
|eBRdb|XFP_OFENTETE|DTDATEDERNIERCHGTETAT||EndDateTime<br>||Last changing state of the work order<br>|
||||~~**OperationExecutionCompensation**~~|~~**OperationExecutionCompensation**~~|~~**Information about compensators of work order**~~|~~**Information about compensators of work order**~~|
|----|----|smallint||OperationExecutionCompensationSiteId|||
|eBRdb|XFP_OFCOMPENS|XFP_OFCOMPENS.NUMOF+'_'+XFP_OFCOMPENS.INDICEOF+'_'+XFP_OFCOMPENS.P<br>HASECOMPENSE+'_'+XFP_OFCOMPENS.NUMSEQPHASECOMPENSE+'_'+XFP_OFCO||OperationExecutionCompensationKey|||
|----|----|smallint||CompensatedOperationResponseId||Identity of the phase, sequence and dose that will be compensated|
|eBRdb|XFP_OFLIGNESP|XOLP.NUMOF+'_'+XOLP.INDICEOF+'_'+XOLP.PHASE+'_'+XOLP.NUMSEQPHASE+'_'+X<br>OLP.DOSE|XOLP.NUMOF+'_'+XOLP.INDICEOF+'_'+XOLP.PHASE+'_'+XOLP.NUMSEQPHASE+'_'+X<br>OLP.DOSE|XOLP.NUMOF+'_'+XOLP.INDICEOF+'_'+XOLP.PHASE+'_'+XOLP.NUMSEQPHASE+'_'+X<br>OLP.DOSE|XOLP.NUMOF+'_'+XOLP.INDICEOF+'_'+XOLP.PHASE+'_'+XOLP.NUMSEQPHASE+'_'+X<br>OLP.DOSE|XOLP.NUMOF+'_'+XOLP.INDICEOF+'_'+XOLP.PHASE+'_'+XOLP.NUMSEQPHASE+'_'+X<br>OLP.DOSE|
|----|----|smallint||CompensatorOperationResponseId||Identity of the phase, sequence and dose that will compensate|
|eBRdb|XFP_OFLIGNESP|XOLP2.NUMOF+'_'+XOLP2.INDICEOF+'_'+XOLP2.PHASE+'_'+XOLP2.NUMSEQPHASE+<br>'_'+XOLP2.DOSE|XOLP2.NUMOF+'_'+XOLP2.INDICEOF+'_'+XOLP2.PHASE+'_'+XOLP2.NUMSEQPHASE+<br>'_'+XOLP2.DOSE|XOLP2.NUMOF+'_'+XOLP2.INDICEOF+'_'+XOLP2.PHASE+'_'+XOLP2.NUMSEQPHASE+<br>'_'+XOLP2.DOSE|XOLP2.NUMOF+'_'+XOLP2.INDICEOF+'_'+XOLP2.PHASE+'_'+XOLP2.NUMSEQPHASE+<br>'_'+XOLP2.DOSE|XOLP2.NUMOF+'_'+XOLP2.INDICEOF+'_'+XOLP2.PHASE+'_'+XOLP2.NUMSEQPHASE+<br>'_'+XOLP2.DOSE|
|eBRdb|XFP_OFCOMPENS|XFP_OFCOMPENS.NBDOSECOMPENSATEUR||CompensatorDoseNumber||The number of doses of compensator|
|eBRdb|XFP_OFCOMPENS|XFP_OFCOMPENS.POURCENTAGE||Percentage<br>||Compensation percentage|
||||~~**OperationExecutionConsumption**~~|~~**OperationExecutionConsumption**~~|**Work Order Consumption**||
|----|----|smallint||OperationExecutionConsumptionSiteId|||
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+DOSE+'_'+CODEART+'_'+<br>INDEXPESEE+'_'+INDEXPESEE+'_'+CONTENANT||OperationExecutionConsumptionKey||Unique identifier of the work order cosumption|
|~~----~~|----|smallint||OperationExecutionId||Identity of the work order|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|
|~~----~~|----|smallint||OperationResponseId||Identity of the work order phase/sequence/dose|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NUMOF+INDICEOF+PHASE+'_'+NUMSEQPHASE+'_'+DOSE|NUMOF+INDICEOF+PHASE+'_'+NUMSEQPHASE+'_'+DOSE|NUMOF+INDICEOF+PHASE+'_'+NUMSEQPHASE+'_'+DOSE|NUMOF+INDICEOF+PHASE+'_'+NUMSEQPHASE+'_'+DOSE|NUMOF+INDICEOF+PHASE+'_'+NUMSEQPHASE+'_'+DOSE|
|~~----~~|----|smallint||ConsumedMaterialDefinitionId||Item code of the consumed material|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|INDEXPESEE||WeighingIndex||Weight index|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NUMTICKET||LabelNumber||Label number|
|~~----~~|----|smallint||OperationExecutionConsumptionActionTypeId||Action (preparation or manufacturing)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TRIM(ACTION)|TRIM(ACTION)|TRIM(ACTION)|TRIM(ACTION)|TRIM(ACTION)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DTDATEFINPESEE||WeighingDatetime||Consumption date|
|----|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DTDATECONTROLE||ReconciliationCheckDatetime||Reconciliation check date|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DTDATECONTROLERF||RadioFrequencyReconciliationCheckDatetime||Radio frequency reconciliation check date|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DTDATEMEO||CombinationDatetime||Combination date|
|~~----~~|----|smallint||WeighingLaborId||User login responsible of the consumption (simple weigh line)|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|OPERATEUR|OPERATEUR|OPERATEUR|OPERATEUR|OPERATEUR|
|~~----~~|----|smallint||ReconciliationCheckLaborId||User login responsible for the consumption (weigh line controlled after<br>weighing)|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CONTROLEUR|CONTROLEUR|CONTROLEUR|CONTROLEUR|CONTROLEUR|
|~~----~~|----|smallint||RadioFrequencyReconciliationCheckLaborId||User login responsible for the consumption (weigh linte controlled before<br>combination (RF controlled))|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CONTROLEURRF|CONTROLEURRF|CONTROLEURRF|CONTROLEURRF|CONTROLEURRF|
|~~----~~|----|smallint||CombinationLaborId||User login responsible for the consumption (combined weigh line)|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|OPERATEURMEO|OPERATEURMEO|OPERATEURMEO|OPERATEURMEO|OPERATEURMEO|
|~~----~~|----|smallint||WeighingWorkstationId||Work station on which the consumption was recorded (simple weigh line)|


|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|POSTEPHYSIQUE|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|~~----~~|----|smallint||ReconciliationCheckWorkstationId||Work station on which the consumption was recorded (weigh line<br>controlled after weighing)|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|POSTEDERECONCIL|POSTEDERECONCIL|POSTEDERECONCIL|POSTEDERECONCIL|POSTEDERECONCIL|
|~~----~~|----|smallint||RadioFrequencyReconciliationCheckWorkstationId||Work station on which the consumption was recorded (weigh line<br>controlled after combination (RF controlled))|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|POSTEDERECONCILRF|POSTEDERECONCILRF|POSTEDERECONCILRF|POSTEDERECONCILRF|POSTEDERECONCILRF|
|~~----~~|----|smallint||CombinationWorkstationId||Work station on which the consumption was recorded (combined weigh<br>line)|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|POSTEMEO|POSTEMEO|POSTEMEO|POSTEMEO|POSTEMEO|
|~~----~~|----|smallint||WorkcenterId||Work center on which the consumption was recorded|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|POSTEDECHARGE|POSTEDECHARGE|POSTEDECHARGE|POSTEDECHARGE|POSTEDECHARGE|
|~~----~~<br>|----|smallint||MaterialLotId||Lot number of the consumed material|
|~~eBRdb~~<br>|XFP_LOTS|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|IDENTIFIANT|
|~~----~~|----|smallint||LocationId||Location where the consumption was recorded|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|EMPLACEMENT|EMPLACEMENT|EMPLACEMENT|EMPLACEMENT|EMPLACEMENT|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TITRELOT||LotPotency||Potency of lot used for consumption|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|.TITRE2LOT||LotPotency2||Potency of lot used for consumption|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|INDTIT||PotencyUomId||Potency UoM|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|INDTIT2||Potency2UomId||Potency UOM|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DENSITELOT||LotDensity||Density of lot used for consumption|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|UNITEART||ItemUomId||Item unit|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TITREART||ItemPotency||Potency of item used for consumption|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TITRE2ART||ItemPotency2||Potency of item used for consumption|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DENSITEART||ItemDensity||Density of item used for consumption|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TOLERANCE||Tolerance||Tolerance|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||TagDensity||Density of tag used for consumption|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NUMEROCONCORDANCE||ConcordanceNumber||Concordance number|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|BRUTDEPART||StartGrossQuantity||Start Gros quantity|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|BRUTFIN||EndGrossQuantity||End Gross quantity|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NETCALCULE||CalculatedNet||Calculated net|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TARE||Tare||Tare|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NET||ConsumedQuantity||Consumed quantity - original UoM|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|QUANTRESTANTE||RemainingQuantity||Remaining quantity in the container after the consumption|


|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|UNITEPESEE|Col4|WeighingUomId|Col6|Original UoM|
|---|---|---|---|---|---|---|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|BRUT||Gross||Gross|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|ECARTPESEE||WeighingGap||Weigh gap|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||ForcedWeighing||Forced weighing (1 or 0)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||SameContainer||Same container indicator (1 or 0)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|PALETTE||PalletNumber||Pallet number|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NBCONTENANTS||NumberOfContainers||Number of containers|
|~~----~~|----|smallint||OperationExecutionConsumptionWeighingModeId||Identity of the weighing mode used to weigh the amount of material|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|MODEPESEE|MODEPESEE|MODEPESEE|MODEPESEE|MODEPESEE|
|~~----~~|----|smallint||OperationExecutionConsumptionWeighingTypeId||Identity of weight type|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TYPEPESEE|TYPEPESEE|TYPEPESEE|TYPEPESEE|TYPEPESEE|
|~~----~~|----|smallint||OperationExecutionConsumptionWeighingStatusId||Identity of weigh status|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|ETATPESEE|ETATPESEE|ETATPESEE|ETATPESEE|ETATPESEE|
|~~----~~|----|smallint||OperationExecutionConsumptionBalanceTypeId||Identity of scale type used|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|TYPEBALANCE|TYPEBALANCE|TYPEBALANCE|TYPEBALANCE|TYPEBALANCE|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NUMBALANCE||BalanceNumber||Scale number|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||ForcedPrecision||Forced precision indicator (1 or 0)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|INDLIBERATIONFORCEE||ForcedRelease||Forced free indicator (1 or 0)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||EndOfContainer||End of container (1 or 0)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||ForcedLot||Force lot flag (1 or 0)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||CorrectLot||Correct lot flag (1 or 0)|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||KeyboardInput||Keyboard input flag (1 or 0)|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|1 OR 0||PrintedLabel||Printed label flag (1 or 0)|
|~~----~~|----|smallint||OperationExecutionConsumptionBarcodeId||Identity of label barcode|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CODEBARRETICKET|CODEBARRETICKET|CODEBARRETICKET|CODEBARRETICKET|CODEBARRETICKET|
|~~----~~|----|smallint||OperationExecutionConsumptionReconciliationCheckId||Identity of reconciliation check|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CONTROLE|CONTROLE|CONTROLE|CONTROLE|CONTROLE|
|~~----~~|----|smallint||OperationExecutionConsumptionRFReconciliationCheckId||Identity of radio frequency reconciliation check|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CONTROLERF|CONTROLERF|CONTROLERF|CONTROLERF|CONTROLERF|
|~~----~~|----|smallint||ContainerId||Identity of the container|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CODEART+'_'+CODELOT+'_'+CONTENANT|CODEART+'_'+CODELOT+'_'+CONTENANT|CODEART+'_'+CODELOT+'_'+CONTENANT|CODEART+'_'+CODELOT+'_'+CONTENANT|CODEART+'_'+CODELOT+'_'+CONTENANT|
|~~----~~|----|smallint||ActionTraceId||Link for electronic signature|


|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|ACTIONID|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|UNITESTOCK||StockUomId||Stock UoM|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|NOTICKET||TicketNumber||Ticket number|
|~~----~~|----|smallint||OperationExecutionConsumptionCombinationId||Identity of combination|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|MEO|MEO|MEO|MEO|MEO|
|~~----~~|----|smallint||SourceEquipmentId||Source equipment code|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CODEEQUIPORIGINE|CODEEQUIPORIGINE|CODEEQUIPORIGINE|CODEEQUIPORIGINE|CODEEQUIPORIGINE|
|~~----~~|----|smallint||EquipmentId||Destination equipment code|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|CODEEQUIPDESTINATION|CODEEQUIPDESTINATION|CODEEQUIPDESTINATION|CODEEQUIPDESTINATION|CODEEQUIPDESTINATION|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|UNITECOMPTAGE||CountingUomId||Counting unit|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DTDATEVIDEDEBOX||WDUCleanDatetime||WDU clean date|
|eBRdb<br>|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|DTDATEDEBUTPESEE||WeighingDatetime||Begin weight date|
|~~----~~|----|smallint||OperationExecutionConsumptionMaterialLineStatusId||Identity of material line status|
|eBRdb|XFP_OFRESULTS, XFP_CONTENANTS,<br>XFP_OFLIGNESP|T' OR 'P'|T' OR 'P'|T' OR 'P'|T' OR 'P'|T' OR 'P'|
||||~~**OperationExecutionConsumptionActionType**~~|~~**OperationExecutionConsumptionActionType**~~|**Action type**||
|----|----|smallint||OperationExecutionConsumptionActionSiteId|||
|eBRdb||P OR F||OperationExecutionConsumptionActionKey||P or F|
|eBRdb||Preparation OR Manufacturing||Name<br>||Preparation or Manufacturing|
||||~~**OperationExecutionConsumptionBalanceType**~~|~~**OperationExecutionConsumptionBalanceType**~~|**Scale type**||
|----|----|smallint||OperationExecutionConsumptionBalanceTypeSiteId|||
|eBRdb|XFP_OFRESULTS|TRIM(TYPEBALANCE)||OperationExecutionConsumptionBalanceTypeKey|||
|eBRdb|XFP_OFRESULTS|TRIM(TYPEBALANCE)||Name<br>||M : METTLER<br>X : METTLER_MULTI<br>B : BIZERBA<br>A : METTLER ID30<br>S : METTLER SICS<br>C : METTLER SICS 2<br>I : SARTORIUS<br>Y : SARTORIUS8MULTI<br>P : PRECIA<br>T : TOLEDO<br>R : PRECIA SLAVE A+|
||||~~**OperationExecutionConsumptionBarcode**~~|~~**OperationExecutionConsumptionBarcode**~~|**Label barcode**||
|----|----|smallint||OperationExecutionConsumptionBarcodeSiteId|||
|eBRdb|XFP_OFRESULTS|CODEBARRETICKET||OperationExecutionConsumptionBarcodeKey|||
|eBRdb|XFP_OFRESULTS|CODEBARRETICKET||Name<br>||Label barcode|
||||~~**OperationExecutionConsumptionCombination**~~|~~**OperationExecutionConsumptionCombination**~~|**Combination**||
|----|----|smallint||OperationExecutionConsumptionCombinationSiteId|||
|eBRdb|XFP_OFRESULTS|MEO||OperationExecutionConsumptionCombinationKey|||
|eBRdb|XFP_OFRESULTS|MEO||Name<br>||Combination<br>|
||||~~**OperationExecutionConsumptionMaterialLineStatus**~~|~~**OperationExecutionConsumptionMaterialLineStatus**~~|~~**Status of material line after consumption**~~|~~**Status of material line after consumption**~~|
|----|----|smallint||OperationExecutionConsumptionMaterialLineStatusSiteId|||
|eBRdb||P OR T||OperationExecutionConsumptionMaterialLineStatusKey|||
|eBRdb||P OR T||Name<br>||P or T|
||||~~**OperationExecutionConsumptionReconciliationCheck**~~|~~**OperationExecutionConsumptionReconciliationCheck**~~|**Reconciliation check**||
|----|----|smallint||OperationExecutionConsumptionReconciliationCheckSiteId|||
|eBRdb|XFP_OFRESULTS|CONTROLE||OperationExecutionConsumptionReconciliationCheckKey|||


|eBRdb|XFP_OFRESULTS|CONTROLE|Col4|Name|Col6|Reconciliation check|
|---|---|---|---|---|---|---|
||||~~**OperationExecutionConsumptionRFReconciliationCheck**~~|~~**OperationExecutionConsumptionRFReconciliationCheck**~~|~~**Radio frequency reconciliation check**~~|~~**Radio frequency reconciliation check**~~|
|----|----|smallint||OperationExecutionConsumptionRFReconciliationCheckSiteId|||
|eBRdb|XFP_OFRESULTS|CONTROLERF||OperationExecutionConsumptionRFReconciliationCheckKey|||
|eBRdb|XFP_OFRESULTS|CONTROLERF||Name<br>||Radio frequency reconciliation check|
||||~~**OperationExecutionConsumptionWeighingMode**~~|~~**OperationExecutionConsumptionWeighingMode**~~|**Weighing Mode**||
|----|----|smallint||OperationExecutionConsumptionWeighingModeSiteId|||
|eBRdb|XFP_OFRESULTS|TRIM(MODEPESEE)||OperationExecutionConsumptionWeighingModeKey|||
|eBRdb|XFP_OFRESULTS|TRIM(MODEPESEE)||Name<br>||Net / Gross|
||||~~**OperationExecutionConsumptionWeighingStatus**~~|~~**OperationExecutionConsumptionWeighingStatus**~~|**Weight Status**||
|----|----|smallint||OperationExecutionConsumptionWeighingStatusSiteId|||
|eBRdb|XFP_OFRESULTS|TRIM(ETATPESEE)||OperationExecutionConsumptionWeighingStatusKey|||
|eBRdb|XFP_OFRESULTS|TRIM(ETATPESEE)||Name<br>||P: Weighing in progress<br>T: Weighing ended<br>R:<br>X:|
||||~~**OperationExecutionConsumptionWeighingType**~~|~~**OperationExecutionConsumptionWeighingType**~~|**Weight Type**||
|----|----|smallint||OperationExecutionConsumptionWeighingTypeSiteId|||
|eBRdb|XFP_OFRESULTS|TRIM(TYPEPESEE)||OperationExecutionConsumptionWeighingTypeKey|||
|eBRdb|XFP_OFRESULTS|TRIM(TYPEPESEE)||Name<br>||OF, MP, MP+|
||||~~**OperationExecutionPalletSpecification**~~|~~**OperationExecutionPalletSpecification**~~|**Pallet production declaration**||
|----|----|smallint||OperationExecutionPalletSpecificationSiteId|||
|eBRdb|XFP_OFPALETTES|CODEPAL||OperationExecutionPalletSpecificationKey||The pallet code|
|----|----|smallint||MaterialDefinitionId||Identity of the material|
|eBRdb|XFP_OFPALETTES|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|TRIM(CODEART)|
|----|----|smallint||OperationExecutionId||Identity of the work order|
|eBRdb|XFP_OFPALETTES|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|NUMOF+'_'+INDICEOF|
|eBRdb|XFP_OFPALETTES|UNITETARE||TareUomId||The tare unit of the pallet|
|eBRdb|XFP_OFPALETTES|IDENTIFIANT||Identifier||Pallet identifier|
|eBRdb|XFP_OFPALETTES|ETIQUETTE||Label||The label associated with the pallet|
|eBRdb|XFP_OFPALETTES|CODELOT||LotNumber||The declared lot number|
|eBRdb|XFP_OFPALETTES|TYPPAL||PalletType||The pallet type|
|eBRdb|XFP_OFPALETTES|QUANTTHEO||Quantity||Theorical quantity in stock unit|
|eBRdb|XFP_OFPALETTES|TARE||Tare||The tare of the pallet|
||||~~**OperationExecutionProperty**~~||**Work Order property**||
|----|----|smallint||OperationExecutionPropertySiteId|||
|----|----|PharmaLotNumber','Priority','ReferenceCode','Stability','WeightEquQuantity','Weig<br>htEquUnit','CustomerCodeRef','AllocationPart','Origine','PlannedLaunchingDate','Tr<br>ansactionCode','FunctionCode','CombinationNumber','DpyLabelCounter','DpyEditio<br>nNumber','DpyPalletNumber','DpyWeighingStartDate,'DpyWeighingEndDate'||OperationExecutionPropertyKey|||
|----|----|PharmaLotNumber','Priority','ReferenceCode','Stability','WeightEquQuantity','Weig<br>htEquUnit','CustomerCodeRef','AllocationPart','Origine','PlannedLaunchingDate','Tr<br>ansactionCode','FunctionCode','CombinationNumber','DpyLabelCounter','DpyEditio<br>nNumber','DpyPalletNumber','DpyWeighingStartDate,'DpyWeighingEndDate'||Name||'PharmaLotNumber','Priority','ReferenceCode','Stability','WeightEquQuantit<br>y','WeightEquUnit','CustomerCodeRef','AllocationPart','Origine','PlannedLau<br>nchingDate','TransactionCode','FunctionCode','CombinationNumber','DpyLa<br>belCounter','DpyEditionNumber','DpyPalletNumber','DpyWeighingStartDate<br>,'DpyWeighingEndDate'|
|----|----|String, Numeric, DateTime||PropertyTypeId<br>|||
||||~~**OperationExecutionPropertyStaticValue**~~|~~**OperationExecutionPropertyStaticValue**~~|**Work Order property value**||
|----|----|smallint||OperationExecutionPropertyStaticValueSiteId|||
|eBRdb|XFP_OFENTETE|XFP_OFENTETE.NUMOF+''_''+XFP_OFENTETE.INDICEOF +'_'+OEPROPERTYKEY<br>(refer to bm20private.OEPROPERTY)||OperationExecutionPropertyStaticValueKey|||
|----|----|'smallint  (refer to bm20private.OEPROPERTY)||OperationExecutionId||Identity of the work order|
|eBRdb|XFP_OFENTETE|XFP_OFENTETE.NUMOF+"_''+XFP_OFENTETE.INDICEOF  (refer to<br>bm20private.OEPROPERTY)|XFP_OFENTETE.NUMOF+"_''+XFP_OFENTETE.INDICEOF  (refer to<br>bm20private.OEPROPERTY)|XFP_OFENTETE.NUMOF+"_''+XFP_OFENTETE.INDICEOF  (refer to<br>bm20private.OEPROPERTY)|XFP_OFENTETE.NUMOF+"_''+XFP_OFENTETE.INDICEOF  (refer to<br>bm20private.OEPROPERTY)|XFP_OFENTETE.NUMOF+"_''+XFP_OFENTETE.INDICEOF  (refer to<br>bm20private.OEPROPERTY)|
|----|----|smallint||OperationExecutionPropertyId||Identity of the work order property|


|----|----|PharmaLotNumber, "Priority", "ReferenceCode", "Stability", "WeightEquUnit",<br>"CustomerCodeRef", "AllocationPart", "TransactionCode", "FunctionCode",<br>"PlannedLaunchingDate", "DpyWeighingStartDate",<br>"DpyWeighingEndDate","WeightEquQuantity", "CombinationNumber",<br>"DpyLabelCounter", "DpyPalletNumber"|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|eBRdb|XFP_OFENTETE|NUMLOTPHARMA, PRIORITE, CODEREFERENCE, STABILITE, UNITEEQUPOIDS,<br>CODEREFERENCECLIENT, SECTIONAFFECTATION, ORIGINE, CODETRANS,<br>CODEMOTIF, NBEDITION||StringValue||Value (if type String)|
|eBRdb|XFP_OFENTETE,XFP_OFENTETECDP|EQUIVALENTPOIDS, NUMEDITMEO, COMPTEURTICKET , NBPALETTE||FloatValue||Value (if type Numerical)|
|eBRdb|XFP_OFENTETE,XFP_OFENTETECDP|.DTDATELANCEMENTPREVUE, DTDATEDEBUTPESEE, DTDATEFINPESEE||DatetimeValue||Value (if type DateTime)|
|----|----|----||Sequence|||
||||~~**OperationExecutionStatus**~~||~~**Work Order status**~~||
|----|----|smallint||OperationExecutionStatusSiteId|||
|----|----|N,S,C,I,L,F,E,P,T,A,R,V||OperationExecutionStatusKey|||
|----|----|Cancel<br>Closured<br>Created<br>In progress<br>Launched<br>Manufacturing in progress<br>Manufacturing terminated<br>Preparation in progress<br>Preparation Terminated<br>Ready for manufacturing<br>Reconciled<br>ServedCancel||Name||Cancel<br>Closured<br>Created<br>In progress<br>Launched<br>Manufacturing in progress<br>Manufacturing terminated<br>Preparation in progress<br>Preparation Terminated<br>Ready for manufacturing<br>Reconciled<br>ServedCancel|
||||~~**OperationRequest**~~||**Process Instruction**||
|----|----|smallint||OperationRequestSiteId|||
|eBRdb|E2S_PIHEADER|PICODE+'_'+PIVERSION||OperationRequestKey|||
|eBRdb|E2S_PIHEADER|TRIM(PICODE)||Name||Process instruction code|
|eBRdb|E2S_PIHEADER|PICODE+'_'+PIVERSION||Description||Contains the concatenation of PI code and Version|
|eBRdb|E2S_PIHEADER|DATEDEBVALID||StartDateTime||The validity of process instruction (beginning date)|
|eBRdb|E2S_PIHEADER|DATEFINVALID||EndDateTime||The validity of process instruction (ending date)|
||||~~**OperationResponse**~~||**Task**||
|----|----|smallint||OperationResponseSiteId|||
|eBRdb|XFP_OFLIGNESP,E2S_PFC_TASK_MAN|NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+DOSE unionall TASKID||OperationResponseKey|||
|eBRdb|XFP_OFLIGNESP,E2S_PFC_TASK_MAN|PHASE unionall TASKID||Name||Unique identifier of the task|
|----|XFP_OFLIGNESP,E2S_PFC_TASK_MAN|Phase: '+PHASE+' - Sequence: '+NUMSEQPHASE unionall TITLE||Description||Task description|
|eBRdb|XFP_OFLIGNESP|NUMSEQPHASE||Sequence|||
|----|----|smallint||OperationDefinitionId|||
|----|----|----|----|----|----|----|
|----|----|smallint||OperationExecutionId<br>||Identity of the work order|
|eBRdb|XFP_OFLIGNESP,E2S_PFC_TASK_MAN|NUMOF+'_'+INDICEOF unionall MANCODE+'_'+MANINDEX|NUMOF+'_'+INDICEOF unionall MANCODE+'_'+MANINDEX|NUMOF+'_'+INDICEOF unionall MANCODE+'_'+MANINDEX|NUMOF+'_'+INDICEOF unionall MANCODE+'_'+MANINDEX|NUMOF+'_'+INDICEOF unionall MANCODE+'_'+MANINDEX|
|----|----|----||~~OperationResponseStatusId~~|||
|----|----|smallint||MaterialDefinitionId||Item identifier|
|eBRdb|XFP_OFLIGNESP|TRIM(XOLP.CODEART)|TRIM(XOLP.CODEART)|TRIM(XOLP.CODEART)|TRIM(XOLP.CODEART)|TRIM(XOLP.CODEART)|
|eBRdb|----|smallint||EquipmentId|||
|----|----|----|----|----|----|----|
|eBRdb|----|smallint||OperationRequestId||Process instructions code and version used for record of the data|
|eBRdb|E2S_PFC_TASK_MAN|PFCCODE+'_'+PFCVERSION|PFCCODE+'_'+PFCVERSION|PFCCODE+'_'+PFCVERSION|PFCCODE+'_'+PFCVERSION|PFCCODE+'_'+PFCVERSION|
|eBRdb|XFP_OFLIGNESP|QTETHEO||ProducedQuantity||Theorical quantity to weigh.|
|----|----|----||ReworkedQuantity|||
|----|----|----||ScrapQuantity|||
|eBRdb|XFP_OFLIGNESP|XOLP.UNITEPESEE||UomId||The weigh unit|
|eBRdb|E2S_PFC_TASK_MAN|CREATIONDATE||StartDateTime||Date of creation of the task|
|eBRdb|E2S_PFC_TASK_MAN|TIMESTAMP||EndDateTime||Date of the last modification of the status value<br>If the execution of the task is finished, this date represents the end date of<br>the task|
|----|----|----||Duration|||
||||~~**OperationResponseClass**~~||**Task type**||
|----|----|smallint||OperationResponseClassSiteId|||


|----|----|10,50,51,80,0,4,7,11,100,12,99,9,70,52,53,13,16,3,8,81,15,5,Task,1,6,60,14,2,WorkO<br>rderDetail|Col4|OperationResponseClassKey|Col6|Col7|
|---|---|---|---|---|---|---|
|----|----|Allocation,And Begin,And<br>End,AnomalyPI,Begin,Combining,Consumption,ControlCommand,End,EPE,EventPI,<br>Move,NULL,Or Begin,Or End,PI,Plugin<br>Task,Reconciliation,Release,RemarkPI,Requisition,Script,Task,Text,Tranfer,Transitio<br>n,Wait,Weight,WorkOrderDetail||Name<br>||'Allocation,And Begin,And<br>End,AnomalyPI,Begin,Combining,Consumption,ControlCommand,End,EPE,E<br>ventPI,Move,NULL,Or Begin,Or End,PI,Plugin<br>Task,Reconciliation,Release,RemarkPI,Requisition,Script,Task,Text,Tranfer,T<br>ransition,Wait,Weight,WorkOrderDetail|
||||~~**OperationResponseLaborSpecification**~~|~~**OperationResponseLaborSpecification**~~|**Task trace for operator actions**||
|----|----|smallint||OperationResponseLaborSpecificationSiteId|||
|eBRdb|E2S_PFC_TASK_MAN_TRAIL|BATCHID+'_'+TASKID+ '_'+USERNAME+'_'+DATEHOUR||OperationResponseLaborSpecificationKey|||
|----|----|smallint||LaborId||User login responsible for the record|
|eBRdb|E2S_PFC_TASK_MAN_TRAIL|trim(USERNAME)|trim(USERNAME)|trim(USERNAME)|trim(USERNAME)|trim(USERNAME)|
|----|----|smallint||OperationResponseId||Identity of the task|
|eBRdb|E2S_PFC_TASK_MAN_TRAIL|TASKID|TASKID|TASKID|TASKID|TASKID|
|----|----|DATEHOUR||StartDateTime<br>||Date of the recorded data<br>|
||||~~**OperationResponseOperationResponseClass**~~|~~**OperationResponseOperationResponseClass**~~|~~**Relation between Task and Task type**~~|~~**Relation between Task and Task type**~~|
|----|----|smallint||OperationResponseOperationResponseClassSiteId|||
|eBRdb|E2S_PFC_TASK_MAN,XFP_OFLIGNESP,<br>E2S_PFC_TASK_MAN|TASKID+'_Task' unionall<br>NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+DOSE+'_WorkOrderDeta<br>il' unionall TASKID+'_TaskType'||OperationResponseOperationResponseClassKey|||
|----|----|smallint||OperationResponseId||Identity of the task|
|eBRdb|E2S_PFC_TASK_MAN,XFP_OFLIGNESP,<br>E2S_PFC_TASK_MAN|TASKID unionall NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+,DOSE<br>unionall TASKID|TASKID unionall NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+,DOSE<br>unionall TASKID|TASKID unionall NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+,DOSE<br>unionall TASKID|TASKID unionall NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+,DOSE<br>unionall TASKID|TASKID unionall NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+,DOSE<br>unionall TASKID|
|----|----|smallint||OperationResponseClassId||Identity of the task type|
|eBRdb|E2S_PFC_TASK_MAN|Task','WorkOrderDetail',TYPE|Task','WorkOrderDetail',TYPE|Task','WorkOrderDetail',TYPE|Task','WorkOrderDetail',TYPE|Task','WorkOrderDetail',TYPE|
||||~~**OperationResponseParameter**~~|~~**OperationResponseParameter**~~|**Process Instruction Parameter**||
|----|----|smallint||OperationResponseParameterSiteId|||
|eBRdb|E2S_PARAMETER_HEADER|PARAMETERCODE+'_'+PARAMETERVERSION||OperationResponseParameterKey|||
|eBRdb|E2S_PARAMETER_HEADER|PARAMETERCODE||Name||Code of a parameter|
|eBRdb|E2S_PARAMETER_HEADER|DESCRIPTION||Description||Description of a parameter|
|eBRdb|E2S_PARAMETER_HEADER|FAMILY||FAMILY||Family of a parameter|
|----|----|smallint||OperationResponseParameterStatusId||Identity of the parameter status|
|eBRdb|E2S_PARAMETER_HEADER|STATUS|STATUS|STATUS|STATUS|STATUS|
|eBRdb|E2S_PARAMETER_HEADER|LASTVERSION||LASTVERSION<br>||Flag determining if this is the record of the highest version of a parameter|
||||~~**OperationResponseParameterStatus**~~|~~**OperationResponseParameterStatus**~~|**Status of a PI parameter**||
|----|----|smallint||OperationResponseParameterStatusSiteId|||
|----|----|C,V,S||OperationResponseParameterStatusKey|||
|----|----|Created,Validated,Obsolete||Name<br>||Created, Validated, Obsolete|
||||~~**OperationResponseParameterValue**~~|~~**OperationResponseParameterValue**~~|**Value of a PI parameter**||
|----|----|smallint||OperationResponseParameterValueSiteId|||
|eBRdb|E2S_PIDATA_MAN,E2S_PFC_TASK_MA<br>N|MANCODE+'_'+MANINDEX+'_'+BATCHID+'_'+PARAMETERCODE+'_'+OPERATIONNU<br>MBER+'_'+BROWSINGINDEX+'_'+INPUTINDEX,'_'+TAGNUMBER+'_'+TASKID+'_'+CM<br>DINDEX||OperationResponseParameterValueKey|||
|----|----|smallint||AnomalyOperationRequestId||PICode and version when an anomaly occurs|
|eBRdb|E2S_PIHEADER_MAN|ANOMALYPICODE+'_'+PIVERSION|ANOMALYPICODE+'_'+PIVERSION|ANOMALYPICODE+'_'+PIVERSION|ANOMALYPICODE+'_'+PIVERSION|ANOMALYPICODE+'_'+PIVERSION|
|----|----|smallint||LaborId||User login responsible for the record|
|eBRdb|E2S_PIDATA_MAN|OPERATOR|OPERATOR|OPERATOR|OPERATOR|OPERATOR|
|----|----|smallint||MaterialDefinitionId||Final product code of the work order in which the data was recorded|
|eBRdb|XFP_OFENTETE|CODEPRODUIT|CODEPRODUIT|CODEPRODUIT|CODEPRODUIT|CODEPRODUIT|
|----|----|smallint||OperationExecutionId||Identity of the work order|
|eBRdb|E2S_PIDATA_MAN|MANCODE+'_'+MANINDEX|MANCODE+'_'+MANINDEX|MANCODE+'_'+MANINDEX|MANCODE+'_'+MANINDEX|MANCODE+'_'+MANINDEX|
|----|----|smallint||OperationRequestId||Identity of the process instruction|
|eBRdb|E2S_PIDATA_MAN|PICODE+'_'+PIVERSION|PICODE+'_'+PIVERSION|PICODE+'_'+PIVERSION|PICODE+'_'+PIVERSION|PICODE+'_'+PIVERSION|
|----|----|smallint||OperationResponseId||Identity of the work order task|
|eBRdb|E2S_PFC_TASK_MAN|TASKID|TASKID|TASKID|TASKID|TASKID|


|----|----|smallint|Col4|OperationResponseParameterId|Col6|Identity of the parameter|
|---|---|---|---|---|---|---|
|eBRdb|E2S_PIDATA_MAN,E2S_PIPARAMETER<br>MAN|PARAMETERCODE+'_'+PARAMETERVERSION|PARAMETERCODE+'_'+PARAMETERVERSION|PARAMETERCODE+'_'+PARAMETERVERSION|PARAMETERCODE+'_'+PARAMETERVERSION|PARAMETERCODE+'_'+PARAMETERVERSION|
|----|----|smallint||OperationResponseParameterValueEbrStatusId||Identity of the parameter EBR status|
|eBRdb|E2S_PIHEADER_MAN|EBRSTATUS|EBRSTATUS|EBRSTATUS|EBRSTATUS|EBRSTATUS|
|----|----|smallint||OperationResponseParameterValueProcessingModeId||Identity of the execution mode|
|eBRdb|E2S_PIHEADER_MAN|PROCESSINGMODE|PROCESSINGMODE|PROCESSINGMODE|PROCESSINGMODE|PROCESSINGMODE|
|----|----|smallint||OperationResponseParameterValueStatusId||Identity of the parameter status|
|eBRdb|E2S_PIHEADER_MAN|STATUS|STATUS|STATUS|STATUS|STATUS|
|----|----|smallint||RemarkOperationRequestId||Identity of the PI when a remark occurs|
|eBRdb|E2S_PIHEADER_MAN|REMARKPICODE+'_'+PIVERSION|REMARKPICODE+'_'+PIVERSION|REMARKPICODE+'_'+PIVERSION|REMARKPICODE+'_'+PIVERSION|REMARKPICODE+'_'+PIVERSION|
|eBRdb|E2S_PIDATA_MAN|UNIT||UomId||UoM of numeric parameter. This field exists if the parameter type is<br>numeric|
|eBRdb|E2S_PIDATA_MAN|WHEN DATATYPE IN (2,3) THEN DATEVALUE||DatetimeValue||Value of date parameter. Exists if the parameter type is date|
|eBRdb|E2S_PIDATA_MAN|WHEN DATATYPE = 1 THEN NUMVALUE||FloatValue||Value of the parameter. Exists if the parameter is numeric|
|eBRdb|E2S_PIDATA_MAN|FORCED||ForcedValue||Defines if the flag has been forced|
|eBRdb|E2S_METADATAVALUE_MAN|VALUE||HighLimit||High limit value|
|eBRdb|E2S_PIDATA_MAN|INPUTDATE||InputDateTime||Date the data was recorded|
|eBRdb|E2S_METADATAVALUE_MAN|VALUE||LowLimit||Low limit value|
|eBRdb|E2S_PIDATA_MAN|WHEN DATATYPE = 0 THEN TEXTVALUE||StringValue<br>||Value of text parameter. Exist if the parameter type is text|
||||~~**OperationResponseParameterValueEbrStatus**~~|~~**OperationResponseParameterValueEbrStatus**~~|**EBR status**||
|----|----|smallint||OperationResponseParameterValueEbrStatusSiteId|||
|----|----|A,P,T,V,I,R,E||OperationResponseParameterValueEbrStatusKey|||
|----|----|Approved,AwaitingAlertProcessing,AwaitingReview,AwaitingValidation,PreparationI<br>nProgress,Rejected,ReviewInProgress||Name<br>||Approved,AwaitingAlertProcessing,AwaitingReview,AwaitingValidation,Prep<br>arationInProgress,Rejected,ReviewInProgress|
||||~~**OperationResponseParameterValueProcessingMode**~~|~~**OperationResponseParameterValueProcessingMode**~~|**Execution Mode**||
|----|----|smallint||OperationResponseParameterValueProcessingModeSiteId|||
|----|----|3,1,0||OperationResponseParameterValueProcessingModeKey|||
|----|----|ExecutionTest,Manufacturing,Simulation||Name||ExecutionTest,Manufacturing,Simulation|
||||~~**OperationRequestStatus**~~||**Process Instruction Status**||
|----|----|smallint||OperationRequestStatusSiteId|||
|----|----|A,C,L,O,Q||OperationRequestStatusKey|||
|----|----|Accepted,Created,Launched,Obsolet,ToBeQualified||Name||Accepted,Created,Launched,Obsolet,ToBeQualified|
||||~~**OperationResponseProperty**~~||**Task Property**||
|----|----|smallint||OperationResponsePropertySiteId|||
|eBRdb|E2S_METADATAVALUE_MAN|Dose','Tolerance','DoseNumber','SetWeighingMod','SetBalanceNumber','UniqueLot<br>','ActivePotency','WorkCenter','ReconcilWorkCenter','WinDpy','Manufacturing','Pac||OperationResponsePropertyKey|||
|eBRdb|E2S_METADATAVALUE_MAN|Dose','Tolerance','DoseNumber','SetWeighingMod','SetBalanceNumber','UniqueLot<br>','ActivePotency','WorkCenter','ReconcilWorkCenter','WinDpy','Manufacturing','Pac<br>kaging','WeighLevelAgreement','WinDpyLineNumber','WorkshopLineNumber','Dpy<br>OrderNumber','RemainTheoQuantity','Control','StockUnit','RfCheck','CompensatorI<br>ndex','ToCompensateIndex','Combination','SubType'<br>,'AutoExecution','Forced','ErrorOccurred','ErrorDescription','ExecutionMode','Assign<br>edUser','AssignedWorkStation','WorkStation','UserAction',NAME||Name||'Dose','Tolerance','DoseNumber','SetWeighingMod','SetBalanceNumber','U<br>niqueLot','ActivePotency','WorkCenter','ReconcilWorkCenter','WinDpy','Ma<br>nufacturing','Packaging','WeighLevelAgreement','WinDpyLineNumber','Wor<br>kshopLineNumber','DpyOrderNumber','RemainTheoQuantity','Control','Stoc<br>kUnit','RfCheck','CompensatorIndex','ToCompensateIndex','Combination','S<br>ubType'<br>,'AutoExecution','Forced','ErrorOccurred','ErrorDescription','ExecutionMode<br>','AssignedUser','AssignedWorkStation','WorkStation','UserAction',NAME|
|----|----|Numeric, String||PropertyTypeId<br>|||
||||~~**OperationResponsePropertyStaticValue**~~|~~**OperationResponsePropertyStaticValue**~~|**Task Property value**||
|----|----|smallint||OperationResponsePropertyStaticValueSiteId|||
|eBRdb|XFP_OFLIGNESP,E2S_METADATAVALU<br>E_MAN,E2S_METADATASET_MAN,E2S<br>_PFC_TASK_MAN,E2S_PFC_TASK_MAN<br>_TRAIL|NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+DOSE+'_'+OEPROPERTY<br>KEY    (refer to bm20private.ORPROPERTY) unionall<br>E2S_METADATASET_MAN.TASKID,'_'+E2S_METADATAVALUE_MAN.NAME+'_'+E2S<br>_METADATAVALUE_MAN.FK_METADATASET unionall<br>E2S_PFC_TASK_MAN.TASKID'_'+ORPROPERTYKEY  (refer to<br>bm20private.ORPROPERTYFROMTASK) unionall TASKID+'_'+ORPROPERTYKEY (refer<br>to bm20private.ORPROPERTYFROMTASKTRAIL)||OperationResponsePropertyStaticValueKey|||
|----|----|smallint||OperationResponseId||Identity of the task|


|eBRdb|XFP_OFLIGNESPE2S_METADATASET_M<br>AN,E2S_PFC_TASK_MAN,E2S_PFC_TAS<br>K_MAN_TRAIL|NUMOF+'_'+INDICEOF+'_'+PHASE+'_'+NUMSEQPHASE+'_'+DOSE (refer to<br>bm20private.ORPROPERTY) unionall E2S_METADATASET_MAN.TASKID unionall<br>E2S_PFC_TASK_MAN.TASKID (refer to bm20private.ORPROPERTYFROMTASK)<br>unionall TASKID (refer to bm20private.ORPROPERTYFROMTASKTRAIL)|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|----|----|smallint||OperationResponsePropertyId||Identity of the property|
|eBRdb|E2S_METADATAVALUE_MAN|SetWeighingMod, "UniqueLot", "ActivePotency", "WorkCenter",<br>"ReconcilWorkCenter", "WinDpy", "Manufacturing", "Packaging",<br>"WeighLevelAgreement", "WinDpyLineNumber",<br>"WorkshopLineNumber","DpyOrderNumber", "Control", "StockUnit", "RfCheck",<br>"CompensatorIndex", "ToCompensateIndex", "Combination" unionall ("Dose",<br>"Tolerance", "DoseNumber", "SetBalanceNumber", "RemainTheoQuantity")<br>unionall E2S_METADATAVALUE_MAN.NAME unionall "SubType",<br>"ErrorDescription", "ExecutionMode", "AssignedUser", "AssignedWorkstation"<br>unionall "AutoExecution", "Forced", "ErrorOccurred" unionall "WorkCenter",<br>"WorkStation", "UserAction"|SetWeighingMod, "UniqueLot", "ActivePotency", "WorkCenter",<br>"ReconcilWorkCenter", "WinDpy", "Manufacturing", "Packaging",<br>"WeighLevelAgreement", "WinDpyLineNumber",<br>"WorkshopLineNumber","DpyOrderNumber", "Control", "StockUnit", "RfCheck",<br>"CompensatorIndex", "ToCompensateIndex", "Combination" unionall ("Dose",<br>"Tolerance", "DoseNumber", "SetBalanceNumber", "RemainTheoQuantity")<br>unionall E2S_METADATAVALUE_MAN.NAME unionall "SubType",<br>"ErrorDescription", "ExecutionMode", "AssignedUser", "AssignedWorkstation"<br>unionall "AutoExecution", "Forced", "ErrorOccurred" unionall "WorkCenter",<br>"WorkStation", "UserAction"|SetWeighingMod, "UniqueLot", "ActivePotency", "WorkCenter",<br>"ReconcilWorkCenter", "WinDpy", "Manufacturing", "Packaging",<br>"WeighLevelAgreement", "WinDpyLineNumber",<br>"WorkshopLineNumber","DpyOrderNumber", "Control", "StockUnit", "RfCheck",<br>"CompensatorIndex", "ToCompensateIndex", "Combination" unionall ("Dose",<br>"Tolerance", "DoseNumber", "SetBalanceNumber", "RemainTheoQuantity")<br>unionall E2S_METADATAVALUE_MAN.NAME unionall "SubType",<br>"ErrorDescription", "ExecutionMode", "AssignedUser", "AssignedWorkstation"<br>unionall "AutoExecution", "Forced", "ErrorOccurred" unionall "WorkCenter",<br>"WorkStation", "UserAction"|SetWeighingMod, "UniqueLot", "ActivePotency", "WorkCenter",<br>"ReconcilWorkCenter", "WinDpy", "Manufacturing", "Packaging",<br>"WeighLevelAgreement", "WinDpyLineNumber",<br>"WorkshopLineNumber","DpyOrderNumber", "Control", "StockUnit", "RfCheck",<br>"CompensatorIndex", "ToCompensateIndex", "Combination" unionall ("Dose",<br>"Tolerance", "DoseNumber", "SetBalanceNumber", "RemainTheoQuantity")<br>unionall E2S_METADATAVALUE_MAN.NAME unionall "SubType",<br>"ErrorDescription", "ExecutionMode", "AssignedUser", "AssignedWorkstation"<br>unionall "AutoExecution", "Forced", "ErrorOccurred" unionall "WorkCenter",<br>"WorkStation", "UserAction"|SetWeighingMod, "UniqueLot", "ActivePotency", "WorkCenter",<br>"ReconcilWorkCenter", "WinDpy", "Manufacturing", "Packaging",<br>"WeighLevelAgreement", "WinDpyLineNumber",<br>"WorkshopLineNumber","DpyOrderNumber", "Control", "StockUnit", "RfCheck",<br>"CompensatorIndex", "ToCompensateIndex", "Combination" unionall ("Dose",<br>"Tolerance", "DoseNumber", "SetBalanceNumber", "RemainTheoQuantity")<br>unionall E2S_METADATAVALUE_MAN.NAME unionall "SubType",<br>"ErrorDescription", "ExecutionMode", "AssignedUser", "AssignedWorkstation"<br>unionall "AutoExecution", "Forced", "ErrorOccurred" unionall "WorkCenter",<br>"WorkStation", "UserAction"|
|eBRdb|XFP_OFLIGNESP,E2S_METADATAVALU<br>E_MAN,E2S_PFC_TASK_MAN,E2S_PFC<br>_HEADER_MAN,E2S_PFC_TASK_MAN_<br>TRAIL|MODEPESEEIMPOSE,UNSEULLOT,TITREACTIF,TITREACTIF,POSTEDERECONCIL,PESAB<br>LECDP,PESABLEATELIER,PESABLECONDIT,NIVEAUACCEPTEPESER,NBLIGNESPESEESC<br>DP,NBLIGNESPESEESATELIER,NUMORDRECDP,CONTROLE,UNITESTOCK,CONTROLER<br>F,INDCOMPENSATEUR,INDACOMPENSER,MEO unionall<br>E2S_METADATAVALUE_MAN.VALUE unionall<br>SUBTYPE,ERRORDESC,E2S_PFC_HEADER_MAN.EXECUTIONMODE,E2S_PFC_HEADER<br>_MAN.ASSIGNEDUSER,E2S_PFC_HEADER_MAN.ASSIGNEDWORKSTATION unionall<br>max(WORKCENTER),max(WORKSTATION),max(USERACTION)||StringValue||Value if property of type string|
|eBRdb|XFP_OFLIGNESP,E2S_PFC_TASK_MAN|DOSE,TOLE,NOMBREDEDOSES,NOBALANCEIMPOSEE,QTETHEORES unionall<br>AUTOEXEC,FORCED,ERROROCCURED||FloatValue||Value if property  of type numeric|
||||~~**OperationResponseStatus**~~||**Status of the task**||
|----|----|smallint||OperationResponseStatusSiteId|||
|----|----|0,6,2,5,4,1,3||OperationResponseStatusKey|||
|----|----|Available,Cancelled,Complete,Error,Forbidden,InProgress,Unavailable||Name||Available,Cancelled,Complete,Error,Forbidden,InProgress,Unavailable|
||||~~**PropertyType**~~||**Type of a property**||
|----|----|"String" or "Numeric" or "DateTime"||PropertyTypeKey||"String" or "Numeric" or "DateTime"|
|----|----|"String" or "Numeric" or "DateTime"||Name|||
||||~~**Uom**~~||**Property unit**||
|eBRdb|XFP_OFMO_UNITE|UNITE||UomKey|||
|eBRdb|XFP_OFMO_UNITE|UNITE||Name||Name|
||||~~**Workstation**~~||**Workstation**||
|----|----|smallint||WorkstationSiteId|||
|eBRdb|XFP_OFRESULTS,<br>EQP_EQPEXE_TRAIL|(POSTEPHYSIQUE OR POSTEDERECONCIL OR POSTEDERECONCILRF OR POSTEMEO)<br>OR<br>WORKSTATION||WorkstationKey|||
|eBRdb|XFP_OFRESULTS,<br>EQP_EQPEXE_TRAIL|(POSTEPHYSIQUE OR POSTEDERECONCIL OR POSTEDERECONCILRF OR POSTEMEO)<br>OR<br>WORKSTATION||Name||Workstation name|
||||~~**Workcenter**~~||**Work Center**||
|----|----|smallint||WorkcenterSiteId|||
|eBRdb|XFP_OFRESULTS,<br>EQP_EQPEXE_TRAIL|POSTEDECHARGE OR<br>WORKCENTER||WorkcenterKey|||
|eBRdb|XFP_OFRESULTS,<br>EQP_EQPEXE_TRAIL|POSTEDECHARGE OR<br>WORKCENTER||Name||Work center name|


