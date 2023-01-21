"Test of the relevant libraries"
try:
    import numpy as np
    import pandas as pa
    import matplotlib

    print(f"numpy version: {np.__version__}")
    print(f"pandas version: {pa.__version__}")
    print(f"matplotlib version: {matplotlib.__version__}")

except Exception as error:
    print("Something wrong with the library import:")
    print(error)
