from collections import defaultdict


class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        seen = set()

        for i in range(len(paths)):
            seen.add(paths[i][0])

        for i in range(len(paths)):
            if paths[i][1] not in seen:
                return paths[i][1]

        return ''

# 1436. Destination City
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
#
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
