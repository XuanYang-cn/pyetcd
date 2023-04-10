#!/bin/bash

#  Copyright (C) 2023 XuanYang-cn. All rights reserved.
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

OUTDIR="etcd3/etcdrpc"
PROTO_DIR="etcd3/proto"

python -m grpc_tools.protoc -I ${PROTO_DIR} --python_out=${OUTDIR} --pyi_out=${OUTDIR} ${PROTO_DIR}/auth.proto
python -m grpc_tools.protoc -I ${PROTO_DIR} --python_out=${OUTDIR} --pyi_out=${OUTDIR} ${PROTO_DIR}/kv.proto
python -m grpc_tools.protoc -I ${PROTO_DIR} --python_out=${OUTDIR} --pyi_out=${OUTDIR} --grpc_python_out=${OUTDIR}  ${PROTO_DIR}/rpc.proto

if [[ $(uname -s) == "Darwin" ]]; then
    if ! brew --prefix --installed gnu-sed >/dev/null 2>&1; then
        brew install gnu-sed
    fi
    export PATH="/usr/local/opt/gsed/libexec/gnubin:$PATH"
fi

sed -i 's/import rpc_pb2 as rpc__pb2/from . import rpc_pb2 as rpc__pb2/' $OUTDIR/*py
sed -i 's/import kv_pb2 as kv__pb2/from . import kv_pb2 as kv__pb2/' $OUTDIR/*py
sed -i 's/import auth_pb2 as auth__pb2/from . import auth_pb2 as auth__pb2/' $OUTDIR/*py

sed -i 's/import kv_pb2 as _kv_pb2/from . import kv_pb2 as _kv_pb2/' $OUTDIR/*pyi
sed -i 's/auth_pb2 as _auth_pb2/from . import auth_pb2 as _auth_pb2/' $OUTDIR/*pyi

echo "Success to generate the python proto files."
