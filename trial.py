import pandas as pd
import numpy as np
data_set_1=pd.DataFrame({
    'OrderId':[1,2,3,4],
    'Product':['smartwatch','watch','cellphone','bottle'],
    'Sales':[100,200,450,500]
})
data_set_2=pd.DataFrame({
    'OrderId':[3,4,5,6],
    'Product':['cellphone','bottle','mouse','keyboard'],
    'Sales':[450,500,300,120]
})
print(f"data set 1 is{data_set_1}")
print (f"data set 2 is {data_set_2}")
#for merging
merge_data=pd.merge(data_set_1,data_set_2,on='OrderId',how='inner',suffixes=('_left','_right'))
print(f"merged data :{merge_data}")
#for concatination
concat_data=pd.concat([data_set_1,data_set_2],ignore_index=True)
print(f"after combining{concat_data}")

reshape_data=pd.DataFrame({
                           'Month':['jan','feb','march','april'],
                           'Product_A':[200,500,800,780],
                           'Product_B':[200,500,400,300]
                           })
print(f"reshapable data{reshape_data}")
melted_data=pd.melt(reshape_data,id_vars=['Month'],var_name='Product',value_name='Sales')
print(f"melted data:{melted_data}")

pivotable_data=pd.DataFrame({
    'Month':['jan','jan','feb','feb','march','march'],
    'Product':['Product_A','Product_A','Product_B','Product_B','Product_c','product_c'],
    'Sales':[200,210,300,521,250,410]
})
print(f"pivotable data{pivotable_data}")

pivoted_data=pivotable_data.pivot(index='Month',columns='Product',values='Sales')

print(f"after pivoted data{pivoted_data}")

pivoted_data.loc['jan','Product_A']=np.nan
pivoted_data.loc['feb','Product_B']=np.nan

print("pivoted data{pivoted_data}")
filled_data=pivoted_data.fillna(pivoted_data.mean())
print(f"missing values handled{filled_data}")

print("descibing the data",filled_data.describe()")
