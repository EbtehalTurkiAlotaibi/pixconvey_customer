
# Delivery Autonomous Mode Description

- Be sure that the Emergency button is released.
- Start always from the starting point because no localization unless starting there.
- Connect to the robot's PC:
  - Using NoMachine:
    - It seems the university WiFi blocks accessing the robot, use a portable router.
    - Connect the PC and robot to the same WiFi/wired network.
    - Use exactly the IP and port of the NoMachine server.
    - User: `coolpi`, Password: `coolpi`.
    - Disconnect the monitor of the robot and insert the fake HDMI dongle.
    - If NoMachine gives “Querying server …” try in the command: `/etc/NX/nxserver –start`

## 1. Direct through Command Line:

### First Terminal
Initiate the ROS core processes by entering 'roscore.'

```bash
cd
roscore
```


### Second Terminal

Navigate to the outdoor-arm directory, configure the environment, and the main program using the provided commands.

```bash
cd
cd outdoor-arm
source devel/setup.bash
cd src/scripts/
./delivery.sh
```

### Third Terminal
Send the nodes to be driven between.

```bash
cd outdoor-arm
source devel/setup.bash
cd src/scripts/
rosservice call /deliver_routing_node/routing_delivery '{"id_list":["10000","10001"]}'
```


### Fourth Terminal
Open the cargo when needed.

```bash
cd outdoor-arm
source devel/setup.bash
rostopic pub /lock_ctl std_msgs/Bool "data: true"
```



## 2. Through the AWS Command Line (example for robot2 000002):
- Using AWS credentials, AWS Management Console > EC2 > pixconvey_4_28 instance > Connect
- Through AWS terminal, pass these commands:
  
### To open the cargo:

```bash
mosquitto_pub -h 51.20.236.180 -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/control/door/000002" -m "{\"timestamp\":1600050933000,\"taskId\":\"180\",\"doorControl\":0}"![image](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/assets/8040282/be0d6699-50e0-492c-b55f-15275333ebc4)
```

### To send from 10000 to 10001:
```bash
mosquitto_pub -h 51.20.236.180 -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/driving/path/000002" -m "{\"timestamp\":1697683950,\"taskId\":123456,\"businessType\":3,\"stopPointList\":[{\"nodeID\":\"10000\"},{\"nodeID\":\"10001\"}]}"

or 
mosquitto_pub -h 51.20.236.180 -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/driving/path/000002" -m "{\"timestamp\":1600050933000,\"taskId\":\"180\",\"businessType\":1,\"stopPointsList\":{\"id_list\":["10000","10001"]}}"
```

## Through the 3D party application:
- [cloud-based dashboard](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/blob/main/cloud_based_manuals/nodered_AWS_instance.md)
- [python code](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/blob/main/access_commands/third_party_app.py)



