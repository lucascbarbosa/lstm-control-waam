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

class FroniusCommand {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.power_set_value = null;
      this.arc_length_correction = null;
      this.dynamic_correction = null;
      this.burn_back = null;
      this.welding_start = null;
      this.working_modes = null;
      this.master_selection_twin = null;
      this.gas_test = null;
      this.wire_forward = null;
      this.job_number = null;
      this.program_number = null;
      this.welding_simulation = null;
      this.synchro_pulse_disable = null;
      this.SFI_disable = null;
      this.dynamic_correction_disable = null;
      this.burn_back_disable = null;
      this.full_power_range = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('power_set_value')) {
        this.power_set_value = initObj.power_set_value
      }
      else {
        this.power_set_value = 0.0;
      }
      if (initObj.hasOwnProperty('arc_length_correction')) {
        this.arc_length_correction = initObj.arc_length_correction
      }
      else {
        this.arc_length_correction = 0.0;
      }
      if (initObj.hasOwnProperty('dynamic_correction')) {
        this.dynamic_correction = initObj.dynamic_correction
      }
      else {
        this.dynamic_correction = 0.0;
      }
      if (initObj.hasOwnProperty('burn_back')) {
        this.burn_back = initObj.burn_back
      }
      else {
        this.burn_back = 0.0;
      }
      if (initObj.hasOwnProperty('welding_start')) {
        this.welding_start = initObj.welding_start
      }
      else {
        this.welding_start = false;
      }
      if (initObj.hasOwnProperty('working_modes')) {
        this.working_modes = initObj.working_modes
      }
      else {
        this.working_modes = 0;
      }
      if (initObj.hasOwnProperty('master_selection_twin')) {
        this.master_selection_twin = initObj.master_selection_twin
      }
      else {
        this.master_selection_twin = false;
      }
      if (initObj.hasOwnProperty('gas_test')) {
        this.gas_test = initObj.gas_test
      }
      else {
        this.gas_test = false;
      }
      if (initObj.hasOwnProperty('wire_forward')) {
        this.wire_forward = initObj.wire_forward
      }
      else {
        this.wire_forward = false;
      }
      if (initObj.hasOwnProperty('job_number')) {
        this.job_number = initObj.job_number
      }
      else {
        this.job_number = 0;
      }
      if (initObj.hasOwnProperty('program_number')) {
        this.program_number = initObj.program_number
      }
      else {
        this.program_number = 0;
      }
      if (initObj.hasOwnProperty('welding_simulation')) {
        this.welding_simulation = initObj.welding_simulation
      }
      else {
        this.welding_simulation = false;
      }
      if (initObj.hasOwnProperty('synchro_pulse_disable')) {
        this.synchro_pulse_disable = initObj.synchro_pulse_disable
      }
      else {
        this.synchro_pulse_disable = false;
      }
      if (initObj.hasOwnProperty('SFI_disable')) {
        this.SFI_disable = initObj.SFI_disable
      }
      else {
        this.SFI_disable = false;
      }
      if (initObj.hasOwnProperty('dynamic_correction_disable')) {
        this.dynamic_correction_disable = initObj.dynamic_correction_disable
      }
      else {
        this.dynamic_correction_disable = false;
      }
      if (initObj.hasOwnProperty('burn_back_disable')) {
        this.burn_back_disable = initObj.burn_back_disable
      }
      else {
        this.burn_back_disable = false;
      }
      if (initObj.hasOwnProperty('full_power_range')) {
        this.full_power_range = initObj.full_power_range
      }
      else {
        this.full_power_range = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FroniusCommand
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [power_set_value]
    bufferOffset = _serializer.float32(obj.power_set_value, buffer, bufferOffset);
    // Serialize message field [arc_length_correction]
    bufferOffset = _serializer.float32(obj.arc_length_correction, buffer, bufferOffset);
    // Serialize message field [dynamic_correction]
    bufferOffset = _serializer.float32(obj.dynamic_correction, buffer, bufferOffset);
    // Serialize message field [burn_back]
    bufferOffset = _serializer.float32(obj.burn_back, buffer, bufferOffset);
    // Serialize message field [welding_start]
    bufferOffset = _serializer.bool(obj.welding_start, buffer, bufferOffset);
    // Serialize message field [working_modes]
    bufferOffset = _serializer.uint8(obj.working_modes, buffer, bufferOffset);
    // Serialize message field [master_selection_twin]
    bufferOffset = _serializer.bool(obj.master_selection_twin, buffer, bufferOffset);
    // Serialize message field [gas_test]
    bufferOffset = _serializer.bool(obj.gas_test, buffer, bufferOffset);
    // Serialize message field [wire_forward]
    bufferOffset = _serializer.bool(obj.wire_forward, buffer, bufferOffset);
    // Serialize message field [job_number]
    bufferOffset = _serializer.uint8(obj.job_number, buffer, bufferOffset);
    // Serialize message field [program_number]
    bufferOffset = _serializer.uint8(obj.program_number, buffer, bufferOffset);
    // Serialize message field [welding_simulation]
    bufferOffset = _serializer.bool(obj.welding_simulation, buffer, bufferOffset);
    // Serialize message field [synchro_pulse_disable]
    bufferOffset = _serializer.bool(obj.synchro_pulse_disable, buffer, bufferOffset);
    // Serialize message field [SFI_disable]
    bufferOffset = _serializer.bool(obj.SFI_disable, buffer, bufferOffset);
    // Serialize message field [dynamic_correction_disable]
    bufferOffset = _serializer.bool(obj.dynamic_correction_disable, buffer, bufferOffset);
    // Serialize message field [burn_back_disable]
    bufferOffset = _serializer.bool(obj.burn_back_disable, buffer, bufferOffset);
    // Serialize message field [full_power_range]
    bufferOffset = _serializer.bool(obj.full_power_range, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FroniusCommand
    let len;
    let data = new FroniusCommand(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [power_set_value]
    data.power_set_value = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [arc_length_correction]
    data.arc_length_correction = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dynamic_correction]
    data.dynamic_correction = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [burn_back]
    data.burn_back = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [welding_start]
    data.welding_start = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [working_modes]
    data.working_modes = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [master_selection_twin]
    data.master_selection_twin = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [gas_test]
    data.gas_test = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wire_forward]
    data.wire_forward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [job_number]
    data.job_number = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [program_number]
    data.program_number = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [welding_simulation]
    data.welding_simulation = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [synchro_pulse_disable]
    data.synchro_pulse_disable = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [SFI_disable]
    data.SFI_disable = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [dynamic_correction_disable]
    data.dynamic_correction_disable = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [burn_back_disable]
    data.burn_back_disable = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [full_power_range]
    data.full_power_range = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 29;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kuka_rsi_msgs/FroniusCommand';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3db99eb4c29a0d366f39cbc70352a89a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FroniusCommand(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.power_set_value !== undefined) {
      resolved.power_set_value = msg.power_set_value;
    }
    else {
      resolved.power_set_value = 0.0
    }

    if (msg.arc_length_correction !== undefined) {
      resolved.arc_length_correction = msg.arc_length_correction;
    }
    else {
      resolved.arc_length_correction = 0.0
    }

    if (msg.dynamic_correction !== undefined) {
      resolved.dynamic_correction = msg.dynamic_correction;
    }
    else {
      resolved.dynamic_correction = 0.0
    }

    if (msg.burn_back !== undefined) {
      resolved.burn_back = msg.burn_back;
    }
    else {
      resolved.burn_back = 0.0
    }

    if (msg.welding_start !== undefined) {
      resolved.welding_start = msg.welding_start;
    }
    else {
      resolved.welding_start = false
    }

    if (msg.working_modes !== undefined) {
      resolved.working_modes = msg.working_modes;
    }
    else {
      resolved.working_modes = 0
    }

    if (msg.master_selection_twin !== undefined) {
      resolved.master_selection_twin = msg.master_selection_twin;
    }
    else {
      resolved.master_selection_twin = false
    }

    if (msg.gas_test !== undefined) {
      resolved.gas_test = msg.gas_test;
    }
    else {
      resolved.gas_test = false
    }

    if (msg.wire_forward !== undefined) {
      resolved.wire_forward = msg.wire_forward;
    }
    else {
      resolved.wire_forward = false
    }

    if (msg.job_number !== undefined) {
      resolved.job_number = msg.job_number;
    }
    else {
      resolved.job_number = 0
    }

    if (msg.program_number !== undefined) {
      resolved.program_number = msg.program_number;
    }
    else {
      resolved.program_number = 0
    }

    if (msg.welding_simulation !== undefined) {
      resolved.welding_simulation = msg.welding_simulation;
    }
    else {
      resolved.welding_simulation = false
    }

    if (msg.synchro_pulse_disable !== undefined) {
      resolved.synchro_pulse_disable = msg.synchro_pulse_disable;
    }
    else {
      resolved.synchro_pulse_disable = false
    }

    if (msg.SFI_disable !== undefined) {
      resolved.SFI_disable = msg.SFI_disable;
    }
    else {
      resolved.SFI_disable = false
    }

    if (msg.dynamic_correction_disable !== undefined) {
      resolved.dynamic_correction_disable = msg.dynamic_correction_disable;
    }
    else {
      resolved.dynamic_correction_disable = false
    }

    if (msg.burn_back_disable !== undefined) {
      resolved.burn_back_disable = msg.burn_back_disable;
    }
    else {
      resolved.burn_back_disable = false
    }

    if (msg.full_power_range !== undefined) {
      resolved.full_power_range = msg.full_power_range;
    }
    else {
      resolved.full_power_range = false
    }

    return resolved;
    }
};

module.exports = FroniusCommand;
