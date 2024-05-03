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

class PlasmaCommand {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.Dinse_wire_feed_speed = null;
      this.EWM_current = null;
      this.EWM_plasma_gas = null;
      this.EWM_shield_gas = null;
      this.Dinse_start_release = null;
      this.Dinse_acknowledge_fault = null;
      this.Dinse_start_wire_feed = null;
      this.Dinse_start_power_source = null;
      this.Dinse_wirebreak = null;
      this.Dinse_wire_forward = null;
      this.Dinse_wire_backward = null;
      this.Dinse_gas_on = null;
      this.Dinse_retraction = null;
      this.Dinse_positioning = null;
      this.EWM_Start = null;
      this.EWM_gas_test_1_shield = null;
      this.EWM_gas_test_2_plasma = null;
      this.EWM_feed_wire = null;
      this.EWM_unfeed_wire = null;
      this.EWM_position_search = null;
      this.EWM_error_reset = null;
      this.EWM_start_aux_process = null;
      this.EWM_user_relay = null;
      this.EWM_welding_simulation = null;
      this.EWM_monitoring_function = null;
      this.EWM_filler_wire_activated = null;
      this.EWM_reserved_1 = null;
      this.EWM_weld_mode_select_bit_0 = null;
      this.EWM_weld_mode_select_bit_1 = null;
      this.EWM_wirefeeder_switch = null;
      this.EWM_reserved_2 = null;
      this.EWM_cold_wire_feed_speed = null;
      this.EWM_job_number = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('Dinse_wire_feed_speed')) {
        this.Dinse_wire_feed_speed = initObj.Dinse_wire_feed_speed
      }
      else {
        this.Dinse_wire_feed_speed = 0.0;
      }
      if (initObj.hasOwnProperty('EWM_current')) {
        this.EWM_current = initObj.EWM_current
      }
      else {
        this.EWM_current = 0.0;
      }
      if (initObj.hasOwnProperty('EWM_plasma_gas')) {
        this.EWM_plasma_gas = initObj.EWM_plasma_gas
      }
      else {
        this.EWM_plasma_gas = 0.0;
      }
      if (initObj.hasOwnProperty('EWM_shield_gas')) {
        this.EWM_shield_gas = initObj.EWM_shield_gas
      }
      else {
        this.EWM_shield_gas = 0.0;
      }
      if (initObj.hasOwnProperty('Dinse_start_release')) {
        this.Dinse_start_release = initObj.Dinse_start_release
      }
      else {
        this.Dinse_start_release = false;
      }
      if (initObj.hasOwnProperty('Dinse_acknowledge_fault')) {
        this.Dinse_acknowledge_fault = initObj.Dinse_acknowledge_fault
      }
      else {
        this.Dinse_acknowledge_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_start_wire_feed')) {
        this.Dinse_start_wire_feed = initObj.Dinse_start_wire_feed
      }
      else {
        this.Dinse_start_wire_feed = false;
      }
      if (initObj.hasOwnProperty('Dinse_start_power_source')) {
        this.Dinse_start_power_source = initObj.Dinse_start_power_source
      }
      else {
        this.Dinse_start_power_source = false;
      }
      if (initObj.hasOwnProperty('Dinse_wirebreak')) {
        this.Dinse_wirebreak = initObj.Dinse_wirebreak
      }
      else {
        this.Dinse_wirebreak = false;
      }
      if (initObj.hasOwnProperty('Dinse_wire_forward')) {
        this.Dinse_wire_forward = initObj.Dinse_wire_forward
      }
      else {
        this.Dinse_wire_forward = false;
      }
      if (initObj.hasOwnProperty('Dinse_wire_backward')) {
        this.Dinse_wire_backward = initObj.Dinse_wire_backward
      }
      else {
        this.Dinse_wire_backward = false;
      }
      if (initObj.hasOwnProperty('Dinse_gas_on')) {
        this.Dinse_gas_on = initObj.Dinse_gas_on
      }
      else {
        this.Dinse_gas_on = false;
      }
      if (initObj.hasOwnProperty('Dinse_retraction')) {
        this.Dinse_retraction = initObj.Dinse_retraction
      }
      else {
        this.Dinse_retraction = false;
      }
      if (initObj.hasOwnProperty('Dinse_positioning')) {
        this.Dinse_positioning = initObj.Dinse_positioning
      }
      else {
        this.Dinse_positioning = false;
      }
      if (initObj.hasOwnProperty('EWM_Start')) {
        this.EWM_Start = initObj.EWM_Start
      }
      else {
        this.EWM_Start = false;
      }
      if (initObj.hasOwnProperty('EWM_gas_test_1_shield')) {
        this.EWM_gas_test_1_shield = initObj.EWM_gas_test_1_shield
      }
      else {
        this.EWM_gas_test_1_shield = false;
      }
      if (initObj.hasOwnProperty('EWM_gas_test_2_plasma')) {
        this.EWM_gas_test_2_plasma = initObj.EWM_gas_test_2_plasma
      }
      else {
        this.EWM_gas_test_2_plasma = false;
      }
      if (initObj.hasOwnProperty('EWM_feed_wire')) {
        this.EWM_feed_wire = initObj.EWM_feed_wire
      }
      else {
        this.EWM_feed_wire = false;
      }
      if (initObj.hasOwnProperty('EWM_unfeed_wire')) {
        this.EWM_unfeed_wire = initObj.EWM_unfeed_wire
      }
      else {
        this.EWM_unfeed_wire = false;
      }
      if (initObj.hasOwnProperty('EWM_position_search')) {
        this.EWM_position_search = initObj.EWM_position_search
      }
      else {
        this.EWM_position_search = false;
      }
      if (initObj.hasOwnProperty('EWM_error_reset')) {
        this.EWM_error_reset = initObj.EWM_error_reset
      }
      else {
        this.EWM_error_reset = false;
      }
      if (initObj.hasOwnProperty('EWM_start_aux_process')) {
        this.EWM_start_aux_process = initObj.EWM_start_aux_process
      }
      else {
        this.EWM_start_aux_process = false;
      }
      if (initObj.hasOwnProperty('EWM_user_relay')) {
        this.EWM_user_relay = initObj.EWM_user_relay
      }
      else {
        this.EWM_user_relay = false;
      }
      if (initObj.hasOwnProperty('EWM_welding_simulation')) {
        this.EWM_welding_simulation = initObj.EWM_welding_simulation
      }
      else {
        this.EWM_welding_simulation = false;
      }
      if (initObj.hasOwnProperty('EWM_monitoring_function')) {
        this.EWM_monitoring_function = initObj.EWM_monitoring_function
      }
      else {
        this.EWM_monitoring_function = false;
      }
      if (initObj.hasOwnProperty('EWM_filler_wire_activated')) {
        this.EWM_filler_wire_activated = initObj.EWM_filler_wire_activated
      }
      else {
        this.EWM_filler_wire_activated = false;
      }
      if (initObj.hasOwnProperty('EWM_reserved_1')) {
        this.EWM_reserved_1 = initObj.EWM_reserved_1
      }
      else {
        this.EWM_reserved_1 = false;
      }
      if (initObj.hasOwnProperty('EWM_weld_mode_select_bit_0')) {
        this.EWM_weld_mode_select_bit_0 = initObj.EWM_weld_mode_select_bit_0
      }
      else {
        this.EWM_weld_mode_select_bit_0 = false;
      }
      if (initObj.hasOwnProperty('EWM_weld_mode_select_bit_1')) {
        this.EWM_weld_mode_select_bit_1 = initObj.EWM_weld_mode_select_bit_1
      }
      else {
        this.EWM_weld_mode_select_bit_1 = false;
      }
      if (initObj.hasOwnProperty('EWM_wirefeeder_switch')) {
        this.EWM_wirefeeder_switch = initObj.EWM_wirefeeder_switch
      }
      else {
        this.EWM_wirefeeder_switch = false;
      }
      if (initObj.hasOwnProperty('EWM_reserved_2')) {
        this.EWM_reserved_2 = initObj.EWM_reserved_2
      }
      else {
        this.EWM_reserved_2 = false;
      }
      if (initObj.hasOwnProperty('EWM_cold_wire_feed_speed')) {
        this.EWM_cold_wire_feed_speed = initObj.EWM_cold_wire_feed_speed
      }
      else {
        this.EWM_cold_wire_feed_speed = 0.0;
      }
      if (initObj.hasOwnProperty('EWM_job_number')) {
        this.EWM_job_number = initObj.EWM_job_number
      }
      else {
        this.EWM_job_number = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PlasmaCommand
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_feed_speed]
    bufferOffset = _serializer.float32(obj.Dinse_wire_feed_speed, buffer, bufferOffset);
    // Serialize message field [EWM_current]
    bufferOffset = _serializer.float32(obj.EWM_current, buffer, bufferOffset);
    // Serialize message field [EWM_plasma_gas]
    bufferOffset = _serializer.float32(obj.EWM_plasma_gas, buffer, bufferOffset);
    // Serialize message field [EWM_shield_gas]
    bufferOffset = _serializer.float32(obj.EWM_shield_gas, buffer, bufferOffset);
    // Serialize message field [Dinse_start_release]
    bufferOffset = _serializer.bool(obj.Dinse_start_release, buffer, bufferOffset);
    // Serialize message field [Dinse_acknowledge_fault]
    bufferOffset = _serializer.bool(obj.Dinse_acknowledge_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_start_wire_feed]
    bufferOffset = _serializer.bool(obj.Dinse_start_wire_feed, buffer, bufferOffset);
    // Serialize message field [Dinse_start_power_source]
    bufferOffset = _serializer.bool(obj.Dinse_start_power_source, buffer, bufferOffset);
    // Serialize message field [Dinse_wirebreak]
    bufferOffset = _serializer.bool(obj.Dinse_wirebreak, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_forward]
    bufferOffset = _serializer.bool(obj.Dinse_wire_forward, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_backward]
    bufferOffset = _serializer.bool(obj.Dinse_wire_backward, buffer, bufferOffset);
    // Serialize message field [Dinse_gas_on]
    bufferOffset = _serializer.bool(obj.Dinse_gas_on, buffer, bufferOffset);
    // Serialize message field [Dinse_retraction]
    bufferOffset = _serializer.bool(obj.Dinse_retraction, buffer, bufferOffset);
    // Serialize message field [Dinse_positioning]
    bufferOffset = _serializer.bool(obj.Dinse_positioning, buffer, bufferOffset);
    // Serialize message field [EWM_Start]
    bufferOffset = _serializer.bool(obj.EWM_Start, buffer, bufferOffset);
    // Serialize message field [EWM_gas_test_1_shield]
    bufferOffset = _serializer.bool(obj.EWM_gas_test_1_shield, buffer, bufferOffset);
    // Serialize message field [EWM_gas_test_2_plasma]
    bufferOffset = _serializer.bool(obj.EWM_gas_test_2_plasma, buffer, bufferOffset);
    // Serialize message field [EWM_feed_wire]
    bufferOffset = _serializer.bool(obj.EWM_feed_wire, buffer, bufferOffset);
    // Serialize message field [EWM_unfeed_wire]
    bufferOffset = _serializer.bool(obj.EWM_unfeed_wire, buffer, bufferOffset);
    // Serialize message field [EWM_position_search]
    bufferOffset = _serializer.bool(obj.EWM_position_search, buffer, bufferOffset);
    // Serialize message field [EWM_error_reset]
    bufferOffset = _serializer.bool(obj.EWM_error_reset, buffer, bufferOffset);
    // Serialize message field [EWM_start_aux_process]
    bufferOffset = _serializer.bool(obj.EWM_start_aux_process, buffer, bufferOffset);
    // Serialize message field [EWM_user_relay]
    bufferOffset = _serializer.bool(obj.EWM_user_relay, buffer, bufferOffset);
    // Serialize message field [EWM_welding_simulation]
    bufferOffset = _serializer.bool(obj.EWM_welding_simulation, buffer, bufferOffset);
    // Serialize message field [EWM_monitoring_function]
    bufferOffset = _serializer.bool(obj.EWM_monitoring_function, buffer, bufferOffset);
    // Serialize message field [EWM_filler_wire_activated]
    bufferOffset = _serializer.bool(obj.EWM_filler_wire_activated, buffer, bufferOffset);
    // Serialize message field [EWM_reserved_1]
    bufferOffset = _serializer.bool(obj.EWM_reserved_1, buffer, bufferOffset);
    // Serialize message field [EWM_weld_mode_select_bit_0]
    bufferOffset = _serializer.bool(obj.EWM_weld_mode_select_bit_0, buffer, bufferOffset);
    // Serialize message field [EWM_weld_mode_select_bit_1]
    bufferOffset = _serializer.bool(obj.EWM_weld_mode_select_bit_1, buffer, bufferOffset);
    // Serialize message field [EWM_wirefeeder_switch]
    bufferOffset = _serializer.bool(obj.EWM_wirefeeder_switch, buffer, bufferOffset);
    // Serialize message field [EWM_reserved_2]
    bufferOffset = _serializer.bool(obj.EWM_reserved_2, buffer, bufferOffset);
    // Serialize message field [EWM_cold_wire_feed_speed]
    bufferOffset = _serializer.float32(obj.EWM_cold_wire_feed_speed, buffer, bufferOffset);
    // Serialize message field [EWM_job_number]
    bufferOffset = _serializer.uint8(obj.EWM_job_number, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PlasmaCommand
    let len;
    let data = new PlasmaCommand(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_feed_speed]
    data.Dinse_wire_feed_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [EWM_current]
    data.EWM_current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [EWM_plasma_gas]
    data.EWM_plasma_gas = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [EWM_shield_gas]
    data.EWM_shield_gas = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [Dinse_start_release]
    data.Dinse_start_release = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_acknowledge_fault]
    data.Dinse_acknowledge_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_start_wire_feed]
    data.Dinse_start_wire_feed = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_start_power_source]
    data.Dinse_start_power_source = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_wirebreak]
    data.Dinse_wirebreak = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_forward]
    data.Dinse_wire_forward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_backward]
    data.Dinse_wire_backward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_gas_on]
    data.Dinse_gas_on = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_retraction]
    data.Dinse_retraction = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_positioning]
    data.Dinse_positioning = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_Start]
    data.EWM_Start = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_gas_test_1_shield]
    data.EWM_gas_test_1_shield = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_gas_test_2_plasma]
    data.EWM_gas_test_2_plasma = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_feed_wire]
    data.EWM_feed_wire = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_unfeed_wire]
    data.EWM_unfeed_wire = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_position_search]
    data.EWM_position_search = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_error_reset]
    data.EWM_error_reset = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_start_aux_process]
    data.EWM_start_aux_process = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_user_relay]
    data.EWM_user_relay = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_welding_simulation]
    data.EWM_welding_simulation = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_monitoring_function]
    data.EWM_monitoring_function = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_filler_wire_activated]
    data.EWM_filler_wire_activated = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_reserved_1]
    data.EWM_reserved_1 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_weld_mode_select_bit_0]
    data.EWM_weld_mode_select_bit_0 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_weld_mode_select_bit_1]
    data.EWM_weld_mode_select_bit_1 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_wirefeeder_switch]
    data.EWM_wirefeeder_switch = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_reserved_2]
    data.EWM_reserved_2 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_cold_wire_feed_speed]
    data.EWM_cold_wire_feed_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [EWM_job_number]
    data.EWM_job_number = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kuka_rsi_msgs/PlasmaCommand';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e908814e1fa1f45ddd9838e2ac41ab4e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    # Field 3-4
    float32 Dinse_wire_feed_speed
    # Field 8-9
    float32 EWM_current
    # Field 12-13
    float32 EWM_plasma_gas
    # Field 14-15
    float32 EWM_shield_gas
    # Field 1
    bool Dinse_start_release
    bool Dinse_acknowledge_fault
    bool Dinse_start_wire_feed
    bool Dinse_start_power_source
    bool Dinse_wirebreak
    bool Dinse_wire_forward
    bool Dinse_wire_backward
    bool Dinse_gas_on
    # Field 2
    bool Dinse_retraction
    bool Dinse_positioning
    # Field 5
    bool EWM_Start
    # Field 6
    bool EWM_gas_test_1_shield
    bool EWM_gas_test_2_plasma
    bool EWM_feed_wire
    bool EWM_unfeed_wire
    bool EWM_position_search
    bool EWM_error_reset
    bool EWM_start_aux_process
    bool EWM_user_relay
    # Field 7
    bool EWM_welding_simulation
    bool EWM_monitoring_function
    bool EWM_filler_wire_activated
    bool EWM_reserved_1
    bool EWM_weld_mode_select_bit_0
    bool EWM_weld_mode_select_bit_1
    bool EWM_wirefeeder_switch
    bool EWM_reserved_2
    # Field 10-11
    float32 EWM_cold_wire_feed_speed
    # Field 16
    uint8 EWM_job_number
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
    const resolved = new PlasmaCommand(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.Dinse_wire_feed_speed !== undefined) {
      resolved.Dinse_wire_feed_speed = msg.Dinse_wire_feed_speed;
    }
    else {
      resolved.Dinse_wire_feed_speed = 0.0
    }

    if (msg.EWM_current !== undefined) {
      resolved.EWM_current = msg.EWM_current;
    }
    else {
      resolved.EWM_current = 0.0
    }

    if (msg.EWM_plasma_gas !== undefined) {
      resolved.EWM_plasma_gas = msg.EWM_plasma_gas;
    }
    else {
      resolved.EWM_plasma_gas = 0.0
    }

    if (msg.EWM_shield_gas !== undefined) {
      resolved.EWM_shield_gas = msg.EWM_shield_gas;
    }
    else {
      resolved.EWM_shield_gas = 0.0
    }

    if (msg.Dinse_start_release !== undefined) {
      resolved.Dinse_start_release = msg.Dinse_start_release;
    }
    else {
      resolved.Dinse_start_release = false
    }

    if (msg.Dinse_acknowledge_fault !== undefined) {
      resolved.Dinse_acknowledge_fault = msg.Dinse_acknowledge_fault;
    }
    else {
      resolved.Dinse_acknowledge_fault = false
    }

    if (msg.Dinse_start_wire_feed !== undefined) {
      resolved.Dinse_start_wire_feed = msg.Dinse_start_wire_feed;
    }
    else {
      resolved.Dinse_start_wire_feed = false
    }

    if (msg.Dinse_start_power_source !== undefined) {
      resolved.Dinse_start_power_source = msg.Dinse_start_power_source;
    }
    else {
      resolved.Dinse_start_power_source = false
    }

    if (msg.Dinse_wirebreak !== undefined) {
      resolved.Dinse_wirebreak = msg.Dinse_wirebreak;
    }
    else {
      resolved.Dinse_wirebreak = false
    }

    if (msg.Dinse_wire_forward !== undefined) {
      resolved.Dinse_wire_forward = msg.Dinse_wire_forward;
    }
    else {
      resolved.Dinse_wire_forward = false
    }

    if (msg.Dinse_wire_backward !== undefined) {
      resolved.Dinse_wire_backward = msg.Dinse_wire_backward;
    }
    else {
      resolved.Dinse_wire_backward = false
    }

    if (msg.Dinse_gas_on !== undefined) {
      resolved.Dinse_gas_on = msg.Dinse_gas_on;
    }
    else {
      resolved.Dinse_gas_on = false
    }

    if (msg.Dinse_retraction !== undefined) {
      resolved.Dinse_retraction = msg.Dinse_retraction;
    }
    else {
      resolved.Dinse_retraction = false
    }

    if (msg.Dinse_positioning !== undefined) {
      resolved.Dinse_positioning = msg.Dinse_positioning;
    }
    else {
      resolved.Dinse_positioning = false
    }

    if (msg.EWM_Start !== undefined) {
      resolved.EWM_Start = msg.EWM_Start;
    }
    else {
      resolved.EWM_Start = false
    }

    if (msg.EWM_gas_test_1_shield !== undefined) {
      resolved.EWM_gas_test_1_shield = msg.EWM_gas_test_1_shield;
    }
    else {
      resolved.EWM_gas_test_1_shield = false
    }

    if (msg.EWM_gas_test_2_plasma !== undefined) {
      resolved.EWM_gas_test_2_plasma = msg.EWM_gas_test_2_plasma;
    }
    else {
      resolved.EWM_gas_test_2_plasma = false
    }

    if (msg.EWM_feed_wire !== undefined) {
      resolved.EWM_feed_wire = msg.EWM_feed_wire;
    }
    else {
      resolved.EWM_feed_wire = false
    }

    if (msg.EWM_unfeed_wire !== undefined) {
      resolved.EWM_unfeed_wire = msg.EWM_unfeed_wire;
    }
    else {
      resolved.EWM_unfeed_wire = false
    }

    if (msg.EWM_position_search !== undefined) {
      resolved.EWM_position_search = msg.EWM_position_search;
    }
    else {
      resolved.EWM_position_search = false
    }

    if (msg.EWM_error_reset !== undefined) {
      resolved.EWM_error_reset = msg.EWM_error_reset;
    }
    else {
      resolved.EWM_error_reset = false
    }

    if (msg.EWM_start_aux_process !== undefined) {
      resolved.EWM_start_aux_process = msg.EWM_start_aux_process;
    }
    else {
      resolved.EWM_start_aux_process = false
    }

    if (msg.EWM_user_relay !== undefined) {
      resolved.EWM_user_relay = msg.EWM_user_relay;
    }
    else {
      resolved.EWM_user_relay = false
    }

    if (msg.EWM_welding_simulation !== undefined) {
      resolved.EWM_welding_simulation = msg.EWM_welding_simulation;
    }
    else {
      resolved.EWM_welding_simulation = false
    }

    if (msg.EWM_monitoring_function !== undefined) {
      resolved.EWM_monitoring_function = msg.EWM_monitoring_function;
    }
    else {
      resolved.EWM_monitoring_function = false
    }

    if (msg.EWM_filler_wire_activated !== undefined) {
      resolved.EWM_filler_wire_activated = msg.EWM_filler_wire_activated;
    }
    else {
      resolved.EWM_filler_wire_activated = false
    }

    if (msg.EWM_reserved_1 !== undefined) {
      resolved.EWM_reserved_1 = msg.EWM_reserved_1;
    }
    else {
      resolved.EWM_reserved_1 = false
    }

    if (msg.EWM_weld_mode_select_bit_0 !== undefined) {
      resolved.EWM_weld_mode_select_bit_0 = msg.EWM_weld_mode_select_bit_0;
    }
    else {
      resolved.EWM_weld_mode_select_bit_0 = false
    }

    if (msg.EWM_weld_mode_select_bit_1 !== undefined) {
      resolved.EWM_weld_mode_select_bit_1 = msg.EWM_weld_mode_select_bit_1;
    }
    else {
      resolved.EWM_weld_mode_select_bit_1 = false
    }

    if (msg.EWM_wirefeeder_switch !== undefined) {
      resolved.EWM_wirefeeder_switch = msg.EWM_wirefeeder_switch;
    }
    else {
      resolved.EWM_wirefeeder_switch = false
    }

    if (msg.EWM_reserved_2 !== undefined) {
      resolved.EWM_reserved_2 = msg.EWM_reserved_2;
    }
    else {
      resolved.EWM_reserved_2 = false
    }

    if (msg.EWM_cold_wire_feed_speed !== undefined) {
      resolved.EWM_cold_wire_feed_speed = msg.EWM_cold_wire_feed_speed;
    }
    else {
      resolved.EWM_cold_wire_feed_speed = 0.0
    }

    if (msg.EWM_job_number !== undefined) {
      resolved.EWM_job_number = msg.EWM_job_number;
    }
    else {
      resolved.EWM_job_number = 0
    }

    return resolved;
    }
};

module.exports = PlasmaCommand;
