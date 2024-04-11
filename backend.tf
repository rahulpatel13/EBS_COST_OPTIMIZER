terraform {
  backend "s3" {
    bucket = "mypersonalbackendtfbucket"
    region = "us-east-1"
    key    = "terraform.tfstate"
  }
}