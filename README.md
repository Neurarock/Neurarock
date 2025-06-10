# text2three - Text-to-3D Model Integration Platform

**text2three** is a Python library and CLI tool that integrates multiple text-to-3D generative model APIs into a unified platform.  
It allows you to generate 3D models from text prompts using various backend APIs like Meshy and Shape-E, and download and preview the results locally.

---

## Features

- Unified interface to multiple text-to-3D APIs
- Supports Meshy API
- Supports Shape-E API via Huggingface Gradio client
- Supports ModelsLab API
- CLI tool to generate models and launch local preview server
- **COMING SOON** more models and ONE API with consolidated pricing

  
## Requirements

- Python 3.8+
- `requests`
- `python-dotenv`
- `gradio-client`
- **COMING SOON** text2three API


## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/text2three.git
cd text2three

2. Create and activate a virtual environment (OPTIONAL but recommended):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Add your API keys in a .env file at project root:

*for now please add the api key for the respective API providers, single API key access will be available soon

## Usage

Generate 3D Model from CLI

python -m text2three.tests.test_meshy -p "a dragon" -m meshy

or for Shape-E:

python -m text2three.tests.test_meshy -p "a dragon" -m shapee

CLI Options:

-p / --prompt : (Required) Text prompt describing the 3D model.
-m / --model : Model backend to use (meshy, shapee, or modelslab).

The generated .glb model will be saved in the output/ directory.

Previewing the Model
After generation, a local HTTP server will start, and a browser window will open automatically showing the preview:

http://localhost:8000/viewer.html?model=a_dragon.glb
Press Ctrl+C in the terminal to stop the server.

Author — Jonathan@neurarock.com
Project Link: https://www.neurarock.com

