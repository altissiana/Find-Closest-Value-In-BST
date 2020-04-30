#average: O(log(n)) time | O(1) space
#worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
	current_node = tree
	while current_node is not None:
		if abs(target - closest) > abs(target - current_node.value):
			closest = current_node.value
		if target < current_node.value:
			current_node = current_node.left
		elif target > current_node.value:
			current_node = current_node.right	
		else:
			break
	return closest	


#average: O(log(n)) time | O(Log(n)) space
#worst: O(n) time | O(n) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
	    return closest
	if abs(target - closest) > abs (target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest

