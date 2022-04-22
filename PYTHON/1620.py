import sys

n, m = map(int, sys.stdin.readline().strip().split())

pokemonList = list()
sortedPokemonList = list()

for i in range(n): # 포켓몬들을 입력받음
    pokemonList.append(sys.stdin.readline().strip())
pokemonDict = {}

for i, v in enumerate(pokemonList):
    pokemonDict[v] = i


targetPokemonList = list()
for i in range(m): # 문제들을 입력받음
    targetPokemonList.append(sys.stdin.readline().strip())

for i in range(m): # 정답 출력
    if targetPokemonList[i].isdigit():
        print(pokemonList[int(targetPokemonList[i]) - 1])
    else:
        print(pokemonDict[targetPokemonList[i]] + 1)


# 해결과정

# 1. 딕셔너리를 사용해서 해결하다가 value값으로 key값을 찾는데에 시간초과가 나서 실패
# 2. 배열을 사용해서 정렬 후 이분탐색으로 key값을 찾아낼려했지만 이분탐색을할려면 정렬을 한 뒤 해야해서 실패
# 3. 딕셔너리를 key에 배열값 value에 배열index값을 넣어서 포켓몬이름으로 인덱스값을 알아내어 시간초과 해결 