resource "aws_iam_policy" "iam-policy-ebs-co" {
  name = "iam-policy-${var.lambda-name}"
  policy = file("${path.module}/iam_policy.json")

}