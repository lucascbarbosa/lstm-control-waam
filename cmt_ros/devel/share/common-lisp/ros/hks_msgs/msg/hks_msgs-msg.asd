
(cl:in-package :asdf)

(defsystem "hks_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "HksState" :depends-on ("_package_HksState"))
    (:file "_package_HksState" :depends-on ("_package"))
    (:file "TpsState" :depends-on ("_package_TpsState"))
    (:file "_package_TpsState" :depends-on ("_package"))
  ))