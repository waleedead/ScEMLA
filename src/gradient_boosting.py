from sklearn.ensemble import GradientBoostingClassifier

def train_model(X, y=None):
    clf = GradientBoostingClassifier(learning_rate=0.003, n_estimators=100, max_depth=3)
    clf.fit(X, y)
    return clf

def predict_labels(model, X):
    return pd.Series(model.predict(X))
