import pandas as pd
data = pd.read_csv('csv/sampleInsurance.csv',index_col=0)
#for agents name
def alldata(name):
    dagentdata = data[data['Insurer'] == name]
    return dagentdata

def countofall(name):
    dagentdata = alldata(name)
    count = dagentdata['Name'].count()
    return count

def policymax(name):
    policydata = alldata(name)
    policy = policydata.groupby('PolicyName')
    countofpolicy = policy['Insurer'].value_counts().reset_index(name='counts_of_names')
    max = countofpolicy[countofpolicy.counts_of_names == countofpolicy.counts_of_names.max()]
    max_column = max['counts_of_names']
    max_value = max_column.iloc[0]
    policy_column = max['PolicyName']
    policyname = policy_column.iloc[0]
    data = {'policy':policyname,'counts':max_value}
    return data
def allpolicy(name):
    policydata = alldata(name)
    policy = policydata.groupby('PolicyName')
    countofpolicy = policy['Insurer'].value_counts().reset_index(name='counts_of_names')
    policynames =  countofpolicy['PolicyName'].values.tolist()
    policycounts = countofpolicy['counts_of_names'].values.tolist()
    data = {'policyname':policynames,'policycounts':policycounts}
    return data
def policyyear(username):
    policydata=alldata(username)
    policydata['EffectiveDate'] = pd.to_datetime(policydata['EffectiveDate'])
    year = policydata.groupby(policydata.EffectiveDate.dt.year)
    countofpolicy = year['Insurer'].value_counts().reset_index(name='counts_of_names')
    policyyears = countofpolicy['EffectiveDate'].values.tolist()
    policycounts = countofpolicy['counts_of_names'].values.tolist()
    data = {'policyyears': policyyears, 'policycounts': policycounts}
    return data
def datawithdate(username,startdate,enddate):
    policydata = alldata(username)
    policydata['EffectiveDate'] = pd.to_datetime(policydata['EffectiveDate'])
    mask = (policydata['EffectiveDate'] > startdate) & (policydata['EffectiveDate'] <= enddate)
    df = policydata.loc[mask]
    names = df['Name']
    dates = df['EffectiveDate']
    details = {'names':names,'dates':dates}
    return details

def merge2csv(urloffile):
    data2 = pd.read_csv('csv/'+urloffile)
    results=data.append(data2,ignore_index=True)
    results.to_csv('csv/sampleInsurance.csv')
    return {'success':'true'}
#for agents
#for company
def compalldata(name):
    dagentdata = data[data['InsuranceCompany'] == name]
    return dagentdata

def compcountofall(name):
    dagentdata = compalldata(name)
    count = dagentdata['InsuranceCompany'].count()
    return count

def comppolicymax(name):
    policydata = compalldata(name)
    policy = policydata.groupby('PolicyName')
    countofpolicy = policy['InsuranceCompany'].value_counts().reset_index(name='counts_of_names')
    max = countofpolicy[countofpolicy.counts_of_names == countofpolicy.counts_of_names.max()]
    max_column = max['counts_of_names']
    max_value = max_column.iloc[0]
    policy_column = max['PolicyName']
    policyname = policy_column.iloc[0]
    data = {'policy':policyname,'counts':max_value}
    return data

def compallpolicy(name):
    policydata = compalldata(name)
    policy = policydata.groupby('PolicyName')
    countofpolicy = policy['InsuranceCompany'].value_counts().reset_index(name='counts_of_names')
    policynames =  countofpolicy['PolicyName'].values.tolist()
    policycounts = countofpolicy['counts_of_names'].values.tolist()
    data = {'policyname':policynames,'policycounts':policycounts}
    return data
def comppolicyyear(username):
    policydata=compalldata(username)
    policydata['EffectiveDate'] = pd.to_datetime(policydata['EffectiveDate'])
    year = policydata.groupby(policydata.EffectiveDate.dt.year)
    countofpolicy = year['InsuranceCompany'].value_counts().reset_index(name='counts_of_names')
    policyyears = countofpolicy['EffectiveDate'].values.tolist()
    policycounts = countofpolicy['counts_of_names'].values.tolist()
    data = {'policyyears': policyyears, 'policycounts': policycounts}
    return data
def compdatawithdate(username,startdate,enddate):
    policydata = compalldata(username)
    policydata['EffectiveDate'] = pd.to_datetime(policydata['EffectiveDate'])
    mask = (policydata['EffectiveDate'] > startdate) & (policydata['EffectiveDate'] <= enddate)
    df = policydata.loc[mask]
    names = df['Name']
    dates = df['EffectiveDate']
    details = {'names':names,'dates':dates}
    return details

def compempdata(username):
    policydata=compalldata(username)
    policy = policydata.groupby('Insurer')
    countofpolicy = policy['InsuranceCompany'].value_counts().reset_index(name='counts_of_policy')
    Insurername = countofpolicy['Insurer']
    countspolicy = countofpolicy['counts_of_policy']
    empdetails={'Insurername':Insurername,'countspolicy':countspolicy}
    return empdetails

def compmerge2csv(urloffile):
    data2 = pd.read_csv('csv/'+urloffile)
    results=data.append(data2,ignore_index=True)
    results.to_csv('csv/sampleInsurance.csv')
    return {'success':'true'}
#for company ends