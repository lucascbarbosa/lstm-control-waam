;; Auto-generated. Do not edit!


(when (boundp 'kuka_rsi_msgs::PlasmaCommand)
  (if (not (find-package "KUKA_RSI_MSGS"))
    (make-package "KUKA_RSI_MSGS"))
  (shadow 'PlasmaCommand (find-package "KUKA_RSI_MSGS")))
(unless (find-package "KUKA_RSI_MSGS::PLASMACOMMAND")
  (make-package "KUKA_RSI_MSGS::PLASMACOMMAND"))

(in-package "ROS")
;;//! \htmlinclude PlasmaCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass kuka_rsi_msgs::PlasmaCommand
  :super ros::object
  :slots (_header _Dinse_wire_feed_speed _EWM_current _EWM_plasma_gas _EWM_shield_gas _Dinse_start_release _Dinse_acknowledge_fault _Dinse_start_wire_feed _Dinse_start_power_source _Dinse_wirebreak _Dinse_wire_forward _Dinse_wire_backward _Dinse_gas_on _Dinse_retraction _Dinse_positioning _EWM_Start _EWM_gas_test_1_shield _EWM_gas_test_2_plasma _EWM_feed_wire _EWM_unfeed_wire _EWM_position_search _EWM_error_reset _EWM_start_aux_process _EWM_user_relay _EWM_welding_simulation _EWM_monitoring_function _EWM_filler_wire_activated _EWM_reserved_1 _EWM_weld_mode_select_bit_0 _EWM_weld_mode_select_bit_1 _EWM_wirefeeder_switch _EWM_reserved_2 _EWM_cold_wire_feed_speed _EWM_job_number ))

(defmethod kuka_rsi_msgs::PlasmaCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:Dinse_wire_feed_speed __Dinse_wire_feed_speed) 0.0)
    ((:EWM_current __EWM_current) 0.0)
    ((:EWM_plasma_gas __EWM_plasma_gas) 0.0)
    ((:EWM_shield_gas __EWM_shield_gas) 0.0)
    ((:Dinse_start_release __Dinse_start_release) nil)
    ((:Dinse_acknowledge_fault __Dinse_acknowledge_fault) nil)
    ((:Dinse_start_wire_feed __Dinse_start_wire_feed) nil)
    ((:Dinse_start_power_source __Dinse_start_power_source) nil)
    ((:Dinse_wirebreak __Dinse_wirebreak) nil)
    ((:Dinse_wire_forward __Dinse_wire_forward) nil)
    ((:Dinse_wire_backward __Dinse_wire_backward) nil)
    ((:Dinse_gas_on __Dinse_gas_on) nil)
    ((:Dinse_retraction __Dinse_retraction) nil)
    ((:Dinse_positioning __Dinse_positioning) nil)
    ((:EWM_Start __EWM_Start) nil)
    ((:EWM_gas_test_1_shield __EWM_gas_test_1_shield) nil)
    ((:EWM_gas_test_2_plasma __EWM_gas_test_2_plasma) nil)
    ((:EWM_feed_wire __EWM_feed_wire) nil)
    ((:EWM_unfeed_wire __EWM_unfeed_wire) nil)
    ((:EWM_position_search __EWM_position_search) nil)
    ((:EWM_error_reset __EWM_error_reset) nil)
    ((:EWM_start_aux_process __EWM_start_aux_process) nil)
    ((:EWM_user_relay __EWM_user_relay) nil)
    ((:EWM_welding_simulation __EWM_welding_simulation) nil)
    ((:EWM_monitoring_function __EWM_monitoring_function) nil)
    ((:EWM_filler_wire_activated __EWM_filler_wire_activated) nil)
    ((:EWM_reserved_1 __EWM_reserved_1) nil)
    ((:EWM_weld_mode_select_bit_0 __EWM_weld_mode_select_bit_0) nil)
    ((:EWM_weld_mode_select_bit_1 __EWM_weld_mode_select_bit_1) nil)
    ((:EWM_wirefeeder_switch __EWM_wirefeeder_switch) nil)
    ((:EWM_reserved_2 __EWM_reserved_2) nil)
    ((:EWM_cold_wire_feed_speed __EWM_cold_wire_feed_speed) 0.0)
    ((:EWM_job_number __EWM_job_number) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _Dinse_wire_feed_speed (float __Dinse_wire_feed_speed))
   (setq _EWM_current (float __EWM_current))
   (setq _EWM_plasma_gas (float __EWM_plasma_gas))
   (setq _EWM_shield_gas (float __EWM_shield_gas))
   (setq _Dinse_start_release __Dinse_start_release)
   (setq _Dinse_acknowledge_fault __Dinse_acknowledge_fault)
   (setq _Dinse_start_wire_feed __Dinse_start_wire_feed)
   (setq _Dinse_start_power_source __Dinse_start_power_source)
   (setq _Dinse_wirebreak __Dinse_wirebreak)
   (setq _Dinse_wire_forward __Dinse_wire_forward)
   (setq _Dinse_wire_backward __Dinse_wire_backward)
   (setq _Dinse_gas_on __Dinse_gas_on)
   (setq _Dinse_retraction __Dinse_retraction)
   (setq _Dinse_positioning __Dinse_positioning)
   (setq _EWM_Start __EWM_Start)
   (setq _EWM_gas_test_1_shield __EWM_gas_test_1_shield)
   (setq _EWM_gas_test_2_plasma __EWM_gas_test_2_plasma)
   (setq _EWM_feed_wire __EWM_feed_wire)
   (setq _EWM_unfeed_wire __EWM_unfeed_wire)
   (setq _EWM_position_search __EWM_position_search)
   (setq _EWM_error_reset __EWM_error_reset)
   (setq _EWM_start_aux_process __EWM_start_aux_process)
   (setq _EWM_user_relay __EWM_user_relay)
   (setq _EWM_welding_simulation __EWM_welding_simulation)
   (setq _EWM_monitoring_function __EWM_monitoring_function)
   (setq _EWM_filler_wire_activated __EWM_filler_wire_activated)
   (setq _EWM_reserved_1 __EWM_reserved_1)
   (setq _EWM_weld_mode_select_bit_0 __EWM_weld_mode_select_bit_0)
   (setq _EWM_weld_mode_select_bit_1 __EWM_weld_mode_select_bit_1)
   (setq _EWM_wirefeeder_switch __EWM_wirefeeder_switch)
   (setq _EWM_reserved_2 __EWM_reserved_2)
   (setq _EWM_cold_wire_feed_speed (float __EWM_cold_wire_feed_speed))
   (setq _EWM_job_number (round __EWM_job_number))
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
  (:EWM_current
   (&optional __EWM_current)
   (if __EWM_current (setq _EWM_current __EWM_current)) _EWM_current)
  (:EWM_plasma_gas
   (&optional __EWM_plasma_gas)
   (if __EWM_plasma_gas (setq _EWM_plasma_gas __EWM_plasma_gas)) _EWM_plasma_gas)
  (:EWM_shield_gas
   (&optional __EWM_shield_gas)
   (if __EWM_shield_gas (setq _EWM_shield_gas __EWM_shield_gas)) _EWM_shield_gas)
  (:Dinse_start_release
   (&optional (__Dinse_start_release :null))
   (if (not (eq __Dinse_start_release :null)) (setq _Dinse_start_release __Dinse_start_release)) _Dinse_start_release)
  (:Dinse_acknowledge_fault
   (&optional (__Dinse_acknowledge_fault :null))
   (if (not (eq __Dinse_acknowledge_fault :null)) (setq _Dinse_acknowledge_fault __Dinse_acknowledge_fault)) _Dinse_acknowledge_fault)
  (:Dinse_start_wire_feed
   (&optional (__Dinse_start_wire_feed :null))
   (if (not (eq __Dinse_start_wire_feed :null)) (setq _Dinse_start_wire_feed __Dinse_start_wire_feed)) _Dinse_start_wire_feed)
  (:Dinse_start_power_source
   (&optional (__Dinse_start_power_source :null))
   (if (not (eq __Dinse_start_power_source :null)) (setq _Dinse_start_power_source __Dinse_start_power_source)) _Dinse_start_power_source)
  (:Dinse_wirebreak
   (&optional (__Dinse_wirebreak :null))
   (if (not (eq __Dinse_wirebreak :null)) (setq _Dinse_wirebreak __Dinse_wirebreak)) _Dinse_wirebreak)
  (:Dinse_wire_forward
   (&optional (__Dinse_wire_forward :null))
   (if (not (eq __Dinse_wire_forward :null)) (setq _Dinse_wire_forward __Dinse_wire_forward)) _Dinse_wire_forward)
  (:Dinse_wire_backward
   (&optional (__Dinse_wire_backward :null))
   (if (not (eq __Dinse_wire_backward :null)) (setq _Dinse_wire_backward __Dinse_wire_backward)) _Dinse_wire_backward)
  (:Dinse_gas_on
   (&optional (__Dinse_gas_on :null))
   (if (not (eq __Dinse_gas_on :null)) (setq _Dinse_gas_on __Dinse_gas_on)) _Dinse_gas_on)
  (:Dinse_retraction
   (&optional (__Dinse_retraction :null))
   (if (not (eq __Dinse_retraction :null)) (setq _Dinse_retraction __Dinse_retraction)) _Dinse_retraction)
  (:Dinse_positioning
   (&optional (__Dinse_positioning :null))
   (if (not (eq __Dinse_positioning :null)) (setq _Dinse_positioning __Dinse_positioning)) _Dinse_positioning)
  (:EWM_Start
   (&optional (__EWM_Start :null))
   (if (not (eq __EWM_Start :null)) (setq _EWM_Start __EWM_Start)) _EWM_Start)
  (:EWM_gas_test_1_shield
   (&optional (__EWM_gas_test_1_shield :null))
   (if (not (eq __EWM_gas_test_1_shield :null)) (setq _EWM_gas_test_1_shield __EWM_gas_test_1_shield)) _EWM_gas_test_1_shield)
  (:EWM_gas_test_2_plasma
   (&optional (__EWM_gas_test_2_plasma :null))
   (if (not (eq __EWM_gas_test_2_plasma :null)) (setq _EWM_gas_test_2_plasma __EWM_gas_test_2_plasma)) _EWM_gas_test_2_plasma)
  (:EWM_feed_wire
   (&optional (__EWM_feed_wire :null))
   (if (not (eq __EWM_feed_wire :null)) (setq _EWM_feed_wire __EWM_feed_wire)) _EWM_feed_wire)
  (:EWM_unfeed_wire
   (&optional (__EWM_unfeed_wire :null))
   (if (not (eq __EWM_unfeed_wire :null)) (setq _EWM_unfeed_wire __EWM_unfeed_wire)) _EWM_unfeed_wire)
  (:EWM_position_search
   (&optional (__EWM_position_search :null))
   (if (not (eq __EWM_position_search :null)) (setq _EWM_position_search __EWM_position_search)) _EWM_position_search)
  (:EWM_error_reset
   (&optional (__EWM_error_reset :null))
   (if (not (eq __EWM_error_reset :null)) (setq _EWM_error_reset __EWM_error_reset)) _EWM_error_reset)
  (:EWM_start_aux_process
   (&optional (__EWM_start_aux_process :null))
   (if (not (eq __EWM_start_aux_process :null)) (setq _EWM_start_aux_process __EWM_start_aux_process)) _EWM_start_aux_process)
  (:EWM_user_relay
   (&optional (__EWM_user_relay :null))
   (if (not (eq __EWM_user_relay :null)) (setq _EWM_user_relay __EWM_user_relay)) _EWM_user_relay)
  (:EWM_welding_simulation
   (&optional (__EWM_welding_simulation :null))
   (if (not (eq __EWM_welding_simulation :null)) (setq _EWM_welding_simulation __EWM_welding_simulation)) _EWM_welding_simulation)
  (:EWM_monitoring_function
   (&optional (__EWM_monitoring_function :null))
   (if (not (eq __EWM_monitoring_function :null)) (setq _EWM_monitoring_function __EWM_monitoring_function)) _EWM_monitoring_function)
  (:EWM_filler_wire_activated
   (&optional (__EWM_filler_wire_activated :null))
   (if (not (eq __EWM_filler_wire_activated :null)) (setq _EWM_filler_wire_activated __EWM_filler_wire_activated)) _EWM_filler_wire_activated)
  (:EWM_reserved_1
   (&optional (__EWM_reserved_1 :null))
   (if (not (eq __EWM_reserved_1 :null)) (setq _EWM_reserved_1 __EWM_reserved_1)) _EWM_reserved_1)
  (:EWM_weld_mode_select_bit_0
   (&optional (__EWM_weld_mode_select_bit_0 :null))
   (if (not (eq __EWM_weld_mode_select_bit_0 :null)) (setq _EWM_weld_mode_select_bit_0 __EWM_weld_mode_select_bit_0)) _EWM_weld_mode_select_bit_0)
  (:EWM_weld_mode_select_bit_1
   (&optional (__EWM_weld_mode_select_bit_1 :null))
   (if (not (eq __EWM_weld_mode_select_bit_1 :null)) (setq _EWM_weld_mode_select_bit_1 __EWM_weld_mode_select_bit_1)) _EWM_weld_mode_select_bit_1)
  (:EWM_wirefeeder_switch
   (&optional (__EWM_wirefeeder_switch :null))
   (if (not (eq __EWM_wirefeeder_switch :null)) (setq _EWM_wirefeeder_switch __EWM_wirefeeder_switch)) _EWM_wirefeeder_switch)
  (:EWM_reserved_2
   (&optional (__EWM_reserved_2 :null))
   (if (not (eq __EWM_reserved_2 :null)) (setq _EWM_reserved_2 __EWM_reserved_2)) _EWM_reserved_2)
  (:EWM_cold_wire_feed_speed
   (&optional __EWM_cold_wire_feed_speed)
   (if __EWM_cold_wire_feed_speed (setq _EWM_cold_wire_feed_speed __EWM_cold_wire_feed_speed)) _EWM_cold_wire_feed_speed)
  (:EWM_job_number
   (&optional __EWM_job_number)
   (if __EWM_job_number (setq _EWM_job_number __EWM_job_number)) _EWM_job_number)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _Dinse_wire_feed_speed
    4
    ;; float32 _EWM_current
    4
    ;; float32 _EWM_plasma_gas
    4
    ;; float32 _EWM_shield_gas
    4
    ;; bool _Dinse_start_release
    1
    ;; bool _Dinse_acknowledge_fault
    1
    ;; bool _Dinse_start_wire_feed
    1
    ;; bool _Dinse_start_power_source
    1
    ;; bool _Dinse_wirebreak
    1
    ;; bool _Dinse_wire_forward
    1
    ;; bool _Dinse_wire_backward
    1
    ;; bool _Dinse_gas_on
    1
    ;; bool _Dinse_retraction
    1
    ;; bool _Dinse_positioning
    1
    ;; bool _EWM_Start
    1
    ;; bool _EWM_gas_test_1_shield
    1
    ;; bool _EWM_gas_test_2_plasma
    1
    ;; bool _EWM_feed_wire
    1
    ;; bool _EWM_unfeed_wire
    1
    ;; bool _EWM_position_search
    1
    ;; bool _EWM_error_reset
    1
    ;; bool _EWM_start_aux_process
    1
    ;; bool _EWM_user_relay
    1
    ;; bool _EWM_welding_simulation
    1
    ;; bool _EWM_monitoring_function
    1
    ;; bool _EWM_filler_wire_activated
    1
    ;; bool _EWM_reserved_1
    1
    ;; bool _EWM_weld_mode_select_bit_0
    1
    ;; bool _EWM_weld_mode_select_bit_1
    1
    ;; bool _EWM_wirefeeder_switch
    1
    ;; bool _EWM_reserved_2
    1
    ;; float32 _EWM_cold_wire_feed_speed
    4
    ;; uint8 _EWM_job_number
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
     ;; float32 _EWM_current
       (sys::poke _EWM_current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _EWM_plasma_gas
       (sys::poke _EWM_plasma_gas (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _EWM_shield_gas
       (sys::poke _EWM_shield_gas (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _Dinse_start_release
       (if _Dinse_start_release (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_acknowledge_fault
       (if _Dinse_acknowledge_fault (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_start_wire_feed
       (if _Dinse_start_wire_feed (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_start_power_source
       (if _Dinse_start_power_source (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_wirebreak
       (if _Dinse_wirebreak (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_wire_forward
       (if _Dinse_wire_forward (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_wire_backward
       (if _Dinse_wire_backward (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_gas_on
       (if _Dinse_gas_on (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_retraction
       (if _Dinse_retraction (write-byte -1 s) (write-byte 0 s))
     ;; bool _Dinse_positioning
       (if _Dinse_positioning (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_Start
       (if _EWM_Start (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_gas_test_1_shield
       (if _EWM_gas_test_1_shield (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_gas_test_2_plasma
       (if _EWM_gas_test_2_plasma (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_feed_wire
       (if _EWM_feed_wire (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_unfeed_wire
       (if _EWM_unfeed_wire (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_position_search
       (if _EWM_position_search (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_error_reset
       (if _EWM_error_reset (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_start_aux_process
       (if _EWM_start_aux_process (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_user_relay
       (if _EWM_user_relay (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_welding_simulation
       (if _EWM_welding_simulation (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_monitoring_function
       (if _EWM_monitoring_function (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_filler_wire_activated
       (if _EWM_filler_wire_activated (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_reserved_1
       (if _EWM_reserved_1 (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_weld_mode_select_bit_0
       (if _EWM_weld_mode_select_bit_0 (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_weld_mode_select_bit_1
       (if _EWM_weld_mode_select_bit_1 (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_wirefeeder_switch
       (if _EWM_wirefeeder_switch (write-byte -1 s) (write-byte 0 s))
     ;; bool _EWM_reserved_2
       (if _EWM_reserved_2 (write-byte -1 s) (write-byte 0 s))
     ;; float32 _EWM_cold_wire_feed_speed
       (sys::poke _EWM_cold_wire_feed_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _EWM_job_number
       (write-byte _EWM_job_number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _Dinse_wire_feed_speed
     (setq _Dinse_wire_feed_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _EWM_current
     (setq _EWM_current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _EWM_plasma_gas
     (setq _EWM_plasma_gas (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _EWM_shield_gas
     (setq _EWM_shield_gas (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _Dinse_start_release
     (setq _Dinse_start_release (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_acknowledge_fault
     (setq _Dinse_acknowledge_fault (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_start_wire_feed
     (setq _Dinse_start_wire_feed (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_start_power_source
     (setq _Dinse_start_power_source (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_wirebreak
     (setq _Dinse_wirebreak (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_wire_forward
     (setq _Dinse_wire_forward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_wire_backward
     (setq _Dinse_wire_backward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_gas_on
     (setq _Dinse_gas_on (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_retraction
     (setq _Dinse_retraction (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Dinse_positioning
     (setq _Dinse_positioning (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_Start
     (setq _EWM_Start (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_gas_test_1_shield
     (setq _EWM_gas_test_1_shield (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_gas_test_2_plasma
     (setq _EWM_gas_test_2_plasma (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_feed_wire
     (setq _EWM_feed_wire (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_unfeed_wire
     (setq _EWM_unfeed_wire (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_position_search
     (setq _EWM_position_search (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_error_reset
     (setq _EWM_error_reset (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_start_aux_process
     (setq _EWM_start_aux_process (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_user_relay
     (setq _EWM_user_relay (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_welding_simulation
     (setq _EWM_welding_simulation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_monitoring_function
     (setq _EWM_monitoring_function (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_filler_wire_activated
     (setq _EWM_filler_wire_activated (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_reserved_1
     (setq _EWM_reserved_1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_weld_mode_select_bit_0
     (setq _EWM_weld_mode_select_bit_0 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_weld_mode_select_bit_1
     (setq _EWM_weld_mode_select_bit_1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_wirefeeder_switch
     (setq _EWM_wirefeeder_switch (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _EWM_reserved_2
     (setq _EWM_reserved_2 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32 _EWM_cold_wire_feed_speed
     (setq _EWM_cold_wire_feed_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _EWM_job_number
     (setq _EWM_job_number (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get kuka_rsi_msgs::PlasmaCommand :md5sum-) "e908814e1fa1f45ddd9838e2ac41ab4e")
(setf (get kuka_rsi_msgs::PlasmaCommand :datatype-) "kuka_rsi_msgs/PlasmaCommand")
(setf (get kuka_rsi_msgs::PlasmaCommand :definition-)
      "Header header
# Field 3-4
float32 Dinse_wire_feed_speed
# Field 8-9
float32 EWM_current
# Field 12-13
float32 EWM_plasma_gas
# Field 14-15
float32 EWM_shield_gas
# Field 1
bool Dinse_start_release
bool Dinse_acknowledge_fault
bool Dinse_start_wire_feed
bool Dinse_start_power_source
bool Dinse_wirebreak
bool Dinse_wire_forward
bool Dinse_wire_backward
bool Dinse_gas_on
# Field 2
bool Dinse_retraction
bool Dinse_positioning
# Field 5
bool EWM_Start
# Field 6
bool EWM_gas_test_1_shield
bool EWM_gas_test_2_plasma
bool EWM_feed_wire
bool EWM_unfeed_wire
bool EWM_position_search
bool EWM_error_reset
bool EWM_start_aux_process
bool EWM_user_relay
# Field 7
bool EWM_welding_simulation
bool EWM_monitoring_function
bool EWM_filler_wire_activated
bool EWM_reserved_1
bool EWM_weld_mode_select_bit_0
bool EWM_weld_mode_select_bit_1
bool EWM_wirefeeder_switch
bool EWM_reserved_2
# Field 10-11
float32 EWM_cold_wire_feed_speed
# Field 16
uint8 EWM_job_number
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



(provide :kuka_rsi_msgs/PlasmaCommand "e908814e1fa1f45ddd9838e2ac41ab4e")


