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

class TpsState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.IRdif = null;
      this.IRpos = null;
      this.IRmaxTemp = null;
      this.IRwidth = null;
      this.IRirreg = null;
      this.IRsymet = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('IRdif')) {
        this.IRdif = initObj.IRdif
      }
      else {
        this.IRdif = 0.0;
      }
      if (initObj.hasOwnProperty('IRpos')) {
        this.IRpos = initObj.IRpos
      }
      else {
        this.IRpos = 0.0;
      }
      if (initObj.hasOwnProperty('IRmaxTemp')) {
        this.IRmaxTemp = initObj.IRmaxTemp
      }
      else {
        this.IRmaxTemp = 0.0;
      }
      if (initObj.hasOwnProperty('IRwidth')) {
        this.IRwidth = initObj.IRwidth
      }
      else {
        this.IRwidth = 0.0;
      }
      if (initObj.hasOwnProperty('IRirreg')) {
        this.IRirreg = initObj.IRirreg
      }
      else {
        this.IRirreg = 0.0;
      }
      if (initObj.hasOwnProperty('IRsymet')) {
        this.IRsymet = initObj.IRsymet
      }
      else {
        this.IRsymet = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TpsState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [IRdif]
    bufferOffset = _serializer.float64(obj.IRdif, buffer, bufferOffset);
    // Serialize message field [IRpos]
    bufferOffset = _serializer.float64(obj.IRpos, buffer, bufferOffset);
    // Serialize message field [IRmaxTemp]
    bufferOffset = _serializer.float64(obj.IRmaxTemp, buffer, bufferOffset);
    // Serialize message field [IRwidth]
    bufferOffset = _serializer.float64(obj.IRwidth, buffer, bufferOffset);
    // Serialize message field [IRirreg]
    bufferOffset = _serializer.float64(obj.IRirreg, buffer, bufferOffset);
    // Serialize message field [IRsymet]
    bufferOffset = _serializer.float64(obj.IRsymet, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TpsState
    let len;
    let data = new TpsState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [IRdif]
    data.IRdif = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [IRpos]
    data.IRpos = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [IRmaxTemp]
    data.IRmaxTemp = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [IRwidth]
    data.IRwidth = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [IRirreg]
    data.IRirreg = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [IRsymet]
    data.IRsymet = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hks_msgs/TpsState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1d051352653a4f46732676ac4e695c1f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TpsState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.IRdif !== undefined) {
      resolved.IRdif = msg.IRdif;
    }
    else {
      resolved.IRdif = 0.0
    }

    if (msg.IRpos !== undefined) {
      resolved.IRpos = msg.IRpos;
    }
    else {
      resolved.IRpos = 0.0
    }

    if (msg.IRmaxTemp !== undefined) {
      resolved.IRmaxTemp = msg.IRmaxTemp;
    }
    else {
      resolved.IRmaxTemp = 0.0
    }

    if (msg.IRwidth !== undefined) {
      resolved.IRwidth = msg.IRwidth;
    }
    else {
      resolved.IRwidth = 0.0
    }

    if (msg.IRirreg !== undefined) {
      resolved.IRirreg = msg.IRirreg;
    }
    else {
      resolved.IRirreg = 0.0
    }

    if (msg.IRsymet !== undefined) {
      resolved.IRsymet = msg.IRsymet;
    }
    else {
      resolved.IRsymet = 0.0
    }

    return resolved;
    }
};

module.exports = TpsState;
