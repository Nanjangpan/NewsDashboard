#!/bin/bash

 $( aws ecr get-login --no-include-email --region ap-northeast-2 --profile ybigta-conference)
export VER=$1

docker build --tag 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/react:$VER -f Dockerfile .

docker push 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/react:$VER
docker tag 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/react:$VER 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/react:dev
docker push 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/react:dev