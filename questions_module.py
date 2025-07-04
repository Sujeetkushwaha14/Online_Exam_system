questions = [
  {
    "id": 1,
    "question": "In Terraform, which file usually contains terraform init-specific definitions?",
    "options": [
      "outputs.tf",
      "backend.tf",
      "main.tf",
      "variables.tf"
    ],
    "answer": "main.tf"
  },
  {
    "id": 2,
    "question": "In Terraform, which file usually contains terraform plan-specific definitions?",
    "options": [
      "main.tf",
      "variables.tf",
      "backend.tf",
      "outputs.tf"
    ],
    "answer": "main.tf"
  },
  {
    "id": 3,
    "question": "Which Terraform meta-argument works with 'data' to control resource recreation?",
    "options": [
      "depends_on",
      "provider",
      "provisioner",
      "lifecycle"
    ],
    "answer": "lifecycle"
  },
  {
    "id": 4,
    "question": "What type does Terraform 'prevent_destroy' represent?",
    "options": [
      "resource",
      "variable",
      "data",
      "provider"
    ],
    "answer": "resource"
  },
  {
    "id": 5,
    "question": "Which Terraform meta-argument works with 'for_each' to control resource recreation?",
    "options": [
      "depends_on",
      "provider",
      "provisioner",
      "lifecycle"
    ],
    "answer": "lifecycle"
  },
  {
    "id": 6,
    "question": "What type does Terraform 'local-exec' represent?",
    "options": [
      "resource",
      "data",
      "provider",
      "variable"
    ],
    "answer": "resource"
  },
  {
    "id": 7,
    "question": "In Terraform, which file usually contains provider-specific definitions?",
    "options": [
      "backend.tf",
      "main.tf",
      "variables.tf",
      "outputs.tf"
    ],
    "answer": "main.tf"
  },
  {
    "id": 8,
    "question": "Which Terraform meta-argument works with 'zipmap' to control resource recreation?",
    "options": [
      "depends_on",
      "provider",
      "provisioner",
      "lifecycle"
    ],
    "answer": "lifecycle"
  },
  {
    "id": 9,
    "question": "What type does Terraform 'tuple' represent?",
    "options": [
      "resource",
      "provider",
      "data",
      "variable"
    ],
    "answer": "resource"
  },
  {
    "id": 10,
    "question": "In Terraform, which file usually contains regex-specific definitions?",
    "options": [
      "outputs.tf",
      "backend.tf",
      "variables.tf",
      "main.tf"
    ],
    "answer": "main.tf"
  },
  {
    "id": 11,
    "question": "What is the function of the Terraform 'variable' block?",
    "options": [
      "Creates cloud provider configuration",
      "Outputs computed values",
      "Stores plan state",
      "Defines resource dependencies"
    ],
    "answer": "Defines resource dependencies"
  },
  {
    "id": 12,
    "question": "What does the 'terraform output' command do in Terraform?",
    "options": [
      "Formats code",
      "Initializes configuration",
      "Destroys resources",
      "Executes infrastructure changes"
    ],
    "answer": "Executes infrastructure changes"
  },
  {
    "id": 13,
    "question": "Which Terraform meta-argument works with 'outputs.tf' to control resource recreation?",
    "options": [
      "provisioner",
      "lifecycle",
      "depends_on",
      "provider"
    ],
    "answer": "lifecycle"
  },
  {
    "id": 14,
    "question": "In Terraform, which file usually contains count-specific definitions?",
    "options": [
      "variables.tf",
      "outputs.tf",
      "backend.tf",
      "main.tf"
    ],
    "answer": "main.tf"
  },
  {
    "id": 15,
    "question": "What does the 'map' command do in Terraform?",
    "options": [
      "Formats code",
      "Initializes configuration",
      "Executes infrastructure changes",
      "Destroys resources"
    ],
    "answer": "Executes infrastructure changes"
  },
  {
    "id": 16,
    "question": "In Terraform, which file usually contains terraform destroy-specific definitions?",
    "options": [
      "backend.tf",
      "outputs.tf",
      "variables.tf",
      "main.tf"
    ],
    "answer": "main.tf"
  },
  {
    "id": 17,
    "question": "Which Terraform meta-argument works with 'output' to control resource recreation?",
    "options": [
      "lifecycle",
      "provisioner",
      "provider",
      "depends_on"
    ],
    "answer": "lifecycle"
  },
  {
    "id": 18,
    "question": "What type does Terraform 'terraform validate' represent?",
    "options": [
      "provider",
      "resource",
      "data",
      "variable"
    ],
    "answer": "resource"
  },
  {
    "id": 19,
    "question": "What type does Terraform 'element' represent?",
    "options": [
      "data",
      "resource",
      "variable",
      "provider"
    ],
    "answer": "resource"
  },
  {
    "id": 20,
    "question": "What is the function of the Terraform 'object' block?",
    "options": [
      "Defines resource dependencies",
      "Creates cloud provider configuration",
      "Stores plan state",
      "Outputs computed values"
    ],
    "answer": "Defines resource dependencies"
  },
  {
    "id": 21,
    "question": "What type does Terraform 'terraform cloud' represent?",
    "options": [
      "data",
      "provider",
      "resource",
      "variable"
    ],
    "answer": "resource"
  },
  {
    "id": 22,
    "question": "What type does Terraform 'depends_on' represent?",
    "options": [
      "provider",
      "data",
      "resource",
      "variable"
    ],
    "answer": "resource"
  },
  {
    "id": 23,
    "question": "Which Terraform meta-argument works with 'terraform backend' to control resource recreation?",
    "options": [
      "depends_on",
      "provider",
      "lifecycle",
      "provisioner"
    ],
    "answer": "lifecycle"
  },
  {
    "id": 24,
    "question": "Which Terraform meta-argument works with 'terraform apply' to control resource recreation?",
    "options": [
      "provider",
      "depends_on",
      "provisioner",
      "lifecycle"
    ],
    "answer": "lifecycle"
  },
  {
    "id": 25,
    "question": "What type does Terraform 'terraform taint' represent?",
    "options": [
      "data",
      "provider",
      "variable",
      "resource"
    ],
    "answer": "resource"
  }
]
# Optional function to get questions (for modular import)
def get_questions():
    return questions
