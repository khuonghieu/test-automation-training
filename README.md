- Clone the project: 
```
git clone https://github.com/khuonghieu/test-automation-training
```  

- Install required packages:
```
pip install behave
pip install selenium
```

- Navigate to the project:
```
cd test-automation-training
```

# Run the unit tests:

- Run all the unit tests:
```
python3 -m unittest --verbose
```

- Run a certain unit test file:
```
python3 -m unittest <dir/testfile.py> --verbose
```
For example:
```
python3 -m unittest test/TestLandingPage.py --verbose
```
  
# Run the features:

- Run test on all features:
```
behave ./features
```
- Run test on a certain feature:
```
behave ./features/<feature_file_name>
```

  Note: the account ID currently being used for testing is 17536. Please terminate its subscription before running the test suite.
