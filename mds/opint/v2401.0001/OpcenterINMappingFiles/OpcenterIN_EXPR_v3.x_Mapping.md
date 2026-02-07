|Opcenter Execution Process|Col2|Col3|Opcenter Intelligence Model Entities|Col5|Opcenter Execution Process – Public object model entities|Col7|
|---|---|---|---|---|---|---|
|~~**Database**~~<br>**Name**|~~**Entity**~~|~~**Attribute**~~|~~**Entity**~~<br>|~~**Attribute - Tables**~~|~~**Entity exposed by POM**~~<br>|~~**Mapping Info**~~|
||||~~**BillOfMaterial**~~||~~**BoM/Bill of Materials**~~||
|----|----|<site_id>||BillOfMaterialSiteId|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Id||BillOfMaterialKey|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Name + "_" + Revision||Name|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Description||Description|||
|UAPIdb|vBillOfMaterials_Si_1599946022|QuantityValue_Refe_1623823649||Quantity|||
|UAPIdb|vBillOfMaterials_Si_1599946022|UoMNId.ReferenceQuantity||UomId|||
||||~~**BillOfMaterialItem**~~||~~**BoM Item/ Bill of Materials Item**~~||
|----|----|<site_id>||BillOfMaterialItemSiteId|||
|UAPIdb|vBillOfMaterialsItem_740980688|Id||BillOfMaterialItemKey|||
|----|----|<site_id>||BillOfMaterialId|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Id|||||
|UAPIdb|vBillOfMaterialsItem_740980688|bi.Name, bi.id||Name|||
|UAPIdb|vBillOfMaterialsItem_740980688|Description||Description|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|MaterialNId|||||
|UAPIdb|vBillOfMaterialsItem_740980688|QuantityValue.Quantity||Quantity|||
|UAPIdb|vBillOfMaterialsItem_740980688|UoMNId.Quantity||UomId|||
||||~~**Equipment**~~||~~**Equipment**~~||
|----|----|<site_id>||EquipmentSiteId|||
|UAPIdb|vEquipment_Siemens__2037264456|Nid||EquipmentKey|||
|UAPIdb|vEquipment_Siemens__2037264456|Name or Nid||Name|||
|UAPIdb|vEquipment_Siemens__2037264456|Description||Description|||
||||~~**EquipmentClass**~~||~~**Equipment Group**~~||
|----|----|<site_id>||EquipmentClassSiteId|||
|UAPIdb|vEquipmentGroup_Sie_1867483323|Nid||EquipmentClassKey|||
|UAPIdb|vEquipmentGroup_Sie_1867483323|Name||Name|||
|UAPIdb|vEquipmentGroup_Sie_1867483323|Description||Description|||
||||~~**EquipmentEquipmentClass**~~||~~**Relation between Equipment and**~~<br>**Equipment Groupd**||
|----|----|<site_id>||EquipmentEquipmentClassSiteId|||
|UAPIdb|vEquipmentGroup-To-<br>_1926046055,vEquipmentGroup_Sie_1867<br>483323|cast(egt.Equipment_Id as nvarchar(255)) + N'_' + cast(egt.EquipmentGroup_Id as<br>nvarchar(255))||EquipmentEquipmentClassKey|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vEquipment_Siemens__2037264456|Nid|||||
|----|----|<site_id>||EquipmentClassId|||
|UAPIdb|vEquipmentGroup_Sie_1867483323|NId|||||
||||~~**EquipmentHierarchy**~~||~~**Equipment Hierarchy**~~|Locations have been deprecated and must<br>be modeled as Equipment|
|----|----|<site_id>||EquipmentHierarchySiteId|||
|UAPIdb|vWorkCenterItem_Sie_2008664163|Label||EquipmentHierarchyKey|||
|----|----|<site_id>||ParentEquipmentId|||
|UAPIdb|vWorkCenter_Siemens_1034519327|Label|||||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vWorkCenterItem_Sie_2008664163|NId|||||
||||~~**EquipmentProperty**~~||~~**Equipment Property**~~||
|----|----|<site_id>||EquipmentPropertySiteId|||
|UAPIdb|vEquipmentProperty__1827472024|NId||EquipmentPropertyKey|||
|----|----|"Numeric" or "DateTime" or "String"||PropertyTypeKey|||


|UAPIdb|vEquipmentProperty__1827472024|NId|Col4|Name|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vEquipmentProperty__1827472024|NId||Description|||
||||~~**EquipmentPropertyStaticValue**~~||~~**Equipment Property Value**~~||
|----|----|<site_id>||EquipmentPropertyStaticValueSiteId|||
|UAPIdb|vEquipmentProperty__1827472024|Id||EquipmentPropertyStaticValueKey|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vEquipment_Siemens__2037264456|NId|||||
|----|----|<site_id>||EquipmentPropertyId|||
|UAPIdb|vEquipmentProperty__1827472024|NId|||||
|UAPIdb|vEquipmentProperty__1827472024|PropertyValue||DatetimeValue|||
|UAPIdb|vEquipmentProperty__1827472024|PropertyValue||FloatValue|||
|UAPIdb|vEquipmentProperty__1827472024|PropertyValue||StringValue|||
||||~~**Location**~~||~~**none**~~|Locations have been deprecated and must<br>be modeled as Equipment.|
|----|----|<site_id>||LocationSiteId|||
|UAPIdb|vLocation_Siemens_Si_307154647|NId||LocationKey|||
|UAPIdb|vLocation_Siemens_Si_307154647|Name||Name|||
|UAPIdb|vLocation_Siemens_Si_307154647|Description||Description|||
||||~~**MaterialClass**~~||~~**Material Group**~~||
|----|----|<site_id>||MaterialClassSiteId|||
|UAPIdb|vMaterialGroup_Siem_2035655829|NId||MaterialClassKey|||
|UAPIdb|vMaterialGroup_Siem_2035655829|Name||Name|||
|UAPIdb|vMaterialGroup_Siem_2035655829|Description||Description|||
||||~~**MaterialDefinition**~~||~~**Material**~~||
|----|----|<site_id>||MaterialDefinitionSiteId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id||MaterialDefinitionKey|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Name||Name|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Description||Description|||
||||~~**MaterialDefinitionMaterialClass**~~||~~**Relation between material and**~~<br>**material group**||
|----|----|<site_id>||MaterialDefinitionMaterialClassSiteId|||
|UAPIdb|vMaterial-To-Materi_1236280494|Material_Id + "_"MaterialGroup_I||MaterialDefinitionMaterialClassKey|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial-To-Materi_1236280494|Material_Id|||||
|----|----|<site_id>||MaterialClassId|||
|UAPIdb|vMaterialGroup_Siem_2035655829|NId|||||
||||~~**MaterialDefinitionPropertyStaticValue**~~|~~**MaterialDefinitionPropertyStaticValue**~~|~~**Material Property value**~~|Value of "Revision" attribute or any other<br>User Field|
|----|----|<site_id>||MaterialDefinitionPropertyStaticValueSiteId|||
|UAPIdb|vMaterialProperty_S_1277555573,<br>vMaterial_Siemens_Si_170253665|Id or<br>"Revision_" + Id||MaterialDefinitionPropertyStaticValueKey|||
|----|----|<site_id>||MaterialPropertyId|||
|UAPIdb|vMaterialProperty_S_1277555573,<br>vMaterial_Siemens_Si_170253665|Nid or "Revision"|||||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterialProperty_S_1277555573,<br>vMaterial_Siemens_Si_170253665|Material_Id or Id|||||
|UAPIdb|vMaterialProperty_S_1277555573,<br>vMaterial_Siemens_Si_170253665|UserFieldValue or null||DatetimeValue|||
|UAPIdb|vMaterialProperty_S_1277555573,<br>vMaterial_Siemens_Si_170253665|UserFieldValue or null||FloatValue|||
|UAPIdb|vMaterialProperty_S_1277555573,<br>vMaterial_Siemens_Si_170253665|"Revision" or UserFieldValue or null||StringValue|||
|----|----|null||Sequence|||
||||~~**MaterialLot**~~||~~**Material Tracking Unit/MTU**~~||
|----|----|<site_id>||MaterialLotSiteId|||


|UAPIdb|vMaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|NId|Col4|MaterialLotKey|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vMaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|Name||Name|||
|UAPIdb|vMaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|Description||Description|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|Id|||||
|UAPIdb|vMaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|QuantityValue.Quantity||Quantity|||
|UAPIdb|vMaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|UoMNId.Quantity||UomId|||
||||~~**MaterialLotOperation**~~||~~**MTU Operation**~~||
|----|----|<site_id>||MaterialLotOperationSiteId|||
|UAPIdb|vMTUOperationTracki_1251369089|Id||MaterialLotOperationKey|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|----|----|<site_id>||LocationId|||
|UAPIdb|vMTUOperationTracki_1251369089|destinationLocationNId|||||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vMaterialTrackingUni_494706508|DestinationMTUNId|||||
|UAPIdb|vMTUOperationTracki_1251369089|Timestamp||OperationDateTime|||
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|SourceQuantity||ActualQuantity|||
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|DestinationQuantity||OperationQuantity|||
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|DestinationUoMNId||UomId|||
|----|----|<site_id>||SourceLocationId|||
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|SourceLocationNId|||||
|----|----|<site_id>||SourceMaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|----|----|<site_id>||SourceMaterialLotId|||
|UAPIdb|vMaterialTrackingUn_1441307385|SourceMTUNId|||||
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|SourceUoMNId||SourceUomId|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vMTUOperationTracki_1251369089|DestinationEquipmentNId|||||
|----|----|<site_id>||SourceEquipmentId|||
|UAPIdb|vMTUOperationTracki_1251369089|SourceEquipmentNId|||||
||||~~**MaterialLotOperationClass**~~||~~**MTU Operation Type (Move;**~~<br>**Contribution, Preparation,)**||
|----|----|<site_id>||MaterialLotOperationClassSiteId|||
|UAPIdb|vMTUOperationType_S_1999203700|NId||MaterialLotOperationClassKey|||
|UAPIdb|vMTUOperationType_S_1999203700|Name||Name|||
|UAPIdb|vMTUOperationType_S_1999203700|Description||Description<br>|||
||||~~**MaterialLotOperationMaterialLotOperationClass**~~|~~**MaterialLotOperationMaterialLotOperationClass**~~|~~**MTU Opeation related to the MTU**~~<br>**Operation Type**||
|----|----|<site_id>||MaterialLotOperationMaterialLotOperationClassSiteId|||
|UAPIdb|vMTUOperationTracki_1251369089|Id||MaterialLotOperationMaterialLotOperationClassKey|||
|----|----|<site_id>||MaterialLotOperationId|||
|UAPIdb|vMTUOperationTracki_1251369089|Id|||||
|----|----|<site_id>||MaterialLotOperationClassId|||
|UAPIdb|vMTUOperationType_S_1999203700|Nid|||||
||||~~**MaterialLotPropertyStaticValue**~~||~~**Material Tracking Unit /MTU**~~<br>**Property Value**||


|----|----|<site_id>|Col4|MaterialLotPropertyStaticValueSiteId|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vMaterialTrackingUn_1899383600,<br>vMaterialTrackingUni_494706508|prop.Id or mtu.Id||MaterialLotPropertyStaticValueKey|||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vMaterialTrackingUni_494706508|NId|||||
|----|----|<site_id>||MaterialPropertyId|||
|UAPIdb|vMaterialTrackingUn_1899383600|prop.Nid or 'LotCode'|||||
|UAPIdb|vMaterialTrackingUni_494706508|vMaterialTrackingUni_494706508.PropertyValue or<br>null||DatetimeValue|||
|UAPIdb|vMaterialTrackingUni_494706508|vMaterialTrackingUni_494706508.PropertyValue or<br>null||FloatValue|||
|UAPIdb|vMaterialTrackingUni_494706508<br>vMaterialLot_Siemen_1503124121|vMaterialTrackingUni_494706508.PropertyValue or<br>vMaterialLot_Siemen_1503124121.Nid or<br>null||StringValue|||
||||~~**MaterialProperty**~~||~~**Material /MTU Property**~~||
|----|----|<site_id>||MaterialPropertySiteId|||
|UAPIdb|vMaterialProperty_S_1277555573 or<br>vMaterialLotPropert_2085247210 or<br>vMaterialTrackingUn_1899383600<br>vMaterialTrackingUni_494706508|NId or<br>"Revision" or<br>"LotCode"||MaterialPropertyKey|||
|UAPIdb|vMaterialProperty_S_1277555573 or<br>vMaterialLotPropert_2085247210 or<br>vMaterialTrackingUn_1899383600<br>vMaterialTrackingUni_494706508|"String" or "Numeric" or "DateTime"||PropertyTypeId|||
|UAPIdb|vMaterialProperty_S_1277555573 or<br>vMaterialLotPropert_2085247210 or<br>vMaterialTrackingUn_1899383600<br>vMaterialTrackingUni_494706508|NId or<br>"Revision" or<br>"LotCode"||Name|||
||||~~**OperationDefinition**~~||~~**Operation/Task Definition/Process**~~<br>**Definition**||
|----|----|<site_id>||OperationDefinitionSiteId|||
|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,<br>vProcessDefinition__1680138349|Id||OperationDefinitionKey|||
|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,<br>vProcessDefinition__1680138349|Name or Nid||Name|||
|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,<br>vProcessDefinition__1680138349|Description||Description|||
||||~~**OperationDefinitionProperty**~~||~~**Task Definition Property**~~||
|----|----|<site_id>||OperationDefinitionPropertySiteId|||
|UAPIdb|VTaskDefinitionParam_745321786|Nid or "Revision"||OperationDefinitionPropertyKey|||
|UAPIdb|VTaskDefinitionParam_745321786|Nid or "Revision"||Name|||
|----|----|"Numeric" or "DateTime" or "String"||PropertyTypeId<br>|||
||||~~**OperationDefinitionPropertyStaticValue**~~|~~**OperationDefinitionPropertyStaticValue**~~|~~**Operation/ Task Definition/Task**~~<br>**Definition Property Value**||
|----|----|<site_id>||OperationDefinitionPropertyStaticValueSiteId|||
|UAPIdb|vOperation_Siemens__1738138217 or<br>vTaskDefinition_Sieme_81158749 or<br>VTaskDefinitionParam_745321786|VTaskDefinitionParam_745321786.Id or<br>"Revision_" +  vOperation_Siemens__1738138217.Id or<br>"Revision_" + vTaskDefinition_Sieme_81158749 .Id||OperationDefinitionPropertyStaticValueKey|||
|----|----|<site_id>||OperationDefinitionId|||
|UAPIdb|VTaskDefinitionParam_745321786 or<br>vTaskDefinition_Sieme_81158749 or<br>vOperation_Siemens__1738138217|vTaskDefinition_Sieme_81158749.Id or<br>vOperation_Siemens__1738138217.Id or<br>VTaskDefinitionParam_745321786.TaskDefinition_Id|||||
|----|----|<site_id>||OperationDefinitionPropertyId|||
|----|VTaskDefinitionParam_745321786 or<br>vTaskDefinition_Sieme_81158749 or<br>vOperation_Siemens__1738138217|Nid or "Revision"|||||
|UAPIdb|VTaskDefinitionParam_745321786|ParameterValue or null||DatetimeValue|||
|UAPIdb|VTaskDefinitionParam_745321786|ParameterValue or null||FloatValue|||
|UAPIdb|VTaskDefinitionParam_745321786|ParameterValue or null or "Revision"||StringValue|||
||||~~**OperationExecution**~~||~~**Work Order/Work Order Operation**~~||


|----|----|<site_id>|Col4|OperationExecutionSiteId|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|wo.NId, 'ERPOrder_'+ o.NId||OperationExecutionKey|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|Name||Name|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|Description||Description|||
|----|----|<site_id>||OperationExecutionStatusId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|StatusNId.Status|||||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|EquipmentNId|||||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|----|----|<site_id>||BillOfMaterialId|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Id|||||
|----|----|<site_id>||OperationSchedulingId|||
|UAPIdb|vWorkMaster_Siemens_1174780169|workmaster.Id|||||
|UAPIdb|vWorkOrderFacet_Siem_649674359,<br>vOrder_Siemens_Simati_69827994|QuantityValue.Quantity, QuantityValue_Actua_751002371||ProducedQuantity|||
|UAPIdb|Order_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359|wofacet.UoMNId_ActualQuant_1016690246 or UoMNId.Quantity||UomId|||
|UAPIdb|Order_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359|ActualStartTime, ActualStartTime_Wo_1764370633||StartDateTime|||
|UAPIdb|Order_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359|ActualEndTime, ActualEndTime_Work_1288523718||EndDateTime|||
|UAPIdb|Order_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359|ActualStartTime_Wo_1764370633 - ActualEndTime_Work_1288523718 or<br>datediff(SECOND, o.ActualStartTime, coalesce(o.ActualEndTime, getutcdate())||Duration|||
||||~~**OperationExecutionClass**~~||~~**Work Order Type**~~||
|----|----|<site_id>||OperationExecutionClassSiteId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder_Siemens_Simati_69827994|TemplateNId or 'Order from External System' or Type_WorkOrderExte_1192338604 or<br>Type||OperationExecutionClassKey|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder_Siemens_Simati_69827994|TemplateNId or 'Order from External System' or Type_WorkOrderExte_1192338604 or<br>Type||Name||Template Id or 'Order from External System'|
||||~~**OperationExecutionHierarchy**~~||~~**Relation between Order and Work**~~<br>**Orders**||
|----|----|<site_id>||OperationExecutionHierarchySiteId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vWorkOrderFacet_Siem_649674359|Id||OperationExecutionHierarchyKey|||
|----|----|<site_id>||ParentOperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|p.Nid, 'ERPOrder_' + p.NId|||||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459|Nid|||||
||||~~**OperationExecutionOperationExecutionClass**~~|~~**OperationExecutionOperationExecutionClass**~~|~~**Releation between Work Order and**~~<br>**its type**||
|----|----|<site_id>||OperationExecutionOperationExecutionClassSiteId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder_Siemens_Simati_69827994|Id||OperationExecutionOperationExecutionClassKey|||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder_Siemens_Simati_69827994|NId , 'ERPOrder_' + NId|||||
|----|----|<site_id>||OperationExecutionClassId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder_Siemens_Simati_69827994|TemplateNId or 'Order from External System' or Type_WorkOrderExte_1192338604 or<br>Type|||||
||||~~**OperationExecutionProperty**~~||~~**Work Order Properties**~~||


|----|----|<site_id>|Col4|OperationExecutionPropertySiteId|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterNId or 'PlannedStartDateTime' or 'PlannedEndDateTime'  or 'PlannedQuantity'||OperationExecutionPropertyKey|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterName or 'PlannedStartDateTime' or 'PlannedEndDateTime'  or<br>'PlannedQuantity'||Name|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterDescription or 'PlannedStartDateTime' or 'PlannedEndDateTime'  or<br>'PlannedQuantity'||Description|||
|----|----|Numeric' or DateTime' or 'String'||PropertyTypeId|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterUoMNId||UomId<br>|||
||||~~**OperationExecutionPropertyStaticValue**~~|~~**OperationExecutionPropertyStaticValue**~~|~~**Work Order Property Values**~~||
|----|----|<site_id>||OperationExecutionPropertyStaticValueSiteId|||
|UAPIdb|vWorkOrderHeaderPar_1415093556,<br>vWorkOrderFacet_Siem_649674359|wop.Id or (wofacet.Id + '_' +'PlannedStartDateTime') or (wofacet.Id + '_'<br>+'PlannedEndDateTime') or (wofacet.Id + '_' +'PlannedQuantity')||OperationExecutionPropertyStaticValueKey|||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459|NId|||||
|----|----|<site_id>||OperationExecutionPropertyId|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterNId or 'PlannedStartDateTime' or 'PlannedEndDateTime' or 'PlannedQuantity'|||||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterTargetValue or null||StringValue|||
|UAPIdb|vWorkOrderHeaderPar_1415093556,vWork<br>Order_Siemens_S_552758459|ParameterTargetValue or QuantityValue.Quantity or null||FloatValue|||
|UAPIdb|vWorkOrderHeaderPar_1415093556,vWork<br>OrderFacet_Siem_649674359|ParameterTargetValue or PlannedStartTime_W_1465081062 or<br>PlannedEndTime_Work_643170049 or null||DatetimeValue|||
||||~~**OperationExecutionStatus**~~||~~**Status**~~||
|----|----|<site_id>||OperationExecutionStatusSiteId|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|NId||OperationExecutionStatusKey|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Name||Name|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Description||Description|||
||||~~**OperationRequest**~~||~~**Work Order Operation (planning)**~~||
|----|----|<site_id>||OperationRequestSiteId|||
|UAPIdb|vWorkOrderOperation__171792286|WorkOrderOperation_Id||OperationRequestKey|||
|UAPIdb|vWorkOrderOperation__171792286|Name or NId||Name|||
|UAPIdb|vWorkOrderOperation__171792286|Description||Description|||
|UAPIdb|vWorkOrderOperation_1396136903|PlannedStartTime_W_2087574194||StartDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|PlannedEndTime_Wor_1658088037||EndDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|EstimatedDuration__1986550722||Duration|||
||||~~**OperationResponse**~~||~~**Work Order**~~<br>**Operations/Tasks/Work Processes**||
|----|----|<site_id>||OperationResponseSiteId|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation_Sie_2000999366|wop.Id, t.Id, wp.Id, Id||OperationResponseKey|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation_Sie_2000999366|wop.[Name], wop.Nid or t.[Name], t.Nid or wp.[Name], wp.Nid, OperationNId||Name|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation_Sie_2000999366|wop.Description, t.escription, wp.Description, [Description]||Description|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vWorkOrderOperation_1396136903|wopfacet.ActualEquipmentNId__815480860|||||
|----|----|<site_id>||OperationResponseStatusId|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351|wop.StatusNId.Status or t.StatusNId.Status or wp.StatusNId.Status|||||
|----|----|<site_id>||OperationDefinitionId|||
|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,|td.Id or od.Id|||||
|----|----|<site_id>||OperationExecutionId|||


|UAPIdb|WorkOrder_Siemens_S_552758459,<br>vOrderOperation_Sie_2000999366|wo.NId, 'ERPOrder_' + o.NId|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|----|----|<site_id>||OperationRequestId|||
|----|vWorkOrderOperation_1396136903|WorkOrderOperation_Id|||||
|UAPIdb|vWorkOrderOperation_1396136903,<br>vWorkProcess_Siemen_1784161351|ActualStartTime_Wo_1768620685 or ProcessDefinitionTimestamp||StartDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualEndTime_Work_1985974042||EndDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685 - ActualEndTime_Work_1985974042||Duration|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation_Sie_2000999366|Sequence or Sequence.TaskFlow||Sequence|||
||||~~**OperationResponseClass**~~||~~**Task Type**~~||
|----|----|<site_id>||OperationResponseClassSiteId|||
|UAPIdb|vTaskType_Siemens_S_1938738239|Nid, 'Operation', 'WorkProcess', 'OrderOperation'||OperationResponseClassKey|||
|UAPIdb|vTaskType_Siemens_S_1938738239|Name, 'Operation', 'WorkProcess', 'OrderOperation'||Name||'Operation', 'WorkProcess',<br>'OrderOperation'|
|UAPIdb|vTaskType_Siemens_S_1938738239|Description||Description<br>|||
||||~~**OperationResponseEquipmentSpecification**~~|~~**OperationResponseEquipmentSpecification**~~|~~**Work Order Equipment**~~<br>**Requirements**||
|----|----|<site_id>||OperationResponseEquipmentSpecificationSiteId|||
|UAPIdb|vWorkOrderOperation_1945809747|Id||OperationResponseEquipmentSpecificationKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation_1945809747|WorkOrderOperation_Id|||||
|UAPIdb|vWorkOrderOperation_1945809747|ActualEquipmentNId||EquipmentId|||
||||~~**OperationResponseHierarchy**~~||~~**Relation between Work Order and**~~<br>**Tasks**||
|----|----|<site_id>||OperationResponseHierarchySiteId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation_1504451725|id||OperationResponseHierarchyKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351|Id|||||
|----|----|<site_id>||ParentOperationResponseId|||
|UAPIdb|vWorkOrderOperation__171792286|p.id|||||
||||~~**OperationResponseMaterialLotSpecificationIn**~~|~~**OperationResponseMaterialLotSpecificationIn**~~|~~**Actual Materials**~~||
|----|----|<site_id>||OperationResponseMaterialLotSpecificationInSiteId|||
|UAPIdb|vActualMaterialMTU__1871174980|Id||OperationResponseMaterialLotSpecificationInKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation__171792286|id|||||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vMaterialTrackingUni_494706508|Nid|||||
|UAPIdb|vActualMaterialMTU__1871174980|QuantityValue.Quantity||Quantity|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685||StartDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualEndTime_Work_1985974042||EndDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685 - ActualEndTime_Work_1985974042||Duration<br>|||
||||~~**OperationResponseMaterialLotSpecificationOut**~~|~~**OperationResponseMaterialLotSpecificationOut**~~|~~**Materials**~~||
|----|----|<site_id>||OperationResponseMaterialLotSpecificationOutSiteId|||
|UAPIdb|vActualMaterialMTU__1871174980|Id||OperationResponseMaterialLotSpecificationOutKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation__171792286|id|||||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vMaterialTrackingUni_494706508|ml.Nid|||||
|UAPIdb|vActualMaterialMTU__1871174980|QuantityValue.Quantity||Quantity|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685||StartDateTime|||


|UAPIdb|vWorkOrderOperation_1396136903|ActualEndTime_Work_1985974042|Col4|EndDateTime|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vWorkOrderOperation_1396136903|datediff(ActualStartTime_Wo_1768620685,ActualEndTime_Work_1985974042)||Duration<br>|||
||||~~**OperationResponseOperationResponseClass**~~|~~**OperationResponseOperationResponseClass**~~|~~**Relation between Task/Work Order**~~<br>**Operation/Work Process/Order**<br>**Operation and Task Type**||
|----|----|<site_id>||OperationResponseOperationResponseClassSiteId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation__171792286,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation_Sie_2000999366|Id||OperationResponseOperationResponseClassKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation__171792286,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation_Sie_2000999366|Id|||||
|----|----|<site_id>||OperationResponseClassId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation__171792286,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation_Sie_2000999366|TaskTypeNId, 'Operation', 'WorkProcess', 'OrderOperation'|||||
||||~~**OperationResponseProperty**~~||~~**Work Order Operation Parameter**~~<br>**Specification/Work Order**<br>**Operation User Fields/Task**<br>**Property**||
|----|----|<site_id>||OperationResponsePropertySiteId|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.ParameterNId or<br>vWorkOrderOperation_1075185191.ParameterNId+'_Target' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_LimitHigh' or<br>vWorkOrderOperationUs_34178630.Nid or<br>vTaskParameter_Sieme_400426804.Nid or<br>vWorkProcessVariable_519271362.Nid||OperationResponsePropertyKey|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.ParameterName or<br>vWorkOrderOperation_1075185191.ParameterName+ ' Target' or<br>vWorkOrderOperation_1075185191.ParameterName+ ' LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterName+ ' ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterName+ ' ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterName+ ' LimitHigh' or<br>vWorkOrderOperationUs_34178630.Nid or<br>vTaskParameter_Sieme_400426804.Nid or<br>(vWorkProcessVariable_519271362.ShortNId or<br>vWorkProcessVariable_519271362.Nid)||Name|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.ParameterDescription or<br>vWorkOrderOperation_1075185191.ParameterDescription+' Target' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' LimitHigh' or<br>vWorkProcessVariable_519271362.Nid or<br>null||Description|||
|----|----|Numeric' or 'DateTime' or 'String'||PropertyTypeId|||
|UAPIdb|vWorkOrderOperation_1075185191|vWorkOrderOperation_1075185191.ParameterUoMNId or null||UomId<br>|||
||||~~**OperationResponsePropertyStaticValue**~~|~~**OperationResponsePropertyStaticValue**~~|~~**Work Order Operation Parameter**~~<br>**Specification/Work Order**<br>**Operation User Fields/Task**<br>**Parameter/Work Process Property**<br>**Value**||
|----|----|<site_id>||OperationResponsePropertyStaticValueSiteId|||


|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_'<br>+vWorkOrderOperation_1075185191.ParameterNId or<br>vWorkOrderOperation_1075185191WorkOrderOperation_Id + '_' +<br>vWorkOrderOperation_1075185191.ParameterNId+ '_Target' or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' +<br>vWorkOrderOperation_1075185191.ParameterNId + '_LimitLow' or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' +<br>vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceLow' or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' +<br>vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceHigh' or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' +<br>vWorkOrderOperation_1075185191.ParameterNId + '_LimitHigh' or<br>vWorkOrderOperationUs_34178630.Id or vTaskParameter_Sieme_400426804.Id or<br>vWorkProcessVariable_519271362.Id|Col4|OperationResponsePropertyStaticValueKey|Col6|Col7|
|---|---|---|---|---|---|---|
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351|vWorkOrderOperation_1075185191.WorkOrderOperation_Id or<br>vWorkOrderOperation__171792286.Id or<br>vTask_Siemens_Simati_357457326.Id or<br>vWorkProcess_Siemen_1784161351.Id|||||
|----|----|<site_id>||OperationResponsePropertyId|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.ParameterNId  or<br>vWorkOrderOperation_1075185191.ParameterNId + '_Target' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_LimitHigh' or<br>vWorkOrderOperationUs_34178630.Nid or vTaskParameter_Sieme_400426804.Nid or<br>vWorkProcessVariable_519271362.Nid|||||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|ParameterActualValue or ParameterTargetValue or UserFieldValue or ParameterValue or<br>VariableValue or null||StringValue|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|ParameterActualValue or ParameterTargetValue or ParameterLimitLow or<br>ParameterToleranceLow or ParameterToleranceHigh or ParameterLimitHigh or<br>UserFieldValue or ParameterValue or VariableValue or null||FloatValue|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804|ParameterActualValue or ParameterTargetValue or UserFieldValue or ParameterValue  or<br>null||DatetimeValue|||
||||~~**OperationResponseStatus**~~||~~**Status**~~||
|----|----|<site_id>||OperationResponseStatusSiteId|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|NId||OperationResponseStatusKey|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Name||Name|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Description||Description|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|CreatedOn||RowInserted|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|LastUpdatedOn||RowUpdated|||
||||~~**OperationScheduling**~~||~~**Work Master**~~||
|----|----|<site_id>||OperationSchedulingSiteId|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Id||OperationSchedulingKey|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Name or Nid||Name|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Description||Description|||
|UAPIdb|VWorkMaster_Siemens_1174780169|UoMNId.Quantity||UomId|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|UAPIdb|VWorkMaster_Siemens_1174780169|QuantityValue.Quantity||EstimatedQuantity|||
||||~~**OperationSchedulingProperty**~~||~~**Work Master Header Parameter**~~||
|----|----|<site_id>||OperationSchedulingPropertySiteId|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterNId||OperationSchedulingPropertyKey|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterName||Name|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterDescription||Description|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterUoMNId||UomId|||
|----|----|Numeric' or 'DateTime' or 'String'||PropertyTypeId|||


|Col1|Col2|Col3|OperationSchedulingPropertyStaticValue|Col5|Work Master Header Parameter<br>Values|Col7|
|---|---|---|---|---|---|---|
|----|----|<site_id>||OperationSchedulingPropertyStaticValueSiteId|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|Id||OperationSchedulingPropertyStaticValueKey|||
|----|----|<site_id>||OperationSchedulingId|||
|UAPIdb|VWorkMaster_Siemens_1174780169|id|||||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterNId||OperationSchedulingPropertyId|||
|----|----|<site_id>|||||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterTargetValue or null||DatetimeValue|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterTargetValue or null||FloatValue|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterTargetValue or null||StringValue|||
||||~~**PropertyType**~~||~~**none**~~||
|----|----|"String" or "Numeric" or "DateTime"||PropertyTypeKey|||
|----|----|"String" or "Numeric" or "DateTime"||Name|||
||||~~**Site**~~||~~**none**~~||
|----|----|----||SiteId|||
|----|----|----||TimeZoneId|||
|----|----|----||Name|||
|----|----|----||Description|||
|----|----|----||Longitude|||
|----|----|----||Latitude|||
||||~~**TimeZone**~~||~~**none**~~||
|----|----|----||TimeZoneKey|||
|----|----|----||Name|||
|----|----|----||Description|||
|----|----|----||OffSet|||
||||~~**TimeZoneDaylightTimeSaving**~~||~~**none**~~||
|----|----|----||TimeZoneDaylightTimeSavingKey|||
|----|----|----||TimeZoneId|||
|----|----|----||OffSet|||
|----|----|----||DateFrom|||
|----|----|----||DateTo|||
||||~~**Uom**~~||~~**UoM//Unit of Measure**~~||
|SitmesDb|vUoM_Siemens_Simati_1027974907|Nid||UomKey|||
|SitmesDb|vUoM_Siemens_Simati_1027974907|Name||Name|||
|SitmesDb|vUoM_Siemens_Simati_1027974907|Description||Description|||
|----|----|1||UomSystemId|||
|----|----|1||UomCategoryId|||


