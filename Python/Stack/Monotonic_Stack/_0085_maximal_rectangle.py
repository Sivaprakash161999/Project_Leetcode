class Solution:
    # Matrix - Monotonic Stack - O(R*C) time; O(C) space
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            n = len(heights)
            stack = []
            maxArea = 0
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height*(i-index))
                    start = index
                stack.append((start, h))
            
            for i, h in stack:
                maxArea = max(maxArea, h*(len(heights) - i))
            return maxArea
        # def maximumRectangleFromHistogram(histogram):
        #     mx_rectangle = 0 # to keep track of local maximum rectangle in current histogram
        #     # if current columns to be fully present in the result rectangle,
        #     # find the left an right margin until we can include in the rectangel;
        #     # simply find the left and right index where the value is less than 
        #     # the current columns value
        #     # to keep track of left and right limit for each column
        #     left = [0] * COLS
        #     right = [0] * COLS
        #     # we will maintain a monotonic increasing stack to
        #     # find the left and right limits effectively
        #     stack = [] # will hold the indices
        #     # finding left limits, traverse forward
        #     for i in range(COLS):
        #         # pop all the elements which are greater than or equal to the current
        #         # element, to maintain monotonic increasing property
        #         while stack and histogram[stack[-1]] >= histogram[i]:
        #             stack.pop()
        #         if not stack: # if the stack is empty
        #             left[i] = 0 # the left limit should be 0
        #         else:
        #             # left limit should be 1 more than the last index in stack
        #             # because, the element at the last index is less than the current element
        #             left[i] = stack[-1] + 1
        #         stack.append(i) # add the current element index in stack

        #     stack = [] # empty the stack before calculating right limits
        #     # finding the right limits and calculating area of mx_rectangle simultaneously
        #     # traverse in reverse
        #     for i in range(COLS - 1, -1, -1):
        #         while stack and histogram[stack[-1]] >= histogram[i]:
        #             stack.pop()
        #         if not stack:
        #             right[i] = COLS - 1 # the right limit should be COLS
        #         else:
        #             # right limit should be 1 less than the last index in stack
        #             # because, the element at the last index is less than the current element
        #             right[i] = stack[-1] - 1
        #         stack.append(i) # add the current element index in stack
        #         # calculate the area = width * height
        #         width = right[i] - left[i] + 1
        #         height = histogram[i]
        #         mx_rectangle = max(mx_rectangle, width * height)
        #     # print(histogram, left, right, width, height, mx_rectangle)
        #     return mx_rectangle


        ROWS, COLS = len(matrix), len(matrix[0])
        max_rectangle = 0 # variable to keep track of our result
        # keeps track of the accumulated histogram upto the current row
        histogram = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "0":
                    histogram[c] = 0
                else:
                    histogram[c] += int(matrix[r][c])
            # print(histogram)
            # calculate the max rectangle for the current 
            # histogram, and update the result if it is larger
            # max_rectangle = max(max_rectangle, maximumRectangleFromHistogram(histogram))
            max_rectangle = max(max_rectangle, largestRectangleArea(histogram))
        return max_rectangle
            
        