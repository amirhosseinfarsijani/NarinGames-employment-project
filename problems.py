def preEDA_downloads(data):
    import pandas as pd
    
    # fix
    data.downloads.iloc[87] = '70,000,000+'
    data.downloads.iloc[154] = '0+'
    
    pd.set_option('display.max_rows', len(data.downloads))
    print(data.downloads)
    
    # remove ',' and '+' from downloads column
    data.downloads = data.downloads.str.replace('\+*\,*', '', regex=True)
    
    # convert str to int
    data.downloads = data.downloads.astype(int)
    
    
def preEDA_score_num(data):
    import pandas as pd
    
    #remove ','
    data.score_num = data.score_num.str.replace('\,*', '', regex=True)
    
    #convert str to int
    data.score_num = data.score_num.astype(int)
    
def preProcess_new_Size(data):
    import pandas as pd
    
    # remove M from Size column
    data.Size = data.Size.str.replace('M*', '', regex=True)
    
    #remove for convert to float
    data.Size = data.Size.apply(pd.to_numeric, errors='coerce')
    data.dropna(inplace=True)
    
def preProcess_new_Installs(data):
    import pandas as pd
    
    # remove ',' and '+' from downloads column
    data.Installs = data.Installs.str.replace('\+*\,*', '', regex=True)
    data.Installs = data.Installs.astype(int)
    
   
    