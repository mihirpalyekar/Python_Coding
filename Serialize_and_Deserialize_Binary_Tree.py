class Codec:

    def serialize(self, root):
        if not root:
            return ""

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
        

    def deserialize(self, data):
        if not data:
            return None

        return self.deserialize_list(data.split(","))
        
    def deserialize_list(self, nums: List[str]):
        val = nums.pop(0)
        if not val:
            return None

        root = TreeNode(val)
        root.left = self.deserialize_list(nums)
        root.right = self.deserialize_list(nums)

        return root
