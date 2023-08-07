Given an array of integers and targets.return indexes of two number such that sum of those two numbers will be equal to target.


Example1
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example2:
  Input: nums = [3,2,4], target = 6
  Output: [1,2]

Solution Idea:
  build a hash map of elemets which are required to make the sum to target(i.e, target-encountered ) as a key and its index as its value which will easier to check weather it is present or not in liner time and acess it.
  when we encounter a already existing key we return the necessary data. 