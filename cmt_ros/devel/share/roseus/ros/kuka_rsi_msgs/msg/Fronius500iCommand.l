;; Auto-generated. Do not edit!


(when (boundp 'kuka_rsi_msgs::Fronius500iCommand)
  (if (not (find-package "KUKA_RSI_MSGS"))
    (make-package "KUKA_RSI_MSGS"))
  (shadow 'Fronius500iCommand (find-package "KUKA_RSI_MSGS")))
(unless (find-package "KUKA_RSI_MSGS::FRONIUS500ICOMMAND")
  (make-package "KUKA_RSI_MSGS::FRONIUS500ICOMMAND"))

(in-package "ROS")
;;//! \htmlinclude Fronius500iCommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass kuka_rsi_msgs::Fronius500iCommand
  :super ros::object
  :slots (_header _wire_feed_speed_command_value _arc_length_correction _dynamic_correction _wire_retract_correction _welding_start _working_modes _gas_test _wire_forward _wire_backward _error_quit _touch_sensing _torch_blow_out _process_line_selection _welding_simulation _synchro_pulse_on ))

(defmethod kuka_rsi_msgs::Fronius500iCommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:wire_feed_speed_command_value __wire_feed_speed_command_value) 0.0)
    ((:arc_length_correction __arc_length_correction) 0.0)
    ((:dynamic_correction __dynamic_correction) 0.0)
    ((:wire_retract_correction __wire_retract_correction) 0.0)
    ((:welding_start __welding_start) nil)
    ((:working_modes __working_modes) 0)
    ((:gas_test __gas_test) nil)
    ((:wire_forward __wire_forward) nil)
    ((:wire_backward __wire_backward) nil)
    ((:error_quit __error_quit) nil)
    ((:touch_sensing __touch_sensing) nil)
    ((:torch_blow_out __torch_blow_out) nil)
    ((:process_line_selection __process_line_selection) 0)
    ((:welding_simulation __welding_simulation) nil)
    ((:synchro_pulse_on __synchro_pulse_on) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _wire_feed_speed_command_value (float __wire_feed_speed_command_value))
   (setq _arc_length_correction (float __arc_length_correction))
   (setq _dynamic_correction (float __dynamic_correction))
   (setq _wire_retract_correction (float __wire_retract_correction))
   (setq _welding_start __welding_start)
   (setq _working_modes (round __working_modes))
   (setq _gas_test __gas_test)
   (setq _wire_forward __wire_forward)
   (setq _wire_backward __wire_backward)
   (setq _error_quit __error_quit)
   (setq _touch_sensing __touch_sensing)
   (setq _torch_blow_out __torch_blow_out)
   (setq _process_line_selection (round __process_line_selection))
   (setq _welding_simulation __welding_simulation)
   (setq _synchro_pulse_on __synchro_pulse_on)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:wire_feed_speed_command_value
   (&optional __wire_feed_speed_command_value)
   (if __wire_feed_speed_command_value (setq _wire_feed_speed_command_value __wire_feed_speed_command_value)) _wire_feed_speed_command_value)
  (:arc_length_correction
   (&optional __arc_length_correction)
   (if __arc_length_correction (setq _arc_length_correction __arc_length_correction)) _arc_length_correction)
  (:dynamic_correction
   (&optional __dynamic_correction)
   (if __dynamic_correction (setq _dynamic_correction __dynamic_correction)) _dynamic_correction)
  (:wire_retract_correction
   (&optional __wire_retract_correction)
   (if __wire_retract_correction (setq _wire_retract_correction __wire_retract_correction)) _wire_retract_correction)
  (:welding_start
   (&optional (__welding_start :null))
   (if (not (eq __welding_start :null)) (setq _welding_start __welding_start)) _welding_start)
  (:working_modes
   (&optional __working_modes)
   (if __working_modes (setq _working_modes __working_modes)) _working_modes)
  (:gas_test
   (&optional (__gas_test :null))
   (if (not (eq __gas_test :null)) (setq _gas_test __gas_test)) _gas_test)
  (:wire_forward
   (&optional (__wire_forward :null))
   (if (not (eq __wire_forward :null)) (setq _wire_forward __wire_forward)) _wire_forward)
  (:wire_backward
   (&optional (__wire_backward :null))
   (if (not (eq __wire_backward :null)) (setq _wire_backward __wire_backward)) _wire_backward)
  (:error_quit
   (&optional (__error_quit :null))
   (if (not (eq __error_quit :null)) (setq _error_quit __error_quit)) _error_quit)
  (:touch_sensing
   (&optional (__touch_sensing :null))
   (if (not (eq __touch_sensing :null)) (setq _touch_sensing __touch_sensing)) _touch_sensing)
  (:torch_blow_out
   (&optional (__torch_blow_out :null))
   (if (not (eq __torch_blow_out :null)) (setq _torch_blow_out __torch_blow_out)) _torch_blow_out)
  (:process_line_selection
   (&optional __process_line_selection)
   (if __process_line_selection (setq _process_line_selection __process_line_selection)) _process_line_selection)
  (:welding_simulation
   (&optional (__welding_simulation :null))
   (if (not (eq __welding_simulation :null)) (setq _welding_simulation __welding_simulation)) _welding_simulation)
  (:synchro_pulse_on
   (&optional (__synchro_pulse_on :null))
   (if (not (eq __synchro_pulse_on :null)) (setq _synchro_pulse_on __synchro_pulse_on)) _synchro_pulse_on)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _wire_feed_speed_command_value
    4
    ;; float32 _arc_length_correction
    4
    ;; float32 _dynamic_correction
    4
    ;; float32 _wire_retract_correction
    4
    ;; bool _welding_start
    1
    ;; uint8 _working_modes
    1
    ;; bool _gas_test
    1
    ;; bool _wire_forward
    1
    ;; bool _wire_backward
    1
    ;; bool _error_quit
    1
    ;; bool _touch_sensing
    1
    ;; bool _torch_blow_out
    1
    ;; uint8 _process_line_selection
    1
    ;; bool _welding_simulation
    1
    ;; bool _synchro_pulse_on
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _wire_feed_speed_command_value
       (sys::poke _wire_feed_speed_command_value (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _arc_length_correction
       (sys::poke _arc_length_correction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dynamic_correction
       (sys::poke _dynamic_correction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _wire_retract_correction
       (sys::poke _wire_retract_correction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _welding_start
       (if _welding_start (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _working_modes
       (write-byte _working_modes s)
     ;; bool _gas_test
       (if _gas_test (write-byte -1 s) (write-byte 0 s))
     ;; bool _wire_forward
       (if _wire_forward (write-byte -1 s) (write-byte 0 s))
     ;; bool _wire_backward
       (if _wire_backward (write-byte -1 s) (write-byte 0 s))
     ;; bool _error_quit
       (if _error_quit (write-byte -1 s) (write-byte 0 s))
     ;; bool _touch_sensing
       (if _touch_sensing (write-byte -1 s) (write-byte 0 s))
     ;; bool _torch_blow_out
       (if _torch_blow_out (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _process_line_selection
       (write-byte _process_line_selection s)
     ;; bool _welding_simulation
       (if _welding_simulation (write-byte -1 s) (write-byte 0 s))
     ;; bool _synchro_pulse_on
       (if _synchro_pulse_on (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _wire_feed_speed_command_value
     (setq _wire_feed_speed_command_value (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _arc_length_correction
     (setq _arc_length_correction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dynamic_correction
     (setq _dynamic_correction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _wire_retract_correction
     (setq _wire_retract_correction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _welding_start
     (setq _welding_start (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _working_modes
     (setq _working_modes (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _gas_test
     (setq _gas_test (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _wire_forward
     (setq _wire_forward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _wire_backward
     (setq _wire_backward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _error_quit
     (setq _error_quit (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _touch_sensing
     (setq _touch_sensing (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _torch_blow_out
     (setq _torch_blow_out (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _process_line_selection
     (setq _process_line_selection (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _welding_simulation
     (setq _welding_simulation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _synchro_pulse_on
     (setq _synchro_pulse_on (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get kuka_rsi_msgs::Fronius500iCommand :md5sum-) "a80028ec811c3f4ac2757241bd4475c6")
(setf (get kuka_rsi_msgs::Fronius500iCommand :datatype-) "kuka_rsi_msgs/Fronius500iCommand")
(setf (get kuka_rsi_msgs::Fronius500iCommand :definition-)
      "Header header
# Field[3]
float32 wire_feed_speed_command_value
# Field[4]
float32 arc_length_correction
# Field[5]
float32 dynamic_correction
# Field[6]
float32 wire_retract_correction
# Field[0]
bool welding_start
# Field[1]
uint8 working_modes # [0-4]
bool gas_test # [6]
bool wire_forward # [7]
# Field[2]
bool wire_backward
bool error_quit
bool touch_sensing
bool torch_blow_out
uint8 process_line_selection
bool welding_simulation
bool synchro_pulse_on

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



(provide :kuka_rsi_msgs/Fronius500iCommand "a80028ec811c3f4ac2757241bd4475c6")


