def generate_parentheses(n: int) -> list:

    def recursion(left, right, current, result_list):
        # import pdb; pdb.set_trace()
        if left == n and right == n or right > left:
            result_list.append(current)
            return current
        elif left == n:
            recursion(left, right + 1, current + ')', result_list)
        else:
            recursion(left + 1, right, current + '(', result_list)
            recursion(left, right + 1, current + ')', result_list)
        return result_list
    if n == 0:
        return []
    results = recursion(1, 0, '(', [])
    final_result = [item for item in results if len(item) == n*2]
    return final_result

print(generate_parentheses(4))