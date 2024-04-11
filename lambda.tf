data "archive_file" "zip_the_python_code" {
  type        = "zip"
  source_file = "${path.module}/code.py"
  output_path = "${path.module}/code.zip"
}
resource "aws_lambda_function" "cost-reporting-lambda" {
  filename         = "${path.module}/code.zip"
  function_name    = var.lambda-name
  role             = aws_iam_role.iam-role-cost-optimizer-EBS.arn
  handler          = "ebs_co.lambda_handler"
  timeout          = 10
  runtime          = "python3.10"
  source_code_hash = data.archive_file.zip_the_python_code.output_base64sha256
}