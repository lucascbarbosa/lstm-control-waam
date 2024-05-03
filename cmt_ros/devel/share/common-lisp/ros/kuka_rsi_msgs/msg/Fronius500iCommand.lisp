; Auto-generated. Do not edit!


(cl:in-package kuka_rsi_msgs-msg)


;//! \htmlinclude Fronius500iCommand.msg.html

(cl:defclass <Fronius500iCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (wire_feed_speed_command_value
    :reader wire_feed_speed_command_value
    :initarg :wire_feed_speed_command_value
    :type cl:float
    :initform 0.0)
   (arc_length_correction
    :reader arc_length_correction
    :initarg :arc_length_correction
    :type cl:float
    :initform 0.0)
   (dynamic_correction
    :reader dynamic_correction
    :initarg :dynamic_correction
    :type cl:float
    :initform 0.0)
   (wire_retract_correction
    :reader wire_retract_correction
    :initarg :wire_retract_correction
    :type cl:float
    :initform 0.0)
   (welding_start
    :reader welding_start
    :initarg :welding_start
    :type cl:boolean
    :initform cl:nil)
   (working_modes
    :reader working_modes
    :initarg :working_modes
    :type cl:fixnum
    :initform 0)
   (gas_test
    :reader gas_test
    :initarg :gas_test
    :type cl:boolean
    :initform cl:nil)
   (wire_forward
    :reader wire_forward
    :initarg :wire_forward
    :type cl:boolean
    :initform cl:nil)
   (wire_backward
    :reader wire_backward
    :initarg :wire_backward
    :type cl:boolean
    :initform cl:nil)
   (error_quit
    :reader error_quit
    :initarg :error_quit
    :type cl:boolean
    :initform cl:nil)
   (touch_sensing
    :reader touch_sensing
    :initarg :touch_sensing
    :type cl:boolean
    :initform cl:nil)
   (torch_blow_out
    :reader torch_blow_out
    :initarg :torch_blow_out
    :type cl:boolean
    :initform cl:nil)
   (process_line_selection
    :reader process_line_selection
    :initarg :process_line_selection
    :type cl:fixnum
    :initform 0)
   (welding_simulation
    :reader welding_simulation
    :initarg :welding_simulation
    :type cl:boolean
    :initform cl:nil)
   (synchro_pulse_on
    :reader synchro_pulse_on
    :initarg :synchro_pulse_on
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Fronius500iCommand (<Fronius500iCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Fronius500iCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Fronius500iCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_rsi_msgs-msg:<Fronius500iCommand> is deprecated: use kuka_rsi_msgs-msg:Fronius500iCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:header-val is deprecated.  Use kuka_rsi_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'wire_feed_speed_command_value-val :lambda-list '(m))
(cl:defmethod wire_feed_speed_command_value-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_feed_speed_command_value-val is deprecated.  Use kuka_rsi_msgs-msg:wire_feed_speed_command_value instead.")
  (wire_feed_speed_command_value m))

(cl:ensure-generic-function 'arc_length_correction-val :lambda-list '(m))
(cl:defmethod arc_length_correction-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:arc_length_correction-val is deprecated.  Use kuka_rsi_msgs-msg:arc_length_correction instead.")
  (arc_length_correction m))

(cl:ensure-generic-function 'dynamic_correction-val :lambda-list '(m))
(cl:defmethod dynamic_correction-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:dynamic_correction-val is deprecated.  Use kuka_rsi_msgs-msg:dynamic_correction instead.")
  (dynamic_correction m))

(cl:ensure-generic-function 'wire_retract_correction-val :lambda-list '(m))
(cl:defmethod wire_retract_correction-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_retract_correction-val is deprecated.  Use kuka_rsi_msgs-msg:wire_retract_correction instead.")
  (wire_retract_correction m))

(cl:ensure-generic-function 'welding_start-val :lambda-list '(m))
(cl:defmethod welding_start-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:welding_start-val is deprecated.  Use kuka_rsi_msgs-msg:welding_start instead.")
  (welding_start m))

(cl:ensure-generic-function 'working_modes-val :lambda-list '(m))
(cl:defmethod working_modes-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:working_modes-val is deprecated.  Use kuka_rsi_msgs-msg:working_modes instead.")
  (working_modes m))

(cl:ensure-generic-function 'gas_test-val :lambda-list '(m))
(cl:defmethod gas_test-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:gas_test-val is deprecated.  Use kuka_rsi_msgs-msg:gas_test instead.")
  (gas_test m))

(cl:ensure-generic-function 'wire_forward-val :lambda-list '(m))
(cl:defmethod wire_forward-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_forward-val is deprecated.  Use kuka_rsi_msgs-msg:wire_forward instead.")
  (wire_forward m))

(cl:ensure-generic-function 'wire_backward-val :lambda-list '(m))
(cl:defmethod wire_backward-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_backward-val is deprecated.  Use kuka_rsi_msgs-msg:wire_backward instead.")
  (wire_backward m))

(cl:ensure-generic-function 'error_quit-val :lambda-list '(m))
(cl:defmethod error_quit-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:error_quit-val is deprecated.  Use kuka_rsi_msgs-msg:error_quit instead.")
  (error_quit m))

(cl:ensure-generic-function 'touch_sensing-val :lambda-list '(m))
(cl:defmethod touch_sensing-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:touch_sensing-val is deprecated.  Use kuka_rsi_msgs-msg:touch_sensing instead.")
  (touch_sensing m))

(cl:ensure-generic-function 'torch_blow_out-val :lambda-list '(m))
(cl:defmethod torch_blow_out-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:torch_blow_out-val is deprecated.  Use kuka_rsi_msgs-msg:torch_blow_out instead.")
  (torch_blow_out m))

(cl:ensure-generic-function 'process_line_selection-val :lambda-list '(m))
(cl:defmethod process_line_selection-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:process_line_selection-val is deprecated.  Use kuka_rsi_msgs-msg:process_line_selection instead.")
  (process_line_selection m))

(cl:ensure-generic-function 'welding_simulation-val :lambda-list '(m))
(cl:defmethod welding_simulation-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:welding_simulation-val is deprecated.  Use kuka_rsi_msgs-msg:welding_simulation instead.")
  (welding_simulation m))

(cl:ensure-generic-function 'synchro_pulse_on-val :lambda-list '(m))
(cl:defmethod synchro_pulse_on-val ((m <Fronius500iCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:synchro_pulse_on-val is deprecated.  Use kuka_rsi_msgs-msg:synchro_pulse_on instead.")
  (synchro_pulse_on m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Fronius500iCommand>) ostream)
  "Serializes a message object of type '<Fronius500iCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'wire_feed_speed_command_value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'arc_length_correction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dynamic_correction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'wire_retract_correction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'welding_start) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'working_modes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'gas_test) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wire_forward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wire_backward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'error_quit) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'touch_sensing) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'torch_blow_out) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'process_line_selection)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'welding_simulation) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'synchro_pulse_on) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Fronius500iCommand>) istream)
  "Deserializes a message object of type '<Fronius500iCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wire_feed_speed_command_value) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arc_length_correction) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dynamic_correction) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wire_retract_correction) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'welding_start) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'working_modes)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'gas_test) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'wire_forward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'wire_backward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'error_quit) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'touch_sensing) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'torch_blow_out) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'process_line_selection)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'welding_simulation) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'synchro_pulse_on) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Fronius500iCommand>)))
  "Returns string type for a message object of type '<Fronius500iCommand>"
  "kuka_rsi_msgs/Fronius500iCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Fronius500iCommand)))
  "Returns string type for a message object of type 'Fronius500iCommand"
  "kuka_rsi_msgs/Fronius500iCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Fronius500iCommand>)))
  "Returns md5sum for a message object of type '<Fronius500iCommand>"
  "a80028ec811c3f4ac2757241bd4475c6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Fronius500iCommand)))
  "Returns md5sum for a message object of type 'Fronius500iCommand"
  "a80028ec811c3f4ac2757241bd4475c6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Fronius500iCommand>)))
  "Returns full string definition for message of type '<Fronius500iCommand>"
  (cl:format cl:nil "Header header~%# Field[3]~%float32 wire_feed_speed_command_value~%# Field[4]~%float32 arc_length_correction~%# Field[5]~%float32 dynamic_correction~%# Field[6]~%float32 wire_retract_correction~%# Field[0]~%bool welding_start~%# Field[1]~%uint8 working_modes # [0-4]~%bool gas_test # [6]~%bool wire_forward # [7]~%# Field[2]~%bool wire_backward~%bool error_quit~%bool touch_sensing~%bool torch_blow_out~%uint8 process_line_selection~%bool welding_simulation~%bool synchro_pulse_on~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Fronius500iCommand)))
  "Returns full string definition for message of type 'Fronius500iCommand"
  (cl:format cl:nil "Header header~%# Field[3]~%float32 wire_feed_speed_command_value~%# Field[4]~%float32 arc_length_correction~%# Field[5]~%float32 dynamic_correction~%# Field[6]~%float32 wire_retract_correction~%# Field[0]~%bool welding_start~%# Field[1]~%uint8 working_modes # [0-4]~%bool gas_test # [6]~%bool wire_forward # [7]~%# Field[2]~%bool wire_backward~%bool error_quit~%bool touch_sensing~%bool torch_blow_out~%uint8 process_line_selection~%bool welding_simulation~%bool synchro_pulse_on~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Fronius500iCommand>))
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
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Fronius500iCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'Fronius500iCommand
    (cl:cons ':header (header msg))
    (cl:cons ':wire_feed_speed_command_value (wire_feed_speed_command_value msg))
    (cl:cons ':arc_length_correction (arc_length_correction msg))
    (cl:cons ':dynamic_correction (dynamic_correction msg))
    (cl:cons ':wire_retract_correction (wire_retract_correction msg))
    (cl:cons ':welding_start (welding_start msg))
    (cl:cons ':working_modes (working_modes msg))
    (cl:cons ':gas_test (gas_test msg))
    (cl:cons ':wire_forward (wire_forward msg))
    (cl:cons ':wire_backward (wire_backward msg))
    (cl:cons ':error_quit (error_quit msg))
    (cl:cons ':touch_sensing (touch_sensing msg))
    (cl:cons ':torch_blow_out (torch_blow_out msg))
    (cl:cons ':process_line_selection (process_line_selection msg))
    (cl:cons ':welding_simulation (welding_simulation msg))
    (cl:cons ':synchro_pulse_on (synchro_pulse_on msg))
))
