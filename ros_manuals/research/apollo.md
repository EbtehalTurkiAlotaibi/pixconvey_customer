## Overview

Apollo can achieve full autonomy with a restrive set of hardware (see requirements). The deep neural networks for perception and reinforcement learning are modern solutions.

The use of HD maps is analogous to our application. Beside a full self-driving stack, it features a cloud service layer and a drive-by-wire interface. The data pipeline in the service layer could be useful. 

They rely heavily on Docker for testing and deployment.

The stack levarages a wide range of sensors, including Lidar and radar.

## Requirements

The suggested hardware is:

- NVIDIA Turing GPU / AMD GFX9/RDNA/CDNA GPU
- A machine with a 8-core processor and 16GB memory minimum

## Localisation and Mapping

Apollo has 3 localisation modes: 

- MSF - Multi-sensor fusion
- NDT - Normal distribution transform
- RTK - Real-time Kinematic.

There are graphical utilities and statistics tools for comparing RTK path data to localisation in an HD map.

The `OpenStreetMap` map representation format is used for intelligent decision making.

They have a tool for detecting problems in data collection files used for creating maps. A similar tool could greatly improve the mapping process for us.

For building HD maps, they use a multiple LiDAR and GNSS setup that [requires calibration](https://github.com/ApolloAuto/apollo/blob/master/docs/06_Perception/multiple_lidar_gnss_calibration_guide.md). They also suggest using base stations with the GNSS.

On a positive note, the docs pointed me to the `pcl-tools` package that has useful tools like `pcl_viewer`.
