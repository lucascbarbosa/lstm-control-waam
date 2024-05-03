;; Auto-generated. Do not edit!


(when (boundp 'hks_msgs::HksState)
  (if (not (find-package "HKS_MSGS"))
    (make-package "HKS_MSGS"))
  (shadow 'HksState (find-package "HKS_MSGS")))
(unless (find-package "HKS_MSGS::HKSSTATE")
  (make-package "HKS_MSGS::HKSSTATE"))

(in-package "ROS")
;;//! \htmlinclude HksState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass hks_msgs::HksState
  :super ros::object
  :slots (_header _current _voltage _gasflow1 _gasflow2 _wfs1 _wfs2 _temperature1 _temperature2 ))

(defmethod hks_msgs::HksState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:current __current) 0.0)
    ((:voltage __voltage) 0.0)
    ((:gasflow1 __gasflow1) 0.0)
    ((:gasflow2 __gasflow2) 0.0)
    ((:wfs1 __wfs1) 0.0)
    ((:wfs2 __wfs2) 0.0)
    ((:temperature1 __temperature1) 0.0)
    ((:temperature2 __temperature2) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _current (float __current))
   (setq _voltage (float __voltage))
   (setq _gasflow1 (float __gasflow1))
   (setq _gasflow2 (float __gasflow2))
   (setq _wfs1 (float __wfs1))
   (setq _wfs2 (float __wfs2))
   (setq _temperature1 (float __temperature1))
   (setq _temperature2 (float __temperature2))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:current
   (&optional __current)
   (if __current (setq _current __current)) _current)
  (:voltage
   (&optional __voltage)
   (if __voltage (setq _voltage __voltage)) _voltage)
  (:gasflow1
   (&optional __gasflow1)
   (if __gasflow1 (setq _gasflow1 __gasflow1)) _gasflow1)
  (:gasflow2
   (&optional __gasflow2)
   (if __gasflow2 (setq _gasflow2 __gasflow2)) _gasflow2)
  (:wfs1
   (&optional __wfs1)
   (if __wfs1 (setq _wfs1 __wfs1)) _wfs1)
  (:wfs2
   (&optional __wfs2)
   (if __wfs2 (setq _wfs2 __wfs2)) _wfs2)
  (:temperature1
   (&optional __temperature1)
   (if __temperature1 (setq _temperature1 __temperature1)) _temperature1)
  (:temperature2
   (&optional __temperature2)
   (if __temperature2 (setq _temperature2 __temperature2)) _temperature2)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _current
    8
    ;; float64 _voltage
    8
    ;; float64 _gasflow1
    8
    ;; float64 _gasflow2
    8
    ;; float64 _wfs1
    8
    ;; float64 _wfs2
    8
    ;; float64 _temperature1
    8
    ;; float64 _temperature2
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _current
       (sys::poke _current (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _voltage
       (sys::poke _voltage (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gasflow1
       (sys::poke _gasflow1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gasflow2
       (sys::poke _gasflow2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _wfs1
       (sys::poke _wfs1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _wfs2
       (sys::poke _wfs2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _temperature1
       (sys::poke _temperature1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _temperature2
       (sys::poke _temperature2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _current
     (setq _current (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _voltage
     (setq _voltage (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gasflow1
     (setq _gasflow1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gasflow2
     (setq _gasflow2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _wfs1
     (setq _wfs1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _wfs2
     (setq _wfs2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _temperature1
     (setq _temperature1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _temperature2
     (setq _temperature2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get hks_msgs::HksState :md5sum-) "590c9f90019cd2bcb973006760e63ddd")
(setf (get hks_msgs::HksState :datatype-) "hks_msgs/HksState")
(setf (get hks_msgs::HksState :definition-)
      "Header header
#
float64 current
float64 voltage
#
float64 gasflow1
float64 gasflow2
#
float64 wfs1
float64 wfs2
#
float64 temperature1
float64 temperature2
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



(provide :hks_msgs/HksState "590c9f90019cd2bcb973006760e63ddd")


