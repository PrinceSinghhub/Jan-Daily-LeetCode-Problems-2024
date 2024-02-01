class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        queue = [(root, None)]
        mapping = {}
        while (queue):
            curr, parent = queue.pop()
            touches = []
            if (curr.left):
                touches.append(curr.left.val)
                queue.append((curr.left, curr))
            if (curr.right):
                touches.append(curr.right.val)
                queue.append((curr.right, curr))
            if (parent):
                touches.append(parent.val)
            mapping[curr.val] = touches

        time = 0
        current_wave = [start]
        next_wave = []
        seen = set()
        seen.add(start)

        while (current_wave):
            node_id = current_wave.pop()
            for touch in mapping[node_id]:
                if touch not in seen:
                    next_wave.append(touch)
                    seen.add(touch)

            if (len(current_wave) == 0):
                if (len(next_wave) == 0):
                    return time
                else:
                    time += 1
                    current_wave = next_wave
                    next_wave = []

        return 0