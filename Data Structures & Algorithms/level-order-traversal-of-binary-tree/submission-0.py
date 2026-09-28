# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        st = deque([root])
        res = []

        if not root:
            return []
        
        while st:
            level = []
            for _ in range(len(st)):
                curr = st.popleft()
                if curr:
                    level.append(curr.val)
                    st.append(curr.left)
                    st.append(curr.right)
            if level:
                res.append(level)
        return res