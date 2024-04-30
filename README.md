# pythontest
**Python exercise**
Create an address book application where API users can create, update and deleteaddresses.
The address should:- contain the coordinates of the address.- be saved to an SQLite database.- be validated
API Users should also be able to retrieve the addresses that are within a given distance and location coordinates.

**Requirements:**
- Python 3
- IDE (Visual Studio Code)
- DB Broswer for SQLite
- Postman

**Steps on running the application:**
1. Clone or download here - https://github.com/jacevelasquez/pythontest/
2. Open terminal and change directory to the cloned repository
3. Install necessary libraries by typing this command - ```pip install -r .\requirements.txt```
4. To run the application locally type this command - ```uvicorn main:app --reload```
![image](https://github.com/jacevelasquez/pythontest/assets/44248245/729808b2-cab8-426f-b86d-35513ef0d094)

**File Structure**
- main.py - main script of the application
- validation.py - validation script of the application
- requirements.txt - list of libraries needed by the application
- test.db - database of the application
- Address book.postman_collection.json - Postman collection (REST) of the application for testing

**How to test APIs using Postman**
1. Open Postman app
2. Import Address book.postman_collection.json
   
![image](https://github.com/jacevelasquez/pythontest/assets/44248245/2e760c84-ce08-4c2d-b9ab-24c3b8467391)

3. Select any of the requests to test

![image](https://github.com/jacevelasquez/pythontest/assets/44248245/af06153e-de1a-4aed-8c8c-882f04e14e7e)
3.1 Request Selection
3.2 API endpoint
3.3 Send request button
3.4 Request body section
3.5 Response body section

**API endpoints**
- Get /items/{item_id} - get address by item_id
- Get /all - get all address
- Post /items - add or insert address (name, description, latitude and longitude are required)
- Put /items/{item_id} - update address (can be updated even if one key value pair is requested)
- Delete /items/{item_id} - delete address by item_id
- Get /areas - get addresses that are within a given distance and location coordinates (distance, latitude and longitude are required)
