; Auto-generated. Do not edit!


(cl:in-package kuka_rsi_msgs-msg)


;//! \htmlinclude Fronius500iState.msg.html

(cl:defclass <Fronius500iState> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (welding_voltage
    :reader welding_voltage
    :initarg :welding_voltage
    :type cl:float
    :initform 0.0)
   (welding_current
    :reader welding_current
    :initarg :welding_current
    :type cl:float
    :initform 0.0)
   (wire_feed_speed
    :reader wire_feed_speed
    :initarg :wire_feed_speed
    :type cl:float
    :initform 0.0)
   (motor_current_M1
    :reader motor_current_M1
    :initarg :motor_current_M1
    :type cl:float
    :initform 0.0)
   (motor_current_M2
    :reader motor_current_M2
    :initarg :motor_current_M2
    :type cl:float
    :initform 0.0)
   (life_toggle_bit
    :reader life_toggle_bit
    :initarg :life_toggle_bit
    :type cl:boolean
    :initform cl:nil)
   (power_source_ready
    :reader power_source_ready
    :initarg :power_source_ready
    :type cl:boolean
    :initform cl:nil)
   (warning
    :reader warning
    :initarg :warning
    :type cl:boolean
    :initform cl:nil)
   (process_active
    :reader process_active
    :initarg :process_active
    :type cl:boolean
    :initform cl:nil)
   (current_flow
    :reader current_flow
    :initarg :current_flow
    :type cl:boolean
    :initform cl:nil)
   (arc_stable
    :reader arc_stable
    :initarg :arc_stable
    :type cl:boolean
    :initform cl:nil)
   (main_current_signal
    :reader main_current_signal
    :initarg :main_current_signal
    :type cl:boolean
    :initform cl:nil)
   (touch_signal
    :reader touch_signal
    :initarg :touch_signal
    :type cl:boolean
    :initform cl:nil)
   (collisionbox_active
    :reader collisionbox_active
    :initarg :collisionbox_active
    :type cl:boolean
    :initform cl:nil)
   (robot_motion_release
    :reader robot_motion_release
    :initarg :robot_motion_release
    :type cl:boolean
    :initform cl:nil)
   (wire_stick_workpiece
    :reader wire_stick_workpiece
    :initarg :wire_stick_workpiece
    :type cl:boolean
    :initform cl:nil)
   (short_circuit_contact_tip
    :reader short_circuit_contact_tip
    :initarg :short_circuit_contact_tip
    :type cl:boolean
    :initform cl:nil)
   (parameter_selection_internally
    :reader parameter_selection_internally
    :initarg :parameter_selection_internally
    :type cl:boolean
    :initform cl:nil)
   (characteristic_number_valid
    :reader characteristic_number_valid
    :initarg :characteristic_number_valid
    :type cl:boolean
    :initform cl:nil)
   (torch_body_gripped
    :reader torch_body_gripped
    :initarg :torch_body_gripped
    :type cl:boolean
    :initform cl:nil)
   (command_value_out_of_range
    :reader command_value_out_of_range
    :initarg :command_value_out_of_range
    :type cl:boolean
    :initform cl:nil)
   (correction_out_of_range
    :reader correction_out_of_range
    :initarg :correction_out_of_range
    :type cl:boolean
    :initform cl:nil)
   (limitsignal
    :reader limitsignal
    :initarg :limitsignal
    :type cl:boolean
    :initform cl:nil)
   (main_supply_status
    :reader main_supply_status
    :initarg :main_supply_status
    :type cl:boolean
    :initform cl:nil)
   (process_id
    :reader process_id
    :initarg :process_id
    :type cl:fixnum
    :initform 0)
   (process_str
    :reader process_str
    :initarg :process_str
    :type cl:string
    :initform "")
   (touch_signal_gas_nozzle
    :reader touch_signal_gas_nozzle
    :initarg :touch_signal_gas_nozzle
    :type cl:boolean
    :initform cl:nil)
   (twin_synchro_active
    :reader twin_synchro_active
    :initarg :twin_synchro_active
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Fronius500iState (<Fronius500iState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Fronius500iState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Fronius500iState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_rsi_msgs-msg:<Fronius500iState> is deprecated: use kuka_rsi_msgs-msg:Fronius500iState instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:header-val is deprecated.  Use kuka_rsi_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'welding_voltage-val :lambda-list '(m))
(cl:defmethod welding_voltage-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:welding_voltage-val is deprecated.  Use kuka_rsi_msgs-msg:welding_voltage instead.")
  (welding_voltage m))

(cl:ensure-generic-function 'welding_current-val :lambda-list '(m))
(cl:defmethod welding_current-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:welding_current-val is deprecated.  Use kuka_rsi_msgs-msg:welding_current instead.")
  (welding_current m))

(cl:ensure-generic-function 'wire_feed_speed-val :lambda-list '(m))
(cl:defmethod wire_feed_speed-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_feed_speed-val is deprecated.  Use kuka_rsi_msgs-msg:wire_feed_speed instead.")
  (wire_feed_speed m))

(cl:ensure-generic-function 'motor_current_M1-val :lambda-list '(m))
(cl:defmethod motor_current_M1-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:motor_current_M1-val is deprecated.  Use kuka_rsi_msgs-msg:motor_current_M1 instead.")
  (motor_current_M1 m))

(cl:ensure-generic-function 'motor_current_M2-val :lambda-list '(m))
(cl:defmethod motor_current_M2-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:motor_current_M2-val is deprecated.  Use kuka_rsi_msgs-msg:motor_current_M2 instead.")
  (motor_current_M2 m))

(cl:ensure-generic-function 'life_toggle_bit-val :lambda-list '(m))
(cl:defmethod life_toggle_bit-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:life_toggle_bit-val is deprecated.  Use kuka_rsi_msgs-msg:life_toggle_bit instead.")
  (life_toggle_bit m))

(cl:ensure-generic-function 'power_source_ready-val :lambda-list '(m))
(cl:defmethod power_source_ready-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:power_source_ready-val is deprecated.  Use kuka_rsi_msgs-msg:power_source_ready instead.")
  (power_source_ready m))

(cl:ensure-generic-function 'warning-val :lambda-list '(m))
(cl:defmethod warning-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:warning-val is deprecated.  Use kuka_rsi_msgs-msg:warning instead.")
  (warning m))

(cl:ensure-generic-function 'process_active-val :lambda-list '(m))
(cl:defmethod process_active-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:process_active-val is deprecated.  Use kuka_rsi_msgs-msg:process_active instead.")
  (process_active m))

(cl:ensure-generic-function 'current_flow-val :lambda-list '(m))
(cl:defmethod current_flow-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:current_flow-val is deprecated.  Use kuka_rsi_msgs-msg:current_flow instead.")
  (current_flow m))

(cl:ensure-generic-function 'arc_stable-val :lambda-list '(m))
(cl:defmethod arc_stable-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:arc_stable-val is deprecated.  Use kuka_rsi_msgs-msg:arc_stable instead.")
  (arc_stable m))

(cl:ensure-generic-function 'main_current_signal-val :lambda-list '(m))
(cl:defmethod main_current_signal-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:main_current_signal-val is deprecated.  Use kuka_rsi_msgs-msg:main_current_signal instead.")
  (main_current_signal m))

(cl:ensure-generic-function 'touch_signal-val :lambda-list '(m))
(cl:defmethod touch_signal-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:touch_signal-val is deprecated.  Use kuka_rsi_msgs-msg:touch_signal instead.")
  (touch_signal m))

(cl:ensure-generic-function 'collisionbox_active-val :lambda-list '(m))
(cl:defmethod collisionbox_active-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:collisionbox_active-val is deprecated.  Use kuka_rsi_msgs-msg:collisionbox_active instead.")
  (collisionbox_active m))

(cl:ensure-generic-function 'robot_motion_release-val :lambda-list '(m))
(cl:defmethod robot_motion_release-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:robot_motion_release-val is deprecated.  Use kuka_rsi_msgs-msg:robot_motion_release instead.")
  (robot_motion_release m))

(cl:ensure-generic-function 'wire_stick_workpiece-val :lambda-list '(m))
(cl:defmethod wire_stick_workpiece-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:wire_stick_workpiece-val is deprecated.  Use kuka_rsi_msgs-msg:wire_stick_workpiece instead.")
  (wire_stick_workpiece m))

(cl:ensure-generic-function 'short_circuit_contact_tip-val :lambda-list '(m))
(cl:defmethod short_circuit_contact_tip-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:short_circuit_contact_tip-val is deprecated.  Use kuka_rsi_msgs-msg:short_circuit_contact_tip instead.")
  (short_circuit_contact_tip m))

(cl:ensure-generic-function 'parameter_selection_internally-val :lambda-list '(m))
(cl:defmethod parameter_selection_internally-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:parameter_selection_internally-val is deprecated.  Use kuka_rsi_msgs-msg:parameter_selection_internally instead.")
  (parameter_selection_internally m))

(cl:ensure-generic-function 'characteristic_number_valid-val :lambda-list '(m))
(cl:defmethod characteristic_number_valid-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:characteristic_number_valid-val is deprecated.  Use kuka_rsi_msgs-msg:characteristic_number_valid instead.")
  (characteristic_number_valid m))

(cl:ensure-generic-function 'torch_body_gripped-val :lambda-list '(m))
(cl:defmethod torch_body_gripped-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:torch_body_gripped-val is deprecated.  Use kuka_rsi_msgs-msg:torch_body_gripped instead.")
  (torch_body_gripped m))

(cl:ensure-generic-function 'command_value_out_of_range-val :lambda-list '(m))
(cl:defmethod command_value_out_of_range-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:command_value_out_of_range-val is deprecated.  Use kuka_rsi_msgs-msg:command_value_out_of_range instead.")
  (command_value_out_of_range m))

(cl:ensure-generic-function 'correction_out_of_range-val :lambda-list '(m))
(cl:defmethod correction_out_of_range-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:correction_out_of_range-val is deprecated.  Use kuka_rsi_msgs-msg:correction_out_of_range instead.")
  (correction_out_of_range m))

(cl:ensure-generic-function 'limitsignal-val :lambda-list '(m))
(cl:defmethod limitsignal-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:limitsignal-val is deprecated.  Use kuka_rsi_msgs-msg:limitsignal instead.")
  (limitsignal m))

(cl:ensure-generic-function 'main_supply_status-val :lambda-list '(m))
(cl:defmethod main_supply_status-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:main_supply_status-val is deprecated.  Use kuka_rsi_msgs-msg:main_supply_status instead.")
  (main_supply_status m))

(cl:ensure-generic-function 'process_id-val :lambda-list '(m))
(cl:defmethod process_id-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:process_id-val is deprecated.  Use kuka_rsi_msgs-msg:process_id instead.")
  (process_id m))

(cl:ensure-generic-function 'process_str-val :lambda-list '(m))
(cl:defmethod process_str-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:process_str-val is deprecated.  Use kuka_rsi_msgs-msg:process_str instead.")
  (process_str m))

(cl:ensure-generic-function 'touch_signal_gas_nozzle-val :lambda-list '(m))
(cl:defmethod touch_signal_gas_nozzle-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:touch_signal_gas_nozzle-val is deprecated.  Use kuka_rsi_msgs-msg:touch_signal_gas_nozzle instead.")
  (touch_signal_gas_nozzle m))

(cl:ensure-generic-function 'twin_synchro_active-val :lambda-list '(m))
(cl:defmethod twin_synchro_active-val ((m <Fronius500iState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:twin_synchro_active-val is deprecated.  Use kuka_rsi_msgs-msg:twin_synchro_active instead.")
  (twin_synchro_active m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Fronius500iState>) ostream)
  "Serializes a message object of type '<Fronius500iState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'welding_voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'welding_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'wire_feed_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_current_M1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_current_M2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'life_toggle_bit) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'power_source_ready) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'warning) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'process_active) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'current_flow) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'arc_stable) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'main_current_signal) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'touch_signal) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'collisionbox_active) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'robot_motion_release) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wire_stick_workpiece) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'short_circuit_contact_tip) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'parameter_selection_internally) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'characteristic_number_valid) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'torch_body_gripped) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'command_value_out_of_range) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'correction_out_of_range) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'limitsignal) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'main_supply_status) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'process_id)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'process_str))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'process_str))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'touch_signal_gas_nozzle) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'twin_synchro_active) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Fronius500iState>) istream)
  "Deserializes a message object of type '<Fronius500iState>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'welding_voltage) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'welding_current) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wire_feed_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_current_M1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_current_M2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'life_toggle_bit) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'power_source_ready) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'warning) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'process_active) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'current_flow) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'arc_stable) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'main_current_signal) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'touch_signal) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'collisionbox_active) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'robot_motion_release) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'wire_stick_workpiece) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'short_circuit_contact_tip) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'parameter_selection_internally) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'characteristic_number_valid) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'torch_body_gripped) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'command_value_out_of_range) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'correction_out_of_range) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'limitsignal) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'main_supply_status) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'process_id)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'process_str) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'process_str) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'touch_signal_gas_nozzle) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'twin_synchro_active) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Fronius500iState>)))
  "Returns string type for a message object of type '<Fronius500iState>"
  "kuka_rsi_msgs/Fronius500iState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Fronius500iState)))
  "Returns string type for a message object of type 'Fronius500iState"
  "kuka_rsi_msgs/Fronius500iState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Fronius500iState>)))
  "Returns md5sum for a message object of type '<Fronius500iState>"
  "4355219bc4b3af559fd32d94b33e5f02")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Fronius500iState)))
  "Returns md5sum for a message object of type 'Fronius500iState"
  "4355219bc4b3af559fd32d94b33e5f02")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Fronius500iState>)))
  "Returns full string definition for message of type '<Fronius500iState>"
  (cl:format cl:nil "Header header~%# Input[4]~%float32 welding_voltage~%# Input[5]~%float32 welding_current~%# Input[6]~%float32 wire_feed_speed~%# Input[7]~%float32 motor_current_M1~%# Input[8]~%float32 motor_current_M2~%# Input[0]~%bool life_toggle_bit # 0~%bool power_source_ready # 1~%bool warning # 2~%bool process_active # 3~%bool current_flow # 4~%bool arc_stable # 5~%bool main_current_signal # 6~%bool touch_signal # 7~%# Input[1]~%bool collisionbox_active # 0~%bool robot_motion_release # 1~%bool wire_stick_workpiece # 2~%bool short_circuit_contact_tip # 4~%bool parameter_selection_internally # 5~%bool characteristic_number_valid # 6~%bool torch_body_gripped # 7~%# Input[2]~%bool command_value_out_of_range # 0~%bool correction_out_of_range # 1~%bool limitsignal # 3~%bool main_supply_status # 6~%# Input[3]~%uint8 process_id # 0-4~%string process_str # none~%bool touch_signal_gas_nozzle # 6~%bool twin_synchro_active # 7~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Fronius500iState)))
  "Returns full string definition for message of type 'Fronius500iState"
  (cl:format cl:nil "Header header~%# Input[4]~%float32 welding_voltage~%# Input[5]~%float32 welding_current~%# Input[6]~%float32 wire_feed_speed~%# Input[7]~%float32 motor_current_M1~%# Input[8]~%float32 motor_current_M2~%# Input[0]~%bool life_toggle_bit # 0~%bool power_source_ready # 1~%bool warning # 2~%bool process_active # 3~%bool current_flow # 4~%bool arc_stable # 5~%bool main_current_signal # 6~%bool touch_signal # 7~%# Input[1]~%bool collisionbox_active # 0~%bool robot_motion_release # 1~%bool wire_stick_workpiece # 2~%bool short_circuit_contact_tip # 4~%bool parameter_selection_internally # 5~%bool characteristic_number_valid # 6~%bool torch_body_gripped # 7~%# Input[2]~%bool command_value_out_of_range # 0~%bool correction_out_of_range # 1~%bool limitsignal # 3~%bool main_supply_status # 6~%# Input[3]~%uint8 process_id # 0-4~%string process_str # none~%bool touch_signal_gas_nozzle # 6~%bool twin_synchro_active # 7~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Fronius500iState>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
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
     1
     1
     1
     1
     1
     4 (cl:length (cl:slot-value msg 'process_str))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Fronius500iState>))
  "Converts a ROS message object to a list"
  (cl:list 'Fronius500iState
    (cl:cons ':header (header msg))
    (cl:cons ':welding_voltage (welding_voltage msg))
    (cl:cons ':welding_current (welding_current msg))
    (cl:cons ':wire_feed_speed (wire_feed_speed msg))
    (cl:cons ':motor_current_M1 (motor_current_M1 msg))
    (cl:cons ':motor_current_M2 (motor_current_M2 msg))
    (cl:cons ':life_toggle_bit (life_toggle_bit msg))
    (cl:cons ':power_source_ready (power_source_ready msg))
    (cl:cons ':warning (warning msg))
    (cl:cons ':process_active (process_active msg))
    (cl:cons ':current_flow (current_flow msg))
    (cl:cons ':arc_stable (arc_stable msg))
    (cl:cons ':main_current_signal (main_current_signal msg))
    (cl:cons ':touch_signal (touch_signal msg))
    (cl:cons ':collisionbox_active (collisionbox_active msg))
    (cl:cons ':robot_motion_release (robot_motion_release msg))
    (cl:cons ':wire_stick_workpiece (wire_stick_workpiece msg))
    (cl:cons ':short_circuit_contact_tip (short_circuit_contact_tip msg))
    (cl:cons ':parameter_selection_internally (parameter_selection_internally msg))
    (cl:cons ':characteristic_number_valid (characteristic_number_valid msg))
    (cl:cons ':torch_body_gripped (torch_body_gripped msg))
    (cl:cons ':command_value_out_of_range (command_value_out_of_range msg))
    (cl:cons ':correction_out_of_range (correction_out_of_range msg))
    (cl:cons ':limitsignal (limitsignal msg))
    (cl:cons ':main_supply_status (main_supply_status msg))
    (cl:cons ':process_id (process_id msg))
    (cl:cons ':process_str (process_str msg))
    (cl:cons ':touch_signal_gas_nozzle (touch_signal_gas_nozzle msg))
    (cl:cons ':twin_synchro_active (twin_synchro_active msg))
))
