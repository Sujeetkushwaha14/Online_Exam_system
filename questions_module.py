questions = [
    {"id": 1, "question": "In Kubernetes, what does 'CrashLoopBackOff' status mean?", "options": [
        "Pod is scheduled to a node but not started",
        "Pod is running successfully",
        "Pod is repeatedly crashing after starting",
        "Pod is stuck in image pulling"
    ], "answer": "Pod is repeatedly crashing after starting"},

    {"id": 2, "question": "Which Terraform command is used to refresh the state file with real infrastructure?", "options": [
        "terraform plan",
        "terraform apply",
        "terraform init",
        "terraform refresh"
    ], "answer": "terraform refresh"},

    {"id": 3, "question": "In Jenkins, what is a 'Declarative Pipeline'?", "options": [
        "Pipeline written in shell script",
        "Pipeline defined using JSON",
        "Pipeline using a defined syntax structure in Jenkinsfile",
        "None of the above"
    ], "answer": "Pipeline using a defined syntax structure in Jenkinsfile"},

    {"id": 4, "question": "Which file defines playbooks in Ansible?", "options": [
        "JSON",
        "YAML",
        "INI",
        "XML"
    ], "answer": "YAML"},

    {"id": 5, "question": "Which Dockerfile instruction is used to set environment variables?", "options": [
        "ARG", "FROM", "ENV", "RUN"
    ], "answer": "ENV"},

    {"id": 6, "question": "What is the default namespace in Kubernetes?", "options": [
        "kube-public", "default", "system", "dev"
    ], "answer": "default"},

    {"id": 7, "question": "What is the purpose of 'terraform taint'?", "options": [
        "To destroy the entire infrastructure",
        "To refresh the state file",
        "To mark a resource for recreation",
        "To rollback changes"
    ], "answer": "To mark a resource for recreation"},

    {"id": 8, "question": "What is a 'canary deployment'?", "options": [
        "Deploying all at once",
        "Testing on staging only",
        "Releasing new version to small user base",
        "Rolling back code automatically"
    ], "answer": "Releasing new version to small user base"},

    {"id": 9, "question": "In Prometheus, what is a metric type?", "options": [
        "Counter", "Gauge", "Histogram", "All of the above"
    ], "answer": "All of the above"},

    {"id": 10, "question": "Which of the following is used to install Docker on Ubuntu?", "options": [
        "apt-get install docker-ce", "yum install docker", "docker install", "pip install docker"
    ], "answer": "apt-get install docker-ce"},

    {"id": 11, "question": "What is the main purpose of 'etcd' in Kubernetes?", "options": [
        "Storing pod logs", "Managing deployments", "Configuration store and key-value store", "Running containers"
    ], "answer": "Configuration store and key-value store"},

    {"id": 12, "question": "Which plugin in Jenkins is used to integrate with GitHub?", "options": [
        "GitHub Plugin", "SCM Plugin", "Webhook Plugin", "Pipeline Plugin"
    ], "answer": "GitHub Plugin"},

    {"id": 13, "question": "What does 'Immutable Infrastructure' mean?", "options": [
        "Infrastructure cannot be modified after deployment",
        "Infrastructure changes automatically",
        "Infrastructure resets every hour",
        "Infrastructure is flexible"
    ], "answer": "Infrastructure cannot be modified after deployment"},

    {"id": 14, "question": "Which of the following tools is primarily used for configuration management?", "options": [
        "Kubernetes", "Ansible", "Docker", "Terraform"
    ], "answer": "Ansible"},

    {"id": 15, "question": "What is a node pool in Kubernetes?", "options": [
        "A group of services", "A set of pods", "A set of nodes with common configuration", "None"
    ], "answer": "A set of nodes with common configuration"},

    {"id": 16, "question": "What command lists all Terraform-managed resources?", "options": [
        "terraform graph", "terraform show", "terraform output", "terraform state list"
    ], "answer": "terraform state list"},

    {"id": 17, "question": "Which command builds a Docker image?", "options": [
        "docker run", "docker build", "docker exec", "docker commit"
    ], "answer": "docker build"},

    {"id": 18, "question": "What is the role of kubelet in Kubernetes?", "options": [
        "Load balancer", "Pod monitor on nodes", "Stores logs", "None"
    ], "answer": "Pod monitor on nodes"},

    {"id": 19, "question": "In Jenkinsfile, which block is used to define stages?", "options": [
        "pipeline", "stages", "jobs", "script"
    ], "answer": "stages"},

    {"id": 20, "question": "What does IaC stand for?", "options": [
        "Internet and Cloud", "Infrastructure as Code", "Input and Code", "Infra access Control"
    ], "answer": "Infrastructure as Code"},

    {"id": 21, "question": "Which command creates an EC2 instance in Terraform?", "options": [
        "resource 'aws_instance'", "create aws_instance", "ec2.run", "aws_instance_create"
    ], "answer": "resource 'aws_instance'"},

    {"id": 22, "question": "What is 'blue-green deployment'?", "options": [
        "Random deployments", "Using Kubernetes nodes", "Two environments: current & new version", "Deploying in blue color"
    ], "answer": "Two environments: current & new version"},

    {"id": 23, "question": "What does `docker-compose up` do?", "options": [
        "Deletes all containers", "Stops all services", "Starts and builds services", "Only builds images"
    ], "answer": "Starts and builds services"},

    {"id": 24, "question": "What is the default port for Prometheus server?", "options": [
        "9090", "8080", "7070", "3000"
    ], "answer": "9090"},

    {"id": 25, "question": "What is the primary goal of DevOps?", "options": [
        "Faster code commits", "Infrastructure monitoring", "CI/CD and collaboration between Dev and Ops", "Just automation"
    ], "answer": "CI/CD and collaboration between Dev and Ops"},
]


# Optional function to get questions (for modular import)
def get_questions():
    return questions
