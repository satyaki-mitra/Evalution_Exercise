import pandas as pd
nodes = ["google.com", "google.in", "facebook.com", "kraysoft.in", "kraysoft.com", "amazon.in", "myntra.com", "jabong.com", "flipkart.com", "facebook.in"]
    
for i in nodes:
    response = "ping -c 50 i"
    pd.to_csv("response"+i+".csv")
    
