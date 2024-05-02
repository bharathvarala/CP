
#can be calculated in 2 ways
# 1. Little fermats theorem
# 2. Extended Euclid Theorem

#1 states that a^(m-1) ~= 1(mod m) if m is prime and (a,m) are co prime
# a^(m-2) ~= a^-1(mod p)

a = 5
m = 7
def power(a,m,mod):
    ans = 1
    while m:
        if m&1:
            ans = (ans%mod * a%mod)%mod
            m-=1
        else:
            a = (a%mod * a%mod)%mod
            m//=2
    return ans
print(power(a,m-2,m))
