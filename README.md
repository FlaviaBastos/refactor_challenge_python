# refactor_challenge_python

Imagine that this repo was legacy code that is currently in production. How would you refactor the code to make is easier to understand? How would you test this to make sure it's working as expected?
Please use your understanding of design patterns and SOLID principles to break the core.py file into smaller discrete pieces.


## Run the code
```
python3 main.py
```


## Install dependencies
```
pip3 install -r requirements.txt
```


## Run tests
```
pytest
```

### Considerations
There are a few functions that have side-effects instead of return values but my main goal was to preserve the functionality as much as possible and opted to not change these functions.
