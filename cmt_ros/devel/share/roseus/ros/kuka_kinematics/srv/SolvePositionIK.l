;; Auto-generated. Do not edit!


(when (boundp 'kuka_kinematics::SolvePositionIK)
  (if (not (find-package "KUKA_KINEMATICS"))
    (make-package "KUKA_KINEMATICS"))
  (shadow 'SolvePositionIK (find-package "KUKA_KINEMATICS")))
(unless (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIK")
  (make-package "KUKA_KINEMATICS::SOLVEPOSITIONIK"))
(unless (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST")
  (make-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(unless (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKRESPONSE")
  (make-package "KUKA_KINEMATICS::SOLVEPOSITIONIKRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(intern "*SEED_AUTO*" (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(shadow '*SEED_AUTO* (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(defconstant kuka_kinematics::SolvePositionIKRequest::*SEED_AUTO* 0)
(intern "*SEED_USER*" (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(shadow '*SEED_USER* (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(defconstant kuka_kinematics::SolvePositionIKRequest::*SEED_USER* 1)
(intern "*SEED_CURRENT*" (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(shadow '*SEED_CURRENT* (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(defconstant kuka_kinematics::SolvePositionIKRequest::*SEED_CURRENT* 2)
(intern "*SEED_NS_MAP*" (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(shadow '*SEED_NS_MAP* (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKREQUEST"))
(defconstant kuka_kinematics::SolvePositionIKRequest::*SEED_NS_MAP* 3)

(defun kuka_kinematics::SolvePositionIKRequest-to-symbol (const)
  (cond
        ((= const 0) 'kuka_kinematics::SolvePositionIKRequest::*SEED_AUTO*)
        ((= const 1) 'kuka_kinematics::SolvePositionIKRequest::*SEED_USER*)
        ((= const 2) 'kuka_kinematics::SolvePositionIKRequest::*SEED_CURRENT*)
        ((= const 3) 'kuka_kinematics::SolvePositionIKRequest::*SEED_NS_MAP*)
        (t nil)))

(defclass kuka_kinematics::SolvePositionIKRequest
  :super ros::object
  :slots (_pose_stamp _seed_angles _seed_mode ))

(defmethod kuka_kinematics::SolvePositionIKRequest
  (:init
   (&key
    ((:pose_stamp __pose_stamp) (instance geometry_msgs::PoseStamped :init))
    ((:seed_angles __seed_angles) (instance sensor_msgs::JointState :init))
    ((:seed_mode __seed_mode) 0)
    )
   (send-super :init)
   (setq _pose_stamp __pose_stamp)
   (setq _seed_angles __seed_angles)
   (setq _seed_mode (round __seed_mode))
   self)
  (:pose_stamp
   (&rest __pose_stamp)
   (if (keywordp (car __pose_stamp))
       (send* _pose_stamp __pose_stamp)
     (progn
       (if __pose_stamp (setq _pose_stamp (car __pose_stamp)))
       _pose_stamp)))
  (:seed_angles
   (&rest __seed_angles)
   (if (keywordp (car __seed_angles))
       (send* _seed_angles __seed_angles)
     (progn
       (if __seed_angles (setq _seed_angles (car __seed_angles)))
       _seed_angles)))
  (:seed_mode
   (&optional __seed_mode)
   (if __seed_mode (setq _seed_mode __seed_mode)) _seed_mode)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/PoseStamped _pose_stamp
    (send _pose_stamp :serialization-length)
    ;; sensor_msgs/JointState _seed_angles
    (send _seed_angles :serialization-length)
    ;; uint8 _seed_mode
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/PoseStamped _pose_stamp
       (send _pose_stamp :serialize s)
     ;; sensor_msgs/JointState _seed_angles
       (send _seed_angles :serialize s)
     ;; uint8 _seed_mode
       (write-byte _seed_mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/PoseStamped _pose_stamp
     (send _pose_stamp :deserialize buf ptr-) (incf ptr- (send _pose_stamp :serialization-length))
   ;; sensor_msgs/JointState _seed_angles
     (send _seed_angles :deserialize buf ptr-) (incf ptr- (send _seed_angles :serialization-length))
   ;; uint8 _seed_mode
     (setq _seed_mode (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(intern "*RESULT_INVALID*" (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKRESPONSE"))
(shadow '*RESULT_INVALID* (find-package "KUKA_KINEMATICS::SOLVEPOSITIONIKRESPONSE"))
(defconstant kuka_kinematics::SolvePositionIKResponse::*RESULT_INVALID* 0)

(defun kuka_kinematics::SolvePositionIKResponse-to-symbol (const)
  (cond
        ((= const 0) 'kuka_kinematics::SolvePositionIKResponse::*RESULT_INVALID*)
        (t nil)))

(defclass kuka_kinematics::SolvePositionIKResponse
  :super ros::object
  :slots (_joints _isValid _result_type ))

(defmethod kuka_kinematics::SolvePositionIKResponse
  (:init
   (&key
    ((:joints __joints) (instance sensor_msgs::JointState :init))
    ((:isValid __isValid) nil)
    ((:result_type __result_type) 0)
    )
   (send-super :init)
   (setq _joints __joints)
   (setq _isValid __isValid)
   (setq _result_type (round __result_type))
   self)
  (:joints
   (&rest __joints)
   (if (keywordp (car __joints))
       (send* _joints __joints)
     (progn
       (if __joints (setq _joints (car __joints)))
       _joints)))
  (:isValid
   (&optional (__isValid :null))
   (if (not (eq __isValid :null)) (setq _isValid __isValid)) _isValid)
  (:result_type
   (&optional __result_type)
   (if __result_type (setq _result_type __result_type)) _result_type)
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/JointState _joints
    (send _joints :serialization-length)
    ;; bool _isValid
    1
    ;; uint8 _result_type
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/JointState _joints
       (send _joints :serialize s)
     ;; bool _isValid
       (if _isValid (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _result_type
       (write-byte _result_type s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/JointState _joints
     (send _joints :deserialize buf ptr-) (incf ptr- (send _joints :serialization-length))
   ;; bool _isValid
     (setq _isValid (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _result_type
     (setq _result_type (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass kuka_kinematics::SolvePositionIK
  :super ros::object
  :slots ())

(setf (get kuka_kinematics::SolvePositionIK :md5sum-) "0b2822586a12e4c26260aa39340340f7")
(setf (get kuka_kinematics::SolvePositionIK :datatype-) "kuka_kinematics/SolvePositionIK")
(setf (get kuka_kinematics::SolvePositionIK :request) kuka_kinematics::SolvePositionIKRequest)
(setf (get kuka_kinematics::SolvePositionIK :response) kuka_kinematics::SolvePositionIKResponse)

(defmethod kuka_kinematics::SolvePositionIKRequest
  (:response () (instance kuka_kinematics::SolvePositionIKResponse :init)))

(setf (get kuka_kinematics::SolvePositionIKRequest :md5sum-) "0b2822586a12e4c26260aa39340340f7")
(setf (get kuka_kinematics::SolvePositionIKRequest :datatype-) "kuka_kinematics/SolvePositionIKRequest")
(setf (get kuka_kinematics::SolvePositionIKRequest :definition-)
      "# Endpoint Pose(s) to request Inverse-Kinematics joint solutions for.
geometry_msgs/PoseStamped pose_stamp

# (optional) Joint Angle Seed(s) for IK solver.
# * specify a JointState seed for each pose_stamp, using name[] and position[]
# * empty arrays or a non-default seed_mode will cause user seed to not be used
sensor_msgs/JointState seed_angles

# Seed Type Mode
# * default (SEED_AUTO) mode: iterate through seed types until first valid
#                             solution is found
# * setting any other mode:   try only that seed type
uint8 SEED_AUTO    = 0
uint8 SEED_USER    = 1
uint8 SEED_CURRENT = 2
uint8 SEED_NS_MAP  = 3

uint8 seed_mode

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: sensor_msgs/JointState
# This is a message that holds data to describe the state of a set of torque controlled joints. 
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.


Header header

string[] name
float64[] position
float64[] velocity
float64[] effort
---
# joints[i]      == joint angle solution for each pose_state[i]
sensor_msgs/JointState joints

# NOTE: isValid will be deprecated by result_type in future versions
bool isValid

# result_type[i] == seed type used to find valid solution, joints[i];
# otherwise,     == RESULT_INVALID (no valid solution found).
uint8 RESULT_INVALID = 0
uint8 result_type


================================================================================
MSG: sensor_msgs/JointState
# This is a message that holds data to describe the state of a set of torque controlled joints. 
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.


Header header

string[] name
float64[] position
float64[] velocity
float64[] effort

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
")

(setf (get kuka_kinematics::SolvePositionIKResponse :md5sum-) "0b2822586a12e4c26260aa39340340f7")
(setf (get kuka_kinematics::SolvePositionIKResponse :datatype-) "kuka_kinematics/SolvePositionIKResponse")
(setf (get kuka_kinematics::SolvePositionIKResponse :definition-)
      "# Endpoint Pose(s) to request Inverse-Kinematics joint solutions for.
geometry_msgs/PoseStamped pose_stamp

# (optional) Joint Angle Seed(s) for IK solver.
# * specify a JointState seed for each pose_stamp, using name[] and position[]
# * empty arrays or a non-default seed_mode will cause user seed to not be used
sensor_msgs/JointState seed_angles

# Seed Type Mode
# * default (SEED_AUTO) mode: iterate through seed types until first valid
#                             solution is found
# * setting any other mode:   try only that seed type
uint8 SEED_AUTO    = 0
uint8 SEED_USER    = 1
uint8 SEED_CURRENT = 2
uint8 SEED_NS_MAP  = 3

uint8 seed_mode

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: sensor_msgs/JointState
# This is a message that holds data to describe the state of a set of torque controlled joints. 
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.


Header header

string[] name
float64[] position
float64[] velocity
float64[] effort
---
# joints[i]      == joint angle solution for each pose_state[i]
sensor_msgs/JointState joints

# NOTE: isValid will be deprecated by result_type in future versions
bool isValid

# result_type[i] == seed type used to find valid solution, joints[i];
# otherwise,     == RESULT_INVALID (no valid solution found).
uint8 RESULT_INVALID = 0
uint8 result_type


================================================================================
MSG: sensor_msgs/JointState
# This is a message that holds data to describe the state of a set of torque controlled joints. 
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.


Header header

string[] name
float64[] position
float64[] velocity
float64[] effort

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
")



(provide :kuka_kinematics/SolvePositionIK "0b2822586a12e4c26260aa39340340f7")


