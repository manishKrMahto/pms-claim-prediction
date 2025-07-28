# 🚑 PMS Claim Prediction API

A FastAPI project for managing patient claim records with full **CRUD operations** and **claim prediction** functionality. This project was built as part of the [CampusX FastAPI Deployment Course](https://www.youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ) by **Nitish Sir**.


---

## 🔧 Features

- ✅ FastAPI-based backend  
- ✅ Pydantic models with validation  
- ✅ Create, Read, Update, Delete (CRUD) operations  
- ✅ Predict claim status using a trained ML model  
- ✅ Dockerized for easy deployment  
- ✅ Ready to be deployed on AWS / any cloud  

---

## 📁 Project Structure

```

pms-claim-prediction/
│
├── .gitignore              # Git ignore rules
├── .env_pms                # Environment variables
├── Dockerfile              # Docker build instructions
├── frontend.py             # Optional frontend/streamlit script
├── main.py                 # FastAPI app entry point
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
│
├── config/                 # Configuration scripts
│ ├── city_tiers.py
│ └── pycache/              # Cached bytecode
│
├── models/                 # Model files and logic
│ ├── model.pkl             # Trained ML model
│ ├── patients.json         # Sample patient data
│ ├── predict.py            # Prediction logic
│ └── pycache/              # Cached bytecode
│
└── schema/                 # Pydantic data schemas
    ├── patient.py
    ├── update_patient.py
    └── user_input.py

````

## 🚀 Run Locally

### 1️⃣ Clone the repo

````bash
git clone https://github.com/manishKrMahto/pms-claim-prediction.git
cd pms-claim-prediction
````

### 2️⃣ Create a virtual environment (optional but recommended)

````bash
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
````

### 3️⃣ Install dependencies

````bash
pip install -r requirements.txt
````

### 4️⃣ Run the app

````bash
uvicorn main:app --reload
````

Now open your browser at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🐳 Run with Docker

### Build the Docker image

````bash
docker build -t pms-claim-prediction .
````

### Run the container

````bash
docker run -d -p 8000:8000 pms-claim-prediction
````

### Or pull the image from Docker Hub

````bash
docker pull manishkrmahto/pms-claim-prediction:latest
docker run -d -p 8000:8000 manishkrmahto/pms-claim-prediction:latest
````

---

## 📌 API Endpoints

| Method | Endpoint              | Description              |
|--------|------------------------|--------------------------|
| GET    | `/`                   | Root message             |
| GET    | `/about`             | About the API            |
| GET    | `/health`            | Health check             |
| POST   | `/create`            | Create a new patient     |
| GET    | `/view`              | View all patients        |
| GET    | `/patient/{patient_id}` | Get patient by ID     |
| PUT    | `/edit/{patient_id}`    | Update patient info   |
| DELETE | `/delete/{patient_id}`  | Delete patient record |
| GET    | `/sort`              | Sort patients            |
| POST   | `/predict`           | Predict premium claim    |


---

## 🙏 Special Thanks

Huge thanks to **Nitish Sir** and **CampusX** for creating the FastAPI Deployment Playlist which guided the development of this project.
🎓 [Watch the full course](https://www.youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ)

---

## 📌 Author

**Manish Kumar Mahto**
📧 [manishcode123@gmail.com](mailto:manishcode123@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/manish-kumar-mahto/)
🐙 [GitHub](https://github.com/manishKrMahto)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
