;; Auto-generated. Do not edit!


(when (boundp 'kuka_rsi_msgs::PlasmaState)
  (if (not (find-package "KUKA_RSI_MSGS"))
    (make-package "KUKA_RSI_MSGS"))
  (shadow 'PlasmaState (find-package "KUKA_RSI_MSGS")))
(unless (find-package "KUKA_RSI_MSGS::PLASMASTATE")
  (make-package "KUKA_RSI_MSGS::PLASMASTATE"))

(in-package "ROS")
;;//! \htmlinclude PlasmaState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass kuka_rsi_msgs::PlasmaState
  :super ros::object
  :slots (_header _Dinse_wire_feed_speed _EWM_voltage _EWM_current _EWM_wire_feed_speed _Dinse_wire_feeder_ready _Dinse_collective_fault _Dinse_wire_feed_fault _Dinse_power_failure _Dinse_positioning_fault _Dinse_hot_wire_fault _Dinse_life_bit _Dinse_current_on _Dinse_service_interval _Dinse_intern_fault _Dinse_emergency_stop _Dinse_gas_fault _Dinse_water_fault _Dinse_process_active _Dinse_wire_end _Dinse_wire_movement_on_stop _EWM_current_flows _EWM_ready_for_welding _EWM_sticking _EWM_error_1 _EWM_collision_signal _EWM_program_sequence_on_main_current _EWM_process_active _EWM_current_flows_aux_process _EWM_error_number _EWM_network_phases_status _EWM_user_defined_input_1 _EWM_no_external_stop_of_operation _EWM_user_defined_input_2 _EWM_wire_available _EWM_wirefeeder_ok _EWM_gas_ok _EWM_cooland_water_ok ))

(defmethod kuka_rsi_msgs::PlasmaState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:Dinse_wire_feed_speed __Dinse_wire_feed_speed) 0.0)
    ((:EWM_voltage __EWM_voltage) 0.0)
    ((:EWM_current __EWM_current) 0.0)
    ((:EWM_wire_feed_speed __EWM_wire_feed_speed) 0.0)
    ((:Dinse_wire_feeder_ready __Dinse_wire_feeder_ready) nil)
    ((:Dinse_collective_fault __Dinse_collective_fault) nil)
    ((:Dinse_wire_feed_fault __Dinse_wire_feed_fault) nil)
    ((:Dinse_power_failure __Dinse_power_failure) nil)
    ((:Dinse_positioning_fault __Dinse_positioning_fault) nil)
    ((:Dinse_hot_wire_fault __Dinse_hot_wire_fault) nil)
    ((:Dinse_life_bit __Dinse_life_bit) nil)
    ((:Dinse_current_on __Dinse_current_on) nil)
    ((:Dinse_service_interval __Dinse_service_interval) nil)
    ((:Dinse_intern_fault __Dinse_intern_fault) nil)
    ((:Dinse_emergency_stop __Dinse_emergency_stop) nil)
    ((:Dinse_gas_fault __Dinse_gas_fault) nil)
    ((:Dinse_water_fault __Dinse_water_fault) nil)
    ((:Dinse_process_active __Dinse_process_active) nil)
    ((:Dinse_wire_end __Dinse_wire_end) nil)
    ((:Dinse_wire_movement_on_stop __Dinse_wire_movement_on_stop) nil)
    ((:EWM_current_flows __EWM_current_flows) nil)
    ((:EWM_ready_for_welding __EWM_ready_for_welding) nil)
    ((:EWM_sticking __EWM_sticking) nil)
    ((:EWM_error_1 __EWM_error_1) nil)
    ((:EWM_collision_signal __EWM_collision_signal) nil)
    ((:EWM_program_sequence_on_main_current __EWM_program_sequence_on_main_current) nil)
    ((:EWM_process_active __EWM_process_active) nil)
    ((:EWM_current_flows_aux_process __EWM_current_flows_aux_process) nil)
    ((:EWM_error_number __EWM_error_number) 0)
    ((:EWM_network_phases_status __EWM_network_phases_status) nil)
    ((:EWM_user_defined_input_1 __EWM_user_defined_input_1) nil)
    ((:EWM_no_external_stop_of_operation __EWM_no_external_stop_of_operation) nil)
    ((:EWM_user_defined_input_2 __EWM_user_defined_input_2) nil)
    ((:EWM_wire_available __EWM_wire_available) nil)
    ((:EWM_wirefeeder_ok __EWM_wirefeeder_ok) nil)
    ((:EWM_gas_ok __EWM_gas_ok) nil)
    ((:EWM_cooland_water_ok __EWM_cooland_water_ok) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _Dinse_wire_feed_speed (float __Dinse_wire_feed_speed))
   (setq _EWM_voltage (float __EWM_voltage))
   (setq _EWM_current (float __EWM_current))
   (setq _EWM_wire_feed_speed (float __EWM_wire_feed_speed))
   (setq _Dinse_wire_feeder_ready __Dinse_wire_feeder_ready)
   (setq _Dinse_collective_fault __Dinse_collective_fault)
   (setq _Dinse_wire_feed_fault __Dinse_wire_feed_fault)
   (setq _Dinse_power_failure __Dinse_power_failure)
   (setq _Dinse_positioning_fault __Dinse_positioning_fault)
   (setq _Dinse_hot_wire_fault __Dinse_hot_wire_fault)
   (setq _Dinse_life_bit __Dinse_life_bit)
   (setq _Dinse_current_on __Dinse_current_on)
   (setq _Dinse_service_interval __Dinse_service_interval)
   (setq _Dinse_intern_fault __Dinse_intern_fault)
   (setq _Dinse_emergency_stop __Dinse_emergency_stop)
   (setq _Dinse_gas_fault __Dinse_gas_fault)
   (setq _Dinse_water_fault __Dinse_water_fault)
   (setq _Dinse_process_active __Dinse_process_active)
   (setq _Dinse_wire_end __Dinse_wire_end)
   (setq _Dinse_wire_movement_on_stop __Dinse_wire_movement_on_stop)
   (setq _EWM_current_flows __EWM_current_flows)
   (setq _EWM_ready_for_welding __EWM_ready_for_welding)
   (setq _EWM_sticking __EWM_sticking)
   (setq _EWM_error_1 __EWM_error_1)
   (setq _EWM_collision_signal __EWM_collision_signal)
   (setq _EWM_program_sequence_on_main_current __EWM_program_sequence_on_main_current)
   (setq _EWM_process_active __EWM_process_active)
   (setq _EWM_current_flows_aux_process __EWM_current_flows_aux_process)
   (setq _EWM_error_number (round __EWM_error_number))
   (setq _EWM_network_phases_status __EWM_network_phases_status)
   (setq _EWM_user_defined_input_1 __EWM_user_defined_input_1)
   (setq _EWM_no_external_stop_of_operation __EWM_no_external_stop_of_operation)
   (setq _EWM_user_defined_input_2 __EWM_user_defined_input_2)
   (setq _EWM_wire_available __EWM_wire_available)
   (setq _EWM_wirefeeder_ok __EWM_wirefeeder_ok)
   (setq _EWM_gas_ok __EWM_gas_ok)
   (setq _EWM_cooland_water_ok __EWM_cooland_water_ok)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:Dinse_wire_feed_speed
   (&optional __Dinse_wire_feed_speed)
   (if __Dinse_wire_feed_speed (setq _Dinse_wire_feed_speed __Dinse_wire_feed_speed)) _Dinse_wire_feed_speed)
  (:EWM_voltage
   (&optional __EWM_voltage)
   (if __EWM_voltage (setq _EWM_voltage __EWM_voltage)) _EWM_voltage)
  (:EWM_current
   (&optional __EWM_current)
   (if __EWM_current (setq _EWM_current __EWM_current)) _EWM_current)
  (:EWM_wire_feed_speed
   (&optional __EWM_wire_feed_speed)
   (if __EWM_wire_feed_speed (setq _EWM_wire_feed_speed __EWM_wire_feed_speed)) _EWM_wire_feed_speed)
  (:Dinse_wire_feeder_ready
   (&optional (__Dinse_wire_feeder_ready :null))
   (if (not (eq __Dinse_wire_feeder_ready :null)) (setq _Dinse_wire_feeder_ready __Dinse_wire_feeder_ready)) _Dinse_wire_feeder_ready)
  (:Dinse_collective_fault
   (&optional (__Dinse_collective_fault :null))
   (if (not (eq __Dinse_collective_fault :null)) (setq _Dinse_collective_fault __Dinse_collective_fault)) _Dinse_collective_fault)
  (:Dinse_wire_feed_fault
   (&optional (__Dinse_wire_feed_fault :null))
   (if (not (eq __Dinse_wire_feed_fault :null)) (setq _Dinse_wire_feed_fault __Dinse_wire_feed_fault)) _Dinse_wire_feed_fault)
  (:Dinse_power_failure
   (&optional (__Dinse_power_failure :null))
   (if (not (eq __Dinse_power_failure :null)) (setq _Dinse_power_failure __Dinse_power_failure)) _Dinse_power_failure)
  (:Dinse_positioning_fault
   (&optional (__Dinse_positioning_fault :null))
   (if (not (eq __Dinse_positioning_fault :null)) (setq _Dinse_positioning_fault __Dinse_positioning_fault)) _Dinse_positioning_fault)
  (:Dinse_hot_wire_fault
   (&optional (__Dinse_hot_wire_fault :null))
   (if (not (eq __Dinse_hot_wire_fault :null)) (setq _Dinse_hot_wire_fault __Dinse_hot_wire_fault)) _Dinse_hot_wire_fault)
  (:Dinse_life_bit
   (&optional (__Dinse_life_bit :null))
   (if (not (eq __Dinse_life_bit :null)) (setq _Dinse_life_bit __Dinse_life_bit)) _Dinse_life_bit)
  (:Dinse_current_on
   (&optional (__Dinse_current_on :null))
   (if (not (eq __Dinse_current_on :null)) (setq _Dinse_current_on __Dinse_current_on)) _Dinse_current_on)
  (:Dinse_service_interval
   (&optional (__Dinse_service_interval :null))
   (if (not (eq __Dinse_service_interval :null)) (setq _Dinse_service_interval __Dinse_service_interval)) _Dinse_service_interval)
  (:Dinse_intern_fault
   (&optional (__Dinse_intern_fault :null))
   (if (not (eq __Dinse_intern_fault :null)) (setq _Dinse_intern_fault __Dinse_intern_fault)) _Dinse_intern_fault)
  (:Dinse_emergency_stop
   (&optional (__Dinse_emergency_stop :null))
   (if (not (eq __Dinse_emergency_stop :null)) (setq _Dinse_emergency_stop __Dinse_emergency_stop)) _Dinse_emergency_stop)
  (:Dinse_gas_fault
   (&optional (__Dinse_gas_fault :null))
   (if (not (eq __Dinse_gas_fault :null)) (setq _Dinse_gas_fault __Dinse_gas_fault)) _Dinse_gas_fault)
  (:Dinse_water_fault
   (&optional (__Dinse_water_fault :null))
   (if (not (eq __Dinse_water_fault :null)) (setq _Dinse_water_fault __Dinse_water_fault)) _Dinse_water_fault)
  (:Dinse_process_active
   (&optional (__Dinse_process_active :null))
   (if (not (eq __Dinse_process_active :null)) (setq _Dinse_process_active __Dinse_process_active)) _Dinse_process_active)
  (:Dinse_wire_end
   (&optional (__Dinse_wire_end :null))
   (if (not (eq __Dinse_wire_end :null)) (setq _Dinse_wire_end __Dinse_wire_end)) _Dinse_wire_end)
  (:Dinse_wire_movement_on_stop
   (&optional (__Dinse_wire_movement_on_stop :null))
   (if (not (eq __Dinse_wire_movement_on_stop :null)) (setq _Dinse_wire_movement_on_stop __Dinse_wire_movement_on_stop)) _Dinse_wire_movement_on_stop)
  (:EWM_current_flows
   (&optional (__EWM_current_flows :null))
   (if (not (eq __EWM_current_flows :null)) (setq _EWM_current_flows __EWM_current_flows)) _EWM_current_flows)
  (:EWM_ready_for_welding
   (&optional (__EWM_ready_for_welding :null))
   (if (not (eq __EWM_ready_for_welding :null)) (setq _EWM_ready_for_welding __EWM_ready_for_welding)) _EWM_ready_for_welding)
  (:EWM_sticking
   (&optional (__EWM_sticking :null))
   (if (not (eq __EWM_sticking :null)) (setq _EWM_sticking __EWM_sticking)) _EWM_sticking)
  (:EWM_error_1
   (&optional (__EWM_error_1 :null))
   (if (not (eq __EWM_error_1 :null)) (setq _EWM_error_1 __EWM_error_1)) _EWM_error_1)
  (:EWM_collision_signal
   (&optional (__EWM_collision_signal :null))
   (if (not (eq __EWM_collision_signal :null)) (setq _EWM_collision_signal __EWM_collision_signal)) _EWM_collision_signal)
  (:EWM_program_sequence_on_main_current
   (&optional (__EWM_program_sequence_on_main_current :null))
   (if (not (eq __EWM_program_sequence_on_main_current :null)) (setq _EWM_program_sequence_on_main_current __EWM_program_sequence_on_main_current)) _EWM_program_sequence_on_main_current)
  (:EWM_process_active
   (&optional (__EWM_process_active :null))
   (if (not (eq __EWM_process_active :null)) (setq _EWM_process_active __EWM_process_active)) _EWM_process_active)
  (:EWM_current_flows_aux_process
   (&optional (__EWM_current_flows_aux_process :null))
   (if (not (eq __EWM_current_flows_aux_process :null)) (setq _EWM_current_flows_aux_process __EWM_current_flows_aux_process)) _EWM_current_flows_aux_process)
  (:EWM_error_number
   (&optional __EWM_error_number)
   (if __EWM_error_number (setq _EWM_error_number __EWM_error_number)) _EWM_error_number)
  (:EWM_network_phases_status
   (&optional (__EWM_network_phases_status :null))
   (if (not (eq __EWM_network_phases_status :null)) (setq _EWM_network_phases_status __EWM_network_phases_status)) _EWM_network_phases_status)
  (:EWM_user_defined_input_1
   (&optional (__EWM_user_defined_input_1 :null))
   (if (not (eq __EWM_user_defined_input_1 :null)) (setq _EWM_user_defined_input_1 __EWM_user_defined_input_1)) _EWM_user_defined_input_1)
  (:EWM_no_external_stop_of_operation
   (&optional (__EWM_no_external_stop_of_operation :null))
   (if (not (eq __EWM_no_external_stop_of_operation :null)) (setq _EWM_no_external_stop_of_operation __EWM_no_external_stop_of_operation)) _EWM_no_external_stop_of_operation)
  (:EWM_user_defined_input_2
   (&optional (__EWM_user_defined_input_2 :null))
   (if (not (eq __EWM_user_defined_input_2 :null)) (setq _EWM_user_defined_input_2 __EWM_user_defined_input_2)) _EWM_user_defined_input_2)
  (:EWM_wire_available
   (&optional (__EWM_wire_available :null))
   (if (not (eq __EWM_wire_available :null)) (setq _EWM_wire_available __EWM_wire_available)) _EWM_wire_available)
  (:EWM_wirefeeder_ok
   (&optional (__EWM_wirefeeder_ok :null))
   (if (not (eq __EWM_wirefeeder_ok :null)) (setq _EWM_wirefeeder_ok __EWM_wirefeeder_ok)) _EWM_wirefeeder_ok)
  (:EWM_gas_ok
   (&optional (__EWM_gas_ok :null))
   (if (not (eq __EWM_gas_ok :null)) (setq _EWM_gas_ok __EWM_gas_ok)) _EWM_gas_ok)
  (:EWM_cooland_water_ok
   (&optional (__EWM_cooland_water_ok :null))
   (if (not (eq __EWM_cooland_water_ok :null)) (setq _EWM_cooland_water_ok __EWM_cooland_water_ok)) _EWM_cooland_water_ok)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _Dinse_wire_feed_speed
    4
    ;; float32 _EWM_voltage
    4
    ;; float32 _EWM_current
    4
    ;; float32 _EWM_wire_feed_speed
    4
    ;; bool _Dinse_wire_feeder_ready
    1
    ;; bool _Dinse_collective_fault
    1
    ;; bool _Dinse_wire_feed_fault
    1
    ;; bool _Dinse_power_failure
    1
    ;; bool _Dinse_positioning_fault
    1
    ;; bool _Dinse_hot_wire_fault
    1
    ;; bool _Dinse_life_bit
    1
    ;; bool _Dinse_current_on
    1
    ;; bool _Dinse_service_interval
    1
    ;; bool _Dinse_intern_fault
    1
    ;; bool _Dinse_emergency_stop
    1
    ;; bool _Dinse_gas_fault
    1
    ;; bool _Dinse_water_fault
    1
    ;; bool _Dinse_process_active
    1
    ;; bool _Dinse_wire_end
    1
    ;; bool _Dinse_wire_movement_on_stop
    1
    ;; bool _EWM_current_flows
    1
    ;; bool _EWM_ready_for_welding
    1
    ;; bool _EWM_sticking
    1
    ;; bool _EWM_error_1
    1
    ;; bool _EWM_collision_signal
    1
    ;; bool _EWM_program_sequence_on_main_current
    1
    ;; bool _EWM_process_active
    1
    ;; bool _EWM_current_flows_aux_process
    1
    ;; uint8 _EWM_error_number
    1
    ;; bool _EWM_network_phases_status
    1
    ;; bool _EWM_user_defined_input_1
    1
    ;; bool _EWM_no_external_stop_of_operation
    1
    ;; bool _EWM_user_defined_input_2
    1
    ;; bool _EWM_wire_available
    1
    ;; bool _EWM_wirefeeder_ok
    1
    ;; bool _EWM_gas_ok
    1
    ;; bool _EWM_cooland_water_ok
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _Dinse_wire_feed_speed
       (sys::poke _Dinse_wire_feed_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _EWM_voltage
       (sys::poke _EWM_voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _EWM_current
       (sys::poke _EWM_current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _EWM_wire_feed_speed
       (sys::poke _EWM_wire_feed_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _Dinse_wire_feeder_ready
       (if _Dinse_wire_feeder_ready (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_collective_fault
       (if _Dinse_collective_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_wire_feed_fault
       (if _Dinse_wire_feed_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_power_failure
       (if _Dinse_power_failure (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_positioning_fault
       (if _Dinse_positioning_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_hot_wire_fault
       (if _Dinse_hot_wire_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_life_bit
       (if _Dinse_life_bit (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_current_on
       (if _Dinse_current_on (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_service_interval
       (if _Dinse_service_interval (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_intern_fault
       (if _Dinse_intern_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_emergency_stop
       (if _Dinse_emergency_stop (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_gas_fault
       (if _Dinse_gas_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_water_fault
       (if _Dinse_water_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_process_active
       (if _Dinse_process_active (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_wire_end
       (if _Dinse_wire_end (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_wire_movement_on_stop
       (if _Dinse_wire_movement_on_stop (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_current_flows
       (if _EWM_current_flows (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_ready_for_welding
       (if _EWM_ready_for_welding (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_sticking
       (if _EWM_sticking (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_error_1
       (if _EWM_error_1 (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_collision_signal
       (if _EWM_collision_signal (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_program_sequence_on_main_current
       (if _EWM_program_sequence_on_main_current (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_process_active
       (if _EWM_process_active (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_current_flows_aux_process
       (if _EWM_current_flows_aux_process (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _EWM_error_number
       (write-byte _EWM_error_number s)
     ;; bool _EWM_network_phases_status
       (if _EWM_network_phases_status (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_user_defined_input_1
       (if _EWM_user_defined_input_1 (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_no_external_stop_of_operation
       (if _EWM_no_external_stop_of_operation (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_user_defined_input_2
       (if _EWM_user_defined_input_2 (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_wire_available
       (if _EWM_wire_available (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_wirefeeder_ok
       (if _EWM_wirefeeder_ok (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_gas_ok
       (if _EWM_gas_ok (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_cooland_water_ok
       (if _EWM_cooland_water_ok (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _Dinse_wire_feed_speed
     (setq _Dinse_wire_feed_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _EWM_voltage
     (setq _EWM_voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _EWM_current
     (setq _EWM_current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _EWM_wire_feed_speed
     (setq _EWM_wire_feed_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _Dinse_wire_feeder_ready
     (setq _Dinse_wire_feeder_ready (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_collective_fault
     (setq _Dinse_collective_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_wire_feed_fault
     (setq _Dinse_wire_feed_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_power_failure
     (setq _Dinse_power_failure (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_positioning_fault
     (setq _Dinse_positioning_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_hot_wire_fault
     (setq _Dinse_hot_wire_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_life_bit
     (setq _Dinse_life_bit (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_current_on
     (setq _Dinse_current_on (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_service_interval
     (setq _Dinse_service_interval (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_intern_fault
     (setq _Dinse_intern_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_emergency_stop
     (setq _Dinse_emergency_stop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_gas_fault
     (setq _Dinse_gas_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_water_fault
     (setq _Dinse_water_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_process_active
     (setq _Dinse_process_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_wire_end
     (setq _Dinse_wire_end (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_wire_movement_on_stop
     (setq _Dinse_wire_movement_on_stop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_current_flows
     (setq _EWM_current_flows (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_ready_for_welding
     (setq _EWM_ready_for_welding (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_sticking
     (setq _EWM_sticking (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_error_1
     (setq _EWM_error_1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_collision_signal
     (setq _EWM_collision_signal (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_program_sequence_on_main_current
     (setq _EWM_program_sequence_on_main_current (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_process_active
     (setq _EWM_process_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_current_flows_aux_process
     (setq _EWM_current_flows_aux_process (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _EWM_error_number
     (setq _EWM_error_number (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _EWM_network_phases_status
     (setq _EWM_network_phases_status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_user_defined_input_1
     (setq _EWM_user_defined_input_1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_no_external_stop_of_operation
     (setq _EWM_no_external_stop_of_operation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_user_defined_input_2
     (setq _EWM_user_defined_input_2 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_wire_available
     (setq _EWM_wire_available (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_wirefeeder_ok
     (setq _EWM_wirefeeder_ok (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_gas_ok
     (setq _EWM_gas_ok (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_cooland_water_ok
     (setq _EWM_cooland_water_ok (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get kuka_rsi_msgs::PlasmaState :md5sum-) "69caddae70f327bd935d395e65e0ca27")
(setf (get kuka_rsi_msgs::PlasmaState :datatype-) "kuka_rsi_msgs/PlasmaState")
(setf (get kuka_rsi_msgs::PlasmaState :definition-)
      "Header header
# Field 3-4
float32 Dinse_wire_feed_speed
# Field 8-9
float32 EWM_voltage
# Field 10-11
float32 EWM_current
# Field 12-13
float32 EWM_wire_feed_speed
# Field 1
bool Dinse_wire_feeder_ready
bool Dinse_collective_fault
bool Dinse_wire_feed_fault
bool Dinse_power_failure
bool Dinse_positioning_fault
bool Dinse_hot_wire_fault
bool Dinse_life_bit
bool Dinse_current_on
# Field 2
bool Dinse_service_interval
bool Dinse_intern_fault
bool Dinse_emergency_stop
bool Dinse_gas_fault
bool Dinse_water_fault
bool Dinse_process_active
bool Dinse_wire_end
bool Dinse_wire_movement_on_stop
# Field 5
bool EWM_current_flows
bool EWM_ready_for_welding
bool EWM_sticking
bool EWM_error_1
bool EWM_collision_signal
bool EWM_program_sequence_on_main_current
bool EWM_process_active
bool EWM_current_flows_aux_process
# Field 6
uint8 EWM_error_number
# Field 7
bool EWM_network_phases_status
bool EWM_user_defined_input_1
bool EWM_no_external_stop_of_operation
bool EWM_user_defined_input_2
bool EWM_wire_available
bool EWM_wirefeeder_ok
bool EWM_gas_ok
bool EWM_cooland_water_ok
#
# Commented fields are not used in WAAM Interface (welding_display.cpp)
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



(provide :kuka_rsi_msgs/PlasmaState "69caddae70f327bd935d395e65e0ca27")


