# Install script for directory: /home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_kp2_support

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kp2_support/catkin_generated/installspace/kuka_kp2_support.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kp2_support/cmake" TYPE FILE FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kp2_support/catkin_generated/installspace/kuka_kp2_supportConfig.cmake"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kp2_support/catkin_generated/installspace/kuka_kp2_supportConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kp2_support" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_kp2_support/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kp2_support" TYPE DIRECTORY FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_kp2_support/config"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_kp2_support/launch"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_kp2_support/meshes"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_kp2_support/urdf"
    )
endif()

