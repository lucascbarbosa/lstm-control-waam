# Install script for directory: /home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_rsi_simulator

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_simulator/catkin_generated/installspace/kuka_rsi_simulator.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_rsi_simulator/cmake" TYPE FILE FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_simulator/catkin_generated/installspace/kuka_rsi_simulatorConfig.cmake"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_simulator/catkin_generated/installspace/kuka_rsi_simulatorConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_rsi_simulator" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_rsi_simulator/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_simulator/scripts" TYPE PROGRAM FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_rsi_simulator/scripts/kuka_rsi_simulator")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_simulator/scripts" TYPE PROGRAM FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_rsi_simulator/scripts/kuka_rsi_simulator_external")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_rsi_simulator" TYPE DIRECTORY FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_rsi_simulator/launch")
endif()

