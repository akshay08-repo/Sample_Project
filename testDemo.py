import unittest
import demo
import sys
import pandas as pd
import csv
import os
import pytest

class knownlengths(unittest.TestCase):
    def test_length_arguments(self):
        result = demo.length_cal()
        if result == 1 :
            print("Error as there are no csv files give in the Command line")
        elif result == 2:
            print("Error as there is only 1 csv file and nothing to merge")
        else:
            all_df = []
            for i in range(1, result):
                # open(sys.argv[i],'rb')
                df = pd.read_csv(sys.argv[i], error_bad_lines=False)
                df['filename'] = sys.argv[i]
                all_df.append(df),
            merged_df = pd.concat(all_df, ignore_index=True)
            merged_df = merged_df.loc[:, ~merged_df.columns.str.contains('^Unnamed')]
            merged_df = merged_df.to_csv()
            print(merged_df)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


