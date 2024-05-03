// Auto-generated. Do not edit!

// (in-package hks_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class HksState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.current = null;
      this.voltage = null;
      this.gasflow1 = null;
      this.gasflow2 = null;
      this.wfs1 = null;
      this.wfs2 = null;
      this.temperature1 = null;
      this.temperature2 = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('current')) {
        this.current = initObj.current
      }
      else {
        this.current = 0.0;
      }
      if (initObj.hasOwnProperty('voltage')) {
        this.voltage = initObj.voltage
      }
      else {
        this.voltage = 0.0;
      }
      if (initObj.hasOwnProperty('gasflow1')) {
        this.gasflow1 = initObj.gasflow1
      }
      else {
        this.gasflow1 = 0.0;
      }
      if (initObj.hasOwnProperty('gasflow2')) {
        this.gasflow2 = initObj.gasflow2
      }
      else {
        this.gasflow2 = 0.0;
      }
      if (initObj.hasOwnProperty('wfs1')) {
        this.wfs1 = initObj.wfs1
      }
      else {
        this.wfs1 = 0.0;
      }
      if (initObj.hasOwnProperty('wfs2')) {
        this.wfs2 = initObj.wfs2
      }
      else {
        this.wfs2 = 0.0;
      }
      if (initObj.hasOwnProperty('temperature1')) {
        this.temperature1 = initObj.temperature1
      }
      else {
        this.temperature1 = 0.0;
      }
      if (initObj.hasOwnProperty('temperature2')) {
        this.temperature2 = initObj.temperature2
      }
      else {
        this.temperature2 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HksState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [current]
    bufferOffset = _serializer.float64(obj.current, buffer, bufferOffset);
    // Serialize message field [voltage]
    bufferOffset = _serializer.float64(obj.voltage, buffer, bufferOffset);
    // Serialize message field [gasflow1]
    bufferOffset = _serializer.float64(obj.gasflow1, buffer, bufferOffset);
    // Serialize message field [gasflow2]
    bufferOffset = _serializer.float64(obj.gasflow2, buffer, bufferOffset);
    // Serialize message field [wfs1]
    bufferOffset = _serializer.float64(obj.wfs1, buffer, bufferOffset);
    // Serialize message field [wfs2]
    bufferOffset = _serializer.float64(obj.wfs2, buffer, bufferOffset);
    // Serialize message field [temperature1]
    bufferOffset = _serializer.float64(obj.temperature1, buffer, bufferOffset);
    // Serialize message field [temperature2]
    bufferOffset = _serializer.float64(obj.temperature2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HksState
    let len;
    let data = new HksState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [current]
    data.current = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [voltage]
    data.voltage = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gasflow1]
    data.gasflow1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gasflow2]
    data.gasflow2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [wfs1]
    data.wfs1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [wfs2]
    data.wfs2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [temperature1]
    data.temperature1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [temperature2]
    data.temperature2 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 64;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hks_msgs/HksState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '590c9f90019cd2bcb973006760e63ddd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HksState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.current !== undefined) {
      resolved.current = msg.current;
    }
    else {
      resolved.current = 0.0
    }

    if (msg.voltage !== undefined) {
      resolved.voltage = msg.voltage;
    }
    else {
      resolved.voltage = 0.0
    }

    if (msg.gasflow1 !== undefined) {
      resolved.gasflow1 = msg.gasflow1;
    }
    else {
      resolved.gasflow1 = 0.0
    }

    if (msg.gasflow2 !== undefined) {
      resolved.gasflow2 = msg.gasflow2;
    }
    else {
      resolved.gasflow2 = 0.0
    }

    if (msg.wfs1 !== undefined) {
      resolved.wfs1 = msg.wfs1;
    }
    else {
      resolved.wfs1 = 0.0
    }

    if (msg.wfs2 !== undefined) {
      resolved.wfs2 = msg.wfs2;
    }
    else {
      resolved.wfs2 = 0.0
    }

    if (msg.temperature1 !== undefined) {
      resolved.temperature1 = msg.temperature1;
    }
    else {
      resolved.temperature1 = 0.0
    }

    if (msg.temperature2 !== undefined) {
      resolved.temperature2 = msg.temperature2;
    }
    else {
      resolved.temperature2 = 0.0
    }

    return resolved;
    }
};

module.exports = HksState;
