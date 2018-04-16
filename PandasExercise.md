

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
dat1 = pd.Series([1, 3, 5, np.nan, 6, 8])
dat1
```




    0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64




```python
type(dat1)
```




    pandas.core.series.Series




```python
dat2 = pd.Series([1, np.nan, 5, np.nan, 6, 8])
dat2
```




    0    1.0
    1    NaN
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64




```python
# 날짜 Data 생성
dates = pd.date_range('20130101', periods =6)
print(dates)
```

    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D')


#### dataframe 만들기


```python
df = pd.DataFrame(np.random.randn(6,4),
                 index = dates, columns = list("ABCD"))
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.070337</td>
      <td>-1.247492</td>
      <td>2.297970</td>
      <td>-2.348321</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.536316</td>
      <td>-0.427812</td>
      <td>0.827342</td>
      <td>-0.336684</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.449928</td>
      <td>-1.372955</td>
      <td>-0.452031</td>
      <td>-0.696063</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.372467</td>
      <td>0.436059</td>
      <td>-0.455822</td>
      <td>-0.385533</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.043319</td>
      <td>-0.856030</td>
      <td>-0.414888</td>
      <td>2.975314</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.012260</td>
      <td>-1.670923</td>
      <td>-0.257511</td>
      <td>0.176139</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({'A': 1. , 
                   'B' : pd.Timestamp('20130103'), 
                   'C' : pd.Series(1, index=list(range(4)), dtype= 'float32'),
                   'D' : np.array([3]*4, dtype = 'int32'), 
                   'E' : pd.Categorical(["test", "train", "test", "train"]), 
                   'F' : "foo"})
df2
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>2013-01-03</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>2013-01-03</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>2013-01-03</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>2013-01-03</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(df2)
```




    pandas.core.frame.DataFrame




```python
df2 = pd.DataFrame({'Date': dates, 
                   'A' : dat1, 'B': dat2})
df2
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>2013-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>2013-01-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>2013-01-03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2013-01-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.0</td>
      <td>6.0</td>
      <td>2013-01-05</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8.0</td>
      <td>8.0</td>
      <td>2013-01-06</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.dtypes
```




    A              float64
    B              float64
    Date    datetime64[ns]
    dtype: object




```python
df2.shape
```




    (6, 3)




```python
df2.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6 entries, 0 to 5
    Data columns (total 3 columns):
    A       5 non-null float64
    B       4 non-null float64
    Date    6 non-null datetime64[ns]
    dtypes: datetime64[ns](1), float64(2)
    memory usage: 224.0 bytes



```python
df2.index
```




    RangeIndex(start=0, stop=6, step=1)




```python
df3 = df2.copy()
df3
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>2013-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>2013-01-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>2013-01-03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2013-01-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.0</td>
      <td>6.0</td>
      <td>2013-01-05</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8.0</td>
      <td>8.0</td>
      <td>2013-01-06</td>
    </tr>
  </tbody>
</table>
</div>




```python
# set_index 인덱스 설정
df3_idx = df3.set_index("Date")
df3_idx
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>3.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>5.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>6.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>8.0</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3_idx.index
```




    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', name='Date', freq=None)




```python
df = pd.DataFrame({'month' : [1, 4, 7, 10, 12], 
                  'year' : [2012, 2014, 2013, 2014, 2015], 
                  'sale' : [55, 40, 84, np.nan, 30]})
df1 = df.set_index('month')
df1
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sale</th>
      <th>year</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>55.0</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40.0</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>7</th>
      <td>84.0</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30.0</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2_idx = df.set_index(['year', 'month'])
df2_idx
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>sale</th>
    </tr>
    <tr>
      <th>year</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <th>1</th>
      <td>55.0</td>
    </tr>
    <tr>
      <th>2014</th>
      <th>4</th>
      <td>40.0</td>
    </tr>
    <tr>
      <th>2013</th>
      <th>7</th>
      <td>84.0</td>
    </tr>
    <tr>
      <th>2014</th>
      <th>10</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2015</th>
      <th>12</th>
      <td>30.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.columns
```




    Index(['A', 'B', 'Date'], dtype='object')




```python
print(df)
df.describe()
```

       month  sale  year
    0      1  55.0  2012
    1      4  40.0  2014
    2      7  84.0  2013
    3     10   NaN  2014
    4     12  30.0  2015





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>sale</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.800000</td>
      <td>52.250000</td>
      <td>2013.600000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.438468</td>
      <td>23.528352</td>
      <td>1.140175</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>30.000000</td>
      <td>2012.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.000000</td>
      <td>37.500000</td>
      <td>2013.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>7.000000</td>
      <td>47.500000</td>
      <td>2014.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>10.000000</td>
      <td>62.250000</td>
      <td>2014.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12.000000</td>
      <td>84.000000</td>
      <td>2015.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(df2)
df2.T
```

         A    B       Date
    0  1.0  1.0 2013-01-01
    1  3.0  NaN 2013-01-02
    2  5.0  5.0 2013-01-03
    3  NaN  NaN 2013-01-04
    4  6.0  6.0 2013-01-05
    5  8.0  8.0 2013-01-06





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>NaN</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Date</th>
      <td>2013-01-01 00:00:00</td>
      <td>2013-01-02 00:00:00</td>
      <td>2013-01-03 00:00:00</td>
      <td>2013-01-04 00:00:00</td>
      <td>2013-01-05 00:00:00</td>
      <td>2013-01-06 00:00:00</td>
    </tr>
  </tbody>
</table>
</div>


