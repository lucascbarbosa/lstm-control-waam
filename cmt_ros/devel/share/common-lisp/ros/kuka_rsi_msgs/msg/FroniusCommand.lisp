; Auto-generated. Do not edit!


(cl:in-package kuka_rsi_msgs-msg)


;//! \htmlinclude FroniusCommand.msg.html

(cl:defclass <FroniusCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (power_set_value
    :reader power_set_value
    :initarg :power_set_value
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
   (burn_back
    :reader burn_back
    :initarg :burn_back
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
   (master_selection_twin
    :reader master_selection_twin
    :initarg :master_selection_twin
    :type cl:boolean
    :initform cl:nil)
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
   (job_number
    :reader job_number
    :initarg :job_number
    :type cl:fixnum
    :initform 0)
   (program_number
    :reader program_number
    :initarg :program_number
    :type cl:fixnum
    :initform 0)
   (welding_simulation
    :reader welding_simulation
    :initarg :welding_simulation
    :type cl:boolean
    :initform cl:nil)
   (synchro_pulse_disable
    :reader synchro_pulse_disable
    :initarg :synchro_pulse_disable
    :type cl:boolean
    :initform cl:nil)
   (SFI_disable
    :reader SFI_disable
    :initarg :SFI_disable
    :type cl:boolean
    :initform cl:nil)
   (dynamic_correction_disable
    :reader dynamic_correction_disable
    :initarg :dynamic_correction_disable
    :type cl:boolean
    :initform cl:nil)
   (burn_back_disable
    :reader burn_back_disable
    :initarg :burn_back_disable
    :type cl:boolean
    :initform cl:nil)
   (full_power_range
    :reader full_power_range
    :initarg :full_power_range
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass FroniusCommand (<FroniusCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FroniusCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FroniusCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_rsi_msgs-msg:<FroniusCommand> is deprecated: use kuka_rsi_msgs-msg:FroniusCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:header-val is deprecated.  Use kuka_rsi_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'power_set_value-val :lambda-list '(m))
(cl:defmethod power_set_value-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:power_set_value-val is deprecated.  Use kuka_rsi_msgs-msg:power_set_value instead.")
  (power_set_value m))

(cl:ensure-generic-function 'arc_length_correction-val :lambda-list '(m))
(cl:defmethod arc_length_correction-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:arc_length_correction-val is deprecated.  Use kuka_rsi_msgs-msg:arc_length_correction instead.")
  (arc_length_correction m))

(cl:ensure-generic-function 'dynamic_correction-val :lambda-list '(m))
(cl:defmethod dynamic_correction-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:dynamic_correction-val is deprecated.  Use kuka_rsi_msgs-msg:dynamic_correction instead.")
  (dynamic_correction m))

(cl:ensure-generic-function 'burn_back-val :lambda-list '(m))
(cl:defmethod burn_back-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:burn_back-val is deprecated.  Use kuka_rsi_msgs-msg:burn_back instead.")
  (burn_back m))

(cl:ensure-generic-function 'welding_start-val :lambda-list '(m))
(cl:defmethod welding_start-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:welding_start-val is deprecated.  Use kuka_rsi_msgs-msg:welding_start instead.")
  (welding_start m))

(cl:ensure-generic-function 'working_modes-val :lambda-list '(m))
(cl:defmethod working_modes-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:working_modes-val is deprecated.  Use kuka_rsi_msgs-msg:working_modes instead.")
  (working_modes m))

(cl:ensure-generic-function 'master_selection_twin-val :lambda-list '(m))
(cl:defmethod master_selection_twin-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:master_selection_twin-val is deprecated.  Use kuka_rsi_msgs-msg:master_selection_twin instead.")
  (master_selection_twin m))

(cl:ensure-generic-function 'gas_test-val :lambda-list '(m))
(cl:defmethod gas_test-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:gas_test-val is deprecated.  Use kuka_rsi_msgs-msg:gas_test instead.")
  (gas_test m))

(cl:ensure-generic-function 'wire_forward-val :lambda-list '(m))
(cl:defmethod wire_forward-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_forward-val is deprecated.  Use kuka_rsi_msgs-msg:wire_forward instead.")
  (wire_forward m))

(cl:ensure-generic-function 'job_number-val :lambda-list '(m))
(cl:defmethod job_number-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:job_number-val is deprecated.  Use kuka_rsi_msgs-msg:job_number instead.")
  (job_number m))

(cl:ensure-generic-function 'program_number-val :lambda-list '(m))
(cl:defmethod program_number-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:program_number-val is deprecated.  Use kuka_rsi_msgs-msg:program_number instead.")
  (program_number m))

(cl:ensure-generic-function 'welding_simulation-val :lambda-list '(m))
(cl:defmethod welding_simulation-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:welding_simulation-val is deprecated.  Use kuka_rsi_msgs-msg:welding_simulation instead.")
  (welding_simulation m))

(cl:ensure-generic-function 'synchro_pulse_disable-val :lambda-list '(m))
(cl:defmethod synchro_pulse_disable-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:synchro_pulse_disable-val is deprecated.  Use kuka_rsi_msgs-msg:synchro_pulse_disable instead.")
  (synchro_pulse_disable m))

(cl:ensure-generic-function 'SFI_disable-val :lambda-list '(m))
(cl:defmethod SFI_disable-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:SFI_disable-val is deprecated.  Use kuka_rsi_msgs-msg:SFI_disable instead.")
  (SFI_disable m))

(cl:ensure-generic-function 'dynamic_correction_disable-val :lambda-list '(m))
(cl:defmethod dynamic_correction_disable-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:dynamic_correction_disable-val is deprecated.  Use kuka_rsi_msgs-msg:dynamic_correction_disable instead.")
  (dynamic_correction_disable m))

(cl:ensure-generic-function 'burn_back_disable-val :lambda-list '(m))
(cl:defmethod burn_back_disable-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:burn_back_disable-val is deprecated.  Use kuka_rsi_msgs-msg:burn_back_disable instead.")
  (burn_back_disable m))

(cl:ensure-generic-function 'full_power_range-val :lambda-list '(m))
(cl:defmethod full_power_range-val ((m <FroniusCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:full_power_range-val is deprecated.  Use kuka_rsi_msgs-msg:full_power_range instead.")
  (full_power_range m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FroniusCommand>) ostream)
  "Serializes a message object of type '<FroniusCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'power_set_value))))
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'burn_back))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'welding_start) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'working_modes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'master_selection_twin) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'gas_test) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wire_forward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'job_number)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'program_number)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'welding_simulation) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'synchro_pulse_disable) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'SFI_disable) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'dynamic_correction_disable) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'burn_back_disable) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'full_power_range) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FroniusCommand>) istream)
  "Deserializes a message object of type '<FroniusCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'power_set_value) (roslisp-utils:decode-single-float-bits bits)))
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
    (cl:setf (cl:slot-value msg 'burn_back) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'welding_start) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'working_modes)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'master_selection_twin) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'gas_test) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'wire_forward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'job_number)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'program_number)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'welding_simulation) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'synchro_pulse_disable) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'SFI_disable) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'dynamic_correction_disable) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'burn_back_disable) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'full_power_range) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FroniusCommand>)))
  "Returns string type for a message object of type '<FroniusCommand>"
  "kuka_rsi_msgs/FroniusCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FroniusCommand)))
  "Returns string type for a message object of type 'FroniusCommand"
  "kuka_rsi_msgs/FroniusCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FroniusCommand>)))
  "Returns md5sum for a message object of type '<FroniusCommand>"
  "3db99eb4c29a0d366f39cbc70352a89a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FroniusCommand)))
  "Returns md5sum for a message object of type 'FroniusCommand"
  "3db99eb4c29a0d366f39cbc70352a89a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FroniusCommand>)))
  "Returns full string definition for message of type '<FroniusCommand>"
  (cl:format cl:nil "Header header~%# Field 5-6~%float32 power_set_value~%# Field 7-8~%float32 arc_length_correction~%# Field 9~%float32 dynamic_correction~%# Field 10~%float32 burn_back~%# Field 1~%bool welding_start~%# Field 2~%uint8 working_modes~%# bool working_modes_bit0~%# bool working_modes_bit1~%# bool working_modes_bit2~%bool master_selection_twin~%bool gas_test~%bool wire_forward~%# Field 3~%uint8 job_number~%# Field 4~%uint8 program_number~%bool welding_simulation~%# Field 11~%bool synchro_pulse_disable~%bool SFI_disable~%bool dynamic_correction_disable~%bool burn_back_disable~%bool full_power_range~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FroniusCommand)))
  "Returns full string definition for message of type 'FroniusCommand"
  (cl:format cl:nil "Header header~%# Field 5-6~%float32 power_set_value~%# Field 7-8~%float32 arc_length_correction~%# Field 9~%float32 dynamic_correction~%# Field 10~%float32 burn_back~%# Field 1~%bool welding_start~%# Field 2~%uint8 working_modes~%# bool working_modes_bit0~%# bool working_modes_bit1~%# bool working_modes_bit2~%bool master_selection_twin~%bool gas_test~%bool wire_forward~%# Field 3~%uint8 job_number~%# Field 4~%uint8 program_number~%bool welding_simulation~%# Field 11~%bool synchro_pulse_disable~%bool SFI_disable~%bool dynamic_correction_disable~%bool burn_back_disable~%bool full_power_range~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FroniusCommand>))
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
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FroniusCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'FroniusCommand
    (cl:cons ':header (header msg))
    (cl:cons ':power_set_value (power_set_value msg))
    (cl:cons ':arc_length_correction (arc_length_correction msg))
    (cl:cons ':dynamic_correction (dynamic_correction msg))
    (cl:cons ':burn_back (burn_back msg))
    (cl:cons ':welding_start (welding_start msg))
    (cl:cons ':working_modes (working_modes msg))
    (cl:cons ':master_selection_twin (master_selection_twin msg))
    (cl:cons ':gas_test (gas_test msg))
    (cl:cons ':wire_forward (wire_forward msg))
    (cl:cons ':job_number (job_number msg))
    (cl:cons ':program_number (program_number msg))
    (cl:cons ':welding_simulation (welding_simulation msg))
    (cl:cons ':synchro_pulse_disable (synchro_pulse_disable msg))
    (cl:cons ':SFI_disable (SFI_disable msg))
    (cl:cons ':dynamic_correction_disable (dynamic_correction_disable msg))
    (cl:cons ':burn_back_disable (burn_back_disable msg))
    (cl:cons ':full_power_range (full_power_range msg))
))
