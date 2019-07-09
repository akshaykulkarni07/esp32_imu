# esp32_imu
Repository for interfacing ESP32 DevKit v1 with MPU6050 IMU sensor and publishing IMU readings to ROS over Wi-Fi. This is part of my internship project of Tower Robogame at [AIRLab, PoliMi](http://airlab.deib.polimi.it/)

### Dependencies
- [ROS](http://wiki.ros.org/ROS/Installation) must be installed in laptop (or PC)
- [Arduino IDE](https://www.arduino.cc/en/Main/Software) must be installed in laptop (or PC) 
- Arduino rosserial must be installed (see [this link](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup))
- ESP32 boards software must be installed in Arduino IDE through the Boards Manager
- Download [MPU6050_tockn](https://github.com/tockn/MPU6050_tockn) library and save in `<installation_location>/Arduino/libraries` path

### Connections between ESP32 DevKit v1 and MPU6050 
| ESP32 DevKit v1  | MPU6050 IMU sensor |
| ------------- | ------------- |
| 3V3  | VCC  |
| GND  | GND  |
| D21  | SDA  |
| D22  | SCL  |

Note : If you are using external power supply (to `VIN` pin), then remember to have common ground for all 3 (ESP, IMU and power supply).

### Usage 
- Open a terminal and do `roscore` to start the ROS master. 
- Do `ifconfig` in another terminal and find your IP address (it is also the IP address of the ROS master)
- Configure your Wi-Fi SSID, password and the ROS master IP address in the `imu_esp_ros.ino` file
- Upload the `imu_esp_ros.ino` file to the ESP32 board through Arduino IDE
- Open another terminal and run `rosrun rosserial_python serial_node.py tcp`. This should allow the ESP32 to publish and subscribe to topics on the PC ROS master.
- Open another terminal and run `rostopic echo /imu_data` to check the output or `rqt_plot` to visualize the IMU data.

Note : In case the ESP32 does not connect when you do `rosrun rosserial_python serial_node.py tcp`, then press the `EN` button on the ESP32.

Note : If you are using an Arduino without Wi-Fi but connected through USB, just use `rosrun rosserial_python serial_node.py /dev/ttyUSB*` where you should replace the * by a number that you can find if you use `ls /dev/ttyUSB`. Sometimes, the command could be `ls /dev/ttyACM`.
