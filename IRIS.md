
## IRIS


```python
import numpy as np
import pandas as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```


```python
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
```


```python
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
```


```python
print(f"KNN_accuracy : {knn.score(iris_te, y_te):.4f}")
```

    KNN_accuracy : 0.9778


### Multinomial classification


```python
from sklearn.linear_model import LogisticRegression
```


```python
lr = LogisticRegression().fit(iris_tr, y_tr)
```


```python
pred_lr = lr.predict(iris_te)
```


```python
print(f"Logistic_accuracy : {lr.score(iris_te, y_te):.4f}")
```

    Logistic_accuracy : 0.8889


### DecisionTreeClassifier


```python
from sklearn.tree import DecisionTreeClassifier
```


```python
tree = DecisionTreeClassifier().fit(iris_tr, y_tr)
```


```python
pred_tree = tree.predict(iris_te)
print(f"Tree_accuracy : {tree.score(iris_te, y_te):.4f}")
```

    Tree_accuracy : 0.9778


### GradientBoostingClassifier


```python
from sklearn.ensemble import GradientBoostingClassifier
```


```python
gbc = GradientBoostingClassifier().fit(iris_tr, y_tr)
```


```python
pred_gb = gbc.predict(iris_te)
print(f"GradientBoostingClassifier_accuracy : {gbc.score(iris_te, y_te):.4f}")
```

    GradientBoostingClassifier_accuracy : 0.9778


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

