import pandas as pd
import numpy as np

if __name__ == '__main__':
    print "2016Q3.csv"
    df = pd.read_csv('../../cleandata/2013.csv', sep=';')
    print df.columns
    print len(df)
    print df.date.unique()
    print "2014 07"
    df = pd.read_csv('../../cleandata/2014.csv', sep=';')
    print df.columns
    print len(df)
    print df.date.unique()
    print "2014 08"
    df = pd.read_csv('../../cleandata/2015.csv', sep=';')
    print df.columns
    print len(df)
    print df.date.unique()
    print "2014 Q4"
    df = pd.read_csv('../../cleandata/2016.csv', sep=';')
    print df.columns
    print len(df)
    print df.date.unique()
    #
    # print "2013 Q1"
    # df = pd.read_csv('../../cleandata/2013Q1.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2013 Q2"
    # df = pd.read_csv('../../cleandata/2013Q2.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2013 Q3"
    # df = pd.read_csv('../../cleandata/2013Q3.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2013 Q4"
    # df = pd.read_csv('../../cleandata/2013Q4.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2014 Q1"
    # df = pd.read_csv('../../cleandata/2014Q1.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2014 Q2"
    # df = pd.read_csv('../../cleandata/2014Q2.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2014 Q3"
    # df = pd.read_csv('../../cleandata/2014Q3.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2014 Q4"
    # df = pd.read_csv('../../cleandata/2014Q4.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
    #
    # print "2015 Q2"
    # df = pd.read_csv('../../cleandata/2015Q2.csv', sep=';')
    # print df.columns
    # print len(df)
    # print df.date.unique()
