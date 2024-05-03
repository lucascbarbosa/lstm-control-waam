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

class PlasmaState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.Dinse_wire_feed_speed = null;
      this.EWM_voltage = null;
      this.EWM_current = null;
      this.EWM_wire_feed_speed = null;
      this.Dinse_wire_feeder_ready = null;
      this.Dinse_collective_fault = null;
      this.Dinse_wire_feed_fault = null;
      this.Dinse_power_failure = null;
      this.Dinse_positioning_fault = null;
      this.Dinse_hot_wire_fault = null;
      this.Dinse_life_bit = null;
      this.Dinse_current_on = null;
      this.Dinse_service_interval = null;
      this.Dinse_intern_fault = null;
      this.Dinse_emergency_stop = null;
      this.Dinse_gas_fault = null;
      this.Dinse_water_fault = null;
      this.Dinse_process_active = null;
      this.Dinse_wire_end = null;
      this.Dinse_wire_movement_on_stop = null;
      this.EWM_current_flows = null;
      this.EWM_ready_for_welding = null;
      this.EWM_sticking = null;
      this.EWM_error_1 = null;
      this.EWM_collision_signal = null;
      this.EWM_program_sequence_on_main_current = null;
      this.EWM_process_active = null;
      this.EWM_current_flows_aux_process = null;
      this.EWM_error_number = null;
      this.EWM_network_phases_status = null;
      this.EWM_user_defined_input_1 = null;
      this.EWM_no_external_stop_of_operation = null;
      this.EWM_user_defined_input_2 = null;
      this.EWM_wire_available = null;
      this.EWM_wirefeeder_ok = null;
      this.EWM_gas_ok = null;
      this.EWM_cooland_water_ok = null;
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
      if (initObj.hasOwnProperty('EWM_voltage')) {
        this.EWM_voltage = initObj.EWM_voltage
      }
      else {
        this.EWM_voltage = 0.0;
      }
      if (initObj.hasOwnProperty('EWM_current')) {
        this.EWM_current = initObj.EWM_current
      }
      else {
        this.EWM_current = 0.0;
      }
      if (initObj.hasOwnProperty('EWM_wire_feed_speed')) {
        this.EWM_wire_feed_speed = initObj.EWM_wire_feed_speed
      }
      else {
        this.EWM_wire_feed_speed = 0.0;
      }
      if (initObj.hasOwnProperty('Dinse_wire_feeder_ready')) {
        this.Dinse_wire_feeder_ready = initObj.Dinse_wire_feeder_ready
      }
      else {
        this.Dinse_wire_feeder_ready = false;
      }
      if (initObj.hasOwnProperty('Dinse_collective_fault')) {
        this.Dinse_collective_fault = initObj.Dinse_collective_fault
      }
      else {
        this.Dinse_collective_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_wire_feed_fault')) {
        this.Dinse_wire_feed_fault = initObj.Dinse_wire_feed_fault
      }
      else {
        this.Dinse_wire_feed_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_power_failure')) {
        this.Dinse_power_failure = initObj.Dinse_power_failure
      }
      else {
        this.Dinse_power_failure = false;
      }
      if (initObj.hasOwnProperty('Dinse_positioning_fault')) {
        this.Dinse_positioning_fault = initObj.Dinse_positioning_fault
      }
      else {
        this.Dinse_positioning_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_hot_wire_fault')) {
        this.Dinse_hot_wire_fault = initObj.Dinse_hot_wire_fault
      }
      else {
        this.Dinse_hot_wire_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_life_bit')) {
        this.Dinse_life_bit = initObj.Dinse_life_bit
      }
      else {
        this.Dinse_life_bit = false;
      }
      if (initObj.hasOwnProperty('Dinse_current_on')) {
        this.Dinse_current_on = initObj.Dinse_current_on
      }
      else {
        this.Dinse_current_on = false;
      }
      if (initObj.hasOwnProperty('Dinse_service_interval')) {
        this.Dinse_service_interval = initObj.Dinse_service_interval
      }
      else {
        this.Dinse_service_interval = false;
      }
      if (initObj.hasOwnProperty('Dinse_intern_fault')) {
        this.Dinse_intern_fault = initObj.Dinse_intern_fault
      }
      else {
        this.Dinse_intern_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_emergency_stop')) {
        this.Dinse_emergency_stop = initObj.Dinse_emergency_stop
      }
      else {
        this.Dinse_emergency_stop = false;
      }
      if (initObj.hasOwnProperty('Dinse_gas_fault')) {
        this.Dinse_gas_fault = initObj.Dinse_gas_fault
      }
      else {
        this.Dinse_gas_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_water_fault')) {
        this.Dinse_water_fault = initObj.Dinse_water_fault
      }
      else {
        this.Dinse_water_fault = false;
      }
      if (initObj.hasOwnProperty('Dinse_process_active')) {
        this.Dinse_process_active = initObj.Dinse_process_active
      }
      else {
        this.Dinse_process_active = false;
      }
      if (initObj.hasOwnProperty('Dinse_wire_end')) {
        this.Dinse_wire_end = initObj.Dinse_wire_end
      }
      else {
        this.Dinse_wire_end = false;
      }
      if (initObj.hasOwnProperty('Dinse_wire_movement_on_stop')) {
        this.Dinse_wire_movement_on_stop = initObj.Dinse_wire_movement_on_stop
      }
      else {
        this.Dinse_wire_movement_on_stop = false;
      }
      if (initObj.hasOwnProperty('EWM_current_flows')) {
        this.EWM_current_flows = initObj.EWM_current_flows
      }
      else {
        this.EWM_current_flows = false;
      }
      if (initObj.hasOwnProperty('EWM_ready_for_welding')) {
        this.EWM_ready_for_welding = initObj.EWM_ready_for_welding
      }
      else {
        this.EWM_ready_for_welding = false;
      }
      if (initObj.hasOwnProperty('EWM_sticking')) {
        this.EWM_sticking = initObj.EWM_sticking
      }
      else {
        this.EWM_sticking = false;
      }
      if (initObj.hasOwnProperty('EWM_error_1')) {
        this.EWM_error_1 = initObj.EWM_error_1
      }
      else {
        this.EWM_error_1 = false;
      }
      if (initObj.hasOwnProperty('EWM_collision_signal')) {
        this.EWM_collision_signal = initObj.EWM_collision_signal
      }
      else {
        this.EWM_collision_signal = false;
      }
      if (initObj.hasOwnProperty('EWM_program_sequence_on_main_current')) {
        this.EWM_program_sequence_on_main_current = initObj.EWM_program_sequence_on_main_current
      }
      else {
        this.EWM_program_sequence_on_main_current = false;
      }
      if (initObj.hasOwnProperty('EWM_process_active')) {
        this.EWM_process_active = initObj.EWM_process_active
      }
      else {
        this.EWM_process_active = false;
      }
      if (initObj.hasOwnProperty('EWM_current_flows_aux_process')) {
        this.EWM_current_flows_aux_process = initObj.EWM_current_flows_aux_process
      }
      else {
        this.EWM_current_flows_aux_process = false;
      }
      if (initObj.hasOwnProperty('EWM_error_number')) {
        this.EWM_error_number = initObj.EWM_error_number
      }
      else {
        this.EWM_error_number = 0;
      }
      if (initObj.hasOwnProperty('EWM_network_phases_status')) {
        this.EWM_network_phases_status = initObj.EWM_network_phases_status
      }
      else {
        this.EWM_network_phases_status = false;
      }
      if (initObj.hasOwnProperty('EWM_user_defined_input_1')) {
        this.EWM_user_defined_input_1 = initObj.EWM_user_defined_input_1
      }
      else {
        this.EWM_user_defined_input_1 = false;
      }
      if (initObj.hasOwnProperty('EWM_no_external_stop_of_operation')) {
        this.EWM_no_external_stop_of_operation = initObj.EWM_no_external_stop_of_operation
      }
      else {
        this.EWM_no_external_stop_of_operation = false;
      }
      if (initObj.hasOwnProperty('EWM_user_defined_input_2')) {
        this.EWM_user_defined_input_2 = initObj.EWM_user_defined_input_2
      }
      else {
        this.EWM_user_defined_input_2 = false;
      }
      if (initObj.hasOwnProperty('EWM_wire_available')) {
        this.EWM_wire_available = initObj.EWM_wire_available
      }
      else {
        this.EWM_wire_available = false;
      }
      if (initObj.hasOwnProperty('EWM_wirefeeder_ok')) {
        this.EWM_wirefeeder_ok = initObj.EWM_wirefeeder_ok
      }
      else {
        this.EWM_wirefeeder_ok = false;
      }
      if (initObj.hasOwnProperty('EWM_gas_ok')) {
        this.EWM_gas_ok = initObj.EWM_gas_ok
      }
      else {
        this.EWM_gas_ok = false;
      }
      if (initObj.hasOwnProperty('EWM_cooland_water_ok')) {
        this.EWM_cooland_water_ok = initObj.EWM_cooland_water_ok
      }
      else {
        this.EWM_cooland_water_ok = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PlasmaState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_feed_speed]
    bufferOffset = _serializer.float32(obj.Dinse_wire_feed_speed, buffer, bufferOffset);
    // Serialize message field [EWM_voltage]
    bufferOffset = _serializer.float32(obj.EWM_voltage, buffer, bufferOffset);
    // Serialize message field [EWM_current]
    bufferOffset = _serializer.float32(obj.EWM_current, buffer, bufferOffset);
    // Serialize message field [EWM_wire_feed_speed]
    bufferOffset = _serializer.float32(obj.EWM_wire_feed_speed, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_feeder_ready]
    bufferOffset = _serializer.bool(obj.Dinse_wire_feeder_ready, buffer, bufferOffset);
    // Serialize message field [Dinse_collective_fault]
    bufferOffset = _serializer.bool(obj.Dinse_collective_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_feed_fault]
    bufferOffset = _serializer.bool(obj.Dinse_wire_feed_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_power_failure]
    bufferOffset = _serializer.bool(obj.Dinse_power_failure, buffer, bufferOffset);
    // Serialize message field [Dinse_positioning_fault]
    bufferOffset = _serializer.bool(obj.Dinse_positioning_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_hot_wire_fault]
    bufferOffset = _serializer.bool(obj.Dinse_hot_wire_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_life_bit]
    bufferOffset = _serializer.bool(obj.Dinse_life_bit, buffer, bufferOffset);
    // Serialize message field [Dinse_current_on]
    bufferOffset = _serializer.bool(obj.Dinse_current_on, buffer, bufferOffset);
    // Serialize message field [Dinse_service_interval]
    bufferOffset = _serializer.bool(obj.Dinse_service_interval, buffer, bufferOffset);
    // Serialize message field [Dinse_intern_fault]
    bufferOffset = _serializer.bool(obj.Dinse_intern_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_emergency_stop]
    bufferOffset = _serializer.bool(obj.Dinse_emergency_stop, buffer, bufferOffset);
    // Serialize message field [Dinse_gas_fault]
    bufferOffset = _serializer.bool(obj.Dinse_gas_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_water_fault]
    bufferOffset = _serializer.bool(obj.Dinse_water_fault, buffer, bufferOffset);
    // Serialize message field [Dinse_process_active]
    bufferOffset = _serializer.bool(obj.Dinse_process_active, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_end]
    bufferOffset = _serializer.bool(obj.Dinse_wire_end, buffer, bufferOffset);
    // Serialize message field [Dinse_wire_movement_on_stop]
    bufferOffset = _serializer.bool(obj.Dinse_wire_movement_on_stop, buffer, bufferOffset);
    // Serialize message field [EWM_current_flows]
    bufferOffset = _serializer.bool(obj.EWM_current_flows, buffer, bufferOffset);
    // Serialize message field [EWM_ready_for_welding]
    bufferOffset = _serializer.bool(obj.EWM_ready_for_welding, buffer, bufferOffset);
    // Serialize message field [EWM_sticking]
    bufferOffset = _serializer.bool(obj.EWM_sticking, buffer, bufferOffset);
    // Serialize message field [EWM_error_1]
    bufferOffset = _serializer.bool(obj.EWM_error_1, buffer, bufferOffset);
    // Serialize message field [EWM_collision_signal]
    bufferOffset = _serializer.bool(obj.EWM_collision_signal, buffer, bufferOffset);
    // Serialize message field [EWM_program_sequence_on_main_current]
    bufferOffset = _serializer.bool(obj.EWM_program_sequence_on_main_current, buffer, bufferOffset);
    // Serialize message field [EWM_process_active]
    bufferOffset = _serializer.bool(obj.EWM_process_active, buffer, bufferOffset);
    // Serialize message field [EWM_current_flows_aux_process]
    bufferOffset = _serializer.bool(obj.EWM_current_flows_aux_process, buffer, bufferOffset);
    // Serialize message field [EWM_error_number]
    bufferOffset = _serializer.uint8(obj.EWM_error_number, buffer, bufferOffset);
    // Serialize message field [EWM_network_phases_status]
    bufferOffset = _serializer.bool(obj.EWM_network_phases_status, buffer, bufferOffset);
    // Serialize message field [EWM_user_defined_input_1]
    bufferOffset = _serializer.bool(obj.EWM_user_defined_input_1, buffer, bufferOffset);
    // Serialize message field [EWM_no_external_stop_of_operation]
    bufferOffset = _serializer.bool(obj.EWM_no_external_stop_of_operation, buffer, bufferOffset);
    // Serialize message field [EWM_user_defined_input_2]
    bufferOffset = _serializer.bool(obj.EWM_user_defined_input_2, buffer, bufferOffset);
    // Serialize message field [EWM_wire_available]
    bufferOffset = _serializer.bool(obj.EWM_wire_available, buffer, bufferOffset);
    // Serialize message field [EWM_wirefeeder_ok]
    bufferOffset = _serializer.bool(obj.EWM_wirefeeder_ok, buffer, bufferOffset);
    // Serialize message field [EWM_gas_ok]
    bufferOffset = _serializer.bool(obj.EWM_gas_ok, buffer, bufferOffset);
    // Serialize message field [EWM_cooland_water_ok]
    bufferOffset = _serializer.bool(obj.EWM_cooland_water_ok, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PlasmaState
    let len;
    let data = new PlasmaState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_feed_speed]
    data.Dinse_wire_feed_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [EWM_voltage]
    data.EWM_voltage = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [EWM_current]
    data.EWM_current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [EWM_wire_feed_speed]
    data.EWM_wire_feed_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_feeder_ready]
    data.Dinse_wire_feeder_ready = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_collective_fault]
    data.Dinse_collective_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_feed_fault]
    data.Dinse_wire_feed_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_power_failure]
    data.Dinse_power_failure = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_positioning_fault]
    data.Dinse_positioning_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_hot_wire_fault]
    data.Dinse_hot_wire_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_life_bit]
    data.Dinse_life_bit = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_current_on]
    data.Dinse_current_on = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_service_interval]
    data.Dinse_service_interval = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_intern_fault]
    data.Dinse_intern_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_emergency_stop]
    data.Dinse_emergency_stop = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_gas_fault]
    data.Dinse_gas_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_water_fault]
    data.Dinse_water_fault = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_process_active]
    data.Dinse_process_active = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_end]
    data.Dinse_wire_end = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Dinse_wire_movement_on_stop]
    data.Dinse_wire_movement_on_stop = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_current_flows]
    data.EWM_current_flows = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_ready_for_welding]
    data.EWM_ready_for_welding = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_sticking]
    data.EWM_sticking = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_error_1]
    data.EWM_error_1 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_collision_signal]
    data.EWM_collision_signal = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_program_sequence_on_main_current]
    data.EWM_program_sequence_on_main_current = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_process_active]
    data.EWM_process_active = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_current_flows_aux_process]
    data.EWM_current_flows_aux_process = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_error_number]
    data.EWM_error_number = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [EWM_network_phases_status]
    data.EWM_network_phases_status = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_user_defined_input_1]
    data.EWM_user_defined_input_1 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_no_external_stop_of_operation]
    data.EWM_no_external_stop_of_operation = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_user_defined_input_2]
    data.EWM_user_defined_input_2 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_wire_available]
    data.EWM_wire_available = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_wirefeeder_ok]
    data.EWM_wirefeeder_ok = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_gas_ok]
    data.EWM_gas_ok = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [EWM_cooland_water_ok]
    data.EWM_cooland_water_ok = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 49;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kuka_rsi_msgs/PlasmaState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '69caddae70f327bd935d395e65e0ca27';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    # Field 3-4
    float32 Dinse_wire_feed_speed
    # Field 8-9
    float32 EWM_voltage
    # Field 10-11
    float32 EWM_current
    # Field 12-13
    float32 EWM_wire_feed_speed
    # Field 1
    bool Dinse_wire_feeder_ready
    bool Dinse_collective_fault
    bool Dinse_wire_feed_fault
    bool Dinse_power_failure
    bool Dinse_positioning_fault
    bool Dinse_hot_wire_fault
    bool Dinse_life_bit
    bool Dinse_current_on
    # Field 2
    bool Dinse_service_interval
    bool Dinse_intern_fault
    bool Dinse_emergency_stop
    bool Dinse_gas_fault
    bool Dinse_water_fault
    bool Dinse_process_active
    bool Dinse_wire_end
    bool Dinse_wire_movement_on_stop
    # Field 5
    bool EWM_current_flows
    bool EWM_ready_for_welding
    bool EWM_sticking
    bool EWM_error_1
    bool EWM_collision_signal
    bool EWM_program_sequence_on_main_current
    bool EWM_process_active
    bool EWM_current_flows_aux_process
    # Field 6
    uint8 EWM_error_number
    # Field 7
    bool EWM_network_phases_status
    bool EWM_user_defined_input_1
    bool EWM_no_external_stop_of_operation
    bool EWM_user_defined_input_2
    bool EWM_wire_available
    bool EWM_wirefeeder_ok
    bool EWM_gas_ok
    bool EWM_cooland_water_ok
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
    const resolved = new PlasmaState(null);
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

    if (msg.EWM_voltage !== undefined) {
      resolved.EWM_voltage = msg.EWM_voltage;
    }
    else {
      resolved.EWM_voltage = 0.0
    }

    if (msg.EWM_current !== undefined) {
      resolved.EWM_current = msg.EWM_current;
    }
    else {
      resolved.EWM_current = 0.0
    }

    if (msg.EWM_wire_feed_speed !== undefined) {
      resolved.EWM_wire_feed_speed = msg.EWM_wire_feed_speed;
    }
    else {
      resolved.EWM_wire_feed_speed = 0.0
    }

    if (msg.Dinse_wire_feeder_ready !== undefined) {
      resolved.Dinse_wire_feeder_ready = msg.Dinse_wire_feeder_ready;
    }
    else {
      resolved.Dinse_wire_feeder_ready = false
    }

    if (msg.Dinse_collective_fault !== undefined) {
      resolved.Dinse_collective_fault = msg.Dinse_collective_fault;
    }
    else {
      resolved.Dinse_collective_fault = false
    }

    if (msg.Dinse_wire_feed_fault !== undefined) {
      resolved.Dinse_wire_feed_fault = msg.Dinse_wire_feed_fault;
    }
    else {
      resolved.Dinse_wire_feed_fault = false
    }

    if (msg.Dinse_power_failure !== undefined) {
      resolved.Dinse_power_failure = msg.Dinse_power_failure;
    }
    else {
      resolved.Dinse_power_failure = false
    }

    if (msg.Dinse_positioning_fault !== undefined) {
      resolved.Dinse_positioning_fault = msg.Dinse_positioning_fault;
    }
    else {
      resolved.Dinse_positioning_fault = false
    }

    if (msg.Dinse_hot_wire_fault !== undefined) {
      resolved.Dinse_hot_wire_fault = msg.Dinse_hot_wire_fault;
    }
    else {
      resolved.Dinse_hot_wire_fault = false
    }

    if (msg.Dinse_life_bit !== undefined) {
      resolved.Dinse_life_bit = msg.Dinse_life_bit;
    }
    else {
      resolved.Dinse_life_bit = false
    }

    if (msg.Dinse_current_on !== undefined) {
      resolved.Dinse_current_on = msg.Dinse_current_on;
    }
    else {
      resolved.Dinse_current_on = false
    }

    if (msg.Dinse_service_interval !== undefined) {
      resolved.Dinse_service_interval = msg.Dinse_service_interval;
    }
    else {
      resolved.Dinse_service_interval = false
    }

    if (msg.Dinse_intern_fault !== undefined) {
      resolved.Dinse_intern_fault = msg.Dinse_intern_fault;
    }
    else {
      resolved.Dinse_intern_fault = false
    }

    if (msg.Dinse_emergency_stop !== undefined) {
      resolved.Dinse_emergency_stop = msg.Dinse_emergency_stop;
    }
    else {
      resolved.Dinse_emergency_stop = false
    }

    if (msg.Dinse_gas_fault !== undefined) {
      resolved.Dinse_gas_fault = msg.Dinse_gas_fault;
    }
    else {
      resolved.Dinse_gas_fault = false
    }

    if (msg.Dinse_water_fault !== undefined) {
      resolved.Dinse_water_fault = msg.Dinse_water_fault;
    }
    else {
      resolved.Dinse_water_fault = false
    }

    if (msg.Dinse_process_active !== undefined) {
      resolved.Dinse_process_active = msg.Dinse_process_active;
    }
    else {
      resolved.Dinse_process_active = false
    }

    if (msg.Dinse_wire_end !== undefined) {
      resolved.Dinse_wire_end = msg.Dinse_wire_end;
    }
    else {
      resolved.Dinse_wire_end = false
    }

    if (msg.Dinse_wire_movement_on_stop !== undefined) {
      resolved.Dinse_wire_movement_on_stop = msg.Dinse_wire_movement_on_stop;
    }
    else {
      resolved.Dinse_wire_movement_on_stop = false
    }

    if (msg.EWM_current_flows !== undefined) {
      resolved.EWM_current_flows = msg.EWM_current_flows;
    }
    else {
      resolved.EWM_current_flows = false
    }

    if (msg.EWM_ready_for_welding !== undefined) {
      resolved.EWM_ready_for_welding = msg.EWM_ready_for_welding;
    }
    else {
      resolved.EWM_ready_for_welding = false
    }

    if (msg.EWM_sticking !== undefined) {
      resolved.EWM_sticking = msg.EWM_sticking;
    }
    else {
      resolved.EWM_sticking = false
    }

    if (msg.EWM_error_1 !== undefined) {
      resolved.EWM_error_1 = msg.EWM_error_1;
    }
    else {
      resolved.EWM_error_1 = false
    }

    if (msg.EWM_collision_signal !== undefined) {
      resolved.EWM_collision_signal = msg.EWM_collision_signal;
    }
    else {
      resolved.EWM_collision_signal = false
    }

    if (msg.EWM_program_sequence_on_main_current !== undefined) {
      resolved.EWM_program_sequence_on_main_current = msg.EWM_program_sequence_on_main_current;
    }
    else {
      resolved.EWM_program_sequence_on_main_current = false
    }

    if (msg.EWM_process_active !== undefined) {
      resolved.EWM_process_active = msg.EWM_process_active;
    }
    else {
      resolved.EWM_process_active = false
    }

    if (msg.EWM_current_flows_aux_process !== undefined) {
      resolved.EWM_current_flows_aux_process = msg.EWM_current_flows_aux_process;
    }
    else {
      resolved.EWM_current_flows_aux_process = false
    }

    if (msg.EWM_error_number !== undefined) {
      resolved.EWM_error_number = msg.EWM_error_number;
    }
    else {
      resolved.EWM_error_number = 0
    }

    if (msg.EWM_network_phases_status !== undefined) {
      resolved.EWM_network_phases_status = msg.EWM_network_phases_status;
    }
    else {
      resolved.EWM_network_phases_status = false
    }

    if (msg.EWM_user_defined_input_1 !== undefined) {
      resolved.EWM_user_defined_input_1 = msg.EWM_user_defined_input_1;
    }
    else {
      resolved.EWM_user_defined_input_1 = false
    }

    if (msg.EWM_no_external_stop_of_operation !== undefined) {
      resolved.EWM_no_external_stop_of_operation = msg.EWM_no_external_stop_of_operation;
    }
    else {
      resolved.EWM_no_external_stop_of_operation = false
    }

    if (msg.EWM_user_defined_input_2 !== undefined) {
      resolved.EWM_user_defined_input_2 = msg.EWM_user_defined_input_2;
    }
    else {
      resolved.EWM_user_defined_input_2 = false
    }

    if (msg.EWM_wire_available !== undefined) {
      resolved.EWM_wire_available = msg.EWM_wire_available;
    }
    else {
      resolved.EWM_wire_available = false
    }

    if (msg.EWM_wirefeeder_ok !== undefined) {
      resolved.EWM_wirefeeder_ok = msg.EWM_wirefeeder_ok;
    }
    else {
      resolved.EWM_wirefeeder_ok = false
    }

    if (msg.EWM_gas_ok !== undefined) {
      resolved.EWM_gas_ok = msg.EWM_gas_ok;
    }
    else {
      resolved.EWM_gas_ok = false
    }

    if (msg.EWM_cooland_water_ok !== undefined) {
      resolved.EWM_cooland_water_ok = msg.EWM_cooland_water_ok;
    }
    else {
      resolved.EWM_cooland_water_ok = false
    }

    return resolved;
    }
};

module.exports = PlasmaState;
