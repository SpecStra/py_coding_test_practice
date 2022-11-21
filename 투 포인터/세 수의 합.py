# 배열을 입력받아 합으로 0을 만들 수 있는 원소 3개의 조합을 출력

def solution(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # 포인터 세팅
        left, right = i+1, len(nums)-1
        while left < right :
            print(left, right)
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0 :
                right -= 1
            else :
                # sum == 0
                results.append([nums[i], nums[left], nums[right]])

                # 동일한 값이 있을 경우 넘겨버리기
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    print(results)
    return results


a = [-4, -1, -1, 0, 1, 2]
solution(a)