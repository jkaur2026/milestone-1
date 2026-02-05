# milestone-1

##Model
- Model Type: scikit-learn classification model  
- Artifact: `model.pkl`  
- Input: Numerical feature vector (4 values)  
Output:
{"prediction": 2,
  "probabilities": [...]}

##Project Files used
milestone-1/
main.py
train_model.py
model.pkl
requirements.txt
Dockerfile
README.md
cloud_function
main.py
requirements.txt


Step 1 of assignment(FastAPI Service) 
created virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train_model.py
uvicorn main:app --reload
Tested with:
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"features":[1,2,3,4]}'

Step 2 of assignment:Cloud Run
Cloud Run URL:https://predict-fn2-546876087348.us-central1.run.app/predict
(Build and Run Docker Locally)
docker build -t milestone1 .
docker run --rm -p 8080:8080 -e PORT=8080 milestone1
gcloud run deploy predict-fn2 \
  --image us-central1-docker.pkg.dev/milestone1-project/mlops-repo/milestone1:latest \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080
Testing it:
curl -X POST "https://predict-fn2-546876087348.us-central1.run.app/predict" \
  -H "Content-Type: application/json" \
  -d '{"features":[1,2,3,4]}'

Step 3 of assignment:
Cloud Function URL:https://us-central1-milestone1-project.cloudfunctions.net/predict-fn2
Deploying and testing the function
cd cloud_function
gcloud functions deploy predict-fn2 \
  --gen2 \
  --runtime python311 \
  --region us-central1 \
  --source . \
  --entry-point predict \
  --trigger-http \
  --allow-unauthenticated
Testing:
curl -X POST "https://us-central1-milestone1-project.cloudfunctions.net/predict-fn2" \
  -H "Content-Type: application/json" \
  -d '{"features":[1,2,3,4]}'










