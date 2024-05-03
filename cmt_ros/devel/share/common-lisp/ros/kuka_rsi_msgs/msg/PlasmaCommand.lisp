; Auto-generated. Do not edit!


(cl:in-package kuka_rsi_msgs-msg)


;//! \htmlinclude PlasmaCommand.msg.html

(cl:defclass <PlasmaCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (Dinse_wire_feed_speed
    :reader Dinse_wire_feed_speed
    :initarg :Dinse_wire_feed_speed
    :type cl:float
    :initform 0.0)
   (EWM_current
    :reader EWM_current
    :initarg :EWM_current
    :type cl:float
    :initform 0.0)
   (EWM_plasma_gas
    :reader EWM_plasma_gas
    :initarg :EWM_plasma_gas
    :type cl:float
    :initform 0.0)
   (EWM_shield_gas
    :reader EWM_shield_gas
    :initarg :EWM_shield_gas
    :type cl:float
    :initform 0.0)
   (Dinse_start_release
    :reader Dinse_start_release
    :initarg :Dinse_start_release
    :type cl:boolean
    :initform cl:nil)
   (Dinse_acknowledge_fault
    :reader Dinse_acknowledge_fault
    :initarg :Dinse_acknowledge_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_start_wire_feed
    :reader Dinse_start_wire_feed
    :initarg :Dinse_start_wire_feed
    :type cl:boolean
    :initform cl:nil)
   (Dinse_start_power_source
    :reader Dinse_start_power_source
    :initarg :Dinse_start_power_source
    :type cl:boolean
    :initform cl:nil)
   (Dinse_wirebreak
    :reader Dinse_wirebreak
    :initarg :Dinse_wirebreak
    :type cl:boolean
    :initform cl:nil)
   (Dinse_wire_forward
    :reader Dinse_wire_forward
    :initarg :Dinse_wire_forward
    :type cl:boolean
    :initform cl:nil)
   (Dinse_wire_backward
    :reader Dinse_wire_backward
    :initarg :Dinse_wire_backward
    :type cl:boolean
    :initform cl:nil)
   (Dinse_gas_on
    :reader Dinse_gas_on
    :initarg :Dinse_gas_on
    :type cl:boolean
    :initform cl:nil)
   (Dinse_retraction
    :reader Dinse_retraction
    :initarg :Dinse_retraction
    :type cl:boolean
    :initform cl:nil)
   (Dinse_positioning
    :reader Dinse_positioning
    :initarg :Dinse_positioning
    :type cl:boolean
    :initform cl:nil)
   (EWM_Start
    :reader EWM_Start
    :initarg :EWM_Start
    :type cl:boolean
    :initform cl:nil)
   (EWM_gas_test_1_shield
    :reader EWM_gas_test_1_shield
    :initarg :EWM_gas_test_1_shield
    :type cl:boolean
    :initform cl:nil)
   (EWM_gas_test_2_plasma
    :reader EWM_gas_test_2_plasma
    :initarg :EWM_gas_test_2_plasma
    :type cl:boolean
    :initform cl:nil)
   (EWM_feed_wire
    :reader EWM_feed_wire
    :initarg :EWM_feed_wire
    :type cl:boolean
    :initform cl:nil)
   (EWM_unfeed_wire
    :reader EWM_unfeed_wire
    :initarg :EWM_unfeed_wire
    :type cl:boolean
    :initform cl:nil)
   (EWM_position_search
    :reader EWM_position_search
    :initarg :EWM_position_search
    :type cl:boolean
    :initform cl:nil)
   (EWM_error_reset
    :reader EWM_error_reset
    :initarg :EWM_error_reset
    :type cl:boolean
    :initform cl:nil)
   (EWM_start_aux_process
    :reader EWM_start_aux_process
    :initarg :EWM_start_aux_process
    :type cl:boolean
    :initform cl:nil)
   (EWM_user_relay
    :reader EWM_user_relay
    :initarg :EWM_user_relay
    :type cl:boolean
    :initform cl:nil)
   (EWM_welding_simulation
    :reader EWM_welding_simulation
    :initarg :EWM_welding_simulation
    :type cl:boolean
    :initform cl:nil)
   (EWM_monitoring_function
    :reader EWM_monitoring_function
    :initarg :EWM_monitoring_function
    :type cl:boolean
    :initform cl:nil)
   (EWM_filler_wire_activated
    :reader EWM_filler_wire_activated
    :initarg :EWM_filler_wire_activated
    :type cl:boolean
    :initform cl:nil)
   (EWM_reserved_1
    :reader EWM_reserved_1
    :initarg :EWM_reserved_1
    :type cl:boolean
    :initform cl:nil)
   (EWM_weld_mode_select_bit_0
    :reader EWM_weld_mode_select_bit_0
    :initarg :EWM_weld_mode_select_bit_0
    :type cl:boolean
    :initform cl:nil)
   (EWM_weld_mode_select_bit_1
    :reader EWM_weld_mode_select_bit_1
    :initarg :EWM_weld_mode_select_bit_1
    :type cl:boolean
    :initform cl:nil)
   (EWM_wirefeeder_switch
    :reader EWM_wirefeeder_switch
    :initarg :EWM_wirefeeder_switch
    :type cl:boolean
    :initform cl:nil)
   (EWM_reserved_2
    :reader EWM_reserved_2
    :initarg :EWM_reserved_2
    :type cl:boolean
    :initform cl:nil)
   (EWM_cold_wire_feed_speed
    :reader EWM_cold_wire_feed_speed
    :initarg :EWM_cold_wire_feed_speed
    :type cl:float
    :initform 0.0)
   (EWM_job_number
    :reader EWM_job_number
    :initarg :EWM_job_number
    :type cl:fixnum
    :initform 0))
)

(cl:defclass PlasmaCommand (<PlasmaCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlasmaCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlasmaCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_rsi_msgs-msg:<PlasmaCommand> is deprecated: use kuka_rsi_msgs-msg:PlasmaCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:header-val is deprecated.  Use kuka_rsi_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'Dinse_wire_feed_speed-val :lambda-list '(m))
(cl:defmethod Dinse_wire_feed_speed-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_feed_speed-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_feed_speed instead.")
  (Dinse_wire_feed_speed m))

(cl:ensure-generic-function 'EWM_current-val :lambda-list '(m))
(cl:defmethod EWM_current-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_current-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_current instead.")
  (EWM_current m))

(cl:ensure-generic-function 'EWM_plasma_gas-val :lambda-list '(m))
(cl:defmethod EWM_plasma_gas-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_plasma_gas-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_plasma_gas instead.")
  (EWM_plasma_gas m))

(cl:ensure-generic-function 'EWM_shield_gas-val :lambda-list '(m))
(cl:defmethod EWM_shield_gas-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_shield_gas-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_shield_gas instead.")
  (EWM_shield_gas m))

(cl:ensure-generic-function 'Dinse_start_release-val :lambda-list '(m))
(cl:defmethod Dinse_start_release-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_start_release-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_start_release instead.")
  (Dinse_start_release m))

(cl:ensure-generic-function 'Dinse_acknowledge_fault-val :lambda-list '(m))
(cl:defmethod Dinse_acknowledge_fault-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_acknowledge_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_acknowledge_fault instead.")
  (Dinse_acknowledge_fault m))

(cl:ensure-generic-function 'Dinse_start_wire_feed-val :lambda-list '(m))
(cl:defmethod Dinse_start_wire_feed-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_start_wire_feed-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_start_wire_feed instead.")
  (Dinse_start_wire_feed m))

(cl:ensure-generic-function 'Dinse_start_power_source-val :lambda-list '(m))
(cl:defmethod Dinse_start_power_source-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_start_power_source-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_start_power_source instead.")
  (Dinse_start_power_source m))

(cl:ensure-generic-function 'Dinse_wirebreak-val :lambda-list '(m))
(cl:defmethod Dinse_wirebreak-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wirebreak-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wirebreak instead.")
  (Dinse_wirebreak m))

(cl:ensure-generic-function 'Dinse_wire_forward-val :lambda-list '(m))
(cl:defmethod Dinse_wire_forward-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_forward-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_forward instead.")
  (Dinse_wire_forward m))

(cl:ensure-generic-function 'Dinse_wire_backward-val :lambda-list '(m))
(cl:defmethod Dinse_wire_backward-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_backward-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_backward instead.")
  (Dinse_wire_backward m))

(cl:ensure-generic-function 'Dinse_gas_on-val :lambda-list '(m))
(cl:defmethod Dinse_gas_on-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_gas_on-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_gas_on instead.")
  (Dinse_gas_on m))

(cl:ensure-generic-function 'Dinse_retraction-val :lambda-list '(m))
(cl:defmethod Dinse_retraction-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_retraction-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_retraction instead.")
  (Dinse_retraction m))

(cl:ensure-generic-function 'Dinse_positioning-val :lambda-list '(m))
(cl:defmethod Dinse_positioning-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_positioning-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_positioning instead.")
  (Dinse_positioning m))

(cl:ensure-generic-function 'EWM_Start-val :lambda-list '(m))
(cl:defmethod EWM_Start-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_Start-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_Start instead.")
  (EWM_Start m))

(cl:ensure-generic-function 'EWM_gas_test_1_shield-val :lambda-list '(m))
(cl:defmethod EWM_gas_test_1_shield-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_gas_test_1_shield-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_gas_test_1_shield instead.")
  (EWM_gas_test_1_shield m))

(cl:ensure-generic-function 'EWM_gas_test_2_plasma-val :lambda-list '(m))
(cl:defmethod EWM_gas_test_2_plasma-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_gas_test_2_plasma-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_gas_test_2_plasma instead.")
  (EWM_gas_test_2_plasma m))

(cl:ensure-generic-function 'EWM_feed_wire-val :lambda-list '(m))
(cl:defmethod EWM_feed_wire-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_feed_wire-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_feed_wire instead.")
  (EWM_feed_wire m))

(cl:ensure-generic-function 'EWM_unfeed_wire-val :lambda-list '(m))
(cl:defmethod EWM_unfeed_wire-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_unfeed_wire-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_unfeed_wire instead.")
  (EWM_unfeed_wire m))

(cl:ensure-generic-function 'EWM_position_search-val :lambda-list '(m))
(cl:defmethod EWM_position_search-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_position_search-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_position_search instead.")
  (EWM_position_search m))

(cl:ensure-generic-function 'EWM_error_reset-val :lambda-list '(m))
(cl:defmethod EWM_error_reset-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_error_reset-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_error_reset instead.")
  (EWM_error_reset m))

(cl:ensure-generic-function 'EWM_start_aux_process-val :lambda-list '(m))
(cl:defmethod EWM_start_aux_process-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_start_aux_process-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_start_aux_process instead.")
  (EWM_start_aux_process m))

(cl:ensure-generic-function 'EWM_user_relay-val :lambda-list '(m))
(cl:defmethod EWM_user_relay-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_user_relay-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_user_relay instead.")
  (EWM_user_relay m))

(cl:ensure-generic-function 'EWM_welding_simulation-val :lambda-list '(m))
(cl:defmethod EWM_welding_simulation-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_welding_simulation-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_welding_simulation instead.")
  (EWM_welding_simulation m))

(cl:ensure-generic-function 'EWM_monitoring_function-val :lambda-list '(m))
(cl:defmethod EWM_monitoring_function-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_monitoring_function-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_monitoring_function instead.")
  (EWM_monitoring_function m))

(cl:ensure-generic-function 'EWM_filler_wire_activated-val :lambda-list '(m))
(cl:defmethod EWM_filler_wire_activated-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_filler_wire_activated-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_filler_wire_activated instead.")
  (EWM_filler_wire_activated m))

(cl:ensure-generic-function 'EWM_reserved_1-val :lambda-list '(m))
(cl:defmethod EWM_reserved_1-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_reserved_1-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_reserved_1 instead.")
  (EWM_reserved_1 m))

(cl:ensure-generic-function 'EWM_weld_mode_select_bit_0-val :lambda-list '(m))
(cl:defmethod EWM_weld_mode_select_bit_0-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_weld_mode_select_bit_0-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_weld_mode_select_bit_0 instead.")
  (EWM_weld_mode_select_bit_0 m))

(cl:ensure-generic-function 'EWM_weld_mode_select_bit_1-val :lambda-list '(m))
(cl:defmethod EWM_weld_mode_select_bit_1-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_weld_mode_select_bit_1-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_weld_mode_select_bit_1 instead.")
  (EWM_weld_mode_select_bit_1 m))

(cl:ensure-generic-function 'EWM_wirefeeder_switch-val :lambda-list '(m))
(cl:defmethod EWM_wirefeeder_switch-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_wirefeeder_switch-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_wirefeeder_switch instead.")
  (EWM_wirefeeder_switch m))

(cl:ensure-generic-function 'EWM_reserved_2-val :lambda-list '(m))
(cl:defmethod EWM_reserved_2-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_reserved_2-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_reserved_2 instead.")
  (EWM_reserved_2 m))

(cl:ensure-generic-function 'EWM_cold_wire_feed_speed-val :lambda-list '(m))
(cl:defmethod EWM_cold_wire_feed_speed-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_cold_wire_feed_speed-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_cold_wire_feed_speed instead.")
  (EWM_cold_wire_feed_speed m))

(cl:ensure-generic-function 'EWM_job_number-val :lambda-list '(m))
(cl:defmethod EWM_job_number-val ((m <PlasmaCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_job_number-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_job_number instead.")
  (EWM_job_number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlasmaCommand>) ostream)
  "Serializes a message object of type '<PlasmaCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'Dinse_wire_feed_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'EWM_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'EWM_plasma_gas))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'EWM_shield_gas))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_start_release) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_acknowledge_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_start_wire_feed) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_start_power_source) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_wirebreak) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_wire_forward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_wire_backward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_gas_on) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_retraction) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_positioning) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_Start) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_gas_test_1_shield) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_gas_test_2_plasma) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_feed_wire) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_unfeed_wire) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_position_search) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_error_reset) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_start_aux_process) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_user_relay) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_welding_simulation) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_monitoring_function) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_filler_wire_activated) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_reserved_1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_weld_mode_select_bit_0) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_weld_mode_select_bit_1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_wirefeeder_switch) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_reserved_2) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'EWM_cold_wire_feed_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EWM_job_number)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlasmaCommand>) istream)
  "Deserializes a message object of type '<PlasmaCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Dinse_wire_feed_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'EWM_current) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'EWM_plasma_gas) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'EWM_shield_gas) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'Dinse_start_release) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_acknowledge_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_start_wire_feed) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_start_power_source) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_wirebreak) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_wire_forward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_wire_backward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_gas_on) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_retraction) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_positioning) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_Start) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_gas_test_1_shield) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_gas_test_2_plasma) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_feed_wire) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_unfeed_wire) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_position_search) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_error_reset) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_start_aux_process) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_user_relay) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_welding_simulation) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_monitoring_function) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_filler_wire_activated) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_reserved_1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_weld_mode_select_bit_0) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_weld_mode_select_bit_1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_wirefeeder_switch) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_reserved_2) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'EWM_cold_wire_feed_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EWM_job_number)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlasmaCommand>)))
  "Returns string type for a message object of type '<PlasmaCommand>"
  "kuka_rsi_msgs/PlasmaCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlasmaCommand)))
  "Returns string type for a message object of type 'PlasmaCommand"
  "kuka_rsi_msgs/PlasmaCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlasmaCommand>)))
  "Returns md5sum for a message object of type '<PlasmaCommand>"
  "e908814e1fa1f45ddd9838e2ac41ab4e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlasmaCommand)))
  "Returns md5sum for a message object of type 'PlasmaCommand"
  "e908814e1fa1f45ddd9838e2ac41ab4e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlasmaCommand>)))
  "Returns full string definition for message of type '<PlasmaCommand>"
  (cl:format cl:nil "Header header~%# Field 3-4~%float32 Dinse_wire_feed_speed~%# Field 8-9~%float32 EWM_current~%# Field 12-13~%float32 EWM_plasma_gas~%# Field 14-15~%float32 EWM_shield_gas~%# Field 1~%bool Dinse_start_release~%bool Dinse_acknowledge_fault~%bool Dinse_start_wire_feed~%bool Dinse_start_power_source~%bool Dinse_wirebreak~%bool Dinse_wire_forward~%bool Dinse_wire_backward~%bool Dinse_gas_on~%# Field 2~%bool Dinse_retraction~%bool Dinse_positioning~%# Field 5~%bool EWM_Start~%# Field 6~%bool EWM_gas_test_1_shield~%bool EWM_gas_test_2_plasma~%bool EWM_feed_wire~%bool EWM_unfeed_wire~%bool EWM_position_search~%bool EWM_error_reset~%bool EWM_start_aux_process~%bool EWM_user_relay~%# Field 7~%bool EWM_welding_simulation~%bool EWM_monitoring_function~%bool EWM_filler_wire_activated~%bool EWM_reserved_1~%bool EWM_weld_mode_select_bit_0~%bool EWM_weld_mode_select_bit_1~%bool EWM_wirefeeder_switch~%bool EWM_reserved_2~%# Field 10-11~%float32 EWM_cold_wire_feed_speed~%# Field 16~%uint8 EWM_job_number~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlasmaCommand)))
  "Returns full string definition for message of type 'PlasmaCommand"
  (cl:format cl:nil "Header header~%# Field 3-4~%float32 Dinse_wire_feed_speed~%# Field 8-9~%float32 EWM_current~%# Field 12-13~%float32 EWM_plasma_gas~%# Field 14-15~%float32 EWM_shield_gas~%# Field 1~%bool Dinse_start_release~%bool Dinse_acknowledge_fault~%bool Dinse_start_wire_feed~%bool Dinse_start_power_source~%bool Dinse_wirebreak~%bool Dinse_wire_forward~%bool Dinse_wire_backward~%bool Dinse_gas_on~%# Field 2~%bool Dinse_retraction~%bool Dinse_positioning~%# Field 5~%bool EWM_Start~%# Field 6~%bool EWM_gas_test_1_shield~%bool EWM_gas_test_2_plasma~%bool EWM_feed_wire~%bool EWM_unfeed_wire~%bool EWM_position_search~%bool EWM_error_reset~%bool EWM_start_aux_process~%bool EWM_user_relay~%# Field 7~%bool EWM_welding_simulation~%bool EWM_monitoring_function~%bool EWM_filler_wire_activated~%bool EWM_reserved_1~%bool EWM_weld_mode_select_bit_0~%bool EWM_weld_mode_select_bit_1~%bool EWM_wirefeeder_switch~%bool EWM_reserved_2~%# Field 10-11~%float32 EWM_cold_wire_feed_speed~%# Field 16~%uint8 EWM_job_number~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlasmaCommand>))
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
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlasmaCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'PlasmaCommand
    (cl:cons ':header (header msg))
    (cl:cons ':Dinse_wire_feed_speed (Dinse_wire_feed_speed msg))
    (cl:cons ':EWM_current (EWM_current msg))
    (cl:cons ':EWM_plasma_gas (EWM_plasma_gas msg))
    (cl:cons ':EWM_shield_gas (EWM_shield_gas msg))
    (cl:cons ':Dinse_start_release (Dinse_start_release msg))
    (cl:cons ':Dinse_acknowledge_fault (Dinse_acknowledge_fault msg))
    (cl:cons ':Dinse_start_wire_feed (Dinse_start_wire_feed msg))
    (cl:cons ':Dinse_start_power_source (Dinse_start_power_source msg))
    (cl:cons ':Dinse_wirebreak (Dinse_wirebreak msg))
    (cl:cons ':Dinse_wire_forward (Dinse_wire_forward msg))
    (cl:cons ':Dinse_wire_backward (Dinse_wire_backward msg))
    (cl:cons ':Dinse_gas_on (Dinse_gas_on msg))
    (cl:cons ':Dinse_retraction (Dinse_retraction msg))
    (cl:cons ':Dinse_positioning (Dinse_positioning msg))
    (cl:cons ':EWM_Start (EWM_Start msg))
    (cl:cons ':EWM_gas_test_1_shield (EWM_gas_test_1_shield msg))
    (cl:cons ':EWM_gas_test_2_plasma (EWM_gas_test_2_plasma msg))
    (cl:cons ':EWM_feed_wire (EWM_feed_wire msg))
    (cl:cons ':EWM_unfeed_wire (EWM_unfeed_wire msg))
    (cl:cons ':EWM_position_search (EWM_position_search msg))
    (cl:cons ':EWM_error_reset (EWM_error_reset msg))
    (cl:cons ':EWM_start_aux_process (EWM_start_aux_process msg))
    (cl:cons ':EWM_user_relay (EWM_user_relay msg))
    (cl:cons ':EWM_welding_simulation (EWM_welding_simulation msg))
    (cl:cons ':EWM_monitoring_function (EWM_monitoring_function msg))
    (cl:cons ':EWM_filler_wire_activated (EWM_filler_wire_activated msg))
    (cl:cons ':EWM_reserved_1 (EWM_reserved_1 msg))
    (cl:cons ':EWM_weld_mode_select_bit_0 (EWM_weld_mode_select_bit_0 msg))
    (cl:cons ':EWM_weld_mode_select_bit_1 (EWM_weld_mode_select_bit_1 msg))
    (cl:cons ':EWM_wirefeeder_switch (EWM_wirefeeder_switch msg))
    (cl:cons ':EWM_reserved_2 (EWM_reserved_2 msg))
    (cl:cons ':EWM_cold_wire_feed_speed (EWM_cold_wire_feed_speed msg))
    (cl:cons ':EWM_job_number (EWM_job_number msg))
))
