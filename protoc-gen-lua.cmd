@IF DEFINED PYTHON (@setlocal enableextensions & %PYTHON% -u -x %~f0 %* & goto :EOF) ELSE (@setlocal enableextensions & python.exe -u -x %~f0 %* & goto :EOF)
#!python.exe
# EASY-INSTALL-SCRIPT: 'lua-protobuf==0.0.1','protoc-gen-lua'
__requires__ = 'lua-protobuf==0.0.1'
import pkg_resources
pkg_resources.run_script('lua-protobuf==0.0.1', 'protoc-gen-lua')
