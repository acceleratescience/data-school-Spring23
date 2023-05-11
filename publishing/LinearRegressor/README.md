## Linear Regressor Packaging
This is a simple package that performs linear regression and saves the model weights. This was used to demonstrate the process of building and distributing a package on PyPi.

Developed by the Accelerate Science team at the Univeristy of Cambridge.


Create a virtual environment:

```bash
python -m venv .env
source .env/bin/activate
```

Or in Windows:

```bash
C:\> .env\Scripts\activate.bat
```

Now install build and twine:

```bash
pip install build twine
```

Build your package:

```bash
python -m build
```

And install a local version to test:

```bash
pip install -e .
```

We can test the install by running

```bash
run-csv test_data.csv coeffs.npy
```


## Distribution
Sign up to [Test PyPi](https://test.pypi.org). And then just run:

```bash
twine upload -r testpypi dist/*
```

Now if you want you can set up a separate environment and run

```bash
pip install -i https://test.pypi.org/simple/ linear-regressor
```

and either run the same script as earlier on the csv file, or import it into a Jupyter notebook.