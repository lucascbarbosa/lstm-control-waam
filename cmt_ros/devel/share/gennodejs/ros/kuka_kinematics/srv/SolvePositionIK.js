// Auto-generated. Do not edit!

// (in-package kuka_kinematics.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SolvePositionIKRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pose_stamp = null;
      this.seed_angles = null;
      this.seed_mode = null;
    }
    else {
      if (initObj.hasOwnProperty('pose_stamp')) {
        this.pose_stamp = initObj.pose_stamp
      }
      else {
        this.pose_stamp = new geometry_msgs.msg.PoseStamped();
      }
      if (initObj.hasOwnProperty('seed_angles')) {
        this.seed_angles = initObj.seed_angles
      }
      else {
        this.seed_angles = new sensor_msgs.msg.JointState();
      }
      if (initObj.hasOwnProperty('seed_mode')) {
        this.seed_mode = initObj.seed_mode
      }
      else {
        this.seed_mode = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SolvePositionIKRequest
    // Serialize message field [pose_stamp]
    bufferOffset = geometry_msgs.msg.PoseStamped.serialize(obj.pose_stamp, buffer, bufferOffset);
    // Serialize message field [seed_angles]
    bufferOffset = sensor_msgs.msg.JointState.serialize(obj.seed_angles, buffer, bufferOffset);
    // Serialize message field [seed_mode]
    bufferOffset = _serializer.uint8(obj.seed_mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SolvePositionIKRequest
    let len;
    let data = new SolvePositionIKRequest(null);
    // Deserialize message field [pose_stamp]
    data.pose_stamp = geometry_msgs.msg.PoseStamped.deserialize(buffer, bufferOffset);
    // Deserialize message field [seed_angles]
    data.seed_angles = sensor_msgs.msg.JointState.deserialize(buffer, bufferOffset);
    // Deserialize message field [seed_mode]
    data.seed_mode = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += geometry_msgs.msg.PoseStamped.getMessageSize(object.pose_stamp);
    length += sensor_msgs.msg.JointState.getMessageSize(object.seed_angles);
    return length + 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'kuka_kinematics/SolvePositionIKRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2587e42983d0081d0a2288230991073b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Endpoint Pose(s) to request Inverse-Kinematics joint solutions for.
    geometry_msgs/PoseStamped pose_stamp
    
    # (optional) Joint Angle Seed(s) for IK solver.
    # * specify a JointState seed for each pose_stamp, using name[] and position[]
    # * empty arrays or a non-default seed_mode will cause user seed to not be used
    sensor_msgs/JointState seed_angles
    
    # Seed Type Mode
    # * default (SEED_AUTO) mode: iterate through seed types until first valid
    #                             solution is found
    # * setting any other mode:   try only that seed type
    uint8 SEED_AUTO    = 0
    uint8 SEED_USER    = 1
    uint8 SEED_CURRENT = 2
    uint8 SEED_NS_MAP  = 3
    
    uint8 seed_mode
    
    ================================================================================
    MSG: geometry_msgs/PoseStamped
    # A Pose with reference coordinate frame and timestamp
    Header header
    Pose pose
    
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
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    ================================================================================
    MSG: sensor_msgs/JointState
    # This is a message that holds data to describe the state of a set of torque controlled joints. 
    #
    # The state of each joint (revolute or prismatic) is defined by:
    #  * the position of the joint (rad or m),
    #  * the velocity of the joint (rad/s or m/s) and 
    #  * the effort that is applied in the joint (Nm or N).
    #
    # Each joint is uniquely identified by its name
    # The header specifies the time at which the joint states were recorded. All the joint states
    # in one message have to be recorded at the same time.
    #
    # This message consists of a multiple arrays, one for each part of the joint state. 
    # The goal is to make each of the fields optional. When e.g. your joints have no
    # effort associated with them, you can leave the effort array empty. 
    #
    # All arrays in this message should have the same size, or be empty.
    # This is the only way to uniquely associate the joint name with the correct
    # states.
    
    
    Header header
    
    string[] name
    float64[] position
    float64[] velocity
    float64[] effort
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SolvePositionIKRequest(null);
    if (msg.pose_stamp !== undefined) {
      resolved.pose_stamp = geometry_msgs.msg.PoseStamped.Resolve(msg.pose_stamp)
    }
    else {
      resolved.pose_stamp = new geometry_msgs.msg.PoseStamped()
    }

    if (msg.seed_angles !== undefined) {
      resolved.seed_angles = sensor_msgs.msg.JointState.Resolve(msg.seed_angles)
    }
    else {
      resolved.seed_angles = new sensor_msgs.msg.JointState()
    }

    if (msg.seed_mode !== undefined) {
      resolved.seed_mode = msg.seed_mode;
    }
    else {
      resolved.seed_mode = 0
    }

    return resolved;
    }
};

// Constants for message
SolvePositionIKRequest.Constants = {
  SEED_AUTO: 0,
  SEED_USER: 1,
  SEED_CURRENT: 2,
  SEED_NS_MAP: 3,
}

class SolvePositionIKResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.joints = null;
      this.isValid = null;
      this.result_type = null;
    }
    else {
      if (initObj.hasOwnProperty('joints')) {
        this.joints = initObj.joints
      }
      else {
        this.joints = new sensor_msgs.msg.JointState();
      }
      if (initObj.hasOwnProperty('isValid')) {
        this.isValid = initObj.isValid
      }
      else {
        this.isValid = false;
      }
      if (initObj.hasOwnProperty('result_type')) {
        this.result_type = initObj.result_type
      }
      else {
        this.result_type = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SolvePositionIKResponse
    // Serialize message field [joints]
    bufferOffset = sensor_msgs.msg.JointState.serialize(obj.joints, buffer, bufferOffset);
    // Serialize message field [isValid]
    bufferOffset = _serializer.bool(obj.isValid, buffer, bufferOffset);
    // Serialize message field [result_type]
    bufferOffset = _serializer.uint8(obj.result_type, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SolvePositionIKResponse
    let len;
    let data = new SolvePositionIKResponse(null);
    // Deserialize message field [joints]
    data.joints = sensor_msgs.msg.JointState.deserialize(buffer, bufferOffset);
    // Deserialize message field [isValid]
    data.isValid = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [result_type]
    data.result_type = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.JointState.getMessageSize(object.joints);
    return length + 2;
  }

  static datatype() {
    // Returns string type for a service object
    return 'kuka_kinematics/SolvePositionIKResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c12d9f771bb138ce4b4650d1b2f8aa4f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # joints[i]      == joint angle solution for each pose_state[i]
    sensor_msgs/JointState joints
    
    # NOTE: isValid will be deprecated by result_type in future versions
    bool isValid
    
    # result_type[i] == seed type used to find valid solution, joints[i];
    # otherwise,     == RESULT_INVALID (no valid solution found).
    uint8 RESULT_INVALID = 0
    uint8 result_type
    
    
    ================================================================================
    MSG: sensor_msgs/JointState
    # This is a message that holds data to describe the state of a set of torque controlled joints. 
    #
    # The state of each joint (revolute or prismatic) is defined by:
    #  * the position of the joint (rad or m),
    #  * the velocity of the joint (rad/s or m/s) and 
    #  * the effort that is applied in the joint (Nm or N).
    #
    # Each joint is uniquely identified by its name
    # The header specifies the time at which the joint states were recorded. All the joint states
    # in one message have to be recorded at the same time.
    #
    # This message consists of a multiple arrays, one for each part of the joint state. 
    # The goal is to make each of the fields optional. When e.g. your joints have no
    # effort associated with them, you can leave the effort array empty. 
    #
    # All arrays in this message should have the same size, or be empty.
    # This is the only way to uniquely associate the joint name with the correct
    # states.
    
    
    Header header
    
    string[] name
    float64[] position
    float64[] velocity
    float64[] effort
    
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
    const resolved = new SolvePositionIKResponse(null);
    if (msg.joints !== undefined) {
      resolved.joints = sensor_msgs.msg.JointState.Resolve(msg.joints)
    }
    else {
      resolved.joints = new sensor_msgs.msg.JointState()
    }

    if (msg.isValid !== undefined) {
      resolved.isValid = msg.isValid;
    }
    else {
      resolved.isValid = false
    }

    if (msg.result_type !== undefined) {
      resolved.result_type = msg.result_type;
    }
    else {
      resolved.result_type = 0
    }

    return resolved;
    }
};

// Constants for message
SolvePositionIKResponse.Constants = {
  RESULT_INVALID: 0,
}

module.exports = {
  Request: SolvePositionIKRequest,
  Response: SolvePositionIKResponse,
  md5sum() { return '0b2822586a12e4c26260aa39340340f7'; },
  datatype() { return 'kuka_kinematics/SolvePositionIK'; }
};
