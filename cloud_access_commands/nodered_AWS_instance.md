**AWS EC2 and Security Groups Tutorials**

1. [Creating a Key Pair and a Security Group for AWS EC2](https://www.youtube.com/watch?v=iH02htvyXck)
2. [Understanding Security Groups in AWS](https://www.youtube.com/watch?v=WoQfOugwzlU)
3. [Launching an EC2 Instance with a Custom Security Group](https://www.youtube.com/watch?v=t4RHgNk1EqY&t=7s)

**Node-RED Library Installation Guide**

4. To install the necessary libraries from the Node-RED manage palette, follow the steps shown below:

   ![Node-RED Palette Installation](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/assets/8040282/b59065c1-7531-4827-9b94-2a924b0be5c6)

5. Ensure you have installed the following libraries:

   ![Required Libraries](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/assets/8040282/2b7a6a57-513e-4d41-a13a-960d5ff63e7c)
   ![Additional Libraries](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/assets/8040282/e29d9679-b48f-42e2-930e-ab9b31ef1d4b)

6. Paste the JSON flow file into Node-RED:

   ![JSON Flow File](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/assets/8040282/3c15aeb1-1ee4-4273-a091-3ecb200d11a4)

7. [MVP Dashboard Code Example](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/blob/main/cloud_based/mvp_dashboard_flows.json)





**Connecting to robot-AWS cloud**
8. From the flow, go to mqtt node, edit as follow: 

<img width="631" alt="Screen Shot 2024-07-14 at 9 48 52 PM" src="https://github.com/user-attachments/assets/16d284d2-f040-44e6-b406-c906a9f08d86">

9. Edit the AWS-robot, update the IP to the robot AWS address:
 <img width="450" alt="Screen Shot 2024-07-14 at 9 49 57 PM" src="https://github.com/user-attachments/assets/f4af2430-372b-4b6b-a0dc-5e083183a0e4">

10. Move to the security tabe and add username and password of the robot
 <img width="481" alt="Screen Shot 2024-08-08 at 3 23 42 PM" src="https://github.com/user-attachments/assets/045659af-3df5-40a6-aaae-c8f90bcd3078">


**Reading MQTT Messages**

11. Use the debug node to read MQTT messages from the debug console. Connect the debug node to the output of the `mqtt_in` node to view incoming MQTT messages in the console
      ![JSON Flow File](https://github.com/EbtehalTurkiAlotaibi/Pixconvey_manuals/assets/8040282/401e1426-ca42-42a6-986d-2a79c28c2693)
   
    Example output messages will appear in the debug console (right-side panel).



    ================
