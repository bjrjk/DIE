#!/bin/bash

pushd fuzz/TS
npm i
node_modules/.bin/tsc
popd

pushd fuzz/afl
make clean
make CC=clang-6.0
popd

pushd llvm_mode
make clean
make CC=clang-6.0 CXX=g++ LLVM_CONFIG=llvm-config-6.0
popd

