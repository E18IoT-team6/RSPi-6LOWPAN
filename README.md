# How to do


## wpan-tools


https://github.com/linux-wpan/wpan-tools.git

## Testing

At the __RSP-sink__

```bash
sudo ip link set lowpan0 down   # Bring lowpa0 offline
sudo ip link set wpan0 down     # Bring wpan0 offline

sudo iwpan dev wpan0 set pan_id 0xcafe      # Set the personal area network(PAN) wpan with the pan_id 0xcafe
sudo iwpan phy0 set channel 0 26            

sudo ip link add link wpan0 name lowpan0 type lowpan

sudo ip link set wpan0 up       # Bring wpan0 online
sudo ip link set lowpan0 up     # Bring lowpa0 online

sudo ip addr add 2001:db8::1/64 dev lowpan0 
```

At the __RSP-client__
```bash
sudo ip link set lowpan0 down
sudo ip link set wpan0 down

sudo iwpan dev wpan0 set pan_id 0xcafe
sudo iwpan phy0 set channel 0 26

sudo ip link add link wpan0 name lowpan0 type lowpan

sudo ip link set wpan0 up
sudo ip link set lowpan0 up

sudo ip addr add 2001:db8::2/64 dev lowpan0
```