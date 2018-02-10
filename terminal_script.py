#! usr/env/bin python3

import subprocess

problems = 3
searches = {1: 'BFS', 2: 'BFTS', 3: 'DFGS', 4: 'DLS', 5: 'UCS', 6: 'RBFSH1', 7: 'GBFGSH1', 8: 'A*H1'}
# 1. breadth_first_search 
# 2. breadth_first_tree_search 
# 3. depth_first_graph_search 
# 4. depth_limited_search 
# 5. uniform_cost_search 
# 6. recursive_best_first_search h_1
# 7. greedy_best_first_graph_search h_1
# 8. astar_search h_1
# 9. astar_search h_ignore_preconditions
# 10. astar_search h_pg_levelsum

times = 5
all_values = "'Expansion', 'Goal Tests', 'New Nodes', 'Plan Length', 'Time Elapsed (s)'\n"

for problem in range(problems):
    p = str(problem+1)
    print("Problem {}".format(p))
    for search in searches.keys():
        for _ in range(times):
            s= str(search)
            print("{}".format(searches[search]))
            returned_values = subprocess.check_output(['python','run_search.py','-p',p,'-s',s]).decode('utf-8')
            _list = returned_values.split('\n')

            stat_value = _list[4].split()

            stat_perf = _list[6].split()
            stat_perf = [stat_perf[2]] + [stat_perf[-1]]

            stats = stat_value + stat_perf
        
            search_values = ""

            for stat in stats:
                search_values += "'" + stat + "',"
                
            search_values = search_values[:-1] + "\n"
            all_values += search_values

with open('search_results.csv', 'w') as f:
   f.write(all_values)

