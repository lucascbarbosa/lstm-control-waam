;; Auto-generated. Do not edit!


(when (boundp 'hks_msgs::TpsState)
  (if (not (find-package "HKS_MSGS"))
    (make-package "HKS_MSGS"))
  (shadow 'TpsState (find-package "HKS_MSGS")))
(unless (find-package "HKS_MSGS::TPSSTATE")
  (make-package "HKS_MSGS::TPSSTATE"))

(in-package "ROS")
;;//! \htmlinclude TpsState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass hks_msgs::TpsState
  :super ros::object
  :slots (_header _IRdif _IRpos _IRmaxTemp _IRwidth _IRirreg _IRsymet ))

(defmethod hks_msgs::TpsState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:IRdif __IRdif) 0.0)
    ((:IRpos __IRpos) 0.0)
    ((:IRmaxTemp __IRmaxTemp) 0.0)
    ((:IRwidth __IRwidth) 0.0)
    ((:IRirreg __IRirreg) 0.0)
    ((:IRsymet __IRsymet) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _IRdif (float __IRdif))
   (setq _IRpos (float __IRpos))
   (setq _IRmaxTemp (float __IRmaxTemp))
   (setq _IRwidth (float __IRwidth))
   (setq _IRirreg (float __IRirreg))
   (setq _IRsymet (float __IRsymet))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:IRdif
   (&optional __IRdif)
   (if __IRdif (setq _IRdif __IRdif)) _IRdif)
  (:IRpos
   (&optional __IRpos)
   (if __IRpos (setq _IRpos __IRpos)) _IRpos)
  (:IRmaxTemp
   (&optional __IRmaxTemp)
   (if __IRmaxTemp (setq _IRmaxTemp __IRmaxTemp)) _IRmaxTemp)
  (:IRwidth
   (&optional __IRwidth)
   (if __IRwidth (setq _IRwidth __IRwidth)) _IRwidth)
  (:IRirreg
   (&optional __IRirreg)
   (if __IRirreg (setq _IRirreg __IRirreg)) _IRirreg)
  (:IRsymet
   (&optional __IRsymet)
   (if __IRsymet (setq _IRsymet __IRsymet)) _IRsymet)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _IRdif
    8
    ;; float64 _IRpos
    8
    ;; float64 _IRmaxTemp
    8
    ;; float64 _IRwidth
    8
    ;; float64 _IRirreg
    8
    ;; float64 _IRsymet
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _IRdif
       (sys::poke _IRdif (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _IRpos
       (sys::poke _IRpos (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _IRmaxTemp
       (sys::poke _IRmaxTemp (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _IRwidth
       (sys::poke _IRwidth (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _IRirreg
       (sys::poke _IRirreg (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _IRsymet
       (sys::poke _IRsymet (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _IRdif
     (setq _IRdif (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _IRpos
     (setq _IRpos (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _IRmaxTemp
     (setq _IRmaxTemp (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _IRwidth
     (setq _IRwidth (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _IRirreg
     (setq _IRirreg (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _IRsymet
     (setq _IRsymet (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get hks_msgs::TpsState :md5sum-) "1d051352653a4f46732676ac4e695c1f")
(setf (get hks_msgs::TpsState :datatype-) "hks_msgs/TpsState")
(setf (get hks_msgs::TpsState :definition-)
      "Header header
#
float64 IRdif
float64 IRpos
float64 IRmaxTemp
float64 IRwidth
float64 IRirreg
float64 IRsymet
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



(provide :hks_msgs/TpsState "1d051352653a4f46732676ac4e695c1f")


