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

class Fronius500iCommand {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.wire_feed_speed_command_value = null;
      this.arc_length_correction = null;
      this.dynamic_correction = null;
      this.wire_retract_correction = null;
      this.welding_start = null;
      this.working_modes = null;
      this.gas_test = null;
      this.wire_forward = null;
      this.wire_backward = null;
      this.error_quit = null;
      this.touch_sensing = null;
      this.torch_blow_out = null;
      this.process_line_selection = null;
      this.welding_simulation = null;
      this.synchro_pulse_on = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('wire_feed_speed_command_value')) {
        this.wire_feed_speed_command_value = initObj.wire_feed_speed_command_value
      }
      else {
        this.wire_feed_speed_command_value = 0.0;
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
      if (initObj.hasOwnProperty('wire_retract_correction')) {
        this.wire_retract_correction = initObj.wire_retract_correction
      }
      else {
        this.wire_retract_correction = 0.0;
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
      if (initObj.hasOwnProperty('wire_backward')) {
        this.wire_backward = initObj.wire_backward
      }
      else {
        this.wire_backward = false;
      }
      if (initObj.hasOwnProperty('error_quit')) {
        this.error_quit = initObj.error_quit
      }
      else {
        this.error_quit = false;
      }
      if (initObj.hasOwnProperty('touch_sensing')) {
        this.touch_sensing = initObj.touch_sensing
      }
      else {
        this.touch_sensing = false;
      }
      if (initObj.hasOwnProperty('torch_blow_out')) {
        this.torch_blow_out = initObj.torch_blow_out
      }
      else {
        this.torch_blow_out = false;
      }
      if (initObj.hasOwnProperty('process_line_selection')) {
        this.process_line_selection = initObj.process_line_selection
      }
      else {
        this.process_line_selection = 0;
      }
      if (initObj.hasOwnProperty('welding_simulation')) {
        this.welding_simulation = initObj.welding_simulation
      }
      else {
        this.welding_simulation = false;
      }
      if (initObj.hasOwnProperty('synchro_pulse_on')) {
        this.synchro_pulse_on = initObj.synchro_pulse_on
      }
      else {
        this.synchro_pulse_on = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Fronius500iCommand
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [wire_feed_speed_command_value]
    bufferOffset = _serializer.float32(obj.wire_feed_speed_command_value, buffer, bufferOffset);
    // Serialize message field [arc_length_correction]
    bufferOffset = _serializer.float32(obj.arc_length_correction, buffer, bufferOffset);
    // Serialize message field [dynamic_correction]
    bufferOffset = _serializer.float32(obj.dynamic_correction, buffer, bufferOffset);
    // Serialize message field [wire_retract_correction]
    bufferOffset = _serializer.float32(obj.wire_retract_correction, buffer, bufferOffset);
    // Serialize message field [welding_start]
    bufferOffset = _serializer.bool(obj.welding_start, buffer, bufferOffset);
    // Serialize message field [working_modes]
    bufferOffset = _serializer.uint8(obj.working_modes, buffer, bufferOffset);
    // Serialize message field [gas_test]
    bufferOffset = _serializer.bool(obj.gas_test, buffer, bufferOffset);
    // Serialize message field [wire_forward]
    bufferOffset = _serializer.bool(obj.wire_forward, buffer, bufferOffset);
    // Serialize message field [wire_backward]
    bufferOffset = _serializer.bool(obj.wire_backward, buffer, bufferOffset);
    // Serialize message field [error_quit]
    bufferOffset = _serializer.bool(obj.error_quit, buffer, bufferOffset);
    // Serialize message field [touch_sensing]
    bufferOffset = _serializer.bool(obj.touch_sensing, buffer, bufferOffset);
    // Serialize message field [torch_blow_out]
    bufferOffset = _serializer.bool(obj.torch_blow_out, buffer, bufferOffset);
    // Serialize message field [process_line_selection]
    bufferOffset = _serializer.uint8(obj.process_line_selection, buffer, bufferOffset);
    // Serialize message field [welding_simulation]
    bufferOffset = _serializer.bool(obj.welding_simulation, buffer, bufferOffset);
    // Serialize message field [synchro_pulse_on]
    bufferOffset = _serializer.bool(obj.synchro_pulse_on, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Fronius500iCommand
    let len;
    let data = new Fronius500iCommand(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [wire_feed_speed_command_value]
    data.wire_feed_speed_command_value = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [arc_length_correction]
    data.arc_length_correction = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dynamic_correction]
    data.dynamic_correction = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [wire_retract_correction]
    data.wire_retract_correction = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [welding_start]
    data.welding_start = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [working_modes]
    data.working_modes = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gas_test]
    data.gas_test = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wire_forward]
    data.wire_forward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wire_backward]
    data.wire_backward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [error_quit]
    data.error_quit = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [touch_sensing]
    data.touch_sensing = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [torch_blow_out]
    data.torch_blow_out = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [process_line_selection]
    data.process_line_selection = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [welding_simulation]
    data.welding_simulation = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [synchro_pulse_on]
    data.synchro_pulse_on = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 27;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kuka_rsi_msgs/Fronius500iCommand';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a80028ec811c3f4ac2757241bd4475c6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Fronius500iCommand(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.wire_feed_speed_command_value !== undefined) {
      resolved.wire_feed_speed_command_value = msg.wire_feed_speed_command_value;
    }
    else {
      resolved.wire_feed_speed_command_value = 0.0
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

    if (msg.wire_retract_correction !== undefined) {
      resolved.wire_retract_correction = msg.wire_retract_correction;
    }
    else {
      resolved.wire_retract_correction = 0.0
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

    if (msg.wire_backward !== undefined) {
      resolved.wire_backward = msg.wire_backward;
    }
    else {
      resolved.wire_backward = false
    }

    if (msg.error_quit !== undefined) {
      resolved.error_quit = msg.error_quit;
    }
    else {
      resolved.error_quit = false
    }

    if (msg.touch_sensing !== undefined) {
      resolved.touch_sensing = msg.touch_sensing;
    }
    else {
      resolved.touch_sensing = false
    }

    if (msg.torch_blow_out !== undefined) {
      resolved.torch_blow_out = msg.torch_blow_out;
    }
    else {
      resolved.torch_blow_out = false
    }

    if (msg.process_line_selection !== undefined) {
      resolved.process_line_selection = msg.process_line_selection;
    }
    else {
      resolved.process_line_selection = 0
    }

    if (msg.welding_simulation !== undefined) {
      resolved.welding_simulation = msg.welding_simulation;
    }
    else {
      resolved.welding_simulation = false
    }

    if (msg.synchro_pulse_on !== undefined) {
      resolved.synchro_pulse_on = msg.synchro_pulse_on;
    }
    else {
      resolved.synchro_pulse_on = false
    }

    return resolved;
    }
};

module.exports = Fronius500iCommand;
