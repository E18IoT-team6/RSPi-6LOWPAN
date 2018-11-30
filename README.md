# How to do

### D-link Address

__RSP-sink__
192.168.0.138

__RSP-client__
192.168.0.198


## wpan-tools


https://github.com/linux-wpan/wpan-tools.git

## Set up networks

At the __RSP-sink__

```bash
# Check current networks
ip addr show

# Bring lowpa0 and wpan0 offline
sudo ip link set lowpan0 down   
sudo ip link set wpan0 down

# Set the personal area network(PAN) wpan with the pan_id 0xabcd
sudo iwpan dev wpan0 set pan_id 0xabcd

# Set up the channel
# Not working
# sudo iwpan phy0 set channel 0 26            

# Set up the ip
sudo ip addr add 2001:db8::1/64 dev lowpan0

# Set up the interface
sudo ip link add link wpan0 name lowpan0 type lowpan

# Bring up the Interface
sudo ip link set wpan0 up
sudo ip link set lowpan0 up

# Check the current 6lowpan
ip addr show lowpan0
```

At the __RSP-client__
```bash
# Check current networks
ip addr show

# Bring lowpa0 and wpan0 offline
sudo ip link set lowpan0 down   
sudo ip link set wpan0 down

# Set the personal area network(PAN) wpan with the pan_id 0xabcd
sudo iwpan dev wpan0 set pan_id 0xabcd

# Set up the channel
# Not working
# sudo iwpan phy0 set channel 0 26            

# Set up the ip
sudo ip addr add 2001:db8::2/64 dev lowpan0

# Set up the interface
sudo ip link add link wpan0 name lowpan0 type lowpan

# Bring up the Interface
sudo ip link set wpan0 up
sudo ip link set lowpan0 up

# Check the current 6lowpan
ip addr show lowpan0

```


## Just copy it
```bash
sudo ip link set lowpan0 down   
sudo ip link set wpan0 down
sudo iwpan dev wpan0 set pan_id 0xabcd
sudo ip link add link wpan0 name lowpan0 type lowpan
sudo ip addr add 2001:db8::1/64 dev lowpan0
#sudo ip addr add 2001:db8::2/64 dev lowpan0
sudo ip link set wpan0 up
sudo ip link set lowpan0 up
clear
ip addr show lowpan0

```