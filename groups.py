import hashlib

salt = 'final_ab'
group_percent = 50


def get_exp_group(user_id: int) -> str:
    value_str = str(user_id) + salt
    value_num = int(hashlib.md5(value_str.encode()).hexdigest(), base=16)
    if value_num % 100 <= group_percent:
        return 'control'
    return 'test'
