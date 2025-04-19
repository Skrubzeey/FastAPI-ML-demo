import joblib
import pandas
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine

# załadowanie modelu oraz skalera
model = joblib.load('wine_model.pkl')
scaler = joblib.load('scaler.pkl')

# ładowanie danych dla modelu
data = load_wine(as_frame=True)
X = data.data
y = data.target

# dokonanie predykcji modelu
X_scaled = scaler.transform(X)
preds = model.predict(X_scaled)


# stworzenie testów jednostkowych
def test_predict_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    assert preds is not None


def test_prediction_length():
    """
    Test 2: Sprawdza, czy długość listy predykcji jest większa
    od 0 i czy odpowiada przewidywanej liczbie próbek testowych.
    """

    assert len(preds) > 0, "List cannot be empty"
    assert len(preds) == len(y), f"Returned {len(preds)}, was supposed to get {len(y)}"


def test_predictions_value_range():
    """
    Test 3: Sprawdza, czy wartości w predykcjach mieszczą się w
    spodziewanym zakresie
    """

    valid_classes = set(y)
    assert set(preds).intersection(y) == set(preds), "Predicted classes out of range"


def test_model_accuracy():
    """
    Test 4: Sprawdza, czy model osiąga co najmniej 70% dokładności.
    """
    model_accuracy = accuracy_score(y, preds)
    assert model_accuracy > 0.7, f"Model's accuracy is lower than threshold: {model_accuracy}"



