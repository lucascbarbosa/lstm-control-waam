# Install script for directory: /home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_rsi_velocity_interface

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_velocity_interface/catkin_generated/installspace/kuka_rsi_velocity_interface.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_rsi_velocity_interface/cmake" TYPE FILE FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_velocity_interface/catkin_generated/installspace/kuka_rsi_velocity_interfaceConfig.cmake"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_velocity_interface/catkin_generated/installspace/kuka_rsi_velocity_interfaceConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_rsi_velocity_interface" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src/kuka-kin/kuka_experimental/kuka_rsi_velocity_interface/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libkuka_velocity_interface.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libkuka_velocity_interface.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libkuka_velocity_interface.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/lib/libkuka_velocity_interface.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libkuka_velocity_interface.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libkuka_velocity_interface.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libkuka_velocity_interface.so"
         OLD_RPATH "/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libkuka_velocity_interface.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface" TYPE EXECUTABLE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node"
         OLD_RPATH "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/lib:/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface" TYPE EXECUTABLE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table"
         OLD_RPATH "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/devel/lib:/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/kuka_rsi_velocity_interface/kuka_velocity_interface_node_virtual_table")
    endif()
  endif()
endif()
