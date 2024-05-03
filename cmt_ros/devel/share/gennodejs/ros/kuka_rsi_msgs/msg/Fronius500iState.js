// Auto-generated. Do not edit!

// (in-package kuka_rsi_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Fronius500iState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.welding_voltage = null;
      this.welding_current = null;
      this.wire_feed_speed = null;
      this.motor_current_M1 = null;
      this.motor_current_M2 = null;
      this.life_toggle_bit = null;
      this.power_source_ready = null;
      this.warning = null;
      this.process_active = null;
      this.current_flow = null;
      this.arc_stable = null;
      this.main_current_signal = null;
      this.touch_signal = null;
      this.collisionbox_active = null;
      this.robot_motion_release = null;
      this.wire_stick_workpiece = null;
      this.short_circuit_contact_tip = null;
      this.parameter_selection_internally = null;
      this.characteristic_number_valid = null;
      this.torch_body_gripped = null;
      this.command_value_out_of_range = null;
      this.correction_out_of_range = null;
      this.limitsignal = null;
      this.main_supply_status = null;
      this.process_id = null;
      this.process_str = null;
      this.touch_signal_gas_nozzle = null;
      this.twin_synchro_active = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('welding_voltage')) {
        this.welding_voltage = initObj.welding_voltage
      }
      else {
        this.welding_voltage = 0.0;
      }
      if (initObj.hasOwnProperty('welding_current')) {
        this.welding_current = initObj.welding_current
      }
      else {
        this.welding_current = 0.0;
      }
      if (initObj.hasOwnProperty('wire_feed_speed')) {
        this.wire_feed_speed = initObj.wire_feed_speed
      }
      else {
        this.wire_feed_speed = 0.0;
      }
      if (initObj.hasOwnProperty('motor_current_M1')) {
        this.motor_current_M1 = initObj.motor_current_M1
      }
      else {
        this.motor_current_M1 = 0.0;
      }
      if (initObj.hasOwnProperty('motor_current_M2')) {
        this.motor_current_M2 = initObj.motor_current_M2
      }
      else {
        this.motor_current_M2 = 0.0;
      }
      if (initObj.hasOwnProperty('life_toggle_bit')) {
        this.life_toggle_bit = initObj.life_toggle_bit
      }
      else {
        this.life_toggle_bit = false;
      }
      if (initObj.hasOwnProperty('power_source_ready')) {
        this.power_source_ready = initObj.power_source_ready
      }
      else {
        this.power_source_ready = false;
      }
      if (initObj.hasOwnProperty('warning')) {
        this.warning = initObj.warning
      }
      else {
        this.warning = false;
      }
      if (initObj.hasOwnProperty('process_active')) {
        this.process_active = initObj.process_active
      }
      else {
        this.process_active = false;
      }
      if (initObj.hasOwnProperty('current_flow')) {
        this.current_flow = initObj.current_flow
      }
      else {
        this.current_flow = false;
      }
      if (initObj.hasOwnProperty('arc_stable')) {
        this.arc_stable = initObj.arc_stable
      }
      else {
        this.arc_stable = false;
      }
      if (initObj.hasOwnProperty('main_current_signal')) {
        this.main_current_signal = initObj.main_current_signal
      }
      else {
        this.main_current_signal = false;
      }
      if (initObj.hasOwnProperty('touch_signal')) {
        this.touch_signal = initObj.touch_signal
      }
      else {
        this.touch_signal = false;
      }
      if (initObj.hasOwnProperty('collisionbox_active')) {
        this.collisionbox_active = initObj.collisionbox_active
      }
      else {
        this.collisionbox_active = false;
      }
      if (initObj.hasOwnProperty('robot_motion_release')) {
        this.robot_motion_release = initObj.robot_motion_release
      }
      else {
        this.robot_motion_release = false;
      }
      if (initObj.hasOwnProperty('wire_stick_workpiece')) {
        this.wire_stick_workpiece = initObj.wire_stick_workpiece
      }
      else {
        this.wire_stick_workpiece = false;
      }
      if (initObj.hasOwnProperty('short_circuit_contact_tip')) {
        this.short_circuit_contact_tip = initObj.short_circuit_contact_tip
      }
      else {
        this.short_circuit_contact_tip = false;
      }
      if (initObj.hasOwnProperty('parameter_selection_internally')) {
        this.parameter_selection_internally = initObj.parameter_selection_internally
      }
      else {
        this.parameter_selection_internally = false;
      }
      if (initObj.hasOwnProperty('characteristic_number_valid')) {
        this.characteristic_number_valid = initObj.characteristic_number_valid
      }
      else {
        this.characteristic_number_valid = false;
      }
      if (initObj.hasOwnProperty('torch_body_gripped')) {
        this.torch_body_gripped = initObj.torch_body_gripped
      }
      else {
        this.torch_body_gripped = false;
      }
      if (initObj.hasOwnProperty('command_value_out_of_range')) {
        this.command_value_out_of_range = initObj.command_value_out_of_range
      }
      else {
        this.command_value_out_of_range = false;
      }
      if (initObj.hasOwnProperty('correction_out_of_range')) {
        this.correction_out_of_range = initObj.correction_out_of_range
      }
      else {
        this.correction_out_of_range = false;
      }
      if (initObj.hasOwnProperty('limitsignal')) {
        this.limitsignal = initObj.limitsignal
      }
      else {
        this.limitsignal = false;
      }
      if (initObj.hasOwnProperty('main_supply_status')) {
        this.main_supply_status = initObj.main_supply_status
      }
      else {
        this.main_supply_status = false;
      }
      if (initObj.hasOwnProperty('process_id')) {
        this.process_id = initObj.process_id
      }
      else {
        this.process_id = 0;
      }
      if (initObj.hasOwnProperty('process_str')) {
        this.process_str = initObj.process_str
      }
      else {
        this.process_str = '';
      }
      if (initObj.hasOwnProperty('touch_signal_gas_nozzle')) {
        this.touch_signal_gas_nozzle = initObj.touch_signal_gas_nozzle
      }
      else {
        this.touch_signal_gas_nozzle = false;
      }
      if (initObj.hasOwnProperty('twin_synchro_active')) {
        this.twin_synchro_active = initObj.twin_synchro_active
      }
      else {
        this.twin_synchro_active = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Fronius500iState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [welding_voltage]
    bufferOffset = _serializer.float32(obj.welding_voltage, buffer, bufferOffset);
    // Serialize message field [welding_current]
    bufferOffset = _serializer.float32(obj.welding_current, buffer, bufferOffset);
    // Serialize message field [wire_feed_speed]
    bufferOffset = _serializer.float32(obj.wire_feed_speed, buffer, bufferOffset);
    // Serialize message field [motor_current_M1]
    bufferOffset = _serializer.float32(obj.motor_current_M1, buffer, bufferOffset);
    // Serialize message field [motor_current_M2]
    bufferOffset = _serializer.float32(obj.motor_current_M2, buffer, bufferOffset);
    // Serialize message field [life_toggle_bit]
    bufferOffset = _serializer.bool(obj.life_toggle_bit, buffer, bufferOffset);
    // Serialize message field [power_source_ready]
    bufferOffset = _serializer.bool(obj.power_source_ready, buffer, bufferOffset);
    // Serialize message field [warning]
    bufferOffset = _serializer.bool(obj.warning, buffer, bufferOffset);
    // Serialize message field [process_active]
    bufferOffset = _serializer.bool(obj.process_active, buffer, bufferOffset);
    // Serialize message field [current_flow]
    bufferOffset = _serializer.bool(obj.current_flow, buffer, bufferOffset);
    // Serialize message field [arc_stable]
    bufferOffset = _serializer.bool(obj.arc_stable, buffer, bufferOffset);
    // Serialize message field [main_current_signal]
    bufferOffset = _serializer.bool(obj.main_current_signal, buffer, bufferOffset);
    // Serialize message field [touch_signal]
    bufferOffset = _serializer.bool(obj.touch_signal, buffer, bufferOffset);
    // Serialize message field [collisionbox_active]
    bufferOffset = _serializer.bool(obj.collisionbox_active, buffer, bufferOffset);
    // Serialize message field [robot_motion_release]
    bufferOffset = _serializer.bool(obj.robot_motion_release, buffer, bufferOffset);
    // Serialize message field [wire_stick_workpiece]
    bufferOffset = _serializer.bool(obj.wire_stick_workpiece, buffer, bufferOffset);
    // Serialize message field [short_circuit_contact_tip]
    bufferOffset = _serializer.bool(obj.short_circuit_contact_tip, buffer, bufferOffset);
    // Serialize message field [parameter_selection_internally]
    bufferOffset = _serializer.bool(obj.parameter_selection_internally, buffer, bufferOffset);
    // Serialize message field [characteristic_number_valid]
    bufferOffset = _serializer.bool(obj.characteristic_number_valid, buffer, bufferOffset);
    // Serialize message field [torch_body_gripped]
    bufferOffset = _serializer.bool(obj.torch_body_gripped, buffer, bufferOffset);
    // Serialize message field [command_value_out_of_range]
    bufferOffset = _serializer.bool(obj.command_value_out_of_range, buffer, bufferOffset);
    // Serialize message field [correction_out_of_range]
    bufferOffset = _serializer.bool(obj.correction_out_of_range, buffer, bufferOffset);
    // Serialize message field [limitsignal]
    bufferOffset = _serializer.bool(obj.limitsignal, buffer, bufferOffset);
    // Serialize message field [main_supply_status]
    bufferOffset = _serializer.bool(obj.main_supply_status, buffer, bufferOffset);
    // Serialize message field [process_id]
    bufferOffset = _serializer.uint8(obj.process_id, buffer, bufferOffset);
    // Serialize message field [process_str]
    bufferOffset = _serializer.string(obj.process_str, buffer, bufferOffset);
    // Serialize message field [touch_signal_gas_nozzle]
    bufferOffset = _serializer.bool(obj.touch_signal_gas_nozzle, buffer, bufferOffset);
    // Serialize message field [twin_synchro_active]
    bufferOffset = _serializer.bool(obj.twin_synchro_active, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Fronius500iState
    let len;
    let data = new Fronius500iState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [welding_voltage]
    data.welding_voltage = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [welding_current]
    data.welding_current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [wire_feed_speed]
    data.wire_feed_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_current_M1]
    data.motor_current_M1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_current_M2]
    data.motor_current_M2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [life_toggle_bit]
    data.life_toggle_bit = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [power_source_ready]
    data.power_source_ready = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [warning]
    data.warning = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [process_active]
    data.process_active = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [current_flow]
    data.current_flow = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [arc_stable]
    data.arc_stable = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [main_current_signal]
    data.main_current_signal = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [touch_signal]
    data.touch_signal = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [collisionbox_active]
    data.collisionbox_active = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [robot_motion_release]
    data.robot_motion_release = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wire_stick_workpiece]
    data.wire_stick_workpiece = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [short_circuit_contact_tip]
    data.short_circuit_contact_tip = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [parameter_selection_internally]
    data.parameter_selection_internally = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [characteristic_number_valid]
    data.characteristic_number_valid = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [torch_body_gripped]
    data.torch_body_gripped = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [command_value_out_of_range]
    data.command_value_out_of_range = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [correction_out_of_range]
    data.correction_out_of_range = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [limitsignal]
    data.limitsignal = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [main_supply_status]
    data.main_supply_status = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [process_id]
    data.process_id = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [process_str]
    data.process_str = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [touch_signal_gas_nozzle]
    data.touch_signal_gas_nozzle = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [twin_synchro_active]
    data.twin_synchro_active = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += _getByteLength(object.process_str);
    return length + 46;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kuka_rsi_msgs/Fronius500iState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4355219bc4b3af559fd32d94b33e5f02';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Fronius500iState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.welding_voltage !== undefined) {
      resolved.welding_voltage = msg.welding_voltage;
    }
    else {
      resolved.welding_voltage = 0.0
    }

    if (msg.welding_current !== undefined) {
      resolved.welding_current = msg.welding_current;
    }
    else {
      resolved.welding_current = 0.0
    }

    if (msg.wire_feed_speed !== undefined) {
      resolved.wire_feed_speed = msg.wire_feed_speed;
    }
    else {
      resolved.wire_feed_speed = 0.0
    }

    if (msg.motor_current_M1 !== undefined) {
      resolved.motor_current_M1 = msg.motor_current_M1;
    }
    else {
      resolved.motor_current_M1 = 0.0
    }

    if (msg.motor_current_M2 !== undefined) {
      resolved.motor_current_M2 = msg.motor_current_M2;
    }
    else {
      resolved.motor_current_M2 = 0.0
    }

    if (msg.life_toggle_bit !== undefined) {
      resolved.life_toggle_bit = msg.life_toggle_bit;
    }
    else {
      resolved.life_toggle_bit = false
    }

    if (msg.power_source_ready !== undefined) {
      resolved.power_source_ready = msg.power_source_ready;
    }
    else {
      resolved.power_source_ready = false
    }

    if (msg.warning !== undefined) {
      resolved.warning = msg.warning;
    }
    else {
      resolved.warning = false
    }

    if (msg.process_active !== undefined) {
      resolved.process_active = msg.process_active;
    }
    else {
      resolved.process_active = false
    }

    if (msg.current_flow !== undefined) {
      resolved.current_flow = msg.current_flow;
    }
    else {
      resolved.current_flow = false
    }

    if (msg.arc_stable !== undefined) {
      resolved.arc_stable = msg.arc_stable;
    }
    else {
      resolved.arc_stable = false
    }

    if (msg.main_current_signal !== undefined) {
      resolved.main_current_signal = msg.main_current_signal;
    }
    else {
      resolved.main_current_signal = false
    }

    if (msg.touch_signal !== undefined) {
      resolved.touch_signal = msg.touch_signal;
    }
    else {
      resolved.touch_signal = false
    }

    if (msg.collisionbox_active !== undefined) {
      resolved.collisionbox_active = msg.collisionbox_active;
    }
    else {
      resolved.collisionbox_active = false
    }

    if (msg.robot_motion_release !== undefined) {
      resolved.robot_motion_release = msg.robot_motion_release;
    }
    else {
      resolved.robot_motion_release = false
    }

    if (msg.wire_stick_workpiece !== undefined) {
      resolved.wire_stick_workpiece = msg.wire_stick_workpiece;
    }
    else {
      resolved.wire_stick_workpiece = false
    }

    if (msg.short_circuit_contact_tip !== undefined) {
      resolved.short_circuit_contact_tip = msg.short_circuit_contact_tip;
    }
    else {
      resolved.short_circuit_contact_tip = false
    }

    if (msg.parameter_selection_internally !== undefined) {
      resolved.parameter_selection_internally = msg.parameter_selection_internally;
    }
    else {
      resolved.parameter_selection_internally = false
    }

    if (msg.characteristic_number_valid !== undefined) {
      resolved.characteristic_number_valid = msg.characteristic_number_valid;
    }
    else {
      resolved.characteristic_number_valid = false
    }

    if (msg.torch_body_gripped !== undefined) {
      resolved.torch_body_gripped = msg.torch_body_gripped;
    }
    else {
      resolved.torch_body_gripped = false
    }

    if (msg.command_value_out_of_range !== undefined) {
      resolved.command_value_out_of_range = msg.command_value_out_of_range;
    }
    else {
      resolved.command_value_out_of_range = false
    }

    if (msg.correction_out_of_range !== undefined) {
      resolved.correction_out_of_range = msg.correction_out_of_range;
    }
    else {
      resolved.correction_out_of_range = false
    }

    if (msg.limitsignal !== undefined) {
      resolved.limitsignal = msg.limitsignal;
    }
    else {
      resolved.limitsignal = false
    }

    if (msg.main_supply_status !== undefined) {
      resolved.main_supply_status = msg.main_supply_status;
    }
    else {
      resolved.main_supply_status = false
    }

    if (msg.process_id !== undefined) {
      resolved.process_id = msg.process_id;
    }
    else {
      resolved.process_id = 0
    }

    if (msg.process_str !== undefined) {
      resolved.process_str = msg.process_str;
    }
    else {
      resolved.process_str = ''
    }

    if (msg.touch_signal_gas_nozzle !== undefined) {
      resolved.touch_signal_gas_nozzle = msg.touch_signal_gas_nozzle;
    }
    else {
      resolved.touch_signal_gas_nozzle = false
    }

    if (msg.twin_synchro_active !== undefined) {
      resolved.twin_synchro_active = msg.twin_synchro_active;
    }
    else {
      resolved.twin_synchro_active = false
    }

    return resolved;
    }
};

module.exports = Fronius500iState;
