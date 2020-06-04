# This code gives us all the shots taken by belgium alone in the WC2018.
# Don't mind the name, i've created this for eng, but was lazy to change it again
# If you want a specific player's shots alone for all matches, just change the total_attempts line where i've specified belgium
# Feel free to edit the file for increasing any efficiency!

def key_pass(filename):
    total_attempts1 = pd.DataFrame()
    for item in filename:
        total_attempts = pd.DataFrame()
        with open(item) as f:
            comp = json.load(f)
        eng = pd.json_normalize(comp)
        for team in eng['possession_team.name'].unique():
            if team != 'Belgium':
                opp = team
        eng = pd.json_normalize(comp).assign(Oppn = opp)
        eng_pan = eng[['shot.statsbomb_xg','minute','player.name','shot.outcome.name','shot.key_pass_id','location','type.name','play_pattern.name','possession_team.name','Oppn']]
        eng_pan.rename(columns={'shot.statsbomb_xg':'Statsbomb_xG','shot.outcome.name':'Outcome','shot.key_pass_id':'Keypass_id'})
        total_attempts = eng_pan.loc[(eng_pan['type.name'] == 'Shot') & (eng_pan['possession_team.name'] == 'Belgium')]
        #total_attempts.reset_index(drop=True,inplace=True)

        total_attempts1 = total_attempts1.append(total_attempts,ignore_index=True)
    return(total_attempts1)
    
    
output = key_pass(['7552.json','7536.json','7570.json','7584.json','8650.json','8655.json','8657.json'])
output
