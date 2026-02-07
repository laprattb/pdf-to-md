|Opcenter EX DS 4.1-4.2-4.3 Entities|Col2|Col3|Col4|Opcenter Intelligence Model Entities|Col6|Opcenter Execution Discrete – Public object model entities|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~**DB Name**~~<br>|~~**Entity**~~<br>|~~**Attribute**~~|~~**Used**~~|~~**Entity**~~<br>|~~**Attributes**~~|~~**Entity exposed by POM**~~<br><br>|~~**UI**~~<br><br>|~~**Mapping info**~~|
||||Y<br>|~~**BillOfMaterial**~~||~~**BoM**~~|~~UI Material Definitions >> select a Material Definition >> tab BoM~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~BillOfMaterialSiteId~~<br>||||
|~~UADM~~<br>|~~vBoM_Siemens_Simati_1391740687~~<br>|~~Id~~<br>|~~Y~~<br>||~~BillOfMaterialKey~~<br>|~~BillOfMaterialKey~~<br>|~~BillOfMaterialKey~~<br>|~~BillOfMaterialKey~~<br>|
|~~UADM~~<br>|~~vBoM_Siemens_Simati_1391740687~~<br>|~~Name or NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vBoM_Siemens_Simati_1391740687~~<br>|~~[Description]~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~UADM~~<br>|~~vBoM_Siemens_Simati_1391740687~~<br>|~~QuantityValue.Quantity~~<br>|~~Y~~<br>||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
|~~UADM~~<br>|~~vBoM_Siemens_Simati_1391740687~~<br>|~~UoMNId.Quantity~~<br>|~~Y~~<br>||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~|~~vBoM_Siemens_Simati_1391740687~~|~~MaterialDefinition_Id~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**BillOfMaterialItem**~~||~~**BoMItem**~~|~~UI Material Definitions >> select a Material Definition >> tab BoM,~~<br>select a BoM >> tab BoM Items (flat view) and BoM Tree (hierarchy<br>view)||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~BillOfMaterialItemSiteId~~<br>||||
|~~UADM~~<br>|~~vBoMItem_Siemens_Sim_292660823~~<br>|~~Id~~<br>|~~Y~~<br>||~~BillOfMaterialItemKey~~<br>|~~BillOfMaterialItemKey~~<br>|~~BillOfMaterialItemKey~~<br>|~~BillOfMaterialItemKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~BillOfMaterialId~~|~~BillOfMaterialId~~|~~BillOfMaterialId~~|~~BillOfMaterialId~~|
|~~UADM~~<br>|~~vBoMItem_Siemens_Sim_292660823~~<br>|~~BoM_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vBoMItem_Siemens_Sim_292660823~~<br>|~~NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vBoMItem_Siemens_Sim_292660823~~<br>|~~MaterialDefinition_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vBoMItem_Siemens_Sim_292660823~~<br>|~~QuantityValue.Quantity~~<br>|~~Y~~<br>||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
|~~UADM~~|~~vBoMItem_Siemens_Sim_292660823~~|~~UoMNId.Quantity~~|~~Y~~||~~UomId~~|~~UomId~~|~~UomId~~|~~UomId~~|
||||Y<br>|~~**Defect**~~||~~**Defect**~~|~~UI Non-Conformances >> select a Non-Conformance >> tab Defects~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~DefectSiteId~~<br>||||
|~~UADM~~<br>|~~vDefect_Siemens_Sim_2091630976~~<br>|~~Id~~<br>|~~Y~~<br>||~~DefectKey~~<br>|~~DefectKey~~<br>|~~DefectKey~~<br>|~~DefectKey~~<br>|
|~~UADM~~<br>|~~vDefect_Siemens_Sim_2091630976~~<br>|~~Id~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceId~~|~~NonConformanceId~~|~~NonConformanceId~~|~~NonConformanceId~~|
|~~UADM~~|~~vDefect_Siemens_Sim_2091630976~~|~~NonConformance_Id~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**DefectClass**~~||~~**DefectType**~~|~~UI Defect Types~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~DefectClassSiteId~~<br>||||
|~~UADM~~<br>|~~vDefectType_Siemens_1029800126~~<br>,vDefectGroup_Siemen_1773021159<br>,vFailure_Siemens_Op_1949421172<br>|~~'DefectType_'+ Id ,GroupPath_' +Id,Nid~~<br>|~~Y~~<br>||~~DefectClassKey~~<br>|~~DefectClassKey~~<br>|~~DefectClassKey~~<br>|~~DefectClassKey~~<br>|
|~~UADM~~<br>|~~vDefectType_Siemens_1029800126~~<br>,vDefectGroup_Siemen_1773021159<br>,vFailure_Siemens_Op_1949421172<br>|~~Name or Nid~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vDefectType_Siemens_1029800126~~<br>,vDefectGroup_Siemen_1773021159<br>,vFailure_Siemens_Op_1949421172|~~Description~~|~~Y~~||~~Description~~|~~Description~~|~~Description~~|~~Description~~|
||||Y<br>|~~**DefectDefectClass**~~||~~**Defect**~~|~~UI Non-Conformances >> select a Non-Conformance >> tab Defects~~|~~Defect-Defect type association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~DefectDefectClassSiteId~~<br>||||
|~~UADM~~<br>|~~vDefect_Siemens_Sim_2091630976~~<br>|~~Id + '_' + DefectType,~~<br>Id+ '_' +GroupPath,<br>Id+ '_' +FailureNId<br>|~~Y~~<br>||~~DefectDefectClassKey~~<br>|~~DefectDefectClassKey~~<br>|~~DefectDefectClassKey~~<br>|~~DefectDefectClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~DefectId~~|~~DefectId~~|~~DefectId~~|~~DefectId~~|
|~~UADM~~<br>|~~vDefect_Siemens_Sim_2091630976~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~DefectClassId~~|~~DefectClassId~~|~~DefectClassId~~|~~DefectClassId~~|
|~~UADM~~|~~vDefect_Siemens_Sim_2091630976,~~<br>vDefectGroup_Siemen_1773021159,<br>vDefect_Siemens_Sim_2091630976|~~DefectType_' + DefectType,~~<br>'GroupPath_' + Id,<br>FailureNId|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**Equipment**~~||~~**Equipment**~~|~~UI Equipment~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentSiteId~~<br>||||
|~~UADM~~<br>|~~vEquipment_Siemens__2037264456~~<br>|~~Nid~~<br>|~~Y~~<br>||~~EquipmentKey~~<br>|~~EquipmentKey~~<br>|~~EquipmentKey~~<br>|~~EquipmentKey~~<br>|
|~~UADM~~<br>|~~vEquipment_Siemens__2037264456~~<br>|~~Name or NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vEquipment_Siemens__2037264456~~|~~Description~~|~~Y~~||~~Description~~|~~Description~~|~~Description~~|~~Description~~|
||||Y<br>|~~**EquipmentClass**~~||~~**MachineDefinition**~~|~~UI Equipment >> switch in tile mode: the Machine Definition is~~<br>shown in the Equipment tile||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentClassSiteId~~<br>||||
|~~UADM~~<br>|~~vEquipmentLevel_Sie_1829947488~~<br>|~~NId~~<br>|~~Y~~<br>||~~EquipmentClassKey~~<br>|~~EquipmentClassKey~~<br>|~~EquipmentClassKey~~<br>|~~EquipmentClassKey~~<br>|
|~~UADM~~<br>|~~vEquipmentLevel_Sie_1829947488~~<br>|~~Name or NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vEquipmentLevel_Sie_1829947488~~|~~Description~~|~~Y~~||~~Description~~|~~Description~~|~~Description~~|~~Description~~|
||||Y<br>|~~**EquipmentEquipmentClass**~~||~~**Equipment**~~|~~UI Equipment >> switch in tile mode: the Machine Definition is~~<br>shown in the Equipment tile|~~Equipment-MachineDefinition association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentEquipmentClassSiteId~~<br>||||
|~~UADM~~<br>|~~vEquipment_Siemens__2037264456,~~<br>vEquipmentConfigura_2026297865<br>|~~Id~~<br>|~~Y~~<br>||~~EquipmentEquipmentClassKey~~<br>|~~EquipmentEquipmentClassKey~~<br>|~~EquipmentEquipmentClassKey~~<br>|~~EquipmentEquipmentClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~<br>|~~EquipmentId~~<br>|~~EquipmentId~~<br>|~~EquipmentId~~<br>|
|~~UADM~~<br>|~~vEquipment_Siemens__2037264456~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentClassId~~|~~EquipmentClassId~~|~~EquipmentClassId~~|~~EquipmentClassId~~|
|~~UADM~~|~~vEquipment_Siemens__2037264456,~~<br>vEquipmentConfigura_2026297865|~~LevelNId or EquipmentTypeNId~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**EquipmentHierarchy**~~||~~**Equipment**~~|~~UI Equipment, default tree view~~|~~Equipment-Equipment hierarchical association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentHierarchySiteId~~<br>||||
|~~UADM~~<br>|~~vEquipmentGraphLinkC_636721155~~<br>|~~Id~~<br>|~~Y~~<br>||~~EquipmentHierarchyKey~~<br>|~~EquipmentHierarchyKey~~<br>|~~EquipmentHierarchyKey~~<br>|~~EquipmentHierarchyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~<br>|~~vEquipmentGraphNode__200408322~~<br>|~~EquipmentNId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ParentEquipmentId~~|~~ParentEquipmentId~~|~~ParentEquipmentId~~|~~ParentEquipmentId~~|
|~~UADM~~|~~vEquipmentGraphNode__200408322~~|~~EquipmentNId~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y|~~**Labor**~~||~~**PublicUser (this entity is exposed in the**~~<br>**engineering service layer by UAF)**|~~UI Users~~||


|----|----|<site_id>|Y|Col5|LaborSiteId|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~UADM~~<br>|~~vUserNonProductiveAc_383652110,vWorkOrderHistory_Si~~<br>_518515069<br>|~~User,UserId~~<br>|~~Y~~<br>||~~LaborKey~~<br>|~~LaborKey~~<br>|~~LaborKey~~<br>|~~LaborKey~~<br>|
|~~UADM~~|~~vUserNonProductiveAc_383652110,vWorkOrderHistory_Si~~<br>_518515069|~~User,UserId~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|
||||Y<br>|~~**LaborTimeCategory**~~||~~**WorkOrderHistoryAction**~~|~~UI Work Orders >> select a WorkOrder >> button As Built >> tab~~<br>Activity History<br>You can also see them on UI Genealogy, in the tree representation,<br>under each WorkOrderOperation node||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~LaborTimeCategorySiteId~~<br>||||
|~~UADM~~<br>|~~vNonProductiveActivi_678536801~~<br>|~~Id~~<br>|~~Y~~<br>||~~LaborTimeCategoryKey~~<br>|~~LaborTimeCategoryKey~~<br>|~~LaborTimeCategoryKey~~<br>|~~LaborTimeCategoryKey~~<br>|
|~~UADM~~<br>|~~vNonProductiveActivi_678536801~~<br>|~~NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vNonProductiveActivi_678536801~~|~~Description~~|~~Y~~||~~Description~~|~~Description~~|~~Description~~|~~Description~~|
||||Y<br>|~~**LaborTimeModel**~~||~~**WorkOrderHistory +**~~<br>**WorkOrderHistoryAction**|~~UI Users >> select a user >> tab Log~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~LaborTimeModelSiteId~~<br>||||
|~~UADM~~<br>|~~vUserNonProductiveAc_383652110~~<br>|~~Id~~<br>|~~Y~~<br>||~~LaborTimeModelKey~~<br>|~~LaborTimeModelKey~~<br>|~~LaborTimeModelKey~~<br>|~~LaborTimeModelKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~LaborTimeCategorySiteId~~<br>|~~LaborTimeCategorySiteId~~<br>|~~LaborTimeCategorySiteId~~<br>|~~LaborTimeCategorySiteId~~<br>|
|~~UADM~~<br>|~~vUserNonProductiveAc_383652110~~<br>|~~NPAId~~<br>|~~Y~~<br>||~~LaborTimeCategoryKey~~<br>|~~LaborTimeCategoryKey~~<br>|~~LaborTimeCategoryKey~~<br>|~~LaborTimeCategoryKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~LaborSiteId~~<br>|~~LaborSiteId~~<br>|~~LaborSiteId~~<br>|~~LaborSiteId~~<br>|
|~~----~~<br>|~~----~~<br>|~~User~~<br>|~~Y~~<br>||~~LaborKey~~<br>|~~LaborKey~~<br>|~~LaborKey~~<br>|~~LaborKey~~<br>|
|~~UADM~~<br>|~~vUserNonProductiveAc_383652110~~<br>|~~StartDate-EndDate~~<br>|~~Y~~<br>||~~Duration~~<br>|~~Duration~~<br>|~~Duration~~<br>|~~Duration~~<br>|
|~~UADM~~<br>|~~vUserNonProductiveAc_383652110~~<br>|~~StartDate~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~UADM~~|~~vUserNonProductiveAc_383652110~~|~~EndDate~~|~~Y~~||~~EndDate~~|~~EndDate~~|~~EndDate~~|~~EndDate~~|
||||Y<br>|~~**MaterialClass**~~||~~**MaterialClass**~~|~~UI Material Definitions >> in the default tile view the MaterialClass~~<br>is shown|~~UI Material Definitions >> in the default tile view the MaterialClass~~<br>is shown|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialClassSiteId~~<br>||||
|~~UADM~~<br>|~~vMaterialGroup_Siem_2035655829,vDM_FunctionalCode_~~<br>S_320778133<br>|~~Id or Nid~~<br>|~~Y~~<br>||~~MaterialClassKey~~<br>|~~MaterialClassKey~~<br>|~~MaterialClassKey~~<br>|~~MaterialClassKey~~<br>|
|~~UADM~~<br>|~~vMaterialGroup_Siem_2035655829,vDM_FunctionalCode_~~<br>S_320778133<br>|~~Name or NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vMaterialGroup_Siem_2035655829,vDM_FunctionalCode_~~<br>S_320778133|~~Description~~|~~Y~~||~~Description~~|~~Description~~|~~Description~~|~~Description~~|
||||Y<br>|~~**MaterialDefinition**~~||~~**MaterialDefinition**~~|~~UI Material Definitions~~|~~UI Material Definitions~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionSiteId~~<br>||||
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~Id~~<br>|~~Y~~<br>||~~MaterialDefinitionKey~~<br>|~~MaterialDefinitionKey~~<br>|~~MaterialDefinitionKey~~<br>|~~MaterialDefinitionKey~~<br>|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~Name or NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vMaterial_Siemens_Si_170253665~~|~~Description~~|~~Y~~||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
||||Y<br>|~~**MaterialDefinitionMaterialClass**~~<br>|~~**MaterialDefinitionMaterialClass**~~<br>|~~**MaterialDefinition**~~|~~UI Material Definitions~~|~~MaterialDefinition-MaterialClass association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionMaterialClassSiteId~~<br>||||
|~~UADM~~<br>|~~vDM_Material_Siemens_463872986~~<br>|~~Id or 'FunctionalCode_' + Id~~<br>|~~Y~~<br>||~~MaterialDefinitionMaterialClassKey~~<br>|~~MaterialDefinitionMaterialClassKey~~<br>|~~MaterialDefinitionMaterialClassKey~~<br>|~~MaterialDefinitionMaterialClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~<br>|~~MaterialDefinitionId~~<br>|~~MaterialDefinitionId~~<br>|~~MaterialDefinitionId~~<br>|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialClassId~~|~~MaterialClassId~~|~~MaterialClassId~~|~~MaterialClassId~~|
|~~UADM~~|~~vDM_Material_Siemens_463872986~~|~~MaterialClass_Id or FunctionalCodeNId~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**MaterialDefinitionPropertyStaticValue**~~<br>|~~**MaterialDefinitionPropertyStaticValue**~~<br>|~~**Value of MaterialDefinition attribute**~~|~~UI Material Definitions, grid mode~~|~~"Revision", "SerialNumberProfile", "FirstArticleInspection")~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionPropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~(Id +'_' +'Revision' or Id +'_' +'IsCurrent') or~~<br>(Id +'_' +'SerialNumberProfile' or Id +'_'<br>+'FirstArticleInspection' or Id +'_' +'WeightUom' or Id<br>+'_' +'VolumeUom' or Id +'_' +'WeightQuantity' or Id<br>+'_' +'VolumeQuantity' or<br>Id +'_' +'Code')<br>|~~Y~~<br>||~~MaterialDefinitionPropertyStaticValueKey~~<br>|~~MaterialDefinitionPropertyStaticValueKey~~<br>|~~MaterialDefinitionPropertyStaticValueKey~~<br>|~~MaterialDefinitionPropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~<br>|~~MaterialDefinitionId~~<br>|~~MaterialDefinitionId~~<br>|~~MaterialDefinitionId~~<br>|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialPropertyId~~|~~MaterialPropertyId~~|~~MaterialPropertyId~~|~~MaterialPropertyId~~|
|~~----~~<br>|~~----~~<br>|~~"Revision" or~~<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665 or~~<br>vDM_Material_Siemens_463872986<br>|~~(Revision or IsCurrent) or~~<br>(SerialNumberProfile or FirstArticleInspection or<br>UoMNId.Weight or UoMNId.Volume<br>|~~Y~~<br>||~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|
|~~UADM~~|~~vDM_Material_Siemens_463872986~~|~~QuantityValue.Weight or QuantityValue.Volume~~|~~Y~~||~~FloatValue~~|~~FloatValue~~|~~FloatValue~~|~~FloatValue~~|
||||Y<br>|~~**MaterialLot**~~||~~**MaterialItem**~~|~~UI Material Items~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotSiteId~~<br>||||
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~NId~~<br>|~~Y~~<br>||~~MaterialLotKey~~<br>|~~MaterialLotKey~~<br>|~~MaterialLotKey~~<br>|~~MaterialLotKey~~<br>|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~Name~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~QuantityValue.Quantity~~<br>|~~Y~~<br>||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
|~~UADM~~|~~vMaterialTrackingUni_494706508~~|~~UoMNId.Quantity~~|~~Y~~||~~UomId~~|~~UomId~~|~~UomId~~|~~UomId~~|
||||Y<br>|~~**MaterialLotHierarchy**~~||~~**MaterialItemHistory +**~~<br>**MaterialItemHistoryAction**|~~UI Material Items >> Material Item Details >> Parent Batch~~<br>property and tab History<br>UI Raw Material Genealogy||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotHierarchySiteId~~<br>||||
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~Id~~<br>|~~Y~~<br>||~~MaterialLotHierarchyKey~~<br>|~~MaterialLotHierarchyKey~~<br>|~~MaterialLotHierarchyKey~~<br>|~~MaterialLotHierarchyKey~~<br>|
|~~----~~|~~----~~|~~<site_id>~~|~~Y~~||~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|


|UADM|vMaterialTrackingUni_494706508|NId|Y|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ParentMaterialLotId~~|~~ParentMaterialLotId~~|~~ParentMaterialLotId~~|~~ParentMaterialLotId~~|
|~~UADM~~|~~vMaterialTrackingUni_494706508~~|~~NId~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**MaterialLotOperation**~~||~~**MaterialItemHistory +**~~<br>**MaterialItemHistoryAction**|~~UI Material Items >> select a Material Item >> tab History~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotOperationSiteId~~<br>||||
|~~UADM~~<br>|~~vDM_MaterialTracking_215326293~~<br>|~~Id~~<br>|~~Y~~<br>||~~MaterialLotOperationKey~~<br>|~~MaterialLotOperationKey~~<br>|~~MaterialLotOperationKey~~<br>|~~MaterialLotOperationKey~~<br>|
|~~UADM~~<br>|~~vDM_MaterialTracking_215326293~~<br>|~~Date~~<br>|~~Y~~<br>||~~OperationDateTime~~<br>|~~OperationDateTime~~<br>|~~OperationDateTime~~<br>|~~OperationDateTime~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|
|~~UADM~~<br>|~~vDM_MaterialTrackin_1551871669~~<br>|~~Nid~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vDM_Material_Siemens_463872986~~<br>|~~Material_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vDM_MaterialTracking_215326293~~<br>|~~OldQuantity~~<br>|~~Y~~<br>||~~ActualQuantity~~<br>|~~ActualQuantity~~<br>|~~ActualQuantity~~<br>|~~ActualQuantity~~<br>|
|~~UADM~~<br>|~~vDM_MaterialTracking_215326293~~<br>|~~Quantity~~<br>|~~Y~~<br>||~~OperationQuantity~~<br>|~~OperationQuantity~~<br>|~~OperationQuantity~~<br>|~~OperationQuantity~~<br>|
|~~UADM~~<br>|~~dbo.vMaterialTrackingUni_494706508~~<br>|~~UoMNId.Quantity~~<br>|~~Y~~<br>||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~SourceMaterialDefinitionId~~|~~SourceMaterialDefinitionId~~|~~SourceMaterialDefinitionId~~|~~SourceMaterialDefinitionId~~|
|~~UADM~~<br>|~~vDM_Material_Siemens_463872986~~<br>|~~Material_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~SourceMaterialLotId~~|~~SourceMaterialLotId~~|~~SourceMaterialLotId~~|~~SourceMaterialLotId~~|
|~~UADM~~<br>|~~vDM_MaterialTrackin_1551871669~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~UoMNId.Quantity~~<br>|~~Y~~<br>||~~SourceUomId~~<br>|~~SourceUomId~~<br>|~~SourceUomId~~<br>|~~SourceUomId~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~EquipmentNId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~SourceEquipmentId~~|~~SourceEquipmentId~~|~~SourceEquipmentId~~|~~SourceEquipmentId~~|
|~~UADM~~|~~vMaterialTrackingUni_494706508~~|~~EquipmentNId~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**MaterialLotPropertyStaticValue**~~<br>|~~**MaterialLotPropertyStaticValue**~~<br>|~~**Value of MaterialItem attribute**~~|~~UI Material Items~~|~~"SerialNumberCode", "BatchId", "IsReserved"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotPropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~Id +'_Code'~~<br>|~~Y~~<br>||~~MaterialLotPropertyStaticValueKey~~<br>|~~MaterialLotPropertyStaticValueKey~~<br>|~~MaterialLotPropertyStaticValueKey~~<br>|~~MaterialLotPropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialPropertyId~~|~~MaterialPropertyId~~|~~MaterialPropertyId~~|~~MaterialPropertyId~~|
|~~----~~<br>|~~----~~<br>|~~'Code'~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~Code~~|~~Y~~||~~StringValue~~|~~StringValue~~|~~StringValue~~|~~StringValue~~|
||||Y<br>|~~**MaterialProperty**~~||~~**Attribute/Property of a MaterialDefinition**~~|~~UI Material Definitions, grid mode~~|~~"FirstArticleInspection", "SerialNumberCode","Revision","BatchId"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialPropertySiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~"Revision" or~~<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"<br>|~~Y~~<br>||~~MaterialPropertyKey~~<br>|~~MaterialPropertyKey~~<br>|~~MaterialPropertyKey~~<br>|~~MaterialPropertyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~"Revision" or~~<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~"String" or "Numeric"~~<br>|~~Y~~<br>||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
|~~----~~|~~----~~|~~"n/a"~~|~~Y~~||~~UomId~~|~~UomId~~|~~UomId~~|~~UomId~~|
||||Y<br>|~~**NonConformance**~~||~~**NonConformance**~~|~~UI Non-Conformances~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceSiteId~~<br>||||
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~Id~~<br>|~~Y~~<br>||~~NonConformanceKey~~<br>|~~NonConformanceKey~~<br>|~~NonConformanceKey~~<br>|~~NonConformanceKey~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceStatusId~~|~~NonConformanceStatusId~~|~~NonConformanceStatusId~~|~~NonConformanceStatusId~~|
|~~UADM~~<br>|~~vNonConformanceStat_1246268624~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~StartDate~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~EndDate~~<br>|~~Y~~<br>||~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~(StartDate) - (EndDate)~~<br>|~~Y~~<br>||~~Duration~~<br>|~~Duration~~<br>|~~Duration~~<br>|~~Duration~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~<br>|~~EquipmentId~~<br>|~~EquipmentId~~<br>|~~EquipmentId~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~Equipment~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolDefinitionId~~<br>|~~ToolDefinitionId~~<br>|~~ToolDefinitionId~~<br>|~~ToolDefinitionId~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionId~~|~~OperationExecutionId~~|~~OperationExecutionId~~|~~OperationExecutionId~~|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~<br>|~~OperationResponseId~~<br>|~~OperationResponseId~~<br>|~~OperationResponseId~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~WorkOrderOperation_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~Notes~~<br>|~~Y~~<br>||~~Comment~~<br>|~~Comment~~<br>|~~Comment~~<br>|~~Comment~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~InspectedQuantity~~<br>|~~InspectedQuantity~~<br>|~~InspectedQuantity~~<br>|~~InspectedQuantity~~<br>|
|~~UADM~~|~~vNonConformance_Sieme_73759778~~|~~Quantity~~|~~Y~~||~~NonConformantQuantity~~|~~NonConformantQuantity~~|~~NonConformantQuantity~~|~~NonConformantQuantity~~|
||||Y<br>|~~**NonConformanceClass**~~||~~**NonConformanceSeverity**~~|~~UI Non-Conformances >> tab Details~~||
|~~----~~|~~----~~|~~<site_id>~~|~~Y~~||~~NonConformanceClassSiteId~~||||


|UADM|vNonConformance_Sieme_73759778|("Severity_" + Severity) OR<br>("Type_"+ Type)|Y|Col5|NonConformanceClassKey|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~UADM~~|~~vNonConformance_Sieme_73759778~~|~~Severity OR Type~~|~~Y~~||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
||||Y<br>|~~**NonConformanceEquipmentSpecification**~~<br>|~~**NonConformanceEquipmentSpecification**~~<br>|~~**NonConformanceItem**~~|~~UI Non-Conformances >> tab Machines~~|~~Equipment where the Non-Conformance has been opened on~~|
|~~---~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceEquipmentSpecificationSiteId~~<br>||||
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~Id~~<br>|~~Y~~<br>||~~NonConformanceEquipmentSpecificationKey~~<br>|~~NonConformanceEquipmentSpecificationKey~~<br>|~~NonConformanceEquipmentSpecificationKey~~<br>|~~NonConformanceEquipmentSpecificationKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~NonConformance_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~Equipment~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~1~~|~~Y~~||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
||||Y<br>|~~**NonConformanceNonConformanceClass**~~<br>|~~**NonConformanceNonConformanceClass**~~<br>|~~**NonConformance**~~|~~UI Non-Conformances~~|~~NonConformance-NonConformanceSeverity association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceNonConformanceClassSiteId~~<br>||||
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~(Id + '_' + 'Severity_' + Severity ) OR (Id  + '_' +~~<br>('Type_' + [Type]))<br>|~~Y~~<br>||~~NonConformanceNonConformanceClassKey~~<br>|~~NonConformanceNonConformanceClassKey~~<br>|~~NonConformanceNonConformanceClassKey~~<br>|~~NonConformanceNonConformanceClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceClassId~~<br>|~~NonConformanceClassId~~<br>|~~NonConformanceClassId~~<br>|~~NonConformanceClassId~~<br>|
|~~UADM~~<br>|~~vNonConformance_Sieme_73759778~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceId~~|~~NonConformanceId~~|~~NonConformanceId~~|~~NonConformanceId~~|
|~~UADM~~|~~vNonConformance_Sieme_73759778~~|~~('Severity_' + Severity) OR ('Type_' + [Type])~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**NonConformanceMaterialLotSpecification**~~<br>|~~**NonConformanceMaterialLotSpecification**~~<br>|~~**NonConformanceItem**~~|~~UI Non-Conformances >> tab Material Items~~|~~Material item where the Non-Conformance has been opened on~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceMaterialLotSpecificationSiteId~~<br>||||
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~Id~~<br>|~~Y~~<br>||~~NonConformanceMaterialLotSpecificationKey~~<br>|~~NonConformanceMaterialLotSpecificationKey~~<br>|~~NonConformanceMaterialLotSpecificationKey~~<br>|~~NonConformanceMaterialLotSpecificationKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~NonConformance_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~1~~|~~Y~~||~~Quantity~~|~~Quantity~~|~~Quantity~~|~~Quantity~~|
||||Y<br>|~~**NonConformanceProperty**~~||~~**Attribute of a NonConformance**~~|~~UI Non-Conformances~~|~~"SerialNumber"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformancePropertySiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~"SerialNumber"~~<br>|~~Y~~<br>||~~NonConformancePropertyKey~~<br>|~~NonConformancePropertyKey~~<br>|~~NonConformancePropertyKey~~<br>|~~NonConformancePropertyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~"SerialNumber"~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~"String"~~<br>|~~Y~~<br>||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
|~~----~~|~~----~~|~~"n/a"~~|~~Y~~||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
||||Y<br>|~~**NonConformancePropertyStaticValue**~~<br>|~~**NonConformancePropertyStaticValue**~~<br>|~~**Value for a NonConformance attribute**~~|~~UI Non-Conformances~~|~~"SerialNumber"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformancePropertyStaticValueSiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~NonConformancePropertyStaticValueKey~~<br>|~~NonConformancePropertyStaticValueKey~~<br>|~~NonConformancePropertyStaticValueKey~~<br>|~~NonConformancePropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformancePropertyId~~|~~NonConformancePropertyId~~|~~NonConformancePropertyId~~|~~NonConformancePropertyId~~|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~----~~|~~Y~~||~~StringValue~~|~~StringValue~~|~~StringValue~~|~~StringValue~~|
||||Y<br>|~~**NonConformanceStatus**~~||~~**NonConformanceStatus**~~|~~UI Non-Conformance Lifecycles~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceStatusSiteId~~<br>||||
|~~UADM~~<br>|~~vNonConformanceStat_1246268624~~<br>|~~Id~~<br>|~~Y~~<br>||~~NonConformanceStatusKey~~<br>|~~NonConformanceStatusKey~~<br>|~~NonConformanceStatusKey~~<br>|~~NonConformanceStatusKey~~<br>|
|~~UADM~~<br>|~~vNonConformanceStat_1246268624~~<br>|~~Name or NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vNonConformanceStat_1246268624~~|~~Description~~|~~Y~~||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
||||Y<br>|~~**NonConformanceToolSpecification**~~<br>|~~**NonConformanceToolSpecification**~~<br>|~~**NonConformanceItem**~~|~~UI Non-Conformances >> tab Tools~~|~~Tool item where the Non-Conformance has been opened on~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceToolSpecificationSiteId~~<br>||||
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~Id~~<br>|~~Y~~<br>||~~NonConformanceToolSpecificationKey~~<br>|~~NonConformanceToolSpecificationKey~~<br>|~~NonConformanceToolSpecificationKey~~<br>|~~NonConformanceToolSpecificationKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|~~NonConformanceId~~<br>|
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~NonConformance_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolId~~|~~ToolId~~|~~ToolId~~|~~ToolId~~|
|~~UADM~~<br>|~~vNonConformanceItem_1873176518~~<br>|~~Tool_id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~1~~|~~Y~~||~~Quantity~~|~~Quantity~~|~~Quantity~~|~~Quantity~~|
||||Y<br>|~~**OperationDefinition**~~||~~**Operation/Step**~~|~~UI Operation Catalog/ UI Step Catalog~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionSiteId~~<br>||||
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012<br>|~~Id~~<br>|~~Y~~<br>||~~OperationDefinitionKey~~<br>|~~OperationDefinitionKey~~<br>|~~OperationDefinitionKey~~<br>|~~OperationDefinitionKey~~<br>|
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012<br>|~~Name OR Nid~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionClassSiteId~~<br>|~~OperationDefinitionClassSiteId~~<br>|~~OperationDefinitionClassSiteId~~<br>|~~OperationDefinitionClassSiteId~~<br>|
|~~----~~<br>|~~----~~<br>|~~"Operation" or~~<br>"Step"<br>|~~Y~~<br>||~~OperationDefinitionClassKey~~<br>|~~OperationDefinitionClassKey~~<br>|~~OperationDefinitionClassKey~~<br>|~~OperationDefinitionClassKey~~<br>|
|~~----~~|~~----~~|~~"Operation" or~~<br>"Step"|~~Y~~||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
||||Y<br>|~~**OperationDefinitionEquipmentSpecification**~~<br>|~~**OperationDefinitionEquipmentSpecification**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionEquipmentSpecificationSiteId~~<br>||||
|~~UADM~~<br>|~~vEquipmentSpecifica_1193585561~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationDefinitionEquipmentSpecificationKey~~<br>|~~OperationDefinitionEquipmentSpecificationKey~~<br>|~~OperationDefinitionEquipmentSpecificationKey~~<br>|~~OperationDefinitionEquipmentSpecificationKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~|~~vEquipmentSpecifica_1193585561~~|~~EquipmentNId~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**OperationDefinitionMaterialDefinitionSpecificationIn**~~<br>|~~**OperationDefinitionMaterialDefinitionSpecificationIn**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionMaterialDefinitionSpecificationInSiteId~~<br>||||
|~~UADM~~<br>|~~vMaterialSpecificat_1918342704~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationDefinitionMaterialDefinitionSpecificationInKey~~<br>|~~OperationDefinitionMaterialDefinitionSpecificationInKey~~<br>|~~OperationDefinitionMaterialDefinitionSpecificationInKey~~<br>|~~OperationDefinitionMaterialDefinitionSpecificationInKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~|~~vMaterial_Siemens_Si_170253665~~|~~Id~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|


|UADM|vMaterialSpecificat_1918342704|QuantityValue.Quantity|Y|Col5|Quantity|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~UADM~~|~~vMaterialSpecificat_1918342704~~|~~UoMNId.Quantity~~|~~Y~~<br>||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
||||~~Y~~<br>|~~**OperationDefinitionOperationDefinitionClass**~~<br>|~~**OperationDefinitionOperationDefinitionClass**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionOperationDefinitionClassSiteId~~<br>||||
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012<br>|~~(Id + '_Operation) or (Id + '_Step')~~<br>|~~Y~~<br>||~~OperationDefinitionOperationDefinitionClassKey~~<br>|~~OperationDefinitionOperationDefinitionClassKey~~<br>|~~OperationDefinitionOperationDefinitionClassKey~~<br>|~~OperationDefinitionOperationDefinitionClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionClassId~~<br>|~~OperationDefinitionClassId~~<br>|~~OperationDefinitionClassId~~<br>|~~OperationDefinitionClassId~~<br>|
|~~----~~<br>|~~----~~<br>|~~"Operation" or "Step"~~<br>|~~Y~~<br>||||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|
|~~UADM~~|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012|~~Id~~|~~Y~~||||||
||||Y<br>|~~**OperationDefinitionProperty**~~||~~** Attribute of an Operation**~~|~~UI Operation Catalog, grid mode~~|~~"EstimatedDuration"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionPropertySiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~"EstimatedDuration" or "Revision"~~<br>|~~Y~~<br>||~~OperationDefinitionPropertyKey~~<br>|~~OperationDefinitionPropertyKey~~<br>|~~OperationDefinitionPropertyKey~~<br>|~~OperationDefinitionPropertyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~"n/a"~~<br>|~~Y~~<br>||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
|~~----~~<br>|~~----~~<br>|~~"Numeric" or "String"~~<br>|~~Y~~<br>||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
|~~----~~|~~----~~|~~"EstimatedDuration" or "Revision"~~|~~Y~~||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
||||Y<br>|~~**OperationDefinitionPropertyStaticValue**~~<br>|~~**OperationDefinitionPropertyStaticValue**~~<br>|~~**Value for an Operation/Step attribute**~~|~~UI Operation Catalog/ UI Step Catalog, grid mode~~|~~"EstimatedDuration"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionPropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012<br>|~~(Id+'_' +'EstimatedDuration') or (Id+'_' +'Revision')~~<br>|~~Y~~<br>||~~OperationDefinitionPropertyStaticValueKey~~<br>|~~OperationDefinitionPropertyStaticValueKey~~<br>|~~OperationDefinitionPropertyStaticValueKey~~<br>|~~OperationDefinitionPropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionPropertyId~~|~~OperationDefinitionPropertyId~~|~~OperationDefinitionPropertyId~~|~~OperationDefinitionPropertyId~~|
|~~----~~<br>|~~----~~<br>|~~"EstimatedDuration" or "Revision"~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012<br>|~~EstimatedDuration~~<br>|~~Y~~<br>||~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|
|~~UADM~~|~~vOperation_Siemens_S_700803909 or~~<br>vStep_Siemens_Simati_938557012|~~Revision~~|~~Y~~||~~StringValue~~|~~StringValue~~|~~StringValue~~|~~StringValue~~|
||||Y<br>|~~**OperationExecution**~~||~~**WorkOrder**~~|~~UI Work Orders~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~NId~~<br>|~~Y~~<br>||~~OperationExecutionKey~~<br>|~~OperationExecutionKey~~<br>|~~OperationExecutionKey~~<br>|~~OperationExecutionKey~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Name~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Notes~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionStatusId~~<br>|~~OperationExecutionStatusId~~<br>|~~OperationExecutionStatusId~~<br>|~~OperationExecutionStatusId~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~StatusNId.Status~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~<br>|~~EquipmentId~~<br>|~~EquipmentId~~<br>|~~EquipmentId~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Plant~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vDM_Material_Siemens_463872986~~<br>|~~Material_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationSchedulingId~~|~~OperationSchedulingId~~|~~OperationSchedulingId~~|~~OperationSchedulingId~~|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~ProducedQuantity~~<br>|~~Y~~<br>||~~ProducedQuantity~~<br>|~~ProducedQuantity~~<br>|~~ProducedQuantity~~<br>|~~ProducedQuantity~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~ReworkedQuantity~~<br>|~~Y~~<br>||~~ReworkedQuantity~~<br>|~~ReworkedQuantity~~<br>|~~ReworkedQuantity~~<br>|~~ReworkedQuantity~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~ScrappedQuantity~~<br>|~~Y~~<br>||~~ScrapQuantity~~<br>|~~ScrapQuantity~~<br>|~~ScrapQuantity~~<br>|~~ScrapQuantity~~<br>|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~UoMNId~~<br>|~~Y~~<br>||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~ActualStartTime~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~ActualEndTime~~<br>|~~Y~~<br>||~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|
|~~UADM~~|~~vWorkOrder_Siemens_S_749389132~~|~~ActualStartTime - ActualEndTime~~|~~Y~~||~~Duration~~|~~Duration~~|~~Duration~~|~~Duration~~|
||||Y<br>|~~**OperationExecutionClass**~~||~~**ProductionType/ExecutionGroup**~~|~~UI Work Orders >> tab Details/UI Execution Groups~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionClassSiteId~~<br>||||
|~~UADM~~<br>|~~vProductionType_Siem_763981173~~<br>|~~Id  + '_ProductionType'~~<br>|~~Y~~<br>||~~OperationExecutionClassKey~~<br>|~~OperationExecutionClassKey~~<br>|~~OperationExecutionClassKey~~<br>|~~OperationExecutionClassKey~~<br>|
|~~UADM~~|~~vProductionType_Siem_763981173~~|~~NId~~|~~Y~~<br>||~~Name~~|~~Name~~|~~Name~~|~~Name~~|
||||~~Y~~<br>|~~**OperationExecutionHierarchy**~~|||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionHierarchySiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationExecutionHierarchyKey~~<br>|~~OperationExecutionHierarchyKey~~<br>|~~OperationExecutionHierarchyKey~~<br>|~~OperationExecutionHierarchyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ParentOperationExecutionId~~<br>|~~ParentOperationExecutionId~~<br>|~~ParentOperationExecutionId~~<br>|~~ParentOperationExecutionId~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Nid~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionId~~|~~OperationExecutionId~~|~~OperationExecutionId~~|~~OperationExecutionId~~|
|~~UADM~~|~~vWorkOrder_Siemens_S_749389132~~|~~NId~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**OperationExecutionOperationExecutionClass**~~<br>|~~**OperationExecutionOperationExecutionClass**~~<br>|~~**WorkOrder**~~|~~UI Execution Groups >> open an ExecutionGroup >> tab Operations~~|~~WorkOrder-ProductionType/Execution Group association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionOperationExecutionClassSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationExecutionOperationExecutionClassKey~~<br>|~~OperationExecutionOperationExecutionClassKey~~<br>|~~OperationExecutionOperationExecutionClassKey~~<br>|~~OperationExecutionOperationExecutionClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionId~~<br>|~~OperationExecutionId~~<br>|~~OperationExecutionId~~<br>|~~OperationExecutionId~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionClassId~~|~~OperationExecutionClassId~~|~~OperationExecutionClassId~~|~~OperationExecutionClassId~~|
|~~UADM~~|~~vWorkOrder_Siemens_S_749389132~~|~~ProductionType_Id  + '_ProductionType'~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**OperationExecutionProperty**~~||~~**Attribute of a WorkOrder**~~|~~UI Execution Groups >> open an ExecutionGroup >> tab Operations,~~<br>grid mode|~~"Proces"s, "AsPlanned", "ERPOrder",~~<br>"ParentBatch","InitialQuality","IsUnderScheduling", "PBOPIdentID",<br>"Plant", "Priority", "ProcessNId", "ProcessRevision", "ProcessUId",<br>"PoC", "ReworkOfOrder"|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionPropertySiteId~~<br>||||
|~~----~~|~~----~~|~~"Process" OR "AsPlanned" OR "ERPOrder" OR~~<br>"InitialQuantity" OR "IsUnderScheduling" OR<br>"ParentBatch" OR "PoC" OR "Priority" OR<br>"ProcessNId" OR "ProcessRevision" OR "ProcessUId"<br>OR "ReworkOfOrder"|~~Y~~||~~OperationExecutionPropertyKey~~|~~OperationExecutionPropertyKey~~|~~OperationExecutionPropertyKey~~|~~OperationExecutionPropertyKey~~|


|----|----|"Process" OR "AsPlanned" OR "ERPOrder" OR<br>"InitialQuantity" OR "IsUnderScheduling" OR<br>"ParentBatch" OR "PoC" OR "Priority" OR<br>"ProcessNId" OR "ProcessRevision" OR "ProcessUId"<br>OR "ReworkOfOrder"|Y|Col5|Name|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~"String" OR "Numeric"~~<br>|~~Y~~<br>||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
|~~----~~|~~----~~|~~"n/a"~~|~~Y~~||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
||||Y<br>|~~**OperationExecutionPropertyStaticValue**~~<br>|~~**OperationExecutionPropertyStaticValue**~~<br>|~~**Value for an attribute of a WorkOrder**~~|~~UI Work Orders, grid mode~~|~~"Proces"s, "AsPlanned", "ERPOrder",~~<br>"ParentBatch","InitialQuality","IsUnderScheduling", "PBOPIdentID",<br>"Plant", "Priority", "ProcessNId", "ProcessRevision", "ProcessUId",<br>"PoC", "ReworkOfOrder"|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionPropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~(NId + '_' + 'Process') OR (NId + '_' + 'AsPlanned') OR~~<br>(NId + '_' + 'ERPOrder') OR (NId + '_' +<br>'InitialQuantity') OR (NId + '_' + 'IsUnderScheduling')<br>OR (NId + '_' + 'ParentBatch') OR (NId + '_' + 'PoC')<br>OR (NId + '_' + 'Priority') OR (NId + '_' + 'ProcessNId')<br>OR (NId + '_' + 'ProcessRevision') OR (NId + '_' +<br>'ProcessUId') OR (NId + '_' + 'ReworkOfOrder')<br>|~~Y~~<br>||~~OperationExecutionPropertyStaticValueKey~~<br>|~~OperationExecutionPropertyStaticValueKey~~<br>|~~OperationExecutionPropertyStaticValueKey~~<br>|~~OperationExecutionPropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionId~~|~~OperationExecutionId~~|~~OperationExecutionId~~|~~OperationExecutionId~~|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Process or  AsPlanned or ReworkOfOrder or~~<br>ERPOrder or ParentBatch or ProcessRevision or<br>ProcessNId or ProcessUId<br>|~~Y~~<br>||~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|
|~~UADM~~|~~vWorkOrder_Siemens_S_749389132~~|~~InitialQuantity, IsUnderScheduling, [Priority], PoC~~|~~Y~~||~~FloatValue~~|~~FloatValue~~|~~FloatValue~~|~~FloatValue~~|
||||Y<br>|~~**OperationExecutionStatus**~~||~~**WorkOrder**~~|~~UI Work Orders~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionStatusSiteId~~<br>||||
|~~UADM~~<br>|~~vStatus_Siemens_Sim_2045546455~~<br>|~~NId~~<br>|~~Y~~<br>||~~OperationExecutionStatusKey~~<br>|~~OperationExecutionStatusKey~~<br>|~~OperationExecutionStatusKey~~<br>|~~OperationExecutionStatusKey~~<br>|
|~~UADM~~|~~vStatus_Siemens_Sim_2045546455~~|~~Name~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|
||||Y<br>|~~**OperationRequest**~~||~~**WorkOrderOperation/WorkOrderStep**~~|~~UI Work Orders >> open a WorkOrder >> tab Operations UI Work~~<br>Orders >> open a WorkOrder >> tab Operations >> tab Steps||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>||~~OperationRequestKey~~<br>|~~OperationRequestKey~~<br>|~~OperationRequestKey~~<br>|~~OperationRequestKey~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Name OR Nid~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~Operation~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationSchedulingId~~|~~OperationSchedulingId~~|~~OperationSchedulingId~~|~~OperationSchedulingId~~|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~WorkOrder_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestStatusId~~|~~OperationRequestStatusId~~|~~OperationRequestStatusId~~|~~OperationRequestStatusId~~|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~StatusNId.Status~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~EstimatedStartTime~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~EstimatedEndTime~~<br>|~~Y~~<br>||~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~TargetQuantity~~<br>|~~Y~~<br>||~~EstimatedQuantity~~<br>|~~EstimatedQuantity~~<br>|~~EstimatedQuantity~~<br>|~~EstimatedQuantity~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~EstimatedDuration~~<br>|~~Y~~<br>||~~Duration~~<br>|~~Duration~~<br>|~~Duration~~<br>|~~Duration~~<br>|
|~~UADM~~|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|~~Sequence~~|~~Y~~<br>||~~Sequence~~|~~Sequence~~|~~Sequence~~|~~Sequence~~|
||||~~Y~~<br>|~~**OperationRequestClass**~~||~~**Type of**~~<br>**WorkOrderOperation/WorkOrderStep**||~~WorkOrderOperation OR "ExecutionGroup" OR~~<br>"ExecutionGroupPhase" OR "WorkOrderStep"|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestClassSiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~WorkOrderOperation OR "ExecutionGroup" OR~~<br>"ExecutionGroupPhase" OR "WorkOrderStep"<br>|~~Y~~<br>||~~OperationRequestClassKey~~<br>|~~OperationRequestClassKey~~<br>|~~OperationRequestClassKey~~<br>|~~OperationRequestClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~WorkOrderOperation OR "ExecutionGroup" OR~~<br>"ExecutionGroupPhase" OR "WorkOrderStep"<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestHierarchySiteId~~<br>|~~OperationRequestHierarchySiteId~~<br>|~~OperationRequestHierarchySiteId~~<br>|~~OperationRequestHierarchySiteId~~<br>|
|~~UADM~~<br>|~~vExecutionGroupPhase_469816675 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>||~~OperationRequestHierarchyKey~~<br>|~~OperationRequestHierarchyKey~~<br>|~~OperationRequestHierarchyKey~~<br>|~~OperationRequestHierarchyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestId~~|~~OperationRequestId~~|~~OperationRequestId~~|~~OperationRequestId~~|
|~~UADM~~<br>|~~vExecutionGroupPhase_469816675 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ParentOperationRequestId~~|~~ParentOperationRequestId~~|~~ParentOperationRequestId~~|~~ParentOperationRequestId~~|
|~~UADM~~|~~vExecutionGroupPhase_469816675 or~~<br>vWorkOrderStep_Siem_1809795233|~~ExecutionGroup_Id or WorkOrderOperation_Id~~|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
||||~~Y~~<br>|~~**OperationRequestOperationRequestClass**~~<br>|~~**OperationRequestOperationRequestClass**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestOperationRequestClassSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>||~~OperationRequestOperationRequestClassKey~~<br>|~~OperationRequestOperationRequestClassKey~~<br>|~~OperationRequestOperationRequestClassKey~~<br>|~~OperationRequestOperationRequestClassKey~~<br>|
|~~----~~|~~----~~|~~<site_id>~~|~~Y~~||~~OperationRequestId~~|~~OperationRequestId~~|~~OperationRequestId~~|~~OperationRequestId~~|


|UADM|vWorkOrderOperation_1431095118 or<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Id|Y|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestClassId~~|~~OperationRequestClassId~~|~~OperationRequestClassId~~|~~OperationRequestClassId~~|
|~~----~~|~~----~~|~~WorkOrderOperation OR "ExecutionGroup" OR~~<br>"ExecutionGroupPhase" OR "WorkOrderStep"|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
||||~~Y~~<br>|~~**OperationRequestStatus**~~||~~**Status of**~~<br>**WorkOrderOperation/WorkOrderStep**|||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestStatusSiteId~~<br>||||
|~~UADM~~<br>|~~vStatus_Siemens_Sim_2045546455~~<br>|~~NId~~<br>|~~Y~~<br>||~~OperationRequestStatusKey~~<br>|~~OperationRequestStatusKey~~<br>|~~OperationRequestStatusKey~~<br>|~~OperationRequestStatusKey~~<br>|
|~~UADM~~|~~vStatus_Siemens_Sim_2045546455~~|~~Name~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|
||||Y<br>|~~**OperationResponse**~~||~~**WorkOrderOperation/WorkOrderStep**~~|~~UI Work Orders >> open a WorkOrder >> tab Operations UI Work~~<br>Orders >> open a WorkOrder >> tab Operations >> tab Steps||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>||~~OperationResponseKey~~<br>|~~OperationResponseKey~~<br>|~~OperationResponseKey~~<br>|~~OperationResponseKey~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Name OR Nid~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Sequence~~<br>|~~Y~~<br>||~~Sequence~~<br>|~~Sequence~~<br>|~~Sequence~~<br>|~~Sequence~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|~~OperationDefinitionId~~|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~Operation~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationExecutionId~~<br>|~~OperationExecutionId~~<br>|~~OperationExecutionId~~<br>|~~OperationExecutionId~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~Nid~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseStatusId~~|~~OperationResponseStatusId~~|~~OperationResponseStatusId~~|~~OperationResponseStatusId~~|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~StatusNId.Status~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationRequestId~~|~~OperationRequestId~~|~~OperationRequestId~~|~~OperationRequestId~~|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~ProducedQuantity~~<br>|~~Y~~<br>||~~ProducedQuantity~~<br>|~~ProducedQuantity~~<br>|~~ProducedQuantity~~<br>|~~ProducedQuantity~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~ReworkedQuantity~~<br>|~~Y~~<br>||~~ReworkedQuantity~~<br>|~~ReworkedQuantity~~<br>|~~ReworkedQuantity~~<br>|~~ReworkedQuantity~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~ScrappedQuantity~~<br>|~~Y~~<br>||~~ScrapQuantity~~<br>|~~ScrapQuantity~~<br>|~~ScrapQuantity~~<br>|~~ScrapQuantity~~<br>|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~UoMNId~~<br>|~~Y~~<br>||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~ActualStartTime~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~ActualEndTime~~<br>|~~Y~~<br>||~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|
|~~UADM~~|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233|~~ExecutionDuration~~|~~Y~~||~~Duration~~|~~Duration~~|~~Duration~~|~~Duration~~|
||||Y<br>|~~**OperationResponseClass**~~||~~**WorkOperationType**~~|~~UI Work Operations~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseClassSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOperationType_Si_94474546~~<br>|~~Id OR "WorkOrderOperation" OR "ExecutionGroup"~~<br>OR "ExecutionGroupPhase" OR "WorkOrderStep"<br>|~~Y~~<br><br>||~~OperationResponseClassKey~~<br>|~~OperationResponseClassKey~~<br>|~~OperationResponseClassKey~~<br>|~~OperationResponseClassKey~~<br>|
|~~UADM~~|~~vWorkOperationType_Si_94474546~~|~~NId OR "WorkOrderOperation" OR "ExecutionGroup"~~<br>OR "ExecutionGroupPhase" OR "WorkOrderStep"|~~Y~~||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
||||Y<br>|~~**OperationResponseEquipmentRequirement**~~<br>|~~**OperationResponseEquipmentRequirement**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseEquipmentRequirementSiteId~~<br>||||
|~~UADM~~<br>|~~vToBeUsedMachine_Sie_107405297~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationResponseEquipmentRequirementKey~~<br>|~~OperationResponseEquipmentRequirementKey~~<br>|~~OperationResponseEquipmentRequirementKey~~<br>|~~OperationResponseEquipmentRequirementKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~vToBeUsedMachine_Sie_107405297~~<br>|~~WorkOrderOperation_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~<br>|~~vToBeUsedMachine_Sie_107405297~~<br>|~~Machine~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~1~~|~~Y~~||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
||||Y<br>|~~**OperationResponseEquipmentSpecification**~~<br>|~~**OperationResponseEquipmentSpecification**~~<br>|~~**ActualUsedMachine**~~|~~UI Work Orders >> select a WorkOrder >> button As Built >> tab~~<br>Activity History<br>You can also see them on UI Genealogy, in the tree representation,<br>under each WorkOrderOperation node||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseEquipmentSpecificationSiteId~~<br>||||
|~~UADM~~<br>|~~vActualUsedMachine__2012847191~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationResponseEquipmentSpecificationKey~~<br>|~~OperationResponseEquipmentSpecificationKey~~<br>|~~OperationResponseEquipmentSpecificationKey~~<br>|~~OperationResponseEquipmentSpecificationKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~vActualUsedMachine__2012847191~~<br>|~~WorkOrderOperations_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~<br>|~~vActualUsedMachine__2012847191~~<br>|~~Machine~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~vWorkOrderOperation_1431095118~~<br>|~~ActualStartTime~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~----~~|~~vWorkOrderOperation_1431095118~~|~~ActualEndTime~~|~~Y~~||~~EndDateTime~~|~~EndDateTime~~|~~EndDateTime~~|~~EndDateTime~~|
||||Y<br>|~~**OperationResponseHierarchy**~~||~~**WorkOrderOperation/WorkOrderStep**~~|~~UI Work Orders >> tab Operations >> tab Steps~~|~~Hierarchical association between WorkOrderOperation and~~<br>WorkOrderStep|
|~~----~~|~~----~~|~~<site_id>~~|~~Y~~||~~OperationResponseHierarchySiteId~~||||


|UADM|vExecutionGroupPhase_469816675 or<br>vExecutionGroupPhase_931440969 or<br>vWorkOrderStep_Siem_1809795233|Id|Y|Col5|OperationResponseHierarchyKey|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~vExecutionGroupPhase_469816675 or~~<br>vExecutionGroupPhase_931440969 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Id OR~~<br>WorkOrderOperation_Id OR<br>Id<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ParentOperationResponseId~~|~~ParentOperationResponseId~~|~~ParentOperationResponseId~~|~~ParentOperationResponseId~~|
|~~UADM~~|~~vExecutionGroupPhase_469816675 or~~<br>vExecutionGroupPhase_931440969 or<br>vWorkOrderStep_Siem_1809795233|~~ExecutionGroup_Id OR~~<br>ExecutionGroupPhase_Id OR<br>WorkOrderOperation_Id|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**OperationResponseLaborSpecification**~~<br>|~~**OperationResponseLaborSpecification**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseLaborSpecificationSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrderHistory_Si_518515069~~<br>|~~(UserId + '_' + WorkOrderOperation_Id  + '_' + Date)~~<br>OR (UserId + '_' + ExecutionGroupPhaseId + '_' +<br>Date) OR (UserId + '_' + WorkOrderStep_Id + '_' +<br>Date)<br>|~~Y~~<br>||~~OperationResponseLaborSpecificationKey~~<br>|~~OperationResponseLaborSpecificationKey~~<br>|~~OperationResponseLaborSpecificationKey~~<br>|~~OperationResponseLaborSpecificationKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~LaborId~~|~~LaborId~~|~~LaborId~~|~~LaborId~~|
|~~UADM~~<br>|~~vWorkOrderHistory_Si_518515069~~<br>|~~UserId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~vWorkOrderHistory_Si_518515069~~<br>|~~WorkOrderOperation_Id OR ExecutionGroupPhaseId~~<br>OR WorkOrderStep_Id<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkOrderHistory_Si_518515069~~<br>|~~Date~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~UADM~~|~~vWorkOrderHistory_Si_518515069~~|~~Date~~|~~Y~~||~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|
||||Y<br>|~~**OperationResponseMaterialDefinitionRequirementIn**~~<br>|~~**OperationResponseMaterialDefinitionRequirementIn**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseMaterialDefinitionRequirementInSiteId~~<br>||||
|~~UADM~~<br>|~~vToBeConsumedMateri_2105885214~~<br>|~~id~~<br>|~~Y~~<br>||~~OperationResponseMaterialDefinitionRequirementInKey~~<br>|~~OperationResponseMaterialDefinitionRequirementInKey~~<br>|~~OperationResponseMaterialDefinitionRequirementInKey~~<br>|~~OperationResponseMaterialDefinitionRequirementInKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~<br>|~~OperationResponseId~~<br>|~~OperationResponseId~~<br>|~~OperationResponseId~~<br>|
|~~UADM~~<br>|~~vToBeConsumedMateri_2105885214~~<br>|~~WorkOrderOperation_Id OR WorkOrderStep_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vMaterial_Siemens_Si_170253665~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vToBeConsumedMateri_2105885214~~<br>|~~Quantity~~<br>|~~Y~~<br>||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
|~~UADM~~|~~vMaterial_Siemens_Si_170253665~~|~~UoMNId~~|~~Y~~||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
||||Y<br>|~~**OperationResponseMaterialLotSpecificationIn**~~<br>|~~**OperationResponseMaterialLotSpecificationIn**~~<br>|~~**ActualConsumedMaterial**~~|~~UI Work Orders >> select a WorkOrder >> button As Built >> tab~~<br>Material. You can also see them on UI Genealogy, in the tree<br>representation, under each WorkOrderOperation node||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseMaterialLotSpecificationInSiteId~~<br>||||
|~~UADM~~<br>|~~vActualConsumedMater_420487820~~<br>|~~(Id + '_WorkOrderOperation') OR (Id +~~<br>'_WorkOrderStep')<br>|~~Y~~<br>||~~OperationResponseMaterialLotSpecificationInKey~~<br>|~~OperationResponseMaterialLotSpecificationInKey~~<br>|~~OperationResponseMaterialLotSpecificationInKey~~<br>|~~OperationResponseMaterialLotSpecificationInKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~vActualConsumedMater_420487820~~<br>|~~WorkOrderOperation_Id OR WorkOrderStep_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~|~~vActualConsumedMater_420487820~~|~~MaterialItemAssembledQty~~|~~Y~~||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
||||Y<br>|~~**OperationResponseMaterialLotSpecificationOut**~~<br>|~~**OperationResponseMaterialLotSpecificationOut**~~<br>|~~**ProducedMaterialItem**~~|~~UI Work Orders >> open a WorkOrder: BatchID property/tab Serial~~<br>Numbers<br>UI Genealogy||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseMaterialLotSpecificationOutSiteId~~<br>||||
|~~UADM~~<br>|~~vActualConsumedMater_420487820~~<br>|~~(Id + '_WorkOrderOperation') OR (Id +~~<br>'_WorkOrderStep')<br>|~~Y~~<br>||~~OperationResponseMaterialLotSpecificationOutKey~~<br>|~~OperationResponseMaterialLotSpecificationOutKey~~<br>|~~OperationResponseMaterialLotSpecificationOutKey~~<br>|~~OperationResponseMaterialLotSpecificationOutKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~vActualConsumedMater_420487820~~<br>|~~WorkOrderOperation_Id OR WorkOrderStep_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|~~MaterialLotId~~|
|~~UADM~~<br>|~~vMaterialTrackingUni_494706508~~<br>|~~NId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~|~~vActualConsumedMater_420487820~~|~~ProducedMaterialItemActualQty~~|~~Y~~||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
||||Y<br>|~~**OperationResponseOperationResponseClass**~~<br>|~~**OperationResponseOperationResponseClass**~~<br>|~~**WorkOrderOperation**~~|~~UI Work Orders >> open a WorkOrder >> tab Operations~~|~~WorkOrderOperation-WorkOperationType association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseOperationResponseClassSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~((Id  + '_WorkOperationType') OR (Id  +~~<br>'_WorkOrderOperation' )) OR<br>(Id + '_ExecutionGroup') OR<br>(Id  + '_ExecutionGroupPhase') OR<br>(Id + '_WorkOrderStep')<br>|~~Y~~<br>||~~OperationResponseOperationResponseClassKey~~<br>|~~OperationResponseOperationResponseClassKey~~<br>|~~OperationResponseOperationResponseClassKey~~<br>|~~OperationResponseOperationResponseClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseClassId~~|~~OperationResponseClassId~~|~~OperationResponseClassId~~|~~OperationResponseClassId~~|
|~~UADM~~|~~vWorkOrderOperation_1431095118 or~~<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|~~((WorkOperationType) OR ("WorkOrderOperation"))~~<br>OR<br>"ExecutionGroup" OR<br>"ExecutionGroupPhase" OR<br>"WorkOrderStep"|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**OperationResponseProperty**~~||~~**Attribute of a WorkOrderOperation**~~|~~UI Work Orders >> open a WorkOrder >> tab Operations~~|~~"ElectronicSignatureComplete" , "ElectronicSignaturePause" ,~~<br>"ElectronicSignatureStart" , "EstimatedDuration" , "IsReady" ,<br>"LastPauseTime" , "Optional" , "PauseDuration" ,<br>"ExecutionDuration" , "Priority" , "RequiredCertificateNId" ,<br>"RequiredInspectionRole" , "TargetQuantity" ,<br>"WaitingForInspection" , "ActiveNonConformanceNr"|
|~~----~~|~~----~~|~~<site_id>~~|~~Y~~||~~OperationResponsePropertySiteId~~||||


|----|----|"AvailableQuantity" or<br>"ElectronicSignatureComplete" or<br>"ElectronicSignaturePause" or<br>"ElectronicSignatureStart" or<br>"IsReady" or<br>"Skippable" or<br>"LastPauseTime" or<br>"Optional" or<br>"PauseDuration" or<br>"PartialWorkedQuantity" or<br>"Priority" or<br>"RequiredCertificateNId" or or<br>"RequiredInspectionRole"<br>"TargetQuantity" or<br>"WaitingForInspection" or<br>"ActiveNonConformanceNr"|Y|Col5|OperationResponsePropertyKey|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~"AvailableQuantity" or~~<br>"ElectronicSignatureComplete" or<br>"ElectronicSignaturePause" or<br>"ElectronicSignatureStart" or<br>"IsReady" or<br>"Skippable" or<br>"LastPauseTime" or<br>"Optional" or<br>"PauseDuration" or<br>"PartialWorkedQuantity" or<br>"Priority" or<br>"RequiredCertificateNId" or or<br>"RequiredInspectionRole"<br>"TargetQuantity" or<br>"WaitingForInspection" or<br>"ActiveNonConformanceNr"<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~"Numeric" or "DateTime" or "String"~~<br>|~~Y~~<br>||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
|~~----~~|~~----~~|~~"n/a"~~|~~Y~~||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
||||Y<br>|~~**OperationResponsePropertyStaticValue**~~<br>|~~**OperationResponsePropertyStaticValue**~~<br>|~~**Value for a WorkOrderOperation attribute**~~|~~UI Work Orders >> open a WorkOrder >> tab Operations, grid mode~~|~~"ElectronicSignatureComplete" , "ElectronicSignaturePause" ,~~<br>"ElectronicSignatureStart" , "EstimatedDuration" , "IsReady" ,<br>"LastPauseTime" , "Optional" , "PauseDuration" ,<br>"ExecutionDuration" , "Priority" , "RequiredCertificateNId" ,<br>"RequiredInspectionRole" , "TargetQuantity" ,<br>"WaitingForInspection" , "ActiveNonConformanceNr"|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponsePropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~(Id +'_'+'AvailableQuantity') or~~<br>(Id +'_'+'ElectronicSignatureComplete') or<br>(Id +'_'+'ElectronicSignaturePause') or<br>(Id +'_'+'ElectronicSignatureStart') or<br>(Id +'_'+'IsReady') or<br>(Id +'_'+'Skippable') or<br>(Id +'_'+'LastPauseTime') or<br>(Id +'_'+'Optional') or<br>(Id +'_'+'PauseDuration') or<br>(Id +'_'+'PartialWorkedQuantity') or<br>(Id +'_'+'Priority') or<br>(Id +'_'+'RequiredCertificateNId')or<br>(Id +'_'+'RequiredInspectionRole') or<br>(Id +'_'+'TargetQuantity') or<br>(Id +'_'+'WaitingForInspection') or<br>(Id +'_'+'ActiveNonConformanceNr')<br>|~~Y~~<br>||~~OperationResponsePropertyStaticValueKey~~<br>|~~OperationResponsePropertyStaticValueKey~~<br>|~~OperationResponsePropertyStaticValueKey~~<br>|~~OperationResponsePropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~SitmesDb~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponsePropertyId~~|~~OperationResponsePropertyId~~|~~OperationResponsePropertyId~~|~~OperationResponsePropertyId~~|
|~~----~~<br>|~~----~~<br>|~~"AvailableQuantity" or~~<br>"ElectronicSignatureComplete" or<br>"ElectronicSignaturePause" or<br>"ElectronicSignatureStart" or<br>"IsReady" or<br>"Skippable" or<br>"LastPauseTime" or<br>"Optional" or<br>"PauseDuration" or<br>"PartialWorkedQuantity" or<br>"Priority" or<br>"RequiredCertificateNId" or or<br>"RequiredInspectionRole"<br>"TargetQuantity" or<br>"WaitingForInspection" or<br>"ActiveNonConformanceNr"<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~RequiredCertificateNId, RequiredInspectionRole~~<br>|~~Y~~<br>||~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|
|~~UADM~~<br>|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233<br>|~~ElectronicSignatureComplete,~~<br>ElectronicSignaturePause, ElectronicSignatureStart,<br>IsReady, Optional, PauseDuration,<br>PartialWorkedQuantity, Priority, TargetQuantity,<br>WaitingForInspection, ActiveNonConformanceNr,<br>AvailableQuantity, Skippable<br>|~~Y~~<br>||~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|
|~~UADM~~|~~vWorkOrderOperation_1431095118 or~~<br>vWorkOrderStep_Siem_1809795233|~~LastPauseTime~~|~~Y~~||~~DatetimeValue~~|~~DatetimeValue~~|~~DatetimeValue~~|~~DatetimeValue~~|
||||Y<br>|~~**OperationResponseStatus**~~||~~**Status attribute of**~~<br>**WorkOrderOperation/WorkOrderStep**|||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseStatusSiteId~~<br>||||
|~~UADM~~<br>|~~vStatus_Siemens_Sim_2045546455~~<br>|~~NId~~<br>|~~Y~~<br>||~~OperationResponseStatusKey~~<br>|~~OperationResponseStatusKey~~<br>|~~OperationResponseStatusKey~~<br>|~~OperationResponseStatusKey~~<br>|
|~~UADM~~|~~vStatus_Siemens_Sim_2045546455~~|~~Name~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|


|Col1|Col2|Col3|Y|OperationResponseToolSpecification|Col6|ActualUsedTool|UI Work Orders >> select a WorkOrder >> button As Built >> tab<br>Activity Tools<br>You can also see them on UI Genealogy, in the tree representation,<br>under each WorkOrderOperation node|Col9|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseToolSpecificationSiteId~~<br>||||
|~~UADM~~<br>|~~vActualUsedTool_Sie_1932879556~~<br>|~~(Id  + 'WorkOrderOperation') OR~~<br>(Id  + 'WorkOrderStep')<br>|~~Y~~<br>||~~OperationResponseToolSpecificationKey~~<br>|~~OperationResponseToolSpecificationKey~~<br>|~~OperationResponseToolSpecificationKey~~<br>|~~OperationResponseToolSpecificationKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolId~~|~~ToolId~~|~~ToolId~~|~~ToolId~~|
|~~----~~<br>|~~vActualUsedTool_Sie_1932879556~~<br>|~~Tool_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~<br>|~~----~~<br>|~~WorkOrderOperation_Id OR WorkOrderStep_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~|~~vActualUsedTool_Sie_1932879556~~|~~UsedTimes~~|~~Y~~||~~Quantity~~|~~Quantity~~|~~Quantity~~|~~Quantity~~|
||||Y<br>|~~**OperationScheduling**~~||~~**WorkOrder**~~|~~UI Work Orders >> tab Details~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationSchedulingSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationSchedulingKey~~<br>|~~OperationSchedulingKey~~<br>|~~OperationSchedulingKey~~<br>|~~OperationSchedulingKey~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Name OR Nid~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Notes~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Plant~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vDM_Material_Siemens_463872986~~<br>|~~Material_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~StatusNId.Status~~<br>|~~Y~~<br>||~~OperationSchedulingStatusId~~|~~OperationSchedulingStatusId~~|~~OperationSchedulingStatusId~~|~~OperationSchedulingStatusId~~|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~EstimatedStartTime~~<br>|~~Y~~<br>||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~EstimatedEndTime~~<br>|~~Y~~<br>||~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|~~EndDateTime~~<br>|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~InitialQuantity~~<br>|~~Y~~<br>||~~EstimatedQuantity~~<br>|~~EstimatedQuantity~~<br>|~~EstimatedQuantity~~<br>|~~EstimatedQuantity~~<br>|
|~~UADM~~|~~vWorkOrder_Siemens_S_749389132~~|~~EstimatedStartTime -EstimatedEndTime~~|~~Y~~||~~Duration~~|~~Duration~~|~~Duration~~|~~Duration~~|
||||Y<br>|~~**OperationSchedulingClass**~~||~~**ExecutionGroup**~~|~~UI Execution Groups >> tab Details~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationSchedulingClassSiteId~~<br>||||
|~~UADM~~<br>|~~vProductionType_Siem_763981173~~<br>|~~Id + '_ProductionType'~~<br>|~~Y~~<br>||~~OperationSchedulingClassKey~~<br>|~~OperationSchedulingClassKey~~<br>|~~OperationSchedulingClassKey~~<br>|~~OperationSchedulingClassKey~~<br>|
|~~UADM~~<br>|~~vProductionType_Siem_763981173~~<br>|~~NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~|~~----~~|~~----~~|~~Y~~||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
||||Y<br>|~~**OperationSchedulingOperationSchedulingClass**~~<br>|~~**OperationSchedulingOperationSchedulingClass**~~<br>|~~**WorkOrder**~~||~~WorkOrder-ExecutionGroup association~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationSchedulingOperationSchedulingClassSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~Id~~<br>|~~Y~~<br>||~~OperationSchedulingOperationSchedulingClassKey~~<br>|~~OperationSchedulingOperationSchedulingClassKey~~<br>|~~OperationSchedulingOperationSchedulingClassKey~~<br>|~~OperationSchedulingOperationSchedulingClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationSchedulingClassId~~|~~OperationSchedulingClassId~~|~~OperationSchedulingClassId~~|~~OperationSchedulingClassId~~|
|~~UADM~~<br>|~~vWorkOrder_Siemens_S_749389132~~<br>|~~ProductionType_Id  + '_ProductionType'~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationSchedulingId~~|~~OperationSchedulingId~~|~~OperationSchedulingId~~|~~OperationSchedulingId~~|
|~~UADM~~|~~vWorkOrder_Siemens_S_749389132~~|~~Id~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**OperationSchedulingStatus**~~||~~**Status of WorkOrder**~~|||
|~~UADM~~<br>|~~vStatus_Siemens_Sim_2045546455~~<br>|~~NId~~<br>|~~Y~~<br>||~~OperationSchedulingStatusKey~~<br>||||
|~~UADM~~|~~vStatus_Siemens_Sim_2045546455~~|~~Name~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|
||||Y<br>|~~**ProductionProcess**~~|||||
|~~UADM~~<br>|~~vProcess_Siemens_Si_2118577807~~<br>|~~UId~~<br>|~~Y~~<br>||~~ProductionProcessKey~~<br>|~~ProductionProcessKey~~<br>|~~ProductionProcessKey~~<br>|~~ProductionProcessKey~~<br>|
|~~UADM~~<br>|~~vProcess_Siemens_Si_2118577807~~<br>|~~Name or null~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~vProcess_Siemens_Si_2118577807~~<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|~~MaterialDefinitionId~~|
|~~UADM~~<br>|~~vDM_Material_Siemens_463872986~~<br>|~~Material_Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vProcess_Siemens_Si_2118577807~~<br>|~~QuantityValue.Quantity~~<br>|~~Y~~<br>||~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|~~Quantity~~<br>|
|~~UADM~~|~~vProcess_Siemens_Si_2118577807~~|~~UoMNId.Quantity~~|~~Y~~||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
||||Y<br>|~~**ProductionProcessOperationDefinition**~~<br>|~~**ProductionProcessOperationDefinition**~~<br>||||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ProductionProcessOperationDefinitionSiteId~~<br>||||
|~~UADM~~<br>|~~vProcessToOperation_2065129030~~<br>|~~Id~~<br>|~~Y~~<br>||~~ProductionProcessOperationDefinitionKey~~<br>|~~ProductionProcessOperationDefinitionKey~~<br>|~~ProductionProcessOperationDefinitionKey~~<br>|~~ProductionProcessOperationDefinitionKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|~~OperationDefinitionId~~<br>|
|~~UADM~~<br>|~~vOperation_Siemens_S_700803909~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ProductionProcessId~~|~~ProductionProcessId~~|~~ProductionProcessId~~|~~ProductionProcessId~~|
|~~UADM~~<br>|~~vProcess_Siemens_Si_2118577807~~<br>|~~UId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~1~~|~~Y~~||~~Quantity~~|~~Quantity~~|~~Quantity~~|~~Quantity~~|
||||Y<br>|~~**PropertyType**~~|||||
|~~----~~<br>|~~----~~<br>|~~"String" or "Numeric" or "DateTime"~~<br>|~~Y~~<br>||~~PropertyTypeKey~~<br>||||
|~~----~~|~~----~~|~~"String" or "Numeric" or "DateTime"~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|
||||Y<br>|~~**QualityLimit**~~|||~~UI DCD Engineering~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityLimitSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkInstructionStep_626862590~~<br>|~~Id~~<br>|~~Y~~<br>||~~QualityLimitKey~~<br>|~~QualityLimitKey~~<br>|~~QualityLimitKey~~<br>|~~QualityLimitKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityParameterId~~|~~QualityParameterId~~|~~QualityParameterId~~|~~QualityParameterId~~|
|~~UADM~~<br>|~~vWorkInstructionStep_626862590~~<br>|~~ItemNId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkInstructionStep_626862590~~<br>|~~HighLimit~~<br>|~~Y~~<br>||~~HighLimit~~<br>|~~HighLimit~~<br>|~~HighLimit~~<br>|~~HighLimit~~<br>|
|~~UADM~~<br>|~~vWorkInstructionStep_626862590~~<br>|~~Target~~<br>|~~Y~~<br>||~~Target~~<br>|~~Target~~<br>|~~Target~~<br>|~~Target~~<br>|
|~~UADM~~|~~vWorkInstructionStep_626862590~~|~~LowLimit~~|~~Y~~||~~LowLimit~~|~~LowLimit~~|~~LowLimit~~|~~LowLimit~~|
||||Y<br>|~~**QualityParameter**~~|||~~UI DCD Engineering~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityParameterSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkInstructionStepIt_1299831 or~~<br>vRuntimeCharacteris_1195087565 or<br>vVisualDetectedFailu_686437194<br>|~~ItemNId OR~~<br> Id OR<br>FailureNId<br>|~~Y~~<br>||~~QualityParameterKey~~<br>|~~QualityParameterKey~~<br>|~~QualityParameterKey~~<br>|~~QualityParameterKey~~<br>|
|~~UADM~~<br>|~~vWorkInstructionStepIt_1299831 or~~<br>vRuntimeCharacteris_1195087565 or<br>vVisualDetectedFailu_686437194<br>|~~Label OR~~<br>Label OR<br>FailureNId<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vWorkInstructionStepIt_1299831 or~~<br>vRuntimeCharacteris_1195087565 or<br>vVisualDetectedFailu_686437194|~~Caption OR~~<br>Label OR<br>FailureNId|~~Y~~||~~Description~~|~~Description~~|~~Description~~|~~Description~~|


|Col1|Col2|Col3|Y|QualityParameterValue|Col6|DCDRuntime|UI Operator Landing Page >> select a WorkOrderOperation >> Show<br>Details >> tab Data Collection; UI Genealogy; UI Work Orders >> As<br>Built >> tab Data Collections|Contains the values of data collection stored at runtime, e.g. data<br>collection values acquired on a WorkOrderOperation, or from the<br>automation gateway, etc|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityParameterValueSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkInstructionStepIt_1299831 or~~<br>vInspectionValue_Siem_97476695 or<br>vVisualDetectedFailu_686437194<br>|~~Id~~<br>|~~Y~~<br>||~~QualityParameterValueKey~~<br>|~~QualityParameterValueKey~~<br>|~~QualityParameterValueKey~~<br>|~~QualityParameterValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseId~~|~~QualityResponseId~~|~~QualityResponseId~~|~~QualityResponseId~~|
|~~UADM~~<br>|~~vWorkInstructionSect_440022636 or~~<br>vInspectionValue_Siem_97476695 or<br>vVisualDetectedFailu_686437194<br>|~~WorkInstruction_Id OR~~<br>InspectionSample_Id OR<br>InspectionSample_Id<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityParameterId~~|~~QualityParameterId~~|~~QualityParameterId~~|~~QualityParameterId~~|
|~~UADM~~<br>|~~vWorkInstructionStepIt_1299831 or~~<br>vInspectionValue_Siem_97476695 or<br>vVisualDetectedFailu_686437194<br>|~~ItemNId OR~~<br>Id OR<br>FailureNId<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vWorkInstructionStepIt_1299831~~<br>|~~(ItemValue OR null)~~<br>|~~Y~~<br>||~~DatetimeValue~~<br>|~~DatetimeValue~~<br>|~~DatetimeValue~~<br>|~~DatetimeValue~~<br>|
|~~UADM~~<br>|~~vWorkInstructionStepIt_1299831 or~~<br>vInspectionValue_Siem_97476695 or<br>vVisualDetectedFailu_686437194<br>|~~(ItemValue OR null) OR~~<br>(MeasuredVariableValue OR<br>MeasuredAttributeValuel) OR<br>Count<br>|~~Y~~<br>||~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|
|~~UADM~~<br>|~~vWorkInstructionStepIt_1299831~~<br>|~~(ItemValue OR null)~~<br>|~~Y~~<br>||~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|
|~~UADM~~|~~vWorkInstructionStepIt_1299831 or~~<br>vInspectionValue_Siem_97476695 or<br>vVisualDetectedFailu_686437194|~~LastValueUpdatedOn OR~~<br>Timestamp OR<br>Timestamp|~~Y~~||~~StartDateTime~~|~~StartDateTime~~|~~StartDateTime~~|~~StartDateTime~~|
||||Y<br>|~~**QualityResponse**~~||~~**DCDRuntimeTask**~~|~~UI Operator Landing Page >> select a WorkOrderOperation >> Show~~<br>Details >> tab Data Collection; UI Genealogy; UI Work Orders >> As<br>Built >> tab Data Collections|~~Contains the association between the runtime data collection and~~<br>the WorkOrderOperation / WorkOrderStep / K873MaterialItem, etc|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkInstruction_Si_1625357712 or~~<br>vInspectionSample_S_1984849077<br>|~~Id~~<br>|~~Y~~<br>||~~QualityResponseKey~~<br>|~~QualityResponseKey~~<br>|~~QualityResponseKey~~<br>|~~QualityResponseKey~~<br>|
|~~UADM~~<br>|~~vWorkInstruction_Si_1625357712 or~~<br>vInspectionSample_S_1984849077<br>|~~(Name OR NId) OR~~<br>Id<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vWorkInstruction_Si_1625357712~~<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~LaborId~~|~~LaborId~~|~~LaborId~~|~~LaborId~~|
|~~UADM~~<br>|~~ vInspectionSample_S_1984849077~~<br>|~~User~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseStatusId~~<br>|~~QualityResponseStatusId~~<br>|~~QualityResponseStatusId~~<br>|~~QualityResponseStatusId~~<br>|
|~~UADM~~<br>|~~vWorkInstruction_Si_1625357712~~<br>|~~StatusNId.Status~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|~~EquipmentId~~|
|~~UADM~~<br>|~~vInspectionAcquisiti_557646680~~<br>|~~EquipmentNId~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityTaskDefinitionId~~|~~QualityTaskDefinitionId~~|~~QualityTaskDefinitionId~~|~~QualityTaskDefinitionId~~|
|~~UADM~~<br>|~~vWorkInstruction_Si_1625357712~~<br>|~~WorkInstructionDefinitionNId + '_' +~~<br>WorkInstructionDef_1609828362<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|~~OperationResponseId~~|
|~~UADM~~|~~vWorkInstructionToWo_350679847 or~~<br>dbo.vWorkInstructionToWo_665152508 or<br>vWorkInstructionToEx_538872687 or<br>vToBeUsedInspection__861818088|~~(WorkOrderOperation_Id or~~<br> workorderstep_id  or<br>executiongroupphase_id)  OR<br>(WorkOrderOperation_Id or workorderstep_id)|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
||||~~Y~~<br>|~~**QualityResponseClass**~~||~~**Type of DCDRuntimeTask**~~|||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseClassSiteId~~<br>|||"WorkInstruction" OR "InspectionSample"|
|~~----~~<br>|~~----~~<br>|~~"WorkInstruction" OR "InspectionSample"~~<br>|~~Y~~<br>||~~QualityResponseClassKey~~<br>|~~QualityResponseClassKey~~<br>|~~QualityResponseClassKey~~<br>|~~QualityResponseClassKey~~<br>|
|~~----~~|~~----~~|~~"WorkInstruction" OR "InspectionSample"~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|
||||Y<br>|~~**QualityResponseProperty**~~||~~**DCDRuntimeTask property**~~|||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponsePropertySiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~"AnyViolation"~~<br>|~~Y~~<br>||~~QualityResponsePropertyKey~~<br>|~~QualityResponsePropertyKey~~<br>|~~QualityResponsePropertyKey~~<br>|~~QualityResponsePropertyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~AnyViolation~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~"n/a"~~<br>|~~Y~~<br>||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
|~~----~~|~~----~~|~~"Numeric"~~|~~Y~~||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
||||Y<br>|~~**QualityResponsePropertyStaticValue**~~<br>|~~**QualityResponsePropertyStaticValue**~~<br>|~~**DCDRuntimeTask + DCDRuntime**~~|~~UI Operator Landing Page >> select a WorkOrderOperation >> Show~~<br>Details >> tab Data Collection; UI Genealogy; UI Work Orders >> As<br>Built >> tab Data Collections||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponsePropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vInspectionSample_S_1984849077~~<br>|~~Id + '_AnyViolation'~~<br>|~~Y~~<br>||~~QualityResponsePropertyStaticValueKey~~<br>|~~QualityResponsePropertyStaticValueKey~~<br>|~~QualityResponsePropertyStaticValueKey~~<br>|~~QualityResponsePropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseId~~|~~QualityResponseId~~|~~QualityResponseId~~|~~QualityResponseId~~|
|~~UADM~~<br>|~~vInspectionSample_S_1984849077~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponsePropertyId~~|~~QualityResponsePropertyId~~|~~QualityResponsePropertyId~~|~~QualityResponsePropertyId~~|
|~~----~~<br>|~~----~~<br>|~~"AnyViolation"~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~|~~vInspectionSample_S_1984849077~~|~~AnyViolation~~|~~Y~~<br>||~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|
||||~~Y~~<br>|~~**QualityResponseQualityResponseClass**~~<br>|~~**QualityResponseQualityResponseClass**~~<br>|~~**Relationship between DCDRuntimeTask and**~~<br>**its type**|||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseQualityResponseClassSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkInstruction_Si_1625357712 or~~<br>vInspectionSample_S_1984849077<br>|~~Id + '_WorkInstruction' OR~~<br>Id  + '_InspectionSample'<br>|~~Y~~<br>||~~QualityResponseQualityResponseClassKey~~<br>|~~QualityResponseQualityResponseClassKey~~<br>|~~QualityResponseQualityResponseClassKey~~<br>|~~QualityResponseQualityResponseClassKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseId~~|~~QualityResponseId~~|~~QualityResponseId~~|~~QualityResponseId~~|
|~~UADM~~<br>|~~vWorkInstruction_Si_1625357712 or~~<br>vInspectionSample_S_1984849077<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseClassId~~|~~QualityResponseClassId~~|~~QualityResponseClassId~~|~~QualityResponseClassId~~|
|~~----~~|~~----~~|~~'WorkInstruction" OR "InspectionSample"~~|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
||||~~Y~~<br>|~~**QualityResponseStatus**~~||~~**DCDRuntimeTask status**~~|||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityResponseStatusSiteId~~<br>||||
|~~UADM~~<br>|~~vStatus_Siemens_Sim_2045546455~~<br>|~~NId~~<br>|~~Y~~<br>||~~QualityResponseStatusKey~~<br>|~~QualityResponseStatusKey~~<br>|~~QualityResponseStatusKey~~<br>|~~QualityResponseStatusKey~~<br>|
|~~UADM~~|~~vStatus_Siemens_Sim_2045546455~~|~~Name~~|~~Y~~||~~Name~~|~~Name~~|~~Name~~|~~Name~~|


|Col1|Col2|Col3|Y|QualityTaskDefinition|Col6|DCDTask|UI DCD Engineering; UI Operation Catalog >> Operation Details >><br>tab Data collections; UI Work Orders >> Operations >> tab Data<br>Collections|Defines a runtime data collection|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityTaskDefinitionSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkInstructionDefi_275522137~~<br>|~~NId + '_' + Revision~~<br>|~~Y~~<br>||~~QualityTaskDefinitionKey~~<br>|~~QualityTaskDefinitionKey~~<br>|~~QualityTaskDefinitionKey~~<br>|~~QualityTaskDefinitionKey~~<br>|
|~~UADM~~<br>|~~vWorkInstructionDefi_275522137~~<br>|~~Name OR NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vWorkInstructionDefi_275522137~~|~~Description~~|~~Y~~||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
||||Y<br>|~~**QualityTaskDefinitionProperty**~~<br>|~~**QualityTaskDefinitionProperty**~~<br>|~~**DCDTask property**~~|~~UI DCD Engineering; UI Operation Catalog >> Operation Details >>~~<br>tab Data collections; UI Work Orders >> Operations >> tab Data<br>Collections|~~"Status" or "IsCurrent"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityTaskDefinitionPropertySiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~"IsExecutable" or "IsCurrent"~~<br>|~~Y~~<br>||~~QualityTaskDefinitionPropertyKey~~<br>|~~QualityTaskDefinitionPropertyKey~~<br>|~~QualityTaskDefinitionPropertyKey~~<br>|~~QualityTaskDefinitionPropertyKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~"IsExecutable" or "IsCurrent"~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~"Numeric"~~<br>|~~Y~~<br>||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
|~~----~~|~~----~~|~~"n/a"~~|~~Y~~||~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|~~UomId~~<br>|
||||Y<br>|~~**QualityTaskDefinitionPropertyStaticValue**~~<br>|~~**QualityTaskDefinitionPropertyStaticValue**~~<br>|~~**DCDTask property value**~~|~~UI DCD Engineering; UI Operation Catalog >> Operation Details >>~~<br>tab Data collections; UI Work Orders >> Operations >> tab Data<br>Collections|~~"Approved" or "Editing" or "Obsolete" or "Unknown"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityTaskDefinitionPropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vWorkInstructionDefi_275522137~~<br>|~~NId + '_' + Revision~~<br>|~~Y~~<br>||~~QualityTaskDefinitionPropertyStaticValueKey~~<br>|~~QualityTaskDefinitionPropertyStaticValueKey~~<br>|~~QualityTaskDefinitionPropertyStaticValueKey~~<br>|~~QualityTaskDefinitionPropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityTaskDefinitionId~~|~~QualityTaskDefinitionId~~|~~QualityTaskDefinitionId~~|~~QualityTaskDefinitionId~~|
|~~UADM~~<br>|~~vWorkInstructionDefi_275522137~~<br>|~~NId + '_' + Revision~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~QualityTaskDefinitionPropertyId~~|~~QualityTaskDefinitionPropertyId~~|~~QualityTaskDefinitionPropertyId~~|~~QualityTaskDefinitionPropertyId~~|
|~~----~~<br>|~~----~~<br>|~~"IsExecutable" or "IsCurrent"~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~|~~----~~|~~IsExecutable or IsCurrent~~|~~Y~~||~~FloatValue~~|~~FloatValue~~|~~FloatValue~~|~~FloatValue~~|
||||Y<br>|~~**Site**~~|||||
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~SiteId~~<br>||||
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~TimeZoneId~~<br>|~~TimeZoneId~~<br>|~~TimeZoneId~~<br>|~~TimeZoneId~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~Longitude~~<br>|~~Longitude~~<br>|~~Longitude~~<br>|~~Longitude~~<br>|
|~~----~~|~~----~~|~~----~~|~~Y~~||~~Latitude~~|~~Latitude~~|~~Latitude~~|~~Latitude~~|
||||Y<br>|~~**TimeZone**~~|||||
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~TimeZoneKey~~<br>||||
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~|~~----~~|~~----~~|~~Y~~||~~OffSet~~|~~OffSet~~|~~OffSet~~|~~OffSet~~|
||||Y<br>|~~**TimeZoneDaylightTimeSaving**~~|||||
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~TimeZoneDaylightTimeSavingKey~~<br>||||
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~TimeZoneId~~<br>|~~TimeZoneId~~<br>|~~TimeZoneId~~<br>|~~TimeZoneId~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~OffSet~~<br>|~~OffSet~~<br>|~~OffSet~~<br>|~~OffSet~~<br>|
|~~----~~<br>|~~----~~<br>|~~----~~<br>|~~Y~~<br>||~~DateFrom~~<br>|~~DateFrom~~<br>|~~DateFrom~~<br>|~~DateFrom~~<br>|
|~~----~~|~~----~~|~~----~~|~~Y~~||~~DateTo~~|~~DateTo~~|~~DateTo~~|~~DateTo~~|
||||Y<br>|~~**Tool**~~||~~**Tool**~~|~~UI Tools~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolSiteId~~<br>||||
|~~UADM~~<br>|~~vTool_Siemens_Simat_1812587140~~<br>|~~Id~~<br>|~~Y~~<br>||~~ToolKey~~<br>|~~ToolKey~~<br>|~~ToolKey~~<br>|~~ToolKey~~<br>|
|~~UADM~~<br>|~~vTool_Siemens_Simat_1812587140~~<br>|~~Name OR NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vTool_Siemens_Simat_1812587140~~<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolDefinitionId~~|~~ToolDefinitionId~~|~~ToolDefinitionId~~|~~ToolDefinitionId~~|
|~~UADM~~|~~vTool_Siemens_Simat_1812587140~~|~~ToolDefinition~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|~~Y~~|
||||Y<br>|~~**ToolDefinition**~~||~~**ToolDefinition**~~|~~UI Tool Definitions~~||
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolDefinitionSiteId~~<br>||||
|~~UADM~~<br>|~~vToolDefinition_Sie_1485280720~~<br>|~~Id~~<br>|~~Y~~<br>||~~ToolDefinitionKey~~<br>|~~ToolDefinitionKey~~<br>|~~ToolDefinitionKey~~<br>|~~ToolDefinitionKey~~<br>|
|~~UADM~~<br>|~~vToolDefinition_Sie_1485280720~~<br>|~~Name OR NId~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~|~~vToolDefinition_Sie_1485280720~~|~~Description~~|~~Y~~||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
||||Y<br>|~~**ToolDefinitionPropertyStaticValue**~~<br>|~~**ToolDefinitionPropertyStaticValue**~~<br>|~~**Value for a ToolDefinition attribute**~~|~~UI Tool Definitions, grid mode~~|~~"Revision", "Quantity"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolDefinitionPropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vToolDefinition_Sie_1485280720~~<br>|~~(Id  +'_' + 'ExpirationDate') OR (Id  +'_' +~~<br>'UsageCounterMax') OR (Id  +'_' +<br>'UsageDurationMax')  OR (Id  +'_' + 'Version')  OR (Id<br>+'_' + 'Consumable')<br>|~~Y~~<br>||~~ToolDefinitionPropertyStaticValueKey~~<br>|~~ToolDefinitionPropertyStaticValueKey~~<br>|~~ToolDefinitionPropertyStaticValueKey~~<br>|~~ToolDefinitionPropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolDefinitionId~~<br>|~~ToolDefinitionId~~<br>|~~ToolDefinitionId~~<br>|~~ToolDefinitionId~~<br>|
|~~UADM~~<br>|~~vToolDefinition_Sie_1485280720~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolPropertyId~~|~~ToolPropertyId~~|~~ToolPropertyId~~|~~ToolPropertyId~~|
|~~----~~<br>|~~----~~<br>|~~ "ExpirationDate" OR "UsageCounterMax" OR~~<br>"UsageDurationMax"  OR "Version"  OR<br>"Consumable"<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vToolDefinition_Sie_1485280720~~<br>|~~Version~~<br>|~~Y~~<br><br>||~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|~~StringValue~~<br>|
|~~UADM~~<br>|~~vToolDefinition_Sie_1485280720~~<br>|~~UsageCounterMax OR UsageDurationMax OR Consum~~<br>|~~Y~~<br>||~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|
|~~UADM~~|~~vToolDefinition_Sie_1485280720~~|~~ExpirationDate~~|~~Y~~||~~DatetimeValue~~|~~DatetimeValue~~|~~DatetimeValue~~|~~DatetimeValue~~|
||||Y<br>|~~**ToolProperty**~~||~~**Attribute of a Tool**~~|~~UI Tools, grid mode~~|~~"Revision", "Quantity"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolPropertySiteId~~<br>||||
|~~----~~|~~----~~|~~"ExpirationDate" OR~~<br>"UsageCounter" OR<br>"UsageCounterMax" OR<br>"UsageDuration" OR<br>"UsageDurationMax"OR<br>"Version" OR<br>"Consumable"|~~Y~~||~~ToolPropertyKey~~|~~ToolPropertyKey~~|~~ToolPropertyKey~~|~~ToolPropertyKey~~|


|----|----|"ExpirationDate" OR<br>"UsageCounter" OR<br>"UsageCounterMax" OR<br>"UsageDuration" OR<br>"UsageDurationMax"OR<br>"Version" OR<br>"Consumable"|Y|Col5|Name|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~"String" or "Numeric" OR "DateTime"~~<br>|~~Y~~<br>||~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|~~PropertyTypeId~~<br>|
|~~----~~|~~----~~|~~"n/a"~~|~~Y~~||~~UomId~~|~~UomId~~|~~UomId~~|~~UomId~~|
||||Y<br>|~~**ToolPropertyStaticValue**~~||~~**Value for a Tool attribute**~~|~~UI Tools, grid mode~~|~~"Revision", "Quantity"~~|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolPropertyStaticValueSiteId~~<br>||||
|~~UADM~~<br>|~~vTool_Siemens_Simat_1812587140~~<br>|~~(Id  +'_' + 'ExpirationDate') OR (Id  +'_' +~~<br>'UsageCounter')  OR (Id  +'_' + 'UsageCounterMax')<br>OR (Id  +'_' + 'UsageDuration') OR (Id  +'_' +<br>'UsageDurationMax')<br>|~~Y~~<br>||~~ToolPropertyStaticValueKey~~<br>|~~ToolPropertyStaticValueKey~~<br>|~~ToolPropertyStaticValueKey~~<br>|~~ToolPropertyStaticValueKey~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolId~~<br>|~~ToolId~~<br>|~~ToolId~~<br>|~~ToolId~~<br>|
|~~UADM~~<br>|~~vTool_Siemens_Simat_1812587140~~<br>|~~Id~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~----~~<br>|~~----~~<br>|~~<site_id>~~<br>|~~Y~~<br>||~~ToolPropertyId~~|~~ToolPropertyId~~|~~ToolPropertyId~~|~~ToolPropertyId~~|
|~~----~~<br>|~~----~~<br>|~~"ExpirationDate" OR "UsageCounter" OR~~<br>"UsageCounterMax" OR "UsageDuration" OR<br>"UsageDurationMax"<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|~~Y~~<br>|
|~~UADM~~<br>|~~vTool_Siemens_Simat_1812587140~~<br>|~~UsageCounter OR UsageCounterMax OR~~<br>UsageDuration OR UsageDurationMax<br>|~~Y~~<br>||~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|~~FloatValue~~<br>|
|~~UADM~~|~~vTool_Siemens_Simat_1812587140~~|~~ExpirationDate~~|~~Y~~||~~DatetimeValue~~|~~DatetimeValue~~|~~DatetimeValue~~|~~DatetimeValue~~|
||||Y<br>|~~**Uom**~~|||||
|~~UADM~~<br>|~~vUoM_Siemens_Simati_1027974907~~<br>|~~NId~~<br>|~~Y~~<br>||~~UomKey~~<br>||||
|~~UADM~~<br>|~~vUoM_Siemens_Simati_1027974907~~<br>|~~Name~~<br>|~~Y~~<br>||~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|~~Name~~<br>|
|~~UADM~~<br>|~~vUoM_Siemens_Simati_1027974907~~<br>|~~Description~~<br>|~~Y~~<br>||~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|~~Description~~<br>|
|~~----~~<br>|~~----~~<br>|~~1~~<br>|~~Y~~<br>||~~UomSystemId~~<br>|~~UomSystemId~~<br>|~~UomSystemId~~<br>|~~UomSystemId~~<br>|
|~~----~~|~~----~~|~~1~~|~~Y~~||~~UomCategoryId~~|~~UomCategoryId~~|~~UomCategoryId~~|~~UomCategoryId~~|


