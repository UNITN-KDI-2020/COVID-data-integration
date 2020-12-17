def to_csv_batch(src_csv, dst_dir, filename, size=10000, index=False):

    import pandas as pd
    import math

    # Read source csv
    df = pd.read_csv(src_csv)

    # Initial values
    low = 0
    high = size

    # Loop through batches
    for i in range(math.ceil(len(df) / size)):

        fname = dst_dir+'/' + filename + str(i+1) + '.csv'
        df[low:high].to_csv(fname, index=index)

        # Update selection
        low = high
        if (high + size < len(df)):
            high = high + size
        else:
            high = len(df)


to_csv_batch('../../dataset/Formal Modeling/data/Reference_hospitalization_all_locs.csv',
             '../../dataset/Data Integration/data/Reference_hospitalization', 'Reference_hospitalization_part', 9000)

to_csv_batch('../../dataset/Formal Modeling/data/COVID-19-geographic-disbtribution-worldwide.csv',
             '../../dataset/Data Integration/data/covid19', 'COVID-19-geographic-disbtribution-worldwide')
