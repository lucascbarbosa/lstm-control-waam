// Generated by gencpp from file hks_msgs/HksState.msg
// DO NOT EDIT!


#ifndef HKS_MSGS_MESSAGE_HKSSTATE_H
#define HKS_MSGS_MESSAGE_HKSSTATE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace hks_msgs
{
template <class ContainerAllocator>
struct HksState_
{
  typedef HksState_<ContainerAllocator> Type;

  HksState_()
    : header()
    , current(0.0)
    , voltage(0.0)
    , gasflow1(0.0)
    , gasflow2(0.0)
    , wfs1(0.0)
    , wfs2(0.0)
    , temperature1(0.0)
    , temperature2(0.0)  {
    }
  HksState_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , current(0.0)
    , voltage(0.0)
    , gasflow1(0.0)
    , gasflow2(0.0)
    , wfs1(0.0)
    , wfs2(0.0)
    , temperature1(0.0)
    , temperature2(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef double _current_type;
  _current_type current;

   typedef double _voltage_type;
  _voltage_type voltage;

   typedef double _gasflow1_type;
  _gasflow1_type gasflow1;

   typedef double _gasflow2_type;
  _gasflow2_type gasflow2;

   typedef double _wfs1_type;
  _wfs1_type wfs1;

   typedef double _wfs2_type;
  _wfs2_type wfs2;

   typedef double _temperature1_type;
  _temperature1_type temperature1;

   typedef double _temperature2_type;
  _temperature2_type temperature2;





  typedef boost::shared_ptr< ::hks_msgs::HksState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::hks_msgs::HksState_<ContainerAllocator> const> ConstPtr;

}; // struct HksState_

typedef ::hks_msgs::HksState_<std::allocator<void> > HksState;

typedef boost::shared_ptr< ::hks_msgs::HksState > HksStatePtr;
typedef boost::shared_ptr< ::hks_msgs::HksState const> HksStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::hks_msgs::HksState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::hks_msgs::HksState_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::hks_msgs::HksState_<ContainerAllocator1> & lhs, const ::hks_msgs::HksState_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.current == rhs.current &&
    lhs.voltage == rhs.voltage &&
    lhs.gasflow1 == rhs.gasflow1 &&
    lhs.gasflow2 == rhs.gasflow2 &&
    lhs.wfs1 == rhs.wfs1 &&
    lhs.wfs2 == rhs.wfs2 &&
    lhs.temperature1 == rhs.temperature1 &&
    lhs.temperature2 == rhs.temperature2;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::hks_msgs::HksState_<ContainerAllocator1> & lhs, const ::hks_msgs::HksState_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace hks_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::hks_msgs::HksState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hks_msgs::HksState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hks_msgs::HksState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hks_msgs::HksState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hks_msgs::HksState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hks_msgs::HksState_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::hks_msgs::HksState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "590c9f90019cd2bcb973006760e63ddd";
  }

  static const char* value(const ::hks_msgs::HksState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x590c9f90019cd2bcULL;
  static const uint64_t static_value2 = 0xb973006760e63dddULL;
};

template<class ContainerAllocator>
struct DataType< ::hks_msgs::HksState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "hks_msgs/HksState";
  }

  static const char* value(const ::hks_msgs::HksState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::hks_msgs::HksState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"#\n"
"float64 current\n"
"float64 voltage\n"
"#\n"
"float64 gasflow1\n"
"float64 gasflow2\n"
"#\n"
"float64 wfs1\n"
"float64 wfs2\n"
"#\n"
"float64 temperature1\n"
"float64 temperature2\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::hks_msgs::HksState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::hks_msgs::HksState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.current);
      stream.next(m.voltage);
      stream.next(m.gasflow1);
      stream.next(m.gasflow2);
      stream.next(m.wfs1);
      stream.next(m.wfs2);
      stream.next(m.temperature1);
      stream.next(m.temperature2);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct HksState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::hks_msgs::HksState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::hks_msgs::HksState_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "current: ";
    Printer<double>::stream(s, indent + "  ", v.current);
    s << indent << "voltage: ";
    Printer<double>::stream(s, indent + "  ", v.voltage);
    s << indent << "gasflow1: ";
    Printer<double>::stream(s, indent + "  ", v.gasflow1);
    s << indent << "gasflow2: ";
    Printer<double>::stream(s, indent + "  ", v.gasflow2);
    s << indent << "wfs1: ";
    Printer<double>::stream(s, indent + "  ", v.wfs1);
    s << indent << "wfs2: ";
    Printer<double>::stream(s, indent + "  ", v.wfs2);
    s << indent << "temperature1: ";
    Printer<double>::stream(s, indent + "  ", v.temperature1);
    s << indent << "temperature2: ";
    Printer<double>::stream(s, indent + "  ", v.temperature2);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HKS_MSGS_MESSAGE_HKSSTATE_H
