; Auto-generated. Do not edit!


(cl:in-package kuka_rsi_msgs-msg)


;//! \htmlinclude FroniusState.msg.html

(cl:defclass <FroniusState> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (arc_voltage
    :reader arc_voltage
    :initarg :arc_voltage
    :type cl:float
    :initform 0.0)
   (arc_current
    :reader arc_current
    :initarg :arc_current
    :type cl:float
    :initform 0.0)
   (motor_current
    :reader motor_current
    :initarg :motor_current
    :type cl:float
    :initform 0.0)
   (wire_feed_speed
    :reader wire_feed_speed
    :initarg :wire_feed_speed
    :type cl:float
    :initform 0.0)
   (arc_stable
    :reader arc_stable
    :initarg :arc_stable
    :type cl:boolean
    :initform cl:nil)
   (limit_signal
    :reader limit_signal
    :initarg :limit_signal
    :type cl:boolean
    :initform cl:nil)
   (process_active
    :reader process_active
    :initarg :process_active
    :type cl:boolean
    :initform cl:nil)
   (main_current_signal
    :reader main_current_signal
    :initarg :main_current_signal
    :type cl:boolean
    :initform cl:nil)
   (torch_collision_protection
    :reader torch_collision_protection
    :initarg :torch_collision_protection
    :type cl:boolean
    :initform cl:nil)
   (power_source_ready
    :reader power_source_ready
    :initarg :power_source_ready
    :type cl:boolean
    :initform cl:nil)
   (communication_ready
    :reader communication_ready
    :initarg :communication_ready
    :type cl:boolean
    :initform cl:nil)
   (life_toggle_bit
    :reader life_toggle_bit
    :initarg :life_toggle_bit
    :type cl:boolean
    :initform cl:nil)
   (error_number
    :reader error_number
    :initarg :error_number
    :type cl:fixnum
    :initform 0)
   (wire_stick_control
    :reader wire_stick_control
    :initarg :wire_stick_control
    :type cl:boolean
    :initform cl:nil)
   (robot_access
    :reader robot_access
    :initarg :robot_access
    :type cl:boolean
    :initform cl:nil)
   (wire_available
    :reader wire_available
    :initarg :wire_available
    :type cl:boolean
    :initform cl:nil)
   (timeout_short_circuit
    :reader timeout_short_circuit
    :initarg :timeout_short_circuit
    :type cl:boolean
    :initform cl:nil)
   (data_documentation_ready
    :reader data_documentation_ready
    :initarg :data_documentation_ready
    :type cl:boolean
    :initform cl:nil)
   (power_outside_range
    :reader power_outside_range
    :initarg :power_outside_range
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass FroniusState (<FroniusState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FroniusState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FroniusState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_rsi_msgs-msg:<FroniusState> is deprecated: use kuka_rsi_msgs-msg:FroniusState instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:header-val is deprecated.  Use kuka_rsi_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'arc_voltage-val :lambda-list '(m))
(cl:defmethod arc_voltage-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:arc_voltage-val is deprecated.  Use kuka_rsi_msgs-msg:arc_voltage instead.")
  (arc_voltage m))

(cl:ensure-generic-function 'arc_current-val :lambda-list '(m))
(cl:defmethod arc_current-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:arc_current-val is deprecated.  Use kuka_rsi_msgs-msg:arc_current instead.")
  (arc_current m))

(cl:ensure-generic-function 'motor_current-val :lambda-list '(m))
(cl:defmethod motor_current-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:motor_current-val is deprecated.  Use kuka_rsi_msgs-msg:motor_current instead.")
  (motor_current m))

(cl:ensure-generic-function 'wire_feed_speed-val :lambda-list '(m))
(cl:defmethod wire_feed_speed-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_feed_speed-val is deprecated.  Use kuka_rsi_msgs-msg:wire_feed_speed instead.")
  (wire_feed_speed m))

(cl:ensure-generic-function 'arc_stable-val :lambda-list '(m))
(cl:defmethod arc_stable-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:arc_stable-val is deprecated.  Use kuka_rsi_msgs-msg:arc_stable instead.")
  (arc_stable m))

(cl:ensure-generic-function 'limit_signal-val :lambda-list '(m))
(cl:defmethod limit_signal-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:limit_signal-val is deprecated.  Use kuka_rsi_msgs-msg:limit_signal instead.")
  (limit_signal m))

(cl:ensure-generic-function 'process_active-val :lambda-list '(m))
(cl:defmethod process_active-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:process_active-val is deprecated.  Use kuka_rsi_msgs-msg:process_active instead.")
  (process_active m))

(cl:ensure-generic-function 'main_current_signal-val :lambda-list '(m))
(cl:defmethod main_current_signal-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:main_current_signal-val is deprecated.  Use kuka_rsi_msgs-msg:main_current_signal instead.")
  (main_current_signal m))

(cl:ensure-generic-function 'torch_collision_protection-val :lambda-list '(m))
(cl:defmethod torch_collision_protection-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:torch_collision_protection-val is deprecated.  Use kuka_rsi_msgs-msg:torch_collision_protection instead.")
  (torch_collision_protection m))

(cl:ensure-generic-function 'power_source_ready-val :lambda-list '(m))
(cl:defmethod power_source_ready-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:power_source_ready-val is deprecated.  Use kuka_rsi_msgs-msg:power_source_ready instead.")
  (power_source_ready m))

(cl:ensure-generic-function 'communication_ready-val :lambda-list '(m))
(cl:defmethod communication_ready-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:communication_ready-val is deprecated.  Use kuka_rsi_msgs-msg:communication_ready instead.")
  (communication_ready m))

(cl:ensure-generic-function 'life_toggle_bit-val :lambda-list '(m))
(cl:defmethod life_toggle_bit-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:life_toggle_bit-val is deprecated.  Use kuka_rsi_msgs-msg:life_toggle_bit instead.")
  (life_toggle_bit m))

(cl:ensure-generic-function 'error_number-val :lambda-list '(m))
(cl:defmethod error_number-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:error_number-val is deprecated.  Use kuka_rsi_msgs-msg:error_number instead.")
  (error_number m))

(cl:ensure-generic-function 'wire_stick_control-val :lambda-list '(m))
(cl:defmethod wire_stick_control-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_stick_control-val is deprecated.  Use kuka_rsi_msgs-msg:wire_stick_control instead.")
  (wire_stick_control m))

(cl:ensure-generic-function 'robot_access-val :lambda-list '(m))
(cl:defmethod robot_access-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:robot_access-val is deprecated.  Use kuka_rsi_msgs-msg:robot_access instead.")
  (robot_access m))

(cl:ensure-generic-function 'wire_available-val :lambda-list '(m))
(cl:defmethod wire_available-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_available-val is deprecated.  Use kuka_rsi_msgs-msg:wire_available instead.")
  (wire_available m))

(cl:ensure-generic-function 'timeout_short_circuit-val :lambda-list '(m))
(cl:defmethod timeout_short_circuit-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:timeout_short_circuit-val is deprecated.  Use kuka_rsi_msgs-msg:timeout_short_circuit instead.")
  (timeout_short_circuit m))

(cl:ensure-generic-function 'data_documentation_ready-val :lambda-list '(m))
(cl:defmethod data_documentation_ready-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:data_documentation_ready-val is deprecated.  Use kuka_rsi_msgs-msg:data_documentation_ready instead.")
  (data_documentation_ready m))

(cl:ensure-generic-function 'power_outside_range-val :lambda-list '(m))
(cl:defmethod power_outside_range-val ((m <FroniusState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:power_outside_range-val is deprecated.  Use kuka_rsi_msgs-msg:power_outside_range instead.")
  (power_outside_range m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FroniusState>) ostream)
  "Serializes a message object of type '<FroniusState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'arc_voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'arc_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'wire_feed_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'arc_stable) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'limit_signal) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'process_active) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'main_current_signal) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'torch_collision_protection) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'power_source_ready) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'communication_ready) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'life_toggle_bit) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'error_number)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wire_stick_control) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'robot_access) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wire_available) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'timeout_short_circuit) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'data_documentation_ready) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'power_outside_range) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FroniusState>) istream)
  "Deserializes a message object of type '<FroniusState>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arc_voltage) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arc_current) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_current) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wire_feed_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'arc_stable) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'limit_signal) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'process_active) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'main_current_signal) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'torch_collision_protection) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'power_source_ready) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'communication_ready) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'life_toggle_bit) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'error_number)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wire_stick_control) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'robot_access) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'wire_available) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'timeout_short_circuit) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'data_documentation_ready) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'power_outside_range) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FroniusState>)))
  "Returns string type for a message object of type '<FroniusState>"
  "kuka_rsi_msgs/FroniusState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FroniusState)))
  "Returns string type for a message object of type 'FroniusState"
  "kuka_rsi_msgs/FroniusState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FroniusState>)))
  "Returns md5sum for a message object of type '<FroniusState>"
  "30bd5f2b575dd738b94a41edaf98cf7f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FroniusState)))
  "Returns md5sum for a message object of type 'FroniusState"
  "30bd5f2b575dd738b94a41edaf98cf7f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FroniusState>)))
  "Returns full string definition for message of type '<FroniusState>"
  (cl:format cl:nil "Header header~%# Field 4-5~%float32 arc_voltage~%# Field 6-7~%float32 arc_current~%# Field 8~%float32 motor_current~%# Field 9-10~%float32 wire_feed_speed~%# Field 1~%bool arc_stable~%bool limit_signal~%bool process_active~%bool main_current_signal~%bool torch_collision_protection~%bool power_source_ready~%bool communication_ready~%bool life_toggle_bit~%# Field 2~%uint8 error_number~%# Field 3~%bool wire_stick_control~%bool robot_access~%bool wire_available~%bool timeout_short_circuit~%bool data_documentation_ready~%bool power_outside_range~%#~%# Commented fields are not used in WAAM Interface (welding_display.cpp)~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FroniusState)))
  "Returns full string definition for message of type 'FroniusState"
  (cl:format cl:nil "Header header~%# Field 4-5~%float32 arc_voltage~%# Field 6-7~%float32 arc_current~%# Field 8~%float32 motor_current~%# Field 9-10~%float32 wire_feed_speed~%# Field 1~%bool arc_stable~%bool limit_signal~%bool process_active~%bool main_current_signal~%bool torch_collision_protection~%bool power_source_ready~%bool communication_ready~%bool life_toggle_bit~%# Field 2~%uint8 error_number~%# Field 3~%bool wire_stick_control~%bool robot_access~%bool wire_available~%bool timeout_short_circuit~%bool data_documentation_ready~%bool power_outside_range~%#~%# Commented fields are not used in WAAM Interface (welding_display.cpp)~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FroniusState>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FroniusState>))
  "Converts a ROS message object to a list"
  (cl:list 'FroniusState
    (cl:cons ':header (header msg))
    (cl:cons ':arc_voltage (arc_voltage msg))
    (cl:cons ':arc_current (arc_current msg))
    (cl:cons ':motor_current (motor_current msg))
    (cl:cons ':wire_feed_speed (wire_feed_speed msg))
    (cl:cons ':arc_stable (arc_stable msg))
    (cl:cons ':limit_signal (limit_signal msg))
    (cl:cons ':process_active (process_active msg))
    (cl:cons ':main_current_signal (main_current_signal msg))
    (cl:cons ':torch_collision_protection (torch_collision_protection msg))
    (cl:cons ':power_source_ready (power_source_ready msg))
    (cl:cons ':communication_ready (communication_ready msg))
    (cl:cons ':life_toggle_bit (life_toggle_bit msg))
    (cl:cons ':error_number (error_number msg))
    (cl:cons ':wire_stick_control (wire_stick_control msg))
    (cl:cons ':robot_access (robot_access msg))
    (cl:cons ':wire_available (wire_available msg))
    (cl:cons ':timeout_short_circuit (timeout_short_circuit msg))
    (cl:cons ':data_documentation_ready (data_documentation_ready msg))
    (cl:cons ':power_outside_range (power_outside_range msg))
))
