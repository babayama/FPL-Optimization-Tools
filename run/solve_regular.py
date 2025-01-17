import os
import sys
import pathlib
import json
import datetime

if __name__=="__main__":
    base_folder = pathlib.Path()
    sys.path.append(str(base_folder / "../src"))
    from multi_period_dev import connect, get_my_data, prep_data, solve_multi_period_fpl

    with open('regular_settings.json') as f:
        options = json.load(f)

    session, team_id = connect()
    if session is None and team_id is None:
        exit(0)
    elif team_id is None:
        with open('team.json') as f:
            my_data = json.load(f)
    else:
        my_data = get_my_data(session, team_id)
    data = prep_data(my_data, options)

    result = solve_multi_period_fpl(data, options)
    print(result['summary'])
    time_now = datetime.datetime.now()
    stamp = time_now.strftime("%Y-%m-%d_%H-%M-%S")
    result['picks'].to_csv(f"results/regular_{stamp}.csv")
    