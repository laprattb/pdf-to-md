|Opcenter EX EL Entities|Col2|Col3|Col4|Col5|Opcenter Execution Core Model Entities|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**DB Name**|**Entity**|**Attribute**|~~**Entity**~~<br>|~~**Attribute**~~|~~**Entity exposed by EX CR Model**~~|~~**UI**~~|**Mapping Info**|
||||~~**BillOfMaterial**~~|||||
|----|----|<site id>||BillOfMaterialSiteId<br>||||
|CEPdb|bom|BomId||~~BillOfMaterialKey~~<br>|~~BILLOFMATERIAL~~|||
|CEPdb|bomBase or bom|bomName or BomId||~~Name~~<br>||||
|CEPdb|bom|Description||~~Description~~<br>||||
|----|----|----||~~Quantity~~<br>||||
|----|----|----||~~UomKey~~||||
|----|----|----||MaterialDefinitionId||||
|----|----|----||||||
||||~~**BillOfMaterialItem**~~|||||
|----|----|<site id>||BillOfMaterialItemSiteId||||
|CEPdb|ProductMaterialListItem|ProductMaterialListItemId||BillOfMaterialItemKey|~~BILLOFMATERIALITEM~~|||
|----|----|<site id>||BillOfMaterialId||||
|CEPdb|ProductMaterialListItem|BOMId||||||
|----|----|<site id>||MountingTechnologyId||||
|CEPdb|Product|ES_MountingTechnology||||||
|CEPdb|ProductMaterialListItem|ProductMaterialListItemName||Name||||
|CEPdb|ProductMaterialListItem|ReferenceDesignator||Description||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|ProductMaterialListItem|ProductId||||||
|CEPdb|ProductMaterialListItem|QtyRequired||Quantity||||
|CEPdb|UOM|UOMName||UomKey||||
||||~~**Container**~~|||||
|----|----|<site id>||ContainerSiteId||||
|CEPdb|Container|ContainerId||ContainerKey|CONTAINER|||
|CEPdb|Container|ContainerName||Name||||
|CEPdb|Container|ContainerComments||Description||||
|CEPdb|CurrentStatus|InProcess||IsInProcess||||
|CEPdb|CurrentStatus|InRework||IsInRework||||
|CEPdb|Container|IsFailed||IsFailed||||
|CEPdb|ContainerLevel|CASE ES_LevelType<br>                    WHEN 1 THEN 'PANEL'<br>                    WHEN 2 THEN 'PCB'<br>                    WHEN 3 THEN 'COMPONENT'<br>                    ELSE 'OTHER'||LevelName||||
|CEPdb|Container|ES_PrimarySerialNumber||SerialNumber||||
|----|----|<site id>||ContainerStatusId||||
|CEPdb|Container|Status||||||
||||~~**ContainerClass**~~|||||
|----|----|----||ContainerClassSiteId||||
|CEPdb|ContainerLevel|ContainerLevelId||ContainerClassKey|CONTAINERLEVEL|||
|CEPdb|ContainerLevel|ContainerLevelName||Name||||
|CEPdb|ContainerLevel|Description||Description||||
||||~~**ContainerContainerClass**~~|||||
|----|----|<site id>||ContainerContainerClassSiteId||||
|CEPdb|Container|ContainerId||ContainerContainerClassKey||||
|----|----|<site id>||ContainerClassId||||
|CEPdb|Container|LevelId||||||
|----|----|<site id>||ContainerId||||
|CEPdb|Container|ContainerId||||||
||||~~**ContainerCorrelation**~~|||||
|----|----|<site id>||ContainerCorrelationSiteId||||
|CEPdb|HistoryMainline, HistoryCrossRef|HistoryMainlineId +'_'+ HistoryCrossRefId||ContainerCorrelationKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|HistoryCrossRef|TrackingId||||||
|----|----|<site id>||ParentContainerId||||
|CEPdb|HistoryCrossRef|HistoryId||||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
||||~~**ContainerCurrentStatus**~~|||||
|----|----|<site id>||ContainerCurrentStatusSiteId||||
|CEPdb|CurrentStatus, Container|CurrentStatusId +'_'+ ContainerId||ContainerCurrentStatusKey|CURRENTSTATUS|||
|CEPdb|CurrentStatus|CurrentStepPass||CurrentStepPass||||
|----|----|<site id>||FactoryId||||
|CEPdb|CurrentStatus|FactoryId||||||
|CEPdb|CurrentStatus|LastMoveDate||LastMoveDate||||
|CEPdb|CurrentStatus|LastMoveDateGMT||LastMoveDateGMT||||
|----|----|<site id>||LocationId||||
|CEPdb|CurrentStatus|LocationId||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|CurrentStatus|ResourceId||||||
|CEPdb|CurrentStatus|ReworkLoopCount||ReworkLoopCount||||
|CEPdb|CurrentStatus|ReworkTotalCount||ReworkTotalCount||||
|----|----|<site id>||SpecId||||
|CEPdb|CurrentStatus|SpecId||||||
|CEPdb|CurrentStatus|TimersCount||TimersCount||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|CurrentStatus|WorkflowStepId||||||
|----|----|<site id>||OperationId||||
|CEPdb|Spec|OperationId||||||
|----|----|<site id>||ContainerId||||
|CEPdb|Container|ContainerId||||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|Container|ProductId||||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|Container|MfgOrderId||||||


|CEPdb|CurrentStatus|isOpStartQty|Col4|OpStartQty|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CEPdb|CurrentStatus|isOpStartQty2||OpSecondaryStartQty||||
|CEPdb|Container|Qty||ContainerQty||||
|CEPdb|Container|Qty2||ContainerSecondaryQty||||
|CEPdb|UOM|UOMName||UomId||||
|CEPdb|UOM|UOMName||SecondaryUomId||||
||||~~**ContainerHierarchy**~~|||||
|----|----|<site id>||ContainerHierarchySiteId||||
|CEPdb|Container|ContainerId||ContainerHierarchyKey|CONTAINERHIERARCHY|||
|----|----|<site id>||ParentContainerId||||
|CEPdb|Container|ParentContainerId||||||
|----|----|<site id>||ContainerId||||
|CEPdb|Container|ContainerId||||||
||||~~**ContainerOperation**~~|||||
|----|----|<site id>||ContainerOperationSiteId||||
|CEPdb|HistoryMainline|HistoryMainlineId||ContainerOperationKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|HistoryMainline|ContainerId||||||
|----|----|<site id>||ContainerOperationStatusId||||
|----|----|FAIL' or 'PASS'||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|HistoryMainline|ResourceId||||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|HistoryMainline|ProductId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|----|----|<site id>||ParentContainerId||||
|CEPdb|HistoryMainline|ParentContainerId||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|HistoryMainline|WorkflowStepId||||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|Container|MfgOrderId||||||
|----|----|<site id>||TxnTypeId||||
|CEPdb|HistoryMainline|TxnType||||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|----|----|<site id>||RecipeId||||
|CEPdb|HistoryMainline|ES_RecipeId||||||
|CEPdb|HistoryMainline|Qty||Quantity||||
|CEPdb|MoveHistory|CycleTime||MoveCycleTime||||
|CEPdb|MoveInHistory|CycleTime||MoveInCycleTime||||
|CEPdb|HistoryMainline|TxnId||Txn||||
|----|----|<site id>||LaborId||||
|CEPdb|HistoryMainline|EmployeeId||||||
|CEPdb|HistoryMainline|StepPass||ContainerStepPass||||
||||~~**ContainerOperationAssembly**~~|||||
|----|----|<site id>||ContainerOperationAssemblySiteId||||
|CEPdb|IssueActualsHistory|IssueActualsHistoryId||ContainerOperationAssemblyKey||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
|----|----|<site id>||AssembledContainerId||||
|CEPdb|Container,IssueActualsHistory|ContainerId or FromContainerId||||||
|----|----|<site id>||AssembledMaterialDefinitionId||||
|CEPdb|Container,Product,IssueActualsHistory|ProductId or FromLot||||||
|----|----|<site id>||Assembled2ContainerId||||
|CEPdb|Container,IssueActualsHistory|ContainerId or FromContainerId||||||
|----|----|<site id>||Assembled2MaterialDefinitionId||||
|CEPdb|Container,Product,IssueActualsHistory|ProductId or ES_FromLot2||||||
|----|----|<site id>||Assembled3ContainerId||||
|CEPdb|Container,IssueActualsHistory|ContainerId or FromContainerId||||||
|----|----|<site id>||Assembled3MaterialDefinitionId||||
|CEPdb|Container,Product,IssueActualsHistory|ProductId or ES_FromLot3||||||
|----|----|<site id>||AssembledOnContainerId||||
|CEPdb|HistoryMainline|ParentContainerId or ContainerId||||||
|----|----|<site id>||AssembledOnMaterialDefinitionId||||
|CEPdb|Container|ProductId||||||
|----|----|<site id>||ContainerOperationStatusId||||
|----|----|'FAIL' or 'PASS'||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|HistoryMainline|ResourceId||||||
|----|----|<site id>||PartNumberMaterialDefinitionId||||
|CEPdb|IssueHistoryDetail|ProductId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|----|----|<site id>||ReferenceDesignatorId||||
|CEPdb|IssueActualsHistory|ReferenceDesignator||||||
|----|----|<site id>||SubAssembledOnContainerId||||
|CEPdb|HistoryMainline|ContainerId or null||||||
|----|----|<site id>||SubAssembledOnMaterialDefinitionId||||
|CEPdb|HistoryMainline|ProductId||||||
|----|----|<site id>||TxnTypeId||||
|CEPdb|HistoryMainline|TxnType||||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|----|----|<site id>||RecipeId||||


|CEPdb|HistoryMainline|ES_RecipeId|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CEPdb|HistoryMainline|TxnId||Txn||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|Container|MfgOrderId||||||
||||~~**ContainerOperationDisassociate**~~|||||
|----|----|<site id>||ContainerOperationDisassociateSiteId||||
|CEPdb|DisassociateHistoryChildCnts|DisassociateHistoryId+'-'+Sequence||ContainerOperationDisassociateKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|DisassociateHistoryChildCnts|ChildContainersId||||||
|----|----|<site id>||ParentContainerId||||
|CEPdb|DisassociateHistory|ParentContainerId||||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
|CEPdb|HistoryMainline|TxnId||Txn||||
|CEPdb|DisassociateHistoryChildCnts|Sequence||Sequence||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
||||~~**ContainerOperationStatus**~~|||||
|----|----|<site id>||ContainerOperationStatusSiteId||||
|----|----|'FAIL' or 'PASS'||ContainerOperationStatusKey||||
|----|----|'FAIL' or 'PASS'||Name||||
|----|----|'FAIL' or 'PASS'||Description||||
||||~~**ContainerProperty**~~|||||
|----|----|<site id>||ContainerPropertySiteId||||
|----|----|"X_Out" or "FactoryStartDate"||ContainerPropertyKey|CONTAINERPROPERTY|||
||----|"X_Out" or "FactoryStartDate"||Name||||
|----|----|----||Description||||
||----|"String" or "DateTime"||PropertyTypeKey||||
||----|----||UomKey||||
||||~~**ContainerPropertyStaticValue**~~|||||
|----|----|<site id>||ContainerPropertyStaticValueSiteId||||
|CEPdb|Container|ContainerId + '_X_Out' or<br>ContainerId + '_FactoryStartDate'||ContainerPropertyStaticValueKey|CONTAINERPROPERTYSTATICVALUE|||
|----|----|<site id>||ContainerId||||
|CEPdb|Container|ContainerId||||||
|----|----|<site id>||ContainerPropertyId||||
|----|----|"X_Out" or "FactoryStartDate"||||||
|CEPdb|Container|ES_XOUT||StringValue||||
|----|----|----||FloatValue||||
|CEPdb|Container|FactoryStartDate||DatetimeValue||||
|----|----|----||Sequence||||
||||~~**ContainerStatus**~~|||||
|----|----|<site id>||ContainerStatusSiteId|CONTAINER|||
|----|----|0 or 1 or 2 or 3 or 4||ContainerStatusKey||||
|----|----|Deleted or Open or Closed or In transit or Issued||Name||||
|----|----|----||Description||||
||||~~**Customer**~~|||||
|----|----|<site id>||CustomerSiteId||||
|CEPdb|Customer|CustomerId||CustomerKey||||
|CEPdb|Customer|CustomerName||Name||||
|CEPdb|Customer|Description||Description||||
||||~~**Defect**~~|||||
|----|----|<site id>||DefectSiteId||||
|CEPdb|isDefectHistoryDetail|isGUID||DefectKey|PRODUCTION EVENT / GENERIC EVENT|Container -> Record Production Event OR Event ->  Record<br>Generic Event||
|CEPdb|isDefectHistoryDetail|isGUID||Name||Manage Production Event||
|----|----|----||Description||||
|----|----|<site id>||NonConformanceId||||
|----|----|----||||||
|----|----|1||Quantity||||
||||~~**DefectBoardSide**~~|||||
|----|----|<site id>||~~DefectBoardSideSiteId~~<br>||||
|----|----|0 or 1 or 2 or 3||~~DefectBoardSideKey~~<br>|~~DEFECTBOARDSIDE~~|||
|----|----|Top or Bottom or Both or None||~~Name~~<br>||||
|----|----|----||~~Description~~||||
||||~~**DefectClass**~~|||||
|----|----|----||DefectClassSiteId||||
|----|----|----||DefectClassKey|PRODUCTION EVENT / GENERIC EVENT|Container -> Record Production Event OR Event -> Record<br>Generic Event||
|----|----|----||Name||||
||||~~**DefectDefectClass**~~|||||
|----|----|----||DefectDefectClassSiteId||||
|----|----|----||DefectDefectClassKey|PRODUCTION EVENT / GENERIC EVENT|Container -> Record Production Event OR Event -> Record<br>Generic Event||
|----|----|----||DefectId||Manage Production Event||
|----|----|----||||||
|----|----|----||DefectClassId|FAILURE MODE|Modeling -> Modeling -> Failure Mode||
|----|----|----||||||
||||~~**DefectHistory**~~|||||
|----|----|<site id>||DefectHistorySiteId||||
|CEPdb|isDefectHistoryDetail|isDefectHistoryDetailId||DefectHistoryKey|DEFECTHISTORY|||
|----|----|<site id>||ContainerId||||
|CEPdb|isDefectHistoryDetail|ContainerId||||||
|CEPdb|HistoryMainline|Qty||ContainerQuantity||||
|CEPdb|HistoryMainline|StepPass||ContainerStepPass||||
|CEPdb|isDefectHistoryDetail|isCreateDate||CreateDate||||
|----|----|<site id>||DefectBoardSideId||||
|CEPdb|isDefectHistoryDetail|ES_BoardSide||||||
|----|----|<site id>||DefectId||||
|CEPdb|isDefectHistoryDetail|isGUID||||||
|----|----|<site id>||DefectLocationId||||


|CEPdb|isDefectHistoryDetail|isRefDes|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|<site id>||DefectPinLocationId||||
|CEPdb|isDefectHistoryDetail|ES_Pin||||||
|----|----|<site id>||DefectReasonId||||
|CEPdb|isDefectHistoryDetail|isDefectReasonId||||||
|----|----|<site id>||DefectRepairActionId||||
|CEPdb|isRepairActionHistDetails|isRepairActionId||||||
|----|----|<site id>||DefectSeverityId||||
|CEPdb|isDefectHistoryDetail|isSeverityId||||||
|----|----|<site id>||DefectStatusId||||
|CEPdb|isDefectHistoryDetail|isStatus||||||
|----|----|<site id>||DefectSymptomId||||
|CEPdb|isDefectHistoryDetail|ES_Symptom||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|isDefectHistoryDetail|isResourceId||||||
|----|----|<site id>||FactorySiteId||||
|CEPdb|HistoryMainline|FactoryId||||||
|----|----|<site id>||FromContainerMaterialDefinitionId||||
|CEPdb|HistoryMainline|ProductId||||||
|----|----|<site id>||FromDefectMaterialDefinitionId||||
|CEPdb|isDefectHistoryDetail|isProductId||||||
|----|----|<site id>||InspectLaborId||||
|CEPdb|isDefectHistoryDetail|isInspectUserId||||||
|CEPdb|HistoryMainline|isFailed||IsFailed||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|isDefectHistoryDetail|isMfgOrderId||||||
|----|----|<site id>||OperationId||||
|CEPdb|isDefectHistoryDetail|isOperationId||||||
|CEPdb|isDefectHistoryDetail|isRepairDate||RepairDate||||
|----|----|<site id>||RepairLaborId||||
|CEPdb|isDefectHistoryDetail|isRepairUserId||||||
|----|----|<site id>||ReplacedContainerId||||
|CEPdb|isDefectHistoryDetail|isContainerId||||||
|----|----|<site id>||SpecId||||
|CEPdb|isDefectHistoryDetail|isSpecId||||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|CEPdb|isDefectHistoryDetail|isUpdateDate||UpdateDate||||
|----|----|<site id>||WorkflowId||||
|CEPdb|isDefectHistoryDetail|isWorkflowId||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|isDefectHistoryDetail|isWorkflowStepId||||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
|CEPdb|HistoryMainline|TxnId||Txn||||
||||~~**DefectLocation**~~|||||
|----|----|<site id>||DefectLocationSiteId||||
|CEPdb|isDefectHistoryDetail|isRefDes||DefectLocationKey|DEFECTLOCATION|||
|CEPdb|isDefectHistoryDetail|isRefDes||Name||||
|----|----|----||Description||||
||||~~**DefectPinLocation**~~|||||
|----|----|<site id>||DefectPinLocationSiteId||||
|CEPdb|isDefectHistoryDetail|ES_Pin||DefectPinLocationKey|DEFECTPINLOCATION|||
|CEPdb|isDefectHistoryDetail|ES_Pin||Name||||
|----|----|----||Description||||
||||~~**DefectReason**~~|||||
|----|----|<site id>||DefectReasonSiteId||||
|CEPdb|isDefectReason|isDefectReasonId||DefectReasonKey|DEFECTREASON|||
|CEPdb|isDefectReason|isDefectReasonName||Name||||
|CEPdb|isDefectReason|Description||Description||||
||||~~**DefectRepairAction**~~|||||
|----|----|<site id>||DefectRepairActionSiteId||||
|CEPdb|isRepairAction|isRepairActionId||DefectRepairActionKey|DEFECTREPAIRACTION|||
|CEPdb|isRepairAction|isRepairActionName||Name||||
|CEPdb|isRepairAction|Description||Description||||
|CEPdb|isRepairAction|isRequiresReplacement||isRequiresReplacement||||
||||~~**DefectSeverity**~~|||||
|----|----|<site id>||DefectSeveritySiteId||||
|CEPdb|isDefectSeverity|isDefectSeverityId||DefectSeverityKey|DEFECTSEVERITY|||
|CEPdb|isDefectSeverity|isDefectSeverityName||Name||||
|CEPdb|isDefectSeverity|Description||Description||||
||||~~**DefectStatus**~~|||||
|----|----|<site id>||DefectStatusSiteId||||
|----|----|0 or 1 or 2||DefectStatusKey|DEFECTSTATUS|||
|----|----|"Open defect" or "Defect repaired" or "NFF (Not Fault Found)"||Name||||
|----|----|----||Description||||
||||~~**DefectSymptom**~~|||||
|----|----|<site id>||DefectSymptomSiteId||||
|CEPdb|isDefectHistoryDetail|ES_Symptom||DefectSymptomKey|DEFECTSYMPTOM|||
|CEPdb|isDefectHistoryDetail|ES_Symptom||Name||||
|----|----|----||Description||||
||||~~**Equipment**~~|||||
|----|----|<site id>||EquipmentSiteId||||
|CEPdb|ResourceDef|ResourceId||EquipmentKey|RESOURCE|Modeling -> Modeling -> Resource (Resource field)||
|CEPdb|ResourceDef|ResourceName||Name||||
||||~~**EquipmentClass**~~|||||
|----|----|<site id>||EquipmentClassSiteId||||
|CEPdb|ResourceFamily|ResourceFamilyId||EquipmentClassKey|RESOURCE FAMILY|Modeling -> Modeling -> Resource Family (Resource Family<br>field)||
|CEPdb|ResourceFamily|ResourceFamilyName||Name||||
||||~~**EquipmentEquipmentClass**~~|||||
|----|----|<site id>||EquipmentEquipmentClassSiteId||||


|CEPdb|ResourceDef, ResourceFamily|ResourceDef.ResourceId + "_" + ResourceFamily.ResourceFamilyId|Col4|EquipmentEquipmentClassKey|Col6|Modeling -> Modeling -> Resource (Resource field)<br>Modeling -> Modeling -> Resource Family (Resource Family<br>field)<br>Event -> Record Generic Event or Container -> Record<br>Production Event|Resource / Resource family association|
|---|---|---|---|---|---|---|---|
|----|----|<site id>||EquipmentId|RESOURCE|Modeling -> Modeling -> Resource (Resource field)||
|CEPdb|ResourceDef|ResourceDef.ResourceId||||||
|----|----|smallint||EquipmentClassId|RESOURCE FAMILY|Modeling -> Modeling -> Resource Family (Resource Family<br>field)<br>Event -> Record Generic Event or Container -> Record<br>Production Event||
|CEPdb|ResourceFamily|ResourceFamily.ResourceFamilyId||||||
||||~~**EquipmentHierarchy**~~|||||
|----|----|<site id>||EquipmentHierarchySiteId||||
|CEPdb|ResourceDef|ResourceId||EquipmentHierarchyKey|RESOURCE|Modeling -> Modeling -> Resource (Resource field)||
|----|----|smallint||EquipmentId||||
|CEPdb|ResourceDef|ResourceId||||||
|----|----|smallint||ParentEquipmentId||||
|CEPdb|ResourceDef|ParentResourceId||||Modeling -> Modeling -> Resource (Parent Resource field)||
||||~~**EquipmentProperty**~~|||||
|----|----|<site id>||~~EquipmentPropertySiteId~~<br>||||
|----|----|"Index" or "NumberOfLanes"||~~EquipmentPropertyKey~~<br>|~~EQUIPMENTPROPERTY~~|||
|----|----|'"Index" or "NumberOfLanes"||~~Name~~<br>||||
|----|----|----||~~Description~~<br>||||
|----|----|Numeric||~~PropertyTypeKey~~<br>||||
|----|----|----||~~UomKey~~||||
||||~~**EquipmentPropertyStaticValue**~~|||||
|----|----|<site id>||~~EquipmentPropertyStaticValueSiteId~~<br>||||
|CEPdb|ResourceDef|ResourceId + "_Index'" or ResourceId + "_NumberOfLanes"||~~EquipmentPropertyStaticValueKey~~|~~EQUIPMENTPROPERTYSTATICVALUE~~|||
|----|----|<site id>||EquipmentId||||
|CEPdb|ResourceDef|ResourceId||||||
|----|----|<site id>||EquipmentPropertyId||||
|||'"Index" or "NumberOfLanes"||||||
|----|----|----||~~DatetimeValue~~<br>||||
|CEPdb|ResourceDef|ES_ResourceIndex or ES_NumberOfLanes||~~FloatValue~~<br>||||
|----|----|----||~~Sequence~~<br>||||
|----|----|----||~~StringValue~~||||
||||~~**EquipmentTimeCategory**~~|||||
|----|----|<site id>||EquipmentTimeCategorySiteId||||
|----|----|1 or 2 or 3 or 4 or 5 or 6 or Undefined||EquipmentTimeCategoryKey|RESOURCE STATE|||
|----|----|Nonscheduled Time or Nonscheduled Downtime or Scheduled Downtime or<br>Engineering Time or Productive Time or Standby Time or Undefined||Name||||
|----|----|null||Description||||
||||~~**EquipmentTimeModel**~~|||||
|----|----|<site id>||EquipmentTimeModelSiteId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|ResourceStatusHistoryId<br>'Actual_' + ProductionStatusId||EquipmentTimeModelKey|RESOURCE STATUS HISTORY union<br>PRODUCTION STATUS|Resource -> Resource Set Up - generates<br>ResourceStatusHistory||
|----|----|smallint||EquipmentTimeCategoryId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceState<br>ResourceState||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|HistoryMainline<br>ProductionStatus|ResourceId||||||
|----|----|<site id>||ReasonTreeItemId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceState + OldResourceStatusCodeId + OldResourceStatusReasonCodeId<br>ResourceState + StatusId + ReasonId||||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldLastStatusChangeDateGMT<br>LastStatusChangeDateGMT||StartDateTime||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|LastStatusChangeDateGMT<br>null||EndDateTime||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|datediff(second,[OldLastStatusChangeDateGMT], [LastStatusChangeDateGMT])<br>null||Duration||||
||||~~**Factory**~~|||||
|----|----|<site id>||~~FactorySiteId~~<br>||||
|CEPdb|Factory|FactoryId||~~FactoryKey~~<br>|~~FACTORY~~|||
|CEPdb|Factory|FactoryName||~~Name~~<br>||||
|CEPdb|Factory|Description||~~Description~~||||
||||~~**FunctionalCode**~~|||||
|----|----|<site id>||~~FunctionalCodeSiteId~~<br>||||
|CEPdb|ProductType|ProductTypeId||~~FunctionalCodeKey~~<br>|~~FUNCTIONALCODE~~|||
|CEPdb|ProductType|ProductTypeName||~~Name~~<br>||||
|CEPdb|ProductType|Description||~~Description~~||||
||||~~**Indicator**~~|||||
|----|----|<site id>||~~IndicatorSiteId~~||||
|----|----|GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime||IndicatorKey|SUMMARY TABLE|||
|----|----|GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime||Name<br>||||
|----|----|null||~~Description~~<br>||||
|CEPdb|isOEERawDetails|Uom or Uom2||~~UomId~~||||
||||~~**IndicatorClass**~~|||||
|----|----|<site id>||~~IndicatorClassSiteId~~<br>||||
|----|----|Counter||~~IndicatorClassKey~~<br>||||
|----|----|Counter||~~Name~~<br>||||
|----|----|Counter||~~Description~~||||
||||~~**IndicatorIndicatorClass**~~|||||
|----|----|<site id>||~~IndicatorIndicatorClassSiteId~~||||
|----|----|(GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime) + _Counter||IndicatorIndicatorClassKey||||
|----|----|<site id>||IndicatorClassId||||


|----|----|Counter|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|<site id>||IndicatorId||||
|----|----|GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime||||||
||||~~**IndicatorValue**~~|||||
|----|----|<site id>||IndicatorValueSiteId||||
|CEPdb|isOEERawDetails|isOEERawDetailsId + _+ (GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or<br>SecondaryLossQty or SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime)||IndicatorValueKey|SUMMARY TABLE|||
|----|----|<site id>||EquipmentId||||
|CEPdb|isOEERawDetails|ResourceId||||||
|----|----|<site id>||IndicatorId||||
|----|----|GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime||||||
|CEPdb|isOEERawDetails|GoodQty or GoodQty2 or IdealCycleTime*60 or LossQty or LossQty2 or ReworkedQty or<br>ReworkedQty2 or TotalQty or TotalQty2||Value||||
|CEPdb|isOEERawDetails|TxnDateGMT||StartDateTime||||
|CEPdb|isOEERawDetails|TxnDateGMT||EndDateTime||||
|----|----|null||Duration||||
||||~~**Labor**~~|||||
|----|----|<site id>||LaborId|EMPLOYEE|Modeling -> Modeling -> Employee<br>Event -> Record Generic Event or Container -> Record||
|CEPdb|Employee|EmployeeId||||||
|CEPdb|Employee|EmployeeName||Name||||
|CEPdb|Employee|Description||Description||||
||||~~**Location**~~|||||
|----|----|<site id>||LocationSiteId|LOCATION|||
|CEPdb|Location|LocationId||LocationKey||||
|CEPdb|Location|LocationName||Name||||
|CEPdb|Location|Description||Description||||
||||~~**MaterialClass**~~|||||
|----|----|<site id>||MaterialClassSiteId||||
|CEPdb|ProductFamily|ProductFamilyId||MaterialClassKey|PRODUCT FAMILY|Modeling -> Modeling -> Product Family<br>Event -> Record Generic Event or Container -> Record<br>Production Event<br>Container -> Hold<br>Container -> Rework||
|CEPdb|ProductFamily|ProductFamilyName||Name||||
||||~~**MaterialDefinition**~~|||||
|----|----|<site id>||MaterialDefinitionSiteId||||
|CEPdb|Product,IssueActualsHistory|ProductId or FromLot or ES_FromLot2 or ES_FromLot3||MaterialDefinitionKey|PRODUCT|Modeling -> Modeling -> Product||
|----|----|<site id>||MountingTechnologyId||||
|CEPdb|Product|ES_MountingTechnology||||||
|CEPdb|ProductBase,IssueActualsHistory|ProductName or FromLot or ES_FromLot2 or ES_FromLot3||Name||||
|CEPdb|Product|Description or null||Description||||
|----|----|<site id>||FunctionalCodeId||||
|CEPdb|Product|ProductTypeId or null||||||
||||~~**MaterialDefinitionBillOfMaterial**~~|||||
|----|----|<site id>||MaterialDefinitionBillOfMaterialSiteId||||
|CEPdb|Product|ProductId||MaterialDefinitionBillOfMaterialKey||||
|----|----|<site id>||BillOfMaterialId||||
|CEPdb|BOM|BOMId||||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|Product|ProductId||||||
||||~~**MaterialDefinitionMaterialClass**~~|||||
|----|----|<site id>||MaterialDefinitionMaterialClassSiteId||||
|CEPdb|Product, ProductFamily|ProductId + "_" + ProductFamilyId||MaterialDefinitionMaterialClassKey|PRODUCT FAMILY|Modeling -> Modeling -> Product Family|Product / Product Familiy association|
|----|----|<site id>||MaterialDefinitionId|PRODUCT|||
|CEPdb|Product|ProductId||||||
|----|----|<site id>||MaterialClassId||||
|CEPdb|ProductFamily|ProductFamilyId||||||
||||~~**MaterialDefinitionPropertyStaticValue**~~|||||
|----|----|<site id>||MaterialDefinitionPropertyStaticValueSiteId||||
|CEPdb|Product|ProductId + '_Revision' OR ProductId +'_BOMRevision' OR ProductId +'_CurrentCost' OR ProductId<br>+'_CustomerName' OR ProductId +'_CustomerProductNumber' OR ProductId +'_PinCount' OR<br>ProductId +'_ProductVariation' OR  ProductId +'_Revision' OR ProductId +'_StandardCost'||MaterialDefinitionPropertyStaticValueKey|PRODUCT|||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|Product|ProductId||||||
|----|----|<site id>||MaterialPropertyId||||
|----|----|"Revision" OR "BOMRevision" OR "CurrentCost" OR "CustomerName" OR "CustomerProductNumber"<br>OR "PinCount" OR "ProductVariation" OR "Revision" OR "StandardCost"||||||
|CEPdb|Product, Customer, Bom|ProductRevision OR ProductVariation OR CustomerName OR BOMRevision OR<br>CustomerProductNumber||StringValue||||
|CEPdb|Product|CurrentCost OR StdCost OR ES_PinCount||FloatValue||||
|----|----|----||DatetimeValue||||
|----|----|----||Sequence||||
||||~~**MaterialLot**~~|||||
|----|----|<site id>||MaterialLotSiteId||||
|CEPdb|Eventlot|EventLotId||MaterialLotKey|EVENT / EVENT LOT|Event -> Record Generic Event or Container -> Record<br>Production Event||
|CEPdb|Eventlot, EventData|Lot or Eventlot.OperationName or EventData.OperationName||Name||Container -> Start||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|Product|ProductId||||||
|CEPdb|EventLot|Qty||Quantity||||
|CEPdb|EventLot|UOMName||UomId||||
|CEPdb|EventLot|OriginalStartDate||ValidFromDateTime||||
||||~~**MaterialProperty**~~|||||
|----|----|<site id>||~~MaterialPropertySiteId~~||||


|----|----|"Revision" OR "BOMRevision" OR "CurrentCost" OR "CustomerName" OR "CustomerProductNumber"<br>OR "PinCount" OR "ProductVariation" OR "Revision" OR "StandardCost"|Col4|MaterialPropertyKey|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|"Revision" OR "BOMRevision" OR "CurrentCost" OR "CustomerName" OR "CustomerProductNumber"<br>OR "PinCount" OR "ProductVariation" OR "Revision" OR "StandardCost"||Name<br>||||
|----|----|----||~~Description~~<br>||||
|----|----|"String" OR "Numeric"||~~PropertyTypeKey~~<br>||||
|----|----|----||~~UomKey~~||||
||||~~**MountingTechnology**~~|||||
|----|----|<site id>||~~MountingTechnologySiteId~~<br>||||
|CEPdb|CDOFields|DefaultValue||~~MountingTechnologyKey~~<br>||||
|CEPdb|CDOFields|FieldName||~~Name~~<br>||||
|CEPdb|CDOFields|FieldDescription||~~Description~~||||
||||~~**NonConformance**~~|||||
|----|----|<site id>||NonConformanceSiteId||||
|CEPdb|Event,Eventlot|EventDataId + '_' + Lot||NonConformanceKey|RECORD PRODUCTION EVENT|Container -> Record Production Event||
|CEPdb|Event|EventName||Name||Defaulted by Modeling -> Modeling -> Numbering Rule and<br>Modeling -> Modeling -> Organization (Numbering Rule<br>Map)||
|CEPdb|Event|Description||Description||Record Production Event (Description)||
|----|----|<site id>||NonConformanceStatusId||||
|CEPdb|StatusField|StatusField.FieldID||||||
|CEPdb|Event|ReportedDateGMT||StartDateTime||Record Production Event (Occurrence Date & Time)||
|CEPdb|Event|CloseDateGMT||EndDateTime||Set when Record Production Event is closed||
|----|----|----||Duration|MANAGE EVENT|Search -> Quality Search -> Manage Records||
|----|----|<site id>||EquipmentId|RESOURCE|Record Production Event (Resource)||
|CEPdb|ResourceDef|ResourceDef.ResourceId||||||
|----|----|<site id>||MaterialDefinitionId|EVENT LOT|Container -> Start -> Product||
|CEPdb|Product|ProductId||||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|Container|mfgOrderId||||||
|----|----|----||OperationResponseId||||
|----|----|----||||||
|----|----|<site id>||MaterialLotId||Container -> Record Production Event or Manage Event||
|CEPdb|EventLot|EventLotId||||||
|----|1|float||InspectedQuantity||||
|----|1|float||NonConformantQuantity||||
||||~~**NonConformanceProperty**~~|||||
|----|----|<site id>||NonConformancePropertySiteId||||
|----|----|'PriorityLevel','Owner','InitiatorOrganization','OccurrenceDate','DiscoveryArea','SubClassification','Clas<br>sification','Organization','Reporter','ReporterOrganization','Initiator','Role','ResolutionCode','CloseDes<br>cription','ClosedBy','Category'||NonConformancePropertyKey|RECORD PRODUCTION EVENT|Container -> Record Production Event||
|----|----|'PriorityLevel','Owner','InitiatorOrganization','OccurrenceDate','DiscoveryArea','SubClassification','Clas<br>sification','Organization','Reporter','ReporterOrganization','Initiator','Role','ResolutionCode','CloseDes<br>cription','ClosedBy','Category'||Name|MANAGE EVENT|Search -> Quality Search -> Manage Records|'PriorityLevel','Owner','InitiatorOrganization','Occurrenc<br>eDate','DiscoveryArea','SubClassification','Classification',<br>'Organization','Reporter','ReporterOrganization','Initiato<br>r','Role','ResolutionCode','CloseDescription','ClosedBy','<br>Category'|
|----|----|'String' or 'DateTime'||PropertyTypeId||||
|----|----|'n/a'||UomId||||
||||~~**NonConformancePropertyStaticValue**~~|||||
|----|----|<site id>||NonConformancePropertyStaticValueSiteId||||
|CEPdb|Event|Event.EventDataId+' 'EventLot.Lot<br> (refer to bm20private.<br>NonConcofomarceProperty)||NonConformancePropertyStaticValueKey||||
|----|----|<site id>||NonConformanceId||||
|CEPdb|Event|Event.EventDataId+' 'EventLot.Lot||||||
|CEPdb|Event|<site id>||NonConformancePropertyId|RECORD PRODUCTION EVENT|Container -> Record Production Event||
|----|----|nvarchar||||||
|CEPdb|UnPvt|[Classification], [SubClassification], [DiscoveryArea], [Organization], [Owner], [PriorityLevel],<br>[Reporter], [ReporterOrganization],[Initiator], [InitiatorOrganization], [Role], [ResolutionCode],<br>[CloseDescription], [ClosedBy], [Category])||StringValue|MANAGE EVENT|Search -> Quality Search -> Manage Records||
|CEPdb|UnPvt|OccurrenceDate||DatetimeValue||Record Production Event (Occurrence Date & Time)||
||||~~**NonConformanceStatus**~~|||||
|CEPdb|----|<site id>||NonConformanceStatusSiteId||||
|CEPdb|CDOFields|FieldID||NonConformanceStatusKey|MANAGE EVENT|Search -> Quality Search -> Manage Records (Status field)||
|CEPdb|CDOFields|FieldName||Name||||
||||~~**Operation**~~|||||
|CEPdb|----|<site id>||~~OperationSiteId~~<br>||||
|CEPdb|Operation|OperationId||~~OperationKey~~<br>||||
|CEPdb|Operation|OperationName||~~Name~~<br>||||
|CEPdb|Operation|Notes||~~Description~~||||
||||~~**OperationExecution**~~|||||
|----|----|<site id>||OperationExecutionSiteId||||
|CEPdb|MfgOrder|MfgOrderId||OperationExecutionKey||||
|CEPdb|MfgOrder|MfgOrderName||Name|MFG ORDER|Modeling -> Modeling -> Mfg Order (Mfg Order field)||
|CEPdb|MfgOrder|Description||Description||Modeling -> Modeling -> Mfg Order (Description field)||
|----|----|<site id>||OperationExecutionStatusId||||
|CEPdb|MfgOrder|OrderStatusId||||||
|----|----|----||EquipmentId||||
|----|----|----||||||
|----|----|<site id>||MaterialDefinitionId||Modeling -> Modeling -> Mfg Order (Product field)||
|CEPdb|Product,ProductBase|ProductId or RevOfRcdId||||||
|----|----|----||BillOfMaterialId||||
|----|----|----||||||
|----|----|<site id>||OperationSchedulingId||||
|----|----|nvarchar||||||
|CEPdb|MfgOrder|qty||ProducedQuantity||Modeling -> Modeling -> Mfg Order (Quantity field)||
|----|----|----||ReworkedQuantity<br>||||
|----|----|----||~~ScrapQuantity~~||||
|CEPdb|Uom|UomName||UomId||Modeling -> Modeling -> Mfg Order (UOM field)||
|CEPdb|MfgOrder|PlannedStartDateGMT||StartDateTime||Modeling -> Modeling -> Mfg Order (Planned Start Date<br>field)||


|CEPdb|MfgOrder|PlannedCompletionDateGMT|Col4|EndDateTime|Col6|Modeling -> Modeling -> Mfg Order (Planned Completion<br>Date field)|Col8|
|---|---|---|---|---|---|---|---|
|----|----|float||~~Duration~~||||
|----|----|<site id>||WorkflowId||||
|CEPdb|WorkflowBase,Product|RevOfRcdId or WorkflowId||||||
||||~~**OperationExecutionStatus**~~|||||
|----|----|<site id>||OperationExecutionStatusSiteId||||
|CEPdb|OrderStatus|OrderStatusId||OperationExecutionStatusKey|ORDER STATUS|Modeling -> Order Status||
|CEPdb|OrderStatus|OrderStatusName||Name||||
|CEPdb|OrderStatus|Description||Description||||
||||~~**OperationResponse**~~|||||
|----|----|<site id>||~~OperationResponseSiteId~~<br>|SUMMARY TABLE|||
|CEPdb|isOEERawDetails|OperationId + '_' + MfgOrderId + '_' + ResourceId||~~OperationResponseKey~~<br>|~~OperationResponseKey~~<br>|~~OperationResponseKey~~<br>|~~OperationResponseKey~~<br>|
|CEPdb|isOEERawDetails|OperationName||~~Name~~<br>||||
|----|----|----||~~Description~~|~~Description~~|~~Description~~|~~Description~~|
|----|----|----||EquipmentId||||
|----|----|----||||||
|----|----|----||MaterialDefinitionId||||
|----|----|----||||||
|----|----|----||OperationDefinitionId||||
|----|----|----||||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|isOEERawDetails|MfgOrderId||||||
|----|----|----||OperationRequestId||||
|----|----|----||||||
|----|----|----||OperationResponseStatusId||||
|----|----|----||||||
|----|----|----||~~UomId~~<br>||||
|----|----|----||~~ProducedQuantity~~<br>||||
|----|----|----||~~ReworkedQuantity~~<br>||||
|----|----|----||~~ScrapQuantity~~<br>||||
|----|----|----||~~Sequence~~<br>||||
|CEPdb|MfgOrder|min(PlannedStartDateGMT)||~~StartDateTime~~<br>||||
|CEPdb|MfgOrder|max(PlannedCompletionDateGMT)||~~EndDateTime~~<br>||||
|---|----|----||~~Duration~~||||
||||~~**OperationResponseEquipmentSpecification**~~|||||
|---|----|<site id>||~~OperationResponseEquipmentSpecificationSiteId~~<br>|~~SUMMARY TABLE~~|||
|CEPdb|isOEERawDetails|OperationId + '_' + MfgOrderId + '_' + ResourceId + '_' + TxnDateGMT||~~OperationResponseEquipmentSpecificationKey~~<br>||||
|---|----|<site id>||~~EquipmentId~~||||
|CEPdb|isOEERawDetails|ResourceId||||||
|---|----|<site id>||OperationResponseId||||
|CEPdb|isOEERawDetails|OperationId + '_' + MfgOrderId + '_' + ResourceId||||||
|----|----|----||~~Quantity~~<br>||||
|CEPdb|isOEERawDetails|TxnDateGMT||~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|~~StartDateTime~~<br>|
|CEPdb|isOEERawDetails|TxnDateGMT + (ProcessTime or QueueTime)*24*60*60||~~EndDateTime~~<br>||||
|----|----|----||~~Duration~~|~~Duration~~|~~Duration~~|~~Duration~~|
||||~~**Owner**~~|||||
|----|----|<site id>||~~OwnerSiteId~~<br>||||
|CEPdb|Owner|OwnerName||~~OwnerKey~~<br>||||
|CEPdb|Owner|OwnerName||~~Name~~<br>||||
|CEPdb|Owner|Description||~~Description~~||||
||||~~**PropertyType**~~|||||
|----|----|"String" or "Numeric" or "DateTime"||PropertyTypeKey||||
|----|----|"String" or "Numeric" or "DateTime"||Name||||
||||~~**QualityLimit**~~|||||
|----|----|<site id>||QualityLimitSiteId||||
|CEPdb|DataPoint|DataPointId||QualityLimitKey|MODELING -> USER DATA COLLECTION DEFINITION|Modeling -> Modeling -> User Data Collection Def (Data||
|----|----|<site id>||QualityParameterId||||
|CEPdb|DataPoint|DataPointId||||||
|CEPdb|DataPoint|UpperLimit||HighLimit||Upper Limit field when adding to Data Points Grid||
|CEPdb|DataPoint|LowerLimit||LowLimit||Lower Limit field when adding to Data Points Grid||
||||~~**QualityParameter**~~|||||
|----|----|<site id>||QualityParameterSiteId||||
|CEPdb|DataPoint|DataPointId||QualityParameterKey||||
|CEPdb|DataPoint|DataPointName||Name|MODELING -> USER DATA COLLECTION DEFINITION|Modeling -> Modeling -> User Data Collection Def (Data<br>Points Grid)||
|CEPdb|Uom|UOMName||UomId||UOM on Data Points Grid||
||||~~**QualityParameterValue**~~|||||
|----|----|<site id>||QualityParameterValueSiteId||||
|CEPdb|DataPointHistoryDetail|DataPointHistoryDetailId||QualityParameterValueKey|EPROCEDURE|Container -> Eprocedure||
|----|----|<site id>||QualityResponseId||||
|CEPdb|ExecuteTaskHistory|ExecuteTaskHistoryId||||||
|----|----|<site id>||QualityParameterId||Eproc Data Collection or Container -> Collect Data||
|CEPdb|DataPointHistoryDetail|DataPointId||||||
|CEPdb|DataPointHistoryDetail|DataValue or null||FloatValue||||
|CEPdb|DataPointHistoryDetail|DataValue or null||StringValue||||
|CEPdb|HistoryMainline|SystemDateGMT||StartDateTime||||
|CEPdb|HistoryMainline|SystemDateGMT||EndDateTime||||
||||~~**QualityResponse**~~|||||
|----|----|<site id>||QualityResponseSiteId||||
|CEPdb|ExecuteTaskHistory|ExecuteTaskHistoryId||QualityResponseKey|EPROCEDURE|Container -> Eprocedure||
|CEPdb|TaskItem|TaskItemName||Name|MODELING|Modeling -> Modeling -> Task List (Tasks grid)||
|CEPdb|ExecuteTaskHistory|Instruction||Description||||
|----|----|<site id>||OperationResponseId||||
|CEPdb|ExecuteTaskHistory|ExecuteTaskHistoryId||||||
|CEPdb|HistoryMainline|SystemDateGMT||StartDateTime||||
||||~~**QtyAdjustReason**~~|||||
|----|----|<site id>||~~QtyAdjustReasonSiteId~~||||
|CEPdb|LossReason, QtyAdjustReason, BonusReason|LossReasonName OR QtyAdjustReasonName OR BonusReasonName||QtyAdjustReasonKey||||
|CEPdb|LossReason, QtyAdjustReason, BonusReason|LossReasonName OR QtyAdjustReasonName OR BonusReasonName||Name<br>||||
|----|----|----||~~Description~~||||


|Col1|Col2|Col3|Reason|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|<site id>||ReasonSiteId||||
|CEPdb|ResourceStatusReason|ResourceStatusReasonId||ReasonKey|MODELING|Modeling -> Modeling -> Resource Status Reason||
|CEPdb|ResourceStatusReason|ResourceStatusReasonName||Name||||
|CEPdb|ResourceStatusReason|Description||Description||||
|----|----|0||IsStop||||
||||~~**ReasonTree**~~|||||
|----|----|----||ReasonTreeSiteId||||
|----|----|----||ReasonTreeKey||||
|----|----|----||Name||||
|----|----|----||Description||||
||||~~**ReasonTreeItem**~~|||||
|----|----|<site id>||ReasonTreeItemSiteId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceState + OldResourceStatusCodeId + OldResourceStatusReasonCodeId<br>ResourceState + StatusId + ReasonId||ReasonTreeItemKey|MODELING|Modeling -> Modeling -> Resource Status Reason||
|----|----|----||DetailedReasonId||||
|----|----|----||||||
|----|----|<site id>||StatusId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceStatusCodeId<br>StatusId||||||
|----|----|<site id>||ReasonId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceStatusReasonCodeId<br>ReasonId||||||
|----|----|----||CauseId||||
|----|----|----||||||
|----|----|<site id>||EquipmentTimeCategoryId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceState<br>ResourceState||||||
||||~~**Recipe**~~|||||
|----|----|<site id>||RecipeSiteId||||
|CEPdb|HistoryMainline|ES_RecipeId||RecipeKey||||
|CEPdb|HistoryMainline|ES_RecipeId||Name||||
|CEPdb|HistoryMainline|ES_RecipeId||Description||||
||||~~**ReferenceDesignator**~~|||||
|----|----|<site id>||ReferenceDesignatorSiteId||||
|CEPdb|IssueActualsHistory|ReferenceDesignator||ReferenceDesignatorKey||||
|CEPdb|IssueActualsHistory|ReferenceDesignator||Name||||
|CEPdb|IssueActualsHistory|ReferenceDesignator||Description||||
||||~~**ReworkReason**~~|||||
|----|----|<site id>||ReworkReasonSiteId||||
|CEPdb|ReworkReason|ReworkReasonName||ReworkReasonKey||||
|CEPdb|ReworkReason|ReworkReasonName||Name||||
|----|----|----||Description||||
||||~~**Shift**~~|||||
|----|----|<site id>||ShiftSiteId||||
|CEPdb|Shift|ShiftName||ShiftKey||||
|CEPdb|Shift|ShiftName||Name||||
|CEPdb|Shift|Description||Description||||
|----|----|----||StartTime||||
|----|----|----||EndTime||||
|----|----|0||IsDayAfter||||
||||~~**Spec**~~|||||
|----|----|<site id>||SpecSiteId||||
|CEPdb|Spec|SpecId||SpecKey||||
|CEPdb|SpecBase|SpecName||Name||||
|CEPdb|Spec|Description||Description||||
|CEPdb|Spec|SpecRevision||Revision||||
||||~~**Status**~~|||||
|----|----|<site id>|StatusSiteId||RESOURCE STATE|Modeling -> Modeling -> Resource Status Code (Resource||
|CEPdb|ResourceStatusCode|ResourceStatusCodeId|StatusKey|||Also, Resource -> Resource Set Up (Resource Status Code<br>field)||
|CEPdb|ResourceStatusCode|ResourceStatusCodeName|Name|||||
|CEPdb|ResourceStatusCode|Description|Description|||||
|CEPdb|ResourceStatusCode|case when Availability > 1 then 1 else 0|IsStop<br>|||||
||||~~**SummaryTableCompletedWIPSummary**~~|||||
|----|----|<site id>||SummaryTableCompletedWIPSummarySiteId||||
|CEPdb|isCompletedWIPSummary|isCompletedWIPSummaryId||SummaryTableCompletedWIPSummaryKey|SUMMARY TABLE|||
|CEPdb|isCompletedWIPSummary|CalendarDate||CalendarDate||||
|CEPdb|isCompletedWIPSummary|CompletedDate||CompletedDate||||
|CEPdb|isCompletedWIPSummary|CompletedDateGMT||CompletedDateGMT||||
|----|----|<site id>||ContainerId||||
|CEPdb|isCompletedWIPSummary|ContainerId||||||
|----|----|<site id>||LaborId||||
|CEPdb|isCompletedWIPSummary|EmployeeId||||||
|CEPdb|isCompletedWIPSummary|EndQty||EndQty||||
|CEPdb|isCompletedWIPSummary|EndQty2||SecondaryEndQty||||
|----|----|<site id>||FactoryId||||
|CEPdb|isCompletedWIPSummary|FactoryId||||||


|CEPdb|isCompletedWIPSummary|FactoryStartDate|Col4|FactoryStartDate|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CEPdb|isCompletedWIPSummary|FactoryStartDateGMT||FactoryStartDateGMT||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|isCompletedWIPSummary|MfgOrderId||||||
|----|----|<site id>||OperationId||||
|CEPdb|isCompletedWIPSummary|OperationId||||||
|----|----|<site id>||OwnerId||||
|CEPdb|isCompletedWIPSummary|OwnerName||||||
|CEPdb|isCompletedWIPSummary|PastDue||PastDue||||
|CEPdb|isCompletedWIPSummary|PlannedCompletionDate||PlannedCompletionDate||||
|CEPdb|isCompletedWIPSummary|PlannedCompletionDateGMT||PlannedCompletionDateGMT||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|isCompletedWIPSummary|ProductId||||||
|----|----|<site id>||ShiftId||||
|CEPdb|isCompletedWIPSummary|ShiftName||||||
|----|----|<site id>||SpecId||||
|CEPdb|isCompletedWIPSummary|SpecId||||||
|CEPdb|isCompletedWIPSummary|StartQty||StartQty||||
|CEPdb|isCompletedWIPSummary|StartQty2||SecondaryStartQty||||
|CEPdb|isCompletedWIPSummary|TimePassedCompletionDate||TimePassedCompletionDate||||
|----|----|<site id>||TxnTypeId||||
|CEPdb|isCompletedWIPSummary|TxnType||||||
|CEPdb|isCompletedWIPSummary|UOMName||UomId||||
|CEPdb|isCompletedWIPSummary|UOM2Name||SecondaryUomId||||
|----|----|<site id>||WorkflowId||||
|CEPdb|isCompletedWIPSummary|WorkflowId||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|isCompletedWIPSummary|WorkflowStepId||||||
|CEPdb|isCompletedWIPSummary|datediff(SECOND, FactoryStartDateGMT, CompletedDateGMT)||ManufacturingCycleTime||||
|CEPdb|Container|PlannedQty||PlannedQty||||
|CEPdb|MfgOrder|Qty||MfgOrderPlannedQty||||
|CEPdb|Uom|UomName||PlannedQtyUomKey||||
|CEPdb|Uom|UomName||MfgOrderPlannedQtyUomKey||||
||||~~**SummaryTableOEERawDetails**~~|||||
|----|----|<site id>||SummaryTableOEERawDetailsSiteId||||
|CEPdb|isOEERawDetails|isOEERawDetailsId||SummaryTableOEERawDetailsKey|SUMMARY TABLE|||
|CEPdb|isOEERawDetails|CalendarDate||CalendarDate||||
|----|----|<site id>||ContainerId||||
|CEPdb|isOEERawDetails|ContainerId||||||
|CEPdb|isOEERawDetails|CycleStartGMT||CycleStartGMT||||
|CEPdb|isOEERawDetails|CycleTime||CycleTime||||
|----|----|<site id>||LaborId||||
|CEPdb|isOEERawDetails|EmployeeId||||||
|----|----|<site id>||FactoryId||||
|CEPdb|isOEERawDetails|FactoryId||||||
|CEPdb|isOEERawDetails|GoodQty||GoodQty||||
|CEPdb|isOEERawDetails|GoodQty2||SecondaryGoodQty||||
|CEPdb|isOEERawDetails|IdealCycleTime||IdealCycleTime||||
|CEPdb|isOEERawDetails|LossQty||LossQty||||
|CEPdb|isOEERawDetails|LossQty2||SecondaryLossQty||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|isOEERawDetails|MfgOrderId||||||
|----|----|<site id>||OperationId||||
|CEPdb|isOEERawDetails|OperationId||||||
|----|----|<site id>||OwnerId||||
|CEPdb|isOEERawDetails|OwnerName||||||
|----|----|<site id>||MaterialClassId||||
|CEPdb|isOEERawDetails|ProductFamilyId||||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|isOEERawDetails|ProductId||||||
|----|----|<site id>||QtyAdjustReasonId||||
|CEPdb|isOEERawDetails|QtyAdjustReason||||||
|CEPdb|isOEERawDetails|QueueTime||QueueTime||||
|----|----|<site id>||EquipmentClassId||||
|CEPdb|isOEERawDetails|ResourceFamilyId||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|isOEERawDetails|ResourceId||||||
|CEPdb|isOEERawDetails|ReworkedQty||ReworkedQty||||
|CEPdb|isOEERawDetails|ReworkedQty2||SecondaryReworkedQty||||
|----|----|<site id>||ReworkReasonId||||
|CEPdb|isOEERawDetails|ReworkReason||||||
|----|----|<site id>||ShiftId||||
|CEPdb|isOEERawDetails|Shift||||||
|----|----|<site id>||SpecId||||
|CEPdb|isOEERawDetails|SpecId||||||


|----|----|<site id>|Col4|WorkflowStepId|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CEPdb|isOEERawDetails|StepId||||||
|CEPdb|isOEERawDetails|TotalQty||TotalQty||||
|CEPdb|isOEERawDetails|TotalQty2||SecondaryTotalQty||||
|CEPdb|isOEERawDetails|TxnDate||TxnDate||||
|CEPdb|isOEERawDetails|TxnDateGMT||TxnDateGMT||||
|----|----|<site id>||TxnTypeId||||
|CEPdb|isOEERawDetails|TxnType||||||
|CEPdb|isOEERawDetails|UOM||UomId||||
|CEPdb|isOEERawDetails|UOM2||SecondaryUomId||||
|----|----|<site id>||WorkflowId||||
|CEPdb|isOEERawDetails|WorkflowId||||||
|CEPdb|isOEERawDetails|ProcessTime||ProcessTime||||
|CEPdb|isOEERawDetails|ChildCount||ChildCount||||
|CEPdb|isOEERawDetails|isFailed||isFailed||||
|CEPdb|isOEERawDetails|isFailedQty||FailedQty||||
|CEPdb|isOEERawDetails|isOpenDefectCount||OpenDefectCount||||
|CEPdb|isOEERawDetails|isQty||Qty||||
|CEPdb|isOEERawDetails|isTotalDefectCount||TotalDefectCount||||
||||~~**TxnType**~~|||||
|----|----|<site id>||TxnTypeSiteId||||
|CEPdb|HistoryMainline|TxnType||TxnTypeKey||||
|CEPdb|CDODefinition|CDOName||Name||||
|CEPdb|CDODefinition|CDODescription||Description||||
||||~~**Uom**~~|||||
|CEPdb|UoM|UOMName||UomKey|MODELING|Modeling -> Modeling -> UOM||
|CEPdb|UoM|UomName||Name||||
|----|----|1||UomSystemId||||
|----|----|1||UomCategoryId||||
||||~~**Workflow**~~|||||
|----|----|<site id>||~~WorkflowSiteId~~<br>||||
|CEPdb|Workflow|WorkflowId||~~WorkflowKey~~<br>||||
|CEPdb|WorkflowBase|WorkflowName||~~Name~~||||
|CEPdb|Workflow|Description||Description<br>||||
|CEPdb|Workflow|WorkflowRevision||~~Revision~~||||
||||~~**WorkflowStep**~~|||||
|----|----|<site id>||~~WorkflowStepSiteId~~<br>||||
|CEPdb|WorkflowStep|WorkflowStepId||~~WorkflowStepKey~~<br>||||
|CEPdb|WorkflowStep|WorkflowStepName||~~Name~~||||
|CEPdb|WorkflowStep|Description||Description<br>||||
|CEPdb|WorkflowStep|Sequence||~~Sequence~~<br>||||
|CEPdb|WorkflowStep|IsLastStep||~~IsLastStep~~||||
|----|----|<site id>||WorkflowId||||
|CEPdb|WorkflowStep|WorkflowId||||||


