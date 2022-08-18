package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	queue := []*TreeNode{root}
	flag := true
	ans := [][]int{}
	if root == nil {
		return ans
	}

	for len(queue) != 0 {
		newqueue := []*TreeNode{}
		tmpAns := []int{}
		if flag {
			for i := 0; i < len(queue); i++ {
				tmpAns = append(tmpAns, queue[i].Val)
			}
		} else {
			for i := len(queue) - 1; i >= 0; i-- {
				tmpAns = append(tmpAns, queue[i].Val)
			}
		}

		for i := 0; i < len(queue); i++ {
			n := queue[i]
			if n.Left != nil {
				newqueue = append(newqueue, queue[i].Left)
			}
			if n.Right != nil {
				newqueue = append(newqueue, queue[i].Right)
			}
		}
		ans = append(ans, tmpAns)
		queue = newqueue
		flag = !flag
	}
	return ans
}
