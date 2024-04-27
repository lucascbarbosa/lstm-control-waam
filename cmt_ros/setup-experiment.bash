echo Control
mate-terminal \
  --tab-with-profile="Cell" -e "distrobox enter 'noetic'" \
  --tab-with-profile="Roscore" -e "distrobox enter 'noetic'" \
  --tab-with-profile="Rostopic" -e "distrobox enter 'noetic'" 

    
distrobox enter noetic ; catkin_make ; source devel/setup.bash
