# 🔍 Reflect - Personal Journal & Sentiment Analysis App

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)

A powerful journaling application with built-in sentiment analysis to help you track and understand your emotional patterns over time.

## ✨ Features

- **AI-Powered Insights**: Automatic sentiment analysis of journal entries
- **Beautiful Visualization**: Track your mood trends with interactive charts
- **Secure & Private**: Password-protected with encrypted storage
- **Searchable History**: Find past entries with powerful search
- **Responsive Design**: Works perfectly on desktop and mobile

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/dheeraj7000/reflect.git
cd reflect
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

4. Run the app:
```bash
streamlit run app.py
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Sentiment Analysis**: HuggingFace Transformers
- **Database**: MongoDB
- **Visualization**: Plotly, Matplotlib
- **Authentication**: Passlib

## 📸 Screenshots

| Login Screen | Journal Interface | Sentiment Analysis |
|--------------|-------------------|--------------------|
| ![Login](https://i.imgur.com/login_screenshot.png) | ![Journal](https://i.imgur.com/journal_screenshot.png) | ![Analysis](https://i.imgur.com/analysis_screenshot.png) |

## 📂 Project Structure

```
reflect/
├── app.py                # Main application logic
├── auth.py               # Authentication handlers
├── analysis.py           # Sentiment analysis module
├── database.py           # MongoDB operations
├── visualization.py      # Chart generation
├── requirements.txt      # Python dependencies
├── .env.example          # Environment template
└── README.md             # This file
```

## 🌐 Deployment

### Option 1: Streamlit Sharing
1. Fork this repository
2. Create account on [Streamlit Sharing](https://share.streamlit.io/)
3. Connect your GitHub and deploy

### Option 2: Docker
```bash
docker build -t reflect .
docker run -p 8501:8501 reflect
```

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

MIT License - see [LICENSE](LICENSE) for details

## ✉️ Contact

Dheeraj Kumar - 13kumardheeraj@gmail.com

Project Link: [https://github.com/dheeraj7000/reflect](https://github.com/dheeraj7000/reflect)
