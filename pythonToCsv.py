### code to create a csv file with random data ### 
## Code File 1## 

!pip install pandas 
!pip install pandas faker 
import pandas as pd from faker 
import Faker import random 

fake = Faker() 

num_records = 10 

data = { 'First Name': [fake.first_name() for _ in range(num_records)], 'Last Name': [fake.last_name() for _ in range(num_records)] }  

df = pd.DataFrame(data) 
Print(df)

genders = ['Male','Male','Male','Female','Male','Female','Male','Female','Male','Male'] 

df['Genders'] = genders 

df filename = 'employee.csv' 

df.to_csv(filename, index=False) 

print(filename + ' file created') 
