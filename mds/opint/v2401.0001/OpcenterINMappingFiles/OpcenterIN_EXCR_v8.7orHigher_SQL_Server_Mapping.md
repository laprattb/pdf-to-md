|Opcenter EX CR Entities|Col2|Col3|Col4|Col5|Opcenter Execution Core Model Entities|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**DB Name**|**Entity**|**Attribute**|**Entity**|**Attribute**|**Entity exposed by EX CR Model**|**UI**|**Mapping Info**|
||||**Container**|||||
|----|----|<site id>||ContainerSiteId||||
|CEPdb|Container|ContainerId||ContainerKey|CONTAINER|||
|CEPdb|Container|ContainerName||Name||||
|CEPdb|Container|ContainerComments||Description||||
|CEPdb|CurrentStatus|InProcess||IsInProcess||||
|CEPdb|CurrentStatus|InRework||IsInRework||||
|----|----|<site id>||ContainerStatusId||||
|CEPdb|Container|Status||||||
|----|----|bit||IsFailed||||
|CEPdb|ContainerLevel|ContainerLevelName||LevelName||||
||||**ContainerCorrelation**|||||
|----|----|<site id>||ContainerCorrelationSiteId||||
|CEPdb|HistoryMainline<br>HistoryCrossRef|HistoryMainlineId +'_'+ HistoryCrossRefId||ContainerCorrelationKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|HistoryCrossRef|TrackingId||||||
|----|----|<site id>||ParentContainerId||||
|CEPdb|HistoryCrossRef|HistoryId||||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
||||**ContainerCurrentStatus**|||||
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
|CEPdb|CurrentStatus|isOpStartQty||OpStartQty||||
|CEPdb|CurrentStatus|isOpStartQty2||OpSecondaryStartQty||||
|CEPdb|Container|Qty||ContainerQty||||
|CEPdb|Container|Qty2||ContainerSecondaryQty||||
|CEPdb|UOM|UOMName||UomId||||
|CEPdb|UOM|UOMName||SecondaryUomId||||
|CEPdb|Container|OriginalQty||OriginalQty||||
||||**ContainerOperation**|||||
|----|----|<site id>||ContainerOperationSiteId||||
|CEPdb|HistoryMainline|HistoryMainlineId||ContainerOperationKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|HistoryMainline|ContainerId||||||
|----|----|<site id>||ContainerOperationStatusId||||
|CEPdb|HistoryMainline|isFailed||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|HistoryMainline|ResourceId||||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|HistoryMainline|ProductId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|----|----|<site id>||ParentContainerId||||
|----|----|null||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|HistoryMainline|WorkflowStepId||||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|Container|MfgOrderId||||||
|----|----|<site id>||TxnTypeId||||
|CEPdb|HistoryMainline|TxnType||||||
|----|----|<site id>||RecipeId||||
|----|----|null||||||
|----|----|null||Quantity||||
|CEPdb|MoveHistory|CycleTime||MoveCycletime||||
|CEPdb|MoveInHistory|CycleTime||MoveInCycletime||||
|CEPdb|MoveInHistory|qty||MoveInQuantity||||
|CEPdb|MoveHistory|qty||MoveQuantity||||
|CEPdb|HistoryMainline|TxnId||Txn||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|----|----|<site id>||LaborId||||
|CEPdb|HistoryMainline|EmployeeId||||||
|CEPdb|HistoryMainline|StepPass||ContainerStepPass||||
||||**ContainerOperationAssembly**|||||


|----|----|<site id>|Col4|ContainerOperationAssemblySiteId|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CEPdb|IssueActualsHistory|IssueActualsHistoryId||ContainerOperationAssemblyKey||||
|----|----|<site id>||Assembled2ContainerId||||
|----|----|null||||||
|----|----|<site id>||Assembled2MaterialDefinitionId||||
|----|----|null||||||
|----|----|<site id>||Assembled3ContainerId||||
|----|----|null||||||
|----|----|<site id>||Assembled3MaterialDefinitionId||||
|----|----|null||||||
|----|----|<site id>||AssembledContainerId||||
|CEPdb|Container<br>IssueActualsHistory|CASE WHEN TxnType = 4792754 THEN Container.ContainerId  ELSE<br>IssueActualsHistory.FromContainerId||||||
|----|----|<site id>||AssembledMaterialDefinitionId||||
|CEPdb|Container<br> IssueActualsHistory<br>Product|CASE WHEN TxnType = 4792754 THEN coalesce(Container.ProductId,Product.ProductId,FromLot)<br>ELSE coalesce(Container.ProductId,FromLot)||||||
|----|----|<site id>||AssembledOnContainerId||||
|CEPdb|HistoryMainline|ContainerId||||||
|----|----|<site id>||AssembledOnMaterialDefinitionId||||
|CEPdb|HistoryMainline|ProductId||||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
|----|----|<site id>||ContainerOperationStatusId||||
|CEPdb|HistoryMainline|isFailed||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|HistoryMainline|ResourceId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|----|----|<site id>||PartNumberMaterialDefinitionId||||
|CEPdb|IssueActualsHistory|ProductId||||||
|----|----|<site id>||RecipeId||||
|----|----|null||||||
|----|----|<site id>||ReferenceDesignatorId||||
|CEPdb|IssueActualsHistory|ReferenceDesignator||||||
|----|----|<site id>||SubAssembledOnContainerId||||
|----|----|null||||||
|----|----|<site id>||SubAssembledOnMaterialDefinitionId||||
|----|----|null||||||
|----|----|<site id>||TxnTypeId||||
|CEPdb|HistoryMainline|TxnType||||||
|CEPdb|IssueActualsHistory|Qty||IssueQuantity||||
|CEPdb|HistoryMainline|TxnId||Txn||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|----|----|<site id>||OperationExecutionId||||
|CEPdb|Container|MfgOrderId||||||
||||**ContainerOperationDisassociate**|||||
|----|----|<site id>||ContainerOperationDisassociateSiteId||||
|CEPdb|DisassociateHistoryChildCnts|DisassociateHistoryId-Sequence||ContainerOperationDisassociateKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|DisassociateHistoryChildCnts|ChildContainersId||||||
|----|----|<site id>||ParentContainerId||||
|CEPdb|DisassociateHistory|ParentContainerId||||||
|CEPdb|DisassociateHistoryChildCnts|Sequence||Sequence||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
|CEPdb|HistoryMainline|TxnId||Txn||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
||||**ContainerOperationExecuteTask**|||||
|----|----|<site id>||ContainerOperationExecuteTaskSiteId||||
|CEPdb|ExecuteTaskHistory|ExecuteTaskHistoryId||ContainerOperationExecuteTaskKey||||
|----|----|<site id>||ContainerOperationId||||
|CEPdb|HistoryMainline|HistoryMainlineId||||||
|----|----|<site id>||ParentContainerId||||
|CEPdb|HistoryMainline|HistoryId||||||
|----|----|<site id>||TaskItemId||||
|CEPdb|TaskItem|TaskItemId||||||
|----|----|<site id>||TaskStatusId||||
|CEPdb|ExecuteTaskHistory|Pass||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|HistoryMainline|WorkflowStepId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|----|----|<site id>||ElectronicProcedureId||||
|CEPdb|ExecuteTaskHistory|ElectronicProcedureId||||||
|----|----|<site id>||LaborId||||
|CEPdb|HistoryMainline|EmployeeId||||||
|----|----|<site id>||TxnTypeId||||
|CEPdb|HistoryMainline|TxnType||||||
|----|----|<site id>||ContainerOperationExecuteTaskComputationId||||
|CEPdb|ComputationHistory|ComputationId||||||
|----|ComputationHistory|ResultValue||ComputationValue||||
|----|----|<site id>||SignatureMeaningId||||
|CEPdb|ESigHistorySummary|MeaningId||||||
|----|----|<site id>||SignerLaborId||||
|CEPdb|ESigHistoryDetail|signerId||||||
|----|----|<site id>||CoSignerLaborId||||
|CEPdb|ESigHistoryDetail|cosignerId||||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|CEPdb|HistoryMainline|TxnId||Txn||||
||||**ContainerOperationExecuteTaskComputation**|||||


|----|----|<site id>|Col4|ContainerOperationExecuteTaskComputationSiteId|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CEPdb|Computation|ComputationId||ContainerOperationExecuteTaskComputationKey||||
|CEPdb|Computation|ComputationName||Name||||
|CEPdb|Computation|Description||Description||||
||||**ContainerOperationExecuteTaskParameter**|||||
|----|----|<site id>||ContainerOperationExecuteTaskParameterSiteId||||
|CEPdb|DataPointHistoryDetail|DataName||ContainerOperationExecuteTaskParameterKey||||
|CEPdb|DataPointHistoryDetail|DataName||Name||||
|----|----|null||Description||||
||||**ContainerOperationExecuteTaskParameterValue**|||||
|----|----|<site id>||ContainerOperationExecuteTaskParameterValueSiteId||||
|CEPdb|DataPointHistoryDetail|DataPointHistoryDetailId||ContainerOperationExecuteTaskParameterValueKey||||
|----|----|<site id>||ContainerOperationExecuteTaskId||||
|CEPdb|ExecuteTaskHistory|ExecuteTaskHistoryId||||||
|----|----|<site id>||ContainerOperationExecuteTaskParameterId||||
|CEPdb|DataPointHistoryDetail|DataName||||||
|CEPdb|DataPointHistoryDetail|DataValue||StringValue||||
|CEPdb|DataPointHistoryDetail|LowerLimit||LowerLimit||||
|CEPdb|DataPointHistoryDetail|UpperLimit||UpperLimit||||
|CEPdb|UOM|UOMName||UomKey||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
||||**ContainerOperationHold**|||||
|----|----|<site id>||ContainerOperationHoldSiteId||||
|CEPdb|HistoryMainline<br>HistoryCrossRef|HistoryMainlineId +'_'+HistoryCrossRefId||ContainerOperationHoldKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|HistoryCrossRef|TrackingId||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|HistoryMainline|WorkflowStepId||||||
|----|----|<site id>||LaborId||||
|CEPdb|HistoryMainline|EmployeeId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|CEPdb|HistoryMainline|Comments||Comment||||
|----|----|<site id>||ContainerOperationHoldReasonId||||
|CEPdb|HoldReleaseHistory|HoldReasonId||||||
||||**ContainerOperationHoldReason**|||||
|----|----|<site id>||ContainerOperationHoldReasonSiteId||||
|CEPdb|HoldReason|HoldReasonId||ContainerOperationHoldReasonKey||||
|CEPdb|HoldReason|HoldReasonName||Name||||
|CEPdb|HoldReason|Description||Description||||
||||**ContainerOperationMoveNonStandard**|||||
|----|----|<site id>||ContainerOperationMoveNonStandardSiteId||||
|CEPdb|HistoryMainline, HistoryCrossRef|HistoryMainline.HistoryMainlineId +'_'+ HistoryCrossRef.HistoryCrossRefId||ContainerOperationMoveNonStandardKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|HistoryCrossRef|TrackingId||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|HistoryMainline|WorkflowStepId||||||
|----|----|<site id>||LaborId||||
|CEPdb|HistoryMainline|EmployeeId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|----|----|<site id>||ToWorkflowStepId||||
|CEPdb|MoveHistory|ToStepId||||||
|CEPdb|HistoryMainline|Comments||Comment||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
||||**ContainerOperationRework**|||||
|----|----|<site id>||ContainerOperationReworkSiteId||||
|CEPdb|HistoryMainline<br>HistoryCrossRef|HistoryMainlineId +'_'+HistoryCrossRefId||ContainerOperationReworkKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|HistoryCrossRef|TrackingId||||||
|----|----|<site id>||WorkflowStepId||||
|CEPdb|HistoryMainline|WorkflowStepId||||||
|----|----|<site id>||LaborId||||
|CEPdb|HistoryMainline|EmployeeId||||||
|----|----|<site id>||OperationId||||
|CEPdb|HistoryMainline|OperationId||||||
|CEPdb|HistoryMainline|Comments||Comment||||
|CEPdb|HistoryMainline|TxnDate||TxnDate||||
|CEPdb|HistoryMainline|TxnDateGMT||TxnDateGMT||||
|----|----|<site id>||ContainerOperationReworkReasonId||||
|CEPdb|ReworkReason|ReworkReasonId||||||
||||**ContainerOperationReworkReason**|||||
|----|----|<site id>||ContainerOperationReworkReasonSiteId||||
|CEPdb|ReworkReason|ReworkReasonId||ContainerOperationReworkReasonKey||||
|CEPdb|ReworkReason|ReworkReasonName||Name||||
|CEPdb|ReworkReason|Description||Description||||
||||**ContainerOperationStatus**|||||
|----|----|<site id>||ContainerOperationStatusSiteId||||
|----|----|FAIL or PASS||ContainerOperationStatusKey||||
|----|----|FAIL or PASS||Name||||
|----|----|FAIL or PASS||Description||||
||||**ContainerProperty**|||||
|----|----|<site id>||ContainerPropertySiteId||||
|----||"FactoryStartDate"||ContainerPropertyKey||||
|----||"DateTime"||PropertyTypeKey||||
|----|----|null||UomKey||||


|----|----|"FactoryStartDate"|Col4|Name|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|----|----|null||Description||||
|----|----|0||Multivalue||||
||||**ContainerPropertyStaticValue**|||||
|----|----|<site id>||ContainerPropertyStaticValueSiteId||||
|CEPdb|Container|ContainerId + '_' + 'FactoryStartDate'||ContainerPropertyStaticValueKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|Container|ContainerId||||||
|----|----|<site id>||ContainerPropertyId||||
|----||FactoryStartDate'||||||
|----|----|null||StringValue||||
|----|----|null||FloatValue||||
|CEPdb|Container|FactoryStartDate||DatetimeValue||||
|----|----|null||Sequence||||
||||**ContainerStatus**|||||
|----|----|<site id>||ContainerStatusSiteId|CONTAINER|||
|----|----|0 or 1 or 2 or 3 or 4||ContainerStatusKey||||
|----|----|Deleted or Open or Closed or In transit or Issued||Name||||
|----|----|null||Description||||
||||**ElectronicProcedure**|||||
|----|----|<site id>||ElectronicProcedureSiteId||||
|CEPdb|ElectronicProcedure|ElectronicProcedureId||ElectronicProcedureKey||||
|CEPdb|ElectronicProcedureBase|ElectronicProcedureName||Name||||
|CEPdb|ElectronicProcedure|Description||Description||||
||||**Equipment**|||||
|----|----|<site id>||EquipmentSiteId||||
|CEPdb|ResourceDef|ResourceId||EquipmentKey|RESOURCE|Modeling -> Modeling -> Resource (Resource field)||
|CEPdb|ResourceDef|ResourceName||Name||||
||||**EquipmentClass**|||||
|----|----|<site id>||EquipmentClassSiteId||||
|CEPdb|ResourceFamily|ResourceFamilyId||EquipmentClassKey|RESOURCE FAMILY|Modeling -> Modeling -> Resource Family (Resource<br>Family field)||
|CEPdb|ResourceFamily|ResourceFamilyName||Name||||
||||**EquipmentEquipmentClass**|||||
|----|----|<site id>||EquipmentEquipmentClassSiteId||||
|CEPdb|ResourceDef, ResourceFamily|ResourceDef.ResourceId + "_" + ResourceFamily.ResourceFamilyId||EquipmentEquipmentClassKey||Modeling -> Modeling -> Resource (Resource field)<br>Modeling -> Modeling -> Resource Family (Resource<br>Family field)<br>Event -> Record Generic Event or Container -> Record<br>Production Event|Resource / Resource family association|
|----|----|<site id>||EquipmentId|RESOURCE|Modeling -> Modeling -> Resource (Resource field)||
|CEPdb|ResourceDef|ResourceDef.ResourceId||||||
|----|----|smallint||EquipmentClassId|RESOURCE FAMILY|Modeling -> Modeling -> Resource Family (Resource<br>Family field)<br>Event -> Record Generic Event or Container -> Record<br>Production Event||
|CEPdb|ResourceFamily|ResourceFamily.ResourceFamilyId||||||
||||**EquipmentHierarchy**|||||
|----|----|<site id>||EquipmentHierarchySiteId||||
|CEPdb|ResourceDef|ResourceId||EquipmentHierarchyKey|RESOURCE|Modeling -> Modeling -> Resource (Resource field)||
|----|----|smallint||EquipmentId||||
|CEPdb|ResourceDef|ResourceId||||||
|----|----|smallint||ParentEquipmentId||||
|CEPdb|ResourceDef|ParentResourceId||||Modeling -> Modeling -> Resource (Parent Resource field)||
||||**EquipmentTimeCategory**|||||
|----|----|<site id>||EquipmentTimeCategorySiteId||||
|----|----|1 or 2 or 3 or 4 or 5 or 6 or Undefined||EquipmentTimeCategoryKey|RESOURCE STATE|||
|----|----|Nonscheduled Time or Nonscheduled Downtime or Scheduled Downtime or<br>Engineering Time or Productive Time or Standby Time or Undefined||Name||||
|----|----|null||Description||||
||||**EquipmentTimeModel**|||||
|----|----|<site id>||EquipmentTimeModelSiteId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|ResourceStatusHistoryId<br>'Actual ' + ProductionStatusId||EquipmentTimeModelKey|RESOURCE STATUS HISTORY union<br>PRODUCTION STATUS|Resource -> Resource Set Up - generates<br>ResourceStatusHistory||
|----|----|smallint||EquipmentTimeCategoryId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceState<br>ResourceState||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|HistoryMainline<br>ProductionStatus|ResourceId||||||
|----|----|<site id>||ReasonTreeItemId||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldResourceState + OldResourceStatusCodeId + OldResourceStatusReasonCodeId<br>ResourceState + StatusId + ReasonId||||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|OldLastStatusChangeDateGMT<br>LastStatusChangeDateGMT||StartDateTime||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|LastStatusChangeDateGMT<br>null||EndDateTime||||
|CEPdb|ResourceStatusHistory<br>ProductionStatus|datediff(second,[OldLastStatusChangeDateGMT], [LastStatusChangeDateGMT])<br>null||Duration||||
|----|----|smallint||MicrostopId||||
||||**FailureEvent**|||||
|----|----|<site id>||FailureEventSiteId||||
|CEPdb|Event|EventId||FailureEventKey||||
|----|----|<site id>||FailureEventCauseId||||
|CEPdb|EventFailureCause|CauseCodeId||||||
|----|----|<site id>||FailureEventModeId||||
|CEPdb|EventFailure|FailureModeId||||||
|----|----|<site id>||FailureEventResolutionId||||
|CEPdb|Event|QualityResolutionCodeId||||||
|----|----|<site id>||FailureEventSeverityId||||
|CEPdb|EventFailure|FailureSeverityId||||||
|----|----|<site id>||FailureEventStatusId||||
|CEPdb|Event|Status||||||
|----|----|<site id>||FailureEventTypeId||||
|CEPdb|EventFailure|FailureTypeId||||||
|----|----|<site id>||LaborId||||


|CEPdb|Event|InitiatorId|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CEPdb|Event|EventName||Name||||
|CEPdb|Event|Description||Description||||
|CEPdb|EventFailure|Comments||Comment||||
|CEPdb|Event|ReportedDate||ReportedDate||||
|CEPdb|Event|ReportedDateGMT||ReportedDateGMT||||
||||**FailureEventCause**|||||
|----|----|<site id>||FailureEventCauseSiteId||||
|CEPdb|NCRCauseCode|NCRCauseCodeId||FailureEventCauseKey||||
|CEPdb|NCRCauseCode|NCRCauseCodeName||Name||||
|CEPdb|NCRCauseCode|Description||Description||||
||||**FailureEventDetail**|||||
|----|----|<site id>||FailureEventDetailSiteId||||
|CEPdb|EventLot|EventLotId||FailureEventDetailKey||||
|----|----|<site id>||ContainerId||||
|CEPdb|EventLot|ContainerId||||||
|----|----|<site id>||EquipmentId||||
|CEPdb|ResourceDef|ResourceId||||||
|----|----|<site id>||FailureEventId||||
|CEPdb|Event|EventId||||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|Product|ProductId||||||
||||**FailureEventMode**|||||
|----|----|<site id>||FailureEventModeSiteId||||
|CEPdb|FailureMode|FailureModeId||FailureEventModeKey||||
|CEPdb|FailureMode|FailureModeName||Name||||
|CEPdb|FailureMode|Description||Description||||
||||**FailureEventResolution**|||||
|----|----|<site id>||FailureEventResolutionSiteId||||
|CEPdb|QualityResolutionCode|QualityResolutionCodeId||FailureEventResolutionKey||||
|CEPdb|QualityResolutionCode|QualityResolutionCodeName||Name||||
|CEPdb|QualityResolutionCode|Description||Description||||
||||**FailureEventSeverity**|||||
|----|----|<site id>||FailureEventSeveritySiteId||||
|CEPdb|FailureSeverity|FailureSeverityId||FailureEventSeverityKey||||
|CEPdb|FailureSeverity|FailureSeverityName||Name||||
|CEPdb|FailureSeverity|Description||Description||||
||||**FailureEventStatus**|||||
|----|----|<site id>||FailureEventStatusSiteId||||
|----|----|1 or 2 or 3 or 4 or 5 or 6 or 7 or 8||FailureEventStatusKey||||
|----|----|Active or Pending or Escalated or Void or Closed or Deleted or Initiated or InReview||Name||||
|----|----|----||Description||||
||||**FailureEventType**|||||
|----|----|<site id>||FailureEventTypeSiteId||||
|CEPdb|NCRFailureType|NCRFailureTypeId||FailureEventTypeKey||||
|CEPdb|NCRFailureType|NCRFailureTypeName||Name||||
|CEPdb|NCRFailureType|Description||Description||||
||||**Factory**|||||
|----|----|<site id>||FactorySiteId||||
|CEPdb|Factory|FactoryId||FactoryKey|FACTORY|||
|CEPdb|Factory|FactoryName||Name||||
|CEPdb|Factory|Description||Description||||
||||**Indicator**|||||
|----|----|<site id>||IndicatorSiteId||||
|----|----|GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime||IndicatorKey|SUMMARY TABLE|||
|----|----|GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime||Name||||
|----|----|null||Description||||
|CEPdb|isOEERawDetails|Uom or Uom2||UomId||||
||||**IndicatorClass**|||||
|----|----|<site id>||IndicatorClassSiteId||||
|----|----|Counter||IndicatorClassKey||||
|----|----|Counter||Name||||
|----|----|Counter||Description||||
||||**IndicatorIndicatorClass**|||||
|----|----|<site id>||IndicatorIndicatorClassSiteId||||
|----|----|(GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime) + Counter||IndicatorIndicatorClassKey||||
|----|----|<site id>||IndicatorClassId||||
|----|----|Counter||||||
|----|----|<site id>||IndicatorId||||
|----|----|GoodQty or LossQty or ReworkedQty or TotalQty or SecondaryGoodQty or SecondaryLossQty or<br>SecondaryReworkedQty or SecondaryTotalQty or IdealCycleTime||||||
||||**IndicatorValue**|||||
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
||||**Labor**|||||
|----|----|<site id>||LaborId|EMPLOYEE|Modeling -> Modeling -> Employee<br>Event -> Record Generic Event or Container -> Record||
|CEPdb|Employee|EmployeeId||||||
|CEPdb|Employee|EmployeeName||Name||||
|CEPdb|Employee|Description||Description||||
||||**Location**|||||
|----|----|<site id>||LocationSiteId|LOCATION|||
|CEPdb|Location|LocationId||LocationKey||||
|CEPdb|Location|LocationName||Name||||


|CEPdb|Location|Description|Col4|Description|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||**MaterialClass**|||||
|----|----|<site id>||MaterialClassSiteId||||
|CEPdb|ProductFamily|ProductFamilyId||MaterialClassKey|PRODUCT FAMILY|Modeling -> Modeling -> Product Family<br>Event -> Record Generic Event or Container -> Record<br>Production Event<br>Container -> Hold<br>Container -> Rework||
|CEPdb|ProductFamily|ProductFamilyName||Name||||
||||**MaterialDefinition**|||||
|----|----|<site id>||MaterialDefinitionSiteId||||
|CEPdb|Product|ProductId||MaterialDefinitionKey|PRODUCT|Modeling -> Modeling -> Product<br>Container -> Start (Product field)<br>Event -> Record Generic Event or Container -> Record<br>Production Event||
|CEPdb|ProductBase|ProductName||Name||||
|CEPdb|Product|Description||Description||||
||||**MaterialDefinitionMaterialClass**|||||
|----|----|<site id>||MaterialDefinitionMaterialClassSiteId||||
|CEPdb|Product, ProductFamily|ProductId + "_" + ProductFamilyId||MaterialDefinitionMaterialClassKey|PRODUCT FAMILY|Modeling -> Modeling -> Product Family<br>Modeling -> Modeling -> Product<br>Container -> Start (Product field)<br>Event -> Record Generic Event or Container -> Record<br>Production Event|Product / Product Familiy association|
|----|----|<site id>||MaterialDefinitionId|PRODUCT|||
|CEPdb|Product|ProductId||||||
|----|----|<site id>||MaterialClassId||||
|CEPdb|ProductFamily|ProductFamilyId||||||
||||**MaterialDefinitionPropertyStaticValue**|||||
|----|----|<site id>||MaterialDefinitionPropertyStaticValueSiteId||||
|CEPdb|Product|ProductId + ' Revision' OR  ProductId +' CurrentCost'  OR ProductId +' StandardCost'||MaterialDefinitionPropertyStaticValueKey|PRODUCT|||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|Product|ProductId||||||
|----|----|<site id>||MaterialPropertyId||||
|----|----|"Revision"  OR "CurrentCost" OR  "StandardCost"||||||
|CEPdb|Product|ProductRevision||StringValue||||
|CEPdb|Product|CurrentCost OR StdCost||FloatValue||||
|----|----|----||DatetimeValue||||
|----|----|----||Sequence||||
||||**MaterialLot**|||||
|----|----|<site id>||MaterialLotSiteId||||
|CEPdb|MfgLot|MfgLotId||MaterialLotKey||||
|CEPdb|MfgLot|MfgLotName||Name||||
|----|----|null||Description||||
|----|----|<site id>||MaterialDefinitionId||||
|CEPdb|MfgLot|ProductId||||||
|CEPdb|MfgLot|Qty||Quantity||||
|CEPdb|UOM|UOMName||UomId||||
|CEPdb|MfgLot|CreationDate||ValidFromDateTime||||
|----|----|null||ValidToDateTime||||
||||**MaterialProperty**|||||
|----|----|<site id>||MaterialPropertySiteId||||
|----|----|"Revision"  OR "CurrentCost" OR  "StandardCost"||MaterialPropertyKey||||
|----|----|"Revision"  OR "CurrentCost" OR  "StandardCost"||Name||||
|----|----|----||Description||||
|----|----|"String" OR "Numeric"||PropertyTypeKey||||
|----|----|----||UomKey||||
||||**Operation**|||||
|CEPdb|----|<site id>||OperationSiteId||||
|CEPdb|Operation|OperationId||OperationKey||||
|CEPdb|Operation|OperationName||Name||||
|CEPdb|Operation|Notes||Description||||
||||**OperationExecution**|||||
|----|----|<site id>||OperationExecutionSiteId||||
|CEPdb|MfgOrder|MfgOrderId||OperationExecutionKey||||
|CEPdb|MfgOrder|MfgOrderName||Name|MFG ORDER|Modeling -> Modeling -> Mfg Order (Mfg Order field)||
|CEPdb|MfgOrder|Description||Description||Modeling -> Modeling -> Mfg Order (Description field)||
|----|----|<site id>||OperationExecutionStatusId||||
|CEPdb|MfgOrder|OrderStatusId||||||
|----|----|----||EquipmentId||||
|----|----|----||||||
|----|----|<site id>||MaterialDefinitionId||Modeling -> Modeling -> Mfg Order (Product field)||
|CEPdb|Product|ProductId or RevOfRcdId||||||
|----|----|----||BillOfMaterialId||||
|----|----|----||||||
|----|----|<site id>||OperationSchedulingId||||
|----|----|nvarchar||||||
|CEPdb|MfgOrder|qty||ProducedQuantity||Modeling -> Modeling -> Mfg Order (Quantity field)||
|----|----|----||ReworkedQuantity||||
|----|----|float||ScrapQuantity||||
|CEPdb|Uom|UomName||UomId||Modeling -> Modeling -> Mfg Order (UOM field)||
|CEPdb|MfgOrder|PlannedStartDateGMT||StartDateTime||Modeling -> Modeling -> Mfg Order (Planned Start Date<br>field)||
|CEPdb|MfgOrder|PlannedCompletionDateGMT||EndDateTime||Modeling -> Modeling -> Mfg Order (Planned Completion<br>Date field)||
|----|----|float||Duration||||
|----|----|----||StartDateTime||||
|----|----|----||EndDateTime||||
|----|----|----||DatetimeValue||||
|----|----|----||Sequence||||
||||**OperationExecutionStatus**|||||
|----|----|<site id>||OperationExecutionStatusSiteId||||
|CEPdb|OrderStatus|OrderStatusId||OperationExecutionStatusKey|ORDER STATUS|Modeling -> Order Status||
|CEPdb|OrderStatus|OrderStatusName||Name||||
|CEPdb|OrderStatus|Description||Description||||
||||**OperationResponse**|||||
|----|----|<site id>||~~OperationResponseSiteId~~|SUMMARY TABLE|||


|CEPdb|isOEERawDetails|OperationId + ' ' + MfgOrderId + ' ' + ResourceId|Col4|OperationResponseKey|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
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
|----|----|----||UomId||||
|----|----|----||ProducedQuantity||||
|----|----|----||ReworkedQuantity||||
|----|----|----||ScrapQuantity||||
|----|----|----||Sequence||||
|CEPdb|MfgOrder|min(PlannedStartDateGMT)||StartDateTime||||
|CEPdb|MfgOrder|max(PlannedCompletionDateGMT)||EndDateTime||||
|---|----|----||Duration||||
||||**OperationResponseEquipmentSpecification**|||||
|---|----|<site id>||OperationResponseEquipmentSpecificationSiteId|SUMMARY TABLE|||
|CEPdb|isOEERawDetails|OperationId + ' ' + MfgOrderId + ' ' + ResourceId + ' ' + TxnDateGMT||OperationResponseEquipmentSpecificationKey<br>||||
|---|----|<site id>||~~EquipmentId~~||||
|CEPdb|isOEERawDetails|ResourceId||||||
|---|----|<site id>||OperationResponseId||||
|CEPdb|isOEERawDetails|OperationId + ' ' + MfgOrderId + ' ' + ResourceId||||||
|----|----|----||Quantity||||
|CEPdb|isOEERawDetails|TxnDateGMT||StartDateTime<br>|StartDateTime<br>|StartDateTime<br>|StartDateTime<br>|
|CEPdb|isOEERawDetails|TxnDateGMT + (ProcessTime or QueueTime)*24*60*60||~~EndDateTime~~<br>||||
|----|----|----||~~Duration~~|~~Duration~~|~~Duration~~|~~Duration~~|
||||**Owner**|||||
|----|----|<site id>||OwnerSiteId||||
|CEPdb|Owner|OwnerName||OwnerKey||||
|CEPdb|Owner|OwnerName||Name||||
|CEPdb|Owner|Description||Description||||
||||**PropertyType**|||||
|----|----|"String" or "Numeric" or "DateTime"||PropertyTypeKey||||
|----|----|"String" or "Numeric" or "DateTime"||Name||||
|----|----|----||Description||||
|----|----|----||QualityLimitStatusId||||
|----|----|----||||||
||||**QtyAdjustReason**|||||
|----|----|<site id>||QtyAdjustReasonSiteId||||
|CEPdb|LossReason, QtyAdjustReason, BonusReason|LossReasonName OR QtyAdjustReasonName OR BonusReasonName||QtyAdjustReasonKey||||
|CEPdb|LossReason, QtyAdjustReason, BonusReason|LossReasonName OR QtyAdjustReasonName OR BonusReasonName||Name||||
|----|----|----||Description||||
||||**Reason**|||||
|----|----|<site id>||ReasonSiteId||||
|CEPdb|ResourceStatusReason|ResourceStatusReasonId||ReasonKey|MODELING|Modeling -> Modeling -> Resource Status Reason||
|CEPdb|ResourceStatusReason|ResourceStatusReasonName||Name||||
|CEPdb|ResourceStatusReason|Description||Description||||
|----|----|0||IsStop||||
||||**ReasonTree**|||||
|----|----|----||ReasonTreeSiteId||||
|----|----|----||ReasonTreeKey||||
|----|----|----||Name||||
|----|----|----||Description||||
||||**ReasonTreeItem**|||||
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
||||**ReworkReason**|||||
|----|----|<site id>||ReworkReasonSiteId||||
|CEPdb|ReworkReason|ReworkReasonName||ReworkReasonKey||||
|CEPdb|ReworkReason|ReworkReasonName||Name||||
|----|----|----||Description||||
||||**Shift**|||||
|----|----|<site id>||ShiftSiteId||||
|CEPdb|Shift|ShiftName||ShiftKey||||
|CEPdb|Shift|ShiftName||Name||||
|CEPdb|Shift|Description||Description||||
|----|----|----||StartTime||||
|----|----|----||EndTime||||


|----|----|0|Col4|IsDayAfter|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||**SignatureMeaning**|||||
|----|----|<site id>||SignatureMeaningSiteId||||
|CEPdb|ESigMeaning|ESigMeaningId||SignatureMeaningKey||||
|CEPdb|ESigMeaning|ESigMeaningName||Name||||
|CEPdb|ESigMeaning|Description||Description||||
||||**Spec**|||||
|----|----|<site id>||SpecSiteId||||
|CEPdb|Spec|SpecId||SpecKey||||
|CEPdb|SpecBase|SpecName||Name||||
|CEPdb|Spec|Description||Description||||
|CEPdb|Spec|SpecRevision||Revision||||
||||**Status**|||||
|----|----|<site id>|StatusSiteId||RESOURCE STATE|Modeling -> Modeling -> Resource Status Code (Resource||
|CEPdb|ResourceStatusCode|ResourceStatusCodeId|StatusKey|||Also, Resource -> Resource Set Up (Resource Status Code<br>field)||
|CEPdb|ResourceStatusCode|ResourceStatusCodeName|Name|||||
|CEPdb|ResourceStatusCode|Description|Description|||||
|CEPdb|ResourceStatusCode|case when Availability > 1 then 1 else 0|IsStop|||||
||||**SummaryTableCompletedWIPSummary**|||||
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
|CEPdb|isCompletedWIPSummary|FactoryStartDate||FactoryStartDate||||
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
||||**SummaryTableOEERawDetails**|||||
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


|CEPdb|isOEERawDetails|IdealCycleTime|Col4|IdealCycleTime|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
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
|----|----|<site id>||WorkflowStepId||||
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
||||**TaskItem**|||||
|----|----|<site id>||TaskItemSiteId||||
|CEPdb|TaskItem|TaskItemId||TaskItemKey||||
|----|----|<site id>||TaskListId||||
|CEPdb|TaskItem|TaskListId||||||
|CEPdb|TaskItem|Sequence||Sequence||||
|CEPdb|TaskItem|TaskItemName||Name||||
|CEPdb|TaskItem|ReportInstruction||Description||||
||||**TaskList**|||||
|----|----|<site id>||TaskListSiteId||||
|CEPdb|tasklist|TaskListId||TaskListKey||||
|CEPdb|TaskListBase|TaskListName||Name||||
|CEPdb|tasklist|ReportInstruction||Description||||
||||**TaskStatus**|||||
|----|----|<site id>||TaskStatusSiteId||||
|----|----|1  or 0||TaskStatusKey||||
|----|----|Pass or Fail||Name||||
|----|----|null||Description||||
||||**TxnType**|||||
|----|----|<site id>||TxnTypeSiteId||||
|CEPdb|HistoryMainline|TxnType||TxnTypeKey||||
|CEPdb|CDODefinition|CDOName||Name||||
|CEPdb|CDODefinition|CDODescription||Description||||
||||**Uom**|||||
|CEPdb|UoM|UOMName||UomKey|MODELING|Modeling -> Modeling -> UOM||
|CEPdb|UoM|UomName||Name||||
|----|----|1||UomSystemId||||
|----|----|1||UomCategoryId||||
||||**Workflow**|||||
|----|----|<site id>||WorkflowSiteId||||
|CEPdb|Workflow|WorkflowId||WorkflowKey||||
|CEPdb|WorkflowBase|WorkflowName||Name||||
|CEPdb|Workflow|Description||Description||||
|CEPdb|Workflow|WorkflowRevision||Revision||||
||||**WorkflowStep**|||||
|----|----|<site id>||WorkflowStepSiteId||||
|CEPdb|WorkflowStep|WorkflowStepId||WorkflowStepKey||||
|CEPdb|WorkflowStep|WorkflowStepName||Name||||
|CEPdb|WorkflowStep|Description||Description||||
|CEPdb|WorkflowStep|Sequence||Sequence||||


