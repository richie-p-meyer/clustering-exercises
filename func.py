def outlier_detector(df,column,k=1.5):
    q1,q3 = df[column].quantile([.25,.75])
    iqr = q3 - q1
    upper_bound = q3 +k*iqr
    lower_bound = q1 -k*iqr
    print(column, lower_bound,upper_bound)
    return np.where(df[column]> upper_bound,1,0), np.where(df[column]< lower_bound,1,0)

def assign_outlier(df, cols):
    '''
    Returns a new df with outlier detection for passed in columns
    '''
    for col in cols:
        df[f'{col}_upper_outliers'],df[f'{col}_lower_outliers'] = outlier_detector(df,col)
    return df

def handle_missing_values(df, prop_required_column, prop_required_row):
    temp = explore_nulls(df) 
    cols_drop = temp[temp.null_percent>prop_required_column]['column_name'].values.tolist()
    df.drop(cols_drop,axis=1)

    df['row_missing'] = df.isnull().sum(axis=1)/df.shape[1] #These two lines take care of the rows
    df.drop(df[df.row_missing>.4].index)
        
    return df