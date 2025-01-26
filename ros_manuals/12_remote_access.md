## Requirements
    
- The delivery vehicle
- ROS (tested on Noetic)
- A portable router
- The full `outdoor-arm` package, in the home directory of the delivery vehicle
- The corrected map files
- Waypoint and route graph files

# Remote Delivery

Be sure that the Emergency button is released and that the robot is at the starting point give by the first node in `route_graph.json`.

To establish a connection to the robot, you need a portable router. Eduroam's firewall seems to block connections. Create a wireless access point and connect both your computer and the robot. 

# Using NoMachine


You may need to run the command

```
/etc/NX/nxserver –start
```
if `NoMachine` gives “Querying server …”.

# Using AWS terminal

Use the following AWS creditials
- email: `pix.convey@gmail.com`
- password: `Pixconvey2023$$$$`

and connect to the robot via
```
AWS management console > EC2 > pixconvey_4_28 instance > Connect
```
Through AWS terminal pass this command to open the cargo:
```
mosquitto_pub -h 51.20.236.180 -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/control/door/000002" -m "{\"timestamp\":1600050933000,\"taskId\":\"180\",\"doorControl\":0}"
```
To send from 10000 to 10001 the cargo:
```
mosquitto_pub -h 51.20.236.180 -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/driving/path/000002" -m "{\"timestamp\":1697683950,\"taskId\":123456,\"businessType\":3,\"stopPointList\":[{\"nodeID\":\"10000\"},{\"nodeID\":\"10001\"}]}"
```

or 
```
mosquitto_pub -h 51.20.236.180 -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/driving/path/000002" -m "{\"timestamp\":1600050933000,\"taskId\":\"180\",\"businessType\":1,\"stopPointsList\":{\"id_list\":["10000","10001"]}}"
```