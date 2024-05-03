; Auto-generated. Do not edit!


(cl:in-package kuka_rsi_msgs-msg)


;//! \htmlinclude PlasmaState.msg.html

(cl:defclass <PlasmaState> (roslisp-msg-protocol:ros-message)
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
   (EWM_voltage
    :reader EWM_voltage
    :initarg :EWM_voltage
    :type cl:float
    :initform 0.0)
   (EWM_current
    :reader EWM_current
    :initarg :EWM_current
    :type cl:float
    :initform 0.0)
   (EWM_wire_feed_speed
    :reader EWM_wire_feed_speed
    :initarg :EWM_wire_feed_speed
    :type cl:float
    :initform 0.0)
   (Dinse_wire_feeder_ready
    :reader Dinse_wire_feeder_ready
    :initarg :Dinse_wire_feeder_ready
    :type cl:boolean
    :initform cl:nil)
   (Dinse_collective_fault
    :reader Dinse_collective_fault
    :initarg :Dinse_collective_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_wire_feed_fault
    :reader Dinse_wire_feed_fault
    :initarg :Dinse_wire_feed_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_power_failure
    :reader Dinse_power_failure
    :initarg :Dinse_power_failure
    :type cl:boolean
    :initform cl:nil)
   (Dinse_positioning_fault
    :reader Dinse_positioning_fault
    :initarg :Dinse_positioning_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_hot_wire_fault
    :reader Dinse_hot_wire_fault
    :initarg :Dinse_hot_wire_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_life_bit
    :reader Dinse_life_bit
    :initarg :Dinse_life_bit
    :type cl:boolean
    :initform cl:nil)
   (Dinse_current_on
    :reader Dinse_current_on
    :initarg :Dinse_current_on
    :type cl:boolean
    :initform cl:nil)
   (Dinse_service_interval
    :reader Dinse_service_interval
    :initarg :Dinse_service_interval
    :type cl:boolean
    :initform cl:nil)
   (Dinse_intern_fault
    :reader Dinse_intern_fault
    :initarg :Dinse_intern_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_emergency_stop
    :reader Dinse_emergency_stop
    :initarg :Dinse_emergency_stop
    :type cl:boolean
    :initform cl:nil)
   (Dinse_gas_fault
    :reader Dinse_gas_fault
    :initarg :Dinse_gas_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_water_fault
    :reader Dinse_water_fault
    :initarg :Dinse_water_fault
    :type cl:boolean
    :initform cl:nil)
   (Dinse_process_active
    :reader Dinse_process_active
    :initarg :Dinse_process_active
    :type cl:boolean
    :initform cl:nil)
   (Dinse_wire_end
    :reader Dinse_wire_end
    :initarg :Dinse_wire_end
    :type cl:boolean
    :initform cl:nil)
   (Dinse_wire_movement_on_stop
    :reader Dinse_wire_movement_on_stop
    :initarg :Dinse_wire_movement_on_stop
    :type cl:boolean
    :initform cl:nil)
   (EWM_current_flows
    :reader EWM_current_flows
    :initarg :EWM_current_flows
    :type cl:boolean
    :initform cl:nil)
   (EWM_ready_for_welding
    :reader EWM_ready_for_welding
    :initarg :EWM_ready_for_welding
    :type cl:boolean
    :initform cl:nil)
   (EWM_sticking
    :reader EWM_sticking
    :initarg :EWM_sticking
    :type cl:boolean
    :initform cl:nil)
   (EWM_error_1
    :reader EWM_error_1
    :initarg :EWM_error_1
    :type cl:boolean
    :initform cl:nil)
   (EWM_collision_signal
    :reader EWM_collision_signal
    :initarg :EWM_collision_signal
    :type cl:boolean
    :initform cl:nil)
   (EWM_program_sequence_on_main_current
    :reader EWM_program_sequence_on_main_current
    :initarg :EWM_program_sequence_on_main_current
    :type cl:boolean
    :initform cl:nil)
   (EWM_process_active
    :reader EWM_process_active
    :initarg :EWM_process_active
    :type cl:boolean
    :initform cl:nil)
   (EWM_current_flows_aux_process
    :reader EWM_current_flows_aux_process
    :initarg :EWM_current_flows_aux_process
    :type cl:boolean
    :initform cl:nil)
   (EWM_error_number
    :reader EWM_error_number
    :initarg :EWM_error_number
    :type cl:fixnum
    :initform 0)
   (EWM_network_phases_status
    :reader EWM_network_phases_status
    :initarg :EWM_network_phases_status
    :type cl:boolean
    :initform cl:nil)
   (EWM_user_defined_input_1
    :reader EWM_user_defined_input_1
    :initarg :EWM_user_defined_input_1
    :type cl:boolean
    :initform cl:nil)
   (EWM_no_external_stop_of_operation
    :reader EWM_no_external_stop_of_operation
    :initarg :EWM_no_external_stop_of_operation
    :type cl:boolean
    :initform cl:nil)
   (EWM_user_defined_input_2
    :reader EWM_user_defined_input_2
    :initarg :EWM_user_defined_input_2
    :type cl:boolean
    :initform cl:nil)
   (EWM_wire_available
    :reader EWM_wire_available
    :initarg :EWM_wire_available
    :type cl:boolean
    :initform cl:nil)
   (EWM_wirefeeder_ok
    :reader EWM_wirefeeder_ok
    :initarg :EWM_wirefeeder_ok
    :type cl:boolean
    :initform cl:nil)
   (EWM_gas_ok
    :reader EWM_gas_ok
    :initarg :EWM_gas_ok
    :type cl:boolean
    :initform cl:nil)
   (EWM_cooland_water_ok
    :reader EWM_cooland_water_ok
    :initarg :EWM_cooland_water_ok
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass PlasmaState (<PlasmaState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlasmaState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlasmaState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kuka_rsi_msgs-msg:<PlasmaState> is deprecated: use kuka_rsi_msgs-msg:PlasmaState instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:header-val is deprecated.  Use kuka_rsi_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'Dinse_wire_feed_speed-val :lambda-list '(m))
(cl:defmethod Dinse_wire_feed_speed-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_feed_speed-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_feed_speed instead.")
  (Dinse_wire_feed_speed m))

(cl:ensure-generic-function 'EWM_voltage-val :lambda-list '(m))
(cl:defmethod EWM_voltage-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_voltage-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_voltage instead.")
  (EWM_voltage m))

(cl:ensure-generic-function 'EWM_current-val :lambda-list '(m))
(cl:defmethod EWM_current-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_current-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_current instead.")
  (EWM_current m))

(cl:ensure-generic-function 'EWM_wire_feed_speed-val :lambda-list '(m))
(cl:defmethod EWM_wire_feed_speed-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_wire_feed_speed-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_wire_feed_speed instead.")
  (EWM_wire_feed_speed m))

(cl:ensure-generic-function 'Dinse_wire_feeder_ready-val :lambda-list '(m))
(cl:defmethod Dinse_wire_feeder_ready-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_feeder_ready-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_feeder_ready instead.")
  (Dinse_wire_feeder_ready m))

(cl:ensure-generic-function 'Dinse_collective_fault-val :lambda-list '(m))
(cl:defmethod Dinse_collective_fault-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_collective_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_collective_fault instead.")
  (Dinse_collective_fault m))

(cl:ensure-generic-function 'Dinse_wire_feed_fault-val :lambda-list '(m))
(cl:defmethod Dinse_wire_feed_fault-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_feed_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_feed_fault instead.")
  (Dinse_wire_feed_fault m))

(cl:ensure-generic-function 'Dinse_power_failure-val :lambda-list '(m))
(cl:defmethod Dinse_power_failure-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_power_failure-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_power_failure instead.")
  (Dinse_power_failure m))

(cl:ensure-generic-function 'Dinse_positioning_fault-val :lambda-list '(m))
(cl:defmethod Dinse_positioning_fault-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_positioning_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_positioning_fault instead.")
  (Dinse_positioning_fault m))

(cl:ensure-generic-function 'Dinse_hot_wire_fault-val :lambda-list '(m))
(cl:defmethod Dinse_hot_wire_fault-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_hot_wire_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_hot_wire_fault instead.")
  (Dinse_hot_wire_fault m))

(cl:ensure-generic-function 'Dinse_life_bit-val :lambda-list '(m))
(cl:defmethod Dinse_life_bit-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_life_bit-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_life_bit instead.")
  (Dinse_life_bit m))

(cl:ensure-generic-function 'Dinse_current_on-val :lambda-list '(m))
(cl:defmethod Dinse_current_on-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_current_on-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_current_on instead.")
  (Dinse_current_on m))

(cl:ensure-generic-function 'Dinse_service_interval-val :lambda-list '(m))
(cl:defmethod Dinse_service_interval-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_service_interval-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_service_interval instead.")
  (Dinse_service_interval m))

(cl:ensure-generic-function 'Dinse_intern_fault-val :lambda-list '(m))
(cl:defmethod Dinse_intern_fault-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_intern_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_intern_fault instead.")
  (Dinse_intern_fault m))

(cl:ensure-generic-function 'Dinse_emergency_stop-val :lambda-list '(m))
(cl:defmethod Dinse_emergency_stop-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_emergency_stop-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_emergency_stop instead.")
  (Dinse_emergency_stop m))

(cl:ensure-generic-function 'Dinse_gas_fault-val :lambda-list '(m))
(cl:defmethod Dinse_gas_fault-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_gas_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_gas_fault instead.")
  (Dinse_gas_fault m))

(cl:ensure-generic-function 'Dinse_water_fault-val :lambda-list '(m))
(cl:defmethod Dinse_water_fault-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_water_fault-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_water_fault instead.")
  (Dinse_water_fault m))

(cl:ensure-generic-function 'Dinse_process_active-val :lambda-list '(m))
(cl:defmethod Dinse_process_active-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_process_active-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_process_active instead.")
  (Dinse_process_active m))

(cl:ensure-generic-function 'Dinse_wire_end-val :lambda-list '(m))
(cl:defmethod Dinse_wire_end-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_end-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_end instead.")
  (Dinse_wire_end m))

(cl:ensure-generic-function 'Dinse_wire_movement_on_stop-val :lambda-list '(m))
(cl:defmethod Dinse_wire_movement_on_stop-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:Dinse_wire_movement_on_stop-val is deprecated.  Use kuka_rsi_msgs-msg:Dinse_wire_movement_on_stop instead.")
  (Dinse_wire_movement_on_stop m))

(cl:ensure-generic-function 'EWM_current_flows-val :lambda-list '(m))
(cl:defmethod EWM_current_flows-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_current_flows-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_current_flows instead.")
  (EWM_current_flows m))

(cl:ensure-generic-function 'EWM_ready_for_welding-val :lambda-list '(m))
(cl:defmethod EWM_ready_for_welding-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_ready_for_welding-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_ready_for_welding instead.")
  (EWM_ready_for_welding m))

(cl:ensure-generic-function 'EWM_sticking-val :lambda-list '(m))
(cl:defmethod EWM_sticking-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_sticking-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_sticking instead.")
  (EWM_sticking m))

(cl:ensure-generic-function 'EWM_error_1-val :lambda-list '(m))
(cl:defmethod EWM_error_1-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_error_1-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_error_1 instead.")
  (EWM_error_1 m))

(cl:ensure-generic-function 'EWM_collision_signal-val :lambda-list '(m))
(cl:defmethod EWM_collision_signal-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_collision_signal-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_collision_signal instead.")
  (EWM_collision_signal m))

(cl:ensure-generic-function 'EWM_program_sequence_on_main_current-val :lambda-list '(m))
(cl:defmethod EWM_program_sequence_on_main_current-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_program_sequence_on_main_current-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_program_sequence_on_main_current instead.")
  (EWM_program_sequence_on_main_current m))

(cl:ensure-generic-function 'EWM_process_active-val :lambda-list '(m))
(cl:defmethod EWM_process_active-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_process_active-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_process_active instead.")
  (EWM_process_active m))

(cl:ensure-generic-function 'EWM_current_flows_aux_process-val :lambda-list '(m))
(cl:defmethod EWM_current_flows_aux_process-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_current_flows_aux_process-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_current_flows_aux_process instead.")
  (EWM_current_flows_aux_process m))

(cl:ensure-generic-function 'EWM_error_number-val :lambda-list '(m))
(cl:defmethod EWM_error_number-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_error_number-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_error_number instead.")
  (EWM_error_number m))

(cl:ensure-generic-function 'EWM_network_phases_status-val :lambda-list '(m))
(cl:defmethod EWM_network_phases_status-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_network_phases_status-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_network_phases_status instead.")
  (EWM_network_phases_status m))

(cl:ensure-generic-function 'EWM_user_defined_input_1-val :lambda-list '(m))
(cl:defmethod EWM_user_defined_input_1-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_user_defined_input_1-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_user_defined_input_1 instead.")
  (EWM_user_defined_input_1 m))

(cl:ensure-generic-function 'EWM_no_external_stop_of_operation-val :lambda-list '(m))
(cl:defmethod EWM_no_external_stop_of_operation-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_no_external_stop_of_operation-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_no_external_stop_of_operation instead.")
  (EWM_no_external_stop_of_operation m))

(cl:ensure-generic-function 'EWM_user_defined_input_2-val :lambda-list '(m))
(cl:defmethod EWM_user_defined_input_2-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_user_defined_input_2-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_user_defined_input_2 instead.")
  (EWM_user_defined_input_2 m))

(cl:ensure-generic-function 'EWM_wire_available-val :lambda-list '(m))
(cl:defmethod EWM_wire_available-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_wire_available-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_wire_available instead.")
  (EWM_wire_available m))

(cl:ensure-generic-function 'EWM_wirefeeder_ok-val :lambda-list '(m))
(cl:defmethod EWM_wirefeeder_ok-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_wirefeeder_ok-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_wirefeeder_ok instead.")
  (EWM_wirefeeder_ok m))

(cl:ensure-generic-function 'EWM_gas_ok-val :lambda-list '(m))
(cl:defmethod EWM_gas_ok-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_gas_ok-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_gas_ok instead.")
  (EWM_gas_ok m))

(cl:ensure-generic-function 'EWM_cooland_water_ok-val :lambda-list '(m))
(cl:defmethod EWM_cooland_water_ok-val ((m <PlasmaState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kuka_rsi_msgs-msg:EWM_cooland_water_ok-val is deprecated.  Use kuka_rsi_msgs-msg:EWM_cooland_water_ok instead.")
  (EWM_cooland_water_ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlasmaState>) ostream)
  "Serializes a message object of type '<PlasmaState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'Dinse_wire_feed_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'EWM_voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'EWM_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'EWM_wire_feed_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_wire_feeder_ready) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_collective_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_wire_feed_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_power_failure) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_positioning_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_hot_wire_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_life_bit) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_current_on) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_service_interval) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_intern_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_emergency_stop) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_gas_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_water_fault) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_process_active) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_wire_end) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Dinse_wire_movement_on_stop) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_current_flows) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_ready_for_welding) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_sticking) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_error_1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_collision_signal) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_program_sequence_on_main_current) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_process_active) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_current_flows_aux_process) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EWM_error_number)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_network_phases_status) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_user_defined_input_1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_no_external_stop_of_operation) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_user_defined_input_2) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_wire_available) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_wirefeeder_ok) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_gas_ok) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'EWM_cooland_water_ok) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlasmaState>) istream)
  "Deserializes a message object of type '<PlasmaState>"
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
    (cl:setf (cl:slot-value msg 'EWM_voltage) (roslisp-utils:decode-single-float-bits bits)))
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
    (cl:setf (cl:slot-value msg 'EWM_wire_feed_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'Dinse_wire_feeder_ready) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_collective_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_wire_feed_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_power_failure) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_positioning_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_hot_wire_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_life_bit) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_current_on) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_service_interval) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_intern_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_emergency_stop) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_gas_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_water_fault) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_process_active) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_wire_end) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Dinse_wire_movement_on_stop) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_current_flows) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_ready_for_welding) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_sticking) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_error_1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_collision_signal) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_program_sequence_on_main_current) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_process_active) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_current_flows_aux_process) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EWM_error_number)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'EWM_network_phases_status) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_user_defined_input_1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_no_external_stop_of_operation) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_user_defined_input_2) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_wire_available) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_wirefeeder_ok) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_gas_ok) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'EWM_cooland_water_ok) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlasmaState>)))
  "Returns string type for a message object of type '<PlasmaState>"
  "kuka_rsi_msgs/PlasmaState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlasmaState)))
  "Returns string type for a message object of type 'PlasmaState"
  "kuka_rsi_msgs/PlasmaState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlasmaState>)))
  "Returns md5sum for a message object of type '<PlasmaState>"
  "69caddae70f327bd935d395e65e0ca27")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlasmaState)))
  "Returns md5sum for a message object of type 'PlasmaState"
  "69caddae70f327bd935d395e65e0ca27")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlasmaState>)))
  "Returns full string definition for message of type '<PlasmaState>"
  (cl:format cl:nil "Header header~%# Field 3-4~%float32 Dinse_wire_feed_speed~%# Field 8-9~%float32 EWM_voltage~%# Field 10-11~%float32 EWM_current~%# Field 12-13~%float32 EWM_wire_feed_speed~%# Field 1~%bool Dinse_wire_feeder_ready~%bool Dinse_collective_fault~%bool Dinse_wire_feed_fault~%bool Dinse_power_failure~%bool Dinse_positioning_fault~%bool Dinse_hot_wire_fault~%bool Dinse_life_bit~%bool Dinse_current_on~%# Field 2~%bool Dinse_service_interval~%bool Dinse_intern_fault~%bool Dinse_emergency_stop~%bool Dinse_gas_fault~%bool Dinse_water_fault~%bool Dinse_process_active~%bool Dinse_wire_end~%bool Dinse_wire_movement_on_stop~%# Field 5~%bool EWM_current_flows~%bool EWM_ready_for_welding~%bool EWM_sticking~%bool EWM_error_1~%bool EWM_collision_signal~%bool EWM_program_sequence_on_main_current~%bool EWM_process_active~%bool EWM_current_flows_aux_process~%# Field 6~%uint8 EWM_error_number~%# Field 7~%bool EWM_network_phases_status~%bool EWM_user_defined_input_1~%bool EWM_no_external_stop_of_operation~%bool EWM_user_defined_input_2~%bool EWM_wire_available~%bool EWM_wirefeeder_ok~%bool EWM_gas_ok~%bool EWM_cooland_water_ok~%#~%# Commented fields are not used in WAAM Interface (welding_display.cpp)~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlasmaState)))
  "Returns full string definition for message of type 'PlasmaState"
  (cl:format cl:nil "Header header~%# Field 3-4~%float32 Dinse_wire_feed_speed~%# Field 8-9~%float32 EWM_voltage~%# Field 10-11~%float32 EWM_current~%# Field 12-13~%float32 EWM_wire_feed_speed~%# Field 1~%bool Dinse_wire_feeder_ready~%bool Dinse_collective_fault~%bool Dinse_wire_feed_fault~%bool Dinse_power_failure~%bool Dinse_positioning_fault~%bool Dinse_hot_wire_fault~%bool Dinse_life_bit~%bool Dinse_current_on~%# Field 2~%bool Dinse_service_interval~%bool Dinse_intern_fault~%bool Dinse_emergency_stop~%bool Dinse_gas_fault~%bool Dinse_water_fault~%bool Dinse_process_active~%bool Dinse_wire_end~%bool Dinse_wire_movement_on_stop~%# Field 5~%bool EWM_current_flows~%bool EWM_ready_for_welding~%bool EWM_sticking~%bool EWM_error_1~%bool EWM_collision_signal~%bool EWM_program_sequence_on_main_current~%bool EWM_process_active~%bool EWM_current_flows_aux_process~%# Field 6~%uint8 EWM_error_number~%# Field 7~%bool EWM_network_phases_status~%bool EWM_user_defined_input_1~%bool EWM_no_external_stop_of_operation~%bool EWM_user_defined_input_2~%bool EWM_wire_available~%bool EWM_wirefeeder_ok~%bool EWM_gas_ok~%bool EWM_cooland_water_ok~%#~%# Commented fields are not used in WAAM Interface (welding_display.cpp)~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlasmaState>))
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
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlasmaState>))
  "Converts a ROS message object to a list"
  (cl:list 'PlasmaState
    (cl:cons ':header (header msg))
    (cl:cons ':Dinse_wire_feed_speed (Dinse_wire_feed_speed msg))
    (cl:cons ':EWM_voltage (EWM_voltage msg))
    (cl:cons ':EWM_current (EWM_current msg))
    (cl:cons ':EWM_wire_feed_speed (EWM_wire_feed_speed msg))
    (cl:cons ':Dinse_wire_feeder_ready (Dinse_wire_feeder_ready msg))
    (cl:cons ':Dinse_collective_fault (Dinse_collective_fault msg))
    (cl:cons ':Dinse_wire_feed_fault (Dinse_wire_feed_fault msg))
    (cl:cons ':Dinse_power_failure (Dinse_power_failure msg))
    (cl:cons ':Dinse_positioning_fault (Dinse_positioning_fault msg))
    (cl:cons ':Dinse_hot_wire_fault (Dinse_hot_wire_fault msg))
    (cl:cons ':Dinse_life_bit (Dinse_life_bit msg))
    (cl:cons ':Dinse_current_on (Dinse_current_on msg))
    (cl:cons ':Dinse_service_interval (Dinse_service_interval msg))
    (cl:cons ':Dinse_intern_fault (Dinse_intern_fault msg))
    (cl:cons ':Dinse_emergency_stop (Dinse_emergency_stop msg))
    (cl:cons ':Dinse_gas_fault (Dinse_gas_fault msg))
    (cl:cons ':Dinse_water_fault (Dinse_water_fault msg))
    (cl:cons ':Dinse_process_active (Dinse_process_active msg))
    (cl:cons ':Dinse_wire_end (Dinse_wire_end msg))
    (cl:cons ':Dinse_wire_movement_on_stop (Dinse_wire_movement_on_stop msg))
    (cl:cons ':EWM_current_flows (EWM_current_flows msg))
    (cl:cons ':EWM_ready_for_welding (EWM_ready_for_welding msg))
    (cl:cons ':EWM_sticking (EWM_sticking msg))
    (cl:cons ':EWM_error_1 (EWM_error_1 msg))
    (cl:cons ':EWM_collision_signal (EWM_collision_signal msg))
    (cl:cons ':EWM_program_sequence_on_main_current (EWM_program_sequence_on_main_current msg))
    (cl:cons ':EWM_process_active (EWM_process_active msg))
    (cl:cons ':EWM_current_flows_aux_process (EWM_current_flows_aux_process msg))
    (cl:cons ':EWM_error_number (EWM_error_number msg))
    (cl:cons ':EWM_network_phases_status (EWM_network_phases_status msg))
    (cl:cons ':EWM_user_defined_input_1 (EWM_user_defined_input_1 msg))
    (cl:cons ':EWM_no_external_stop_of_operation (EWM_no_external_stop_of_operation msg))
    (cl:cons ':EWM_user_defined_input_2 (EWM_user_defined_input_2 msg))
    (cl:cons ':EWM_wire_available (EWM_wire_available msg))
    (cl:cons ':EWM_wirefeeder_ok (EWM_wirefeeder_ok msg))
    (cl:cons ':EWM_gas_ok (EWM_gas_ok msg))
    (cl:cons ':EWM_cooland_water_ok (EWM_cooland_water_ok msg))
))
