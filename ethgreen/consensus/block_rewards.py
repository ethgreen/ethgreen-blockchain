from ethgreen.util.ints import uint32, uint64

# 1 xeth coin = 1,000,000,000 = 1 billion mojo.
_mojo_per_ethgreen = 1000000000
_blocks_per_year = 1681920  # 32 * 6 * 24 * 365


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 8/10 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height == 0:
        return uint64(int((9 / 10) * 21000062 * _mojo_per_ethgreen))
    elif height < 3 * _blocks_per_year:
        return uint64(int((8 / 10) * 20 * _mojo_per_ethgreen))
    elif height < 6 * _blocks_per_year:
        return uint64(int((8 / 10) * 10 * _mojo_per_ethgreen))
    elif height < 9 * _blocks_per_year:
        return uint64(int((8 / 10) * 5 * _mojo_per_ethgreen))
    elif height < 12 * _blocks_per_year:
        return uint64(int((8 / 10) * 2.5 * _mojo_per_ethgreen))
    else:
        return uint64(int((8 / 10) * 1.25 * _mojo_per_ethgreen))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/10 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously. Bonus to the dev who contributed starting the blockchain !
    """
    if height == 0:
        return uint64(int((1 / 10) * 21000062 * _mojo_per_ethgreen))
    elif height < 3 * _blocks_per_year:
        return uint64(int((1 / 10) * 20 * _mojo_per_ethgreen))
    elif height < 6 * _blocks_per_year:
        return uint64(int((1 / 10) * 10 * _mojo_per_ethgreen))
    elif height < 9 * _blocks_per_year:
        return uint64(int((1 / 10) * 5 * _mojo_per_ethgreen))
    elif height < 12 * _blocks_per_year:
        return uint64(int((1 / 10) * 2.5 * _mojo_per_ethgreen))
    else:
        return uint64(int((1 / 10) * 1.25 * _mojo_per_ethgreen))

def calculate_base_donationwallet_reward(height: uint32) -> uint64:
    """
    Community Rewards: 10% xeth of every block 
    """
    if height == 0:
        return uint64(int((1 / 10) * 0 * _mojo_per_ethgreen))
    elif height < 3 * _blocks_per_year:
        return uint64(int((1 / 10) * 20 * _mojo_per_ethgreen))
    elif height < 6 * _blocks_per_year:
        return uint64(int((1 / 10) * 10 * _mojo_per_ethgreen))
    elif height < 9 * _blocks_per_year:
        return uint64(int((1 / 10) * 5 * _mojo_per_ethgreen))
    elif height < 12 * _blocks_per_year:
        return uint64(int((1 / 10) * 2.5 * _mojo_per_ethgreen))
    else:
        return uint64(int((1 / 10) * 1.25 * _mojo_per_ethgreen))
