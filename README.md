# How to run all the tests:

- Clone the project: 
```
git clone https://github.com/khuonghieu/test-automation-training
```  

- Navigate to the project:
```
cd test-automation-training
```

- Run all the tests:
```
python3 -m unittest --verbose
```

- Run a certain test file:
```
python3 -m unittest <dir/testfile.py> --verbose
```
For example:
```
python3 -m unittest test/TestLandingPage.py --verbose
```
  
  Note: the account ID currently being used for testing is 17536. Please terminate its subscription before running the test suite.
