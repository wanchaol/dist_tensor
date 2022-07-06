import torch.distributed.distributed_c10d as c10d

from typing import List
from dataclasses import dataclass
from .device_mesh import DeviceMesh

@dataclass
class Placement(object):
    # base class Placement type
    pass

@dataclass
class Shard(Placement):
    # shard placement, shard on a dim
    dim: int

@dataclass
class Replicate(Placement):
    # replicate placement
    pass

@dataclass
class _Partial(Placement):
    # partial placement with reduce op
    reduce_op: c10d.ReduceOp

@dataclass
class PlacementSpec(object):
    device_mesh: DeviceMesh
    strategies: List[Placement]
