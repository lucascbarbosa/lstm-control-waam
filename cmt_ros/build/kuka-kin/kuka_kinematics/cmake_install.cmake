# Install script for directory: /home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_kinematics

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kinematics/srv" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_kinematics/srv/SolvePositionIK.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kinematics/cmake" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_kinematics/catkin_generated/installspace/kuka_kinematics-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/include/kuka_kinematics")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/share/roseus/ros/kuka_kinematics")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/share/common-lisp/ros/kuka_kinematics")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/share/gennodejs/ros/kuka_kinematics")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/lib/python3/dist-packages/kuka_kinematics")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/lib/python3/dist-packages/kuka_kinematics")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_kinematics/catkin_generated/installspace/kuka_kinematics.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kinematics/cmake" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_kinematics/catkin_generated/installspace/kuka_kinematics-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kinematics/cmake" TYPE FILE FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_kinematics/catkin_generated/installspace/kuka_kinematicsConfig.cmake"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_kinematics/catkin_generated/installspace/kuka_kinematicsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kinematics" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_kinematics/package.xml")
endif()

