import pandas as pd

raw = pd.read_csv('core/data/twitter_accounts.csv')

data = raw.rename(columns = {
    'Rank': 'rank',
    'Account name': 'account_name',
    'Owner': 'owner', 
    'Followers\n(millions)': 'million_followers',
    'Occupation': 'occupation',
    'Citizenship': 'citizenship'
})

