# Copyright (c) 2022 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from . import domain
from ... import globals

class Calib_Dataloader(object):
    def __init__(self):
        pass
    def register_transformation(self):
        domain_ = domain.determine_domain(globals.list_code_path[0])
        if domain_ == 'transformers_trainer':
            globals.list_calib_dataloader_name.append('trainer.get_eval_dataloader()')
        elif domain_ == 'transformers_no_trainer':
            pass
        elif domain_ == 'torchvision':
            globals.list_calib_dataloader_name.append('val_loader')
        else: # random model
            pass