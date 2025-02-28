# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Distributed Graph Engine API
"""
import warnings

from pgl.distributed import dist_graph

from pgl.distributed.dist_graph import *

__all__ = []
__all__ += dist_graph.__all__

warnings.warn(
    "The Distributed Graph Engine is experimental, we will officially release it soon"
)
