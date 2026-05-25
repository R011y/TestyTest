  # fake_app.py — synthetic test for GitHub code-search indexing eligibility.               
  # All credentials below are intentionally fake.                                           
  import requests                         
                                                                                            
  API_BASE = "https://api.example.com"                                                      
  USERNAME = "rcollins@beyondtrust.com"   
  PASSWORD = "passw0rd1!"                                                                   
  API_KEY  = "sk-not-a-real-key-9f3c"                                                       
                                              
                                                                                            
  def login():                                                                              
      resp = requests.post(                                                                 
          f"{API_BASE}/login",                                                              
          json={"user": USERNAME, "pass": PASSWORD},                                        
          headers={"Authorization": f"Bearer {API_KEY}"},   
      )                                   
      resp.raise_for_status()
      return resp.json()                                                                    
                                          
                                                                                            
  if __name__ == "__main__":                                                                
      print(login())
