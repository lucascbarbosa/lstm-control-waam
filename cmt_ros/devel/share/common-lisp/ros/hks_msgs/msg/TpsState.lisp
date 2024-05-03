; Auto-generated. Do not edit!


(cl:in-package hks_msgs-msg)


;//! \htmlinclude TpsState.msg.html

(cl:defclass <TpsState> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (IRdif
    :reader IRdif
    :initarg :IRdif
    :type cl:float
    :initform 0.0)
   (IRpos
    :reader IRpos
    :initarg :IRpos
    :type cl:float
    :initform 0.0)
   (IRmaxTemp
    :reader IRmaxTemp
    :initarg :IRmaxTemp
    :type cl:float
    :initform 0.0)
   (IRwidth
    :reader IRwidth
    :initarg :IRwidth
    :type cl:float
    :initform 0.0)
   (IRirreg
    :reader IRirreg
    :initarg :IRirreg
    :type cl:float
    :initform 0.0)
   (IRsymet
    :reader IRsymet
    :initarg :IRsymet
    :type cl:float
    :initform 0.0))
)

(cl:defclass TpsState (<TpsState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TpsState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TpsState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hks_msgs-msg:<TpsState> is deprecated: use hks_msgs-msg:TpsState instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <TpsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hks_msgs-msg:header-val is deprecated.  Use hks_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'IRdif-val :lambda-list '(m))
(cl:defmethod IRdif-val ((m <TpsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hks_msgs-msg:IRdif-val is deprecated.  Use hks_msgs-msg:IRdif instead.")
  (IRdif m))

(cl:ensure-generic-function 'IRpos-val :lambda-list '(m))
(cl:defmethod IRpos-val ((m <TpsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hks_msgs-msg:IRpos-val is deprecated.  Use hks_msgs-msg:IRpos instead.")
  (IRpos m))

(cl:ensure-generic-function 'IRmaxTemp-val :lambda-list '(m))
(cl:defmethod IRmaxTemp-val ((m <TpsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hks_msgs-msg:IRmaxTemp-val is deprecated.  Use hks_msgs-msg:IRmaxTemp instead.")
  (IRmaxTemp m))

(cl:ensure-generic-function 'IRwidth-val :lambda-list '(m))
(cl:defmethod IRwidth-val ((m <TpsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hks_msgs-msg:IRwidth-val is deprecated.  Use hks_msgs-msg:IRwidth instead.")
  (IRwidth m))

(cl:ensure-generic-function 'IRirreg-val :lambda-list '(m))
(cl:defmethod IRirreg-val ((m <TpsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hks_msgs-msg:IRirreg-val is deprecated.  Use hks_msgs-msg:IRirreg instead.")
  (IRirreg m))

(cl:ensure-generic-function 'IRsymet-val :lambda-list '(m))
(cl:defmethod IRsymet-val ((m <TpsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hks_msgs-msg:IRsymet-val is deprecated.  Use hks_msgs-msg:IRsymet instead.")
  (IRsymet m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TpsState>) ostream)
  "Serializes a message object of type '<TpsState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'IRdif))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'IRpos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'IRmaxTemp))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'IRwidth))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'IRirreg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'IRsymet))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TpsState>) istream)
  "Deserializes a message object of type '<TpsState>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'IRdif) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'IRpos) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'IRmaxTemp) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'IRwidth) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'IRirreg) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'IRsymet) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TpsState>)))
  "Returns string type for a message object of type '<TpsState>"
  "hks_msgs/TpsState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TpsState)))
  "Returns string type for a message object of type 'TpsState"
  "hks_msgs/TpsState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TpsState>)))
  "Returns md5sum for a message object of type '<TpsState>"
  "1d051352653a4f46732676ac4e695c1f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TpsState)))
  "Returns md5sum for a message object of type 'TpsState"
  "1d051352653a4f46732676ac4e695c1f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TpsState>)))
  "Returns full string definition for message of type '<TpsState>"
  (cl:format cl:nil "Header header~%#~%float64 IRdif~%float64 IRpos~%float64 IRmaxTemp~%float64 IRwidth~%float64 IRirreg~%float64 IRsymet~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TpsState)))
  "Returns full string definition for message of type 'TpsState"
  (cl:format cl:nil "Header header~%#~%float64 IRdif~%float64 IRpos~%float64 IRmaxTemp~%float64 IRwidth~%float64 IRirreg~%float64 IRsymet~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TpsState>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     8
     8
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TpsState>))
  "Converts a ROS message object to a list"
  (cl:list 'TpsState
    (cl:cons ':header (header msg))
    (cl:cons ':IRdif (IRdif msg))
    (cl:cons ':IRpos (IRpos msg))
    (cl:cons ':IRmaxTemp (IRmaxTemp msg))
    (cl:cons ':IRwidth (IRwidth msg))
    (cl:cons ':IRirreg (IRirreg msg))
    (cl:cons ':IRsymet (IRsymet msg))
))
