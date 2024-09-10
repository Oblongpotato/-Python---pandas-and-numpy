### code to update and save existing csv file ### 
## Code File 2## 
 
import pandas as pd 
import numpy as np 

file_path = 'employee.csv' 

df = pd.read_csv(file_path)  

print (df) 

# auto load titles according to Genders


df['Titles'] = np.where(df['Genders'] == "Female", "Mrs.", "Mr.") 

#reorder headers 
df = df[['Titles', 'First Name', 'Last Name', 'Genders']] 

df filename = 'updated_employee.csv' 
df.to_csv(filename,index = False) 
print("employee.csv updated and saved as " + filename)