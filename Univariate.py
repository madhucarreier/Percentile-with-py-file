import pandas as pd
import numpy as np
class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual

    def freqTable(colunName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","Cusum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cusum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable

    def NewUnivariate(dataset,quan):
        descriptive = pd.DataFrame(
            index=[
                "Mean", "Median", "Mode", "Q1:25%", "Q2:50%", "Q3:75%", "99%", "Q4:100%",
                "IQR", "1.5rule", "Lesser", "Greater", "min", "max"
            ],
            columns=quan
        )
        for columnName in quan:
            descriptive.loc["Mean", columnName] = dataset[columnName].mean()
            descriptive.loc["Median", columnName] = dataset[columnName].median()
            descriptive.loc["Mode", columnName] = dataset[columnName].mode()[0]
            descriptive.loc["Q1:25%", columnName] = dataset.describe().loc["25%", columnName]
            descriptive.loc["Q2:50%", columnName] = dataset.describe().loc["50%", columnName]
            descriptive.loc["Q3:75%", columnName] = dataset.describe().loc["75%", columnName]
            descriptive.loc["99%", columnName] = np.percentile(dataset[columnName].dropna(), 99)
            descriptive.loc["Q4:100%", columnName] = dataset.describe().loc["max", columnName]
            descriptive.loc["IQR", columnName] = descriptive.loc["Q3:75%", columnName] - descriptive.loc["Q1:25%", columnName]
            descriptive.loc["1.5rule", columnName] = 1.5 * descriptive.loc["IQR", columnName]
            descriptive.loc["Lesser", columnName] = descriptive.loc["Q1:25%", columnName] - descriptive.loc["1.5rule", columnName]
            descriptive.loc["Greater", columnName] = descriptive.loc["Q3:75%", columnName] + descriptive.loc["1.5rule", columnName]
            descriptive.loc["min", columnName] = dataset.describe().loc["min", columnName]
            descriptive.loc["max", columnName] = dataset.describe().loc["max", columnName]
        return descriptive
        def NewUnivariate(dataset,quan):
            descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%",
                                       "Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","min","max"],columns=quan)
            for columnName in quan:
                descriptive[columnName]["Mean"]=dataset[columnName].mean()
                descriptive[columnName]["Median"]=dataset[columnName].median()
                descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
                descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
                descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
                descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
                descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
                descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
                descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
                descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
                descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
                descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
                descriptive[columnName]["min"]=dataset[columnName].min()
                descriptive[columnName]["max"]=dataset[columnName].max()
                
                
        return descriptive

    def NewfreqTable(columnName, dataset):
        df_freq = pd.DataFrame()
        counts = dataset[columnName].value_counts()
        df_freq["Unique_values"] = dataset[columnName].value_counts().index
        df_freq["Frequency"] = dataset[columnName].value_counts().values
        df_freq["Relative_frequency"] = df_freq["Frequency"] / df_freq["Frequency"].sum()
        df_freq["Cumsum"] = df_freq["Relative_frequency"].cumsum()
        return df_freq

        
        