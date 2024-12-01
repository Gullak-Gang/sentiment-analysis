# Sentiment Analysis Script

This repository contains a Python script designed to perform sentiment analysis on text data. It serves as the foundation for a custom Kestra plugin, offering flexibility for users to perform sentiment analysis either as a standalone Python script or through the Kestra workflow platform.

## Features

- Analyzes text for sentiment (positive, negative, or neutral).
- Processes individual text inputs or batch datasets.
- Easy-to-use interface for integration into custom pipelines.

## Usage

### 1. **As a Standalone Python Script**
To use this script directly in Python, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/Gullak-Gang/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```


3. Run the script:
    ```bash
        python main.py 
    ```
The script will analyze the input and output the sentiment results.

### 2. **As Part of a Kestra Workflow**
This script was used as a base for creating a custom Kestra plugin, which is available [here](https://github.com/Gullak-Gang/plugin-hackfrost).

With the plugin, you can integrate sentiment analysis seamlessly into your Kestra workflows. The plugin provides:
    * Built-in scheduling and automation.
    * Support for processing large datasets.
    * Easy integration with Kestra-managed data pipelines.

To use the plugin:
1. Refer to the plugin documentation here.
2. Add the plugin to your Kestra configuration.
3. Use it as part of your workflow YAML files.

 ## **Why Use the Kestra Plugin?**
* Automation: The Kestra plugin automates the sentiment analysis process, making it easy to run recurring or large-scale jobs.
* Scalability: The plugin is optimized for handling large datasets as part of Kestra workflows.
* Flexibility: You can still use the original Python script for smaller, ad-hoc analyses when needed.

---
## License
This repository is licensed under the MIT License. See the LICENSE file for details.

For any issues or questions, please create an issue in this repository or contact us through the Kestra plugin repository here.
