|Col1|Opcenter Intelligence Model Entities|Col3|
|---|---|---|
|**Attribute**|**Entity**<br>**Feeder**|**Attributes**|
|<site id><br>FeederID<br>FeederID||FeederSiteId<br>FeederKey<br>Name|
|ExternalFeederid<br>NULL|**Labor**|ExternalNumber<br>Description|
|<site_id><br>OperatorID<br>OperatorID||LaborSiteId<br>LaborKey<br>Name|
|NULL<br><site id>|**MaterialConsumption**|Description<br>MaterialConsumptionSiteId|
|PcbID+'_'+McID+'_'+Operation+'_'+TimeDone'_'+CompID<br><site id><br>ProductId||MaterialConsumptionKey<br>PartNumberMaterialDefinitionId|
|<site id><br>ProductId<br><site id>||MaterialDefinitionId<br>MaterialContainerId|
|CompID<br><site id><br>ResourceId||EquipmentId|
|<site id><br>CustomerId<br><site id>||OperationId<br>CustomerId|
|OperationId<br><site id><br>MfgOrderId||OperationExecutionId|
|<site id><br>Program<br>Station||Station<br>RecipeId|
|Slot<br>SubSlot<br>CurrentCost||Slot<br>SubSlot<br>Cost|
|Correction<br>Amount<br>Placed||Correction<br>InitialAmount<br>Placed|
|Dropped<br>TimeDone|**MaterialContainer**|Rejected<br>Timestamp|
|<site_id><br>CompID<br>CompType||MaterialContainerSiteId<br>MaterialContainerKey<br>Type|
|LotNo<br>MnfPartNo<br>Manufacturer||LotNumber<br>ManufacturerPartNumber<br>Manufacturer|
|Supplier<br>Direction<br>SupplyFormName||Supplier<br>Direction<br>SupplyFormName|
|Remark<br>Remark2<br>Remark3||Remark<br>Remark2<br>Remark3|
|ReceiveDate<br><site_id>|**MaterialContainerAction**|ReceiveDate<br>MaterialContainerActionSiteId|
|ActionID<br>Description<br>Description||MaterialContainerActionKey<br>Name<br>Description|
|<site_id><br>McID+'_'+ActionID+'_'+OperatorID+'_'+Timestamp|**MaterialContainerHistory**|MaterialContainerHistorySiteId<br>MaterialContainerHistoryKey|
|<site_id><br>CompID<br><site_id>||MaterialContainerId<br>PartNumberMaterialDefinitionId|
|ProductId<br><site_id><br>OperatorID||LaborId|
|<site_id><br>ActionID<br><site_id>||MaterialContainerActionId<br>FeederId|
|FeederID<br><site_id><br>ResourceId||EquipmentId<br>|
|<site_id><br>MsdLevel<br><site_id>||MsdLevelId<br>MaterialContainerThicknessId|
|Thickness<br>Amount<br>Station||InitialAmount<br>Station<br>|
|Slot<br>SubSlot<br>OpenTimeStamp||Slot<br>SubSlot<br>OpenTimeStamp|
|DryTimeStamp<br>Timestamp<br>Description||DryTimeStamp<br>Timestamp<br>Comment|
|<site_id>|**MaterialInventory**|MaterialInventorySiteId|
|Year+'_'+Month+'_'+CompID<br><site_id>||MaterialInventoryKey<br>|
|ResourceId<br><site_id>||EquipmentId|
|CompID||MaterialContainerId|
|<site_id><br>ProductId||MaterialDefinitionId|
|<site_id><br>OperatorID<br><site_id>||LaborId|
|Status||MaterialContainerStatusId|
|Station||Station|
|Slot||Slot|
|SubSlot||SubSlot|
|Amount||InitialAmount|
|Inventory||Inventory|
|Cost||Cost|
|Errors<br>Used||Errors<br>|
|Correction||Used<br>Correction|
|Currency<br>0 AS bit||Currency<br>|
|expirationdate||IsCurrent<br>ExpirationDateTime|
|Timestamp||Timestamp|
|<site_id>|**MaterialContainerStatus**|MaterialContainerStatusSiteId|
|StatusID<br>StatusName<br>NULL||MaterialContainerStatusKey<br>Name<br>Description|
|<site_id><br>Thickness|**MaterialContainerThickness**|MaterialContainerThicknessSiteId<br>MaterialContainerThicknessKey|
|Thickness<br>Description|**MsdLevel**|Name<br>Description|
|<site_id><br>1' or '2' or '2a' or '3' or '4' or '5' or '5a' or '6'<br>1' or '2' or '2a' or '3' or '4' or '5' or '5a' or '6'||MsdLevelSiteId<br>MsdLevelKey<br>|
|Lowest sensitivity rating; unlimited floor life. Components<br>with this rating can be exposed to ambient room conditions<br>indefinitely without any risk of moisture-induced damage.'<br>or<br>'Maximum safe exposure of 1 Year.'<br>or<br>'Maximum safe exposure of 4 Weeks.'<br>or<br>'Maximum safe exposure of 168 Hours.'<br>or<br>'Maximum safe exposure of 72 Hours.'<br>or<br>'Maximum safe exposure of 48 Hours.'<br>or<br>'Maximum safe exposure of 24 hours.'<br>or<br>'Mandatory baking before use. This is the most sensitive MSL<br>rating. Components with an MSL 6 rating must be baked to<br>force degassing of any moisture before they are used in<br>assembly.'||Name<br>Description|


