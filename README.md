# Introduction
The inverted pendulum on a cart is a challenging problem for modeling, simulation, and control, since the inverted pendulum is inherently unstable (the pendulum easily goes to the bottom position) and also non-linear dynamics (fortunately, it's not that non-linear for a small angle). This model is a fundamental benchmark for highly unstable system with slightly non-linear dynamics such as crane controlling, SpaceX vertical landing thrust vector control, vehicle stabilization.

This project has 2 main tasks which are
1. Model and simulate the inverted pendulum on a cart
2. Control the stick to be up-right and at the center (with cascade PID, optimal controller, or ML)

# The Modeling
Since I haven't study any course of engineering dynamics, so I don't know about the Lagrangian mechanics which is one of the most convinient way to find the equation of motion. Therefore, I must use some background knowledges about Newtonian mechanics, Rotational motion, and especially the concept about non-inertial frame of reference & ficticious forces, because the motion of pendulum will be analyzed by observing on the cart.

# Cascade PID control
The simplest linear controller is PID, so we'll implement this as our first controller. However, the single loop PID can't stabilize and control the cart position at the same time; therefore, we'll use 2-loop cascade control with overide control. The idea is using the cart position control as the outer loop. The outer loop will send angle setpoint signals to the inner loop; however, if that signal is much deviate from the up-right equilibrium angle, the controller will fail. Therefore, we need to add an overide control system to stabilize the pendulum before controlling the cart position by adding the setpoint constraints to not over or lower than the limits.

Our sub-task for this controller is to tune the PID controller in the inner and outer loop. (Ziegler-Nichols might not works :moyai:)