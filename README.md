# N8n Example

This repository contains a small example script demonstrating how to call a few different large language model APIs.

## Usage
1. Install the required packages (if you have internet access):
   ```bash
   pip install python-dotenv langchain-openai langchain-anthropic langchain-google-genai
   ```
   If you cannot install packages due to network restrictions, you can still run the script after installing them manually.

2. Save the `compare_models.py` file exactly as it appears in this repository. Ensure your copy **does not** contain any git diff lines such as `index 0000...` or `--- /dev/null`.

3. Set any necessary API keys in a `.env` file.

4. Run the script with Python:
   ```bash
   python compare_models.py
   ```

