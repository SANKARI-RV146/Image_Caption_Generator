# VisionaryLens - AI-Powered Image Caption Generator

## Overview
VisionaryLens is an AI-powered image caption generator that uses state-of-the-art deep learning models to interpret and describe the content of images. Built with Streamlit for interactive user experience and powered by BLIP (Bootstrapping Language-Image Pre-training).

---

## Project Structure

---

## 🚀 **Features**
- 📸 **Image Upload:** Upload any image (JPG, PNG, JPEG) to the application.  
- 📝 **AI-Generated Caption:** Automatically generates a descriptive caption based on the image content.  
- ⚡ **Real-Time Processing:** Get instant results after image upload.  
- 🎨 **User-Friendly Interface:** Built with **Streamlit** for smooth user interaction.  

---

## 🛠️ **Tech Stack**
- **Language:** Python  
- **Framework:** Streamlit  
- **Model:** BLIP (Bootstrapping Language-Image Pre-training)  
- **Libraries:**  
  - `transformers` → For loading pre-trained BLIP model  
  - `torch` → For tensor manipulations and model inference  
  - `Pillow` → For image processing  
  - `Streamlit` → For interactive web UI  

---

## 💻 **Setup Instructions**
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Image_Caption_Generator.git
    cd Image_Caption_Generator
    ```

2. **Create a virtual environment (Optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use: .\venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.Run the application:
    streamlit run app.py
5.Access the application:  
    Open your browser and navigate to `http://localhost:8501`
## Usage
- Upload an image using the **"Choose an image..."** button.  
- Click **"Generate Caption"** to see the AI-generated description.  
- The caption is displayed instantly beneath the image.  
## Sample Output
**Input Image:**  
*(An image of a golden retriever playing in a park)*  
**Generated Caption:**  
*"A happy golden retriever playing in the grass at a sunny park."*  
## Future Enhancements
- Integrate multilingual caption generation for global accessibility.  
- Deploy the application on **Streamlit Cloud** and **HuggingFace Spaces**.  
- Improve caption accuracy with **fine-tuning** on custom datasets.  
- Add support for **Object Detection** along with captioning.  
## Deployment Strategy
1.Streamlit Cloud:For fast and simple deployment, accessible with a public URL.  
## Contributors
 Sankari R V - Developer  
## Acknowledgements
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [PyTorch](https://pytorch.org/)  

