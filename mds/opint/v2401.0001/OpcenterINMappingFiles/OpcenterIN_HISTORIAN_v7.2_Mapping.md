|SIMATIC IT Historian 7.2|Col2|Col3|Opcenter Intelligence Model Entities|Col5|SIMATIC IT Historian Model Entities|Col7|
|---|---|---|---|---|---|---|
|~~**DB Name**~~|~~**Entity**~~<br>|~~**Attribute**~~<br>|~~**Entity**~~<br><br>|~~**Attribute - Tables**~~<br>|~~**SIT HST Entity**~~<br><br>|~~**Mapping info**~~<br>|
||||~~**Tag**~~||~~**Tag**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~TagSiteId~~<br>|||
|~~PPA~~<br>|~~TAG~~<br>|~~TagName~~<br>||~~TagKey~~<br>|||
|~~PPA~~<br>|~~TAG~~<br>|~~TagName~~<br>||~~Name~~<br>||~~Tag name~~<br>|
|~~PPA~~<br>|~~TAG~~<br>|~~TagDescription~~<br>||~~Description~~<br>||~~Tag description~~<br>|
|~~PPA~~<br>|~~TAG~~<br>|~~case when TagType in ('I','F','D') then 'Numeric' else 'String'~~<br>||~~TagTypeId~~<br>||~~TagType~~<br>|
|~~PPA~~|~~VISUALIZATION_INFO~~|~~EngUnit~~||~~UomId~~||~~Engineering unit id~~|
||||~~**TagClass**~~||~~**Tag Class**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~TagClassSiteId~~<br>|||
|~~PPA~~<br>|~~CLASS~~<br>|~~ClassID~~<br>||~~TagClassKey~~<br>|||
|~~PPA~~<br>|~~CLASS~~<br>|~~Name~~<br>||~~Name~~<br>||~~Class name~~<br>|
|~~PPA~~|~~CLASS~~|~~[Description]~~||~~Description~~||~~Class description~~|
||||~~**TagTagClass**~~||~~**Relationship between**~~<br>**Tag and Tag Class**||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~TagTagClassSiteId~~<br>|||
|~~PPA~~<br>|~~TAG~~<br>|~~TagName~~<br>||~~TagTagClassKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~TagId~~<br>|||
|~~PPA~~<br>|~~TAG~~<br>|~~TagName~~<br>|~~TagName~~<br>|~~TagName~~<br>|~~TagName~~<br>|~~TagName~~<br>|
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~TagClassId~~|||
|~~PPA~~|~~CLASS~~|~~ClassID~~|~~ClassID~~|~~ClassID~~|~~ClassID~~|~~ClassID~~|
||||~~**TagType**~~||~~**none**~~||
|~~----~~<br>|~~----~~<br>|~~"String" or "Numeric"~~<br>||~~TagTypeKey~~<br>|||
|~~----~~|~~----~~|~~"String" or "Numeric"~~||~~Name~~|||
||||~~**TagValue**~~||~~**Tag Value**~~||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~TagValueSiteId~~<br>|||
|~~PPA~~<br>|~~TAG,[View_Read_FLOATArchive] OR~~<br>TAG,[View_Read_REALTIMEFLOATArchive] OR<br>TAG,[View_Read_INTArchive] OR<br>TAG,[View_Read_REALTIMEINTArchive] OR<br>TAG,[View_Read_DIGITArchive] OR<br>TAG,[View_Read_REALTIMEDIGITArchive] OR<br>TAG,[View_Read_STRINGArchive]<br>|~~[TagName]  + '_FloatArchive_' + ('1970-01-01'+[time]) OR~~<br>[TagName]  + '_RealtimeFloatArchive_' + ('1970-01-01'+[time]) OR<br>[TagName]  + '_IntArchive_' + ('1970-01-01'+[time]) OR<br>[TagName]  + '_RealtimeIntArchive_' + ('1970-01-01'+[time]) OR<br>[TagName]  + '_DigitArchive_' + ('1970-01-01'+[time]) OR<br>[TagName]  + '_RealtimeDigitArchive_' + ('1970-01-01'+[time]) OR<br>[TagName]  + '_StringArchive_'' + ('1970-01-01'+[time])<br>||~~TagValueKey~~<br>|||
|~~----~~<br>|~~----~~<br>|~~smallint~~<br>||~~TagId~~|||
|~~PPA~~<br>|~~TAG~~<br>|~~TagName~~<br>|~~TagName~~<br>|~~TagName~~<br>|~~TagName~~<br>|~~TagName~~<br>|
|~~PPA~~|~~[View_Read_FLOATArchive] OR~~<br>[View_Read_REALTIMEFLOATArchive] OR<br>[View_Read_INTArchive] OR<br>[View_Read_REALTIMEINTArchive] OR<br>[View_Read_DIGITArchive] OR<br>[View_Read_REALTIMEDIGITArchive] OR<br>[View_Read_STRINGArchive]|~~'1970-01-01'+[time]~~||~~EventDateTime~~||~~Tag value timestamp~~|


|PPA|[View_Read_FLOATArchive] OR<br>[View_Read_REALTIMEFLOATArchive] OR<br>[View_Read_INTArchive] OR<br>[View_Read_REALTIMEINTArchive] OR<br>[View_Read_DIGITArchive] OR<br>[View_Read_REALTIMEDIGITArchive]|Value OR null|Col4|FloatValue|Col6|Value (in case of float, int, digit)|
|---|---|---|---|---|---|---|
|~~PPA~~|~~[View_Read_STRINGArchive]~~|~~Value OR null~~||~~StringValue~~||~~Value (in case of string)~~|
||||~~**Uom**~~||~~**Engineering unit**~~||
|~~PPA~~<br>|~~VISUALIZATION_INFO~~<br>|~~EngUnit~~<br>||~~UomKey~~<br>|||
|~~PPA~~<br>|~~VISUALIZATION_INFO~~<br>|~~EngUnit~~<br>||~~Name~~<br>|||
|~~----~~<br>|~~----~~<br>|~~1~~<br>||~~UomSystemId~~<br>|||
|~~----~~|~~----~~|~~1~~||~~UomCategoryId~~|||


