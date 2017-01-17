import re
import pandas as pd
import sys

pattern = re.compile(r"[\W\s.,!?:;\"()<>#$=-\[\]\\/]+")

#df = pd.read_csv('./datasets/forum_node.tsv', delimiter='\t', usecols=['body'])
df = pd.read_csv(sys.stdin, delimiter='\t', usecols=['body'])
count = int(0)
columnbody = df['body']
while (count < columnbody.size):
    row = next(df.iterrows())
    body = str(columnbody[count])
    data = pattern.split(body.strip())
    for item in data:
        print(item + "\t" + "1")
    count += int(1)
