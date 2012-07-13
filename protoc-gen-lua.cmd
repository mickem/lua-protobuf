@setlocal enableextensions & %~dp0\..\python.exe -u -x %~f0 %* & goto :EOF
#!C:\Python\27x64\Python.exe
# EASY-INSTALL-SCRIPT: 'lua-protobuf==0.0.1','protoc-gen-lua'
__requires__ = 'lua-protobuf==0.0.1'
import pkg_resources
pkg_resources.run_script('lua-protobuf==0.0.1', 'protoc-gen-lua')
