callback_classes = [
    ['ns3::ObjectBase *', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['bool', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['bool', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'const ns3::Address &', 'ns3::NetDevice::PacketType', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::ArpCache>', 'ns3::Ipv4Address', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'const ns3::Address &', 'ns3::NetDevice::PacketType', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::NetDevice>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::Ipv4Address', 'ns3::Ipv4Address', 'unsigned char', 'ns3::Ptr<ns3::Ipv4Route>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::Ipv6Address', 'ns3::Ipv6Address', 'unsigned char', 'ns3::Ptr<ns3::Ipv6Route>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Socket>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['bool', 'ns3::Ptr<ns3::Socket>', 'const ns3::Address &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Socket>', 'const ns3::Address &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Socket>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv4Header &', 'ns3::Ptr<const ns3::Packet>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ptr<ns3::Ipv4>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv4Header &', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ipv4L3Protocol::DropReason', 'ns3::Ptr<ns3::Ipv4>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ptr<ns3::Ipv6>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv6Header &', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ipv6L3Protocol::DropReason', 'ns3::Ptr<ns3::Ipv6>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv6Header &', 'ns3::Ptr<const ns3::Packet>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'std::basic_string<char>', 'ns3::Ptr<const ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned int', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::TcpSocketState::TcpCongState_t', 'ns3::TcpSocketState::TcpCongState_t', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::SequenceNumber<unsigned int, int>', 'ns3::SequenceNumber<unsigned int, int>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Time', 'ns3::Time', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'double', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ipv4Address', 'unsigned char', 'unsigned char', 'unsigned char', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ipv6Address', 'unsigned char', 'unsigned char', 'unsigned char', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::TcpSocket::TcpStates_t', 'ns3::TcpSocket::TcpStates_t', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'const ns3::TcpHeader &', 'ns3::Ptr<const ns3::TcpSocketBase>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
]
