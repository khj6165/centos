#!/bin/sh
./nvidia.sh
./utility.sh
./code.sh
./djv.sh
./mpv.sh
./rmbeep.sh
./trans.sh
./pip.sh
./devtools.sh
./ffmpeg.sh
./handbrake.sh
./ocio_config.sh
./alembic.sh

#gcc6.x를 이용해서 빌드한다.
scl enable devtoolset-6 ./cmake.sh
scl enable devtoolset-6 ./openexr.sh
scl enable devtoolset-6 ./opencolorio.sh
