
## Overview

Openpilot is a driver-assistance system, which supports [a number of cars](https://github.com/commaai/openpilot/blob/master/docs/CARS.md). 

Some parts of the software are released under licenses which restrict commercial use.

Only the [Body submodule](https://github.com/commaai/body/tree/0e74db67ae6aaa7c30054bd4335dcafe69a5aa72) has the restrictive GNU General Public License v3.0. All other repositories have the MIT license.

The [tuning guide](https://github.com/commaai/openpilot/wiki/Tuning) by them is a cool resource for getting PID control right.

## Requirements

You need to buy [relatively expensive](https://docs.comma.ai/), custom hardware device, and a harness to attach it. Only components of the software may be useful to us.

## Technical Details

The modules that may pose value to us, and their potential use, are below.

- Components use [msgq](https://github.com/commaai/msgq/tree/74074d650f5d516a33962c1681a2a15b1d603537) to communicate. The library's pub/sub mechanism is already present in ROS. The component for sharing large contiguous buffers could be useful for efficient Lidar processing.

- The [rednose](https://github.com/commaai/rednose/tree/72b3479bababc658f24cc7aa0dc8bb550f0474fc) repo has an implementation of Kalman Filtering, including incorporating visual features as observations. Would be a good starting point to improve our localisation accuracy.

- The [teleoprtc](https://github.com/commaai/teleoprtc/tree/fdcff87aaf2b1ca099be4fc820044334cec02cc5) repo has some abstractions over WebRTC. A good reference if we ever want low-latency streaming of data to the browser.

The `tools` directory has useful utilities. Some highlights are:

- [joystick](https://github.com/commaai/openpilot/tree/master/tools/joystick) is an example of using a library to interface a robot with many common controllers. It relies on custom networking code though, and would need some adaptation.

- [latencylogger](https://github.com/commaai/openpilot/tree/master/tools/latencylogger) can create graphs from timestamp logs. Could be useful to determine delays in the stack if there's a need. Requires access to source code for logging messages to be added.

- [plotjuggler](https://github.com/commaai/openpilot/tree/master/tools/plotjuggler) is a good example for creating time-series graphs. Can also create plots for tuning control.

- [sim](https://github.com/commaai/openpilot/tree/master/tools/sim) shows how to leverage open-source simulators.
