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
    
    [
  {
    "id": 1,
    "question": "Which Kubernetes controller guarantees a fixed number of pod replicas across node failures?",
    "options": [
      "DaemonSet",
      "StatefulSet",
      "ReplicaSet",
      "Deployment"
    ],
    "answer": "ReplicaSet"
  },
  {
    "id": 2,
    "question": "What is the primary function of a Docker layer cache during container image builds?",
    "options": [
      "Reduce image pull time",
      "Avoid redundant computation",
      "Improve container startup",
      "Isolate filesystem writes"
    ],
    "answer": "Avoid redundant computation"
  },
  {
    "id": 3,
    "question": "In CI/CD, what does a blue-green deployment achieve?",
    "options": [
      "A/B testing of microservices",
      "Instant rollback with minimal downtime",
      "Automatic scaling under traffic",
      "Zero-trust service exposure"
    ],
    "answer": "Instant rollback with minimal downtime"
  },
  {
    "id": 4,
    "question": "What does the `terraform taint` command do?",
    "options": [
      "Removes resource state lock",
      "Forces resource recreation on next apply",
      "Deletes entire infrastructure",
      "Refreshes the backend config"
    ],
    "answer": "Forces resource recreation on next apply"
  },
  {
    "id": 5,
    "question": "Which tool supports GitOps workflows and Kubernetes-native sync automation?",
    "options": [
      "ArgoCD",
      "Jenkins",
      "Packer",
      "Terraform Cloud"
    ],
    "answer": "ArgoCD"
  },
  {
    "id": 6,
    "question": "Which Git strategy allows organizing changes into logical units with replay capability?",
    "options": [
      "Squash and merge",
      "Rebase",
      "Fast-forward",
      "Cherry-pick"
    ],
    "answer": "Rebase"
  },
  {
    "id": 7,
    "question": "What is the function of a service mesh like Istio?",
    "options": [
      "Manages pod DNS resolution",
      "Handles inter-service communication policies",
      "Provision storage volumes",
      "Scales up compute capacity"
    ],
    "answer": "Handles inter-service communication policies"
  },
  {
    "id": 8,
    "question": "Which log aggregation tool is built on top of Elasticsearch and integrates with Kibana?",
    "options": [
      "Logstash",
      "Grafana",
      "Promtail",
      "Fluent Bit"
    ],
    "answer": "Logstash"
  },
  {
    "id": 9,
    "question": "Which type of Helm template construct allows looping over input values?",
    "options": [
      "with",
      "range",
      "if",
      "define"
    ],
    "answer": "range"
  },
  {
    "id": 10,
    "question": "What does a readiness probe failure cause in Kubernetes?",
    "options": [
      "Pod is restarted by kubelet",
      "Pod is removed from service endpoints",
      "Container is paused",
      "Pod enters Failed phase"
    ],
    "answer": "Pod is removed from service endpoints"
  },

  {
    "id": 100,
    "question": "Which configuration enforces Kubernetes RBAC for restricting dashboard access per namespace?",
    "options": [
      "ClusterRoleBinding",
      "RoleBinding",
      "Admission Controller",
      "PodSecurityPolicy"
    ],
    "answer": "RoleBinding"
  }
]
  {
    "id": 11,
    "question": "What is the role of a Vault dynamic secret backend?",
    "options": [
      "Rotates SSH keys automatically",
      "Generates credentials on-demand",
      "Encrypts TLS certificates",
      "Stores static API tokens"
    ],
    "answer": "Generates credentials on-demand"
  },
  {
    "id": 12,
    "question": "Which Prometheus metric type accumulates monotonically over time?",
    "options": [
      "Histogram",
      "Gauge",
      "Counter",
      "Summary"
    ],
    "answer": "Counter"
  },
  {
    "id": 13,
    "question": "Which AWS service allows managed Kubernetes clusters?",
    "options": [
      "ECS",
      "EKS",
      "Fargate",
      "CloudFormation"
    ],
    "answer": "EKS"
  },
  {
    "id": 14,
    "question": "In Linux, what does the `netstat -tuln` command show?",
    "options": [
      "Active routes",
      "Listening ports",
      "Socket count",
      "Interface throughput"
    ],
    "answer": "Listening ports"
  },
  {
    "id": 15,
    "question": "What is the effect of `docker-compose down`?",
    "options": [
      "Stops and removes services and volumes",
      "Halts CPU usage temporarily",
      "Scales services to zero",
      "Pushes images to registry"
    ],
    "answer": "Stops and removes services and volumes"
  },
  {
    "id": 16,
    "question": "Which Terraform block connects modules to variables dynamically?",
    "options": [
      "resource",
      "provider",
      "module",
      "data"
    ],
    "answer": "module"
  },
  {
    "id": 17,
    "question": "Which CI/CD platform uses YAML-defined workflows triggered by GitHub events?",
    "options": [
      "GitLab CI",
      "Jenkins",
      "GitHub Actions",
      "CircleCI"
    ],
    "answer": "GitHub Actions"
  },
  {
    "id": 18,
    "question": "Which Linux command can limit process CPU usage?",
    "options": [
      "renice",
      "kill",
      "nice",
      "cpulimit"
    ],
    "answer": "cpulimit"
  },
  {
    "id": 19,
    "question": "In ArgoCD, what does sync wave control?",
    "options": [
      "Application secrets",
      "Resource ordering",
      "Authentication tokens",
      "Load balancing priority"
    ],
    "answer": "Resource ordering"
  },
  {
    "id": 20,
    "question": "Which Git command reverts a merge commit without rewriting history?",
    "options": [
      "git reset",
      "git revert -m 1",
      "git checkout HEAD~",
      "git stash"
    ],
    "answer": "git revert -m 1"
  },


  {
    "id": 100,
    "question": "Which configuration enforces Kubernetes RBAC for restricting dashboard access per namespace?",
    "options": [
      "ClusterRoleBinding",
      "RoleBinding",
      "Admission Controller",
      "PodSecurityPolicy"
    ],
    "answer": "RoleBinding"
  }

[
  {
    "id": 101,
    "question": "What technique ensures ephemeral containers regain external connection post-node restart?",
    "options": [
      "Static routing",
      "Overlay tunneling",
      "HostPort exposure",
      "PersistentVolumeClaim"
    ],
    "answer": "Overlay tunneling"
  },
  {
    "id": 102,
    "question": "Which tool scans Terraform templates for security violations?",
    "options": [
      "TFLint",
      "Checkov",
      "Infracost",
      "Terragrunt"
    ],
    "answer": "Checkov"
  },
  {
    "id": 103,
    "question": "Which systemd unit option defines dependencies before launching services?",
    "options": [
      "Requires=",
      "Wants=",
      "Before=",
      "After="
    ],
    "answer": "Requires="
  },
  {
    "id": 104,
    "question": "What is used in Jenkins to isolate concurrent pipeline executions?",
    "options": [
      "Parallel block",
      "Build queue",
      "Workspace locking",
      "Executor throttling"
    ],
    "answer": "Workspace locking"
  },
  {
    "id": 105,
    "question": "What is the purpose of an ingress class annotation in manifests?",
    "options": [
      "Control scheduler affinity",
      "Select ingress controller",
      "Assign node labels",
      "Override container specs"
    ],
    "answer": "Select ingress controller"
  },
  {
    "id": 106,
    "question": "Which DNS record maps subdomain hierarchy using zone delegation?",
    "options": [
      "SRV",
      "MX",
      "NS",
      "CNAME"
    ],
    "answer": "NS"
  },
  {
    "id": 107,
    "question": "Which tool enables provisioning ephemeral development environments via containers?",
    "options": [
      "Vagrant",
      "DevSpace",
      "Minikube",
      "Podman"
    ],
    "answer": "DevSpace"
  },
  {
    "id": 108,
    "question": "What does the `docker exec -it` option achieve?",
    "options": [
      "Starts interactive session inside container",
      "Initiates background file copy",
      "Resumes paused process",
      "Rebuilds layer hierarchy"
    ],
    "answer": "Starts interactive session inside container"
  },
  {
    "id": 109,
    "question": "Which YAML syntax permits inheritance of CI stages?",
    "options": [
      "extends",
      "anchors",
      "includes",
      "references"
    ],
    "answer": "anchors"
  },
  {
    "id": 110,
    "question": "Which controller ensures PVCs get attached with consistent stateful data?",
    "options": [
      "ReplicaSet",
      "StatefulSet",
      "Job",
      "CronJob"
    ],
    "answer": "StatefulSet"
  },
  {
    "id": 200,
    "question": "Which CI component validates commit structure before merging pull requests?",
    "options": [
      "Pre-merge hook",
      "Schema linter",
      "Workflow enforcer",
      "Commit policy checker"
    ],
    "answer": "Commit policy checker"
  }
]
[
  {
    "id": 201,
    "question": "What mechanism in GitLab CI enforces job dependencies across multiple stages?",
    "options": [
      "needs",
      "requires",
      "before_script",
      "trigger"
    ],
    "answer": "needs"
  },
  {
    "id": 202,
    "question": "Which monitoring feature in Grafana allows alert dispatch through webhooks?",
    "options": [
      "Notification channel",
      "Contact point",
      "Expression evaluator",
      "Alert manager"
    ],
    "answer": "Contact point"
  },
  {
    "id": 203,
    "question": "What Linux utility traces system calls for troubleshooting binaries?",
    "options": [
      "strace",
      "lsof",
      "gdb",
      "dstat"
    ],
    "answer": "strace"
  },
  {
    "id": 204,
    "question": "Which CI/CD construct in Azure DevOps allows conditional step evaluation?",
    "options": [
      "jobs",
      "phases",
      "dependsOn",
      "conditions"
    ],
    "answer": "conditions"
  },
  {
    "id": 205,
    "question": "What defines horizontal scaling strategy for stateless microservices?",
    "options": [
      "Load-based replication",
      "Service sharding",
      "Instance duplication",
      "Pod autoscaling"
    ],
    "answer": "Pod autoscaling"
  },
  {
    "id": 206,
    "question": "Which GCP product provides managed container orchestration?",
    "options": [
      "App Engine",
      "Cloud Run",
      "GKE",
      "Dataproc"
    ],
    "answer": "GKE"
  },
  {
    "id": 207,
    "question": "Which YAML keyword in CircleCI allows matrix testing?",
    "options": [
      "matrix",
      "parallelism",
      "docker",
      "executor"
    ],
    "answer": "matrix"
  },
  {
    "id": 208,
    "question": "What prevents recursive CI/CD triggers in multi-branch workflows?",
    "options": [
      "Tag filtering",
      "Branch protections",
      "Skip CI directives",
      "Pipeline guards"
    ],
    "answer": "Skip CI directives"
  },
  {
    "id": 209,
    "question": "Which API object allows encrypted secret mounting into containers?",
    "options": [
      "SecretVolume",
      "ConfigMap",
      "PersistentVolume",
      "ClusterRole"
    ],
    "answer": "SecretVolume"
  },
  {
    "id": 210,
    "question": "Which method secures SSH access through one-time vault credentials?",
    "options": [
      "OTP SSH helper",
      "IAM proxying",
      "EC2 key injection",
      "Cloud bastion"
    ],
    "answer": "OTP SSH helper"
  },

  // Questions 211–300 to follow in the next message...

  {
    "id": 300,
    "question": "What mechanism prevents unintentional Terraform drift during deployment?",
    "options": [
      "State locking",
      "Lifecycle ignore_changes",
      "Remote backend checks",
      "Explicit refresh"
    ],
    "answer": "Lifecycle ignore_changes"
  }
]
[
  {
    "id": 379,
    "question": "What Helm CLI command previews manifest output without installing charts?",
    "options": [
      "helm render",
      "helm dry-run",
      "helm template",
      "helm preview"
    ],
    "answer": "helm template"
  },
  {
    "id": 312,
    "question": "Which container runtime replaced Docker in Kubernetes v1.24?",
    "options": [
      "CRI-O",
      "containerd",
      "rkt",
      "gVisor"
    ],
    "answer": "containerd"
  },
  {
    "id": 331,
    "question": "Which kubectl flag allows context switching across multiple clusters?",
    "options": [
      "--kube-context",
      "--context",
      "--cluster-name",
      "--namespace"
    ],
    "answer": "--context"
  },
  {
    "id": 398,
    "question": "What Git config setting avoids overwriting of divergent branches during push?",
    "options": [
      "push.default=simple",
      "pull.rebase=false",
      "merge.conflictstyle",
      "rebase.autostash"
    ],
    "answer": "push.default=simple"
  },
  {
    "id": 305,
    "question": "Which tool provisions infrastructure as code across multiple clouds using automation workflows?",
    "options": [
      "Crossplane",
      "Pulumi",
      "Chef",
      "Nomad"
    ],
    "answer": "Pulumi"
  },
  {
    "id": 367,
    "question": "Which filesystem driver is best suited for container layered storage?",
    "options": [
      "aufs",
      "zfs",
      "btrfs",
      "overlay2"
    ],
    "answer": "overlay2"
  },
  {
    "id": 346,
    "question": "Which Jenkins plugin manages secret injection into pipeline environments?",
    "options": [
      "HashiCorp Vault",
      "Credentials Binding",
      "Environment Injector",
      "KubeSecretManager"
    ],
    "answer": "Credentials Binding"
  },
  {
    "id": 392,
    "question": "Which ArgoCD feature prevents resource deletions during synchronization?",
    "options": [
      "SelfHeal",
      "Prune=false",
      "IgnoreDifferences",
      "ValidateOnly"
    ],
    "answer": "Prune=false"
  },
  {
    "id": 321,
    "question": "Which protocol is commonly used by node exporters to expose metrics?",
    "options": [
      "HTTP",
      "gRPC",
      "UDP",
      "NATS"
    ],
    "answer": "HTTP"
  },
  {
    "id": 352,
    "question": "Which Terraform feature can reduce costs by simulating plan without applying?",
    "options": [
      "terraform plan",
      "terraform graph",
      "terraform validate",
      "terraform cost-estimate"
    ],
    "answer": "terraform plan"
  },

  {
    "id": 400,
    "question": "Which GCP resource enables secure VM access without managing SSH keys manually?",
    "options": [
      "OS Login",
      "IAP Tunnel",
      "Cloud Identity",
      "Metadata script"
    ],
    "answer": "OS Login"
  }
]
{"id":379,"question":"What Helm CLI command previews manifest output without installing charts?","options":["helm render","helm dry-run","helm template","helm preview"],"answer":"helm template"}
{"id":312,"question":"Which container runtime replaced Docker in Kubernetes v1.24?","options":["CRI-O","containerd","rkt","gVisor"],"answer":"containerd"}
{"id":331,"question":"Which kubectl flag allows context switching across multiple clusters?","options":["--kube-context","--context","--cluster-name","--namespace"],"answer":"--context"}
{"id":398,"question":"What Git config setting avoids overwriting of divergent branches during push?","options":["push.default=simple","pull.rebase=false","merge.conflictstyle","rebase.autostash"],"answer":"push.default=simple"}
{"id":305,"question":"Which tool provisions infrastructure as code across multiple clouds using automation workflows?","options":["Crossplane","Pulumi","Chef","Nomad"],"answer":"Pulumi"}
{"id":367,"question":"Which filesystem driver is best suited for container layered storage?","options":["aufs","zfs","btrfs","overlay2"],"answer":"overlay2"}
{"id":346,"question":"Which Jenkins plugin manages secret injection into pipeline environments?","options":["HashiCorp Vault","Credentials Binding","Environment Injector","KubeSecretManager"],"answer":"Credentials Binding"}
{"id":392,"question":"Which ArgoCD feature prevents resource deletions during synchronization?","options":["SelfHeal","Prune=false","IgnoreDifferences","ValidateOnly"],"answer":"Prune=false"}
{"id":321,"question":"Which protocol is commonly used by node exporters to expose metrics?","options":["HTTP","gRPC","UDP","NATS"],"answer":"HTTP"}
{"id":352,"question":"Which Terraform feature can reduce costs by simulating plan without applying?","options":["terraform plan","terraform graph","terraform validate","terraform cost-estimate"],"answer":"terraform plan"}
{"id":400,"question":"Which GCP resource enables secure VM access without managing SSH keys manually?","options":["OS Login","IAP Tunnel","Cloud Identity","Metadata script"],"answer":"OS Login"}
{"id":437,"question":"Which cloud-native tool observes distributed trace propagation for microservices?","options":["Jaeger","Fluentd","Elasticsearch","Logrotate"],"answer":"Jaeger"}
{"id":418,"question":"Which Linux command forcefully releases file descriptor locks?","options":["fuser","ulimit","flock","lsof"],"answer":"fuser"}
{"id":456,"question":"Which component in Spinnaker automates deployment pipelines?","options":["Orca","Kayenta","Clouddriver","Front50"],"answer":"Orca"}
{"id":405,"question":"Which configuration ensures OpenID tokens expire automatically post login?","options":["TokenTTL","SessionDuration","IDTokenExpiry","AccessLifespan"],"answer":"SessionDuration"}
{"id":472,"question":"Which concept in Git maintains clean history during collaborative rebases?","options":["Interactive","Rewritten","Detached","Squashed"],"answer":"Interactive"}
{"id":431,"question":"Which GCP mechanism ensures IAM policies propagate consistently?","options":["Policy Bindings","Inherited Roles","Org Constraints","Resource Hierarchy"],"answer":"Resource Hierarchy"}
{"id":499,"question":"Which setting limits Prometheus retention period for metrics?","options":["--storage.tsdb.retention","--data-ttl","--metrics-expiry","--scrape-limit"],"answer":"--storage.tsdb.retention"}
{"id":421,"question":"Which artifact repository format does JFrog Artifactory support for Docker images?","options":["OCI","Tarball","Blobstore","ManifestV2"],"answer":"OCI"}
{"id":466,"question":"Which Kubernetes scheduling policy favors least allocated CPU node?","options":["LeastRequestedPriority","BalancedResourceAllocation","NodeAffinity","SpreadConstraint"],"answer":"LeastRequestedPriority"}
{"id":414,"question":"Which tool emulates full AWS environment locally for testing?","options":["LocalStack","Minio","Moto","MockAWS"],"answer":"LocalStack"}
{"id":486,"question":"Which method prevents concurrency issues in Terraform parallel apply?","options":["State Locking","Plan Isolation","Mutex Guarding","Graph Reordering"],"answer":"State Locking"}
{"id":453,"question":"Which format does Docker use internally to describe image manifests?","options":["JSON Schema","ImageSpec","ManifestV2","OCI Descriptor"],"answer":"ManifestV2"}
{"id":489,"question":"Which component in Helm helps define reusable logic blocks?","options":["_helpers.tpl","values.yaml","Chart.yaml","global block"],"answer":"_helpers.tpl"}
{"id":447,"question":"Which plugin secures Jenkins secrets with Vault backend integration?","options":["Vault Credentials","HashiPlugin","SecureStore","SecretInjector"],"answer":"Vault Credentials"}
{"id":474,"question":"Which Linux feature provides security context isolation between containers?","options":["Seccomp","AppArmor","SELinux","Namespaces"],"answer":"Namespaces"}
{"id":462,"question":"Which Prometheus exporter collects metrics from NodeJS applications?","options":["prom-client","node_exporter","express-metrics","prom-node"],"answer":"prom-client"}
{"id":407,"question":"Which AWS CLI flag ensures idempotent stack creation in CloudFormation?","options":["--capabilities","--client-request-token","--on-failure","--disable-rollback"],"answer":"--client-request-token"}
{"id":494,"question":"Which DevOps tool provides blueprint templates for service scaffolding?","options":["Cookiecutter","Backstage","Hygen","Plop"],"answer":"Backstage"}
{"id":445,"question":"Which git configuration disables auto-merge conflict markers?","options":["merge.conflictstyle=diff3","rerere.enabled=false","merge.autoStash=false","merge.tool=manual"],"answer":"merge.conflictstyle=diff3"}
{"id":401,"question":"Which utility manages Linux audit framework rules?","options":["auditctl","journald","auditd","syslog-ng"],"answer":"auditctl"}
{"id":463,"question":"Which CLI validates Kubernetes admission controllers configuration?","options":["kubeadm","kubectl","kube-apiserver","kube-bench"],"answer":"kube-apiserver"}
{"id":498,"question":"Which Kubernetes API object defines volume snapshot schedules?","options":["VolumeSnapshotClass","VolumeBackupPolicy","PersistentSnapshot","SnapshotSchedule"],"answer":"VolumeSnapshotClass"}
{"id":409,"question":"Which open-source software provides automated chaos experiments in Kubernetes?","options":["LitmusChaos","Gremlin","ChaosBlade","KubeMonkey"],"answer":"LitmusChaos"}
{"id":477,"question":"Which GitLab concept allows infra provisioning via Terraform state integration?","options":["Remote Backend","State Locking","Terraform Module","Infrastructure-as-Code"],"answer":"Remote Backend"}
{"id":451,"question":"Which Jenkins agent launch method runs via WebSocket when firewall blocks JNLP?","options":["Tunnel","SSH","Inbound","WebSocket"],"answer":"WebSocket"}
{"id":417,"question":"Which API version controls CRD lifecycle in Kubernetes?","options":["v1","v1beta1","apiextensions.k8s.io","apps/v1"],"answer":"apiextensions.k8s.io"}
{"id":490,"question":"Which tool generates dynamic AWS IAM policies from Terraform state?","options":["PolicySentry","InfraPolicy","IAMAudit","TF-IAM"],"answer":"PolicySentry"}
{"id":420,"question":"Which resource type in GKE enforces cluster autoscaler behavior?","options":["NodePool","ManagedGroup","AutoNodeSet","ClusterScaler"],"answer":"NodePool"}
{"id":484,"question":"Which HTTP status code indicates ArgoCD sync error from webhook timeout?","options":["408","504","422","503"],"answer":"504"}
{"id":443,"question":"Which kubectl plugin discovers unused resource definitions in namespaces?","options":["kubectl-prune","kubectl-tree","kubectl-unused","kubectl-unused-resources"],"answer":"kubectl-unused-resources"}
{"id":476,"question":"Which Git strategy avoids duplicate commits during rebasing?","options":["Rebase-merge","Fast-forward","Interactive","Onto"],"answer":"Fast-forward"}
{"id":426,"question":"Which parameter adjusts Ansible verbosity during playbook execution?","options":["-v","-d","--debug","--trace"],"answer":"-v"}
{"id":423,"question":"Which Kubernetes metric type represents histogram buckets?","options":["Summary","Gauge","Histogram","Timer"],"answer":"Histogram"}
{"id":469,"question":"Which AWS construct ensures temporary permissions for cross-account roles?","options":["AssumeRole","Federation","STS","IdentityBroker"],"answer":"AssumeRole"}
{"id":491,"question":"Which Jenkins construct avoids simultaneous job execution for a specific resource?","options":["Throttle","Resource Locking","Executor Pool","Concurrency Guard"],"answer":"Resource Locking"}
{"id":416,"question":"Which Bash syntax prevents script exit on pipeline error?","options":["set +e","trap ERR","|| true","set -o pipefail"],"answer":"set +e"}
{"id":429,"question":"Which config prevents container privilege escalation in pod spec?","options":["allowPrivilegeEscalation: false","runAsNonRoot: true","securityContext: drop","capabilities: none"],"answer":"allowPrivilegeEscalation: false"}
{"id":497,"question":"Which HTTP header is used by Kubernetes for client certificate authentication?","options":["X-Remote-User","X-Auth-Token","Authorization","X-Client-Cert"],"answer":"X-Remote-User"}
{"id":402,"question":"Which Linux mechanism ensures predictable device naming across boots?","options":["udev","systemd","devtmpfs","sysfs"],"answer":"udev"}
{"id":471,"question":"Which S3 event triggers Lambda for new object uploads?","options":["s3:ObjectCreated:*","s3:NewUpload","s3:PutObject","s3:ObjectPut"],"answer":"s3:ObjectCreated:*"}
{"id":442,"question":"Which parameter enables Airflow DAG retries after transient failure?","options":["retry_delay","retry_interval","max_retries","delay_seconds"],"answer":"retry_delay"}
{"id":428,"question":"Which command-line flag disables container DNS search domain injection?","options":["--dns-opt","--no-search","--disable-search","--dns-search=false"],"answer":"--dns-opt"}
{"id":434,"question":"Which method allows GKE workload identity mapping to service accounts?","options":["Workload Identity Binding","IAM Service Projection","Kubernetes Federation","Pod IAM Delegation"],"answer":"Workload Identity Binding"}
{"id":424,"question":"Which kubelet flag sets eviction thresholds for memory pressure?","options":["--eviction-hard","--memory-limit","--oom-threshold","--memory-throttle"],"answer":"--eviction-hard"}
{"id":487,"question":"Which plugin verifies OpenPolicyAgent constraints in admission requests?","options":["Gatekeeper","OPA-Webhook","K-RBAC","AdmissionPolicy"],"answer":"Gatekeeper"}
{"id":408,"question":"Which Consul feature performs DNS-based service discovery?","options":["Consul DNS","Service Resolver","Discovery Agent","Mesh Catalog"],"answer":"Consul DNS"}
{"id":432,"question":"Which Kubernetes method manages resource limits at namespace level?","options":["LimitRange","ResourceQuota","PodPreset","NamespacePolicy"],"answer":"ResourceQuota"}
{"id":495,"question":"Which pipeline construct in Tekton defines step-level execution logic?","options":["Task","PodTemplate","PipelineRun","StepDefinition"],"answer":"Task"}
{"id":538,"question":"Which Ansible lookup plugin fetches vault-encrypted variables securely?","options":["lookup('ansible.builtin.vault')","lookup('community.vault')","lookup('env')","lookup('secrets')"],"answer":"lookup('community.vault')"}
{"id":579,"question":"Which Kustomize patch type updates Deployment replica count?","options":["StrategicMerge","JSON6902","PatchTransformer","OverlayPatch"],"answer":"StrategicMerge"}
{"id":556,"question":"Which cloud-native solution provides log routing via CRDs and Kubernetes operators?","options":["Fluent Bit Operator","Vector","LokiStack","KubeLog"],"answer":"Fluent Bit Operator"}
{"id":501,"question":"Which GitHub feature requires successful checks before merging pull requests?","options":["Branch protection","Status gate","Push policy","Review rules"],"answer":"Branch protection"}
{"id":574,"question":"Which container image scanner performs in-depth SBOM analysis?","options":["Trivy","Grype","Clair","Anchore"],"answer":"Grype"}
{"id":523,"question":"Which CI pipeline attribute skips cache restoration in GitHub Actions?","options":["restore-keys","cache-hit","skip-restore","no-cache"],"answer":"cache-hit"}
{"id":583,"question":"Which Kubernetes concept enables multi-tenancy isolation per environment?","options":["Namespace","ClusterRole","TenantSet","EnvironmentPool"],"answer":"Namespace"}
{"id":507,"question":"Which GCP flag enables minimal container image size for Cloud Run deployments?","options":["--allow-unauthenticated","--memory","--platform","--no-cloud-logging"],"answer":"--no-cloud-logging"}
{"id":593,"question":"Which OpenShift resource automates image trigger-based rollouts?","options":["ImageStream","DeploymentConfig","TriggerBinding","BuildHook"],"answer":"DeploymentConfig"}
{"id":519,"question":"Which shell construct evaluates exit codes in multi-command pipelines?","options":["pipefail","exittrap","&&","catch"],"answer":"pipefail"}
{"id":544,"question":"Which Kubernetes volume type is best suited for read-only configuration data?","options":["ConfigMap","emptyDir","HostPath","PersistentVolume"],"answer":"ConfigMap"}
{"id":533,"question":"Which Jenkinsfile section defines tool installation like Maven or NodeJS?","options":["tools","environment","agent","stage"],"answer":"tools"}
{"id":590,"question":"Which monitoring method alerts on anomaly detection using Prometheus rules?","options":["Threshold-based","Predictive","Statistical","Outlier"],"answer":"Statistical"}
{"id":536,"question":"Which Ingress annotation enables client IP forwarding in NGINX controller?","options":["nginx.ingress.kubernetes.io/forwarded-for-header","nginx.ingress.kubernetes.io/use-forwarded-headers","nginx.ingress.kubernetes.io/x-forwarded-for","nginx.ingress.kubernetes.io/client-ip-header"],"answer":"nginx.ingress.kubernetes.io/use-forwarded-headers"}
{"id":582,"question":"Which configuration field sets container lifecycle hook pre-start logic?","options":["lifecycle.preStart","startupCommand","hookCommand","initHook"],"answer":"lifecycle.preStart"}
{"id":514,"question":"Which Helm value type accepts arbitrary key-value nested maps?","options":["dict","map","object","yaml"],"answer":"map"}
{"id":599,"question":"Which tool allows centralized Kubernetes policy enforcement using Rego?","options":["Gatekeeper","OPA-K8s","KubePolicy","PolicyController"],"answer":"Gatekeeper"}
{"id":532,"question":"Which Terraform command checks syntax and argument correctness?","options":["terraform validate","terraform fmt","terraform init","terraform check"],"answer":"terraform validate"}
{"id":568,"question":"Which S3 setting ensures deletion protection for accidental data loss?","options":["Versioning","MFA-Delete","Retention","Immutable Lock"],"answer":"MFA-Delete"}
{"id":509,"question":"Which DevOps methodology promotes ephemeral environments via pull requests?","options":["Preview Environments","Dynamic Review","Branch Deploy","On-Demand Staging"],"answer":"Preview Environments"}
{"id":525,"question":"Which Git command rewords last commit message without changing content?","options":["git commit --amend","git reword","git message","git change-log"],"answer":"git commit --amend"}
{"id":562,"question":"Which tool decodes JWT tokens via CLI without external dependencies?","options":["jwt-cli","decode-jwt","jwt-decoder","tokentool"],"answer":"jwt-cli"}
{"id":517,"question":"Which CRI-compatible tool allows runtime benchmarking of container startup time?","options":["crun-bench","ctr","crictl","containerd-bench"],"answer":"crictl"}
{"id":558,"question":"Which setting in Prometheus prevents query overloads via cardinality limits?","options":["query.maxSeries","max_samples","limit_series","sample_cap"],"answer":"max_samples"}
{"id":587,"question":"Which Kubernetes admission webhook mutates resource definitions at runtime?","options":["MutatingAdmissionWebhook","ValidateAndMutate","KubeMutator","WebhookMutator"],"answer":"MutatingAdmissionWebhook"}
{"id":504,"question":"Which container orchestrator runs without a centralized control plane?","options":["Nomad","Docker Swarm","K3s","Supervisord"],"answer":"Nomad"}
{"id":546,"question":"Which database supports time-series metrics storage optimized for Grafana?","options":["InfluxDB","ClickHouse","VictoriaMetrics","TimescaleDB"],"answer":"InfluxDB"}
{"id":580,"question":"Which Terraform feature splits infrastructure into manageable blueprints?","options":["Modules","Stacks","Blocks","Layouts"],"answer":"Modules"}
{"id":564,"question":"Which open-source CLI audits Kubernetes security posture using benchmarks?","options":["kube-bench","kubescape","kubeaudit","kubesec"],"answer":"kube-bench"}
{"id":540,"question":"Which DNS service provides recursive resolution with caching and DoH support?","options":["CoreDNS","dnsmasq","Unbound","PowerDNS"],"answer":"Unbound"}
{"id":552,"question":"Which CI/CD strategy validates pull request changes before merging to main?","options":["Pre-submit","Pre-merge","Check-before-merge","Pre-flight"],"answer":"Pre-submit"}
{"id":534,"question":"Which config file sets environment variables for containerized NodeJS apps in Kubernetes?","options":["envFrom","configMapRef","app.env","env-file"],"answer":"envFrom"}
{"id":510,"question":"Which Git config disables tracking of unmerged commits during fetch?","options":["fetch.prune","merge.avoid","pull.skip","rebase.omit"],"answer":"fetch.prune"}
{"id":577,"question":"Which plugin collects logs from Windows nodes into ELK stack?","options":["Winlogbeat","Nxlog","FluentdWin","ElasticAgent"],"answer":"Winlogbeat"}
{"id":595,"question":"Which build tool uses a `build.sbt` file for Scala-based microservices?","options":["sbt","mill","maven-scala","bazel"],"answer":"sbt"}
{"id":521,"question":"Which Docker Compose setting declares network driver per service?","options":["driver","net_mode","service_network","net_driver"],"answer":"driver"}
{"id":597,"question":"Which tool observes Kubernetes audit logs for anomalous API access?","options":["Falco","Auditbeat","KubeHound","GuardDog"],"answer":"Falco"}
{"id":530,"question":"Which Argo Workflow template type enables DAG-style task chaining?","options":["dag","steps","workflow","pipelinerun"],"answer":"dag"}
{"id":541,"question":"Which method avoids version conflicts in shared Python virtual environments?","options":["pyenv-virtualenv","venv","poetry","pipenv"],"answer":"pyenv-virtualenv"}
{"id":581,"question":"Which service type allows exposing Kubernetes workloads externally via LoadBalancer?","options":["ClusterIP","NodePort","ExternalName","LoadBalancer"],"answer":"LoadBalancer"}
{"id":566,"question":"Which annotation prevents autoscaler from modifying specific Kubernetes pods?","options":["cluster-autoscaler.kubernetes.io/safe-to-evict","autoscaling.k8s.io/ignore","no-scale","safe-to-skip"],"answer":"cluster-autoscaler.kubernetes.io/safe-to-evict"}
{"id":506,"question":"Which Ansible module manages EC2 instance lifecycle declaratively?","options":["ec2_instance","ec2_lifecycle","aws_vm","ec2_manage"],"answer":"ec2_instance"}
{"id":520,"question":"Which CI/CD tool manages pipelines using .drone.yml files?","options":["Drone","Concourse","Tekton","Woodpecker"],"answer":"Drone"}
{"id":515,"question":"Which config flag enables Terraform to skip backend reinitialization?","options":["-reconfigure=false","-force-copy","-skip-backend","-migrate-state=false"],"answer":"-migrate-state=false"}
{"id":529,"question":"Which Vault auth method uses cloud-native identity verification for AWS EC2?","options":["IAM Auth","EC2 Auth","Cloud Identity","Instance Metadata"],"answer":"EC2 Auth"}
{"id":535,"question":"Which protocol does Envoy proxy use to communicate with xDS management servers?","options":["gRPC","HTTP2","UDP","Thrift"],"answer":"gRPC"}
{"id":553,"question":"Which GitHub feature allows commenting on lines of code inside pull requests?","options":["Inline Comments","Line Notes","Code Review","Diff Annotations"],"answer":"Inline Comments"}
{"id":508,"question":"Which option allows kubectl to wait for resource status condition?","options":["--wait=true","--for=condition","--watch","--status=ready"],"answer":"--for=condition"}
{"id":526,"question":"Which Kubernetes mechanism restricts container access to host namespaces?","options":["SecurityContext","PodSecurityPolicy","RunAsGroup","HostPID=false"],"answer":"PodSecurityPolicy"}
{"id":601,"question":"Which Prometheus component performs alert rule evaluation on time series data?","options":["Alerting Engine","Rule Evaluator","Alertmanager","TSDB"],"answer":"Rule Evaluator"}
{"id":602,"question":"Which Kubernetes field guarantees container restart on failure but not on exit 0?","options":["restartPolicy: OnFailure","alwaysRestart: true","policy: retry","exitHook: enabled"],"answer":"restartPolicy: OnFailure"}
{"id":603,"question":"Which open-source project provisions GitOps workflows via pull request triggers?","options":["FluxCD","Werf","ArgoCD","Flagger"],"answer":"FluxCD"}
{"id":604,"question":"Which tool allows scanning of Terraform plans for misconfigured resources?","options":["Tfsec","TFSentinel","PolicyCheck","InfraScan"],"answer":"Tfsec"}
{"id":605,"question":"Which CLI tool provides interactive debugging of container networks?","options":["nsenter","netshoot","tcpdump","ctr netns"],"answer":"netshoot"}
{"id":606,"question":"Which Kubernetes resource creates periodic Jobs based on cron schedule?","options":["CronJob","JobScheduler","ScheduledPod","TimedJob"],"answer":"CronJob"}
{"id":607,"question":"Which Spinnaker microservice interacts with Kubernetes for deployment operations?","options":["Clouddriver","Echo","Orca","Fiat"],"answer":"Clouddriver"}
{"id":608,"question":"Which AWS CLI command syncs S3 bucket contents recursively?","options":["aws s3 sync","aws s3 cp --recursive","aws sync s3","aws s3 mirror"],"answer":"aws s3 sync"}
{"id":609,"question":"Which Docker option prevents container daemon from logging stdout?","options":["--log-driver=none","--detach=true","--silent","--no-stdout"],"answer":"--log-driver=none"}
{"id":610,"question":"Which GKE configuration ensures regional control plane availability?","options":["Regional Cluster","HA Mode","Zonal Redundancy","MultiZone"],"answer":"Regional Cluster"}
{"id":611,"question":"Which Helm concept enables multiple chart deployments with parameter overrides?","options":["Release","Instance","ChartGroup","ValuesBundle"],"answer":"Release"}
{"id":612,"question":"Which GitLab feature provides audit log tracking for pipeline executions?","options":["Audit Events","Job Logs","CI Inspector","Trace Report"],"answer":"Audit Events"}
{"id":613,"question":"Which logging backend supports structured JSON ingestion for container output?","options":["Loki","Stackdriver","Graylog","Logstash"],"answer":"Logstash"}
{"id":614,"question":"Which file defines default environment for Terraform Cloud runs?","options":["terraform.tfvars",".terraform/environment","backend.hcl","env.auto.tfvars"],"answer":"env.auto.tfvars"}
{"id":615,"question":"Which Jenkins setting allows reuse of workspace between builds?","options":["reuseNode","workspaceReuse","cacheWorkspace","reuseWorkspace"],"answer":"reuseNode"}
{"id":616,"question":"Which command enables dynamic port forwarding via SSH tunnel?","options":["ssh -D","ssh -L","ssh -R","ssh -T"],"answer":"ssh -D"}
{"id":617,"question":"Which Kubernetes admission controller checks container image registries?","options":["ImagePolicyWebhook","RegistryGuard","AdmissionScan","SecureImage"],"answer":"ImagePolicyWebhook"}
{"id":618,"question":"Which flag prevents docker-compose from recreating unchanged services?","options":["--no-recreate","--skip-rebuild","--preserve","--keep"],"answer":"--no-recreate"}
{"id":619,"question":"Which Linux tool collects system performance snapshots periodically?","options":["sysstat","iostat","sar","perfmon"],"answer":"sar"}
{"id":620,"question":"Which Git hook runs before a push operation is executed?","options":["pre-push","pre-commit","post-checkout","update"],"answer":"pre-push"}
{"id":621,"question":"Which CI/CD strategy promotes successful builds to production without delay?","options":["Continuous Deployment","Auto Promotion","Rapid Delivery","Instant Rollout"],"answer":"Continuous Deployment"}
{"id":622,"question":"Which config file does Docker use to load custom daemon settings?","options":["daemon.json","docker.conf","dockerd.yaml","engine.cfg"],"answer":"daemon.json"}
{"id":623,"question":"Which Terraform block fetches secrets from external shell scripts?","options":["external data source","script backend","shell_input","remote_exec"],"answer":"external data source"}
{"id":624,"question":"Which tool analyzes Kubernetes RBAC for excessive permission exposure?","options":["rbac-lookup","rbac-police","kubent","kube-rbac-audit"],"answer":"kube-rbac-audit"}
{"id":625,"question":"Which Git strategy flattens all commits into a single patch before merge?","options":["Squash Merge","Rebase Interactive","Flat Merge","Patch Stack"],"answer":"Squash Merge"}
{"id":626,"question":"Which pipeline tool allows dynamic parallelism using matrix expansion?","options":["CircleCI","DroneCI","GitHub Actions","GitLab CI"],"answer":"GitHub Actions"}
{"id":627,"question":"Which annotation allows sidecar injection to be skipped in Istio?","options":["sidecar.istio.io/inject: false","istio-injection: disabled","skip-injection: true","no-sidecar: true"],"answer":"sidecar.istio.io/inject: false"}
{"id":628,"question":"Which OpenTelemetry component collects spans from instrumented services?","options":["Collector","Exporter","Sampler","SpanReader"],"answer":"Collector"}
{"id":629,"question":"Which Kubernetes controller monitors etcd state for object reconciliation?","options":["Controller Manager","Reconciler","State Syncer","Kube Watcher"],"answer":"Controller Manager"}
{"id":630,"question":"Which container networking technology allocates IPs at pod-level in AWS EKS?","options":["CNI","ENI","Bridge","Veth"],"answer":"CNI"}
{"id":631,"question":"Which configuration in Jenkinsfile defines global environment variables?","options":["environment","globalEnv","envVars","vars"],"answer":"environment"}
{"id":632,"question":"Which Linux feature allows grouping of processes for resource isolation?","options":["cgroups","namespaces","isolators","slices"],"answer":"cgroups"}
{"id":633,"question":"Which K8s object ensures exclusive pod placement on specific nodes?","options":["nodeAffinity","nodeSelector","taints","tolerations"],"answer":"nodeSelector"}
{"id":634,"question":"Which feature in Azure DevOps enables YAML pipeline reuse across repositories?","options":["template","extends","includes","shared-config"],"answer":"template"}
{"id":635,"question":"Which container tool provides minimal OS base images with CVE scanning?","options":["Distroless","Alpine","Slim","Bottlerocket"],"answer":"Distroless"}
{"id":636,"question":"Which configuration lets you pass Helm values using environment variables?","options":["--set-env","--values-env","envsubst + -f","helm template + export"],"answer":"envsubst + -f"}
{"id":637,"question":"Which Prometheus feature calculates instant rate of time series changes?","options":["rate()","delta()","irate()","change()"],"answer":"irate()"}
{"id":638,"question":"Which Vault backend stores credentials using cloud-native encryption services?","options":["KMS","Transit","Secrets Engine","CloudKey"],"answer":"Transit"}
{"id":639,"question":"Which Git command removes tracking of a deleted branch from origin?","options":["git remote prune origin","git clean -d","git fetch --delete","git branch --remove"],"answer":"git remote prune origin"}
{"id":640,"question":"Which Terraform lifecycle setting delays deletion until after replacement?","options":["create_before_destroy","prevent_destroy","ignore_changes","delayed_replacement"],"answer":"create_before_destroy"}
{"id":641,"question":"Which Jenkins executor label restricts job execution to certain agents?","options":["node label","restrict label","agent filter","build tag"],"answer":"node label"}
{"id":642,"question":"Which cloud-native service mesh enables transparent mTLS between services?","options":["Istio","Linkerd","Consul Connect","Traefik Mesh"],"answer":"Istio"}
{"id":643,"question":"Which Terraform construct controls module instantiation using loops?","options":["for_each","repeat","loop","foreach_resource"],"answer":"for_each"}
{"id":644,"question":"Which kustomize command displays final manifest after all overlays?","options":["kustomize build","kustomize render","kustomize apply --dry-run","kustomize compile"],"answer":"kustomize build"}
{"id":645,"question":"Which container runtime provides rootless container support natively?","options":["Podman","Docker","rkt","CRI-O"],"answer":"Podman"}
{"id":646,"question":"Which OpenShift CLI command triggers a manual build for an image stream?","options":["oc start-build","oc trigger","oc image-build","oc manual-build"],"answer":"oc start-build"}
{"id":647,"question":"Which Prometheus exporter monitors JVM metrics like heap and GC?","options":["jmx_exporter","java_metrics","jvm_exporter","metrics4j"],"answer":"jmx_exporter"}
{"id":648,"question":"Which Git feature allows rewriting commit timestamps and authors?","options":["git rebase --interactive","git filter-branch","git amend","git restore-history"],"answer":"git filter-branch"}
{"id":649,"question":"Which Azure DevOps feature defines parallel jobs matrix using YAML?","options":["strategy.matrix","run.parallel","matrix.jobs","template.loop"],"answer":"strategy.matrix"}
{"id":650,"question":"Which shell command lists current ulimit settings for user processes?","options":["ulimit -a","limit","env | grep ulimit","procstatus"],"answer":"ulimit -a"}
{"id":651,"question":"Which Linux file defines static hostname information on most distributions?","options":["/etc/hostname","/etc/hosts","/etc/sysconfig/network","/etc/netname"],"answer":"/etc/hostname"}
{"id":652,"question":"Which kubectl command views pending events of a specific namespace?","options":["kubectl get events --field-selector type=Warning","kubectl describe ns","kubectl logs ns","kubectl ns-events"],"answer":"kubectl get events --field-selector type=Warning"}
{"id":653,"question":"Which security scanner checks known CVEs in base OS packages of containers?","options":["Trivy","Dockle","Hadolint","OpenSCAP"],"answer":"Trivy"}
{"id":654,"question":"Which Jenkins plugin provides shared libraries for reusing pipeline code?","options":["Pipeline Shared Groovy","Shared Libraries","Reusable Code","Global Pipeline"],"answer":"Shared Libraries"}
{"id":655,"question":"Which Linux scheduling policy ensures fixed-priority real-time processes?","options":["SCHED_FIFO","SCHED_OTHER","SCHED_NORMAL","SCHED_RR"],"answer":"SCHED_FIFO"}
{"id":656,"question":"Which tool provides a web UI to visualize Terraform plan and apply changes?","options":["Terraform Cloud","Atlantis","Terraboard","InfraVis"],"answer":"Terraboard"}
{"id":657,"question":"Which file extension is used by Helm chart values override files?","options":[".yaml",".json",".env",".override"],"answer":".yaml"}
{"id":658,"question":"Which Dockerfile instruction copies a local folder recursively to image?","options":["COPY","ADD","PUSH","INCLUDE"],"answer":"COPY"}
{"id":659,"question":"Which Linux package manager resolves RPM-based dependencies on RHEL?","options":["dnf","apt","zypper","brew"],"answer":"dnf"}
{"id":660,"question":"Which CI tool supports GoCD-style value stream mapping and artifact tracing?","options":["GoCD","Concourse","JenkinsX","Tekton"],"answer":"GoCD"}
{"id":661,"question":"Which Kubernetes controller ensures requested replicas are always running?","options":["ReplicaSet","Deployment","Job","PodDisruptionBudget"],"answer":"ReplicaSet"}
{"id":662,"question":"Which Git command displays commit ancestry as a tree-like structure?","options":["git log --graph","git show-tree","git reflog","git branch-tree"],"answer":"git log --graph"}
{"id":663,"question":"Which Linux daemon manages encrypted volumes using LUKS at boot?","options":["cryptsetup","systemd-cryptsetup","luksctl","dmcrypt"],"answer":"systemd-cryptsetup"}
{"id":664,"question":"Which Ansible module manages line entries inside config files idempotently?","options":["lineinfile","blockinfile","replace","fileentry"],"answer":"lineinfile"}
{"id":665,"question":"Which logging pattern prevents log injection in structured JSON outputs?","options":["Sanitization","Escaping","Field Masking","Log Normalization"],"answer":"Escaping"}
{"id":666,"question":"Which GitHub Actions command uploads test artifacts to the runner?","options":["actions/upload-artifact","run.upload","save-artifact","send-output"],"answer":"actions/upload-artifact"}
{"id":667,"question":"Which command enables on-demand metrics scraping from a pod's endpoint?","options":["curl /metrics","promql query","scrape-now","kubectl port-forward + curl"],"answer":"kubectl port-forward + curl"}
{"id":668,"question":"Which AWS feature groups IAM users under common policy scope?","options":["IAM Group","Access Set","RoleBundle","PolicyGroup"],"answer":"IAM Group"}
{"id":669,"question":"Which pipeline-as-code engine powers Jenkins X internally?","options":["Tekton","Argo","Concourse","Drone"],"answer":"Tekton"}
{"id":670,"question":"Which Vault concept ensures data is unseal-able only with quorum?","options":["Shamir's Secret Sharing","Vault Token","Master Key","Key Split"],"answer":"Shamir's Secret Sharing"}
{"id":671,"question":"Which CI/CD concept defines promotion from staging to production on approval?","options":["Manual Gate","Approval Step","Release Strategy","Change Control"],"answer":"Manual Gate"}
{"id":672,"question":"Which Kubernetes scheduler configuration balances pods based on custom weights?","options":["Scoring Function","Custom Plugin","Extender","Weight-based Filter"],"answer":"Scoring Function"}
{"id":673,"question":"Which tool converts Docker Compose files into Kubernetes YAML?","options":["kompose","helmify","dock2kube","compose2k8s"],"answer":"kompose"}
{"id":674,"question":"Which container runtime is used under the hood by OpenShift 4+?","options":["CRI-O","containerd","runc","Docker"],"answer":"CRI-O"}
{"id":675,"question":"Which cloud-native log processor uses WebAssembly for custom filters?","options":["Vector","Fluent Bit","LogstashX","WASMLog"],"answer":"Vector"}
{"id":676,"question":"Which CLI command installs Tekton pipelines in a Kubernetes cluster?","options":["kubectl apply -f release.yaml","tkn install","tektonctl deploy","tkn apply"],"answer":"kubectl apply -f release.yaml"}
{"id":677,"question":"Which Linux command views I/O stats of devices interactively?","options":["iotop","iostat","blktrace","vmstat -d"],"answer":"iotop"}
{"id":678,"question":"Which Kubernetes CRD enables declarative deployment rollouts with analysis?","options":["Rollout","CanaryStrategy","AnalysisRun","BlueGreenStep"],"answer":"Rollout"}
{"id":679,"question":"Which Git feature supports signed commits and tag verification?","options":["GPG Key","SSH Signature","Verified Sign","Trusted Tag"],"answer":"GPG Key"}
{"id":680,"question":"Which setting in .gitignore ensures folder contents are ignored but folder remains?","options":["folder/*\n!folder/.gitkeep","folder/**\n!folder","folder/\n!important","folder/**\n!.keep"],"answer":"folder/*\n!folder/.gitkeep"}
{"id":681,"question":"Which HTTP header is inspected to determine client IP behind proxy in Kubernetes?","options":["X-Forwarded-For","X-Real-IP","X-Client-IP","Forwarded-For"],"answer":"X-Forwarded-For"}
{"id":682,"question":"Which Git command resets a file only from staging, not working directory?","options":["git reset HEAD <file>","git restore --staged <file>","git unstage","git unadd"],"answer":"git reset HEAD <file>"}
{"id":683,"question":"Which CLI option in kubectl disables validation against OpenAPI schema?","options":["--validate=false","--skip-schema","--force","--no-check"],"answer":"--validate=false"}
{"id":684,"question":"Which CI/CD pattern splits infrastructure, app, and secrets into separate pipelines?","options":["Pipeline Separation","Stage Isolation","Parallel CI","Split Delivery"],"answer":"Pipeline Separation"}
{"id":685,"question":"Which Git workflow requires each developer to push to their own fork?","options":["Fork and Pull","Feature Branch","Git Flow","Monorepo"],"answer":"Fork and Pull"}
{"id":686,"question":"Which AWS IAM entity provides temporary security credentials?","options":["Role","Session Token","Access Key","Federation"],"answer":"Role"}
{"id":687,"question":"Which tool tracks and enforces Open Policy Agent rules for Terraform configs?","options":["Conftest","TFSec","OPA Guard","TerraformPolicy"],"answer":"Conftest"}
{"id":688,"question":"Which Jenkins view displays visual pipeline execution graphically?","options":["Blue Ocean","Pipeline Graph View","Stage Monitor","Jenkins Dashboard"],"answer":"Blue Ocean"}
{"id":689,"question":"Which Docker Compose version introduced support for secrets?","options":["v3","v2.1","v3.1","v2"],"answer":"v3.1"}
{"id":690,"question":"Which Helm chart template function converts string to uppercase?","options":["upper","toupper","ToUpper","str_upper"],"answer":"upper"}
{"id":691,"question":"Which GitHub Actions event triggers workflow on forked repo pull request?","options":["pull_request","pull_request_target","forked_push","external_pr"],"answer":"pull_request_target"}
{"id":692,"question":"Which Kubernetes command creates a deployment from CLI without YAML?","options":["kubectl create deployment","kubectl run --image","kubectl init","kubectl deploy"],"answer":"kubectl create deployment"}
{"id":693,"question":"Which command shows full configuration and environment of a running container?","options":["docker inspect","docker config","docker env","docker meta"],"answer":"docker inspect"}
{"id":694,"question":"Which Terraform file keeps backend config when using remote state?","options":["backend.tf","provider.tf","state.tf","remote.tfvars"],"answer":"backend.tf"}
{"id":695,"question":"Which log level is most verbose in containerized applications?","options":["TRACE","DEBUG","INFO","VERBOSE"],"answer":"TRACE"}
{"id":696,"question":"Which cloud build tool supports buildpack-based images without Dockerfile?","options":["Cloud Native Buildpacks","Skaffold","Kaniko","Jib"],"answer":"Cloud Native Buildpacks"}
{"id":697,"question":"Which Kubernetes resource restricts Pod execution via hostname rules?","options":["PodSecurityPolicy","NetworkPolicy","HostAliases","AdmissionPolicy"],"answer":"PodSecurityPolicy"}
{"id":698,"question":"Which GitHub feature allows writing reusable action steps?","options":["Composite Actions","Reusable Steps","Action Modules","Common Tasks"],"answer":"Composite Actions"}
{"id":699,"question":"Which service exposes metrics to Prometheus for horizontal pod autoscaling?","options":["Metrics Server","Kube State Metrics","Heapster","Resource Exporter"],"answer":"Metrics Server"}
{"id":700,"question":"Which CI/CD tool supports native Helm deployment as pipeline step?","options":["Codefresh","Spinnaker","Flux","Harness"],"answer":"Codefresh"}
{"id":701,"question":"Which CI/CD feature performs rollback if health checks fail post-deploy?","options":["Automatic Rollback","Post-Deploy Check","Failure Recovery","HealthGuard"],"answer":"Automatic Rollback"}
{"id":702,"question":"Which Kubernetes API object controls access to resources via role bindings?","options":["ClusterRoleBinding","AccessPolicy","RoleAttachment","RBACRule"],"answer":"ClusterRoleBinding"}
{"id":703,"question":"Which GitLab keyword retries failed CI jobs automatically?","options":["retry","rerun","repeat","on_fail"],"answer":"retry"}
{"id":704,"question":"Which container scanning tool integrates with GitHub Code Scanning natively?","options":["Trivy","Snyk","Grype","Dockle"],"answer":"Snyk"}
{"id":705,"question":"Which log aggregator provides log correlation with distributed tracing support?","options":["Loki","New Relic","Elastic Observability","Datadog Logs"],"answer":"Datadog Logs"}
{"id":706,"question":"Which Helm command verifies chart dependencies are installed properly?","options":["helm dependency list","helm dependency update","helm verify","helm check-deps"],"answer":"helm dependency update"}
{"id":707,"question":"Which Open Policy Agent feature allows bundling policies with data?","options":["Policy Bundle","OPA Package","Data Inclusion","Bundle Mode"],"answer":"Policy Bundle"}
{"id":708,"question":"Which Git command changes the default branch locally and remotely?","options":["git branch -m && git push --set-upstream","git rename && git sync","git set-default","git move-branch"],"answer":"git branch -m && git push --set-upstream"}
{"id":709,"question":"Which Prometheus data type stores current values without history?","options":["Gauge","Counter","Summary","Histogram"],"answer":"Gauge"}
{"id":710,"question":"Which Docker Compose file key sets environment variable values directly?","options":["environment","env_file","env","variables"],"answer":"environment"}
{"id":711,"question":"Which K8s configmap field allows loading as volume mount?","options":["volumeMounts","configMapKeyRef","configMapVolume","mountFrom"],"answer":"configMapVolume"}
{"id":712,"question":"Which Terraform state command locks backend to avoid concurrent runs?","options":["terraform force-unlock","terraform state lock","terraform state hold","terraform lock-backend"],"answer":"terraform force-unlock"}
{"id":713,"question":"Which container image format supports OCI spec compliance?","options":["Docker","OCI","Singularity","PodmanImage"],"answer":"OCI"}
{"id":714,"question":"Which Jenkins syntax checks for required plugin version during pipeline execution?","options":["@Library","pluginVersion","requiresPlugin","loadPlugin"],"answer":"requiresPlugin"}
{"id":715,"question":"Which CI/CD system uses pipelines-as-code and stores history as Tekton CRDs?","options":["Jenkins X","OpenShift Pipelines","Tekton","Argo Events"],"answer":"Tekton"}
{"id":716,"question":"Which GCP service integrates service mesh with Anthos for secure traffic flow?","options":["Traffic Director","Mesh Gateway","Secure Routing","Service Flow"],"answer":"Traffic Director"}
{"id":717,"question":"Which kubectl subcommand describes component configuration in kubelet?","options":["kubectl get componentstatus","kubectl describe node-config","kubectl get configz","kubectl describe kubelet"],"answer":"kubectl get configz"}
{"id":718,"question":"Which tool uses signatures to validate integrity of Helm charts?","options":["cosign","notary","chart-verifier","helm-sign"],"answer":"cosign"}
{"id":719,"question":"Which Vault method allows machine login via cloud-native identity metadata?","options":["GCP Auth","AppRole","Metadata Login","Instance Identity"],"answer":"GCP Auth"}
{"id":720,"question":"Which Jenkins option limits parallel builds across agents globally?","options":["Throttle Concurrent Builds","Limit Executors","Global Agent Cap","Pipeline Lock"],"answer":"Throttle Concurrent Builds"}
{"id":721,"question":"Which Git flag enables pushing all local branches at once?","options":["--all","--push-everything","--branches","--multi"],"answer":"--all"}
{"id":722,"question":"Which Kubernetes resource ensures minimal Pod availability during disruptions?","options":["PodDisruptionBudget","AvailabilityZone","UptimePolicy","ResilienceGroup"],"answer":"PodDisruptionBudget"}
{"id":723,"question":"Which container runtime uses systemd for cgroup management by default?","options":["CRI-O","runc","systemd-nspawn","containerd"],"answer":"systemd-nspawn"}
{"id":724,"question":"Which config file sets custom Kubelet args on a node in managed clusters?","options":["kubelet-config.yaml","node-agent.yaml","bootstrap-kubelet.conf","custom-args.json"],"answer":"kubelet-config.yaml"}
{"id":725,"question":"Which Azure service automates deployment of ARM templates in pipelines?","options":["Azure Resource Manager","Deployment Center","Template Task","ARM Deploy"],"answer":"ARM Deploy"}
{"id":726,"question":"Which Ansible feature enables loop over dictionaries in playbooks?","options":["with_dict","loop_var","foreach","map_keys"],"answer":"with_dict"}
{"id":727,"question":"Which DevOps concept ensures infra changes are tracked as commits?","options":["Infrastructure as Code","Versioned Infra","Change as YAML","Infra Commits"],"answer":"Infrastructure as Code"}
{"id":728,"question":"Which Git command switches branches and updates working directory?","options":["git switch","git checkout","git move","git jump"],"answer":"git switch"}
{"id":729,"question":"Which Tekton component defines reusable task steps?","options":["Task","Pipeline","StepTemplate","StepDef"],"answer":"Task"}
{"id":730,"question":"Which Linux utility shows disk usage in human-readable tree format?","options":["ncdu","du -h","tree -size","df -T"],"answer":"ncdu"}
{"id":731,"question":"Which shell command removes exported variable from current session?","options":["unset","unexport","del","export -d"],"answer":"unset"}
{"id":732,"question":"Which ArgoCD setting forces sync even on non-drifted apps?","options":["syncPolicy: automated","force: true","reapply: yes","syncOptions: ForceApply"],"answer":"syncOptions: ForceApply"}
{"id":733,"question":"Which tool deploys serverless functions on Kubernetes using CRDs?","options":["OpenFaaS","Knative","Kubeless","Fission"],"answer":"Knative"}
{"id":734,"question":"Which Prometheus function returns latest value of a metric?","options":["last_over_time","max_over_time","end_value","instant"],"answer":"last_over_time"}
{"id":735,"question":"Which Kubernetes scheduler component supports custom plugins in scheduling cycle?","options":["Framework","PluginSlot","SchedulingCycle","ExtenderV2"],"answer":"Framework"}
{"id":736,"question":"Which AWS CLI flag generates signed URL for S3 object access?","options":["presign","get-url","signed-link","generate-url"],"answer":"presign"}
{"id":737,"question":"Which GitLab config keyword defines retry attempts for failed jobs?","options":["retry","attempts","on_fail","try"],"answer":"retry"}
{"id":738,"question":"Which CI/CD practice involves ephemeral review environments per PR?","options":["Preview Environments","Dynamic Branch Testing","On-demand Sandbox","Ephemeral Review"],"answer":"Preview Environments"}
{"id":739,"question":"Which Linux systemd command enables a unit at boot time?","options":["systemctl enable","systemctl persist","unitctl start","enable-unit"],"answer":"systemctl enable"}
{"id":740,"question":"Which tool validates YAML and Kubernetes manifests against schemas?","options":["kubeval","yamllint","kubescore","kubecheck"],"answer":"kubeval"}
{"id":741,"question":"Which Git merge strategy preserves all commits during branch integration?","options":["--no-ff","--squash","--rebase","--flatten"],"answer":"--no-ff"}
{"id":742,"question":"Which Terraform feature allows usage of third-party providers?","options":["required_providers","provider_registry","source_providers","terraform_plugin"],"answer":"required_providers"}
{"id":743,"question":"Which container orchestrator integrates with Nomad for service discovery?","options":["Consul","Vault","Serf","DNSMasq"],"answer":"Consul"}
{"id":744,"question":"Which Git config disables detached HEAD warning?","options":["advice.detachedHead=false","core.noWarning=true","safe.detached=false","ui.headsafe=off"],"answer":"advice.detachedHead=false"}
{"id":745,"question":"Which Helm test hook validates deployment readiness post-install?","options":["test-success","post-install-test","hook-test-ready","tests"],"answer":"test-success"}
{"id":746,"question":"Which CI/CD mechanism in GitHub restricts workflow access to approved orgs?","options":["workflow permissions","access matrix","runner policy","trusted list"],"answer":"workflow permissions"}
{"id":747,"question":"Which Kubernetes object manages external IPs via DNS and load balancing?","options":["Ingress","LoadBalancer","ServiceEntry","Gateway"],"answer":"Ingress"}
{"id":748,"question":"Which Azure DevOps file defines multi-stage pipelines as YAML?","options":["azure-pipelines.yml","pipeline-definition.yaml","build-deploy.yml","ado.yml"],"answer":"azure-pipelines.yml"}
{"id":749,"question":"Which Docker command removes all stopped containers at once?","options":["docker container prune","docker clean","docker rm -a","docker gc"],"answer":"docker container prune"}
{"id":750,"question":"Which Git commit object stores tree snapshot and parent hash?","options":["commit object","blob object","tree object","tag object"],"answer":"commit object"}
{"id":751,"question":"Which Kubernetes default service type exposes cluster-internal access only?","options":["ClusterIP","NodePort","LoadBalancer","ExternalName"],"answer":"ClusterIP"}
{"id":752,"question":"Which Docker runtime parameter mounts host directory read-only into container?","options":["--mount type=bind,ro","-v host:container:ro","--volume host:container:ro","--read-only-host"],"answer":"--mount type=bind,ro"}
{"id":753,"question":"Which shell built-in command replaces current process without spawning a child?","options":["exec","source","eval","spawn"],"answer":"exec"}
{"id":754,"question":"Which Terraform interpolation reference fetches all objects from map variable?","options":["values(map)","keys(map)","lookup(map)","each.value"],"answer":"values(map)"}
{"id":755,"question":"Which GitHub Actions environment variable contains event name triggering workflow?","options":["GITHUB_EVENT_NAME","GITHUB_TRIGGER","ACTION_EVENT","EVENT_TYPE"],"answer":"GITHUB_EVENT_NAME"}
{"id":756,"question":"Which Kubernetes PodPriority class ensures critical workload scheduling before others?","options":["system-cluster-critical","high-priority","critical-svc","batch-elevated"],"answer":"system-cluster-critical"}
{"id":757,"question":"Which Linux sysctl parameter enables IP forwarding between interfaces?","options":["net.ipv4.ip_forward","net.ipv4.forwarding","net.ip6.forwarding","net.bridge.ip_forward"],"answer":"net.ipv4.ip_forward"}
{"id":758,"question":"Which Argo Workflow field defines timeout for entire execution?","options":["activeDeadlineSeconds","timeoutSeconds","runDeadline","executionTimeout"],"answer":"activeDeadlineSeconds"}
{"id":759,"question":"Which Jenkins pipeline block ensures steps always execute regardless of failure?","options":["post","always","cleanup","finally"],"answer":"post"}
{"id":760,"question":"Which environment variable in Kubernetes sets custom DNS search domains?","options":["dnsSearch","DNS_SEARCH","clusterDNSSearches","dnsPolicy"],"answer":"dnsPolicy"}
{"id":761,"question":"Which GCP CI/CD service natively integrates with Cloud Build triggers?","options":["Cloud Deploy","Cloud Build","Cloud Composer","Cloud Functions"],"answer":"Cloud Deploy"}
{"id":762,"question":"Which Terraform construct defines complex object type for module outputs?","options":["object","map","tuple","complex"],"answer":"object"}
{"id":763,"question":"Which Kubernetes scheduler plugin filters nodes by resource labels?","options":["NodeAffinity","LabelFilter","PodPredicate","ResourcePlugin"],"answer":"NodeAffinity"}
{"id":764,"question":"Which Vault backend encrypts data in transit over TLS automatically?","options":["PKI","Transit","Storage","Cubbyhole"],"answer":"Transit"}
{"id":765,"question":"Which Docker storage driver supports copy-on-write layered filesystems?","options":["overlay2","devicemapper","btrfs","aufs"],"answer":"overlay2"}
{"id":766,"question":"Which Git config enables commit signing validation on push?","options":["commit.gpgSign","push.verify","validate.sign","tag.gpgSign"],"answer":"commit.gpgSign"}
{"id":767,"question":"Which CI pipeline language supports YAML anchors for reuse across jobs?","options":["GitHub Actions","GitLab CI","Azure Pipelines","CircleCI"],"answer":"GitLab CI"}
{"id":768,"question":"Which Prometheus rule grouping option avoids duplicated alerts across replicas?","options":["group_wait","group_interval","group_by","group_labels"],"answer":"group_by"}
{"id":769,"question":"Which Kubernetes field sets CPU limit enforcement at kubelet level?","options":["cpu.cfs_quota","cpuLimit","cpu_max","cpuRequest"],"answer":"cpu.cfs_quota"}
{"id":770,"question":"Which cloud-init directive adds users at instance boot time declaratively?","options":["users","user_add","add_user","initial_users"],"answer":"users"}
{"id":771,"question":"Which OpenShift operator automates cluster logging deployment?","options":["ClusterLogging","LoggingOperator","FluentdOperator","LoggingCluster"],"answer":"ClusterLogging"}
{"id":772,"question":"Which Jenkins syntax loads external shared library at runtime?","options":["@Library","load","libraryPath","includeLib"],"answer":"@Library"}
{"id":773,"question":"Which Kubernetes resource restricts outgoing traffic per namespace?","options":["NetworkPolicy","EgressRule","PolicyEndpoint","TrafficLimit"],"answer":"NetworkPolicy"}
{"id":774,"question":"Which method allows SSH jump host chaining automatically?","options":["ProxyJump","SSHControlMaster","ProxyCommand","JumpHostConfig"],"answer":"ProxyJump"}
{"id":775,"question":"Which Ansible directive fails fast on hostgroup errors?","options":["any_errors_fatal","fail_fast","stop_on_error","exit_on_fail"],"answer":"any_errors_fatal"}
{"id":776,"question":"Which tool visualizes helm chart value schema validation via IDE integration?","options":["Helm VSCode Extension","chart-schema-validator","helm-docs","cvsch"],"answer":"Helm VSCode Extension"}
{"id":777,"question":"Which Kubernetes PodSpec field controls node scheduling based on disk availability?","options":["volumeBindingMode","nodeSelector","tolerations","affinity"],"answer":"affinity"}
{"id":778,"question":"Which Bash option prevents globbing expansion in scripts?","options":["set -f","set -u","set -o noglob","set -k"],"answer":"set -f"}
{"id":779,"question":"Which Vault policy type grants access to read dynamic secrets at path?","options":["read-only","cap_read","policy-reader","key_reader"],"answer":"cap_read"}
{"id":780,"question":"Which cloudformation feature rolls back stack on failure by default?","options":["RollbackConfiguration","AutoRollback","OnFailure","FailurePolicy"],"answer":"RollbackConfiguration"}
{"id":781,"question":"Which Kubernetes readiness check verifies HTTP endpoint status codes?","options":["httpGet","tcpSocket","exec","grpcProbe"],"answer":"httpGet"}
{"id":782,"question":"Which Git command rebases interactive onto remote tracking branch?","options":["git rebase origin/main","git rebase -i","git rebase --onto","git rebase upstream"],"answer":"git rebase origin/main"}
{"id":783,"question":"Which CI/CD metric measures deployment frequency across environments?","options":["DeploymentRate","Lead Time","MTTR","ChangeFailureRate"],"answer":"DeploymentRate"}
{"id":784,"question":"Which Terraform command shows explicit diff before apply?","options":["terraform plan","terraform show","terraform diff","terraform preview"],"answer":"terraform plan"}
{"id":785,"question":"Which Prometheus exporter collects host-level disk metrics via Node exporter?","options":["node_exporter","disk_exporter","host_exporter","fs_exporter"],"answer":"node_exporter"}
{"id":786,"question":"Which Kubernetes command patches resource inline using strategic merge?","options":["kubectl patch -p","kubectl apply --patch","kubectl edit","kubectl replace"],"answer":"kubectl patch -p"}
{"id":787,"question":"Which Docker CLI flag assigns custom name to container on creation?","options":["--name","-n","--alias","--nickname"],"answer":"--name"}
{"id":788,"question":"Which GitLab file allows multi-project pipeline includes via URLs?","options":["include","template","subpipeline","external_include"],"answer":"include"}
{"id":789,"question":"Which Vault secret engine supports key-value versioning?","options":["kv-v2","kv","versioned-kv","vault-kv"],"answer":"kv-v2"}
{"id":790,"question":"Which Kubernetes field defines number of pod restart retries before failure?","options":["backoffLimit","restartLimit","retryPolicy","failureThreshold"],"answer":"backoffLimit"}
{"id":791,"question":"Which cloud-native build tool runs Kaniko images in cluster without privileged mode?","options":["kaniko","buildkit","img","pack"],"answer":"kaniko"}
{"id":792,"question":"Which Git command stashes staged and unstaged changes separately?","options":["git stash push --keep-index","git stash --stash-index","git stash save staged","git stash partial"],"answer":"git stash push --keep-index"}
{"id":793,"question":"Which Azure CLI command adds a tag to a VM resource?","options":["az resource tag","az vm update --set tags","az tag create","az tag add"],"answer":"az resource tag"}
{"id":794,"question":"Which Kubernetes scheduler algorithm prioritizes nodes with most free memory?","options":["MostRequestedPriority","LeastRequestedPriority","BalancedPriority","MemoryFirstPriority"],"answer":"LeastRequestedPriority"}
{"id":795,"question":"Which Helm lifecycle hook runs before chart deletion occurs?","options":["pre-delete","post-delete","pre-remove","before-uninstall"],"answer":"pre-delete"}
{"id":796,"question":"Which Docker healthcheck option defines consecutive failure threshold?","options":["--health-retries","--health-interval","--health-start-period","--health-timeout"],"answer":"--health-retries"}
{"id":797,"question":"Which Git credential helper stores passwords in macOS Keychain?","options":["osxkeychain","cache","store","wincred"],"answer":"osxkeychain"}
{"id":798,"question":"Which Prometheus metric type estimates quantiles over sliding windows?","options":["Summary","Histogram","Gauge","ExponentiallyWeighted"],"answer":"Summary"}
{"id":799,"question":"Which Kubectl plugin applies resource definitions with live pruning?","options":["kubectl apply","kubectl-kapply","kubectl prune","kubectl liveapply"],"answer":"kubectl-kapply"}
{"id":800,"question":"Which CI server provides Blue/Green deployment support out-of-the-box?","options":["GoCD","Spinnaker","Jenkins","Bamboo"],"answer":"Spinnaker"}




]


# Optional function to get questions (for modular import)
def get_questions():
    return questions
