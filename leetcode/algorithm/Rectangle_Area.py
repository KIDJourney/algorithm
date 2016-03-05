class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        total = (C - A) * (D - B) + (G - E) * (H - F)

        width = max(0, min(C, G) - max(A, E))
        height = max(0, min(D, H) - max(B, F))

        return total - width * height