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

"""urls module tests."""



import logging
logging.basicConfig(filename='/dev/null')

import re
import types
import tests.appenginesdk
from google.apputils import app
from google.apputils import basetest
import mox
import stubout
from simian.mac import urls


class MacsimianMainModuleTest(mox.MoxTestBase):
  """Test module level portions of urls."""

  def setUp(self):
    mox.MoxTestBase.setUp(self)
    self.stubs = stubout.StubOutForTesting()

  def tearDown(self):
    self.mox.UnsetStubs()
    self.stubs.UnsetAll()

  def testStructure(self):
    """Test the overall structure of the module."""
    self.assertTrue(hasattr(urls, 'application'))
    self.assertTrue(hasattr(urls, 'main'))
    self.assertEqual(types.FunctionType, type(urls.main))
    self.assertEqual(
        urls.webapp.WSGIApplication, type(urls.application))

  def testWgsiAppInitArgs(self):
    """Test the arguments that are supplied to setup the application var."""

    def wsgiapp_hook(*args, **kwargs):
      o = self.mox.CreateMockAnything()
      o.set_by_test_hook = 1
      o.args = args
      o.kwargs = kwargs
      return o

    self.stubs.Set(
        urls.webapp, 'WSGIApplication', wsgiapp_hook)
    self.mox.ReplayAll()
    reload(urls)
    app = urls.application
    self.assertNotEqual(
        urls.webapp.WSGIApplication, type(app))
    self.assertTrue(hasattr(app, 'set_by_test_hook'))
    self.assertTrue(type(app.args) is types.TupleType)
    self.assertTrue(type(app.args[0]) is types.ListType)
    self.assertTrue(type(app.kwargs) is types.DictType)

    for (regex, cls) in app.args[0]:
      unused = re.compile(regex)
      self.assertTrue(issubclass(cls, urls.webapp.RequestHandler))

    if 'debug' in app.kwargs:
      self.assertTrue(type(app.kwargs['debug']) is types.BooleanType)

    self.mox.VerifyAll()


def main(unused_argv):
  basetest.main()


if __name__ == '__main__':
  app.run()