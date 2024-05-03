# Install script for directory: /home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/src

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
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install" TYPE PROGRAM FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install" TYPE PROGRAM FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/setup.bash;/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install" TYPE FILE FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/setup.bash"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/setup.sh;/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install" TYPE FILE FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/setup.sh"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/setup.zsh;/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install" TYPE FILE FILES
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/setup.zsh"
    "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/install" TYPE FILE FILES "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/gtest/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_experimental/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_resources/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_simulator/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/rqt_joint_trajectory_controller/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/hks_msgs/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_msgs/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/cmt_ros_pkg/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_remap/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_dkp400_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kp2_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kr10_dkp400_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kr10_kp2_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kr10_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kr30_dkp400_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kr30_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kr90_kp2_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_kr90_support/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_kinematics/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_hw_interface/cmake_install.cmake")
  include("/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/kuka-kin/kuka_experimental/kuka_rsi_velocity_interface/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/lbarbosa/Documents/Github/lstm-control-waam/cmt_ros/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
