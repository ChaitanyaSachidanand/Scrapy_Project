import pandas as pd
dictionary={"name":"abc","age":2,"gen":"addvd","fnsuvusd":1322}
output = pd.DataFrame()
output = output.append(dictionary, ignore_index=True)
dictionary={"name":"abc","age":3,"gen":"addvd","fnsuvusd":1322}
output = output.append(dictionary, ignore_index=True)
dictionary={"name":"abc","age":4,"gen":"addvd","fnsuvusd":1322}
output = output.append(dictionary, ignore_index=True)
dictionary={"name":"abc","age":5,"gen":"addvd","fnsuvusd":1322}
output = output.append(dictionary, ignore_index=True)
dictionary={"name":"abc","age":6,"gen":"addvd","fnsuvusd":1322}
print(output.head())

output = pd.DataFrame()
df_dictionary = pd.DataFrame([dictionary])
output = pd.concat([output, df_dictionary], ignore_index=True)
print(output.head())