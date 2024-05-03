
(cl:in-package :asdf)

(defsystem "kuka_rsi_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Fronius500iCommand" :depends-on ("_package_Fronius500iCommand"))
    (:file "_package_Fronius500iCommand" :depends-on ("_package"))
    (:file "Fronius500iState" :depends-on ("_package_Fronius500iState"))
    (:file "_package_Fronius500iState" :depends-on ("_package"))
    (:file "FroniusCommand" :depends-on ("_package_FroniusCommand"))
    (:file "_package_FroniusCommand" :depends-on ("_package"))
    (:file "FroniusState" :depends-on ("_package_FroniusState"))
    (:file "_package_FroniusState" :depends-on ("_package"))
    (:file "PlasmaCommand" :depends-on ("_package_PlasmaCommand"))
    (:file "_package_PlasmaCommand" :depends-on ("_package"))
    (:file "PlasmaState" :depends-on ("_package_PlasmaState"))
    (:file "_package_PlasmaState" :depends-on ("_package"))
  ))