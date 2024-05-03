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

class FroniusState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.arc_voltage = null;
      this.arc_current = null;
      this.motor_current = null;
      this.wire_feed_speed = null;
      this.arc_stable = null;
      this.limit_signal = null;
      this.process_active = null;
      this.main_current_signal = null;
      this.torch_collision_protection = null;
      this.power_source_ready = null;
      this.communication_ready = null;
      this.life_toggle_bit = null;
      this.error_number = null;
      this.wire_stick_control = null;
      this.robot_access = null;
      this.wire_available = null;
      this.timeout_short_circuit = null;
      this.data_documentation_ready = null;
      this.power_outside_range = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('arc_voltage')) {
        this.arc_voltage = initObj.arc_voltage
      }
      else {
        this.arc_voltage = 0.0;
      }
      if (initObj.hasOwnProperty('arc_current')) {
        this.arc_current = initObj.arc_current
      }
      else {
        this.arc_current = 0.0;
      }
      if (initObj.hasOwnProperty('motor_current')) {
        this.motor_current = initObj.motor_current
      }
      else {
        this.motor_current = 0.0;
      }
      if (initObj.hasOwnProperty('wire_feed_speed')) {
        this.wire_feed_speed = initObj.wire_feed_speed
      }
      else {
        this.wire_feed_speed = 0.0;
      }
      if (initObj.hasOwnProperty('arc_stable')) {
        this.arc_stable = initObj.arc_stable
      }
      else {
        this.arc_stable = false;
      }
      if (initObj.hasOwnProperty('limit_signal')) {
        this.limit_signal = initObj.limit_signal
      }
      else {
        this.limit_signal = false;
      }
      if (initObj.hasOwnProperty('process_active')) {
        this.process_active = initObj.process_active
      }
      else {
        this.process_active = false;
      }
      if (initObj.hasOwnProperty('main_current_signal')) {
        this.main_current_signal = initObj.main_current_signal
      }
      else {
        this.main_current_signal = false;
      }
      if (initObj.hasOwnProperty('torch_collision_protection')) {
        this.torch_collision_protection = initObj.torch_collision_protection
      }
      else {
        this.torch_collision_protection = false;
      }
      if (initObj.hasOwnProperty('power_source_ready')) {
        this.power_source_ready = initObj.power_source_ready
      }
      else {
        this.power_source_ready = false;
      }
      if (initObj.hasOwnProperty('communication_ready')) {
        this.communication_ready = initObj.communication_ready
      }
      else {
        this.communication_ready = false;
      }
      if (initObj.hasOwnProperty('life_toggle_bit')) {
        this.life_toggle_bit = initObj.life_toggle_bit
      }
      else {
        this.life_toggle_bit = false;
      }
      if (initObj.hasOwnProperty('error_number')) {
        this.error_number = initObj.error_number
      }
      else {
        this.error_number = 0;
      }
      if (initObj.hasOwnProperty('wire_stick_control')) {
        this.wire_stick_control = initObj.wire_stick_control
      }
      else {
        this.wire_stick_control = false;
      }
      if (initObj.hasOwnProperty('robot_access')) {
        this.robot_access = initObj.robot_access
      }
      else {
        this.robot_access = false;
      }
      if (initObj.hasOwnProperty('wire_available')) {
        this.wire_available = initObj.wire_available
      }
      else {
        this.wire_available = false;
      }
      if (initObj.hasOwnProperty('timeout_short_circuit')) {
        this.timeout_short_circuit = initObj.timeout_short_circuit
      }
      else {
        this.timeout_short_circuit = false;
      }
      if (initObj.hasOwnProperty('data_documentation_ready')) {
        this.data_documentation_ready = initObj.data_documentation_ready
      }
      else {
        this.data_documentation_ready = false;
      }
      if (initObj.hasOwnProperty('power_outside_range')) {
        this.power_outside_range = initObj.power_outside_range
      }
      else {
        this.power_outside_range = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FroniusState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [arc_voltage]
    bufferOffset = _serializer.float32(obj.arc_voltage, buffer, bufferOffset);
    // Serialize message field [arc_current]
    bufferOffset = _serializer.float32(obj.arc_current, buffer, bufferOffset);
    // Serialize message field [motor_current]
    bufferOffset = _serializer.float32(obj.motor_current, buffer, bufferOffset);
    // Serialize message field [wire_feed_speed]
    bufferOffset = _serializer.float32(obj.wire_feed_speed, buffer, bufferOffset);
    // Serialize message field [arc_stable]
    bufferOffset = _serializer.bool(obj.arc_stable, buffer, bufferOffset);
    // Serialize message field [limit_signal]
    bufferOffset = _serializer.bool(obj.limit_signal, buffer, bufferOffset);
    // Serialize message field [process_active]
    bufferOffset = _serializer.bool(obj.process_active, buffer, bufferOffset);
    // Serialize message field [main_current_signal]
    bufferOffset = _serializer.bool(obj.main_current_signal, buffer, bufferOffset);
    // Serialize message field [torch_collision_protection]
    bufferOffset = _serializer.bool(obj.torch_collision_protection, buffer, bufferOffset);
    // Serialize message field [power_source_ready]
    bufferOffset = _serializer.bool(obj.power_source_ready, buffer, bufferOffset);
    // Serialize message field [communication_ready]
    bufferOffset = _serializer.bool(obj.communication_ready, buffer, bufferOffset);
    // Serialize message field [life_toggle_bit]
    bufferOffset = _serializer.bool(obj.life_toggle_bit, buffer, bufferOffset);
    // Serialize message field [error_number]
    bufferOffset = _serializer.uint8(obj.error_number, buffer, bufferOffset);
    // Serialize message field [wire_stick_control]
    bufferOffset = _serializer.bool(obj.wire_stick_control, buffer, bufferOffset);
    // Serialize message field [robot_access]
    bufferOffset = _serializer.bool(obj.robot_access, buffer, bufferOffset);
    // Serialize message field [wire_available]
    bufferOffset = _serializer.bool(obj.wire_available, buffer, bufferOffset);
    // Serialize message field [timeout_short_circuit]
    bufferOffset = _serializer.bool(obj.timeout_short_circuit, buffer, bufferOffset);
    // Serialize message field [data_documentation_ready]
    bufferOffset = _serializer.bool(obj.data_documentation_ready, buffer, bufferOffset);
    // Serialize message field [power_outside_range]
    bufferOffset = _serializer.bool(obj.power_outside_range, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FroniusState
    let len;
    let data = new FroniusState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [arc_voltage]
    data.arc_voltage = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [arc_current]
    data.arc_current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_current]
    data.motor_current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [wire_feed_speed]
    data.wire_feed_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [arc_stable]
    data.arc_stable = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [limit_signal]
    data.limit_signal = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [process_active]
    data.process_active = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [main_current_signal]
    data.main_current_signal = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [torch_collision_protection]
    data.torch_collision_protection = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [power_source_ready]
    data.power_source_ready = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [communication_ready]
    data.communication_ready = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [life_toggle_bit]
    data.life_toggle_bit = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [error_number]
    data.error_number = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [wire_stick_control]
    data.wire_stick_control = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [robot_access]
    data.robot_access = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wire_available]
    data.wire_available = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [timeout_short_circuit]
    data.timeout_short_circuit = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [data_documentation_ready]
    data.data_documentation_ready = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [power_outside_range]
    data.power_outside_range = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 31;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kuka_rsi_msgs/FroniusState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '30bd5f2b575dd738b94a41edaf98cf7f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FroniusState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.arc_voltage !== undefined) {
      resolved.arc_voltage = msg.arc_voltage;
    }
    else {
      resolved.arc_voltage = 0.0
    }

    if (msg.arc_current !== undefined) {
      resolved.arc_current = msg.arc_current;
    }
    else {
      resolved.arc_current = 0.0
    }

    if (msg.motor_current !== undefined) {
      resolved.motor_current = msg.motor_current;
    }
    else {
      resolved.motor_current = 0.0
    }

    if (msg.wire_feed_speed !== undefined) {
      resolved.wire_feed_speed = msg.wire_feed_speed;
    }
    else {
      resolved.wire_feed_speed = 0.0
    }

    if (msg.arc_stable !== undefined) {
      resolved.arc_stable = msg.arc_stable;
    }
    else {
      resolved.arc_stable = false
    }

    if (msg.limit_signal !== undefined) {
      resolved.limit_signal = msg.limit_signal;
    }
    else {
      resolved.limit_signal = false
    }

    if (msg.process_active !== undefined) {
      resolved.process_active = msg.process_active;
    }
    else {
      resolved.process_active = false
    }

    if (msg.main_current_signal !== undefined) {
      resolved.main_current_signal = msg.main_current_signal;
    }
    else {
      resolved.main_current_signal = false
    }

    if (msg.torch_collision_protection !== undefined) {
      resolved.torch_collision_protection = msg.torch_collision_protection;
    }
    else {
      resolved.torch_collision_protection = false
    }

    if (msg.power_source_ready !== undefined) {
      resolved.power_source_ready = msg.power_source_ready;
    }
    else {
      resolved.power_source_ready = false
    }

    if (msg.communication_ready !== undefined) {
      resolved.communication_ready = msg.communication_ready;
    }
    else {
      resolved.communication_ready = false
    }

    if (msg.life_toggle_bit !== undefined) {
      resolved.life_toggle_bit = msg.life_toggle_bit;
    }
    else {
      resolved.life_toggle_bit = false
    }

    if (msg.error_number !== undefined) {
      resolved.error_number = msg.error_number;
    }
    else {
      resolved.error_number = 0
    }

    if (msg.wire_stick_control !== undefined) {
      resolved.wire_stick_control = msg.wire_stick_control;
    }
    else {
      resolved.wire_stick_control = false
    }

    if (msg.robot_access !== undefined) {
      resolved.robot_access = msg.robot_access;
    }
    else {
      resolved.robot_access = false
    }

    if (msg.wire_available !== undefined) {
      resolved.wire_available = msg.wire_available;
    }
    else {
      resolved.wire_available = false
    }

    if (msg.timeout_short_circuit !== undefined) {
      resolved.timeout_short_circuit = msg.timeout_short_circuit;
    }
    else {
      resolved.timeout_short_circuit = false
    }

    if (msg.data_documentation_ready !== undefined) {
      resolved.data_documentation_ready = msg.data_documentation_ready;
    }
    else {
      resolved.data_documentation_ready = false
    }

    if (msg.power_outside_range !== undefined) {
      resolved.power_outside_range = msg.power_outside_range;
    }
    else {
      resolved.power_outside_range = false
    }

    return resolved;
    }
};

module.exports = FroniusState;
