# text2three - Text-to-3D Model Integration Platform

**text2three** is a Python library and CLI tool that integrates multiple text-to-3D generative model APIs into a unified platform.  
It allows you to generate 3D models from text prompts using various backend APIs like Meshy and Shape-E, and download and preview the results locally.

---
<<<<<<< HEAD

## Features

- Unified interface to multiple text-to-3D APIs
- Supports Meshy API
- Supports Shape-E API via Huggingface Gradio client
- Supports ModelsLab API
- CLI tool to generate models and launch local preview server
- (**COMING SOON**) more models and ONE API with consolidated pricing

  
## Requirements

- Python 3.8+
- `requests`
- `python-dotenv`
- `gradio-client`
- text2three API (**COMING SOON**)



---

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/yourusername/text2three.git
    cd text2three
    ```

2. Create and activate a virtual environment (OPTIONAL but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your API keys in a `.env` file at the project root:

    > *For now, please add the API key for the respective API providers. Single API key access will be available soon.*

---
## Usage

Generate 3D Model from CLI using Meshy Model

    python -m text2three.tests.test_meshy -p "a dragon" -m meshy

CLI Options:

    -p / --prompt : (Required) Text prompt describing the 3D model.
    -m / --model : Model backend to use (meshy, shapee, or modelslab).

The generated .glb model will be saved in the output/ directory.
---
## Usage

Previewing the Model
After generation, a local HTTP server will start, and a browser window will open automatically showing the preview:

    http://localhost:8000/viewer.html?model=a_dragon.glb
    
Press Ctrl+C in the terminal to stop the server.




Author 
— Jonathan@neurarock.com
Project Link: 
https://www.neurarock.com

=======

## Features

- Unified interface to multiple text-to-3D APIs
- Supports Meshy API
- Supports Shape-E API via Huggingface Gradio client
- Supports ModelsLab API
- CLI tool to generate models and launch local preview server
- (**COMING SOON**) more models and ONE API with consolidated pricing

  
## Requirements

- Python 3.8+
- `requests`
- `python-dotenv`
- `gradio-client`
- text2three API (**COMING SOON**)



---

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/yourusername/text2three.git
    cd text2three
    ```

2. Create and activate a virtual environment (OPTIONAL but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your API keys in a `.env` file at the project root:

    > *For now, please add the API key for the respective API providers. Single API key access will be available soon.*

---
## Usage

Generate 3D Model from CLI using Meshy Model

    python -m text2three.tests.test_meshy -p "a dragon" -m meshy

CLI Options:

    -p / --prompt : (Required) Text prompt describing the 3D model.
    -m / --model : Model backend to use (meshy, shapee, or modelslab).

The generated .glb model will be saved in the output/ directory.
---
## Usage

Previewing the Model
After generation, a local HTTP server will start, and a browser window will open automatically showing the preview:

    http://localhost:8000/viewer.html?model=a_dragon.glb
    
Press Ctrl+C in the terminal to stop the server.




Author 
— Jonathan@neurarock.com
Project Link: 
https://www.neurarock.com
>>>>>>> 6e5e980 (Added ModelsLab Model)
