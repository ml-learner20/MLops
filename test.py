import joblib
var1="prediction_service\model\model.joblib"
a = joblib.load(var1)
d=a.predict([[12,12,12,12,12,12,12,12,17,17,17]])
print(d)