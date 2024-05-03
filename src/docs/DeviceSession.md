# DeviceSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | **str** | Session UID | [optional] 
**device** | **str** | Device UID | [optional] 
**sn** | **str** | Device Serial Number | [optional] 
**product** | **str** | Product UID | [optional] 
**fleets** | **List[str]** | Array of Fleet UIDs | [optional] 
**cell** | **str** | Cell ID where the session originated and quality (\&quot;mcc,mnc,lac,cellid\&quot;) | [optional] 
**scan** | **bytearray** |  | [optional] 
**triangulate** | **object** |  | [optional] 
**rssi** | **float** |  | [optional] 
**sinr** | **float** |  | [optional] 
**rsrp** | **float** |  | [optional] 
**rsrq** | **float** |  | [optional] 
**bars** | **float** |  | [optional] 
**rat** | **str** |  | [optional] 
**bearer** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**bssid** | **str** |  | [optional] 
**ssid** | **str** |  | [optional] 
**iccid** | **str** |  | [optional] 
**apn** | **str** |  | [optional] 
**tower** | [**TowerLocation**](TowerLocation.md) |  | [optional] 
**tri** | [**TowerLocation**](TowerLocation.md) |  | [optional] 
**when** | **float** | Last known capture time of a note routed through this session | [optional] 
**where_when** | **float** |  | [optional] 
**where** | **str** | Where OLC | [optional] 
**where_lat** | **float** |  | [optional] 
**where_lon** | **float** |  | [optional] 
**where_location** | **str** |  | [optional] 
**where_country** | **str** |  | [optional] 
**where_timezone** | **str** |  | [optional] 
**usage_actual** | **bool** |  | [optional] 
**voltage** | **float** |  | [optional] 
**temp** | **float** |  | [optional] 
**continuous** | **bool** |  | [optional] 
**tls** | **bool** |  | [optional] 
**work** | **float** | Last time work was done for this session | [optional] 
**events** | **float** | Number of events routed | [optional] 
**moved** | **float** |  | [optional] 
**orientation** | **str** |  | [optional] 
**hp_secs_total** | **float** |  | [optional] 
**hp_secs_data** | **float** |  | [optional] 
**hp_secs_gps** | **float** |  | [optional] 
**hp_cycles_total** | **float** |  | [optional] 
**hp_cycles_data** | **float** |  | [optional] 
**hp_cycles_gps** | **float** |  | [optional] 
**period** | [**DeviceUsage**](DeviceUsage.md) |  | [optional] 

## Example

```python
from notehub_py.models.device_session import DeviceSession

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSession from a JSON string
device_session_instance = DeviceSession.from_json(json)
# print the JSON string representation of the object
print(DeviceSession.to_json())

# convert the object into a dict
device_session_dict = device_session_instance.to_dict()
# create an instance of DeviceSession from a dict
device_session_from_dict = DeviceSession.from_dict(device_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


