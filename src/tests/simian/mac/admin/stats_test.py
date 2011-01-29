#!/usr/bin/env python
# 
# Copyright 2010 Google Inc. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# #

"""stats module tests."""



import logging
logging.basicConfig(filename='/dev/null')

from google.apputils import app
from google.apputils import basetest
import mox
import stubout
from simian.mac.admin import stats


class StatsTest(mox.MoxTestBase):
  """Test Stats class."""

  def setUp(self):
    mox.MoxTestBase.setUp(self)
    self.stubs = stubout.StubOutForTesting()
    self.stats = stats.Stats()
    self.stats.response = self.mox.CreateMockAnything()
    self.stats.response.out = self.stats.response

  def tearDown(self):
    self.mox.UnsetStubs()
    self.stubs.UnsetAll()


def main(unused_argv):
  basetest.main()


if __name__ == '__main__':
  app.run()