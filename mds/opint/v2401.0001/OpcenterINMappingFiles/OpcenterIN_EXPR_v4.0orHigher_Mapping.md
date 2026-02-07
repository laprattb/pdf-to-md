|Opcenter Execution Process Entities|Col2|Col3|Opcenter Intelligence Model Entities|Col5|Opcenter Execution Process – Public object model entities|Col7|
|---|---|---|---|---|---|---|
|**Database**<br>**Name**|**Entity**|**Attribute**|~~**Entity**~~<br>|~~**Attribute - Tables**~~|**Entity exposed by POM**|**Mapping Info**|
||||~~**BillOfMaterial**~~||**BoM/Bill of Materials**||
|----|----|<site_id>||BillOfMaterialSiteId|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Id||BillOfMaterialKey|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Name + "_" + Revision||Name|||
|UAPIdb|vBillOfMaterials_Si_1599946022|Description||Description|||
|UAPIdb|vBillOfMaterials_Si_1599946022|QuantityValue_Refe_1623823649||Quantity|||
|UAPIdb|vBillOfMaterials_Si_1599946022|UoMNId.ReferenceQuantity||UomId|||
||||~~**BillOfMaterialItem**~~||**BoM Item/ Bill of Materials Item**||
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
||||~~**Equipment**~~||**Equipment**||
|----|----|<site_id>||EquipmentSiteId|||
|UAPIdb|vEquipment_Siemens__2037264456|Nid||EquipmentKey|||
|UAPIdb|vEquipment_Siemens__2037264456|Name or Nid||Name|||
|UAPIdb|vEquipment_Siemens__2037264456|Description||Description|||
||||~~**EquipmentClass**~~||**Equipment Group / Equipment Type**||
|----|----|<site_id>||EquipmentClassSiteId|||
|UAPIdb|vEquipmentGroup_Sie_1867483323<br>vEquipmentType_Siemen_12677547|Nid||EquipmentClassKey|||
|UAPIdb|vEquipmentGroup_Sie_1867483323<br>vEquipmentType_Siemen_12677547|Name or Nid||Name|||
|UAPIdb|vEquipmentGroup_Sie_1867483323<br>vEquipmentType_Siemen_12677547|Description||Description|||
||||~~**EquipmentEquipmentClass**~~||**Relation between Equipment and**<br>**Equipment Group / Type**||
|----|----|<site_id>||EquipmentEquipmentClassSiteId|||
|UAPIdb|vEquipmentGroup-To-<br>_1926046055,vEquipmentGroup_Sie_1867483323<br>vEquipmentConfigura 2026297865|Equipment_Id + '_' + EquipmentGroup_Id<br>Id||EquipmentEquipmentClassKey|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vEquipment_Siemens__2037264456|Nid|||||
|----|----|<site_id>||EquipmentClassId|||
|UAPIdb|vEquipmentGroup_Sie_1867483323<br>vEquipmentConfigura_2026297865|NId<br>EquipmentTypeNId|||||
||||~~**EquipmentHierarchy**~~||**Equipment Hierarchy**|Locations have been deprecated and must<br>be modeled as Equipment|
|----|----|<site_id>||EquipmentHierarchySiteId|||
|UAPIdb|vEquipment_Siemens__2037264456|Id||EquipmentHierarchyKey|||
|----|----|<site_id>||ParentEquipmentId|||
|UAPIdb|vEquipmentGraphNode__200408322|EquipmentNId|||||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vEquipment_Siemens__2037264456|NId|||||
||||~~**EquipmentProperty**~~||**Equipment Property**||
|----|----|<site_id>||EquipmentPropertySiteId|||
|UAPIdb|vEquipmentProperty__1827472024|NId||EquipmentPropertyKey|||
|----|----|"Numeric" or "DateTime" or "String"||PropertyTypeKey|||
|UAPIdb|vEquipmentProperty__1827472024|NId||Name|||
|UAPIdb|vEquipmentProperty__1827472024|NId||Description|||
||||~~**EquipmentPropertyStaticValue**~~||**Equipment Property Value**||
|----|----|<site_id>||EquipmentPropertyStaticValueSiteId|||
|UAPIdb|vEquipmentProperty__1827472024|Id||EquipmentPropertyStaticValueKey|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vEquipment_Siemens__2037264456|NId|||||
|----|----|<site_id>||EquipmentPropertyId|||
|UAPIdb|vEquipmentProperty__1827472024|NId|||||
|UAPIdb|vEquipmentProperty__1827472024|PropertyValue||DatetimeValue|||


|UAPIdb|vEquipmentProperty__1827472024|PropertyValue|Col4|FloatValue|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vEquipmentProperty__1827472024|PropertyValue||StringValue|||
||||~~**Labor**~~||**none**|Locations have been deprecated and must<br>be modeled as Equipment.|
|----|----|<site_id>||LaborSiteId|||
|UAPIdb|vPerson_Siemens_Sima_950534528<br>vProductionHistoryR_1247477467|NId<br>User||LaborKey|||
|UAPIdb|vPerson_Siemens_Sima_950534528<br>vProductionHistoryR_1247477467|FullName<br>User||Name|||
|UAPIdb|vPerson_Siemens_Sima_950534528|Description||Description|||
||||~~**MaterialClass**~~||**Material Group**||
|----|----|<site_id>||MaterialClassSiteId|||
|UAPIdb|vMaterialGroup_Siem_2035655829|NId||MaterialClassKey|||
|UAPIdb|vMaterialGroup_Siem_2035655829|Name||Name|||
|UAPIdb|vMaterialGroup_Siem_2035655829|Description||Description|||
||||~~**MaterialDefinition**~~||**Material**||
|----|----|<site_id>||MaterialDefinitionSiteId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id||MaterialDefinitionKey|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Name or Nid||Name|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Description||Description|||
|UAPIdb|vMaterial_Siemens_Si_170253665|NId||Identifier|||
||||~~**MaterialDefinitionMaterialClass**~~||**Relation between material and material**<br>**group**||
|----|----|<site_id>||MaterialDefinitionMaterialClassSiteId|||
|UAPIdb|vMaterial-To-Materia_299161986|Material_Id + "_"MaterialGroup_Id||MaterialDefinitionMaterialClassKey|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial-To-Materia_299161986|Material_Id|||||
|----|----|<site_id>||MaterialClassId|||
|UAPIdb|vMaterialGroup_Siem_2035655829|NId|||||
||||~~**MaterialDefinitionPropertyStaticValue**~~|~~**MaterialDefinitionPropertyStaticValue**~~|**Material Property value**|Value of "Revision" attribute or any other<br>User Field|
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
||||~~**MaterialLot**~~||**Material Tracking Unit/MTU**||
|----|----|<site_id>||MaterialLotSiteId|||
|UAPIdb|MaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|NId||MaterialLotKey|||
|UAPIdb|MaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|Name||Name|||
|UAPIdb|MaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|Description||Description|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|MaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|Id|||||
|UAPIdb|MaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|QuantityValue.Quantity||Quantity|||
|UAPIdb|MaterialTrackingUni_494706508,<br>vMaterial_Siemens_Si_170253665|UoMNId.Quantity||UomId|||
|----|----|<site_id>||MaterialLotStatusId|||
|UAPIdb|MaterialTrackingUni_494706508|StatusNId.Status|||||
||||~~**MaterialLotOperation**~~||**MTU Operation**||
|----|----|<site_id>||MaterialLotOperationSiteId|||
|UAPIdb|vMTUOperationTracki_1251369089|Id||MaterialLotOperationKey|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vMaterialTrackingUni_494706508|DestinationMTUNId|||||
|UAPIdb|vMTUOperationTracki_1251369089|Timestamp||OperationDateTime|||


|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|SourceQuantity|Col4|ActualQuantity|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|DestinationQuantity||OperationQuantity|||
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|DestinationUoMNId||UomId|||
|----|----|<site_id>||SourceMaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|----|----|<site_id>||SourceMaterialLotId|||
|UAPIdb|vMaterialTrackingUn_1441307385|SourceMTUNId|||||
|UAPIdb|vMTUOperationTracki_1251369089,<br>vMTUOperationMateri_1953736380|SourceUoMNId||SourceUomId|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vMTUOperationTracki_1251369089|DestinationEquipmentNId|||||
|----|----|<site_id>||SourceEquipmentId|||
|UAPIdb|vMTUOperationTracki_1251369089|SourceEquipmentNId|||||
||||~~**MaterialLotOperationClass**~~||**MTU Operation Type (Move;**<br>**Contribution, Preparation,)**||
|----|----|<site_id>||MaterialLotOperationClassSiteId|||
|UAPIdb|vMTUOperationType_S_1999203700|NId||MaterialLotOperationClassKey|||
|UAPIdb|vMTUOperationType_S_1999203700|Name||Name|||
|UAPIdb|vMTUOperationType_S_1999203700|Description||Description<br>|||
||||~~**MaterialLotOperationMaterialLotOperationClass**~~|~~**MaterialLotOperationMaterialLotOperationClass**~~|**MTU Opeation related to the MTU**<br>**Operation Type**||
|----|----|<site_id>||MaterialLotOperationMaterialLotOperationClassSiteId|||
|UAPIdb|vMTUOperationTracki_1251369089|Id||MaterialLotOperationMaterialLotOperationClassKey|||
|----|----|<site_id>||MaterialLotOperationId|||
|UAPIdb|vMTUOperationTracki_1251369089|Id|||||
|----|----|<site_id>||MaterialLotOperationClassId|||
|UAPIdb|vMTUOperationType_S_1999203700|Nid|||||
||||~~**MaterialLotPropertyStaticValue**~~||**Material Tracking Unit /MTU Property**<br>**Value**||
|----|----|<site_id>||MaterialLotPropertyStaticValueSiteId|||
|UAPIdb|vMaterialTrackingUn_1899383600,<br>MaterialTrackingUni_494706508|prop.Id or mtu.Id||MaterialLotPropertyStaticValueKey|||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|MaterialTrackingUni_494706508|NId|||||
|----|----|<site_id>||MaterialPropertyId|||
|UAPIdb|vMaterialTrackingUn_1899383600|prop.Nid or 'LotCode'|||||
|UAPIdb|MaterialTrackingUni_494706508|vMaterialTrackingUni_494706508.PropertyValue or<br>null||DatetimeValue|||
|UAPIdb|MaterialTrackingUni_494706508|vMaterialTrackingUni_494706508.PropertyValue or<br>null||FloatValue|||
|UAPIdb|MaterialTrackingUni_494706508<br>vMaterialLot_Siemen_1503124121|vMaterialTrackingUni_494706508.PropertyValue or<br>vMaterialLot_Siemen_1503124121.Nid or<br>null||StringValue|||
||||~~**MaterialLotStatus**~~||~~**Material Tracking Unit/MTU Status**~~||
|----|----|<site_id>||MaterialLotStatusSiteId|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|NId||MaterialLotStatusKey|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Name||Name|||
|UAPIdb|'vStatus_Siemens_Sim_2045546455|Description||Description|||
||||~~**MaterialProperty**~~||**Material /MTU Property**||
|----|----|<site_id>||MaterialPropertySiteId|||
|UAPIdb|vMaterialProperty_S_1277555573 or<br>vMaterialLotPropert_2085247210 or<br>vMaterialTrackingUn_1899383600<br>MaterialTrackingUni 494706508|NId or<br>"Revision" or<br>"LotCode"||MaterialPropertyKey|||
|UAPIdb|vMaterialProperty_S_1277555573 or<br>vMaterialLotPropert_2085247210 or<br>vMaterialTrackingUn_1899383600<br>MaterialTrackingUni 494706508|"String" or "Numeric" or "DateTime"||PropertyTypeId|||
|UAPIdb|vMaterialProperty_S_1277555573 or<br>vMaterialLotPropert_2085247210 or<br>vMaterialTrackingUn_1899383600<br>MaterialTrackingUni 494706508|NId or<br>"Revision" or<br>"LotCode"||Name|||
||||~~**OperationDefinition**~~||**Operation/Task Definition/Process**<br>**Definition**||
|----|----|<site_id>||OperationDefinitionSiteId|||
|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,<br>vProcessDefinition<br>1680138349|Id||OperationDefinitionKey|||
|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,<br>vProcessDefinition<br>1680138349|Name or Nid||Name|||


|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,<br>vProcessDefinition 1680138349|Description|Col4|Description|Col6|Col7|
|---|---|---|---|---|---|---|
||||~~**OperationDefinitionProperty**~~||**Task Definition Property**||
|----|----|<site_id>||OperationDefinitionPropertySiteId|||
|UAPIdb|VTaskDefinitionParam_745321786|Nid or "Revision"||OperationDefinitionPropertyKey|||
|UAPIdb|VTaskDefinitionParam_745321786|Nid or "Revision"||Name|||
|----|----|"Numeric" or "DateTime" or "String"||PropertyTypeId<br>|||
||||~~**OperationDefinitionPropertyStaticValue**~~|~~**OperationDefinitionPropertyStaticValue**~~|**Operation/ Task Definition/Task**<br>**Definition Property Value**||
|----|----|<site_id>||OperationDefinitionPropertyStaticValueSiteId|||
|UAPIdb|vOperation_Siemens__1738138217 or<br>vTaskDefinition_Sieme_81158749 or<br>VTaskDefinitionParam 745321786|VTaskDefinitionParam_745321786.Id or<br>"Revision_" +  vOperation_Siemens__1738138217.Id or<br>"Revision " + vTaskDefinition Sieme 81158749 .Id||OperationDefinitionPropertyStaticValueKey|||
|----|----|<site_id>||OperationDefinitionId|||
|UAPIdb|VTaskDefinitionParam_745321786 or<br>vTaskDefinition_Sieme_81158749 or<br>vOperation Siemens<br>1738138217|vTaskDefinition_Sieme_81158749.Id or<br>vOperation_Siemens__1738138217.Id or<br>VTaskDefinitionParam 745321786.TaskDefinition Id|||||
|----|----|<site_id>||OperationDefinitionPropertyId|||
|----|VTaskDefinitionParam_745321786 or<br>vTaskDefinition_Sieme_81158749 or<br>vOperation Siemens<br>1738138217|Nid or "Revision"|||||
|UAPIdb|VTaskDefinitionParam_745321786|ParameterValue or null||DatetimeValue|||
|UAPIdb|VTaskDefinitionParam_745321786|ParameterValue or null||FloatValue|||
|UAPIdb|VTaskDefinitionParam_745321786|ParameterValue or null or "Revision"||StringValue|||
||||~~**OperationExecution**~~||**Work Order/Work Order Operation**||
|----|----|<site_id>||OperationExecutionSiteId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|wo.NId, o.Nid||OperationExecutionKey|||
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
|UAPIdb|Order_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359|ActualStartTime_Wo_1764370633 - ActualEndTime_Work_1288523718 or datediff(SECOND, o.ActualStartTime, coalesce(o.ActualEndTime,<br>getutcdate())||Duration|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|QuantityValue.Quantity||PlannedQuantity|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|UoMNId.Quantity||PlannedQuantityUomId|||
|UAPIdb|vWorkOrderFacet_Siem_649674359<br>vOrder_Siemens_Simati_69827994|PlannedStartTime_W_1465081062<br>PlannedStartTime||PlannedStartDateTime|||
|UAPIdb|vWorkOrderFacet_Siem_649674359<br>vOrder_Siemens_Simati_69827994|PlannedEndTime_Work_643170049<br>PlannedEndTime||PlannedEndDateTime|||
||||~~**OperationExecutionClass**~~||**Work Order Type**||
|----|----|<site_id>||OperationExecutionClassSiteId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder Siemens Simati 69827994|TemplateNId or 'Order from External System' or Type_WorkOrderExte_1192338604 or Type||OperationExecutionClassKey|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder Siemens Simati 69827994|TemplateNId or 'Order from External System' or Type_WorkOrderExte_1192338604 or Type||Name||Template Id or 'Order from External<br>System'|
||||~~**OperationExecutionHierarchy**~~||**Relation between Order and Work**<br>**Orders**||
|----|----|<site_id>||OperationExecutionHierarchySiteId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vWorkOrderFacet_Siem_649674359|Id||OperationExecutionHierarchyKey|||
|----|----|<site_id>||ParentOperationExecutionId|||


|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994|p.Nid|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459|Nid|||||
||||~~**OperationExecutionHistory**~~||||
|----|----|<site_id>||OperationExecutionHistorySiteId|||
|UAPIdb|vProductionHistoryR_1247477467|Id||OperationExecutionHistoryKey|||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vProductionHistoryR_1247477467|SourceNId|||||
|UAPIdb|vProductionHistoryR_1247477467|Timestamp||StartDateTime|||
|UAPIdb|vProductionHistoryR_1247477467|LEAD(Timestamp,1) over(partition by SourceId order by Timestamp)||EndDateTime|||
|----|----|DATEDIFF(SECOND, StartDateTime, EndDateTime)||Duration|||
|----|----|<site_id>||OperationExecutionStatusId|||
|UAPIdb|vProductionHistoryR_2066796202|NewValue|||||
|----|----|<site_id>||LaborId|||
|UAPIdb|vProductionHistoryR_1247477467|User|||||
||||~~**OperationExecutionOperationExecutionClass**~~|~~**OperationExecutionOperationExecutionClass**~~|**Releation between Work Order and its**<br>**type**||
|----|----|<site_id>||OperationExecutionOperationExecutionClassSiteId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder Siemens Simati 69827994|Id||OperationExecutionOperationExecutionClassKey|||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder Siemens Simati 69827994|NId|||||
|----|----|<site_id>||OperationExecutionClassId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459,<br>vOrder_Siemens_Simati_69827994,<br>vWorkOrderFacet_Siem_649674359,<br>vOrder Siemens Simati 69827994|TemplateNId or 'Order from External System' or Type_WorkOrderExte_1192338604 or Type|||||
||||~~**OperationExecutionProperty**~~||**Work Order Properties**||
|----|----|<site_id>||OperationExecutionPropertySiteId|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterNId + '_Target' or ParameterNId + '_Actual'  or 'PlannedStartDateTime' or 'PlannedEndDateTime'||OperationExecutionPropertyKey|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterName + '_Target' or ParameterName + '_Actual' or ParameterNId + '_Target' or  ParameterNId + '_Actual' or 'PlannedStartDateTime' or<br>'PlannedEndDateTime'||Name|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterDescription + '_Target' or 'ParameterDescription + '_Actual' or 'PlannedStartDateTime' or 'PlannedEndDateTime'||Description|||
|----|----|Numeric' or DateTime' or 'String'||PropertyTypeId|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterUoMNId||UomId|||
|UAPIdb|'vWorkOrderHeaderPar_1415093556|0||Multivalue<br>|||
||||~~**OperationExecutionPropertyStaticValue**~~|~~**OperationExecutionPropertyStaticValue**~~|**Work Order Property Values**||
|----|----|<site_id>||OperationExecutionPropertyStaticValueSiteId|||
|UAPIdb|vWorkOrderHeaderPar_1415093556,<br>vWorkOrderFacet_Siem_649674359|wop.Id + '_Target' or wop.Id + '_Actual' or (wofacet.Id + '_' +'PlannedStartDateTime') or (wofacet.Id + '_' +'PlannedEndDateTime')||OperationExecutionPropertyStaticValueKey|||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459|NId|||||
|----|----|<site_id>||OperationExecutionPropertyId|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterNId + '_Target' or  ParameterNId + '_Actual' or 'PlannedStartDateTime' or 'PlannedEndDateTime'|||||
|UAPIdb|vWorkOrderHeaderPar_1415093556|ParameterTargetValue or null or ParameterActualValue||StringValue|||
|UAPIdb|vWorkOrderHeaderPar_1415093556,vWorkOrder_Siemen<br>s_S_552758459|ParameterTargetValue or null or ParameterActualValue||FloatValue|||
|UAPIdb|vWorkOrderHeaderPar_1415093556,vWorkOrderFacet_Si<br>em_649674359|ParameterTargetValue or PlannedStartTime_W_1465081062 or PlannedEndTime_Work_643170049 or null or ParameterActualValue||DatetimeValue|||
|UAPIdb|vWorkOrderHeaderPar_1415093556|null||Sequence|||
||||~~**OperationExecutionStatus**~~||**Status**||
|----|----|<site_id>||OperationExecutionStatusSiteId|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|NId||OperationExecutionStatusKey|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Name||Name|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Description||Description|||
||||~~**OperationRequest**~~||**Work Order Operation (planning)**||
|----|----|<site_id>||OperationRequestSiteId|||
|UAPIdb|vWorkOrderOperation__171792286|WorkOrderOperation_Id||OperationRequestKey|||
|UAPIdb|vWorkOrderOperation__171792286|Name or NId||Name|||
|UAPIdb|vWorkOrderOperation__171792286|Description||Description|||
|UAPIdb|vWorkOrderOperation_1396136903|PlannedStartTime_W_2087574194||StartDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|PlannedEndTime_Wor_1658088037||EndDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|EstimatedDuration__1986550722||Duration|||


|Col1|Col2|Col3|OperationResponse|Col5|Work Order Operations/Tasks/Work<br>Processes|Col7|
|---|---|---|---|---|---|---|
|----|----|<site_id>||OperationResponseSiteId|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|wop.Id, t.Id, wp.Id, Id||OperationResponseKey|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|wop.[Name], wop.Nid or t.[Name], t.Nid or wp.[Name], wp.Nid, OperationNId||Name|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|wop.Description, t.escription, wp.Description, [Description]||Description|||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vWorkOrderOperation_1396136903|wopfacet.ActualEquipmentNId__815480860|||||
|----|----|<site_id>||OperationResponseStatusId|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess Siemen 1784161351|wop.StatusNId.Status or t.StatusNId.Status or wp.StatusNId.Status|||||
|----|----|<site_id>||OperationDefinitionId|||
|UAPIdb|vOperation_Siemens__1738138217,<br>vTaskDefinition_Sieme_81158749,|td.Id or od.Id|||||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|WorkOrder_Siemens_S_552758459,<br>vOrderOperation_Sie_2000999366|wo.NId, o.Nid|||||
|----|----|<site_id>||OperationRequestId|||
|----|vWorkOrderOperation_1396136903|WorkOrderOperation_Id|||||
|UAPIdb|vWorkOrderOperation_1396136903,<br>vWorkProcess_Siemen_1784161351|ActualStartTime_Wo_1768620685 or ProcessDefinitionTimestamp||StartDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualEndTime_Work_1985974042||EndDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685 - ActualEndTime_Work_1985974042||Duration|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|Sequence or Sequence.TaskFlow||Sequence|||
|UAPIdb|vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|Nid||Identifier|||
||||~~**OperationResponseClass**~~||**Task Type**||
|----|----|<site_id>||OperationResponseClassSiteId|||
|UAPIdb|vTaskType_Siemens_S_1938738239|Nid, 'Operation', 'WorkProcess', 'OrderOperation'||OperationResponseClassKey|||
|UAPIdb|vTaskType_Siemens_S_1938738239|Name, 'Operation', 'WorkProcess', 'OrderOperation'||Name||'Operation', 'WorkProcess',<br>'OrderOperation'|
|UAPIdb|vTaskType_Siemens_S_1938738239|Description||Description<br>|||
||||~~**OperationResponseEquipmentSpecification**~~|~~**OperationResponseEquipmentSpecification**~~|**Work Order Equipment Requirements**||
|----|----|<site_id>||OperationResponseEquipmentSpecificationSiteId|||
|UAPIdb|vWorkOrderOperation_1945809747|Id||OperationResponseEquipmentSpecificationKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation_1945809747|WorkOrderOperation_Id|||||
|UAPIdb|vWorkOrderOperation_1945809747|ActualEquipmentNId||EquipmentId|||
||||~~**OperationResponseHierarchy**~~||**Relation between Work Order and Tasks**||
|----|----|<site_id>||OperationResponseHierarchySiteId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation_1504451725|id||OperationResponseHierarchyKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkProcess_Siemen_1784161351|Id|||||
|----|----|<site_id>||ParentOperationResponseId|||
|UAPIdb|vWorkOrderOperation__171792286|p.id|||||
||||~~**OperationResponseHistory**~~||||
|----|----|<site_id>||OperationResponseHistorySiteId|||
|UAPIdb|vProductionHistoryR_1247477467|Id||OperationResponseHistoryKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vProductionHistoryR_1247477467|SourceId|||||
|UAPIdb|vProductionHistoryR_1247477467|Timestamp||StartDateTime|||
|UAPIdb|vProductionHistoryR_1247477467|LEAD(Timestamp,1) over(partition by SourceId order by Timestamp||EndDateTime|||
|----|----|DATEDIFF(SECOND, StartDateTime, EndDateTime)||Duration|||
|----|----|<site_id>||OperationResponseStatusId|||


|UAPIdb|vProductionHistoryR_2066796202|NewValue|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|----|----|<site_id>||LaborId|||
|UAPIdb|vProductionHistoryR_1247477467|User|||||
||||~~**OperationResponseMaterialDefinitionRequirementIn**~~|~~**OperationResponseMaterialDefinitionRequirementIn**~~|||
|----|----|<site_id>||OperationResponseMaterialDefinitionRequirementInSiteId|||
|UAPIdb|vWorkOrderOperation_2072960688|Id||OperationResponseMaterialDefinitionRequirementInKey|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation_2072960688|Id|||||
|UAPIdb|vWorkOrderOperation_2072960688|QuantityValue.Quantity||Quantity|||
|UAPIdb|vWorkOrderOperation_2072960688|UoMNId.Quantity||UomKey<br>|||
||||~~**OperationResponseMaterialLotSpecificationIn**~~|~~**OperationResponseMaterialLotSpecificationIn**~~|**Actual Materials**||
|----|----|<site_id>||OperationResponseMaterialLotSpecificationInSiteId|||
|UAPIdb|vActualMaterialMTU__1871174980|Id||OperationResponseMaterialLotSpecificationInKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation__171792286|id|||||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vActualMaterialMTU__1871174980|MTUNId|||||
|UAPIdb|vActualMaterialMTU__1871174980|QuantityValue.Quantity||Quantity|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685||StartDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualEndTime_Work_1985974042||EndDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685 - ActualEndTime_Work_1985974042||Duration<br>|||
||||~~**OperationResponseMaterialLotSpecificationOut**~~|~~**OperationResponseMaterialLotSpecificationOut**~~|**Materials**||
|----|----|<site_id>||OperationResponseMaterialLotSpecificationOutSiteId|||
|UAPIdb|vActualMaterialMTU__1871174980|Id||OperationResponseMaterialLotSpecificationOutKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation__171792286|id|||||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vActualMaterialMTU__1871174980|MTUNId|||||
|UAPIdb|vActualMaterialMTU__1871174980|QuantityValue.Quantity||Quantity|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualStartTime_Wo_1768620685||StartDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|ActualEndTime_Work_1985974042||EndDateTime|||
|UAPIdb|vWorkOrderOperation_1396136903|datediff(ActualStartTime_Wo_1768620685,ActualEndTime_Work_1985974042)||Duration<br>|||
||||~~**OperationResponseOperationResponseClass**~~|~~**OperationResponseOperationResponseClass**~~|**Relation between Task/Work Order**<br>**Operation/Work Process/Order**<br>**Operation and Task Type**||
|----|----|<site_id>||OperationResponseOperationResponseClassSiteId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation__171792286,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|Id||OperationResponseOperationResponseClassKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation__171792286,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|Id|||||
|----|----|<site_id>||OperationResponseClassId|||
|UAPIdb|vTask_Siemens_Simati_357457326,<br>vWorkOrderOperation__171792286,<br>vWorkProcess_Siemen_1784161351,<br>vOrderOperation Sie 2000999366|TaskTypeNId, 'Operation', 'WorkProcess', 'OrderOperation'|||||
||||~~**OperationResponseProperty**~~||**Work Order Operation Parameter**<br>**Specification/Work Order Operation**<br>**User Fields/Task Property**||
|----|----|<site_id>||OperationResponsePropertySiteId|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.ParameterNId or<br>vWorkOrderOperation_1075185191.ParameterNId+'_Target' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterNId+'_LimitHigh' or<br>vWorkOrderOperationUs_34178630.Nid or<br>vTaskParameter_Sieme_400426804.Nid or<br>vWorkProcessVariable 519271362.Nid||OperationResponsePropertyKey|||


|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|(vWorkOrderOperation_1075185191.ParameterName or<br>vWorkOrderOperation_1075185191.ParameterNId) or<br>(vWorkOrderOperation_1075185191.ParameterName+ ' Target' or<br>vWorkOrderOperation_1075185191.ParameterNId+ ' Target') or<br>(vWorkOrderOperation_1075185191.ParameterName+ ' LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterNId+ ' LimitLow') or<br>(vWorkOrderOperation_1075185191.ParameterName+ ' ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterNId+ ' ToleranceLow') or<br>(vWorkOrderOperation_1075185191.ParameterName+ ' ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterNId+ ' ToleranceHigh') or<br>(vWorkOrderOperation_1075185191.ParameterName+ ' LimitHigh' or<br>vWorkOrderOperation_1075185191.ParameterNId+ ' LimitHigh') or<br>vWorkOrderOperationUs_34178630.Nid or<br>vTaskParameter_Sieme_400426804.Nid or<br>(vWorkProcessVariable_519271362.ShortNId or<br>vWorkProcessVariable 519271362.Nid)|Col4|Name|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.ParameterDescription or<br>vWorkOrderOperation_1075185191.ParameterDescription+' Target' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterDescription+' LimitHigh' or<br>vWorkProcessVariable_519271362.Nid or<br>null||Description|||
|----|----|Numeric' or 'DateTime' or 'String'||PropertyTypeId|||
|UAPIdb|vWorkOrderOperation_1075185191|vWorkOrderOperation_1075185191.ParameterUoMNId or null||UomId<br>|||
||||~~**OperationResponsePropertyStaticValue**~~|~~**OperationResponsePropertyStaticValue**~~|**Work Order Operation Parameter**<br>**Specification/Work Order Operation**<br>**User Fields/Task Parameter/Work**<br>**Process Property Value**||
|----|----|<site_id>||OperationResponsePropertyStaticValueSiteId|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable_519271362|vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' +vWorkOrderOperation_1075185191.ParameterNId or<br>vWorkOrderOperation_1075185191WorkOrderOperation_Id + '_' + vWorkOrderOperation_1075185191.ParameterNId+ '_Target' or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' + vWorkOrderOperation_1075185191.ParameterNId + '_LimitLow'  or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' + vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceLow' or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' + vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceHigh' or<br>vWorkOrderOperation_1075185191.WorkOrderOperation_Id + '_' + vWorkOrderOperation_1075185191.ParameterNId + '_LimitHigh' or<br>vWorkOrderOperationUs_34178630.Id or vTaskParameter_Sieme_400426804.Id or vWorkProcessVariable_519271362.Id||OperationResponsePropertyStaticValueKey|||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperation__171792286,<br>vTask_Siemens_Simati_357457326,<br>vWorkProcess Siemen 1784161351|vWorkOrderOperation_1075185191.WorkOrderOperation_Id or<br>vWorkOrderOperation__171792286.Id or<br>vTask_Siemens_Simati_357457326.Id or<br>vWorkProcess Siemen 1784161351.Id|||||
|----|----|<site_id>||OperationResponsePropertyId|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vTaskParameter_Sieme_400426804,<br> vWorkProcessVariable_519271362,<br>vWorkOrderOperationUs_34178630|vWorkOrderOperation_1075185191.ParameterNId  or<br>vWorkOrderOperation_1075185191.ParameterNId + '_Target' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_LimitLow' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceLow' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_ToleranceHigh' or<br>vWorkOrderOperation_1075185191.ParameterNId + '_LimitHigh' or<br>vWorkOrderOperationUs 34178630.Nid or vTaskParameter Sieme 400426804.Nid or vWorkProcessVariable 519271362.Nid|||||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable 519271362|ParameterActualValue or ParameterTargetValue or UserFieldValue or ParameterValue or VariableValue or null||StringValue|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter_Sieme_400426804,<br>vWorkProcessVariable 519271362|ParameterActualValue or ParameterTargetValue or ParameterLimitLow or ParameterToleranceLow or ParameterToleranceHigh or<br>ParameterLimitHigh or UserFieldValue or ParameterValue or VariableValue or null||FloatValue|||
|UAPIdb|vWorkOrderOperation_1075185191,<br>vWorkOrderOperationUs_34178630,<br>vTaskParameter Sieme 400426804|ParameterActualValue or ParameterTargetValue or UserFieldValue or ParameterValue  or null||DatetimeValue|||
||||~~**OperationResponseStatus**~~||**Status**||
|----|----|<site_id>||OperationResponseStatusSiteId|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|NId||OperationResponseStatusKey|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Name||Name|||
|UAPIdb|vStatus_Siemens_Sim_2045546455|Description||Description|||
||||~~**OperationScheduling**~~||**Work Master**||
|----|----|<site_id>||OperationSchedulingSiteId|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Id||OperationSchedulingKey|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Name or Nid||Name|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Description||Description|||
|UAPIdb|VWorkMaster_Siemens_1174780169|UoMNId.Quantity||UomId|||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|UAPIdb|VWorkMaster_Siemens_1174780169|QuantityValue.Quantity||EstimatedQuantity|||
|UAPIdb|VWorkMaster_Siemens_1174780169|NId||Identifier|||
||||~~**OperationSchedulingClass**~~||**Work Master**||


|----|----|<site_id>|Col4|OperationSchedulingClassSiteId|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|VWorkMaster_Siemens_1174780169|Type||OperationSchedulingClassKey|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Type||Name|||
|UAPIdb|VWorkMaster_Siemens_1174780169|null||Description<br>|||
||||~~**OperationSchedulingOperationSchedulingClass**~~|~~**OperationSchedulingOperationSchedulingClass**~~|**Work Master**||
|----|----|<site_id>||OperationSchedulingOperationSchedulingClassSiteId|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Id||OperationSchedulingOperationSchedulingClassKey|||
|----|----|<site_id>||OperationSchedulingClassId|||
|UAPIdb|VWorkMaster_Siemens_1174780169|Type|||||
|----|----|<site_id>||OperationSchedulingId|||
|UAPIdb|'VWorkMaster_Siemens_1174780169|Id|||||
||||~~**OperationSchedulingProperty**~~||**Work Master Header Parameter**||
|----|----|<site_id>||OperationSchedulingPropertySiteId|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterNId or<br>'Revision'||OperationSchedulingPropertyKey|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterName or ParameterNId or<br>'Revision'||Name|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterDescription or<br>'Revision'||Description|||
|UAPIdb|vWorkMasterHeaderPa_1578763129|ParameterUoMNId or<br>NULL||UomId|||
|----|----|Numeric' or 'DateTime' or 'String'||PropertyTypeId<br>|||
||||~~**OperationSchedulingPropertyStaticValue**~~|~~**OperationSchedulingPropertyStaticValue**~~|**Work Master Header Parameter Values**||
|----|----|<site_id>||OperationSchedulingPropertyStaticValueSiteId|||
|UAPIdb|vWorkMasterHeaderPa_1578763129,<br>VWorkMaster_Siemens_1174780169|Id or<br>Id + '_Revision'||OperationSchedulingPropertyStaticValueKey|||
|----|----|<site_id>||OperationSchedulingId|||
|UAPIdb|VWorkMaster_Siemens_1174780169,<br>VWorkMaster_Siemens_1174780169|id|||||
|UAPIdb|vWorkMasterHeaderPa_1578763129,<br>VWorkMaster_Siemens_1174780169|ParameterNId or<br>'Revision'||OperationSchedulingPropertyId|||
|----|----|<site_id>|||||
|UAPIdb|vWorkMasterHeaderPa_1578763129,<br>VWorkMaster_Siemens_1174780169|ParameterTargetValue or null||DatetimeValue|||
|UAPIdb|vWorkMasterHeaderPa_1578763129,<br>VWorkMaster_Siemens_1174780169|ParameterTargetValue or null||FloatValue|||
|UAPIdb|vWorkMasterHeaderPa_1578763129,<br>VWorkMaster_Siemens_1174780169|ParameterTargetValue or null or<br>Revision||StringValue|||
||||**Parameter**||||
|----|----|<site_id>||ParameterSiteId|||
|UAPIdb|vResultParameter_Si_1808344069|Name||ParameterKey|||
|UAPIdb|vResultParameter_Si_1808344069|Name||Name|||
|UAPIdb|vResultParameter_Si_1808344069|Description||Description|||
||||**ParameterGroup**||||
|----|----|<site_id>||ParameterGroupSiteId|||
|UAPIdb|vParameterGroup_Sie_1984142957|Id||ParameterGroupKey|||
|UAPIdb|vParameterGroup_Sie_1984142957|Name||Name|||
|UAPIdb|vParameterGroup_Sie_1984142957|Description||Description|||
||||**ParameterResult**||||
|----|----|<site_id>||ParameterResultSiteId|||
|UAPIdb|vResultParameter_Si_1808344069|Id||ParameterResultKey|||
|----|----|<site_id>||ParameterId|||
|UAPIdb|vResultParameter_Si_1808344069|Name|||||
|----|----|<site_id>||ParameterGroupId|||
|UAPIdb|vResultParameter_Si_1808344069|ParameterGroup_Id|||||
|----|----|<site_id>||SampleResultId|||
|UAPIdb|vResultParameter_Si_1808344069|SampleResult_Id|||||
|UAPIdb|vResultParameter_Si_1808344069|ActualValue||FloatValue|||
|UAPIdb|vResultParameter_Si_1808344069|ActualValue||StringValue|||
|UAPIdb|vResultParameter_Si_1808344069|Uom||UomId|||
|UAPIdb|vResultParameter_Si_1808344069|AnalysisResult||Result|||
|UAPIdb|vResultParameter_Si_1808344069|Comment||Comment|||
|UAPIdb|vResultParameter_Si_1808344069|Reanalysis||Reanalysis|||
|UAPIdb|vResultParameter_Si_1808344069|LowerLimit||LowerLimit|||
|UAPIdb|vResultParameter_Si_1808344069|UpperLimit||UpperLimit|||
|UAPIdb|vResultParameter_Si_1808344069|LowSpec||LowSpec|||
|UAPIdb|vResultParameter_Si_1808344069|HighSpec||HighSpec|||
|UAPIdb|vResultParameter_Si_1808344069|LowDeviation||LowDeviation|||


|UAPIdb|vResultParameter_Si_1808344069|HighDeviation|Col4|HighDeviation|Col6|Col7|
|---|---|---|---|---|---|---|
||||~~**PropertyType**~~||**none**||
|----|----|"String" or "Numeric" or "DateTime"||PropertyTypeKey|||
|----|----|"String" or "Numeric" or "DateTime"||Name|||
|----|----|----||Description|||
||||~~**QualityExecution**~~||~~**Inspection Order**~~||
|----|----|<site_id>||QualityExecutionSiteId|||
|UAPIdb|vInspectionOrder_Si_2142042601|NId||QualityExecutionKey|||
|UAPIdb|vInspectionOrder_Si_2142042601|Name or Nid||Name|||
|UAPIdb|vInspectionOrder_Si_2142042601|Description||Description|||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vWorkOrder_Siemens_S_552758459|NId|NId|NId|||
|----|----|----||QualityExecutionStatusId|||
|----|----|----|----|----|||
|----|----|----||EquipmentId|||
|----|----|----|----|----|||
|----|----|----||MaterialDefinitionId|||
|----|----|----|----|----|||
|----|----|----||StartDateTime|||
|----|----|----||EndDateTime|||
|----|----|----||Duration|||
||||~~**QualityFailure**~~||~~**Failure**~~||
|----|----|<site_id>||QualityFailureSiteId|||
|UAPIdb|vFailure_Siemens_Op_1949421172|NId||QualityFailureKey|||
|UAPIdb|vFailure_Siemens_Op_1949421172|Name||Name|||
|UAPIdb|vFailure_Siemens_Op_1949421172|Description||Description|||
||||~~**QualityLimit**~~||~~**CharacteristicSpecification**~~||
|----|----|<site_id>||QualityLimitSiteId|||
|UAPIdb|vCharacteristicSpeci_112675600|Id||QualityLimitKey|||
|----|----|----||QualityLimitStatusId|||
|----|----|----|----|----|||
|----|----|<site_id>||QualityParameterId|||
|UAPIdb|vCharacteristicSpeci_112675600|Id|Id|Id|||
|----|----|----||StartDateTime|||
|----|----|----||EndDateTime|||
|UAPIdb|vCharacteristicSpeci_112675600|QuantityValue_Uppe_2121646290||HighLimit|||
|UAPIdb|vCharacteristicSpeci_112675600|QuantityValue_Nomi_1650198520||Target|||
|UAPIdb|vCharacteristicSpeci_112675600|QuantityValue_Lowe_1569687123||LowLimit|||
||||~~**QualityParameter**~~||~~**CharacteristicSpecification**~~||
|----|----|<site_id>||QualityParameterSiteId|||
|UAPIdb|vCharacteristicSpeci_112675600|Id||QualityParameterKey|||
|UAPIdb|vCharacteristicSpeci_112675600|NId||Name|||
|UAPIdb|vCharacteristicSpeci_112675600|Description||Description|||
|UAPIdb|vCharacteristicSpeci_112675600|UoMNId_NominalValu_2066917009||UomId|||
||||~~**QualityParameterValue**~~||||
|----|----|<site_id>||QualityParameterValueSiteId|||
|UAPIdb|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|Id||QualityParameterValueKey|||
|----|----|<site_id>||SampleId|||
|UAPIdb|vInspectionSampleFa_1591458715|SampleId_Inspection_123018035|SampleId_Inspection_123018035|SampleId_Inspection_123018035|||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|MTUNId|MTUNId|MTUNId|||
|----|----|<site_id>||LaborId|||
|UAPIdb|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|User|User|User|||
|----|----|<site_id>||QualityParameterId|||
|UAPIdb|vCharacteristicSpeci_112675600|Id|Id|Id|||
|----|----|<site_id>||QualityFailureId|||
|UAPIdb|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|FailureNId|FailureNId|FailureNId|||
|----|----|<site_id>||QualityResponseId|||
|----|----|----|----|----|||
|----|----|----||DatetimeValue|||
|UAPIdb|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|MeasuredAttributeValue OR MeasuredVariableValue<br>Count||FloatValue|||


|----|----|----|Col4|StringValue|Col6|Col7|
|---|---|---|---|---|---|---|
|UAPIdb|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|Timestamp||StartDateTime|||
|UAPIdb|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|Timestamp||EndDateTime|||
||||~~**Sample**~~||||
|----|----|<site_id>||SampleSiteId|||
|UAPIdb|vSample_Siemens_Opce_108366506|NId||SampleKey|||
|UAPIdb|vSample_Siemens_Opce_108366506|Name||Name|||
|UAPIdb|vSample_Siemens_Opce_108366506|Description||Description|||
|UAPIdb|vSample_Siemens_Opce_108366506|SampleType||SampleType|||
|----|----|<site_id>||LaborId|||
|UAPIdb|vSample_Siemens_Opce_108366506|User|||||
|----|----|<site_id>||OperationResponseId|||
|UAPIdb|vSample_Siemens_Opce_108366506|SampleWorkOrderOperationId|||||
|----|----|<site_id>||TaskOperationResponseId|||
|UAPIdb|vSample_Siemens_Opce_108366506|TaskID|||||
|----|----|<site_id>||WorkProcessOperationResponseId|||
|UAPIdb|vSample_Siemens_Opce_108366506|SampleWorkProcessId|||||
|----|----|<site_id>||OperationExecutionId|||
|UAPIdb|vSample_Siemens_Opce_108366506|SampleWorkOrderNId|||||
|----|----|<site_id>||MaterialLotId|||
|UAPIdb|vSample_Siemens_Opce_108366506|SampleMTUNId|||||
|----|----|<site_id>||SourceMaterialLotId|||
|UAPIdb|vSample_Siemens_Opce_108366506|SourceMTUNId|||||
|----|----|<site_id>||EquipmentId|||
|UAPIdb|vSample_Siemens_Opce_108366506|EquipmentNId|||||
|----|----|<site_id>||MaterialDefinitionId|||
|UAPIdb|vMaterial_Siemens_Si_170253665|Id|||||
|UAPIdb|vSample_Siemens_Opce_108366506|QuantityValue.Quantity||Quantity|||
|UAPIdb|vSample_Siemens_Opce_108366506|UoMNId.Quantity||UomdId|||
||||**SampleResult**||||
|----|----|<site_id>||SampleResultSiteId|||
|UAPIdb|vSampleResult_Sieme_2054851575|Id||SampleResultKey|||
|----|----|<site_id>||SampleId|||
|UAPIdb|vSample_Siemens_Opce_108366506|NId|||||
|UAPIdb|vSampleResult_Sieme_2054851575|Result||Result|||
|UAPIdb|vSampleResult_Sieme_2054851575|executionenddate||ExecutionEndDateTime|||
|UAPIdb|vSampleResult_Sieme_2054851575|reanalysis||Reanalysis|||
||||**SampleResultParameterGroup**||||
|----|----|<site_id>||SampleResultParameterGroupSiteId|||
|UAPIdb|vParameterGroup_Sie_1984142957|Id||SampleResultParameterGroupKey|||
|----|----|<site_id>||SampleResultId|||
|UAPIdb|vParameterGroup_Sie_1984142957|SampleResult_Id|||||
|----|----|<site_id>||ParameterGroupId|||
|UAPIdb|vParameterGroup_Sie_1984142957|Id|||||
|UAPIdb|vParameterGroup_Sie_1984142957|AnalysisResult||Result|||
|UAPIdb|vParameterGroup_Sie_1984142957|Comments||Comment|||
|UAPIdb|vParameterGroup_Sie_1984142957|reanalysis||Reanalysis|||
||||~~**Site**~~||**none**||
|----|----|----||SiteId|||
|----|----|----||TimeZoneId|||
|----|----|----||Name|||
|----|----|----||Description|||
|----|----|----||Longitude|||
|----|----|----||Latitude|||
||||~~**TimeZone**~~||**none**||
|----|----|----||TimeZoneKey|||
|----|----|----||Name|||
|----|----|----||Description|||
|----|----|----||OffSet|||
||||~~**TimeZoneDaylightTimeSaving**~~||**none**||
|----|----|----||TimeZoneDaylightTimeSavingKey|||
|----|----|----||TimeZoneId|||


|----|----|----|Col4|OffSet|Col6|Col7|
|---|---|---|---|---|---|---|
|----|----|----||DateFrom|||
|----|----|----||DateTo|||
||||~~**Uom**~~||**UoM//Unit of Measure**||
|SitmesDb|vUoM_Siemens_Simati_1027974907|Nid||UomKey|||
|SitmesDb|vUoM_Siemens_Simati_1027974907|Name||Name|||
|SitmesDb|vUoM_Siemens_Simati_1027974907|Description||Description|||
|----|----|1||UomSystemId|||
|----|----|1||UomCategoryId|||


