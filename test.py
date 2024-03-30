import unittest
from train_model import load_iris, train_test_split, accuracy_score, joblib, LogisticRegression
import os  # Import the os module


class TestTrainModel(unittest.TestCase):
    def test_load_iris(self):
        # Test if the Iris dataset loads correctly
        iris = load_iris()
        self.assertEqual(iris.data.shape, (150, 4))
        self.assertEqual(len(iris.target), 150)

    def test_model_training(self):
        # Test if the model trains and predicts correctly
        iris = load_iris()
        X, y = iris.data, iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        self.assertTrue(0 <= accuracy <= 1)

    def test_model_saving(self):
        # Test if the model is saved correctly
        iris = load_iris()
        X, y = iris.data, iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)
        joblib.dump(model, 'test_iris_model.pkl')
        self.assertTrue(os.path.exists('test_iris_model.pkl'))


if __name__ == '__main__':
    unittest.main()
