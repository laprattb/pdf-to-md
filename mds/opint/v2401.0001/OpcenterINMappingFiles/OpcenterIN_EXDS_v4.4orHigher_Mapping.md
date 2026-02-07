|Opcenter EX DS Entities|Col2|Col3|Opcenter Intelligence Model Entities|Col5|Opcenter Execution Discrete – Public object model entities|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**DB Name**<br>|**Entity**<br>|**Attribute**|**Entity**|**Attributes**|**Entity exposed by POM**<br>|**UI**<br>|**Mapping info**|
||||**BillOfFeature**|||||
|----|----|<site_id>||BillOfFeatureSiteId||||
|UADM|vBillOfFeature_Sieme_362867332|NId||BillOfFeatureKey|BillOfFeatureKey|BillOfFeatureKey|BillOfFeatureKey|
|UADM|vBillOfFeature_Sieme_362867332|Name or NId||Name|Name|Name|Name|
|UADM|vBillOfFeature_Sieme_362867332|Description||Description|Description|Description|Description|
|UADM|vBillOfFeature_Sieme_362867332|Revision||Revision|Revision|Revision|Revision|
|UADM|vBillOfFeature_Sieme_362867332|IsCurrent||IsCurrent|IsCurrent|IsCurrent|IsCurrent|
||||**BillOfFeatureItem**|||||
|----|----|<site_id>||BillOfFeatureItemSiteId||||
|UADM|vBillOfFeatureItem_S_230590845|Id||BillOfFeatureItemKey|BillOfFeatureItemKey|BillOfFeatureItemKey|BillOfFeatureItemKey|
|----|----|<site_id>||BillOfFeatureId|BillOfFeatureId|BillOfFeatureId|BillOfFeatureId|
|UADM|vBillOfFeature_Sieme_362867332|Nid|Nid|Nid|Nid|Nid|Nid|
|UADM|vFeature_Siemens_Op_1528510985|Name or Nid||Name|Name|Name|Name|
|UADM|vFeature_Siemens_Op_1528510985|Description||Description|Description|Description|Description|
|UADM|vFeatureValue_Siemen_578621938|Name||Value|Value|Value|Value|
||||**BillOfMaterial**||**BoM**|UI Material Definitions >> select a Material Definition >> tab BoM||
|----|----|<site_id>||BillOfMaterialSiteId||||
|UADM|vBoM_Siemens_Simati_1391740687|Id||BillOfMaterialKey|BillOfMaterialKey|BillOfMaterialKey|BillOfMaterialKey|
|UADM|vBoM_Siemens_Simati_1391740687|Name or NId||Name|Name|Name|Name|
|UADM|vBoM_Siemens_Simati_1391740687|[Description]||Description|Description|Description|Description|
|UADM|vBoM_Siemens_Simati_1391740687|QuantityValue.Quantity||Quantity|Quantity|Quantity|Quantity|
|UADM|vBoM_Siemens_Simati_1391740687|UoMNId.Quantity||UomId|UomId|UomId|UomId|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vBoM_Siemens_Simati_1391740687|MaterialDefinition_Id|MaterialDefinition_Id|MaterialDefinition_Id|MaterialDefinition_Id|MaterialDefinition_Id|MaterialDefinition_Id|
||||**BillOfMaterialItem**||**BoMItem**|UI Material Definitions >> select a Material Definition >> tab BoM,<br>select a BoM >> tab BoM Items (flat view) and BoM Tree (hierarchy<br>view)||
|----|----|<site_id>||BillOfMaterialItemSiteId||||
|UADM|vBoMItem_Siemens_Sim_292660823|Id||BillOfMaterialItemKey|BillOfMaterialItemKey|BillOfMaterialItemKey|BillOfMaterialItemKey|
|----|----|<site_id>||BillOfMaterialId|BillOfMaterialId|BillOfMaterialId|BillOfMaterialId|
|UADM|vBoMItem_Siemens_Sim_292660823|BoM_Id|BoM_Id|BoM_Id|BoM_Id|BoM_Id|BoM_Id|
|UADM|vBoMItem_Siemens_Sim_292660823|NId||Name|Name|Name|Name|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|
|UADM|vBoMItem_Siemens_Sim_292660823|QuantityValue.Quantity||Quantity|Quantity|Quantity|Quantity|
|UADM|vBoMItem_Siemens_Sim_292660823|UoMNId.Quantity||UomId|UomId|UomId|UomId|
||||**Certification**||**Certification**|||
|----|----|<site_id>||CertificationSiteId||||
|UADM|vCertification_Sieme_165689816|NId||CertificationKey|CertificationKey|CertificationKey|CertificationKey|
|UADM|vCertification_Sieme_165689816|Name||Name|Name|Name|Name|
|UADM|vCertification_Sieme_165689816|Description||Description|Description|Description|Description|
||||**Defect**||**Defect**|UI Non-Conformances >> select a Non-Conformance >> tab Defects||
|----|----|<site_id>||DefectSiteId||||
|UADM|vDefect_Siemens_Sim_2091630976|Id||DefectKey|DefectKey|DefectKey|DefectKey|
|UADM|vFailure_Siemens_Op_1949421172<br>vDefect Siemens Sim 2091630976|Name or<br>Id||Name|Name|Name|Name|
|UADM|vFailure_Siemens_Op_1949421172|Description||Description|Description|Description|Description|
|----|----|<site_id>||NonConformanceId|NonConformanceId|NonConformanceId|NonConformanceId|
|UADM|vDefect_Siemens_Sim_2091630976|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|
||||**DefectClass**||**DefectType**|UI Defect Types||
|----|----|<site_id>||DefectClassSiteId||||
|UADM|vDefectType_Siemens_1029800126 ,vDefectGroup_Siemen_1773021159<br>,vFailure_Siemens_Op_1949421172|'DefectType_'+ Id ,GroupPath_' +Id,Nid||DefectClassKey|DefectClassKey|DefectClassKey|DefectClassKey|
|UADM|vDefectType_Siemens_1029800126 ,vDefectGroup_Siemen_1773021159<br>,vFailure_Siemens_Op_1949421172|Name or Nid||Name|Name|Name|Name|
|UADM|vDefectType_Siemens_1029800126 ,vDefectGroup_Siemen_1773021159<br>,vFailure_Siemens_Op_1949421172|Description||Description|Description|Description|Description|
||||**DefectDefectClass**||**Defect**|UI Non-Conformances >> select a Non-Conformance >> tab Defects|Defect-Defect type association|
|----|----|<site_id>||DefectDefectClassSiteId||||
|UADM|vDefect_Siemens_Sim_2091630976|Id + '_' + DefectType,<br>Id+ '_' +GroupPath,<br>Id+ ' ' +FailureNId||DefectDefectClassKey|DefectDefectClassKey|DefectDefectClassKey|DefectDefectClassKey|
|----|----|<site_id>||DefectId|DefectId|DefectId|DefectId|
|UADM|vDefect_Siemens_Sim_2091630976|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||DefectClassId|DefectClassId|DefectClassId|DefectClassId|
|UADM|vDefect_Siemens_Sim_2091630976,<br>vDefectGroup_Siemen_1773021159,<br>vDefect Siemens Sim 2091630976|DefectType_' + DefectType,<br>'GroupPath_' + Id,<br>FailureNId|DefectType_' + DefectType,<br>'GroupPath_' + Id,<br>FailureNId|DefectType_' + DefectType,<br>'GroupPath_' + Id,<br>FailureNId|DefectType_' + DefectType,<br>'GroupPath_' + Id,<br>FailureNId|DefectType_' + DefectType,<br>'GroupPath_' + Id,<br>FailureNId|DefectType_' + DefectType,<br>'GroupPath_' + Id,<br>FailureNId|
||||**Equipment**||**Equipment**|UI Equipment||
|----|----|<site_id>||EquipmentSiteId||||
|UADM|vEquipment_Siemens__2037264456|Nid||EquipmentKey|EquipmentKey|EquipmentKey|EquipmentKey|
|UADM|vEquipment_Siemens__2037264456|Name or NId||Name|Name|Name|Name|
|UADM|vEquipment_Siemens__2037264456|Description||Description|Description|Description|Description|
||||**EquipmentCertification**||**EquipmentCertification**|||
|----|----|<site_id>||EquipmentCertificationSiteId||||
|UADM|vEquipmentCertificat_156833050|Id||EquipmentCertificationKey|EquipmentCertificationKey|EquipmentCertificationKey|EquipmentCertificationKey|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vEquipmentCertificat_156833050|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|
|----|----|<site_id>||CertificationId|CertificationId|CertificationId|CertificationId|
|UADM|vCertification_Sieme_165689816|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||EquipmentClassId|EquipmentClassId|EquipmentClassId|EquipmentClassId|
|UADM|vEquipmentCertificat_156833050|EquipmentTypeNId|EquipmentTypeNId|EquipmentTypeNId|EquipmentTypeNId|EquipmentTypeNId|EquipmentTypeNId|
||||**EquipmentClass**||**MachineDefinition**|UI Equipment >> switch in tile mode: the Machine Definition is shown<br>in the Equipment tile||
|----|----|<site_id>||EquipmentClassSiteId||||
|UADM|vEquipmentLevel_Sie_1829947488|NId||EquipmentClassKey|EquipmentClassKey|EquipmentClassKey|EquipmentClassKey|
|UADM|vEquipmentLevel_Sie_1829947488|Name or NId||Name|Name|Name|Name|
|UADM|vEquipmentLevel_Sie_1829947488|Description||Description|Description|Description|Description|
||||**EquipmentEquipmentClass**||**Equipment**|UI Equipment >> switch in tile mode: the Machine Definition is shown<br>in the Equipment tile|Equipment-MachineDefinition association|
|----|----|<site_id>||EquipmentEquipmentClassSiteId||||


|UADM|vEquipment_Siemens__2037264456,<br>vEquipmentConfigura 2026297865|Id|Col4|EquipmentEquipmentClassKey|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vEquipment_Siemens__2037264456|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||EquipmentClassId|EquipmentClassId|EquipmentClassId|EquipmentClassId|
|UADM|vEquipment_Siemens__2037264456,<br>vEquipmentConfigura 2026297865|LevelNId or EquipmentTypeNId|LevelNId or EquipmentTypeNId|LevelNId or EquipmentTypeNId|LevelNId or EquipmentTypeNId|LevelNId or EquipmentTypeNId|LevelNId or EquipmentTypeNId|
||||**EquipmentHierarchy**||**Equipment**|UI Equipment, default tree view|Equipment-Equipment hierarchical association|
|----|----|<site_id>||EquipmentHierarchySiteId||||
|UADM|vEquipment_Siemens__2037264456|Id||EquipmentHierarchyKey|EquipmentHierarchyKey|EquipmentHierarchyKey|EquipmentHierarchyKey|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vEquipment_Siemens__2037264456|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||ParentEquipmentId|ParentEquipmentId|ParentEquipmentId|ParentEquipmentId|
|UADM|vEquipmentGraphNode__200408322|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|
||||**ExtendedPropertyType**|||||
|----|----|"Feature"||ExtendedPropertyTypeKey||||
|----|----|"Feature"||Name|Name|Name|Name|
|----|----|----||Description|Description|Description|Description|
||||**FinalProductFamily**|||||
|----|----|<site_id>||FinalProductFamilySiteId||||
|UADM|vProductConfiguratio_994723817|FinalProductFamilyNId + '_' + Revision||FinalProductFamilyKey|FinalProductFamilyKey|FinalProductFamilyKey|FinalProductFamilyKey|
|UADM|vProductConfiguratio_994723817|Name or FinalProductFamilyNId||Name|Name|Name|Name|
|UADM|vProductConfiguratio_994723817|Description||Description|Description|Description|Description|
|UADM|vProductConfiguratio_994723817|Revision||Revision|Revision|Revision|Revision|
|----|----|<site_id>||BillOfFeatureId|BillOfFeatureId|BillOfFeatureId|BillOfFeatureId|
|UADM|vProductConfiguratio_653021277|BillOfFeatureNId_L_1902833995|BillOfFeatureNId_L_1902833995|BillOfFeatureNId_L_1902833995|BillOfFeatureNId_L_1902833995|BillOfFeatureNId_L_1902833995|BillOfFeatureNId_L_1902833995|
|----|----|<site_id>||BillOfMaterialId|BillOfMaterialId|BillOfMaterialId|BillOfMaterialId|
|UADM|vBoM_Siemens_Simati_1391740687|Id|Id|Id|Id|Id|Id|
||||**FinalProductType**|||||
|----|----|<site_id>||FinalProductTypeSiteId||||
|UADM|vFinalProductType_S_1210354233|NId||FinalProductTypeKey|FinalProductTypeKey|FinalProductTypeKey|FinalProductTypeKey|
|UADM|vFinalProductType_S_1210354233|Name OR NId||Name|Name|Name|Name|
|UADM|vFinalProductType_S_1210354233|Description||Description|Description|Description|Description|
||||**FunctionalCode**|||||
|----|----|<site_id>||FunctionalCodeSiteId||||
|UADM|vDM_FunctionalCode_S_320778133|NId||FunctionalCodeKey|FunctionalCodeKey|FunctionalCodeKey|FunctionalCodeKey|
|UADM|vDM_FunctionalCode_S_320778133|Name OR NId||Name|Name|Name|Name|
|UADM|vDM_FunctionalCode_S_320778133|Description||Description|Description|Description|Description|
||||**Indicator**|||||
|----|----|<site_id>||IndicatorSiteId||||
|----|----|"NonConformance_Scrap" or "NonConformance_Rework"||IndicatorKey|IndicatorKey|IndicatorKey|IndicatorKey|
|----|----|NonConformance_Scrap or "NonConformance_Rework"||Name|Name|Name|Name|
|----|----|----||Description|Description|Description|Description|
|----|----|----||UomId|UomId|UomId|UomId|
||||**IndicatorClass**|||||
|----|----|<site_id>||IndicatorClassSiteId||||
|----|----|"Counter"||IndicatorClassKey|IndicatorClassKey|IndicatorClassKey|IndicatorClassKey|
|----|----|"Counter"||Name|Name|Name|Name|
|----|----|"Counter"||Description|Description|Description|Description|
||||**IndicatorIndicatorClass**|||||
|----|----|<site_id>||IndicatorIndicatorClassSiteId||||
|----|----|NonConformance_Scrap or "NonConformance_Rework"||IndicatorIndicatorClassKey|IndicatorIndicatorClassKey|IndicatorIndicatorClassKey|IndicatorIndicatorClassKey|
|----|----|<site_id>||IndicatorId|IndicatorId|IndicatorId|IndicatorId|
|----|----|NonConformance_Scrap or "NonConformance_Rework"|NonConformance_Scrap or "NonConformance_Rework"|NonConformance_Scrap or "NonConformance_Rework"|NonConformance_Scrap or "NonConformance_Rework"|NonConformance_Scrap or "NonConformance_Rework"|NonConformance_Scrap or "NonConformance_Rework"|
|----|----|<site_id>||IndicatorClassId|IndicatorClassId|IndicatorClassId|IndicatorClassId|
|----|----|"Counter"|"Counter"|"Counter"|"Counter"|"Counter"|"Counter"|
||||**IndicatorValue**||**NonConformance**|UI Non-Conformances|Only NC with Type = 'QUALITY' and Status IN ('SCRAP','REWORK') and Context IN<br>('Machine','WorkOrderOperation') are taken and contextualized with the relative<br>equipment|
|----|----|<site_id>||IndicatorValueSiteId||||
|UADM|vNonConformance_Sieme_73759778|Id||IndicatorValueKey|IndicatorValueKey|IndicatorValueKey|IndicatorValueKey|
|----|----|<site_id>||IndicatorId|IndicatorId|IndicatorId|IndicatorId|
||----|"NonConformance_Scrap" or "NonConformance_Rework"||||||
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vNonConformance_Sieme_73759778<br>vActualUsedMachine<br>2012847191|Equipment or<br>Machine||||||
|UADM|vNonConformance_Sieme_73759778|StartDate||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vNonConformance_Sieme_73759778|StartDate||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|----|----|----||Duration|Duration|Duration|Duration|
|UADM|vNonConformance_Sieme_73759778|Quantity||Value|Value|Value|Value|
||||**Labor**||**PublicUser (this entity is exposed in the**<br>**engineering service layer by UAF)**|UI Users||
|----|----|<site_id>||LaborSiteId||||
|UADM|vUserNonProductiveAc_383652110,vWorkOrderHistory_Si_518515069|User,UserId||LaborKey|LaborKey|LaborKey|LaborKey|
|UADM|vUserNonProductiveAc_383652110,vWorkOrderHistory_Si_518515069|User,UserId||Name|Name|Name|Name|
||||**LaborCertification**||**LaborCertification**|||
|----|----|<site_id>||LaborCertificationSiteId||||
||vUserCertificationA_1661281456|Id||LaborCertificationKey|LaborCertificationKey|LaborCertificationKey|LaborCertificationKey|
|----|----|<site_id>||LaborId|LaborId|LaborId|LaborId|
|UADM|vUserCertificationA_1661281456|User|User|User|User|User|User|
|----|----|<site_id>||CertificationId|CertificationId|CertificationId|CertificationId|
|UADM|vCertification_Sieme_165689816|NId|NId|NId|NId|NId|NId|
|UADM|vUserCertificationA_1661281456|ExpiryDate||ExpirationDate|ExpirationDate|ExpirationDate|ExpirationDate|
||||**LaborTimeCategory**||**WorkOrderHistoryAction**|UI Work Orders >> select a WorkOrder >> button As Built >> tab<br>Activity History<br>You can also see them on UI Genealogy, in the tree representation,<br>under each WorkOrderOperation node||
|----|----|<site_id>||LaborTimeCategorySiteId||||
|UADM|vNonProductiveActivi_678536801|Id||LaborTimeCategoryKey|LaborTimeCategoryKey|LaborTimeCategoryKey|LaborTimeCategoryKey|
|UADM|vNonProductiveActivi_678536801|NId||Name|Name|Name|Name|
|UADM|vNonProductiveActivi_678536801|Description||Description|Description|Description|Description|
||||**LaborTimeModel**||**WorkOrderHistory + WorkOrderHistoryAction**|UI Users >> select a user >> tab Log||
|----|----|<site_id>||LaborTimeModelSiteId||||
|UADM|vUserNonProductiveAc_383652110|Id||LaborTimeModelKey|LaborTimeModelKey|LaborTimeModelKey|LaborTimeModelKey|
|----|----|<site_id>||LaborTimeCategorySiteId|LaborTimeCategorySiteId|LaborTimeCategorySiteId|LaborTimeCategorySiteId|
|UADM|vUserNonProductiveAc_383652110|NPAId||LaborTimeCategoryKey|LaborTimeCategoryKey|LaborTimeCategoryKey|LaborTimeCategoryKey|


|----|----|<site_id>|Col4|LaborSiteId|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|User||LaborKey|LaborKey|LaborKey|LaborKey|
|UADM|vUserNonProductiveAc_383652110|StartDate-EndDate||Duration|Duration|Duration|Duration|
|UADM|vUserNonProductiveAc_383652110|StartDate||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vUserNonProductiveAc_383652110|EndDate||EndDate|EndDate|EndDate|EndDate|
||||**MaterialClass**||**MaterialClass**|UI Material Definitions >> in the default tile view the MaterialClass is<br>shown|UI Material Definitions >> in the default tile view the MaterialClass is shown|
|----|----|<site_id>||MaterialClassSiteId||||
|UADM|vMaterialGroup_Siem_2035655829,vDM_FunctionalCode_S_320778133|Id or Nid||MaterialClassKey|MaterialClassKey|MaterialClassKey|MaterialClassKey|
|UADM|vMaterialGroup_Siem_2035655829,vDM_FunctionalCode_S_320778133|Name or NId||Name|Name|Name|Name|
|UADM|vMaterialGroup_Siem_2035655829,vDM_FunctionalCode_S_320778133|Description||Description|Description|Description|Description|
||||**MaterialDefinition**||**MaterialDefinition**|UI Material Definitions|UI Material Definitions|
|----|----|<site_id>||MaterialDefinitionSiteId||||
|UADM|vMaterial_Siemens_Si_170253665|Id||MaterialDefinitionKey|MaterialDefinitionKey|MaterialDefinitionKey|MaterialDefinitionKey|
|UADM|vMaterial_Siemens_Si_170253665|Name or NId||Name|Name|Name|Name|
|UADM|vMaterial_Siemens_Si_170253665|Description||Description|Description|Description|Description|
|----|----|<site_id>||FunctionalCodeId|FunctionalCodeId|FunctionalCodeId|FunctionalCodeId|
|UADM|vDM_Material_Siemens_463872986|FunctionalCodeNId|FunctionalCodeNId|FunctionalCodeNId|FunctionalCodeNId|FunctionalCodeNId|FunctionalCodeNId|
|UADM|vMaterial_Siemens_Si_170253665|NId||Identifier|Identifier|Identifier|Identifier|
||||**MaterialDefinitionMaterialClass**||**MaterialDefinition**|UI Material Definitions|MaterialDefinition-MaterialClass association|
|----|----|<site_id>||MaterialDefinitionMaterialClassSiteId||||
|UADM|vDM_Material_Siemens_463872986|Id or 'FunctionalCode_' + Id||MaterialDefinitionMaterialClassKey|MaterialDefinitionMaterialClassKey|MaterialDefinitionMaterialClassKey|MaterialDefinitionMaterialClassKey|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||MaterialClassId|MaterialClassId|MaterialClassId|MaterialClassId|
|UADM|vDM_Material_Siemens_463872986|MaterialClass_Id or FunctionalCodeNId|MaterialClass_Id or FunctionalCodeNId|MaterialClass_Id or FunctionalCodeNId|MaterialClass_Id or FunctionalCodeNId|MaterialClass_Id or FunctionalCodeNId|MaterialClass_Id or FunctionalCodeNId|
||||**MaterialDefinitionPropertyStaticValue**||**Value of MaterialDefinition attribute**|UI Material Definitions, grid mode|"Revision", "SerialNumberProfile", "FirstArticleInspection")|
|----|----|<site_id>||MaterialDefinitionPropertyStaticValueSiteId||||
|UADM|vMaterial_Siemens_Si_170253665|(Id +'_' +'Revision' or Id +'_' +'IsCurrent') or<br>(Id +'_' +'SerialNumberProfile' or Id +'_'<br>+'FirstArticleInspection' or Id +'_' +'WeightUom' or Id +'_'<br>+'VolumeUom' or Id +'_' +'WeightQuantity' or Id +'_'<br>+'VolumeQuantity' or<br>Id +'_' +'Code')||MaterialDefinitionPropertyStaticValueKey|MaterialDefinitionPropertyStaticValueKey|MaterialDefinitionPropertyStaticValueKey|MaterialDefinitionPropertyStaticValueKey|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||MaterialPropertyId|MaterialPropertyId|MaterialPropertyId|MaterialPropertyId|
|----|----|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code"|
|UADM|vMaterial_Siemens_Si_170253665 or<br>vDM_Material_Siemens_463872986|(Revision or IsCurrent) or<br>(SerialNumberProfile or FirstArticleInspection or<br>UoMNId.Weight or UoMNId.Volume||StringValue|StringValue|StringValue|StringValue|
|UADM|vDM_Material_Siemens_463872986|QuantityValue.Weight or QuantityValue.Volume||FloatValue|FloatValue|FloatValue|FloatValue|
||||**MaterialExtendedProperty**|||||
|----|----|<site_id>||MaterialExtendedPropertySiteId||||
|UADM|vFeature_Siemens_Op_1528510985|NId||MaterialExtendedPropertyKey|MaterialExtendedPropertyKey|MaterialExtendedPropertyKey|MaterialExtendedPropertyKey|
|UADM|vFeature_Siemens_Op_1528510985|Name or NId||Name|Name|Name|Name|
|UADM|vFeature_Siemens_Op_1528510985|Description||Description|Description|Description|Description|
|UADM|vFeature_Siemens_Op_1528510985|IsOption||IsOption|IsOption|IsOption|IsOption|
|----|----|"Feature"||ExtendedPropertyTypeId|ExtendedPropertyTypeId|ExtendedPropertyTypeId|ExtendedPropertyTypeId|
||||**MaterialLot**||**MaterialItem**|UI Material Items||
|----|----|<site_id>||MaterialLotSiteId||||
|UADM|vMaterialTrackingUni_494706508|NId||MaterialLotKey|MaterialLotKey|MaterialLotKey|MaterialLotKey|
|UADM|vMaterialTrackingUni_494706508|Name||Name|Name|Name|Name|
|UADM|vMaterialTrackingUni_494706508|Description||Description|Description|Description|Description|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|
|UADM|vMaterialTrackingUni_494706508|QuantityValue.Quantity||Quantity|Quantity|Quantity|Quantity|
|UADM|vMaterialTrackingUni_494706508|UoMNId.Quantity||UomId|UomId|UomId|UomId|
||||**MaterialLotExtendedPropertyStaticValue**|||||
|----|----|<site_id>||MaterialLotExtendedPropertyStaticValueSiteId||||
|UADM|vFeatureItem_Siemen_1080518525|Id||MaterialLotExtendedPropertyStaticValueKey|MaterialLotExtendedPropertyStaticValueKey|MaterialLotExtendedPropertyStaticValueKey|MaterialLotExtendedPropertyStaticValueKey|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vFrozenStructureCont_464866249|MaterialTrackingUnitNId||||||
|----|----|<site_id>||MaterialExtendedPropertyId|MaterialExtendedPropertyId|MaterialExtendedPropertyId|MaterialExtendedPropertyId|
|UADM|vFeatureItem_Siemen_1080518525|FeatureNId||||||
|UADM|vFeatureItem_Siemen_1080518525|FeatureValueNId||Value|Value|Value|Value|
|UADM|vFeatureItem_Siemen_1080518525|FeatureValueName||ValueName|ValueName|ValueName|ValueName|
|UADM|vFeatureItem_Siemen_1080518525|FeatureValueDescription||ValueDescription|ValueDescription|ValueDescription|ValueDescription|
||||**MaterialLotHierarchy**||**MaterialItemHistory +**<br>**MaterialItemHistoryAction**|UI Material Items >> Material Item Details >> Parent Batch property<br>and tab History<br>UI Raw Material Genealogy||
|----|----|<site_id>||MaterialLotHierarchySiteId||||
|UADM|vMaterialTrackingUni_494706508|Id||MaterialLotHierarchyKey|MaterialLotHierarchyKey|MaterialLotHierarchyKey|MaterialLotHierarchyKey|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vMaterialTrackingUni_494706508|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||ParentMaterialLotId|ParentMaterialLotId|ParentMaterialLotId|ParentMaterialLotId|
|UADM|vMaterialTrackingUni_494706508|NId|NId|NId|NId|NId|NId|
||||**MaterialLotMaterialDefinition**|||||
|----|----|<site_id>||MaterialLotMaterialDefinitionSiteId||||
|UADM|vMaterialItem_Sieme_2082583269|Id||MaterialLotMaterialDefinitionKey|MaterialLotMaterialDefinitionKey|MaterialLotMaterialDefinitionKey|MaterialLotMaterialDefinitionKey|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vFrozenStructureCont_464866249|MaterialTrackingUnitNId||||||
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id||||||
|UADM|vMaterialItem_Sieme_2082583269|ConsumedQuantityValue||ConsumedQuantity|ConsumedQuantity|ConsumedQuantity|ConsumedQuantity|
|UADM|vMaterialItem_Sieme_2082583269|QuantityValue.ItemQuantity||Quantity|Quantity|Quantity|Quantity|


|UADM|vMaterialItem_Sieme_2082583269|UoMNId.ItemQuantity|Col4|UomId|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||**MaterialLotOperation**||**MaterialItemHistory +**<br>**MaterialItemHistoryAction**|UI Material Items >> select a Material Item >> tab History||
|----|----|<site_id>||MaterialLotOperationSiteId||||
|UADM|vDM_MaterialTracking_215326293|Id||MaterialLotOperationKey|MaterialLotOperationKey|MaterialLotOperationKey|MaterialLotOperationKey|
|UADM|vDM_MaterialTracking_215326293|Date||OperationDateTime|OperationDateTime|OperationDateTime|OperationDateTime|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vDM_MaterialTrackin_1551871669|Nid|Nid|Nid|Nid|Nid|Nid|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vDM_Material_Siemens_463872986|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|
|UADM|vDM_MaterialTracking_215326293|OldQuantity||ActualQuantity|ActualQuantity|ActualQuantity|ActualQuantity|
|UADM|vDM_MaterialTracking_215326293|Quantity||OperationQuantity|OperationQuantity|OperationQuantity|OperationQuantity|
|UADM|dbo.vMaterialTrackingUni_494706508|UoMNId.Quantity||UomId|UomId|UomId|UomId|
|----|----|<site_id>||SourceMaterialDefinitionId|SourceMaterialDefinitionId|SourceMaterialDefinitionId|SourceMaterialDefinitionId|
|UADM|vDM_Material_Siemens_463872986|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|
|----|----|<site_id>||SourceMaterialLotId|SourceMaterialLotId|SourceMaterialLotId|SourceMaterialLotId|
|UADM|vDM_MaterialTrackin_1551871669|NId|NId|NId|NId|NId|NId|
|UADM|vMaterialTrackingUni_494706508|UoMNId.Quantity||SourceUomId|SourceUomId|SourceUomId|SourceUomId|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vMaterialTrackingUni_494706508|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|
|----|----|<site_id>||SourceEquipmentId|SourceEquipmentId|SourceEquipmentId|SourceEquipmentId|
|UADM|vMaterialTrackingUni_494706508|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|
||||**MaterialLotPropertyStaticValue**||**Value of MaterialItem attribute**|UI Material Items||
|----|----|<site_id>||MaterialLotPropertyStaticValueSiteId||||
|UADM|vMaterialTrackingUni_494706508<br>vMaterialTrackingUni 298595082|Id +'_Code' OR<br>Id +' LineSequence'||MaterialLotPropertyStaticValueKey|MaterialLotPropertyStaticValueKey|MaterialLotPropertyStaticValueKey|MaterialLotPropertyStaticValueKey|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vMaterialTrackingUni_494706508|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||MaterialPropertyId|MaterialPropertyId|MaterialPropertyId|MaterialPropertyId|
|----|----|"Code" or "LineSequence"|"Code" or "LineSequence"|"Code" or "LineSequence"|"Code" or "LineSequence"|"Code" or "LineSequence"|"Code" or "LineSequence"|
|UADM|vMaterialTrackingUni_494706508<br>vMaterialTrackingUni 298595082|Code OR<br>LineSequence Sequenc 24591405||StringValue|StringValue|StringValue|StringValue|
||||**MaterialProperty**||**Attribute/Property of a MaterialDefinition**|UI Material Definitions, grid mode||
|----|----|<site_id>||MaterialPropertySiteId||||
|----|----|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code" or<br>"LineSequence"||MaterialPropertyKey|MaterialPropertyKey|MaterialPropertyKey|MaterialPropertyKey|
|----|----|"Revision" or<br>"IsCurrent"or<br>"SerialNumberProfile" or<br>"FirstArticleInspection" or<br>"WeightUom" or<br>"VolumeUom" or<br>"WeightQuantity" or<br>"VolumeQuantity" or<br>"Code" or<br>"LineSequence"||Name|Name|Name|Name|
|----|----|"String" or "Numeric"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
||||**Milestone**||**Milestone**|||
|----|----|<site_id>||MilestoneSiteId||||
|UADM|vPFCMilestone_Sieme_1916168515|NId||MilestoneKey|MilestoneKey|MilestoneKey|MilestoneKey|
|UADM|vPFCMilestone_Sieme_1916168515|Name or NId||Name|Name|Name|Name|
|UADM|vPFCMilestone_Sieme_1916168515|Description||Description|Description|Description|Description|
|UADM|vPFCMilestone_Sieme_1916168515|SequenceNumber||Sequence|Sequence|Sequence|Sequence|
|----|----|<site_id>||MilestoneDiagramd|MilestoneDiagramd|MilestoneDiagramd|MilestoneDiagramd|
|UADM|vPFCDiagram_Siemens_1121636391|NId||||||
||||**MilestoneDiagram**|||||
|----|----|<site_id>||MilestoneDiagramSiteId||||
|UADM|vPFCDiagram_Siemens_1121636391|NId||MilestoneDiagramKey|MilestoneDiagramKey|MilestoneDiagramKey|MilestoneDiagramKey|
|UADM|vPFCDiagram_Siemens_1121636391|Name or NId||Name|Name|Name|Name|
|UADM|vPFCDiagram_Siemens_1121636391|Description||Description|Description|Description|Description|
|UADM|vPFCDiagram_Siemens_1121636391|Revision||Revision|Revision|Revision|Revision|
|----|----|<site_id>||FinalProductTypeId|FinalProductTypeId|FinalProductTypeId|FinalProductTypeId|
|UADM|vPFCDiagram_Siemens_1121636391|FinalProductTypeNId||||||
||||**MilestoneHistory**|||||
|----|----|<site_id>||MilestoneHistorySiteId||||
|UADM|vPFCMilestoneReached_392872107|Id||MilestoneHistoryKey|MilestoneHistoryKey|MilestoneHistoryKey|MilestoneHistoryKey|
|UADM|vPFCMilestoneReached_392872107|TimeStamp||EventDateTime|EventDateTime|EventDateTime|EventDateTime|
|----|----|<site_id>||MilestoneId|MilestoneId|MilestoneId|MilestoneId|
|UADM|vPFCMilestoneReached_392872107|MilestoneNId||||||
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vPFCMilestoneReached_392872107|WorkplaceNId||||||
|----|----|<site_id>||OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|
|UADM|vPFCMaterialInstance_177437800|ERPOrderNId||||||
|----|----|<site_id>||FinalProductTypeId|FinalProductTypeId|FinalProductTypeId|FinalProductTypeId|
|UADM|vPFCMaterialInstance_177437800|FinalProductTypeNId||||||
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vPFCMaterialInstance_177437800|MaterialInstanceNId||||||
||||**NonConformance**||**NonConformance**|UI Non-Conformances||
|----|----|<site_id>||NonConformanceSiteId||||
|UADM|vNonConformance_Sieme_73759778|Id||NonConformanceKey|NonConformanceKey|NonConformanceKey|NonConformanceKey|
|UADM|vNonConformance_Sieme_73759778|NId||Name|Name|Name|Name|
|----|----|<site_id>||NonConformanceStatusId|NonConformanceStatusId|NonConformanceStatusId|NonConformanceStatusId|
|UADM|vNonConformanceStat_1246268624|Id|Id|Id|Id|Id|Id|
|UADM|vNonConformance_Sieme_73759778|StartDate||StartDateTime|StartDateTime|StartDateTime|StartDateTime|


|UADM|vNonConformance_Sieme_73759778|EndDate|Col4|EndDateTime|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|UADM|vNonConformance_Sieme_73759778|(StartDate) - (EndDate)||Duration|Duration|Duration|Duration|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vNonConformance_Sieme_73759778|Equipment|Equipment|Equipment|Equipment|Equipment|Equipment|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|----|----|----|----|----|----|----|----|
|----|----|<site_id>||ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|
|----|----|----|----|----|----|----|----|
|----|----|<site_id>||OperationExecutionId|OperationExecutionId|OperationExecutionId|OperationExecutionId|
|UADM|vNonConformance_Sieme_73759778|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vNonConformance_Sieme_73759778|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|----|----|----|----|----|----|----|----|
|UADM|vNonConformance_Sieme_73759778|Notes||Comment|Comment|Comment|Comment|
|----|----|----||InspectedQuantity|InspectedQuantity|InspectedQuantity|InspectedQuantity|
|UADM|vNonConformance_Sieme_73759778|Quantity||NonConformantQuantity|NonConformantQuantity|NonConformantQuantity|NonConformantQuantity|
||||**NonConformanceClass**||**NonConformanceSeverity**|UI Non-Conformances >> tab Details||
|----|----|<site_id>||NonConformanceClassSiteId||||
|UADM|vNonConformance_Sieme_73759778|("Severity_" + Severity) OR<br>("Type "+ Type)||NonConformanceClassKey|NonConformanceClassKey|NonConformanceClassKey|NonConformanceClassKey|
|UADM|vNonConformance_Sieme_73759778|Severity OR Type||Name|Name|Name|Name|
||||**NonConformanceEquipmentSpecification**||**NonConformanceItem**|UI Non-Conformances >> tab Machines|Equipment where the Non-Conformance has been opened on|
|---|----|<site_id>||NonConformanceEquipmentSpecificationSiteId||||
|UADM|vNonConformanceItem_1873176518|Id||NonConformanceEquipmentSpecificationKey|NonConformanceEquipmentSpecificationKey|NonConformanceEquipmentSpecificationKey|NonConformanceEquipmentSpecificationKey|
|----|----|<site_id>||NonConformanceId|NonConformanceId|NonConformanceId|NonConformanceId|
|UADM|vNonConformanceItem_1873176518|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vNonConformanceItem_1873176518|Equipment|Equipment|Equipment|Equipment|Equipment|Equipment|
|----|----|1||Quantity|Quantity|Quantity|Quantity|
||||**NonConformanceHistory**|||||
|---|----|<site_id>||NonConformanceHistorySiteId||||
|UADM|vNonConformanceHist_1332403411|Id||NonConformanceHistoryKey|NonConformanceHistoryKey|NonConformanceHistoryKey|NonConformanceHistoryKey|
|---|----|<site_id>||NonConformanceId|NonConformanceId|NonConformanceId|NonConformanceId|
|UADM|vNonConformanceHist_1332403411|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|
|UADM|vNonConformanceHist_1332403411|Date||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vNonConformanceHist_1332403411|Date||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|UADM|vNonConformanceHist_1332403411|DATEDIFF(SECOND, Date, Date)||Duration|Duration|Duration|Duration|
|---|----|<site_id>||NonConformanceStatusId|NonConformanceStatusId|NonConformanceStatusId|NonConformanceStatusId|
|UADM|vNonConformanceStat_1246268624|Id|Id|Id|Id|Id|Id|
|---|----|<site_id>||LaborId|LaborId|LaborId|LaborId|
|UADM|vNonConformanceHist_1332403411|UserId|UserId|UserId|UserId|UserId|UserId|
|---|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vNonConformanceHist_1332403411|Equipment|Equipment|Equipment|Equipment|Equipment|Equipment|
||||**NonConformanceNonConformanceClass**||**NonConformance**|UI Non-Conformances|NonConformance-NonConformanceSeverity association|
|----|----|<site_id>||NonConformanceNonConformanceClassSiteId||||
|UADM|vNonConformance_Sieme_73759778|(Id + '_' + 'Severity_' + Severity ) OR (Id  + '_' + ('Type_' +<br>[Type]))||NonConformanceNonConformanceClassKey|NonConformanceNonConformanceClassKey|NonConformanceNonConformanceClassKey|NonConformanceNonConformanceClassKey|
|----|----|<site_id>||NonConformanceClassId|NonConformanceClassId|NonConformanceClassId|NonConformanceClassId|
|UADM|vNonConformance_Sieme_73759778|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||NonConformanceId|NonConformanceId|NonConformanceId|NonConformanceId|
|UADM|vNonConformance_Sieme_73759778|('Severity_' + Severity) OR ('Type_' + [Type])|('Severity_' + Severity) OR ('Type_' + [Type])|('Severity_' + Severity) OR ('Type_' + [Type])|('Severity_' + Severity) OR ('Type_' + [Type])|('Severity_' + Severity) OR ('Type_' + [Type])|('Severity_' + Severity) OR ('Type_' + [Type])|
||||**NonConformanceMaterialLotSpecification**||**NonConformanceItem**|UI Non-Conformances >> tab Material Items|Material item where the Non-Conformance has been opened on|
|----|----|<site_id>||NonConformanceMaterialLotSpecificationSiteId||||
|UADM|vNonConformanceItem_1873176518|Id||NonConformanceMaterialLotSpecificationKey|NonConformanceMaterialLotSpecificationKey|NonConformanceMaterialLotSpecificationKey|NonConformanceMaterialLotSpecificationKey|
|----|----|<site_id>||NonConformanceId|NonConformanceId|NonConformanceId|NonConformanceId|
|UADM|vNonConformanceItem_1873176518|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vMaterialTrackingUni_494706508|NId|NId|NId|NId|NId|NId|
|----|----|1||Quantity|Quantity|Quantity|Quantity|
||||**NonConformanceProperty**||**Attribute of a NonConformance**|UI Non-Conformances|"SerialNumber"|
|----|----|<site_id>||NonConformancePropertySiteId||||
|----|----|"SerialNumber"||NonConformancePropertyKey|NonConformancePropertyKey|NonConformancePropertyKey|NonConformancePropertyKey|
|----|----|"SerialNumber"||Name|Name|Name|Name|
|----|----|"String"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
||||**NonConformancePropertyStaticValue**||**Value for a NonConformance attribute**|UI Non-Conformances|"SerialNumber"|
|----|----|<site_id>||NonConformancePropertyStaticValueSiteId||||
|----|----|----||NonConformancePropertyStaticValueKey|NonConformancePropertyStaticValueKey|NonConformancePropertyStaticValueKey|NonConformancePropertyStaticValueKey|
|----|----|<site_id>||NonConformanceId|NonConformanceId|NonConformanceId|NonConformanceId|
|----|----|----|----|----|----|----|----|
|----|----|<site_id>||NonConformancePropertyId|NonConformancePropertyId|NonConformancePropertyId|NonConformancePropertyId|
|----|----|----|----|----|----|----|----|
|----|----|----||StringValue|StringValue|StringValue|StringValue|
||||**NonConformanceStatus**||**NonConformanceStatus**|UI Non-Conformance Lifecycles||
|----|----|<site_id>||NonConformanceStatusSiteId||||
|UADM|vNonConformanceStat_1246268624|Id||NonConformanceStatusKey|NonConformanceStatusKey|NonConformanceStatusKey|NonConformanceStatusKey|
|UADM|vNonConformanceStat_1246268624|Name or NId||Name|Name|Name|Name|
|UADM|vNonConformanceStat_1246268624|Description||Description|Description|Description|Description|
||||**NonConformanceToolSpecification**||**NonConformanceItem**|UI Non-Conformances >> tab Tools|Tool item where the Non-Conformance has been opened on|
|----|----|<site_id>||NonConformanceToolSpecificationSiteId||||
|UADM|vNonConformanceItem_1873176518|Id||NonConformanceToolSpecificationKey|NonConformanceToolSpecificationKey|NonConformanceToolSpecificationKey|NonConformanceToolSpecificationKey|
|----|----|<site_id>||NonConformanceId|NonConformanceId|NonConformanceId|NonConformanceId|
|UADM|vNonConformanceItem_1873176518|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|NonConformance_Id|
|----|----|<site_id>||ToolId|ToolId|ToolId|ToolId|
|UADM|vNonConformanceItem_1873176518|Tool_id|Tool_id|Tool_id|Tool_id|Tool_id|Tool_id|
|----|----|1||Quantity|Quantity|Quantity|Quantity|
||||**OperationDefinition**||**Operation/Step**|UI Operation Catalog/ UI Step Catalog||
|----|----|<site_id>||OperationDefinitionSiteId||||
|UADM|vOperation_Siemens_S_700803909 or<br>vStep Siemens Simati 938557012|Id||OperationDefinitionKey|OperationDefinitionKey|OperationDefinitionKey|OperationDefinitionKey|
|UADM|vOperation_Siemens_S_700803909 or<br>vStep Siemens Simati 938557012|Name OR Nid||Name|Name|Name|Name|
|UADM|vOperation_Siemens_S_700803909 or<br>vStep Siemens Simati 938557012|Description||Description|Description|Description|Description|
|----|----|<site_id>||OperationDefinitionClassSiteId|OperationDefinitionClassSiteId|OperationDefinitionClassSiteId|OperationDefinitionClassSiteId|
|----|----|"Operation" or<br>"Step"||OperationDefinitionClassKey|OperationDefinitionClassKey|OperationDefinitionClassKey|OperationDefinitionClassKey|


|----|----|"Operation" or<br>"Step"|Col4|Name|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||**OperationDefinitionEquipmentSpecification**|||||
|----|----|<site_id>||OperationDefinitionEquipmentSpecificationSiteId||||
|UADM|vEquipmentSpecifica_1193585561|Id||OperationDefinitionEquipmentSpecificationKey|OperationDefinitionEquipmentSpecificationKey|OperationDefinitionEquipmentSpecificationKey|OperationDefinitionEquipmentSpecificationKey|
|----|----|<site_id>||OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|
|UADM|vOperation_Siemens_S_700803909|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vEquipmentSpecifica_1193585561|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|
||||**OperationDefinitionMaterialDefinitionSpecificationIn**|||||
|----|----|<site_id>||OperationDefinitionMaterialDefinitionSpecificationInSiteId||||
|UADM|vMaterialSpecificat_1918342704|Id||OperationDefinitionMaterialDefinitionSpecificationInKey|OperationDefinitionMaterialDefinitionSpecificationInKey|OperationDefinitionMaterialDefinitionSpecificationInKey|OperationDefinitionMaterialDefinitionSpecificationInKey|
|----|----|<site_id>||OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|
|UADM|vOperation_Siemens_S_700803909|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|
|UADM|vMaterialSpecificat_1918342704|QuantityValue.Quantity||Quantity|Quantity|Quantity|Quantity|
|UADM|vMaterialSpecificat_1918342704|UoMNId.Quantity||UomId|UomId|UomId|UomId|
||||**OperationDefinitionOperationDefinitionClass**|||||
|----|----|<site_id>||OperationDefinitionOperationDefinitionClassSiteId||||
|UADM|vOperation_Siemens_S_700803909 or vStep_Siemens_Simati_938557012|(Id + '_Operation) or (Id + '_Step')||OperationDefinitionOperationDefinitionClassKey|OperationDefinitionOperationDefinitionClassKey|OperationDefinitionOperationDefinitionClassKey|OperationDefinitionOperationDefinitionClassKey|
|----|----|<site_id>||OperationDefinitionClassId|OperationDefinitionClassId|OperationDefinitionClassId|OperationDefinitionClassId|
|----|----|"Operation" or "Step"||||||
|----|----|<site_id>||OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|
|UADM|vOperation_Siemens_S_700803909 or vStep_Siemens_Simati_938557012|Id||||||
||||**OperationDefinitionProperty**||** Attribute of an Operation**|UI Operation Catalog, grid mode|"EstimatedDuration"|
|----|----|<site_id>||OperationDefinitionPropertySiteId||||
|----|----|"EstimatedDuration" or "Revision"||OperationDefinitionPropertyKey|OperationDefinitionPropertyKey|OperationDefinitionPropertyKey|OperationDefinitionPropertyKey|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
|----|----|"Numeric" or "String"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
|----|----|"EstimatedDuration" or "Revision"||Name|Name|Name|Name|
||||**OperationDefinitionPropertyStaticValue**||**Value for an Operation/Step attribute**|UI Operation Catalog/ UI Step Catalog, grid mode|"EstimatedDuration"|
|----|----|<site_id>||OperationDefinitionPropertyStaticValueSiteId||||
|UADM|vOperation_Siemens_S_700803909 or<br>vStep Siemens Simati 938557012|(Id+'_' +'EstimatedDuration') or (Id+'_' +'Revision')||OperationDefinitionPropertyStaticValueKey|OperationDefinitionPropertyStaticValueKey|OperationDefinitionPropertyStaticValueKey|OperationDefinitionPropertyStaticValueKey|
|----|----|<site_id>||OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|
|UADM|vOperation_Siemens_S_700803909 or<br>vStep Siemens Simati 938557012|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||OperationDefinitionPropertyId|OperationDefinitionPropertyId|OperationDefinitionPropertyId|OperationDefinitionPropertyId|
|----|----|"EstimatedDuration" or "Revision"|"EstimatedDuration" or "Revision"|"EstimatedDuration" or "Revision"|"EstimatedDuration" or "Revision"|"EstimatedDuration" or "Revision"|"EstimatedDuration" or "Revision"|
|UADM|vOperation_Siemens_S_700803909 or<br>vStep Siemens Simati 938557012|EstimatedDuration||FloatValue|FloatValue|FloatValue|FloatValue|
|UADM|vOperation_Siemens_S_700803909 or<br>vStep Siemens Simati 938557012|Revision||StringValue|StringValue|StringValue|StringValue|
||||**OperationExecution**||**WorkOrder**|UI Work Orders||
|----|----|<site_id>||OperationExecutionSiteId||||
|UADM|vWorkOrder_Siemens_S_749389132|NId||OperationExecutionKey|OperationExecutionKey|OperationExecutionKey|OperationExecutionKey|
|UADM|vWorkOrder_Siemens_S_749389132|Name||Name|Name|Name|Name|
|UADM|vWorkOrder_Siemens_S_749389132|Notes||Description|Description|Description|Description|
|----|----|<site_id>||OperationExecutionStatusId|OperationExecutionStatusId|OperationExecutionStatusId|OperationExecutionStatusId|
|UADM|vWorkOrder_Siemens_S_749389132|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vWorkOrder_Siemens_S_749389132|Plant|Plant|Plant|Plant|Plant|Plant|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vDM_Material_Siemens_463872986|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|
|----|----|<site_id>||OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|
|UADM|vWorkOrder_Siemens_S_749389132|ErpOrder|ErpOrder|ErpOrder|ErpOrder|ErpOrder|ErpOrder|
|UADM|vWorkOrder_Siemens_S_749389132|ProducedQuantity||ProducedQuantity|ProducedQuantity|ProducedQuantity|ProducedQuantity|
|UADM|vWorkOrder_Siemens_S_749389132|ReworkedQuantity||ReworkedQuantity|ReworkedQuantity|ReworkedQuantity|ReworkedQuantity|
|UADM|vWorkOrder_Siemens_S_749389132|ScrappedQuantity||ScrapQuantity|ScrapQuantity|ScrapQuantity|ScrapQuantity|
|UADM|vMaterial_Siemens_Si_170253665|UoMNId||UomId|UomId|UomId|UomId|
|UADM|vWorkOrder_Siemens_S_749389132|ActualStartTime||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vWorkOrder_Siemens_S_749389132|ActualEndTime||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|UADM|vWorkOrder_Siemens_S_749389132|ActualStartTime - ActualEndTime||Duration|Duration|Duration|Duration|
|UADM|vWorkOrder_Siemens_S_749389132|PlannedTargetQuantity||PlannedQuantity|PlannedQuantity|PlannedQuantity|PlannedQuantity|
|UADM|vMaterial_Siemens_Si_170253665|UoMNId||PlannedQuantityUomId|PlannedQuantityUomId|PlannedQuantityUomId|PlannedQuantityUomId|
|UADM|vWorkOrder_Siemens_S_749389132|EstimatedStartTime||PlannedStartDateTime|PlannedStartDateTime|PlannedStartDateTime|PlannedStartDateTime|
|UADM|vWorkOrder_Siemens_S_749389132|EstimatedEndTime||PlannedEndDateTime|PlannedEndDateTime|PlannedEndDateTime|PlannedEndDateTime|
||||**OperationExecutionClass**||**ProductionType/ExecutionGroup**|UI Work Orders >> tab Details/UI Execution Groups||
|----|----|<site_id>||OperationExecutionClassSiteId||||
|UADM|vProductionType_Siem_763981173|Id  + '_ProductionType'||OperationExecutionClassKey|OperationExecutionClassKey|OperationExecutionClassKey|OperationExecutionClassKey|
|UADM|vProductionType_Siem_763981173|NId||Name|Name|Name|Name|
||||**OperationExecutionHierarchy**|||||
|----|----|<site_id>||OperationExecutionHierarchySiteId||||
|UADM|vWorkOrder_Siemens_S_749389132|Id||OperationExecutionHierarchyKey|OperationExecutionHierarchyKey|OperationExecutionHierarchyKey|OperationExecutionHierarchyKey|
|----|----|<site_id>||ParentOperationExecutionId|ParentOperationExecutionId|ParentOperationExecutionId|ParentOperationExecutionId|
|UADM|vWorkOrder_Siemens_S_749389132|Nid|Nid|Nid|Nid|Nid|Nid|
|----|----|<site_id>||OperationExecutionId|OperationExecutionId|OperationExecutionId|OperationExecutionId|
|UADM|vWorkOrder_Siemens_S_749389132|NId|NId|NId|NId|NId|NId|
||||**OperationExecutionOperationExecutionClass**||**WorkOrder**|UI Execution Groups >> open an ExecutionGroup >> tab Operations|WorkOrder-ProductionType/Execution Group association|
|----|----|<site_id>||OperationExecutionOperationExecutionClassSiteId||||
|UADM|vWorkOrder_Siemens_S_749389132|Id||OperationExecutionOperationExecutionClassKey|OperationExecutionOperationExecutionClassKey|OperationExecutionOperationExecutionClassKey|OperationExecutionOperationExecutionClassKey|
|----|----|<site_id>||OperationExecutionId|OperationExecutionId|OperationExecutionId|OperationExecutionId|
|UADM|vWorkOrder_Siemens_S_749389132|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||OperationExecutionClassId|OperationExecutionClassId|OperationExecutionClassId|OperationExecutionClassId|
|UADM|vWorkOrder_Siemens_S_749389132|ProductionType_Id  + '_ProductionType'|ProductionType_Id  + '_ProductionType'|ProductionType_Id  + '_ProductionType'|ProductionType_Id  + '_ProductionType'|ProductionType_Id  + '_ProductionType'|ProductionType_Id  + '_ProductionType'|
||||**OperationExecutionProperty**||**Attribute of a WorkOrder**|UI Execution Groups >> open an ExecutionGroup >> tab Operations,<br>grid mode|"Proces"s, "AsPlanned", "ERPOrder",<br>"ParentBatch","InitialQuality","IsUnderScheduling", "PBOPIdentID", "Plant",<br>"Priority", "ProcessNId", "ProcessRevision", "ProcessUId", "PoC",<br>"ReworkOfOrder", "EstimatedStartTime", "EstimatedEndTime"|
|----|----|<site_id>||OperationExecutionPropertySiteId||||
|----|----|"Process" OR "AsPlanned" OR "ERPOrder" OR<br>"InitialQuantity" OR "IsUnderScheduling" OR<br>"ParentBatch" OR "PoC" OR "Priority" OR "ProcessNId" OR<br>"ProcessRevision" OR "ProcessUId" OR "ReworkOfOrder"<br>OR "EstimatedStartTime" OR "EstimatedEndTime"||OperationExecutionPropertyKey|OperationExecutionPropertyKey|OperationExecutionPropertyKey|OperationExecutionPropertyKey|


|----|----|"Process" OR "AsPlanned" OR "ERPOrder" OR<br>"InitialQuantity" OR "IsUnderScheduling" OR<br>"ParentBatch" OR "PoC" OR "Priority" OR "ProcessNId" OR<br>"ProcessRevision" OR "ProcessUId" OR "ReworkOfOrder"<br>OR "EstimatedStartTime" OR "EstimatedEndTime"|Col4|Name|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|"String" OR "Numeric"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
||||**OperationExecutionPropertyStaticValue**||**Value for an attribute of a WorkOrder**|UI Work Orders, grid mode|"Proces"s, "AsPlanned", "ERPOrder",<br>"ParentBatch","InitialQuality","IsUnderScheduling", "PBOPIdentID", "Plant",<br>"Priority", "ProcessNId", "ProcessRevision", "ProcessUId", "PoC",<br>"ReworkOfOrder", "EstimatedStartTime", "EstimatedEndTime"|
|----|----|<site_id>||OperationExecutionPropertyStaticValueSiteId||||
|UADM|vWorkOrder_Siemens_S_749389132|(NId + '_' + 'Process') OR (NId + '_' + 'AsPlanned') OR (NId<br>+ '_' + 'ERPOrder') OR (NId + '_' + 'InitialQuantity') OR (NId<br>+ '_' + 'IsUnderScheduling') OR (NId + '_' + 'ParentBatch')<br>OR (NId + '_' + 'PoC') OR (NId + '_' + 'Priority') OR (NId + '_'<br>+ 'ProcessNId') OR (NId + '_' + 'ProcessRevision') OR (NId +<br>'_' + 'ProcessUId') OR (NId + '_' + 'ReworkOfOrder') OR<br>(NId + '_' + EstimatedStartTime) OR (NId + '_' +<br>EstimatedEndTime)||OperationExecutionPropertyStaticValueKey|OperationExecutionPropertyStaticValueKey|OperationExecutionPropertyStaticValueKey|OperationExecutionPropertyStaticValueKey|
|----|----|<site_id>||OperationExecutionId|OperationExecutionId|OperationExecutionId|OperationExecutionId|
|UADM|vWorkOrder_Siemens_S_749389132|NId|NId|NId|NId|NId|NId|
|UADM|vWorkOrder_Siemens_S_749389132|Process or  AsPlanned or ReworkOfOrder or ERPOrder or<br>ParentBatch or ProcessRevision or ProcessNId or<br>ProcessUId||StringValue|StringValue|StringValue|StringValue|
|UADM|vWorkOrder_Siemens_S_749389132|InitialQuantity, IsUnderScheduling, [Priority], PoC||FloatValue|FloatValue|FloatValue|FloatValue|
|UADM|vWorkOrder_Siemens_S_749389132|EstimatedStartTime, EstimatedEndTime||DatetimeValue|DatetimeValue|DatetimeValue|DatetimeValue|
|----|----|----||Sequence|Sequence|Sequence|Sequence|
||||**OperationExecutionStatus**||**WorkOrder**|UI Work Orders||
|----|----|<site_id>||OperationExecutionStatusSiteId||||
|UADM|vStatus_Siemens_Sim_2045546455|NId||OperationExecutionStatusKey|OperationExecutionStatusKey|OperationExecutionStatusKey|OperationExecutionStatusKey|
|UADM|vStatus_Siemens_Sim_2045546455|Name||Name|Name|Name|Name|
||||**OperationRequest**||**WorkOrderOperation/WorkOrderStep**|UI Work Orders >> open a WorkOrder >> tab Operations UI Work<br>Orders >> open a WorkOrder >> tab Operations >> tab Steps||
|----|----|<site_id>||OperationRequestSiteId||||
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Id||OperationRequestKey|OperationRequestKey|OperationRequestKey|OperationRequestKey|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Name OR Nid||Name|Name|Name|Name|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762|Description||Description|Description|Description|Description|
|----|----|<site_id>||OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|
|UADM|vWorkOrderOperation_1431095118|Operation|Operation|Operation|Operation|Operation|Operation|
|----|----|<site_id>||OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|
|UADM|vWorkOrderOperation_1431095118|WorkOrder_Id|WorkOrder_Id|WorkOrder_Id|WorkOrder_Id|WorkOrder_Id|WorkOrder_Id|
|----|----|<site_id>||OperationRequestStatusId|OperationRequestStatusId|OperationRequestStatusId|OperationRequestStatusId|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|EstimatedStartTime||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|EstimatedEndTime||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|UADM|vWorkOrderOperation_1431095118|TargetQuantity||EstimatedQuantity|EstimatedQuantity|EstimatedQuantity|EstimatedQuantity|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|EstimatedDuration||Duration|Duration|Duration|Duration|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroupPhase_469816675<br>or vWorkOrderStep_Siem_1809795233|Sequence||Sequence|Sequence|Sequence|Sequence|
||||**OperationRequestClass**||**Type of**<br>**WorkOrderOperation/WorkOrderStep**||WorkOrderOperation OR "ExecutionGroup" OR "ExecutionGroupPhase" OR<br>"WorkOrderStep"|
|----|----|<site_id>||OperationRequestClassSiteId||||
|----|----|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"||OperationRequestClassKey|OperationRequestClassKey|OperationRequestClassKey|OperationRequestClassKey|
|----|----|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"||Name|Name|Name|Name|
|----|----|<site_id>||OperationRequestHierarchySiteId|OperationRequestHierarchySiteId|OperationRequestHierarchySiteId|OperationRequestHierarchySiteId|
|UADM|vExecutionGroupPhase_469816675 or vWorkOrderStep_Siem_1809795233|Id||OperationRequestHierarchyKey|OperationRequestHierarchyKey|OperationRequestHierarchyKey|OperationRequestHierarchyKey|
|----|----|<site_id>||OperationRequestId|OperationRequestId|OperationRequestId|OperationRequestId|
|UADM|vExecutionGroupPhase_469816675 or vWorkOrderStep_Siem_1809795233|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||ParentOperationRequestId|ParentOperationRequestId|ParentOperationRequestId|ParentOperationRequestId|
|UADM|vExecutionGroupPhase_469816675 or vWorkOrderStep_Siem_1809795233|ExecutionGroup_Id or WorkOrderOperation_Id|ExecutionGroup_Id or WorkOrderOperation_Id|ExecutionGroup_Id or WorkOrderOperation_Id|ExecutionGroup_Id or WorkOrderOperation_Id|ExecutionGroup_Id or WorkOrderOperation_Id|ExecutionGroup_Id or WorkOrderOperation_Id|
||||**OperationRequestOperationRequestClass**|||||
|----|----|<site_id>||OperationRequestOperationRequestClassSiteId||||
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Id||OperationRequestOperationRequestClassKey|OperationRequestOperationRequestClassKey|OperationRequestOperationRequestClassKey|OperationRequestOperationRequestClassKey|
|----|----|<site_id>||OperationRequestId|OperationRequestId|OperationRequestId|OperationRequestId|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||OperationRequestClassId|OperationRequestClassId|OperationRequestClassId|OperationRequestClassId|
|----|----|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"|WorkOrderOperation OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep"|
||||**OperationRequestStatus**||**Status of**<br>**WorkOrderOperation/WorkOrderStep**|||
|----|----|<site_id>||OperationRequestStatusSiteId||||
|UADM|vStatus_Siemens_Sim_2045546455|NId||OperationRequestStatusKey|OperationRequestStatusKey|OperationRequestStatusKey|OperationRequestStatusKey|
|UADM|vStatus_Siemens_Sim_2045546455|Name||Name|Name|Name|Name|
||||**OperationResponse**||**WorkOrderOperation/WorkOrderStep**|UI Work Orders >> open a WorkOrder >> tab Operations UI Work<br>Orders >> open a WorkOrder >> tab Operations >> tab Steps||
|----|----|<site_id>||OperationResponseSiteId||||


|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Id|Col4|OperationResponseKey|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Name OR Nid||Name|Name|Name|Name|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vWorkOrderStep_Siem_1809795233|Description||Description|Description|Description|Description|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroupPhase_469816675<br>or vWorkOrderStep_Siem_1809795233|Sequence||Sequence|Sequence|Sequence|Sequence|
|----|----|<site_id>||OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|
|UADM|vWorkOrderOperation_1431095118|Operation|Operation|Operation|Operation|Operation|Operation|
|----|----|<site_id>||OperationExecutionId|OperationExecutionId|OperationExecutionId|OperationExecutionId|
|UADM|vWorkOrderOperation_1431095118|Nid|Nid|Nid|Nid|Nid|Nid|
|----|----|<site_id>||OperationResponseStatusId|OperationResponseStatusId|OperationResponseStatusId|OperationResponseStatusId|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||OperationRequestId|OperationRequestId|OperationRequestId|OperationRequestId|
|UADM|vWorkOrderOperation_1431095118 or vExecutionGroup_Siem_277554762<br>or vExecutionGroupPhase_469816675 or<br>vWorkOrderStep_Siem_1809795233|Id|Id|Id|Id|Id|Id|
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|ProducedQuantity||ProducedQuantity|ProducedQuantity|ProducedQuantity|ProducedQuantity|
|UADM|vWorkOrderOperation_1431095118|ReworkedQuantity||ReworkedQuantity|ReworkedQuantity|ReworkedQuantity|ReworkedQuantity|
|UADM|vWorkOrderOperation_1431095118|ScrappedQuantity||ScrapQuantity|ScrapQuantity|ScrapQuantity|ScrapQuantity|
|UADM|vMaterial_Siemens_Si_170253665|UoMNId||UomId|UomId|UomId|UomId|
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|ActualStartTime||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|ActualEndTime||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|ExecutionDuration||Duration|Duration|Duration|Duration|
|UADM|vWorkOrderOperation_1431095118 or<br>vExecutionGroup_Siem_277554762 or<br>vExecutionGroupPhase_469816675 or<br>vWorkOrderStep Siem 1809795233|NId||Identifier|Identifier|Identifier|Identifier|
||||**OperationResponseClass**||**WorkOperationType**|UI Work Operations||
|----|----|<site_id>||OperationResponseClassSiteId||||
|UADM|vWorkOperationType_Si_94474546<br>vOperationStepCateg 1572966020|Id OR "WorkOrderOperation" OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep" OR NId||OperationResponseClassKey|OperationResponseClassKey|OperationResponseClassKey|OperationResponseClassKey|
|UADM|vWorkOperationType_Si_94474546<br>vOperationStepCateg_1572966020|NId OR "WorkOrderOperation" OR "ExecutionGroup" OR<br>"ExecutionGroupPhase" OR "WorkOrderStep" OR Name||Name|Name|Name|Name|
|UADM|vOperationStepCateg_1572966020|Description OR NULL||Description|Description|Description|Description|
||||**OperationResponseEquipmentRequirement**|||||
|----|----|<site_id>||OperationResponseEquipmentRequirementSiteId||||
|UADM|vToBeUsedMachine_Sie_107405297|Id||OperationResponseEquipmentRequirementKey|OperationResponseEquipmentRequirementKey|OperationResponseEquipmentRequirementKey|OperationResponseEquipmentRequirementKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vToBeUsedMachine_Sie_107405297|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vToBeUsedMachine_Sie_107405297|Machine|Machine|Machine|Machine|Machine|Machine|
|----|----|1||Quantity|Quantity|Quantity|Quantity|
||||**OperationResponseEquipmentSpecification**||**ActualUsedMachine**|UI Work Orders >> select a WorkOrder >> button As Built >> tab<br>Activity History<br>You can also see them on UI Genealogy, in the tree representation,<br>under each WorkOrderOperation node||
|----|----|<site_id>||OperationResponseEquipmentSpecificationSiteId||||
|UADM|vWorkOrderHistory_Si_518515069|WorkOrderOperation_Id + '_' + Equipment + '_' + [Date]||OperationResponseEquipmentSpecificationKey|OperationResponseEquipmentSpecificationKey|OperationResponseEquipmentSpecificationKey|OperationResponseEquipmentSpecificationKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vWorkOrderHistory_Si_518515069|WorkOrderOperations_Id|WorkOrderOperations_Id|WorkOrderOperations_Id|WorkOrderOperations_Id|WorkOrderOperations_Id|WorkOrderOperations_Id|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vWorkOrderHistory_Si_518515069|Equipment|Equipment|Equipment|Equipment|Equipment|Equipment|
|UADM|vWorkOrderHistory_Si_518515069|Date||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vWorkOrderHistory_Si_518515069|Date||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|UADM|vWorkOrderHistory_Si_518515069|DATEDIFF(SECOND,Date,Date)||Duration|Duration|Duration|Duration|
|----|----|----||Quantity|Quantity|Quantity|Quantity|
||||**OperationResponseHierarchy**||**WorkOrderOperation/WorkOrderStep**|UI Work Orders >> tab Operations >> tab Steps|Hierarchical association between WorkOrderOperation and WorkOrderStep|
|----|----|<site_id>||OperationResponseHierarchySiteId||||
|UADM|vExecutionGroupPhase_469816675 or vExecutionGroupPhase_931440969<br>or vWorkOrderStep_Siem_1809795233|Id||OperationResponseHierarchyKey|OperationResponseHierarchyKey|OperationResponseHierarchyKey|OperationResponseHierarchyKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vExecutionGroupPhase_469816675 or vExecutionGroupPhase_931440969<br>or vWorkOrderStep_Siem_1809795233|Id OR<br>WorkOrderOperation_Id OR<br>Id|Id OR<br>WorkOrderOperation_Id OR<br>Id|Id OR<br>WorkOrderOperation_Id OR<br>Id|Id OR<br>WorkOrderOperation_Id OR<br>Id|Id OR<br>WorkOrderOperation_Id OR<br>Id|Id OR<br>WorkOrderOperation_Id OR<br>Id|
|----|----|<site_id>||ParentOperationResponseId|ParentOperationResponseId|ParentOperationResponseId|ParentOperationResponseId|
|UADM|vExecutionGroupPhase_469816675 or vExecutionGroupPhase_931440969<br>or vWorkOrderStep_Siem_1809795233|ExecutionGroup_Id OR<br>ExecutionGroupPhase_Id OR<br>WorkOrderOperation Id|ExecutionGroup_Id OR<br>ExecutionGroupPhase_Id OR<br>WorkOrderOperation Id|ExecutionGroup_Id OR<br>ExecutionGroupPhase_Id OR<br>WorkOrderOperation Id|ExecutionGroup_Id OR<br>ExecutionGroupPhase_Id OR<br>WorkOrderOperation Id|ExecutionGroup_Id OR<br>ExecutionGroupPhase_Id OR<br>WorkOrderOperation Id|ExecutionGroup_Id OR<br>ExecutionGroupPhase_Id OR<br>WorkOrderOperation Id|
||||**OperationResponseLaborSpecification**|||||
|----|----|<site_id>||OperationResponseLaborSpecificationSiteId||||
|UADM|vWorkOrderHistory_Si_518515069|Id||OperationResponseLaborSpecificationKey|OperationResponseLaborSpecificationKey|OperationResponseLaborSpecificationKey|OperationResponseLaborSpecificationKey|
|----|----|<site_id>||LaborId|LaborId|LaborId|LaborId|
|UADM|vWorkOrderHistory_Si_518515069|UserId|UserId|UserId|UserId|UserId|UserId|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vWorkOrderHistory_Si_518515069|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|WorkOrderOperation_Id|
|UADM|vWorkOrderHistory_Si_518515069|Date||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vWorkOrderHistory_Si_518515069|Date||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|----|----|----||Quantity|Quantity|Quantity|Quantity|
|UADM|vWorkOrderHistory_Si_518515069|DATEDIFF(SECOND,Date,Date)||Duration|Duration|Duration|Duration|
||||**OperationResponseMaterialDefinitionRequirementIn**|||||
|----|----|<site_id>||OperationResponseMaterialDefinitionRequirementInSiteId||||
|UADM|vToBeConsumedMateri_2105885214|id||OperationResponseMaterialDefinitionRequirementInKey|OperationResponseMaterialDefinitionRequirementInKey|OperationResponseMaterialDefinitionRequirementInKey|OperationResponseMaterialDefinitionRequirementInKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vToBeConsumedMateri_2105885214|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|


|UADM|vToBeConsumedMateri_2105885214|Quantity|Col4|Quantity|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|UADM|vMaterial_Siemens_Si_170253665|UoMNId||UomId|UomId|UomId|UomId|
||||**OperationResponseMaterialLotSpecificationIn**||**ActualConsumedMaterial**|UI Work Orders >> select a WorkOrder >> button As Built >> tab<br>Material. You can also see them on UI Genealogy, in the tree<br>representation, under each WorkOrderOperation node||
|----|----|<site_id>||OperationResponseMaterialLotSpecificationInSiteId||||
|UADM|vActualConsumedMater_420487820|(Id + '_WorkOrderOperation') OR (Id + '_WorkOrderStep')||OperationResponseMaterialLotSpecificationInKey|OperationResponseMaterialLotSpecificationInKey|OperationResponseMaterialLotSpecificationInKey|OperationResponseMaterialLotSpecificationInKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vActualConsumedMater_420487820|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vMaterialTrackingUni_494706508|NId|NId|NId|NId|NId|NId|
|UADM|vActualConsumedMater_420487820|MaterialItemAssembledQty||Quantity|Quantity|Quantity|Quantity|
||||**OperationResponseMaterialLotSpecificationOut**||**ProducedMaterialItem**|UI Work Orders >> open a WorkOrder: BatchID property/tab Serial<br>Numbers<br>UI Genealogy||
|----|----|<site_id>||OperationResponseMaterialLotSpecificationOutSiteId||||
|UADM|vActualConsumedMater_420487820|(Id + '_WorkOrderOperation') OR (Id + '_WorkOrderStep')||OperationResponseMaterialLotSpecificationOutKey|OperationResponseMaterialLotSpecificationOutKey|OperationResponseMaterialLotSpecificationOutKey|OperationResponseMaterialLotSpecificationOutKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vActualConsumedMater_420487820|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vMaterialTrackingUni_494706508|NId|NId|NId|NId|NId|NId|
|UADM|vActualConsumedMater_420487820|ProducedMaterialItemActualQty||Quantity|Quantity|Quantity|Quantity|
||||**OperationResponseOperationResponseClass**||**WorkOrderOperation**|UI Work Orders >> open a WorkOrder >> tab Operations|WorkOrderOperation-WorkOperationType association|
|----|----|<site_id>||OperationResponseOperationResponseClassSiteId||||
|UADM|vWorkOrderOperation_1431095118<br>vExecutionGroup_Siem_277554762<br>vExecutionGroupPhase_469816675<br>vWorkOrderStep_Siem_1809795233|((Id  + '_WorkOperationType') OR (Id  +<br>'_WorkOrderOperation' )) OR<br>(Id + '_ExecutionGroup') OR<br>(Id  + '_ExecutionGroupPhase') OR<br>(Id + ' WorkOrderStep') OR (Id + ' Category')||OperationResponseOperationResponseClassKey|OperationResponseOperationResponseClassKey|OperationResponseOperationResponseClassKey|OperationResponseOperationResponseClassKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vWorkOrderOperation_1431095118<br>vExecutionGroup_Siem_277554762<br>vExecutionGroupPhase_469816675<br>vWorkOrderStep Siem 1809795233|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||OperationResponseClassId|OperationResponseClassId|OperationResponseClassId|OperationResponseClassId|
|UADM|vWorkOrderOperation_1431095118<br>vExecutionGroup_Siem_277554762<br>vExecutionGroupPhase_469816675<br>vWorkOrderStep_Siem_1809795233<br>vOperationStepCateg_1572966020|WorkOperationType OR<br>"WorkOrderOperation" OR<br>"ExecutionGroup" OR<br>"ExecutionGroupPhase" OR<br>"WorkOrderStep" OR<br>NId|WorkOperationType OR<br>"WorkOrderOperation" OR<br>"ExecutionGroup" OR<br>"ExecutionGroupPhase" OR<br>"WorkOrderStep" OR<br>NId|WorkOperationType OR<br>"WorkOrderOperation" OR<br>"ExecutionGroup" OR<br>"ExecutionGroupPhase" OR<br>"WorkOrderStep" OR<br>NId|WorkOperationType OR<br>"WorkOrderOperation" OR<br>"ExecutionGroup" OR<br>"ExecutionGroupPhase" OR<br>"WorkOrderStep" OR<br>NId|WorkOperationType OR<br>"WorkOrderOperation" OR<br>"ExecutionGroup" OR<br>"ExecutionGroupPhase" OR<br>"WorkOrderStep" OR<br>NId|WorkOperationType OR<br>"WorkOrderOperation" OR<br>"ExecutionGroup" OR<br>"ExecutionGroupPhase" OR<br>"WorkOrderStep" OR<br>NId|
||||**OperationResponseProperty**||**Attribute of a WorkOrderOperation**|UI Work Orders >> open a WorkOrder >> tab Operations|"ElectronicSignatureComplete" , "ElectronicSignaturePause" ,<br>"ElectronicSignatureStart" , "EstimatedDuration" , "IsReady" , "LastPauseTime" ,<br>"Optional" , "PauseDuration" , "ExecutionDuration" , "Priority" ,<br>"RequiredCertificateNId" , "RequiredInspectionRole" , "TargetQuantity" ,<br>"WaitingForInspection" , "ActiveNonConformanceNr"|
|----|----|<site_id>||OperationResponsePropertySiteId||||
|----|----|"AvailableQuantity" or<br>"ElectronicSignatureComplete" or<br>"ElectronicSignaturePause" or<br>"ElectronicSignatureStart" or<br>"IsReady" or<br>"Skippable" or<br>"LastPauseTime" or<br>"Optional" or<br>"PauseDuration" or<br>"PartialWorkedQuantity" or<br>"Priority" or<br>"RequiredCertificateNId" or or<br>"RequiredInspectionRole"<br>"TargetQuantity" or<br>"WaitingForInspection" or<br>"ActiveNonConformanceNr"||OperationResponsePropertyKey|OperationResponsePropertyKey|OperationResponsePropertyKey|OperationResponsePropertyKey|
|----|----|"AvailableQuantity" or<br>"ElectronicSignatureComplete" or<br>"ElectronicSignaturePause" or<br>"ElectronicSignatureStart" or<br>"IsReady" or<br>"Skippable" or<br>"LastPauseTime" or<br>"Optional" or<br>"PauseDuration" or<br>"PartialWorkedQuantity" or<br>"Priority" or<br>"RequiredCertificateNId" or or<br>"RequiredInspectionRole"<br>"TargetQuantity" or<br>"WaitingForInspection" or<br>~~"ActiveNonConformanceNr"~~||Name|Name|Name|Name|
|----|----|"Numeric" or "DateTime" or "String"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
||||**OperationResponsePropertyStaticValue**||**Value for a WorkOrderOperation attribute**|UI Work Orders >> open a WorkOrder >> tab Operations, grid mode|"ElectronicSignatureComplete" , "ElectronicSignaturePause" ,<br>"ElectronicSignatureStart" , "EstimatedDuration" , "IsReady" , "LastPauseTime" ,<br>"Optional" , "PauseDuration" , "ExecutionDuration" , "Priority" ,<br>"RequiredCertificateNId" , "RequiredInspectionRole" , "TargetQuantity" ,<br>"WaitingForInspection" , "ActiveNonConformanceNr"|
|----|----|<site_id>||OperationResponsePropertyStaticValueSiteId||||
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|(Id +'_'+'AvailableQuantity') or<br>(Id +'_'+'ElectronicSignatureComplete') or<br>(Id +'_'+'ElectronicSignaturePause') or<br>(Id +'_'+'ElectronicSignatureStart') or<br>(Id +'_'+'IsReady') or<br>(Id +'_'+'Skippable') or<br>(Id +'_'+'LastPauseTime') or<br>(Id +'_'+'Optional') or<br>(Id +'_'+'PauseDuration') or<br>(Id +'_'+'PartialWorkedQuantity') or<br>(Id +'_'+'Priority') or<br>(Id +'_'+'RequiredCertificateNId')or<br>(Id +'_'+'RequiredInspectionRole') or<br>(Id +'_'+'TargetQuantity') or<br>(Id +'_'+'WaitingForInspection') or<br>(Id +'_'+'ActiveNonConformanceNr')||OperationResponsePropertyStaticValueKey|OperationResponsePropertyStaticValueKey|OperationResponsePropertyStaticValueKey|OperationResponsePropertyStaticValueKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|SitmesDb|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||OperationResponsePropertyId|OperationResponsePropertyId|OperationResponsePropertyId|OperationResponsePropertyId|


|----|----|"AvailableQuantity" or<br>"ElectronicSignatureComplete" or<br>"ElectronicSignaturePause" or<br>"ElectronicSignatureStart" or<br>"IsReady" or<br>"Skippable" or<br>"LastPauseTime" or<br>"Optional" or<br>"PauseDuration" or<br>"PartialWorkedQuantity" or<br>"Priority" or<br>"RequiredCertificateNId" or or<br>"RequiredInspectionRole"<br>"TargetQuantity" or<br>"WaitingForInspection" or<br>"ActiveNonConformanceNr"|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|RequiredCertificateNId, RequiredInspectionRole||StringValue|StringValue|StringValue|StringValue|
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|ElectronicSignatureComplete, ElectronicSignaturePause,<br>ElectronicSignatureStart, IsReady, Optional,<br>PauseDuration,<br>PartialWorkedQuantity, Priority, TargetQuantity,<br>WaitingForInspection, ActiveNonConformanceNr,<br>AvailableQuantity, Skippable||FloatValue|FloatValue|FloatValue|FloatValue|
|UADM|vWorkOrderOperation_1431095118 or vWorkOrderStep_Siem_1809795233|LastPauseTime||DatetimeValue|DatetimeValue|DatetimeValue|DatetimeValue|
||||**OperationResponseScrewingToolHistory**|||||
|----|----|<site_id>||OperationResponseScrewingToolHistorySiteId||||
|UADM|vScrewingToolHistor_1267691792|Id||OperationResponseScrewingToolHistoryKey|OperationResponseScrewingToolHistoryKey|||
|UADM|vScrewingToolHistor_1267691792|ItemId||Sequence|Sequence|||
|UADM|vScrewingToolHistor_1267691792|Torque||TorqueValue|TorqueValue|||
|UADM|vScrewingToolHistor_1267691792|Angle||AngleValue|AngleValue|||
|----|----|<site_id>||ToolId|ToolId|||
|UADM|vTool_Siemens_Simat_1812587140|Id|Id|Id|Id|||
|----|----|<site_id>||OperationResponseId|OperationResponseId|||
|UADM|vToBeUsedTool_Sieme_1383133102|WorkOrderOperation_Id or WorkorderStep_id|WorkOrderOperation_Id or WorkorderStep_id|WorkOrderOperation_Id or WorkorderStep_id|WorkOrderOperation_Id or WorkorderStep_id|||
|UADM|vScrewingToolHistor_1267691792|IsOk||IsOk|IsOk|||
|UADM|vScrewingToolHistor_1267691792|Reason||ResultValue|ResultValue|||
|UADM|vScrewingToolHistor_1267691792|UsageDate||EventDateTime|EventDateTime|||
||||**OperationResponseStatus**||**Status attribute of**<br>**WorkOrderOperation/WorkOrderStep**|||
|----|----|<site_id>||OperationResponseStatusSiteId||||
|UADM|vStatus_Siemens_Sim_2045546455|NId||OperationResponseStatusKey|OperationResponseStatusKey|OperationResponseStatusKey|OperationResponseStatusKey|
|UADM|vStatus_Siemens_Sim_2045546455|Name||Name|Name|Name|Name|
||||**OperationResponseToolDefinitionRequirement**|||||
|----|----|<site_id>||OperationResponseToolDefinitionRequirementSiteId||||
|UADM|vToBeUsedTool_Sieme_1383133102|Id||OperationResponseToolDefinitionRequirementKey|OperationResponseToolDefinitionRequirementKey|OperationResponseToolDefinitionRequirementKey|OperationResponseToolDefinitionRequirementKey|
|----|----|<site_id>||ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|
|UADM|vToBeUsedTool_Sieme_1383133102|ToolDefinition||||||
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vToBeUsedTool_Sieme_1383133102|WorkOrderOperation_Id OR WorkOrderStep_Id||||||
|UADM|vToBeUsedTool_Sieme_1383133102|TimesToBeUsed||TimesToBeUsed|TimesToBeUsed|TimesToBeUsed|TimesToBeUsed|
|UADM|vToBeUsedToolFacet__1563354502|AngleValueMin_Scre_1740246138||AngleValueMin|AngleValueMin|AngleValueMin|AngleValueMin|
|UADM|vToBeUsedToolFacet__1563354502|AngleValueMax_Screw_306736849||AngleValueMax|AngleValueMax|AngleValueMax|AngleValueMax|
|UADM|vToBeUsedToolFacet__1563354502|TorqueValueMin_Scre_438811650||TorqueValueMin|TorqueValueMin|TorqueValueMin|TorqueValueMin|
|UADM|vToBeUsedToolFacet__1563354502|TorqueValueMax_Scr_1023436010||TorqueValueMax|TorqueValueMax|TorqueValueMax|TorqueValueMax|
|UADM|vToBeUsedToolFacet__1563354502|NumberOfBolts_Scre_1350982661||NumberOfBolts|NumberOfBolts|NumberOfBolts|NumberOfBolts|
||||**OperationResponseToolSpecification**||**ActualUsedTool**|UI Work Orders >> select a WorkOrder >> button As Built >> tab<br>Activity Tools<br>You can also see them on UI Genealogy, in the tree representation,<br>under each WorkOrderOperation node||
|----|----|<site_id>||OperationResponseToolSpecificationSiteId||||
|UADM|vActualUsedTool_Sie_1932879556|(Id  + 'WorkOrderOperation') OR<br>(Id + 'WorkOrderStep')||OperationResponseToolSpecificationKey|OperationResponseToolSpecificationKey|OperationResponseToolSpecificationKey|OperationResponseToolSpecificationKey|
|----|----|<site_id>||ToolId|ToolId|ToolId|ToolId|
|----|vActualUsedTool_Sie_1932879556|Tool_Id|Tool_Id|Tool_Id|Tool_Id|Tool_Id|Tool_Id|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|----|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|WorkOrderOperation_Id OR WorkOrderStep_Id|
|UADM|vActualUsedTool_Sie_1932879556|UsedTimes||Quantity|Quantity|Quantity|Quantity|
||||**OperationScheduling**||**ErpOrder**|||
|----|----|<site_id>||OperationSchedulingSiteId||||
|UADM|vERPOrder_Siemens_O_1961544537|NId||OperationSchedulingKey|OperationSchedulingKey|OperationSchedulingKey|OperationSchedulingKey|
|UADM|vERPOrder_Siemens_O_1961544537|Name OR Nid||Name|Name|Name|Name|
|UADM|vERPOrder_Siemens_O_1961544537|Description||Description|Description|Description|Description|
|----|----|----||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|----|----|----|----|----|----|----|----|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||OperationSchedulingStatusId|OperationSchedulingStatusId|OperationSchedulingStatusId|OperationSchedulingStatusId|
|UADM|vERPOrder_Siemens_O_1961544537|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|
|UADM|vERPOrder_Siemens_O_1961544537|ProductionDate||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
|UADM|vERPOrder_Siemens_O_1961544537|DeliveryDate||EndDateTime|EndDateTime|EndDateTime|EndDateTime|
|UADM|vERPOrder_Siemens_O_1961544537|QuantityValue||EstimatedQuantity|EstimatedQuantity|EstimatedQuantity|EstimatedQuantity|
|----|----|----||Duration|Duration|Duration|Duration|
|----|----|<site_id>||FinalProductFamilyId|FinalProductFamilyId|FinalProductFamilyId|FinalProductFamilyId|
|UADM|vERPOrder_Siemens_O_1961544537|erp.FinalProductFamilyNId + '_' +<br>ProductConfigurationRevision|erp.FinalProductFamilyNId + '_' +<br>ProductConfigurationRevision|erp.FinalProductFamilyNId + '_' +<br>ProductConfigurationRevision|erp.FinalProductFamilyNId + '_' +<br>ProductConfigurationRevision|erp.FinalProductFamilyNId + '_' +<br>ProductConfigurationRevision|erp.FinalProductFamilyNId + '_' +<br>ProductConfigurationRevision|
|----|----|<site_id>||FinalProductTypeId|FinalProductTypeId|FinalProductTypeId|FinalProductTypeId|
|UADM|vERPOrder_Siemens_O_1961544537|FinalProductTypeNId|FinalProductTypeNId|FinalProductTypeNId|FinalProductTypeNId|FinalProductTypeNId|FinalProductTypeNId|
|UADM|vERPOrder_Siemens_O_1961544537|CustomerTypeNId||CustomerType|CustomerType|CustomerType|CustomerType|
|UADM|vERPOrder_Siemens_O_1961544537|Sequence||Sequence|Sequence|Sequence|Sequence|
|UADM|vERPOrder_Siemens_O_1961544537|SerialNumber||SerialNumber|SerialNumber|SerialNumber|SerialNumber|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vERPOrder_Siemens_O_1961544537|MaterialInstanceNId|MaterialInstanceNId|MaterialInstanceNId|MaterialInstanceNId|MaterialInstanceNId|MaterialInstanceNId|
||||**OperationSchedulingClass**|||||
|----|----|----||OperationSchedulingClassSiteId||||
|----|----|----||OperationSchedulingClassKey|OperationSchedulingClassKey|OperationSchedulingClassKey|OperationSchedulingClassKey|


|----|----|----|Col4|Name|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|----||Description|Description|Description|Description|
||||**OperationSchedulingExtendedProperty**|||||
|----|----|<site_id>||OperationSchedulingExtendedPropertySiteId||||
|UADM|vFeature_Siemens_Op_1528510985|NId||OperationSchedulingExtendedPropertyKey|OperationSchedulingExtendedPropertyKey|OperationSchedulingExtendedPropertyKey|OperationSchedulingExtendedPropertyKey|
|UADM|vFeature_Siemens_Op_1528510985|Name OR NId||Name|Name|Name|Name|
|UADM|vFeature_Siemens_Op_1528510985|Description||Description|Description|Description|Description|
|UADM|vFeature_Siemens_Op_1528510985|IsOption||IsOption|IsOption|IsOption|IsOption|
|----|----|"Feature"||ExtendedPropertyTypeId|ExtendedPropertyTypeId|ExtendedPropertyTypeId|ExtendedPropertyTypeId|
||||**OperationSchedulingExtendedPropertyStaticValue**|||||
|----|----|<site_id>||OperationSchedulingExtendedPropertyStaticValueSiteId||||
|UADM|vERPOrder_Siemens_O_1961544537<br>vFeatureItem Siemens 696016417|NId + '_' + FeatureNId||OperationSchedulingExtendedPropertyStaticValueKey|OperationSchedulingExtendedPropertyStaticValueKey|OperationSchedulingExtendedPropertyStaticValueKey|OperationSchedulingExtendedPropertyStaticValueKey|
|----|----|<site_id>||OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|
|UADM|vERPOrder_Siemens_O_1961544537|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||OperationSchedulingExtendedPropertyId|OperationSchedulingExtendedPropertyId|OperationSchedulingExtendedPropertyId|OperationSchedulingExtendedPropertyId|
|UADM|vFeatureItem_Siemens_696016417|FeatureNId|FeatureNId|FeatureNId|FeatureNId|FeatureNId|FeatureNId|
|UADM|vFeatureItem_Siemens_696016417|FeatureValueNId||Value|Value|Value|Value|
|UADM|vFeatureItem_Siemens_696016417|FeatureValueName||ValueName|ValueName|ValueName|ValueName|
|UADM|vFeatureItem_Siemens_696016417|FeatureValueDescription||ValueDescription|ValueDescription|ValueDescription|ValueDescription|
||||**OperationSchedulingMaterialDefinition**|||||
|----|----|<site_id>||OperationSchedulingMaterialDefinitionSiteId||||
|UADM|vERPOrder_Siemens_O_1961544537<br>vMaterial Siemens Si 170253665|NId + '_' + Id||OperationSchedulingMaterialDefinitionKey|OperationSchedulingMaterialDefinitionKey|OperationSchedulingMaterialDefinitionKey|OperationSchedulingMaterialDefinitionKey|
|----|----|<site_id>||OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|
|UADM|vERPOrder_Siemens_O_1961544537|NId||||||
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vMaterial_Siemens_Si_170253665|Id||||||
|UADM|vMaterialItem_Sieme_1585527977|QuantityValue.ItemQuantity||Quantity|Quantity|Quantity|Quantity|
|UADM|vMaterialItem_Sieme_1585527977|UoMNId.ItemQuantity||UomId|UomId|UomId|UomId|
||||**OperationSchedulingOperationSchedulingClass**|||||
|----|----|----||OperationSchedulingOperationSchedulingClassSiteId||||
|----|----|----||OperationSchedulingOperationSchedulingClassKey|OperationSchedulingOperationSchedulingClassKey|OperationSchedulingOperationSchedulingClassKey|OperationSchedulingOperationSchedulingClassKey|
|----|----|----||OperationSchedulingClassId|OperationSchedulingClassId|OperationSchedulingClassId|OperationSchedulingClassId|
|----|----|----|----|----|----|----|----|
|----|----|----||OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|OperationSchedulingId|
|----|----|----|----|----|----|----|----|
||||**OperationSchedulingStatus**||**Status of WorkOrder**|||
|UADM|vStatus_Siemens_Sim_2045546455|NId||OperationSchedulingStatusKey||||
|UADM|vStatus_Siemens_Sim_2045546455|Name||Name|Name|Name|Name|
||||**ProductionProcess**|||||
|UADM|vProcess_Siemens_Si_2118577807|UId||ProductionProcessKey|ProductionProcessKey|ProductionProcessKey|ProductionProcessKey|
|UADM|vProcess_Siemens_Si_2118577807|Name or null||Name|Name|Name|Name|
|----|vProcess_Siemens_Si_2118577807|Description||Description|Description|Description|Description|
|----|----|<site_id>||MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|MaterialDefinitionId|
|UADM|vDM_Material_Siemens_463872986|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|Material_Id|
|UADM|vProcess_Siemens_Si_2118577807|QuantityValue.Quantity||Quantity|Quantity|Quantity|Quantity|
|UADM|vProcess_Siemens_Si_2118577807|UoMNId.Quantity||UomId|UomId|UomId|UomId|
||||**ProductionProcessOperationDefinition**|||||
|----|----|<site_id>||ProductionProcessOperationDefinitionSiteId||||
|UADM|vProcessToOperation_2065129030|Id||ProductionProcessOperationDefinitionKey|ProductionProcessOperationDefinitionKey|ProductionProcessOperationDefinitionKey|ProductionProcessOperationDefinitionKey|
|----|----|<site_id>||OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|OperationDefinitionId|
|UADM|vOperation_Siemens_S_700803909|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||ProductionProcessId|ProductionProcessId|ProductionProcessId|ProductionProcessId|
|UADM|vProcess_Siemens_Si_2118577807|UId|UId|UId|UId|UId|UId|
|----|----|1||Quantity|Quantity|Quantity|Quantity|
||||**PropertyType**|||||
|----|----|"String" or "Numeric" or "DateTime"||PropertyTypeKey||||
|----|----|"String" or "Numeric" or "DateTime"||Name|Name|Name|Name|
|----|----|----||Description|Description|Description|Description|
||||**QualityFailure**|||||
|----|----|<site_id>||QualityFailureSiteId||||
|UADM|vFailure_Siemens_Op_1949421172|NId||QualityFailureKey|QualityFailureKey|QualityFailureKey|QualityFailureKey|
|UADM|vFailure_Siemens_Op_1949421172|Name||Name|Name|Name|Name|
|UADM|vFailure_Siemens_Op_1949421172|Description||Description|Description|Description|Description|
||||**QualityGate**|||||
|----|----|<site_id>||QualityGateSiteId||||
|UADM|vQualityGate_Siemen_1925666555|NId||QualityGateKey|QualityGateKey|QualityGateKey|QualityGateKey|
|UADM|vQualityGate_Siemen_1925666555|Name or NId||Name|Name|Name|Name|
|UADM|vQualityGate_Siemen_1925666555|Description||Description|Description|Description|Description|
||||**QualityGateEquipmentSpecification**|||||
|----|----|<site_id>||QualityGateEquipmentSpecificationSiteId||||
|UADM|vQGWorkplace_Siemens_895454935|Id||QualityGateEquipmentSpecificationKey|QualityGateEquipmentSpecificationKey|QualityGateEquipmentSpecificationKey|QualityGateEquipmentSpecificationKey|
|----|----|<site_id>||QualityGateId|QualityGateId|QualityGateId|QualityGateId|
|UADM|vQualityGate_Siemen_1925666555|NId||||||
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vQGWorkplace_Siemens_895454935|WorkplaceNId||||||
||||**QualityGateMonitoredEquipment**|||||
|----|----|<site_id>||QualityGateMonitoredEquipmentSiteId||||
|UADM|vQGMonitoredEquip_S_1538463432|Id||QualityGateMonitoredEquipmentKey|QualityGateMonitoredEquipmentKey|QualityGateMonitoredEquipmentKey|QualityGateMonitoredEquipmentKey|
|----|----|<site_id>||QualityGateId|QualityGateId|QualityGateId|QualityGateId|
|UADM|vQualityGate_Siemen_1925666555|NId||||||
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vQGMonitoredEquip_S_1538463432|EquipmentNId||||||
||||**QualityLimit**|||UI DCD Engineering||


|----|----|<site_id>|Col4|QualityLimitSiteId|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|UADM|vWorkInstructionStep_626862590|Id||QualityLimitKey|QualityLimitKey|QualityLimitKey|QualityLimitKey|
|----|----|<site_id>||QualityParameterId|QualityParameterId|QualityParameterId|QualityParameterId|
|UADM|vWorkInstructionStep_626862590|ItemNId|ItemNId|ItemNId|ItemNId|ItemNId|ItemNId|
|UADM|vWorkInstructionStep_626862590|HighLimit||HighLimit|HighLimit|HighLimit|HighLimit|
|UADM|vWorkInstructionStep_626862590|Target||Target|Target|Target|Target|
|UADM|vWorkInstructionStep_626862590|LowLimit||LowLimit|LowLimit|LowLimit|LowLimit|
||||**QualityParameter**|||UI DCD Engineering||
|----|----|<site_id>||QualityParameterSiteId||||
|UADM|vWorkInstructionStepIt_1299831 or vRuntimeCharacteris_1195087565|ItemNId<br>Id||QualityParameterKey|QualityParameterKey|QualityParameterKey|QualityParameterKey|
|UADM|vWorkInstructionStepIt_1299831 or vRuntimeCharacteris_1195087565|Label<br>NId||Name|Name|Name|Name|
|UADM|vWorkInstructionStepIt_1299831 or vRuntimeCharacteris_1195087565|Caption<br>Label||Description|Description|Description|Description|
||||**QualityParameterValue**||**DCDRuntime**|UI Operator Landing Page >> select a WorkOrderOperation >> Show<br>Details >> tab Data Collection; UI Genealogy; UI Work Orders >> As<br>Built >> tab Data Collections|Contains the values of data collection stored at runtime, e.g. data collection values<br>acquired on a WorkOrderOperation, or from the automation gateway, etc|
|----|----|<site_id>||QualityParameterValueSiteId||||
|UADM|vWorkInstructionStepIt_1299831  vInspectionValue_Siem_97476695<br>vVisualDetectedFailu 686437194|Id||QualityParameterValueKey|QualityParameterValueKey|QualityParameterValueKey|QualityParameterValueKey|
|----|----|<site_id>||QualityResponseId|QualityResponseId|QualityResponseId|QualityResponseId|
|UADM|vWorkInstructionSect_440022636  vInspectionValue_Siem_97476695<br>vVisualDetectedFailu 686437194|WorkInstruction_Id<br>InspectionSample Id|WorkInstruction_Id<br>InspectionSample Id|WorkInstruction_Id<br>InspectionSample Id|WorkInstruction_Id<br>InspectionSample Id|WorkInstruction_Id<br>InspectionSample Id|WorkInstruction_Id<br>InspectionSample Id|
|----|----|<site_id>||QualityParameterId|QualityParameterId|QualityParameterId|QualityParameterId|
|UADM|vWorkInstructionStepIt_1299831<br>vRuntimeCharacteris 1195087565|ItemNId<br>Id|ItemNId<br>Id|ItemNId<br>Id|ItemNId<br>Id|ItemNId<br>Id|ItemNId<br>Id|
|----|----|<site_id>||QualityFailureId|QualityFailureId|QualityFailureId|QualityFailureId|
|UADM|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu 686437194|FailureNId|FailureNId|FailureNId|FailureNId|FailureNId|FailureNId|
|----|----|<site_id>||LaborId|LaborId|LaborId|LaborId|
|UADM|vWorkInstructionStepIt_1299831<br>vInspectionValue_Siem_97476695<br>vVisualDetectedFailu 686437194|CompletedBy<br>User|CompletedBy<br>User|CompletedBy<br>User|CompletedBy<br>User|CompletedBy<br>User|CompletedBy<br>User|
|----|----|<site_id>||SampleId|SampleId|SampleId|SampleId|
|----|----|----|----|----|----|----|----|
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vInspectionValue_Siem_97476695<br>vVisualDetectedFailu 686437194|MTUNId|MTUNId|MTUNId|MTUNId|MTUNId|MTUNId|
|UADM|vWorkInstructionStepIt_1299831|ItemValue||DatetimeValue|DatetimeValue|DatetimeValue|DatetimeValue|
|UADM|vWorkInstructionStepIt_1299831 vInspectionValue_Siem_97476695<br>vVisualDetectedFailu_686437194|ItemValue<br>MeasuredVariableValue OR MeasuredAttributeValuel<br>Count||FloatValue|FloatValue|FloatValue|FloatValue|
|UADM|vWorkInstructionStepIt_1299831|ItemValue||StringValue|StringValue|StringValue|StringValue|
|UADM|vWorkInstructionStepIt_1299831  vInspectionValue_Siem_97476695<br>vVisualDetectedFailu 686437194|LastValueUpdatedOn<br>Timestamp||StartDateTime|StartDateTime|StartDateTime|StartDateTime|
||||**QualityResponse**||**DCDRuntimeTask**|UI Operator Landing Page >> select a WorkOrderOperation >> Show<br>Details >> tab Data Collection; UI Genealogy; UI Work Orders >> As<br>Built >> tab Data Collections|Contains the association between the runtime data collection and the<br>WorkOrderOperation / WorkOrderStep / K873MaterialItem, etc|
|----|----|<site_id>||QualityResponseSiteId||||
|UADM|vWorkInstruction_Si_1625357712 or vInspectionSample_S_1984849077|Id||QualityResponseKey|QualityResponseKey|QualityResponseKey|QualityResponseKey|
|UADM|vWorkInstruction_Si_1625357712 or vInspectionSample_S_1984849077|(Name OR NId) OR<br>Id||Name|Name|Name|Name|
|UADM|vWorkInstruction_Si_1625357712|Description||Description|Description|Description|Description|
|----|----|<site_id>||LaborId|LaborId|LaborId|LaborId|
|UADM|vInspectionSample_S_1984849077|User|User|User|User|User|User|
|----|----|<site_id>||QualityResponseStatusId|QualityResponseStatusId|QualityResponseStatusId|QualityResponseStatusId|
|UADM|vWorkInstruction_Si_1625357712|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|StatusNId.Status|
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vInspectionAcquisiti_557646680|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|EquipmentNId|
|----|----|<site_id>||QualityTaskDefinitionId|QualityTaskDefinitionId|QualityTaskDefinitionId|QualityTaskDefinitionId|
|UADM|vWorkInstruction_Si_1625357712|WorkInstructionDefinitionNId + '_' +<br>WorkInstructionDef 1609828362|WorkInstructionDefinitionNId + '_' +<br>WorkInstructionDef 1609828362|WorkInstructionDefinitionNId + '_' +<br>WorkInstructionDef 1609828362|WorkInstructionDefinitionNId + '_' +<br>WorkInstructionDef 1609828362|WorkInstructionDefinitionNId + '_' +<br>WorkInstructionDef 1609828362|WorkInstructionDefinitionNId + '_' +<br>WorkInstructionDef 1609828362|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vWorkInstructionToWo_350679847 or<br>dbo.vWorkInstructionToWo_665152508 or<br>vWorkInstructionToEx_538872687 or<br>vToBeUsedInspection<br>861818088|(WorkOrderOperation_Id or<br> workorderstep_id  or<br>executiongroupphase_id)  OR<br>(WorkOrderOperation Id or workorderstep id)|(WorkOrderOperation_Id or<br> workorderstep_id  or<br>executiongroupphase_id)  OR<br>(WorkOrderOperation Id or workorderstep id)|(WorkOrderOperation_Id or<br> workorderstep_id  or<br>executiongroupphase_id)  OR<br>(WorkOrderOperation Id or workorderstep id)|(WorkOrderOperation_Id or<br> workorderstep_id  or<br>executiongroupphase_id)  OR<br>(WorkOrderOperation Id or workorderstep id)|(WorkOrderOperation_Id or<br> workorderstep_id  or<br>executiongroupphase_id)  OR<br>(WorkOrderOperation Id or workorderstep id)|(WorkOrderOperation_Id or<br> workorderstep_id  or<br>executiongroupphase_id)  OR<br>(WorkOrderOperation Id or workorderstep id)|
||||**QualityResponseClass**||**Type of DCDRuntimeTask**|||
|----|----|<site_id>||QualityResponseClassSiteId|||"WorkInstruction" OR "InspectionSample"|
|----|----|"WorkInstruction" OR "InspectionSample"||QualityResponseClassKey|QualityResponseClassKey|QualityResponseClassKey|QualityResponseClassKey|
|----|----|"WorkInstruction" OR "InspectionSample"||Name|Name|Name|Name|
||||**QualityResponseProperty**||**DCDRuntimeTask property**|||
|----|----|<site_id>||QualityResponsePropertySiteId||||
|----|----|"AnyViolation"||QualityResponsePropertyKey|QualityResponsePropertyKey|QualityResponsePropertyKey|QualityResponsePropertyKey|
|----|----|AnyViolation||Name|Name|Name|Name|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
|----|----|"Numeric"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
||||**QualityResponsePropertyStaticValue**||**DCDRuntimeTask + DCDRuntime**|UI Operator Landing Page >> select a WorkOrderOperation >> Show<br>Details >> tab Data Collection; UI Genealogy; UI Work Orders >> As<br>Built >> tab Data Collections||
|----|----|<site_id>||QualityResponsePropertyStaticValueSiteId||||
|UADM|vInspectionSample_S_1984849077|Id + '_AnyViolation'||QualityResponsePropertyStaticValueKey|QualityResponsePropertyStaticValueKey|QualityResponsePropertyStaticValueKey|QualityResponsePropertyStaticValueKey|
|----|----|<site_id>||QualityResponseId|QualityResponseId|QualityResponseId|QualityResponseId|
|UADM|vInspectionSample_S_1984849077|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||QualityResponsePropertyId|QualityResponsePropertyId|QualityResponsePropertyId|QualityResponsePropertyId|
|----|----|"AnyViolation"|"AnyViolation"|"AnyViolation"|"AnyViolation"|"AnyViolation"|"AnyViolation"|
|UADM|vInspectionSample_S_1984849077|AnyViolation||FloatValue|FloatValue|FloatValue|FloatValue|
||||**QualityResponseQualityResponseClass**||**Relationship between DCDRuntimeTask and**<br>**its type**|||
|----|----|<site_id>||QualityResponseQualityResponseClassSiteId||||
|UADM|vWorkInstruction_Si_1625357712 or vInspectionSample_S_1984849077|Id + '_WorkInstruction' OR<br>Id + ' InspectionSample'||QualityResponseQualityResponseClassKey|QualityResponseQualityResponseClassKey|QualityResponseQualityResponseClassKey|QualityResponseQualityResponseClassKey|
|----|----|<site_id>||QualityResponseId|QualityResponseId|QualityResponseId|QualityResponseId|
|UADM|vWorkInstruction_Si_1625357712 or vInspectionSample_S_1984849077|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||QualityResponseClassId|QualityResponseClassId|QualityResponseClassId|QualityResponseClassId|
|----|----|'WorkInstruction" OR "InspectionSample"|'WorkInstruction" OR "InspectionSample"|'WorkInstruction" OR "InspectionSample"|'WorkInstruction" OR "InspectionSample"|'WorkInstruction" OR "InspectionSample"|'WorkInstruction" OR "InspectionSample"|
||||**QualityResponseStatus**||**DCDRuntimeTask status**|||
|----|----|<site_id>||QualityResponseStatusSiteId||||
|UADM|vStatus_Siemens_Sim_2045546455|NId||QualityResponseStatusKey|QualityResponseStatusKey|QualityResponseStatusKey|QualityResponseStatusKey|
|UADM|vStatus_Siemens_Sim_2045546455|Name||Name|Name|Name|Name|
||||**QualityTaskDefinition**||**DCDTask**|UI DCD Engineering; UI Operation Catalog >> Operation Details >> tab<br>Data collections; UI Work Orders >> Operations >> tab Data<br>Collections|Defines a runtime data collection|


|----|----|<site_id>|Col4|QualityTaskDefinitionSiteId|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|UADM|vWorkInstructionDefi_275522137|NId + '_' + Revision||QualityTaskDefinitionKey|QualityTaskDefinitionKey|QualityTaskDefinitionKey|QualityTaskDefinitionKey|
|UADM|vWorkInstructionDefi_275522137|Name OR NId||Name|Name|Name|Name|
|UADM|vWorkInstructionDefi_275522137|Description||Description|Description|Description|Description|
||||**QualityTaskDefinitionProperty**||**DCDTask property**|UI DCD Engineering; UI Operation Catalog >> Operation Details >> tab<br>Data collections; UI Work Orders >> Operations >> tab Data<br>Collections|"Status" or "IsCurrent"|
|----|----|<site_id>||QualityTaskDefinitionPropertySiteId||||
|----|----|"IsExecutable" or "IsCurrent"||QualityTaskDefinitionPropertyKey|QualityTaskDefinitionPropertyKey|QualityTaskDefinitionPropertyKey|QualityTaskDefinitionPropertyKey|
|----|----|"IsExecutable" or "IsCurrent"||Name|Name|Name|Name|
|----|----|"Numeric"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
||||**QualityTaskDefinitionPropertyStaticValue**||**DCDTask property value**|UI DCD Engineering; UI Operation Catalog >> Operation Details >> tab<br>Data collections; UI Work Orders >> Operations >> tab Data<br>Collections|"Approved" or "Editing" or "Obsolete" or "Unknown"|
|----|----|<site_id>||QualityTaskDefinitionPropertyStaticValueSiteId||||
|UADM|vWorkInstructionDefi_275522137|NId + '_' + Revision||QualityTaskDefinitionPropertyStaticValueKey|QualityTaskDefinitionPropertyStaticValueKey|QualityTaskDefinitionPropertyStaticValueKey|QualityTaskDefinitionPropertyStaticValueKey|
|----|----|<site_id>||QualityTaskDefinitionId|QualityTaskDefinitionId|QualityTaskDefinitionId|QualityTaskDefinitionId|
|UADM|vWorkInstructionDefi_275522137|NId + '_' + Revision|NId + '_' + Revision|NId + '_' + Revision|NId + '_' + Revision|NId + '_' + Revision|NId + '_' + Revision|
|----|----|<site_id>||QualityTaskDefinitionPropertyId|QualityTaskDefinitionPropertyId|QualityTaskDefinitionPropertyId|QualityTaskDefinitionPropertyId|
|----|----|"IsExecutable" or "IsCurrent"|"IsExecutable" or "IsCurrent"|"IsExecutable" or "IsCurrent"|"IsExecutable" or "IsCurrent"|"IsExecutable" or "IsCurrent"|"IsExecutable" or "IsCurrent"|
|----|----|IsExecutable or IsCurrent||FloatValue|FloatValue|FloatValue|FloatValue|
||||**Result**|||||
|----|----|<site_id>||ResultSiteId||||
|UADM|vResult_Siemens_Sim_1883522939|Id||ResultKey|ResultKey|ResultKey|ResultKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vWorkOrderOperation_1431095118 or<br>vWorkOrderStep Siem 1809795233|Id||||||
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vResult_Siemens_Sim_1883522939|MaterialTrackingUnitNId||||||
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vResult_Siemens_Sim_1883522939|EquipmentNId||||||
|UADM|vResultType_Siemens_1039918083|ResultValue||Value|Value|Value|Value|
|----|----|<site_id>||ResultStrategyId|ResultStrategyId|ResultStrategyId|ResultStrategyId|
|UADM|vResultStrategy_Sie_1169113914|NId||||||
|UADM|vResult_Siemens_Sim_1883522939|ActivityNId||Activity|Activity|Activity|Activity|
|UADM|vResultType_Siemens_1039918083|IsKO||IsKO|IsKO|IsKO|IsKO|
||||**ResultHistory**|||||
|----|----|<site_id>||ResultHistorySiteId||||
|UADM|vResultHistory_Sieme_750013293|Id||ResultHistoryKey|ResultHistoryKey|ResultHistoryKey|ResultHistoryKey|
|----|----|<site_id>||OperationResponseId|OperationResponseId|OperationResponseId|OperationResponseId|
|UADM|vWorkOrderOperation_1431095118 or<br>vWorkOrderStep Siem 1809795233|Id||||||
|----|----|<site_id>||MaterialLotId|MaterialLotId|MaterialLotId|MaterialLotId|
|UADM|vResultHistory_Sieme_750013293|MaterialTrackingUnitNId||||||
|----|----|<site_id>||EquipmentId|EquipmentId|EquipmentId|EquipmentId|
|UADM|vResultHistory_Sieme_750013293|EquipmentNId||||||
|----|----|<site_id>||LaborId|LaborId|LaborId|LaborId|
|UADM|vResultHistory_Sieme_750013293|UserId||||||
|UADM|vResultHistory_Sieme_750013293|Date||EventDateTime|EventDateTime|EventDateTime|EventDateTime|
|UADM|vResultHistory_Sieme_750013293|ResultValue||Value|Value|Value|Value|
|UADM|vResultHistory_Sieme_750013293|ResultIsKO||IsKO|IsKO|IsKO|IsKO|
|UADM|vResultHistory_Sieme_750013293|IsPartial||IsPartial|IsPartial|IsPartial|IsPartial|
|----|----|<site_id>||ResultStrategyId|ResultStrategyId|ResultStrategyId|ResultStrategyId|
|UADM|vResultHistory_Sieme_750013293|ResultStrategy||||||
|UADM|vResultHistory_Sieme_750013293|ActivityNId||Activity|Activity|Activity|Activity|
|----|----|<site_id>||ResultId|ResultId|ResultId|ResultId|
|UADM|vResultHistory_Sieme_750013293|Results_Id||||||
||||**ResultHistoryTraceabilityDetail**|||||
|----|----|<site_id>||ResultHistoryTraceabilityDetailSiteId||||
|UADM|vResultHistoryFacet_2015840138|Id||ResultHistoryTraceabilityDetailKey||||
|----|----|<site_id>||ResultHistoryId||||
|UADM|vResultHistoryFacet_2015840138|ResultHistory_Id||||||
|UADM|vResultHistoryFacet_2015840138|Barcode_Traceabilit_273389130||Barcode||||
||||**ResultStrategy**|||||
|----|----|<site_id>||ResultStrategySiteId||||
|UADM|vResultStrategy_Sie_1169113914|NId||ResultStrategyKey|ResultStrategyKey|ResultStrategyKey|ResultStrategyKey|
|UADM|vResultStrategy_Sie_1169113914|NId||Name|Name|Name|Name|
|----|----|----||Description|Description|Description|Description|
||||**Site**|||||
|----|----|----||SiteId||||
|----|----|----||TimeZoneId|TimeZoneId|TimeZoneId|TimeZoneId|
|----|----|----||Name|Name|Name|Name|
|----|----|----||Description|Description|Description|Description|
|----|----|----||Longitude|Longitude|Longitude|Longitude|
|----|----|----||Latitude|Latitude|Latitude|Latitude|
||||**Skill**||**Skill**|||
|----|----|<site_id>||SkillSiteId||||
|UADM|vSkill_Siemens_Simati_42755608|NId||SkillKey|SkillKey|SkillKey|SkillKey|
|UADM|vSkill_Siemens_Simati_42755608|Name||Name|Name|Name|Name|
|UADM|vSkill_Siemens_Simati_42755608|Description||Description|Description|Description|Description|
||||**SkillCertification**||**SkillCertification**|||
|----|----|<site_id>||SkillCertificationSiteId||||
|UADM|vSkillCertificationA_173620417|Id||SkillCertificationKey|SkillCertificationKey|SkillCertificationKey|SkillCertificationKey|
|----|----|<site_id>||SkillId|SkillId|SkillId|SkillId|
|UADM|vSkill_Siemens_Simati_42755608|NId|NId|NId|NId|NId|NId|
|----|----|<site_id>||CertificationId|CertificationId|CertificationId|CertificationId|


|UADM|vCertification_Sieme_165689816|NId|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||**TimeZone**|||||
|----|----|----||TimeZoneKey||||
|----|----|----||Name|Name|Name|Name|
|----|----|----||Description|Description|Description|Description|
|----|----|----||OffSet|OffSet|OffSet|OffSet|
||||**TimeZoneDaylightTimeSaving**|||||
|----|----|----||TimeZoneDaylightTimeSavingKey||||
|----|----|----||TimeZoneId|TimeZoneId|TimeZoneId|TimeZoneId|
|----|----|----||OffSet|OffSet|OffSet|OffSet|
|----|----|----||DateFrom|DateFrom|DateFrom|DateFrom|
|----|----|----||DateTo|DateTo|DateTo|DateTo|
||||**Tool**||**Tool**|UI Tools||
|----|----|<site_id>||ToolSiteId||||
|UADM|vTool_Siemens_Simat_1812587140|Id||ToolKey|ToolKey|ToolKey|ToolKey|
|UADM|vTool_Siemens_Simat_1812587140|Name OR NId||Name|Name|Name|Name|
|UADM|vTool_Siemens_Simat_1812587140|Description||Description|Description|Description|Description|
|----|----|<site_id>||ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|
|UADM|vTool_Siemens_Simat_1812587140|ToolDefinition|ToolDefinition|ToolDefinition|ToolDefinition|ToolDefinition|ToolDefinition|
||||**ToolDefinition**||**ToolDefinition**|UI Tool Definitions||
|----|----|<site_id>||ToolDefinitionSiteId||||
|UADM|vToolDefinition_Sie_1485280720|Id||ToolDefinitionKey|ToolDefinitionKey|ToolDefinitionKey|ToolDefinitionKey|
|UADM|vToolDefinition_Sie_1485280720|Name OR NId||Name|Name|Name|Name|
|UADM|vToolDefinition_Sie_1485280720|Description||Description|Description|Description|Description|
||||**ToolDefinitionPropertyStaticValue**||**Value for a ToolDefinition attribute**|UI Tool Definitions, grid mode|"Revision", "Quantity"|
|----|----|<site_id>||ToolDefinitionPropertyStaticValueSiteId||||
|UADM|vToolDefinition_Sie_1485280720|(Id  +'_' + 'ExpirationDate') OR (Id  +'_' +<br>'UsageCounterMax') OR (Id  +'_' + 'UsageDurationMax')<br>OR (Id  +' ' + 'Version')  OR (Id  +' ' + 'Consumable')||ToolDefinitionPropertyStaticValueKey|ToolDefinitionPropertyStaticValueKey|ToolDefinitionPropertyStaticValueKey|ToolDefinitionPropertyStaticValueKey|
|----|----|<site_id>||ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|ToolDefinitionId|
|UADM|vToolDefinition_Sie_1485280720|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||ToolPropertyId|ToolPropertyId|ToolPropertyId|ToolPropertyId|
|----|----|"ExpirationDate" OR "UsageCounterMax" OR<br>"UsageDurationMax"  OR "Version"  OR "Consumable"|"ExpirationDate" OR "UsageCounterMax" OR<br>"UsageDurationMax"  OR "Version"  OR "Consumable"|"ExpirationDate" OR "UsageCounterMax" OR<br>"UsageDurationMax"  OR "Version"  OR "Consumable"|"ExpirationDate" OR "UsageCounterMax" OR<br>"UsageDurationMax"  OR "Version"  OR "Consumable"|"ExpirationDate" OR "UsageCounterMax" OR<br>"UsageDurationMax"  OR "Version"  OR "Consumable"|"ExpirationDate" OR "UsageCounterMax" OR<br>"UsageDurationMax"  OR "Version"  OR "Consumable"|
|UADM|vToolDefinition_Sie_1485280720|Version||StringValue|StringValue|StringValue|StringValue|
|UADM|vToolDefinition_Sie_1485280720|UsageCounterMax OR UsageDurationMax OR Consumable||FloatValue|FloatValue|FloatValue|FloatValue|
|UADM|vToolDefinition_Sie_1485280720|ExpirationDate||DatetimeValue|DatetimeValue|DatetimeValue|DatetimeValue|
||||**ToolProperty**||**Attribute of a Tool**|UI Tools, grid mode|"Revision", "Quantity"|
|----|----|<site_id>||ToolPropertySiteId||||
|----|----|"ExpirationDate" OR<br>"UsageCounter" OR<br>"UsageCounterMax" OR<br>"UsageDuration" OR<br>"UsageDurationMax"OR<br>"Version" OR<br>"Consumable"||ToolPropertyKey|ToolPropertyKey|ToolPropertyKey|ToolPropertyKey|
|----|----|"ExpirationDate" OR<br>"UsageCounter" OR<br>"UsageCounterMax" OR<br>"UsageDuration" OR<br>"UsageDurationMax"OR<br>"Version" OR<br>"Consumable"||Name|Name|Name|Name|
|----|----|"String" or "Numeric" OR "DateTime"||PropertyTypeId|PropertyTypeId|PropertyTypeId|PropertyTypeId|
|----|----|"n/a"||UomId|UomId|UomId|UomId|
||||**ToolPropertyStaticValue**||**Value for a Tool attribute**|UI Tools, grid mode|"Revision", "Quantity"|
|----|----|<site_id>||ToolPropertyStaticValueSiteId||||
|UADM|vTool_Siemens_Simat_1812587140|(Id  +'_' + 'ExpirationDate') OR (Id  +'_' + 'UsageCounter')<br>OR (Id  +'_' + 'UsageCounterMax') OR (Id  +'_' +<br>'UsageDuration') OR (Id  +' ' + 'UsageDurationMax')||ToolPropertyStaticValueKey|ToolPropertyStaticValueKey|ToolPropertyStaticValueKey|ToolPropertyStaticValueKey|
|----|----|<site_id>||ToolId|ToolId|ToolId|ToolId|
|UADM|vTool_Siemens_Simat_1812587140|Id|Id|Id|Id|Id|Id|
|----|----|<site_id>||ToolPropertyId|ToolPropertyId|ToolPropertyId|ToolPropertyId|
|----|----|"ExpirationDate" OR "UsageCounter" OR<br>"UsageCounterMax" OR "UsageDuration" OR<br>"UsageDurationMax"|"ExpirationDate" OR "UsageCounter" OR<br>"UsageCounterMax" OR "UsageDuration" OR<br>"UsageDurationMax"|"ExpirationDate" OR "UsageCounter" OR<br>"UsageCounterMax" OR "UsageDuration" OR<br>"UsageDurationMax"|"ExpirationDate" OR "UsageCounter" OR<br>"UsageCounterMax" OR "UsageDuration" OR<br>"UsageDurationMax"|"ExpirationDate" OR "UsageCounter" OR<br>"UsageCounterMax" OR "UsageDuration" OR<br>"UsageDurationMax"|"ExpirationDate" OR "UsageCounter" OR<br>"UsageCounterMax" OR "UsageDuration" OR<br>"UsageDurationMax"|
|UADM|vTool_Siemens_Simat_1812587140|UsageCounter OR UsageCounterMax OR UsageDuration<br>OR UsageDurationMax||FloatValue|FloatValue|FloatValue|FloatValue|
|UADM|vTool_Siemens_Simat_1812587140|ExpirationDate||DatetimeValue|DatetimeValue|DatetimeValue|DatetimeValue|
||||**Uom**|||||
|UADM|vUoM_Siemens_Simati_1027974907|NId||UomKey||||
|UADM|vUoM_Siemens_Simati_1027974907|Name||Name|Name|Name|Name|
|UADM|vUoM_Siemens_Simati_1027974907|Description||Description|Description|Description|Description|
|----|----|1||UomSystemId|UomSystemId|UomSystemId|UomSystemId|
|----|----|1||UomCategoryId|UomCategoryId|UomCategoryId|UomCategoryId|


