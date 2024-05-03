;; Auto-generated. Do not edit!


(when (boundp 'kuka_rsi_msgs::Fronius500iState)
  (if (not (find-package "KUKA_RSI_MSGS"))
    (make-package "KUKA_RSI_MSGS"))
  (shadow 'Fronius500iState (find-package "KUKA_RSI_MSGS")))
(unless (find-package "KUKA_RSI_MSGS::FRONIUS500ISTATE")
  (make-package "KUKA_RSI_MSGS::FRONIUS500ISTATE"))

(in-package "ROS")
;;//! \htmlinclude Fronius500iState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass kuka_rsi_msgs::Fronius500iState
  :super ros::object
  :slots (_header _welding_voltage _welding_current _wire_feed_speed _motor_current_M1 _motor_current_M2 _life_toggle_bit _power_source_ready _warning _process_active _current_flow _arc_stable _main_current_signal _touch_signal _collisionbox_active _robot_motion_release _wire_stick_workpiece _short_circuit_contact_tip _parameter_selection_internally _characteristic_number_valid _torch_body_gripped _command_value_out_of_range _correction_out_of_range _limitsignal _main_supply_status _process_id _process_str _touch_signal_gas_nozzle _twin_synchro_active ))

(defmethod kuka_rsi_msgs::Fronius500iState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:welding_voltage __welding_voltage) 0.0)
    ((:welding_current __welding_current) 0.0)
    ((:wire_feed_speed __wire_feed_speed) 0.0)
    ((:motor_current_M1 __motor_current_M1) 0.0)
    ((:motor_current_M2 __motor_current_M2) 0.0)
    ((:life_toggle_bit __life_toggle_bit) nil)
    ((:power_source_ready __power_source_ready) nil)
    ((:warning __warning) nil)
    ((:process_active __process_active) nil)
    ((:current_flow __current_flow) nil)
    ((:arc_stable __arc_stable) nil)
    ((:main_current_signal __main_current_signal) nil)
    ((:touch_signal __touch_signal) nil)
    ((:collisionbox_active __collisionbox_active) nil)
    ((:robot_motion_release __robot_motion_release) nil)
    ((:wire_stick_workpiece __wire_stick_workpiece) nil)
    ((:short_circuit_contact_tip __short_circuit_contact_tip) nil)
    ((:parameter_selection_internally __parameter_selection_internally) nil)
    ((:characteristic_number_valid __characteristic_number_valid) nil)
    ((:torch_body_gripped __torch_body_gripped) nil)
    ((:command_value_out_of_range __command_value_out_of_range) nil)
    ((:correction_out_of_range __correction_out_of_range) nil)
    ((:limitsignal __limitsignal) nil)
    ((:main_supply_status __main_supply_status) nil)
    ((:process_id __process_id) 0)
    ((:process_str __process_str) "")
    ((:touch_signal_gas_nozzle __touch_signal_gas_nozzle) nil)
    ((:twin_synchro_active __twin_synchro_active) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _welding_voltage (float __welding_voltage))
   (setq _welding_current (float __welding_current))
   (setq _wire_feed_speed (float __wire_feed_speed))
   (setq _motor_current_M1 (float __motor_current_M1))
   (setq _motor_current_M2 (float __motor_current_M2))
   (setq _life_toggle_bit __life_toggle_bit)
   (setq _power_source_ready __power_source_ready)
   (setq _warning __warning)
   (setq _process_active __process_active)
   (setq _current_flow __current_flow)
   (setq _arc_stable __arc_stable)
   (setq _main_current_signal __main_current_signal)
   (setq _touch_signal __touch_signal)
   (setq _collisionbox_active __collisionbox_active)
   (setq _robot_motion_release __robot_motion_release)
   (setq _wire_stick_workpiece __wire_stick_workpiece)
   (setq _short_circuit_contact_tip __short_circuit_contact_tip)
   (setq _parameter_selection_internally __parameter_selection_internally)
   (setq _characteristic_number_valid __characteristic_number_valid)
   (setq _torch_body_gripped __torch_body_gripped)
   (setq _command_value_out_of_range __command_value_out_of_range)
   (setq _correction_out_of_range __correction_out_of_range)
   (setq _limitsignal __limitsignal)
   (setq _main_supply_status __main_supply_status)
   (setq _process_id (round __process_id))
   (setq _process_str (string __process_str))
   (setq _touch_signal_gas_nozzle __touch_signal_gas_nozzle)
   (setq _twin_synchro_active __twin_synchro_active)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:welding_voltage
   (&optional __welding_voltage)
   (if __welding_voltage (setq _welding_voltage __welding_voltage)) _welding_voltage)
  (:welding_current
   (&optional __welding_current)
   (if __welding_current (setq _welding_current __welding_current)) _welding_current)
  (:wire_feed_speed
   (&optional __wire_feed_speed)
   (if __wire_feed_speed (setq _wire_feed_speed __wire_feed_speed)) _wire_feed_speed)
  (:motor_current_M1
   (&optional __motor_current_M1)
   (if __motor_current_M1 (setq _motor_current_M1 __motor_current_M1)) _motor_current_M1)
  (:motor_current_M2
   (&optional __motor_current_M2)
   (if __motor_current_M2 (setq _motor_current_M2 __motor_current_M2)) _motor_current_M2)
  (:life_toggle_bit
   (&optional (__life_toggle_bit :null))
   (if (not (eq __life_toggle_bit :null)) (setq _life_toggle_bit __life_toggle_bit)) _life_toggle_bit)
  (:power_source_ready
   (&optional (__power_source_ready :null))
   (if (not (eq __power_source_ready :null)) (setq _power_source_ready __power_source_ready)) _power_source_ready)
  (:warning
   (&optional (__warning :null))
   (if (not (eq __warning :null)) (setq _warning __warning)) _warning)
  (:process_active
   (&optional (__process_active :null))
   (if (not (eq __process_active :null)) (setq _process_active __process_active)) _process_active)
  (:current_flow
   (&optional (__current_flow :null))
   (if (not (eq __current_flow :null)) (setq _current_flow __current_flow)) _current_flow)
  (:arc_stable
   (&optional (__arc_stable :null))
   (if (not (eq __arc_stable :null)) (setq _arc_stable __arc_stable)) _arc_stable)
  (:main_current_signal
   (&optional (__main_current_signal :null))
   (if (not (eq __main_current_signal :null)) (setq _main_current_signal __main_current_signal)) _main_current_signal)
  (:touch_signal
   (&optional (__touch_signal :null))
   (if (not (eq __touch_signal :null)) (setq _touch_signal __touch_signal)) _touch_signal)
  (:collisionbox_active
   (&optional (__collisionbox_active :null))
   (if (not (eq __collisionbox_active :null)) (setq _collisionbox_active __collisionbox_active)) _collisionbox_active)
  (:robot_motion_release
   (&optional (__robot_motion_release :null))
   (if (not (eq __robot_motion_release :null)) (setq _robot_motion_release __robot_motion_release)) _robot_motion_release)
  (:wire_stick_workpiece
   (&optional (__wire_stick_workpiece :null))
   (if (not (eq __wire_stick_workpiece :null)) (setq _wire_stick_workpiece __wire_stick_workpiece)) _wire_stick_workpiece)
  (:short_circuit_contact_tip
   (&optional (__short_circuit_contact_tip :null))
   (if (not (eq __short_circuit_contact_tip :null)) (setq _short_circuit_contact_tip __short_circuit_contact_tip)) _short_circuit_contact_tip)
  (:parameter_selection_internally
   (&optional (__parameter_selection_internally :null))
   (if (not (eq __parameter_selection_internally :null)) (setq _parameter_selection_internally __parameter_selection_internally)) _parameter_selection_internally)
  (:characteristic_number_valid
   (&optional (__characteristic_number_valid :null))
   (if (not (eq __characteristic_number_valid :null)) (setq _characteristic_number_valid __characteristic_number_valid)) _characteristic_number_valid)
  (:torch_body_gripped
   (&optional (__torch_body_gripped :null))
   (if (not (eq __torch_body_gripped :null)) (setq _torch_body_gripped __torch_body_gripped)) _torch_body_gripped)
  (:command_value_out_of_range
   (&optional (__command_value_out_of_range :null))
   (if (not (eq __command_value_out_of_range :null)) (setq _command_value_out_of_range __command_value_out_of_range)) _command_value_out_of_range)
  (:correction_out_of_range
   (&optional (__correction_out_of_range :null))
   (if (not (eq __correction_out_of_range :null)) (setq _correction_out_of_range __correction_out_of_range)) _correction_out_of_range)
  (:limitsignal
   (&optional (__limitsignal :null))
   (if (not (eq __limitsignal :null)) (setq _limitsignal __limitsignal)) _limitsignal)
  (:main_supply_status
   (&optional (__main_supply_status :null))
   (if (not (eq __main_supply_status :null)) (setq _main_supply_status __main_supply_status)) _main_supply_status)
  (:process_id
   (&optional __process_id)
   (if __process_id (setq _process_id __process_id)) _process_id)
  (:process_str
   (&optional __process_str)
   (if __process_str (setq _process_str __process_str)) _process_str)
  (:touch_signal_gas_nozzle
   (&optional (__touch_signal_gas_nozzle :null))
   (if (not (eq __touch_signal_gas_nozzle :null)) (setq _touch_signal_gas_nozzle __touch_signal_gas_nozzle)) _touch_signal_gas_nozzle)
  (:twin_synchro_active
   (&optional (__twin_synchro_active :null))
   (if (not (eq __twin_synchro_active :null)) (setq _twin_synchro_active __twin_synchro_active)) _twin_synchro_active)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _welding_voltage
    4
    ;; float32 _welding_current
    4
    ;; float32 _wire_feed_speed
    4
    ;; float32 _motor_current_M1
    4
    ;; float32 _motor_current_M2
    4
    ;; bool _life_toggle_bit
    1
    ;; bool _power_source_ready
    1
    ;; bool _warning
    1
    ;; bool _process_active
    1
    ;; bool _current_flow
    1
    ;; bool _arc_stable
    1
    ;; bool _main_current_signal
    1
    ;; bool _touch_signal
    1
    ;; bool _collisionbox_active
    1
    ;; bool _robot_motion_release
    1
    ;; bool _wire_stick_workpiece
    1
    ;; bool _short_circuit_contact_tip
    1
    ;; bool _parameter_selection_internally
    1
    ;; bool _characteristic_number_valid
    1
    ;; bool _torch_body_gripped
    1
    ;; bool _command_value_out_of_range
    1
    ;; bool _correction_out_of_range
    1
    ;; bool _limitsignal
    1
    ;; bool _main_supply_status
    1
    ;; uint8 _process_id
    1
    ;; string _process_str
    4 (length _process_str)
    ;; bool _touch_signal_gas_nozzle
    1
    ;; bool _twin_synchro_active
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _welding_voltage
       (sys::poke _welding_voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _welding_current
       (sys::poke _welding_current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _wire_feed_speed
       (sys::poke _wire_feed_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_current_M1
       (sys::poke _motor_current_M1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_current_M2
       (sys::poke _motor_current_M2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _life_toggle_bit
       (if _life_toggle_bit (write-byte -1 s) (write-byte 0 s))
     ;; bool _power_source_ready
       (if _power_source_ready (write-byte -1 s) (write-byte 0 s))
     ;; bool _warning
       (if _warning (write-byte -1 s) (write-byte 0 s))
     ;; bool _process_active
       (if _process_active (write-byte -1 s) (write-byte 0 s))
     ;; bool _current_flow
       (if _current_flow (write-byte -1 s) (write-byte 0 s))
     ;; bool _arc_stable
       (if _arc_stable (write-byte -1 s) (write-byte 0 s))
     ;; bool _main_current_signal
       (if _main_current_signal (write-byte -1 s) (write-byte 0 s))
     ;; bool _touch_signal
       (if _touch_signal (write-byte -1 s) (write-byte 0 s))
     ;; bool _collisionbox_active
       (if _collisionbox_active (write-byte -1 s) (write-byte 0 s))
     ;; bool _robot_motion_release
       (if _robot_motion_release (write-byte -1 s) (write-byte 0 s))
     ;; bool _wire_stick_workpiece
       (if _wire_stick_workpiece (write-byte -1 s) (write-byte 0 s))
     ;; bool _short_circuit_contact_tip
       (if _short_circuit_contact_tip (write-byte -1 s) (write-byte 0 s))
     ;; bool _parameter_selection_internally
       (if _parameter_selection_internally (write-byte -1 s) (write-byte 0 s))
     ;; bool _characteristic_number_valid
       (if _characteristic_number_valid (write-byte -1 s) (write-byte 0 s))
     ;; bool _torch_body_gripped
       (if _torch_body_gripped (write-byte -1 s) (write-byte 0 s))
     ;; bool _command_value_out_of_range
       (if _command_value_out_of_range (write-byte -1 s) (write-byte 0 s))
     ;; bool _correction_out_of_range
       (if _correction_out_of_range (write-byte -1 s) (write-byte 0 s))
     ;; bool _limitsignal
       (if _limitsignal (write-byte -1 s) (write-byte 0 s))
     ;; bool _main_supply_status
       (if _main_supply_status (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _process_id
       (write-byte _process_id s)
     ;; string _process_str
       (write-long (length _process_str) s) (princ _process_str s)
     ;; bool _touch_signal_gas_nozzle
       (if _touch_signal_gas_nozzle (write-byte -1 s) (write-byte 0 s))
     ;; bool _twin_synchro_active
       (if _twin_synchro_active (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _welding_voltage
     (setq _welding_voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _welding_current
     (setq _welding_current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _wire_feed_speed
     (setq _wire_feed_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_current_M1
     (setq _motor_current_M1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_current_M2
     (setq _motor_current_M2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _life_toggle_bit
     (setq _life_toggle_bit (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _power_source_ready
     (setq _power_source_ready (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _warning
     (setq _warning (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _process_active
     (setq _process_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _current_flow
     (setq _current_flow (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _arc_stable
     (setq _arc_stable (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _main_current_signal
     (setq _main_current_signal (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _touch_signal
     (setq _touch_signal (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _collisionbox_active
     (setq _collisionbox_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _robot_motion_release
     (setq _robot_motion_release (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _wire_stick_workpiece
     (setq _wire_stick_workpiece (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _short_circuit_contact_tip
     (setq _short_circuit_contact_tip (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _parameter_selection_internally
     (setq _parameter_selection_internally (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _characteristic_number_valid
     (setq _characteristic_number_valid (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _torch_body_gripped
     (setq _torch_body_gripped (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _command_value_out_of_range
     (setq _command_value_out_of_range (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _correction_out_of_range
     (setq _correction_out_of_range (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _limitsignal
     (setq _limitsignal (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _main_supply_status
     (setq _main_supply_status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _process_id
     (setq _process_id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; string _process_str
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _process_str (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _touch_signal_gas_nozzle
     (setq _touch_signal_gas_nozzle (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _twin_synchro_active
     (setq _twin_synchro_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get kuka_rsi_msgs::Fronius500iState :md5sum-) "4355219bc4b3af559fd32d94b33e5f02")
(setf (get kuka_rsi_msgs::Fronius500iState :datatype-) "kuka_rsi_msgs/Fronius500iState")
(setf (get kuka_rsi_msgs::Fronius500iState :definition-)
      "Header header
# Input[4]
float32 welding_voltage
# Input[5]
float32 welding_current
# Input[6]
float32 wire_feed_speed
# Input[7]
float32 motor_current_M1
# Input[8]
float32 motor_current_M2
# Input[0]
bool life_toggle_bit # 0
bool power_source_ready # 1
bool warning # 2
bool process_active # 3
bool current_flow # 4
bool arc_stable # 5
bool main_current_signal # 6
bool touch_signal # 7
# Input[1]
bool collisionbox_active # 0
bool robot_motion_release # 1
bool wire_stick_workpiece # 2
bool short_circuit_contact_tip # 4
bool parameter_selection_internally # 5
bool characteristic_number_valid # 6
bool torch_body_gripped # 7
# Input[2]
bool command_value_out_of_range # 0
bool correction_out_of_range # 1
bool limitsignal # 3
bool main_supply_status # 6
# Input[3]
uint8 process_id # 0-4
string process_str # none
bool touch_signal_gas_nozzle # 6
bool twin_synchro_active # 7

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



(provide :kuka_rsi_msgs/Fronius500iState "4355219bc4b3af559fd32d94b33e5f02")


