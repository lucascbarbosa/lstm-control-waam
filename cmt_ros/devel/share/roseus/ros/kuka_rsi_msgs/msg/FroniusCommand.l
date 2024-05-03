;; Auto-generated. Do not edit!


(when (boundp 'kuka_rsi_msgs::FroniusCommand)
  (if (not (find-package "KUKA_RSI_MSGS"))
    (make-package "KUKA_RSI_MSGS"))
  (shadow 'FroniusCommand (find-package "KUKA_RSI_MSGS")))
(unless (find-package "KUKA_RSI_MSGS::FRONIUSCOMMAND")
  (make-package "KUKA_RSI_MSGS::FRONIUSCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude FroniusCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass kuka_rsi_msgs::FroniusCommand
  :super ros::object
  :slots (_header _power_set_value _arc_length_correction _dynamic_correction _burn_back _welding_start _working_modes _master_selection_twin _gas_test _wire_forward _job_number _program_number _welding_simulation _synchro_pulse_disable _SFI_disable _dynamic_correction_disable _burn_back_disable _full_power_range ))

(defmethod kuka_rsi_msgs::FroniusCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:power_set_value __power_set_value) 0.0)
    ((:arc_length_correction __arc_length_correction) 0.0)
    ((:dynamic_correction __dynamic_correction) 0.0)
    ((:burn_back __burn_back) 0.0)
    ((:welding_start __welding_start) nil)
    ((:working_modes __working_modes) 0)
    ((:master_selection_twin __master_selection_twin) nil)
    ((:gas_test __gas_test) nil)
    ((:wire_forward __wire_forward) nil)
    ((:job_number __job_number) 0)
    ((:program_number __program_number) 0)
    ((:welding_simulation __welding_simulation) nil)
    ((:synchro_pulse_disable __synchro_pulse_disable) nil)
    ((:SFI_disable __SFI_disable) nil)
    ((:dynamic_correction_disable __dynamic_correction_disable) nil)
    ((:burn_back_disable __burn_back_disable) nil)
    ((:full_power_range __full_power_range) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _power_set_value (float __power_set_value))
   (setq _arc_length_correction (float __arc_length_correction))
   (setq _dynamic_correction (float __dynamic_correction))
   (setq _burn_back (float __burn_back))
   (setq _welding_start __welding_start)
   (setq _working_modes (round __working_modes))
   (setq _master_selection_twin __master_selection_twin)
   (setq _gas_test __gas_test)
   (setq _wire_forward __wire_forward)
   (setq _job_number (round __job_number))
   (setq _program_number (round __program_number))
   (setq _welding_simulation __welding_simulation)
   (setq _synchro_pulse_disable __synchro_pulse_disable)
   (setq _SFI_disable __SFI_disable)
   (setq _dynamic_correction_disable __dynamic_correction_disable)
   (setq _burn_back_disable __burn_back_disable)
   (setq _full_power_range __full_power_range)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:power_set_value
   (&optional __power_set_value)
   (if __power_set_value (setq _power_set_value __power_set_value)) _power_set_value)
  (:arc_length_correction
   (&optional __arc_length_correction)
   (if __arc_length_correction (setq _arc_length_correction __arc_length_correction)) _arc_length_correction)
  (:dynamic_correction
   (&optional __dynamic_correction)
   (if __dynamic_correction (setq _dynamic_correction __dynamic_correction)) _dynamic_correction)
  (:burn_back
   (&optional __burn_back)
   (if __burn_back (setq _burn_back __burn_back)) _burn_back)
  (:welding_start
   (&optional (__welding_start :null))
   (if (not (eq __welding_start :null)) (setq _welding_start __welding_start)) _welding_start)
  (:working_modes
   (&optional __working_modes)
   (if __working_modes (setq _working_modes __working_modes)) _working_modes)
  (:master_selection_twin
   (&optional (__master_selection_twin :null))
   (if (not (eq __master_selection_twin :null)) (setq _master_selection_twin __master_selection_twin)) _master_selection_twin)
  (:gas_test
   (&optional (__gas_test :null))
   (if (not (eq __gas_test :null)) (setq _gas_test __gas_test)) _gas_test)
  (:wire_forward
   (&optional (__wire_forward :null))
   (if (not (eq __wire_forward :null)) (setq _wire_forward __wire_forward)) _wire_forward)
  (:job_number
   (&optional __job_number)
   (if __job_number (setq _job_number __job_number)) _job_number)
  (:program_number
   (&optional __program_number)
   (if __program_number (setq _program_number __program_number)) _program_number)
  (:welding_simulation
   (&optional (__welding_simulation :null))
   (if (not (eq __welding_simulation :null)) (setq _welding_simulation __welding_simulation)) _welding_simulation)
  (:synchro_pulse_disable
   (&optional (__synchro_pulse_disable :null))
   (if (not (eq __synchro_pulse_disable :null)) (setq _synchro_pulse_disable __synchro_pulse_disable)) _synchro_pulse_disable)
  (:SFI_disable
   (&optional (__SFI_disable :null))
   (if (not (eq __SFI_disable :null)) (setq _SFI_disable __SFI_disable)) _SFI_disable)
  (:dynamic_correction_disable
   (&optional (__dynamic_correction_disable :null))
   (if (not (eq __dynamic_correction_disable :null)) (setq _dynamic_correction_disable __dynamic_correction_disable)) _dynamic_correction_disable)
  (:burn_back_disable
   (&optional (__burn_back_disable :null))
   (if (not (eq __burn_back_disable :null)) (setq _burn_back_disable __burn_back_disable)) _burn_back_disable)
  (:full_power_range
   (&optional (__full_power_range :null))
   (if (not (eq __full_power_range :null)) (setq _full_power_range __full_power_range)) _full_power_range)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _power_set_value
    4
    ;; float32 _arc_length_correction
    4
    ;; float32 _dynamic_correction
    4
    ;; float32 _burn_back
    4
    ;; bool _welding_start
    1
    ;; uint8 _working_modes
    1
    ;; bool _master_selection_twin
    1
    ;; bool _gas_test
    1
    ;; bool _wire_forward
    1
    ;; uint8 _job_number
    1
    ;; uint8 _program_number
    1
    ;; bool _welding_simulation
    1
    ;; bool _synchro_pulse_disable
    1
    ;; bool _SFI_disable
    1
    ;; bool _dynamic_correction_disable
    1
    ;; bool _burn_back_disable
    1
    ;; bool _full_power_range
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _power_set_value
       (sys::poke _power_set_value (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _arc_length_correction
       (sys::poke _arc_length_correction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dynamic_correction
       (sys::poke _dynamic_correction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _burn_back
       (sys::poke _burn_back (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _welding_start
       (if _welding_start (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _working_modes
       (write-byte _working_modes s)
     ;; bool _master_selection_twin
       (if _master_selection_twin (write-byte -1 s) (write-byte 0 s))
     ;; bool _gas_test
       (if _gas_test (write-byte -1 s) (write-byte 0 s))
     ;; bool _wire_forward
       (if _wire_forward (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _job_number
       (write-byte _job_number s)
     ;; uint8 _program_number
       (write-byte _program_number s)
     ;; bool _welding_simulation
       (if _welding_simulation (write-byte -1 s) (write-byte 0 s))
     ;; bool _synchro_pulse_disable
       (if _synchro_pulse_disable (write-byte -1 s) (write-byte 0 s))
     ;; bool _SFI_disable
       (if _SFI_disable (write-byte -1 s) (write-byte 0 s))
     ;; bool _dynamic_correction_disable
       (if _dynamic_correction_disable (write-byte -1 s) (write-byte 0 s))
     ;; bool _burn_back_disable
       (if _burn_back_disable (write-byte -1 s) (write-byte 0 s))
     ;; bool _full_power_range
       (if _full_power_range (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _power_set_value
     (setq _power_set_value (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _arc_length_correction
     (setq _arc_length_correction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dynamic_correction
     (setq _dynamic_correction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _burn_back
     (setq _burn_back (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _welding_start
     (setq _welding_start (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _working_modes
     (setq _working_modes (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _master_selection_twin
     (setq _master_selection_twin (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _gas_test
     (setq _gas_test (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _wire_forward
     (setq _wire_forward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _job_number
     (setq _job_number (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _program_number
     (setq _program_number (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _welding_simulation
     (setq _welding_simulation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _synchro_pulse_disable
     (setq _synchro_pulse_disable (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _SFI_disable
     (setq _SFI_disable (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _dynamic_correction_disable
     (setq _dynamic_correction_disable (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _burn_back_disable
     (setq _burn_back_disable (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _full_power_range
     (setq _full_power_range (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get kuka_rsi_msgs::FroniusCommand :md5sum-) "3db99eb4c29a0d366f39cbc70352a89a")
(setf (get kuka_rsi_msgs::FroniusCommand :datatype-) "kuka_rsi_msgs/FroniusCommand")
(setf (get kuka_rsi_msgs::FroniusCommand :definition-)
      "Header header
# Field 5-6
float32 power_set_value
# Field 7-8
float32 arc_length_correction
# Field 9
float32 dynamic_correction
# Field 10
float32 burn_back
# Field 1
bool welding_start
# Field 2
uint8 working_modes
# bool working_modes_bit0
# bool working_modes_bit1
# bool working_modes_bit2
bool master_selection_twin
bool gas_test
bool wire_forward
# Field 3
uint8 job_number
# Field 4
uint8 program_number
bool welding_simulation
# Field 11
bool synchro_pulse_disable
bool SFI_disable
bool dynamic_correction_disable
bool burn_back_disable
bool full_power_range

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



(provide :kuka_rsi_msgs/FroniusCommand "3db99eb4c29a0d366f39cbc70352a89a")


