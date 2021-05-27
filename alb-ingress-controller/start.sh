# IAM OIDC 공급자를 생성하여 클러스터와 연결합니다
eksctl utils associate-iam-oidc-provider \
--region ap-northeast-2 \
--cluster ybigta-news --approve\
 --profile ybigta-conference

# policy 다운로드
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json

# IAM policy 생성하
aws iam create-policy \
    --policy-name alb-ingress-controller \
    --policy-document file://iam-policy.json --profile ybigta-conference

# 사용할 로드 밸런서 컨트롤러에 대한 IAM 네임스페이스의 aws-load-balancer-controller,
# 클러스터 역할 및 클러스터 역할 바인딩이라는 kube-system 역할과
# Kubernetes 서비스 계정을 생성합니다.
eksctl create iamserviceaccount \
  --cluster=ybigta-news \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --attach-policy-arn=arn:aws:iam::532214462726:policy/alb-ingress-controller \
  --override-existing-serviceaccounts \
  --approve --profile ybigta-conference

#HELM 차트를 이용해 aws loadblancer install
kubectl apply -k "github.com/aws/eks-charts/stable/aws-load-balancer-controller//crds?ref=master"

helm repo add eks https://aws.github.io/eks-charts

helm upgrade -i aws-load-balancer-controller eks/aws-load-balancer-controller \
  --set clusterName=ybigta-news \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  -n kube-system