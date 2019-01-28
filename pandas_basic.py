import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,4,1]) # similar with 1D numpy
print(s)

dates = pd.date_range('20160101', periods=6)
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
print(df1['B'])
df2 = pd.DataFrame({'A' : 1.,
                       'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                        'D' : np.array([3] * 4,dtype='int32'),
                        'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo'})
print(df2)
print(df2.dtypes)

# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.describe())
# print(df.T)
# print(df.sort_index(axis=1, ascending=False))
# print(df.sort_values(by='B'))

############索引##############################
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df['A'], df.A)
print(df[0:3], df['20130102':'20130104'])

# select by label: loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df.loc['20130102', ['A','B']])

# select by position: iloc
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])

# mixed selection: ix
print(df.ix[:3, ['A', 'C']])
# Boolean indexing
print(df[df.A > 0])
#####################################################


#################修改值#############################
dates = pd.date_range('20130101', periods=6)
df4 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])

df4.iloc[2,2] = 1111
df4.loc['2013-01-03', 'D'] = 2222
df4.A[df.A>0] = 0
df4['F'] = np.nan
df4['G']  = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
print(df4)
####################################################

#################open&save#############################
# read from
data = pd.read_csv('AssetsImportCompleteSample.csv')
print(data)

# save to
data.to_pickle('AssetsImportCompleteSample.pickle')
#######################################################