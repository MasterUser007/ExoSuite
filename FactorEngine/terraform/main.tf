provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "primeengine_gpu" {
  ami           = "ami-0c02fb55956c7d316"  # Ubuntu 20.04 LTS
  instance_type = "g4dn.xlarge"
  key_name      = "your-ssh-key-name"
  tags = {
    Name = "PrimeEngineAI-GPU"
  }

  user_data = <<-EOF
              #!/bin/bash
              apt update && apt install -y docker.io git python3-pip
              git clone https://github.com/yourorg/PrimeEngineAI.git
              cd PrimeEngineAI
              pip3 install -r requirements.txt
              nohup python3 main.py > output.log 2>&1 &
              EOF
}
