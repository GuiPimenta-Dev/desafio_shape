# This repository is dedicated to solving the challenge proposed by the shape digital company

The challenge is presented below:

<img src = "utils/hard-skills-assignment-shape.PNG">


The challenge was to create a simple python api, but I took the liberty of creating a frontend to consume the available endpoints.

**The front functionalities is presented below:**

<img src = "utils/gif-frontend2.gif">

**The front is hosted on netlify, and you can easily acess it on : https://shapechallenge.netlify.app/**


The api is hosted on heroku and has the following endpoints:

<img src ="utils/available_endpoints.PNG">


**The base url is https://shapechallenge.herokuapp.com/**

**It`s possible to test the available endpoints on https://shapechallenge.herokuapp.com/docs.html:**

<img src="utils/api_documentation.PNG">

<img src="utils/created_vessel_endpoint.PNG">

### Test Output
```bash
$ pytest .
Test session starts (platform: win32, Python 3.9.4, pytest 6.2.4, pytest-sugar 0.9.4)
rootdir: C:\Users\guial\PycharmProjects\home_automation\tests
plugins: sugar-0.9.4
collecting ... 
 test_equipament.py ✓                                                                                   5% ▌
 test_equipament.py ✓✓                                                                                 11% █▏        
 test_equipament.py ✓✓✓                                                                                16% █▋        
 test_equipament.py ✓✓✓✓                                                                               21% ██▏       
 test_equipament.py ✓✓✓✓✓                                                                              26% ██▋       
 test_equipament.py ✓✓✓✓✓✓                                                                             32% ███▎      
 test_equipament.py ✓✓✓✓✓✓✓                                                                            37% ███▊      
 test_equipament.py ✓✓✓✓✓✓✓✓                                                                           42% ████▎     

 test_status.py ✓                                                                                      47% ████▊     
 test_status.py ✓✓                                                                                     53% █████▍    
 test_status.py ✓✓✓                                                                                    58% █████▊    

 test_vessel.py ✓                                                                                      63% ██████▍   
 test_vessel.py ✓✓                                                                                     68% ██████▉   
 test_vessel.py ✓✓✓                                                                                    74% ███████▍  
 test_vessel.py ✓✓✓✓                                                                                   79% ███████▉  

 test_vessels.py ✓                                                                                     84% ████████▌ 
 test_vessels.py ✓✓                                                                                    89% ████████▉ 
 test_vessels.py ✓✓✓                                                                                   95% █████████▌ 
 test_vessels.py ✓✓✓✓                                                                                  100% ██████████                                                                                                                                    

Results (4.48s):
      19 passed
```
