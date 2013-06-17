# -*- coding: utf-8 -*-
#    Copyright 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json

from nailgun.errors import errors


class BasicValidator(object):
    @classmethod
    def validate_json(cls, data, desired_type=None):
        if data:
            try:
                res = json.loads(data)
            except:
                raise errors.InvalidData(
                    "Invalid json received",
                    log_message=True
                )
            if desired_type and not isinstance(res, desired_type):
                raise errors.InvalidData(
                    "Invalid data received (expected {0})".format(
                        str(desired_type)
                    ),
                    log_message=True
                )
        else:
            raise errors.InvalidData(
                "Empty request received",
                log_message=True
            )
        return res

    @classmethod
    def validate(cls, data):
        raise NotImplementedError("You should override this method")