# Write-Up: Deploy An Article CMS to Azure

## Analyze, Choose, and Justify the Appropriate 
## Cloud Deployment Option for This Project

---

## Virtual Machine (VM) vs Azure App Service

### Cost

**Virtual Machine (VM):**
VMs use a Pay-as-you-go pricing model where you
pay for compute resources (CPU, RAM, storage)
continuously, even when the app is idle. For a
small CMS application, this is expensive since
the VM runs 24/7 regardless of traffic. Additional
costs include OS licensing, storage, and network
usage, making VMs significantly more expensive
than App Service for small applications.

**Azure App Service:**
App Service offers tiered pricing plans including
Free (F1), Basic (B1 ~$13/month), Standard, and
Premium tiers. The Free tier is available for
development and testing at no cost. For production,
the Basic plan is significantly cheaper than
running a VM for a small web application like
this CMS.

---

### Scalability

**Virtual Machine (VM):**
VMs require manual scaling configuration. To
handle traffic spikes, you need to manually add
more VMs or configure VM Scale Sets. This process
requires significant technical expertise and
additional setup time. Vertical scaling (adding
more CPU/RAM) requires VM downtime, which affects
availability.

**Azure App Service:**
App Service provides built-in auto-scaling
capabilities. You can configure automatic scaling
rules based on CPU usage, memory, or HTTP queue
length. Scaling out by adding more instances
happens automatically without any downtime. This
makes App Service much more suitable for
applications with variable or unpredictable
traffic patterns.

---

### Availability

**Virtual Machine (VM):**
VMs offer 99.9% SLA for single instances and
99.99% SLA for multiple instances in availability
sets. However, maintaining high availability
requires manually configuring load balancers,
availability sets, and health probes. OS updates
and security patches can also cause unexpected
downtime if not carefully managed.

**Azure App Service:**
App Service provides a 99.95% SLA out of the box
without any additional configuration. Microsoft
manages the underlying infrastructure, OS updates,
and security patches automatically. Built-in health
monitoring and automatic instance replacement
ensure high availability without any manual
intervention from the developer.

---

### Workflow

**Virtual Machine (VM):**
Deploying to a VM requires significant manual work:
setting up the VM, installing Python and
dependencies, configuring Nginx or Apache as a
web server, deploying code via SSH or FTP, and
managing security updates manually. This process
is complex, time-consuming, and requires strong
DevOps expertise. Every update requires manual
intervention.

**Azure App Service:**
App Service offers a streamlined deployment
workflow. By connecting a GitHub repository to
App Service, every push to the master branch
triggers an automatic deployment via GitHub
Actions CI/CD pipeline. No server configuration
is needed, environment variables are managed
through the Azure Portal, and built-in monitoring
tools make debugging straightforward.

---

## My Choice: Azure App Service

I chose Azure App Service over a Virtual Machine
for deploying this Article CMS application because
it eliminates the need to manage server
infrastructure, allowing me to focus entirely on
application development. App Service's built-in
CI/CD integration with GitHub, automatic scaling,
and lower cost make it the most practical and
efficient choice for this Flask web application.
Additionally, since this CMS does not require
custom system software or special OS configurations,
App Service provides all the necessary capabilities
without the overhead of managing a VM.

---

## How the App Would Change if I Chose a VM

If I were to switch to a Virtual Machine, several
aspects of the application and its deployment
would need to change. I would need to install and
configure a web server such as Nginx or Apache,
set up a Python virtual environment manually, and
configure firewall rules and network security
groups for the VM. Additionally, I would need to
implement a CI/CD pipeline manually using tools
like Jenkins or GitHub Actions with SSH deployment,
and set up monitoring and logging separately using
Azure Monitor or third-party tools. The increased
control over infrastructure that a VM provides
would only be justified if the application required
custom system software, specific OS configurations,
or needed to run background processes that exceed
App Service limitations.