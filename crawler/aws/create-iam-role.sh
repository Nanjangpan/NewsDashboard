aws iam create-policy \
    --policy-name just10minutes-crawler-service-role \
    --policy-document file://just10minutes-crawler-service-iam-policy.json \
    --profile ybigta-conference

aws iam create-role \
    --role-name just10minutes-crawler-service-serviceaccount \
    --assume-role-policy-document file://just10minutes-crawler-service-iam-assume-role-policy.json \
    --profile ybigta-conference

aws iam attach-role-policy \
    --role-name just10minutes-crawler-service-serviceaccount \
    --policy-arn arn:aws:iam::532214462726:policy/just10minutes-crawler-service-role \
    --profile ybigta-conference
