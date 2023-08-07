def two_sum(nums, target)
  a = {}
  nums.each_with_index do |num, i|
    return [i, a[num]] if a.key?(num)
    a[target - num] = i
  end
end