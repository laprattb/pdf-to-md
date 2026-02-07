|SIMATIC IT LMS 2.3-2.4-2.5-2.6-2.7|Col2|Col3|Opcenter Intelligence Model Entities|Col5|SIMATIC IT LMS Model Entities|Col7|
|---|---|---|---|---|---|---|
|~~**Database Name**~~|~~**Entity**~~|~~**Attribute**~~|~~**Entity**~~<br>|~~**Attribute - Tables**~~|~~**LMS Entity**~~<br>|~~**Mapping Info**~~|
||||~~**Cause**~~||~~**Cause**~~||
|~~---~~<br>|~~----~~<br>|~~smallint~~<br>||~~CauseSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe~~<br>-9AF5-66BEE7A3BA76/OEEStateList<br>|~~IDObj~~<br>||~~CauseKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe~~<br>-9AF5-66BEE7A3BA76/OEEStateList<br>|~~StateDescription~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5~~<br>-66BEE7A3BA76/OEEStateList<br>|~~coalesce(UNIStateDescription,StateDescription)~~<br>||~~Description~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5~~<br>-66BEE7A3BA76/OEEStateList<br>|~~isStop~~<br>||~~IsStop~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5~~<br>-66BEE7A3BA76/OEEStateList|~~StateColor~~||~~Color~~|||
||||~~**DetailedReason**~~||~~**Detailed Reason**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~DetailedReasonSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~IDObj~~<br>||~~DetailedReasonKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5~~<br>-66BEE7A3BA76/OEEStateList<br>|~~StateDescription~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5~~<br>-66BEE7A3BA76/OEEStateList<br>|~~coalesce(UNIStateDescription,StateDescription)~~<br>||~~Description~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~StateColor~~<br>||~~Color~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5~~<br>-66BEE7A3BA76/OEEStateList|~~isStop~~||~~IsStop~~|||
||||~~**Equipment**~~||~~**Equipment**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>||~~EquipmentKey~~<br>|||
|~~LMS24Proj~~<br>|~~Equipment~~<br>|~~EquipmentName~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~|~~Equipment~~|~~description~~||~~Description~~|||
||||~~**EquipmentCapacity**~~||~~**Design Speed (definition)**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentCapacitySiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedRegistry<br>|~~Name~~<br>||~~EquipmentCapacityKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedRegistry<br>|~~Name~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedRegistry|~~Description~~||~~Description~~|||
||||~~**EquipmentClas**~~||~~**Equipment Class**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentClassSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Equipment~~<br>|~~ClassName~~<br>||~~EquipmentClassKey~~<br>|||
|~~LMS24Proj~~<br>|~~Equipment~~<br>|~~ClassName~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~|~~Equipment~~|~~ClassName~~||~~Description~~|||
||||~~**EquipmentEquipmentClass**~~||~~**Relationship between equipment and**~~<br>**equipment class**||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentEquipmentClassSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>||~~EquipmentEquipmentClassKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentId~~<br>|||
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentClassId~~|||
|~~LMS24Proj~~|~~Equipment~~|~~ClassName~~|||||
||||~~**EquipmentHierarchy**~~||~~**Equipment model**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentHierarchySiteId~~<br>|||
|~~LMS24Proj~~|~~equipment_version~~|~~ Equipmentid~~||~~EquipmentHierarchyKey~~|||


|----|----|smallint|Col4|EquipmentId|Col6|Col7|
|---|---|---|---|---|---|---|
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ParentEquipmentId~~|||
|~~LMS24Proj~~|~~equipment_version~~|~~FullPath (parent)~~|||||
||||~~**EquipmentTimeCategory**~~||~~**Time Category (definition)**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentTimeCategorySiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem<br>|~~PPAObjectId~~<br>||~~EquipmentTimeCategoryKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem<br>|~~ItemDescr~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem<br>|~~UNIItemDescr~~<br>||~~Description~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem|~~ItemColor~~||~~ItemColor~~|||
||||~~**EquipmentTimeCategoryHierarchy**~~||~~**Time category hierarchy (Time Model)**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentTimeCategoryHierarchySiteId~~<br>|||
|~~LMS24Proj~~<br>SITMESDB_LMS24<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem<br>SHC_WORK_SCHED_BREAK<br>|~~PPAObjectId  or Id~~<br>||~~EquipmentTimeCategoryHierarchyKey~~<br>|||
|~~LMS24Proj~~<br>SITMESDB_LMS24<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem,SHC_WORK_SCHE<br>D_BREAK<br>|~~PPAObjectId  or Id~~<br>||~~EquipmentTimeCategoryId~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>|||||
|~~LMS24Proj~~<br>SITMESDB_LMS24<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem<br>|~~PRNT_TIME_CAT_ID or 'CalendarBreak'~~<br>||~~ParentEquipmentTimeCategoryId~~|||
|~~----~~|~~----~~|~~smallint~~|||||
||||~~**Indicator**~~||~~**KPI or Counter (definition)**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~IndicatorSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithm<br>Complete_OEEENG546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEECounter<br>|~~algorithmName+ '_' + Uom or CounterDescription +~~<br>'_'+ Uom<br>||~~IndicatorKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithm<br>Complete_OEEENG546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEECounter<br>|~~algorithmName+ '_' + Uom or CounterDescription +~~<br>'_'+ Uom<br>||~~Name~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithm<br>Complete_OEEENG546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEECounter<br>|~~algorithmDescription or~~<br>UNICounterDescription<br>||~~Description~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithm<br>OEEEng546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEECounterLink|~~uomvalue or~~<br>ToUOM||~~UomId~~|||
||||~~**IndicatorClass**~~||~~**Algorithm family**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~IndicatorClassSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithmFamily<br>|~~familyDescription or~~<br>'Algorithm' or<br>'Counter'<br>||~~IndicatorClassKey~~<br>|||
|~~LMS24Proj~~<br>|~~OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithmFamily<br>|~~familyDescription or~~<br>'Algorithm' or<br>'Counter'<br>||~~Name~~<br>|||
|~~LMS24Proj~~|~~OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithmFamily|~~familyDescription or~~<br>'Algorithm' or<br>'Counter'||~~Description~~|||
||||~~**IndicatorIndicatorClass**~~||~~**Relationship between KPI and Algorithm**~~<br>**family**||
|~~----~~|~~----~~|~~smallint~~||~~IndicatorIndicatorClassSiteId~~|||


|LMS24Proj|Complete_OEEEng546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEEAlgorithm,Complete_OEEEng546C<br>3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEEAlgorithmFamily,Complete_OEEEN<br>G546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEECounter,OEEEng546C3276-B61D-<br>47fe-9AF5-66BEE7A3BA76/OEECounterLink|algorithmName+ '_' + Uom + familyDescription or<br>algorithmName+ '_' + Uom + 'Algorithm' or<br>CounterDescription + '_'+ Uom + 'Counter'|Col4|IndicatorIndicatorClassKey|Col6|Col7|
|---|---|---|---|---|---|---|
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~IndicatorId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithm<br>Complete_OEEENG546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEECounter<br>|~~algorithmName+ '_' + Uom or CounterDescription +~~<br>'_'+ Uom<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~IndicatorClassId~~|||
|~~LMS24Proj~~|~~OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEAlgorithmFamily|~~familyDescription or~~<br>'Algorithm' or<br>'Counter'|||||
||||~~**IndicatorLimit**~~||~~**KPI limit**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~IndicatorLimitSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry<br>equipment_version<br>|~~AlgorithmName +'_' + FullPath + '_' +  StartTime~~<br>||~~IndicatorLimitKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~IndicatorId~~|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry|~~AlgorithmName+ '_' + UOM~~<br>|||||
|~~----~~<br>||~~smallint~~<br>||~~EquipmentId~~|||
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>|||||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry<br>|~~StartTime~~<br>||~~StartDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry<br>|~~EndTime~~<br>||~~EndDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry<br>|~~UOM~~<br>||~~UomId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry<br>|~~when BasedOnTime = 0 then null else 's'~~<br>||~~BaseOnTimeUomId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry<br>|~~when BasedOnTime = 0 then TargetValue else~~<br>TargetValue/TargetTimeNormalization<br>||~~Target~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETargetRegistry|~~when IsAlarm = 0 then 1 else 0~~||~~HighIsBetter~~|||
||||~~**MaterialDefinition**~~||~~**Product**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~MaterialDefinitionSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounterTable<br>|~~ProductId~~<br>||~~MaterialDefinitionKey~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounterTable<br>|~~ProductId~~<br>||~~Description~~<br>|||
|~~LMS24Proj~~|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounterTable|~~ProductId~~||~~Name~~|||
||||~~**OperationExecution**~~||~~**Order**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~OperationExecutionSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounterTable<br>|~~OrderId~~<br>||~~OperationExecutionKey~~<br>|||
|~~LMS24Proj~~|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounterTable|~~OrderId~~||~~Name~~|||
||||~~**Reason**~~||~~**Reason**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ReasonSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~IDObj~~<br>||~~ReasonKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~coalesce(UNIStateDescription,StateDescription)~~<br>||~~Description~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~StateDescription~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList|~~StateColor~~||~~Color~~|||


|LMS24Proj|Complete_OEEEng546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEEStateList|isStop|Col4|IsStop|Col6|Col7|
|---|---|---|---|---|---|---|
||||~~**ReasonTree**~~||~~**Reason tree**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ReasonTreeSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEReasonTreeAnag<br>|~~name~~<br>||~~ReasonTreeKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEReasonTreeAnag<br>|~~name~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEReasonTreeAnag|~~Description~~||~~Description~~|||
||||~~**ReasonTreeItem**~~||~~**Reason tree item**~~||
|||~~smallint~~<br>||~~ReasonTreeItemSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEReasonTree<br>|~~PPAObjectId~~<br>||~~ReasonTreeItemKey~~<br>|||
|~~----~~|~~----~~<br>|~~smallint~~<br>||~~ReasonTreeId~~<br>|||
||~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEReasonTreeAnag<br>|~~Name~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentTimeCategoryId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEETimeModelItem<br>|~~PPAObjectId~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~StatusId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe~~<br>-9AF5-66BEE7A3BA76/OEEStateList<br>|~~IDObj~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~CauseId~~|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe~~<br>-9AF5-66BEE7A3BA76/OEEStateList<br>|~~IDObj~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ReasonId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe~~<br>-9AF5-66BEE7A3BA76/OEEStateList<br>|~~IDObj~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~DetailedReasonId~~|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe~~<br>-9AF5-66BEE7A3BA76/OEEStateList|~~IDObj~~|||||
||||~~**Shift**~~||~~**Shift**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ShiftSiteId~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~SHC_SHIFT_TEMPLATE~~<br>|~~id~~<br>||~~ShiftKey~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~SHC_SHIFT_TEMPLATE~~<br>|~~coalesce(label, ID)~~<br>||~~name~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~SHC_SHIFT_TEMPLATE~~<br>|~~coalesce(label, ID)~~<br>||~~description~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~SHC_WORKING_TIME~~<br>|~~work_start~~<br>||~~StartTime~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~SHC_WORKING_TIME~~<br>|~~work_end~~<br>||~~EndTime~~<br>|||
|~~SITMESDB_LMS24~~|~~SHC_WORKING_TIME~~|~~1 or 0~~||~~IsDayAfter~~|||
||||~~**Status**~~||~~**Status**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~StatusSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~IDObj~~<br>||~~StatusKey~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~StateDescription~~<br>||~~Name~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~COALESCE(UNIStateDescription,StateDescription)~~<br>||~~Description~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList<br>|~~StateColor~~<br>||~~Color~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEStateList|~~IsStop~~||~~IsStop~~|||
||||~~**Uom**~~||~~**Unit of Measure**~~||
|~~SITMESDB_LMS24~~<br>|~~dbo.MESUoMs~~<br>|~~UomID~~<br>||~~UomKey~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~dbo.MESUoMs~~<br>|~~UomName~~<br>||~~Name~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~dbo.MESUoMs~~<br>|~~Descript~~<br>||~~Description~~<br>|||
|~~----~~|~~----~~|~~1~~||~~UomSystemId~~|||


|----|----|1|Col4|UomCategoryId|Col6|Col7|
|---|---|---|---|---|---|---|
||||~~**WorkingTimeException**~~||~~**Shift calendar exception**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~WorkingTimeExceptionSiteId~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~SHC_WORK_SCHED_BREAK~~<br>SHC_WORK_SCHED_DAY<br>equipment_version<br>|~~break_start+' '+ FullPath or~~<br>work_start+' '+ FullPath<br>||~~WorkingTimeExceptionKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentId~~|||
|~~SITMESDB_LMS24~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>|||||
|~~SITMESDB_LMS24~~<br>|~~SHC_WORK_SCHED_BREAK~~<br>SHC_WORK_SCHED_DAY<br>|~~break_start or~~<br>work_start<br>||~~StartDateTime~~<br>|||
|~~SITMESDB_LMS24~~<br>|~~SHC_WORK_SCHED_BREAK~~<br>SHC_WORK_SCHED_DAY<br>|~~break_end or~~<br>work_end<br>||~~EndDateTime~~<br>|||
|~~SITMESDB_LMS24~~|~~SHC_WORK_SCHED_BREAK~~<br>SHC_WORK_SCHED_DAY|~~datediff(SECOND, break_start, break_end) or~~<br>datediff(SECOND, work_start, work_end)||~~Duration~~|||
||||~~**EquipmentCapacityValue**~~||~~**Design speed (runtime value)**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentCapacityValueSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedTable<br>|~~$IDArchiveValue +' '+ $IDArchObj+ ' '+ $UniqueDbId~~<br>||~~EquipmentCapacityValueKey~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedTable<br>|~~StartTime~~<br>||~~StartDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedTable<br>|~~EndTime~~<br>||~~EndDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedTable<br>|~~datediff(SECOND, StartTime,~~<br>coalesce(EndTime,getutcdate()))<br>||~~Duration~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedTable<br>|~~DesignSpeedValue~~<br>||~~Value~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentCapacityId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDesignSpeedRegistry<br>|~~Name~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentId~~|||
|~~LMS24Proj~~|~~equipment_version~~|~~FullPath~~|||||
||||~~**EquipmentTimeModel**~~||~~**Equipment State (runtime value)**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentTimeModelSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~$IDArchObj+'_'+$IDArchiveValue+'_'+$UniqueDbId~~<br>||~~EquipmentTimeModelKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentTimeCategoryId~~<br>|||
|~~----~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~TimeCategory~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ReasonTreeItemId~~<br>|||
|~~----~~<br>|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEReasonTree<br>|~~PPAObjectId~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentId~~|||
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>|||||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~StartTime~~<br>||~~StartDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~EndTime~~<br>||~~EndDateTime~~<br>|||
|~~LMS24Proj~~|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable|~~DATEDIFF(S, StartTime, coalesce(EndTime,~~<br>GETUTCDATE()))||~~Duration~~|||
||||~~**EquipmentTimeModelEmulation**~~||~~**Equipment state (contextualized runtime value)**~~|~~**Equipment state (contextualized runtime value)**~~|
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentTimeModelEmulationSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~$IDArchObj+'_'+$IDArchiveValue+'_'+$UniqueDbId~~<br>||~~EquipmentTimeModelEmulationKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentTimeCategoryId~~<br>|||
|~~----~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~TimeCategory~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ReasonTreeItemId~~|||
|~~----~~|~~Complete_OEEEng546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEReasonTree|~~PPAObjectId~~|||||


|----|----|smallint|Col4|EquipmentId|Col6|Col7|
|---|---|---|---|---|---|---|
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~MaterialDefinitionId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~ProductId~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~OperationExecutionId~~|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~OrderID~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~OperationResponseId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~BatchID~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~MaterialLotId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~LotID~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~LaborId~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~UserName~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~ShiftId~~|||
|~~SITMESDB_LMS24~~<br>|~~SHC_WORK_SCHED_DAY~~<br>|~~shc_shift_id~~<br>|||||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~StartTime~~<br>||~~StartDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~EndTime~~<br>||~~EndDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~SHC_WORK_SCHED_DAY~~<br>|~~work_date~~<br>||~~WorkingDate~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~StartTime,EndTime~~<br>||~~Duration~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~duration-break~~<br>||~~DurationNoBreak~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~when HDN <> 0 then 1 else 0~~<br>||~~IsHidden~~<br>|||
|~~LMS24Proj~~<br>|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable<br>|~~when RO <> 0 OR PLANNED <> 0 then 1 else 0~~<br>||~~IsPlanned~~<br>|||
|~~LMS24Proj~~|~~ArchOEERT546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEEDTMTable|~~UserComment~~||~~Comment~~|||
||||~~**IndicatorValue**~~||~~**Counter (runtime value)**~~||
|~~LMS24Proj~~<br>|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounter<br>|~~$UniqueDbId+ '_'+$IDArchObj]+ '_'+$IDArchiveValue~~<br>||~~IndicatorValueKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~IndicatorValueSiteId~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounter<br>OEEEng546C3276-B61D-47fe-9AF5-<br>66BEE7A3BA76/OEECounterLink<br>|~~CounterDescription + ' '+ ToUOM~~<br>||~~IndicatorId~~|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>|||||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~EquipmentId~~|||
|~~LMS24Proj~~<br>|~~equipment_version~~<br>|~~FullPath~~<br>|||||
|~~LMS24Proj~~<br>|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounter<br>|~~StartTime~~<br>||~~StartDateTime~~<br>|||
|~~LMS24Proj~~<br>|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounter<br>|~~EndTime~~<br>||~~EndDateTime~~<br>|||
|~~LMS24Proj~~|~~Complete_OEEENG546C3276-B61D-47fe-9AF5-~~<br>66BEE7A3BA76/OEECounter|~~datediff(SECOND, StartTime, EndTime)~~||~~Duration~~|||


