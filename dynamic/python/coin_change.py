
def coin(goal, cursum, coins):
	if len(coins) == 0:
		return 0
	if cursum > goal:
		return 0
	if cursum == goal:
		return 1
	return coin(goal, cursum+coins[0], coins) + coin(goal, cursum, coins[1:])


print coin(100,0,[25,10,5,1])
