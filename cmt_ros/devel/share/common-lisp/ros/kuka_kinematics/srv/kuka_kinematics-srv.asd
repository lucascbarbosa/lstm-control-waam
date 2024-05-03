
(cl:in-package :asdf)

(defsystem "kuka_kinematics-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "SolvePositionIK" :depends-on ("_package_SolvePositionIK"))
    (:file "_package_SolvePositionIK" :depends-on ("_package"))
  ))