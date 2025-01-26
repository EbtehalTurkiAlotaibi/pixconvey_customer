
## On the AWS Server Side

1. **Set Up an Ubuntu Server**
-  [Creating a Key Pair and a Security Group for AWS EC2](https://www.youtube.com/watch?v=iH02htvyXck)
-  [Understanding Security Groups in AWS](https://www.youtube.com/watch?v=WoQfOugwzlU)
-  [Launching an EC2 Instance with a Custom Security Group](https://www.youtube.com/watch?v=t4RHgNk1EqY&t=7s)

2. **Install MQTT on the Server**
   ```bash
    sudo apt-get update
  	 sudo apt instal mosquitto
  	 sudo apt install mosquitto
  	 sudo apt install mosquitto-clients

   
3. **Configure the MQTT Server**

- Edit the mosquitto.conf file:
   ```bash
   sudo vi /etc/mosquitto/mosquitto.conf

- Add the following five lines of code to mosquitto.conf
   ```bash
   include_dir /etc/mosquitto/conf.d
   allow_anonymous false
   password_file /etc/mosquitto/pwfile
   acl_file /etc/mosquitto/aclfile
   listener 1883


- Copy aclfile.example to aclfile:
   ```bash
   sudo cp aclfile.example aclfile
- Ensure aclfile content matches the provided configuration:


  <img width="412" alt="image" src="https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/assets/8040282/0b210447-f269-4d36-897d-b9fccda9a91f">

- Copy pwfile.example to pwfile:
   ```bash
   sudo cp pwfile.example pwfile
   sudo mosquitto_passwd -c /etc/mosquitto/pwfile Pixconvey

- Use Pixconvey as the password.
- [Set Up Security Groups](https://www.youtube.com/watch?v=WoQfOugwzlU)


4. **Test the Setup**

- From AWS terminal, subscribe to the MQTT topic:
  
   ```bash
   mosquitto_sub -h <AWS_SERVER_IP> -p 1883 -t 111 -u Pixconvey -P Pixconvey

- Publish a message from your local machine:

   ```bash
   mosquitto_pub -h <AWS_SERVER_IP> -p 1883 -t 111 -u Pixconvey -P Pixconvey -m 55


- Verify that 55 is received on the server.

- Replace `<AWS_SERVER_IP>` with the actual IP address of your AWS server.

5. **On the Robot Server Side**

- Copy the interaction_delivery folder to /interaction_delivery on the robot.
- From the AWS terminal, execute the following commands to test:
   ```bash
   mosquitto_pub -h <AWS_SERVER_IP> -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/control/door/000002" -m {\"timestamp\":1600050933000,\"taskId\":\"180\",\"doorControl\":0}"


   mosquitto_pub -h <AWS_SERVER_IP> -p 1883 -u Pixconvey -P Pixconvey -t "/cloud/driving/path/000002" -m "{\"timestamp\":1600050933000,\"taskId\":\"180\",\"path\":{\"id_list\":[\"10000\",\"10001\"]}}"


