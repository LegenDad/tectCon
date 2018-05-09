
## IRIS


```python
import numpy as np
import pandas as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
```

### Train Test Split


```python
iris_tr, iris_te, y_tr, y_te = train_test_split(
    iris['data'], 
    iris['target'], 
    train_size = 0.7, 
    test_size = 0.3, 
    random_state = 0)
print(f"train size : {iris_tr.shape}")
print(f"test size : {iris_te.shape}")
```

    train size : (105, 4)
    test size : (45, 4)
    

### KNN


```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(iris_tr, y_tr)
```




    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
               metric_params=None, n_jobs=1, n_neighbors=1, p=2,
               weights='uniform')




```python
pred_knn = knn.predict(iris_te)
print(f"KNN_accuracy : {knn.score(iris_te, y_te):.4f}")
```

    KNN_accuracy : 0.9778
    

### Multinomial classification


```python
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression().fit(iris_tr, y_tr)
pred_lr = lr.predict(iris_te)
print(f"Logistic_accuracy : {lr.score(iris_te, y_te):.4f}")
```

### DecisionTreeClassifier


```python
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier().fit(iris_tr, y_tr)
pred_tree = tree.predict(iris_te)
print(f"Tree_accuracy : {tree.score(iris_te, y_te):.4f}")
```

    Tree_accuracy : 0.9778
    

### GradientBoostingClassifier


```python
from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier().fit(iris_tr, y_tr)
pred_gb = gbc.predict(iris_te)
print(f"GradientBoostingClassifier_accuracy : {gbc.score(iris_te, y_te):.4f}")
```

    GradientBoostingClassifier_accuracy : 0.9778
    


```python
print(f"KNN_accuracy                        : {accuracy_score(y_te, pred_knn)}")
print(f"Logistic_accuracy                   : {accuracy_score(y_te, pred_lr)}")
print(f"Tree_accuracy                       : {accuracy_score(y_te, pred_tree)}")
print(f"GradientBoostingClassifier_accuracy : {accuracy_score(y_te, pred_gb)}")

```

    KNN_accuracy                        : 0.9777777777777777
    Logistic_accuracy                   : 0.8888888888888888
    Tree_accuracy                       : 0.9777777777777777
    GradientBoostingClassifier_accuracy : 0.9777777777777777
    

### Confusion Matrix


```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
```


```python
classification_report(y_te, pred_knn)
```




    '             precision    recall  f1-score   support\n\n          0       1.00      1.00      1.00        16\n          1       1.00      0.94      0.97        18\n          2       0.92      1.00      0.96        11\n\navg / total       0.98      0.98      0.98        45\n'




```python
confusion_matrix(y_te, pred_knn) 
```




    array([[16,  0,  0],
           [ 0, 17,  1],
           [ 0,  0, 11]], dtype=int64)




```python
confusion_matrix(y_te, pred_lr)
```




    array([[16,  0,  0],
           [ 0, 13,  5],
           [ 0,  0, 11]], dtype=int64)




```python
confusion_matrix(y_te, pred_tree)
```




    array([[16,  0,  0],
           [ 0, 17,  1],
           [ 0,  0, 11]], dtype=int64)




```python
confusion_matrix(y_te, pred_gb)
```




    array([[16,  0,  0],
           [ 0, 17,  1],
           [ 0,  0, 11]], dtype=int64)



## Conclusion


```python
print(f"KNN_accuracy                        : {knn.score(iris_te, y_te):.4f}")
print(f"Logistic_accuracy                   : {lr.score(iris_te, y_te):.4f}")
print(f"Tree_accuracy                       : {tree.score(iris_te, y_te):.4f}")
print(f"GradientBoostingClassifier_accuracy : {gbc.score(iris_te, y_te):.4f}")
```

    KNN_accuracy                        : 0.9778
    Logistic_accuracy                   : 0.8889
    Tree_accuracy                       : 0.9778
    GradientBoostingClassifier_accuracy : 0.9778
    
