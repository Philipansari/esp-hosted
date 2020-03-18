# Copyright 2019 Espressif Systems (Shanghai) PTE LTD
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

from struct import *
from .transport import Transport
import binascii
import time
import utils

class Transport_pserial(Transport):
    def __init__(self, devname):
        self.f1 = open(devname, "wb",buffering = 5120)
        self.f2 = open(devname, "rb",buffering = 5120)

    def send_data(self, ep_name, data, wait):
        buf = bytearray([0x01])
        buf.extend(pack('<H', len(ep_name)))
        buf.extend(map(ord,ep_name))
        buf.extend(b'\x02')
        buf.extend(pack('<H', len(data)))
        print(bytearray(data))
       # print(bytearray(data,'utf-8'))
       # buf.extend(bytearray(data, 'utf8'))
        buf.extend(bytearray(data))
        #print(utils.str_to_hexstr(str(buf)))
        s = self.f1.write(buf)
        self.f1.flush()
        time.sleep(wait)
        s = self.f2.read(5120)
        self.f2.flush()
        return s
        
