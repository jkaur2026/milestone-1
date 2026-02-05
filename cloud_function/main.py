import joblib
import numpy as np

with open("model.pkl", "rb") as f:
    model = joblib.load("model.pkl")

def predict(request):
    """
    HTTP Cloud Function.
    Expects JSON: {"features":[f1,f2,f3,f4]}
    """
    data = request.get_json(silent=True) or {}
    features = data.get("features")

    if not isinstance(features, list):
        return ({"error": "Missing 'features' list in JSON body"}, 400)

    if len(features) != 4:
        return ({"error": f"Expected 4 features, got {len(features)}"}, 400)

    X = np.array(features, dtype=float).reshape(1, -1)
    pred = int(model.predict(X)[0])
    
    probs = None
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X)[0].tolist()

    return {"prediction": pred, "probabilities": probs}
