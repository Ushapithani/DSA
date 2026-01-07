def is_palindrome(n: int) -> bool:
    def reverse(x: int, rev: int = 0) -> int:
        if x == 0:
            return rev
        return reverse(x // 10, rev * 10 + x % 10)
    
    if n < 0:
        return False
    return n == reverse(n)