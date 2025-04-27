# Conversational AI Chatbot using Flask and Transformers 

## Overview  
This project features a conversational AI chatbot powered by the **Facebook BlenderBot 400M Distill** model from Hugging Face Transformers, which is designed for engaging, natural, and context-aware human-like conversations. The backend is implemented using **Flask**, a lightweight Python web framework, exposing a RESTful API that handles chat requests. This API can be easily integrated with any frontend or external system.

The chatbot leverages advanced NLP techniques to understand user inputs in context by maintaining conversation history, which improves the quality and relevance of responses. The project serves as a practical example of deploying state-of-the-art transformer models in production-ready web services.

---

## Features  
- **Real-time Conversational AI:** Uses BlenderBot 400M Distill, a well-optimized transformer model fine-tuned for dialogue, providing human-like conversational responses.  
- **Contextual Awareness:** Maintains an ongoing conversation history between the user and the bot to generate contextually relevant replies rather than isolated answers.  
- **RESTful API:** Built with Flask, the API accepts chat prompts via HTTP POST requests, making it straightforward to connect with web or mobile frontends.  
- **Concurrent Request Handling:** CORS (Cross-Origin Resource Sharing) support is enabled via the `flask-cors` extension, allowing safe and secure interaction from multiple client origins simultaneously.  
- **Lightweight and Scalable:** Designed to be minimalistic yet functional, allowing further extension or deployment on cloud platforms.

---

## Technologies Used  
- **Python:** Main programming language, chosen for its simplicity and vast ecosystem in AI and web development.  
- **Flask:** Framework used to create the backend API, known for its ease of use and flexibility in building RESTful services.  
- **Transformers (Hugging Face):** Provides pretrained state-of-the-art conversational models like BlenderBot, enabling natural language understanding and generation.  
- **PyTorch:** Deep learning framework used as the backend for running the transformer model efficiently on CPU or GPU.  
- **flask-cors:** Flask extension to handle Cross-Origin Resource Sharing, enabling the API to serve requests from web applications running on different domains or ports.

---

## Acknowledgements  
This project was developed as part of a guided project provided by the IBM Skills Network, which helped me understand conversational AI and deploying transformer models using Flask.
