#  Copyright 2010 Gregory Szorc, 
# This fork maintained by Michael Medin
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name             = 'lua-protobuf',
    version          = '1.0.1',
    author           = 'Michael Medin',
    author_email     = 'michael@medin.name',
    description      = 'Lua protocol buffer code generator',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url              = 'http://github.com/mickem/lua-protobuf',
    packages         = [ 'lua_protobuf' ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    scripts          = ['protoc-gen-lua', 'protoc-gen-lua.cmd'],
    python_requires  = '>=3.6',
    install_requires = [ 'protobuf>=3.0.0' ]
)
