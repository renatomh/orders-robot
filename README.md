# Orders Robot - RobotSpareBin Industries

This robot automates the process of ordering robots from RobotSpareBin Industries Inc. It processes orders from a CSV file, fills out order forms on the website, generates receipts, and creates a comprehensive archive of all transactions.

[Automation Certification Level II: Build a robot](https://sema4.ai/docs/automation/courses/build-a-robot-python)

## What This Robot Does

 **Automated Order Processing**: Downloads order data from a CSV file and processes each order automatically

 **Form Automation**: Fills out robot order forms with:
- Head selection
- Body type selection  
- Leg part numbers
- Delivery addresses

 **Receipt Generation**: Creates PDF receipts for each order with embedded robot screenshots

 **Archive Creation**: Compiles all receipts into a ZIP archive for easy storage and retrieval

## Robot Workflow

1. **Download Orders**: Fetches the latest orders from https://robotsparebinindustries.com/orders.csv
2. **Open Website**: Navigates to the robot order website
3. **Process Each Order**:
   - Closes any modal dialogs
   - Fills out the order form with customer data
   - Previews and submits the order
   - Retries if order fails
   - Generates PDF receipt
   - Takes screenshot of the ordered robot
   - Embeds screenshot into the receipt
4. **Create Archive**: Compiles all receipts into a ZIP file

# Template: Python - Minimal

This template leverages the new [Python framework](https://github.com/robocorp/robocorp), the [libraries](https://github.com/robocorp/robocorp/blob/master/docs/README.md#python-libraries) from to same project as well.

The template provides you with the basic structure of a Python project: logging out of the box and controlling your tasks without fiddling with the base Python stuff. The environment contains the most used libraries, so you do not have to start thinking about those right away. 

👉 Other templates are available as well via our tooling and on our [Portal](https://robocorp.com/portal/tag/template)

## Running

#### VS Code
1. Get [Robocorp Code](https://robocorp.com/docs/developer-tools/visual-studio-code/extension-features) -extension for VS Code.
1. You'll get an easy-to-use side panel and powerful command-palette commands for running, debugging, code completion, docs, etc.

#### Command line

1. [Get RCC](https://github.com/robocorp/rcc?tab=readme-ov-file#getting-started)
1. Use the command: `rcc run`

## Results

🚀 After running the bot, check out the `log.html` under the `output` -folder.

## Pushing to Robocorp Cloud

### Prerequisites
1. **RCC installed** and configured
2. **Robocorp account** with access to Control Room
3. **Workspace** created in Robocorp Control Room

### Step 1: Configure RCC Credentials
```bash
rcc configure credentials YOUR_CREDENTIALS_HERE
```

Get your credentials from Control Room  User Settings  Access Credentials

### Step 2: Find Your Workspace ID
```bash
rcc cloud workspace
```

### Step 3: Create Robot in Workspace (if needed)
```bash
rcc cloud new -r orders-robot -w YOUR_WORKSPACE_ID
```

This will return the robot identity, which is used in the next step.

### Step 4: Upload Your Robot
```bash
rcc cloud push -r YOUR_ROBOT_ID -w YOUR_WORKSPACE_ID
```

## Dependencies

We strongly recommend getting familiar with adding your dependencies in [conda.yaml](conda.yaml) to control your Python dependencies and the whole Python environment for your automation.

<details>
  <summary>🙋‍♂️ "Why not just pip install...?"</summary>

Think of [conda.yaml](conda.yaml) as an equivalent of the requirements.txt, but much better. 👩‍💻 With `conda.yaml`, you are not just controlling your PyPI dependencies; you control the complete Python environment, which makes things repeatable and easy.

👉 You will probably need to run your code on another machine quite soon, so by using `conda.yaml`:
- You can avoid `Works on my machine` -cases
- You do not need to manage Python installations on all the machines
- You can control exactly which version of Python your automation will run on 
  - You'll also control the pip version to avoid dep. resolution changes
- No need for venv, pyenv, ... tooling and knowledge sharing inside your team.
- Define dependencies in conda.yaml, let our tooling do the heavy lifting.
- You get all the content of [conda-forge](https://prefix.dev/channels/conda-forge) without any extra tooling

> Dive deeper with [these](https://github.com/robocorp/rcc/blob/master/docs/recipes.md#what-is-in-condayaml) resources.

</details>
<br/>

> The full power of [rpaframework](https://robocorp.com/docs/python/rpa-framework) -libraries is also available on Python as a backup while we implement the new Python libraries.

## What now?

🚀 Now, go get'em

Start writing Python and remember that the AI/LLM's out there are getting really good and creating Python code specifically.

👉 Try out [Robocorp ReMark 💬](https://chat.robocorp.com)

For more information, do not forget to check out the following:
- [Robocorp Documentation -site](https://robocorp.com/docs)
- [Portal for more examples](https://robocorp.com/portal)
- Follow our main [robocorp -repository](https://github.com/robocorp/robocorp) as it is the main location where we developed the libraries and the framework.