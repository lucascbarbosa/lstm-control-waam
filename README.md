# lstm-control-waam

Final project for my graduation envolving application of a LSTM neural network coupled with MPC in the optimization of a single bead geometry welded through WAAM. The MPC communicates with the outside world via ROS nodes.

# Description

This project has 3 components:  \

1. Process model (PM): The model used to identify the process dynamics and modelling it, used in the MPC as the predictive model of the system.

2. Gradient model (GM): The model used to estimate the gradients of PM.

3. MPC: The controller itself, with the optimizer, the predictive model (PM) and the gradient model (GM).

The workflow in divided in 3 main parts: data generation, models training and MPC deployment in ROS.

## Data generation

## Models training

## MPC deployment
