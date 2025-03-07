import sys
import pandas as pd

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    
    for f in filenames:
        data = pd.read_csv(f)
    
        if action == '--min':
            values = data.min(axis=1)
        elif action == '--mean':
            values = data.mean(axis=1)
        elif action == '--max':
            values = data.max(axis=1)
            
        for m in values:
            print(m)
            
if __name__ == '__main__':
    main()
                                                                
