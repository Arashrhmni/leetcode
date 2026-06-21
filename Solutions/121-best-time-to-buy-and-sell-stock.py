# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10**5
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            current_profit = price - min_price

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit