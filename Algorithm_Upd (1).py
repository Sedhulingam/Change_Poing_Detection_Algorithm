import pandas as pd

def change_point_detection_v2(temp):
    demo=[]
    start = None
    for i in range(len(temp) - 1):
        if (temp[i+1] - temp[i] > -0.6 and temp[i + 1] - temp[i] < 0.6 ):
            if start is None:
                start = temp[i]
        else:
            if start is not None:
                if(start == temp[i]):
                    pass
                else:
                    demo.append(temp[i])       
                start = None
    if start is not None:
        demo.append(temp[i])
      
    max1 = max(temp)
    if max1 not in demo:
        demo.append(max1)   
    demo.sort()  
    i = 0
    j = 0
    result = []    
    while j < len(demo) - 1:
        if round(demo[j + 1],0) - round(demo[j],0) <= 1:
            j += 1
        else:
            i = j
            result.append(demo[i])
            j += 1   
    result.append(demo[-1])    
    if max1 not in result:
        result.append(max1)
    
    return result

df = pd.read_excel('Leg10.xlsx')
temp = df[df['Legend'] == df['Legend'].iloc[0]]['Temp'].tolist()
result = change_point_detection_v2(temp)

print(result)

