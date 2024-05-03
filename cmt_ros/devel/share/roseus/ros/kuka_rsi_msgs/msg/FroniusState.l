;; Auto-generated. Do not edit!


(when (boundp 'kuka_rsi_msgs::FroniusState)
  (if (not (find-package "KUKA_RSI_MSGS"))
    (make-package "KUKA_RSI_MSGS"))
  (shadow 'FroniusState (find-package "KUKA_RSI_MSGS")))
(unless (find-package "KUKA_RSI_MSGS::FRONIUSSTATE")
  (make-package "KUKA_RSI_MSGS::FRONIUSSTATE"))

(in-package "ROS")
;;//! \htmlinclude FroniusState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass kuka_rsi_msgs::FroniusState
  :super ros::object
  :slots (_header _arc_voltage _arc_current _motor_current _wire_feed_speed _arc_stable _limit_signal _process_active _main_current_signal _torch_collision_protection _power_source_ready _communication_ready _life_toggle_bit _error_number _wire_stick_control _robot_access _wire_available _timeout_short_circuit _data_documentation_ready _power_outside_range ))

(defmethod kuka_rsi_msgs::FroniusState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:arc_voltage __arc_voltage) 0.0)
    ((:arc_current __arc_current) 0.0)
    ((:motor_current __motor_current) 0.0)
    ((:wire_feed_speed __wire_feed_speed) 0.0)
    ((:arc_stable __arc_stable) nil)
    ((:limit_signal __limit_signal) nil)
    ((:process_active __process_active) nil)
    ((:main_current_signal __main_current_signal) nil)
    ((:torch_collision_protection __torch_collision_protection) nil)
    ((:power_source_ready __power_source_ready) nil)
    ((:communication_ready __communication_ready) nil)
    ((:life_toggle_bit __life_toggle_bit) nil)
    ((:error_number __error_number) 0)
    ((:wire_stick_control __wire_stick_control) nil)
    ((:robot_access __robot_access) nil)
    ((:wire_available __wire_available) nil)
    ((:timeout_short_circuit __timeout_short_circuit) nil)
    ((:data_documentation_ready __data_documentation_ready) nil)
    ((:power_outside_range __power_outside_range) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _arc_voltage (float __arc_voltage))
   (setq _arc_current (float __arc_current))
   (setq _motor_current (float __motor_current))
   (setq _wire_feed_speed (float __wire_feed_speed))
   (setq _arc_stable __arc_stable)
   (setq _limit_signal __limit_signal)
   (setq _process_active __process_active)
   (setq _main_current_signal __main_current_signal)
   (setq _torch_collision_protection __torch_collision_protection)
   (setq _power_source_ready __power_source_ready)
   (setq _communication_ready __communication_ready)
   (setq _life_toggle_bit __life_toggle_bit)
   (setq _error_number (round __error_number))
   (setq _wire_stick_control __wire_stick_control)
   (setq _robot_access __robot_access)
   (setq _wire_available __wire_available)
   (setq _timeout_short_circuit __timeout_short_circuit)
   (setq _data_documentation_ready __data_documentation_ready)
   (setq _power_outside_range __power_outside_range)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:arc_voltage
   (&optional __arc_voltage)
   (if __arc_voltage (setq _arc_voltage __arc_voltage)) _arc_voltage)
  (:arc_current
   (&optional __arc_current)
   (if __arc_current (setq _arc_current __arc_current)) _arc_current)
  (:motor_current
   (&optional __motor_current)
   (if __motor_current (setq _motor_current __motor_current)) _motor_current)
  (:wire_feed_speed
   (&optional __wire_feed_speed)
   (if __wire_feed_speed (setq _wire_feed_speed __wire_feed_speed)) _wire_feed_speed)
  (:arc_stable
   (&optional (__arc_stable :null))
   (if (not (eq __arc_stable :null)) (setq _arc_stable __arc_stable)) _arc_stable)
  (:limit_signal
   (&optional (__limit_signal :null))
   (if (not (eq __limit_signal :null)) (setq _limit_signal __limit_signal)) _limit_signal)
  (:process_active
   (&optional (__process_active :null))
   (if (not (eq __process_active :null)) (setq _process_active __process_active)) _process_active)
  (:main_current_signal
   (&optional (__main_current_signal :null))
   (if (not (eq __main_current_signal :null)) (setq _main_current_signal __main_current_signal)) _main_current_signal)
  (:torch_collision_protection
   (&optional (__torch_collision_protection :null))
   (if (not (eq __torch_collision_protection :null)) (setq _torch_collision_protection __torch_collision_protection)) _torch_collision_protection)
  (:power_source_ready
   (&optional (__power_source_ready :null))
   (if (not (eq __power_source_ready :null)) (setq _power_source_ready __power_source_ready)) _power_source_ready)
  (:communication_ready
   (&optional (__communication_ready :null))
   (if (not (eq __communication_ready :null)) (setq _communication_ready __communication_ready)) _communication_ready)
  (:life_toggle_bit
   (&optional (__life_toggle_bit :null))
   (if (not (eq __life_toggle_bit :null)) (setq _life_toggle_bit __life_toggle_bit)) _life_toggle_bit)
  (:error_number
   (&optional __error_number)
   (if __error_number (setq _error_number __error_number)) _error_number)
  (:wire_stick_control
   (&optional (__wire_stick_control :null))
   (if (not (eq __wire_stick_control :null)) (setq _wire_stick_control __wire_stick_control)) _wire_stick_control)
  (:robot_access
   (&optional (__robot_access :null))
   (if (not (eq __robot_access :null)) (setq _robot_access __robot_access)) _robot_access)
  (:wire_available
   (&optional (__wire_available :null))
   (if (not (eq __wire_available :null)) (setq _wire_available __wire_available)) _wire_available)
  (:timeout_short_circuit
   (&optional (__timeout_short_circuit :null))
   (if (not (eq __timeout_short_circuit :null)) (setq _timeout_short_circuit __timeout_short_circuit)) _timeout_short_circuit)
  (:data_documentation_ready
   (&optional (__data_documentation_ready :null))
   (if (not (eq __data_documentation_ready :null)) (setq _data_documentation_ready __data_documentation_ready)) _data_documentation_ready)
  (:power_outside_range
   (&optional (__power_outside_range :null))
   (if (not (eq __power_outside_range :null)) (setq _power_outside_range __power_outside_range)) _power_outside_range)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _arc_voltage
    4
    ;; float32 _arc_current
    4
    ;; float32 _motor_current
    4
    ;; float32 _wire_feed_speed
    4
    ;; bool _arc_stable
    1
    ;; bool _limit_signal
    1
    ;; bool _process_active
    1
    ;; bool _main_current_signal
    1
    ;; bool _torch_collision_protection
    1
    ;; bool _power_source_ready
    1
    ;; bool _communication_ready
    1
    ;; bool _life_toggle_bit
    1
    ;; uint8 _error_number
    1
    ;; bool _wire_stick_control
    1
    ;; bool _robot_access
    1
    ;; bool _wire_available
    1
    ;; bool _timeout_short_circuit
    1
    ;; bool _data_documentation_ready
    1
    ;; bool _power_outside_range
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _arc_voltage
       (sys::poke _arc_voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _arc_current
       (sys::poke _arc_current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_current
       (sys::poke _motor_current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _wire_feed_speed
       (sys::poke _wire_feed_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _arc_stable
       (if _arc_stable (write-byte -1 s) (write-byte 0 s))
     ;; bool _limit_signal
       (if _limit_signal (write-byte -1 s) (write-byte 0 s))
     ;; bool _process_active
       (if _process_active (write-byte -1 s) (write-byte 0 s))
     ;; bool _main_current_signal
       (if _main_current_signal (write-byte -1 s) (write-byte 0 s))
     ;; bool _torch_collision_protection
       (if _torch_collision_protection (write-byte -1 s) (write-byte 0 s))
     ;; bool _power_source_ready
       (if _power_source_ready (write-byte -1 s) (write-byte 0 s))
     ;; bool _communication_ready
       (if _communication_ready (write-byte -1 s) (write-byte 0 s))
     ;; bool _life_toggle_bit
       (if _life_toggle_bit (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _error_number
       (write-byte _error_number s)
     ;; bool _wire_stick_control
       (if _wire_stick_control (write-byte -1 s) (write-byte 0 s))
     ;; bool _robot_access
       (if _robot_access (write-byte -1 s) (write-byte 0 s))
     ;; bool _wire_available
       (if _wire_available (write-byte -1 s) (write-byte 0 s))
     ;; bool _timeout_short_circuit
       (if _timeout_short_circuit (write-byte -1 s) (write-byte 0 s))
     ;; bool _data_documentation_ready
       (if _data_documentation_ready (write-byte -1 s) (write-byte 0 s))
     ;; bool _power_outside_range
       (if _power_outside_range (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _arc_voltage
     (setq _arc_voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _arc_current
     (setq _arc_current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_current
     (setq _motor_current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _wire_feed_speed
     (setq _wire_feed_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _arc_stable
     (setq _arc_stable (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _limit_signal
     (setq _limit_signal (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _process_active
     (setq _process_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _main_current_signal
     (setq _main_current_signal (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _torch_collision_protection
     (setq _torch_collision_protection (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _power_source_ready
     (setq _power_source_ready (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _communication_ready
     (setq _communication_ready (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _life_toggle_bit
     (setq _life_toggle_bit (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _error_number
     (setq _error_number (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _wire_stick_control
     (setq _wire_stick_control (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _robot_access
     (setq _robot_access (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _wire_available
     (setq _wire_available (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _timeout_short_circuit
     (setq _timeout_short_circuit (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _data_documentation_ready
     (setq _data_documentation_ready (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _power_outside_range
     (setq _power_outside_range (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get kuka_rsi_msgs::FroniusState :md5sum-) "30bd5f2b575dd738b94a41edaf98cf7f")
(setf (get kuka_rsi_msgs::FroniusState :datatype-) "kuka_rsi_msgs/FroniusState")
(setf (get kuka_rsi_msgs::FroniusState :definition-)
      "Header header
# Field 4-5
float32 arc_voltage
# Field 6-7
float32 arc_current
# Field 8
float32 motor_current
# Field 9-10
float32 wire_feed_speed
# Field 1
bool arc_stable
bool limit_signal
bool process_active
bool main_current_signal
bool torch_collision_protection
bool power_source_ready
bool communication_ready
bool life_toggle_bit
# Field 2
uint8 error_number
# Field 3
bool wire_stick_control
bool robot_access
bool wire_available
bool timeout_short_circuit
bool data_documentation_ready
bool power_outside_range
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



(provide :kuka_rsi_msgs/FroniusState "30bd5f2b575dd738b94a41edaf98cf7f")


