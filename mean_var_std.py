import numpy as np

def calculate(list):
    # Expecting a 9-element list to be converted to a 3x3 array
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array( [ list[:3], list[3:6], list[6:9] ] )

    
    
    calculations = {
        'mean': [ np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).tolist() ],
        'variance': [ np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).tolist() ],
        'standard deviation': [ np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).tolist() ],
        'max': [ np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).tolist() ],
        'min': [ np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).tolist() ],
        'sum': [ np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).tolist() ]
    }

    return calculations