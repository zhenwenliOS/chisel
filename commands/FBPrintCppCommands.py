#!/usr/bin/python

# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import lldb
import fblldbbase as fb

def lldbcommands():
  return [
    FBPrintCppStringCommand(),
    FBPrintCppObjectCommand(),
    FBPrintCppVectorCommand(),
    FBPrintCppMapCommand(),
  ]

# pcstring
class FBPrintCppStringCommand(fb.FBCommand):
  def name(self):
    return 'pcstring'

  def description(self):
    return 'Print the description of <cpp string>.'
    
  def args(self):
    return [ fb.FBCommandArgument(arg='cstring', type='std::string', help='Print the description of cpp string.') ]

  def run(self, arguments, options):
    print(fb.describeObject('[[NSString alloc] initWithUTF8String:{}.data]'.format(arguments[0])))


# pcobject
class FBPrintCppObjectCommand(fb.FBCommand):
  def name(self):
    return 'pcobject'

  def description(self):
    return 'Print the description of <cpp object>.'

  def args(self):
    return [ fb.FBCommandArgument(arg='cpp class object', type='', help='Print the description of cpp class object.') ]

  def run(self, arguments, options):
    # 'call {}'.format(arguments[0])
    lldb.debugger.HandleCommand('frame variable {}'.format(arguments[0]))


# pcvector
class FBPrintCppVectorCommand(fb.FBCommand):
  def name(self):
    return 'pcvector'

  def description(self):
    return 'Print the description of <cpp vector>.'

  def args(self):
    return [ fb.FBCommandArgument(arg='cpp vector', type='', help='Print the description of cpp vector.') ]

  def run(self, arguments, options):
    # 'call {}'.format(arguments[0])
    lldb.debugger.HandleCommand('frame variable {}'.format(arguments[0]))


# pcmap
class FBPrintCppMapCommand(fb.FBCommand):
  def name(self):
    return 'pcmap'

  def description(self):
    return 'Print the description of <cpp map>.'

  def args(self):
    return [ fb.FBCommandArgument(arg='cpp map', type='', help='Print the description of cpp map.') ]

  def run(self, arguments, options):
    # 'call {}'.format(arguments[0])
    lldb.debugger.HandleCommand('frame variable {}'.format(arguments[0]))
