import requests
import math

# Replace 'YOUR_STEAM_API_KEY' with your actual Steam API key
STEAM_API_KEY = ''

# Replace 'YOUR_STEAM_ID' with the Steam ID of the player whose stats you want to fetch
steam_id = '76561199223346730'

# Function to make an API request and return the response as a JSON object
def make_api_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: Status code {response.status_code}")
        return None

# Function to fetch the player's TF2 stats from the Steam API
def get_tf2_stats(steam_id):
    url = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=440&key={STEAM_API_KEY}&steamid={steam_id}'
    data = make_api_request(url)
    if data and 'playerstats' in data:
        return data['playerstats']['stats']
    else:
        print(f"Error fetching TF2 stats for Steam ID '{steam_id}'")
        return None



def timegood(time):
    time = int(time)
    pol = int(math.floor(time/3600))
    if math.floor(time/3600) > 0:
        if math.floor(int((time/(60*pol))-60)) < 10:
            if ((time)%60) < 10:
                return (str(math.floor(time/3600)) + ':0' + str(math.floor(int((time/(60*pol))-60))) + ':0' + str(((time)%60)))
            else:
                return (str(math.floor(time/3600)) + ':0' + str(math.floor(int((time/(60*pol))-60))) + ':' + str(((time)%60)))
        else:
            if ((time)%60) < 10:
                return (str(math.floor(time/3600)) + ':' + str(math.floor(int((time/(60*pol))-60))) + ':0' + str(((time)%60)))
            else:
                return (str(math.floor(time/3600)) + ':' + str(math.floor(int((time/(60*pol))-60))) + ':' + str(((time)%60)))
    else:
        if math.floor((time)/60) < 10:
            if time%60 < 10:
                return ('0' + str(math.floor((time)/60)) + ':0' + str((time)%60))
            else:
                return ('0' + str(math.floor((time)/60)) + ':' + str((time)%60))
        else:
            if time%60 < 10:
                return (str(math.floor((time)/60)) + ':0' + str((time)%60))
            else:
                return (str(math.floor((time)/60)) + ':' + str((time)%60))
    


# print(timegood(7561))

# Main function to fetch stats and store them in individual variables
def fetch_tf2_stats():
    tf2_stats = get_tf2_stats(steam_id)
    # print(tf2_stats)
    if tf2_stats:
        # Example: Fetching specific stats and storing them in variables
        scout_kills = 0
        scout_deaths = 0
        scout_time_played = 0
        pyro_kills = 0
        pyro_deaths = 0
        pyro_time_played = 0
        sniper_kills = 0
        sniper_deaths = 0
        sniper_time_played = 0
        soldier_kills = 0
        soldier_deaths = 0
        soldier_time_played = 0
        engineer_deaths = 0

        for stat in tf2_stats:
            if stat['name'] == 'Scout.accum.iNumberOfKills':
                scout_kills = stat['value']
            elif stat['name'] == 'Scout.accum.iDamageDealt':
                scout_damage = stat['value']
            elif stat['name'] == 'Scout.accum.iPointCaptures':
                scout_deaths = stat['value']
            elif stat['name'] == 'Scout.accum.iPlayTime':
                scout_time_played = stat['value']
            if stat['name'] == 'Pyro.accum.iNumberOfKills':
                pyro_kills = stat['value']
            elif stat['name'] == 'Pyro.accum.iDamageDealt':
                pyro_damage = stat['value']
            elif stat['name'] == 'Pyro.accum.iPointCaptures':
                pyro_deaths = stat['value']
            elif stat['name'] == 'Pyro.accum.iPlayTime':
                pyro_time_played = stat['value']
            if stat['name'] == 'Sniper.accum.iNumberOfKills':
                sniper_kills = stat['value']
            elif stat['name'] == 'Sniper.accum.iDamageDealt':
                sniper_damage = stat['value']
            elif stat['name'] == 'Sniper.accum.iPointCaptures':
                sniper_deaths = stat['value']
            elif stat['name'] == 'Sniper.accum.iPlayTime':
                sniper_time_played = stat['value']
            if stat['name'] == 'Soldier.accum.iNumberOfKills':
                soldier_kills = stat['value']
            elif stat['name'] == 'Soldier.accum.iDamageDealt':
                soldier_damage = stat['value']
            elif stat['name'] == 'Soldier.accum.iPointCaptures':
                soldier_deaths = stat['value']
            elif stat['name'] == 'Soldier.accum.iPlayTime':
                soldier_time_played = stat['value']
            if stat['name'] == 'Spy.accum.iNumberOfKills':
                spy_kills = stat['value']
            elif stat['name'] == 'Spy.accum.iDamageDealt':
                spy_damage = stat['value']
            elif stat['name'] == 'Spy.accum.iPointCaptures':
                spy_deaths = stat['value']
            elif stat['name'] == 'Spy.accum.iPlayTime':
                spy_time_played = stat['value']
            if stat['name'] == 'Engineer.accum.iNumberOfKills':
                engineer_kills = stat['value']
            elif stat['name'] == 'Engineer.accum.iDamageDealt':
                engineer_damage = stat['value']
            elif stat['name'] == 'Engineer.accum.iPointCaptures':
                engineer_deaths = stat['value']
            elif stat['name'] == 'Engineer.accum.iPlayTime':
                engineer_time_played = stat['value']
            if stat['name'] == 'Medic.accum.iNumberOfKills':
                medic_kills = stat['value']
            elif stat['name'] == 'Medic.accum.iDamageDealt':
                medic_damage = stat['value']
            elif stat['name'] == 'Medic.accum.iPointCaptures':
                medic_deaths = stat['value']
            elif stat['name'] == 'Medic.accum.iPlayTime':
                medic_time_played = stat['value']
            if stat['name'] == 'Heavy.accum.iNumberOfKills':
                heavy_kills = stat['value']
            elif stat['name'] == 'Heavy.accum.iDamageDealt':
                heavy_damage = stat['value']
            elif stat['name'] == 'Heavy.accum.iPointCaptures':
                heavy_deaths = stat['value']
            elif stat['name'] == 'Heavy.accum.iPlayTime':
                heavy_time_played = stat['value']
            if stat['name'] == 'Demoman.accum.iNumberOfKills':
                demoman_kills = stat['value']
            elif stat['name'] == 'Demoman.accum.iDamageDealt':
                demoman_damage = stat['value']
            elif stat['name'] == 'Demoman.accum.iPointCaptures':
                demoman_deaths = stat['value']
            elif stat['name'] == 'Demoman.accum.iPlayTime':
                demoman_time_played = stat['value']
        '''bitch = ['Scout', 'Pyro', 'Sniper', 'Soldier', 'Spy', 'Heavy']
        for stat in tf2_stats:
             for classes in bitch:
                if stat['name'] == classes + '.accum.iNumberOfKills':
                    temp = stat['value']
                    x = classes + '_kills'
                    
                    
                    my_dict = {}
                    tt = x
                    my_dict[tt] = temp
                    print(classes + ' Kills: ' + str(temp))
                elif stat['name'] == classes + '.accum.iDamageDealt':
                    scout_damage = stat['value']
                elif stat['name'] == classes + '.accum.iPointCaptures':
                    scout_deaths = stat['value']
                elif stat['name'] == classes + '.accum.iPlayTime':
                    scout_time_played = stat['value']'''

        # You can continue to fetch other stats as needed
        tuple_ = (scout_time_played, pyro_time_played, sniper_time_played, soldier_time_played, spy_time_played,
                  engineer_time_played, medic_time_played, heavy_time_played, demoman_time_played)
        list1 = [(scout_time_played, "Scout", scout_kills), (pyro_time_played, "Pyro", pyro_kills), (sniper_time_played, "Sniper", sniper_kills),
                 (soldier_time_played, "Soldier", soldier_kills), (spy_time_played, "Spy", spy_kills), (demoman_time_played, "Demoman", demoman_kills),
                 (engineer_time_played, "Engineer", engineer_kills), (medic_time_played, "Medic", medic_kills), (heavy_time_played, "Heavy", heavy_kills)]
        killvmaim = (scout_kills, pyro_kills, soldier_kills, demoman_kills, heavy_kills, engineer_kills, medic_kills, sniper_kills, spy_kills)
        kvm=sorted(killvmaim, reverse=True)
        sorted_ = tuple(sorted(tuple_))  
        # print('Sorted Tuple :', sorted_)
        a = sorted(tuple_, reverse=True)
        # print(a)
        er = sorted(list1, reverse=True)
        # print(kvm)
        # print(er)
        # print(er[0][1])
        # print(type(a))
        # print(a[0])
        '''zaza = a.index(pyro_time_played)
        print('scout: ' + str(a.index(scout_time_played)))
        print('sniper: ' + str(a.index(sniper_time_played)))
        print('pyro: ' + str(zaza))
        print('soldier: ' + str(a.index(soldier_time_played)))
        print('engineer: ' + str(a.index(engineer_time_played)))'''
        bb = int(a[0])
        b = bb / bb
        c = int(a[1]) / int(a[0])
        d = int(a[2]) / int(a[0])
        e = int(a[3]) / int(a[0])
        fff = int(a[4]) / int(a[0])
        g = int(a[5]) / int(a[0])
        h = int(a[6]) / int(a[0])
        iii = int(a[7]) / int(a[0])
        jjj = int(a[8]) / int(a[0])
        # print(b, c, d, e, fff, g, h, iii, jjj)
        bibi = int(kvm[0])
        asa = 1 - (er[0][2] / bibi)
        sds = 1 - (er[1][2] / bibi)
        dfd = 1 - (er[2][2] / bibi)
        fgf = 1 - (er[3][2] / bibi)
        ghg = 1 - (er[4][2] / bibi)
        hjh = 1 - (er[5][2] / bibi)
        jkj = 1 - (er[6][2] / bibi)
        klk = 1 - (er[7][2] / bibi)
        lml = 1 - (er[8][2] / bibi)
        # print(asa, sds, dfd, fgf, ghg, hjh, jkj, klk, lml)
        # Print the stats or use them as needed
        qrt = timegood(a[0])
        wrt = timegood(a[1])
        ert = timegood(a[2])
        rrt = timegood(a[3])
        trt = timegood(a[4])
        yrt = timegood(a[5])
        urt = timegood(a[6])
        irt = timegood(a[7])
        ort = timegood(a[8])
        # print("Scout Kills:", scout_kills)
        print("Scout Damage:", scout_damage)
        print("Scout Captures:", scout_deaths)
        # print("Scout Time Played:", scout_time_played)
        # print("Pyro Kills:", pyro_kills)
        print("Pyro Damage:", pyro_damage)
        print("Pyro Captures:", pyro_deaths)
        # print("Pyro Time Played:", pyro_time_played)
        # print("Sniper Kills:", sniper_kills)
        print("Sniper Damage:", sniper_damage)
        print("Sniper Captures:", sniper_deaths)
        # print("Sniper Time Played:", sniper_time_played)
        # print("Soldier Kills:", soldier_kills)
        print("Soldier Damage:", soldier_damage)
        print("Soldier Captures:", soldier_deaths)
        # print("Soldier Time Played:", soldier_time_played)
        # print("Spy Kills:", spy_kills)
        print("Spy Damage:", spy_damage)
        print("Spy Captures:", spy_deaths)
        # print("Spy Time Played:", spy_time_played)
        # print("Engineer Kills:", engineer_kills)
        print("Engineer Damage:", engineer_damage)
        print("Engineer Captures:", engineer_deaths)
        # print("Engineer Time Played:", engineer_time_played)
        # print("Medic Kills:", medic_kills)
        # print("Heavy Kills:", heavy_kills)
        # print("Demoman Kills:", demoman_kills)
        with open('scoutkillsint.txt', 'w') as f:
            f.write(str(scout_kills))
        with open('0rt.txt', 'w') as f:
            f.write(str(qrt))
        with open('1rt.txt', 'w') as f:
            f.write(str(wrt))
        with open('2rt.txt', 'w') as f:
            f.write(str(ert))
        with open('3rt.txt', 'w') as f:
            f.write(str(rrt))
        with open('4rt.txt', 'w') as f:
            f.write(str(trt))
        with open('5rt.txt', 'w') as f:
            f.write(str(yrt))
        with open('6rt.txt', 'w') as f:
            f.write(str(urt))
        with open('7rt.txt', 'w') as f:
            f.write(str(irt))
        with open('8rt.txt', 'w') as f:
            f.write(str(ort))
        with open('0tf.txt', 'w') as f:
            f.write(str(b))
        with open('1tf.txt', 'w') as f:
            f.write(str(c))
        with open('2tf.txt', 'w') as f:
            f.write(str(d))
        with open('3tf.txt', 'w') as f:
            f.write(str(e))
        with open('4tf.txt', 'w') as f:
            f.write(str(fff))
        with open('5tf.txt', 'w') as f:
            f.write(str(g))
        with open('6tf.txt', 'w') as f:
            f.write(str(h))
        with open('7tf.txt', 'w') as f:
            f.write(str(iii))
        with open('8tf.txt', 'w') as f:
            f.write(str(jjj))
        with open('namerank0.txt', 'w') as f:
            f.write(str(er[0][1]))
        with open('namerank1.txt', 'w') as f:
            f.write(str(er[1][1]))
        with open('namerank2.txt', 'w') as f:
            f.write(str(er[2][1]))
        with open('namerank3.txt', 'w') as f:
            f.write(str(er[3][1]))
        with open('namerank4.txt', 'w') as f:
            f.write(str(er[4][1]))
        with open('namerank5.txt', 'w') as f:
            f.write(str(er[5][1]))
        with open('namerank6.txt', 'w') as f:
            f.write(str(er[6][1]))
        with open('namerank7.txt', 'w') as f:
            f.write(str(er[7][1]))
        with open('namerank8.txt', 'w') as f:
            f.write(str(er[8][1]))
        with open('kills0.txt', 'w') as f:
            f.write(str(er[0][2]))
        with open('kills1.txt', 'w') as f:
            f.write(str(er[1][2]))
        with open('kills2.txt', 'w') as f:
            f.write(str(er[2][2]))
        with open('kills3.txt', 'w') as f:
            f.write(str(er[3][2]))
        with open('kills4.txt', 'w') as f:
            f.write(str(er[4][2]))
        with open('kills5.txt', 'w') as f:
            f.write(str(er[5][2]))
        with open('kills6.txt', 'w') as f:
            f.write(str(er[6][2]))
        with open('kills7.txt', 'w') as f:
            f.write(str(er[7][2]))
        with open('kills8.txt', 'w') as f:
            f.write(str(er[8][2]))
        with open('0kf.txt', 'w') as f:
            f.write(str(asa))
        with open('1kf.txt', 'w') as f:
            f.write(str(sds))
        with open('2kf.txt', 'w') as f:
            f.write(str(dfd))
        with open('3kf.txt', 'w') as f:
            f.write(str(fgf))
        with open('4kf.txt', 'w') as f:
            f.write(str(ghg))
        with open('5kf.txt', 'w') as f:
            f.write(str(hjh))
        with open('6kf.txt', 'w') as f:
            f.write(str(jkj))
        with open('7kf.txt', 'w') as f:
            f.write(str(klk))
        with open('8kf.txt', 'w') as f:
            f.write(str(lml))


# Call the main function to fetch and display the stats
fetch_tf2_stats()
