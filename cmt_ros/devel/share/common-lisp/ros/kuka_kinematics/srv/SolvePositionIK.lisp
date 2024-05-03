; Auto-generated. Do not edit!


(cl:in-package kuka_kinematics-srv)


;//! \htmlinclude SolvePositionIK-request.msg.html

(cl:defclass <SolvePositionIK-request> (roslisp-msg-protocol:ros-message)
  ((pose_stamp
    :reader pose_stamp
    :initarg :pose_stamp
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (seed_angles
    :reader seed_angles
    :initarg :seed_angles
    :type sensor_msgs-msg:JointState
    :initform (cl:make-instance 'sensor_msgs-msg:JointState))
   (seed_mode
    :reader seed_mode
    :initarg :seed_mode
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SolvePositionIK-request (<SolvePositionIK-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SolvePositionIK-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SolvePositionIK-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_kinematics-srv:<SolvePositionIK-request> is deprecated: use kuka_kinematics-srv:SolvePositionIK-request instead.")))

(cl:ensure-generic-function 'pose_stamp-val :lambda-list '(m))
(cl:defmethod pose_stamp-val ((m <SolvePositionIK-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_kinematics-srv:pose_stamp-val is deprecated.  Use kuka_kinematics-srv:pose_stamp instead.")
  (pose_stamp m))

(cl:ensure-generic-function 'seed_angles-val :lambda-list '(m))
(cl:defmethod seed_angles-val ((m <SolvePositionIK-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_kinematics-srv:seed_angles-val is deprecated.  Use kuka_kinematics-srv:seed_angles instead.")
  (seed_angles m))

(cl:ensure-generic-function 'seed_mode-val :lambda-list '(m))
(cl:defmethod seed_mode-val ((m <SolvePositionIK-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_kinematics-srv:seed_mode-val is deprecated.  Use kuka_kinematics-srv:seed_mode instead.")
  (seed_mode m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<SolvePositionIK-request>)))
    "Constants for message type '<SolvePositionIK-request>"
  '((:SEED_AUTO . 0)
    (:SEED_USER . 1)
    (:SEED_CURRENT . 2)
    (:SEED_NS_MAP . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'SolvePositionIK-request)))
    "Constants for message type 'SolvePositionIK-request"
  '((:SEED_AUTO . 0)
    (:SEED_USER . 1)
    (:SEED_CURRENT . 2)
    (:SEED_NS_MAP . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SolvePositionIK-request>) ostream)
  "Serializes a message object of type '<SolvePositionIK-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose_stamp) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'seed_angles) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'seed_mode)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SolvePositionIK-request>) istream)
  "Deserializes a message object of type '<SolvePositionIK-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose_stamp) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'seed_angles) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'seed_mode)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SolvePositionIK-request>)))
  "Returns string type for a service object of type '<SolvePositionIK-request>"
  "kuka_kinematics/SolvePositionIKRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SolvePositionIK-request)))
  "Returns string type for a service object of type 'SolvePositionIK-request"
  "kuka_kinematics/SolvePositionIKRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SolvePositionIK-request>)))
  "Returns md5sum for a message object of type '<SolvePositionIK-request>"
  "0b2822586a12e4c26260aa39340340f7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SolvePositionIK-request)))
  "Returns md5sum for a message object of type 'SolvePositionIK-request"
  "0b2822586a12e4c26260aa39340340f7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SolvePositionIK-request>)))
  "Returns full string definition for message of type '<SolvePositionIK-request>"
  (cl:format cl:nil "# Endpoint Pose(s) to request Inverse-Kinematics joint solutions for.~%geometry_msgs/PoseStamped pose_stamp~%~%# (optional) Joint Angle Seed(s) for IK solver.~%# * specify a JointState seed for each pose_stamp, using name[] and position[]~%# * empty arrays or a non-default seed_mode will cause user seed to not be used~%sensor_msgs/JointState seed_angles~%~%# Seed Type Mode~%# * default (SEED_AUTO) mode: iterate through seed types until first valid~%#                             solution is found~%# * setting any other mode:   try only that seed type~%uint8 SEED_AUTO    = 0~%uint8 SEED_USER    = 1~%uint8 SEED_CURRENT = 2~%uint8 SEED_NS_MAP  = 3~%~%uint8 seed_mode~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SolvePositionIK-request)))
  "Returns full string definition for message of type 'SolvePositionIK-request"
  (cl:format cl:nil "# Endpoint Pose(s) to request Inverse-Kinematics joint solutions for.~%geometry_msgs/PoseStamped pose_stamp~%~%# (optional) Joint Angle Seed(s) for IK solver.~%# * specify a JointState seed for each pose_stamp, using name[] and position[]~%# * empty arrays or a non-default seed_mode will cause user seed to not be used~%sensor_msgs/JointState seed_angles~%~%# Seed Type Mode~%# * default (SEED_AUTO) mode: iterate through seed types until first valid~%#                             solution is found~%# * setting any other mode:   try only that seed type~%uint8 SEED_AUTO    = 0~%uint8 SEED_USER    = 1~%uint8 SEED_CURRENT = 2~%uint8 SEED_NS_MAP  = 3~%~%uint8 seed_mode~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SolvePositionIK-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose_stamp))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'seed_angles))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SolvePositionIK-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SolvePositionIK-request
    (cl:cons ':pose_stamp (pose_stamp msg))
    (cl:cons ':seed_angles (seed_angles msg))
    (cl:cons ':seed_mode (seed_mode msg))
))
;//! \htmlinclude SolvePositionIK-response.msg.html

(cl:defclass <SolvePositionIK-response> (roslisp-msg-protocol:ros-message)
  ((joints
    :reader joints
    :initarg :joints
    :type sensor_msgs-msg:JointState
    :initform (cl:make-instance 'sensor_msgs-msg:JointState))
   (isValid
    :reader isValid
    :initarg :isValid
    :type cl:boolean
    :initform cl:nil)
   (result_type
    :reader result_type
    :initarg :result_type
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SolvePositionIK-response (<SolvePositionIK-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SolvePositionIK-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SolvePositionIK-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_kinematics-srv:<SolvePositionIK-response> is deprecated: use kuka_kinematics-srv:SolvePositionIK-response instead.")))

(cl:ensure-generic-function 'joints-val :lambda-list '(m))
(cl:defmethod joints-val ((m <SolvePositionIK-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_kinematics-srv:joints-val is deprecated.  Use kuka_kinematics-srv:joints instead.")
  (joints m))

(cl:ensure-generic-function 'isValid-val :lambda-list '(m))
(cl:defmethod isValid-val ((m <SolvePositionIK-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_kinematics-srv:isValid-val is deprecated.  Use kuka_kinematics-srv:isValid instead.")
  (isValid m))

(cl:ensure-generic-function 'result_type-val :lambda-list '(m))
(cl:defmethod result_type-val ((m <SolvePositionIK-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_kinematics-srv:result_type-val is deprecated.  Use kuka_kinematics-srv:result_type instead.")
  (result_type m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<SolvePositionIK-response>)))
    "Constants for message type '<SolvePositionIK-response>"
  '((:RESULT_INVALID . 0))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'SolvePositionIK-response)))
    "Constants for message type 'SolvePositionIK-response"
  '((:RESULT_INVALID . 0))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SolvePositionIK-response>) ostream)
  "Serializes a message object of type '<SolvePositionIK-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'joints) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'isValid) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'result_type)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SolvePositionIK-response>) istream)
  "Deserializes a message object of type '<SolvePositionIK-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'joints) istream)
    (cl:setf (cl:slot-value msg 'isValid) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'result_type)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SolvePositionIK-response>)))
  "Returns string type for a service object of type '<SolvePositionIK-response>"
  "kuka_kinematics/SolvePositionIKResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SolvePositionIK-response)))
  "Returns string type for a service object of type 'SolvePositionIK-response"
  "kuka_kinematics/SolvePositionIKResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SolvePositionIK-response>)))
  "Returns md5sum for a message object of type '<SolvePositionIK-response>"
  "0b2822586a12e4c26260aa39340340f7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SolvePositionIK-response)))
  "Returns md5sum for a message object of type 'SolvePositionIK-response"
  "0b2822586a12e4c26260aa39340340f7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SolvePositionIK-response>)))
  "Returns full string definition for message of type '<SolvePositionIK-response>"
  (cl:format cl:nil "# joints[i]      == joint angle solution for each pose_state[i]~%sensor_msgs/JointState joints~%~%# NOTE: isValid will be deprecated by result_type in future versions~%bool isValid~%~%# result_type[i] == seed type used to find valid solution, joints[i];~%# otherwise,     == RESULT_INVALID (no valid solution found).~%uint8 RESULT_INVALID = 0~%uint8 result_type~%~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SolvePositionIK-response)))
  "Returns full string definition for message of type 'SolvePositionIK-response"
  (cl:format cl:nil "# joints[i]      == joint angle solution for each pose_state[i]~%sensor_msgs/JointState joints~%~%# NOTE: isValid will be deprecated by result_type in future versions~%bool isValid~%~%# result_type[i] == seed type used to find valid solution, joints[i];~%# otherwise,     == RESULT_INVALID (no valid solution found).~%uint8 RESULT_INVALID = 0~%uint8 result_type~%~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SolvePositionIK-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'joints))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SolvePositionIK-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SolvePositionIK-response
    (cl:cons ':joints (joints msg))
    (cl:cons ':isValid (isValid msg))
    (cl:cons ':result_type (result_type msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SolvePositionIK)))
  'SolvePositionIK-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SolvePositionIK)))
  'SolvePositionIK-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SolvePositionIK)))
  "Returns string type for a service object of type '<SolvePositionIK>"
  "kuka_kinematics/SolvePositionIK")